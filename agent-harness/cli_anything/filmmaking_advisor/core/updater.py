"""Universal Multi-Agent Skill Installer, Terminal Update Checker & Self-Updater (hmfa).

Safety Guarantees:
- NEVER modifies Hermes config.yaml, provider, model (Main Agent, Sub-Agent, MoA), SOUL.md, or API keys.
- Preserves user's curiosity_ledger/ across updates.
- Supports Git fast-forward updates AND Git-less HTTPS archive updates from GitHub.
"""

from __future__ import annotations

import json
import os
import platform
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from cli_anything.filmmaking_advisor.core.discovery import (
    discover_hermes_installations,
    discover_other_agents,
)

DEFAULT_GITHUB_OWNER = "zidanaisar624"
DEFAULT_GITHUB_REPO = "hermes-mfa-filmmaking-and-agent-skills"
DEFAULT_BRANCH = "main"
INSTALL_STATE_DIR_NAME = "hermes-filmmaking-cli"


def get_repo_root() -> Path:
    """Resolve repository root relative to this module."""
    return Path(__file__).resolve().parents[4]


def get_local_version_info(repo_root: Optional[Path] = None) -> Dict[str, object]:
    root = repo_root or get_repo_root()
    version_file = root / "VERSION"
    version = version_file.read_text(encoding="utf-8").strip() if version_file.is_file() else "1.0.0"

    commit_sha = None
    commit_date = None
    branch = DEFAULT_BRANCH
    is_git = (root / ".git").exists()

    if is_git and shutil.which("git"):
        try:
            sha_p = subprocess.run(
                ["git", "-C", str(root), "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
            if sha_p.returncode == 0:
                commit_sha = sha_p.stdout.strip()
            date_p = subprocess.run(
                ["git", "-C", str(root), "log", "-1", "--format=%ci"],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
            if date_p.returncode == 0:
                commit_date = date_p.stdout.strip()
            br_p = subprocess.run(
                ["git", "-C", str(root), "rev-parse", "--abbrev-ref", "HEAD"],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
            if br_p.returncode == 0 and br_p.stdout.strip():
                branch = br_p.stdout.strip()
        except Exception:
            pass

    meta_file = root / ".hmfa_install_meta.json"
    if not commit_sha and meta_file.is_file():
        try:
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
            commit_sha = meta.get("commit_sha")
            commit_date = meta.get("commit_date")
        except Exception:
            pass

    return {
        "repo_root": str(root),
        "version": version,
        "commit_sha": commit_sha,
        "commit_short": commit_sha[:7] if commit_sha else "unknown",
        "commit_date": commit_date,
        "branch": branch,
        "is_git_checkout": is_git,
    }


def _http_get_json(url: str, timeout: int = 8) -> Optional[dict]:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "hermes-filmmaking-cli/2.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except Exception:
        return None


def _http_get_text(url: str, timeout: int = 8) -> Optional[str]:
    req = urllib.request.Request(url, headers={"User-Agent": "hermes-filmmaking-cli/2.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace").strip()
    except Exception:
        return None


def check_remote_update(
    repo_root: Optional[Path] = None,
    owner: str = DEFAULT_GITHUB_OWNER,
    repo: str = DEFAULT_GITHUB_REPO,
    branch: str = DEFAULT_BRANCH,
) -> Dict[str, object]:
    """Compare local version & commit SHA against GitHub remote without leaving the terminal."""
    local = get_local_version_info(repo_root)
    remote_sha: Optional[str] = None
    remote_date: Optional[str] = None
    remote_message: Optional[str] = None

    # 1. Try git ls-remote first (fast, no API rate limit)
    if shutil.which("git"):
        try:
            repo_url = f"https://github.com/{owner}/{repo}.git"
            p = subprocess.run(
                ["git", "ls-remote", repo_url, f"refs/heads/{branch}"],
                capture_output=True,
                text=True,
                timeout=8,
                check=False,
            )
            if p.returncode == 0 and p.stdout.strip():
                remote_sha = p.stdout.strip().split()[0]
        except Exception:
            pass

    # 2. Enrich or fallback via GitHub Commits API
    commit_json = _http_get_json(f"https://api.github.com/repos/{owner}/{repo}/commits/{branch}")
    if isinstance(commit_json, dict) and commit_json.get("sha"):
        remote_sha = remote_sha or str(commit_json["sha"])
        commit_obj = commit_json.get("commit", {})
        remote_message = (commit_obj.get("message") or "").splitlines()[0] if commit_obj else None
        remote_date = commit_obj.get("committer", {}).get("date") if commit_obj else None

    remote_version = _http_get_text(
        f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/VERSION"
    )

    if not remote_sha and not remote_version:
        return {
            "ok": False,
            "error": "Could not reach GitHub to check updates. Check internet connection.",
            "local": local,
        }

    local_sha = local.get("commit_sha")
    local_ahead = False
    if local_sha and remote_sha:
        if str(local_sha).lower() == str(remote_sha).lower():
            update_available = False
        else:
            update_available = True
            root = repo_root or get_repo_root()
            if (root / ".git").exists() and shutil.which("git"):
                try:
                    anc_p = subprocess.run(
                        ["git", "-C", str(root), "merge-base", "--is-ancestor", str(remote_sha), str(local_sha)],
                        capture_output=True,
                        timeout=4,
                        check=False,
                    )
                    if anc_p.returncode == 0:
                        update_available = False
                        local_ahead = True
                except Exception:
                    pass
    elif remote_version:
        update_available = str(local.get("version")) != str(remote_version)
    else:
        update_available = False

    return {
        "ok": True,
        "repository": f"{owner}/{repo}",
        "branch": branch,
        "update_available": update_available,
        "local_ahead_of_remote": local_ahead,
        "status": "UPDATE_AVAILABLE" if update_available else ("LOCAL_AHEAD" if local_ahead else "UP_TO_DATE"),
        "local": local,
        "remote": {
            "version": remote_version or "unknown",
            "commit_sha": remote_sha,
            "commit_short": remote_sha[:7] if remote_sha else "unknown",
            "commit_date": remote_date,
            "latest_commit_title": remote_message,
        },
        "command_to_update": "hmfa update",
    }


def _copy_or_link_skill(src_skill: Path, dst_skill: Path, prefer_link: bool = True) -> str:
    """Link or copy ``src_skill`` to ``dst_skill`` safely (Windows Junction -> Symlink -> Copy fallback)."""
    try:
        if src_skill.resolve() == dst_skill.resolve():
            return "same_source_skipped"
    except OSError:
        pass

    dst_skill.parent.mkdir(parents=True, exist_ok=True)
    marker_name = ".hmfa-managed"

    # Remove previous skill link/copy safely; if an unrelated user folder exists, back it up first!
    if dst_skill.is_symlink():
        dst_skill.unlink()
    elif dst_skill.exists():
        is_managed = (dst_skill / marker_name).is_file()
        is_junction_to_us = False
        try:
            if dst_skill.resolve() == src_skill.resolve():
                return "same_source_skipped"
            if get_repo_root() in dst_skill.resolve().parents:
                is_junction_to_us = True
        except OSError:
            pass

        if is_junction_to_us and platform.system() == "Windows":
            try:
                os.rmdir(dst_skill)
            except OSError:
                shutil.rmtree(dst_skill)
        elif is_managed:
            shutil.rmtree(dst_skill)
        else:
            backup_dst = dst_skill.with_name(f"{dst_skill.name}.bak-pre-hmfa-{int(time.time())}")
            shutil.move(str(dst_skill), str(backup_dst))

    if prefer_link:
        try:
            dst_skill.symlink_to(src_skill, target_is_directory=True)
            return "symlinked"
        except OSError:
            if platform.system() == "Windows":
                try:
                    import _winapi  # type: ignore

                    _winapi.CreateJunction(str(src_skill), str(dst_skill))
                    if dst_skill.exists():
                        return "junction_linked"
                except Exception:
                    try:
                        proc = subprocess.run(
                            ["cmd", "/c", "mklink", "/J", str(dst_skill), str(src_skill)],
                            capture_output=True,
                            text=True,
                            timeout=5,
                            check=False,
                        )
                        if proc.returncode == 0 and dst_skill.exists():
                            return "junction_linked"
                    except Exception:
                        pass

    shutil.copytree(
        src_skill,
        dst_skill,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
    )
    try:
        (dst_skill / ".hmfa-managed").write_text("managed-by-hermes-mfa-filmmaking-and-agent-skills\n", encoding="utf-8")
    except OSError:
        pass
    return "copied"


def _cli_bin_dir() -> Path:
    if platform.system() == "Windows":
        local_app = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
        return Path(local_app) / INSTALL_STATE_DIR_NAME / "bin"
    return Path.home() / ".local" / "bin"


def _ensure_windows_user_path(bin_dir: Path) -> bool:
    """Add ``bin_dir`` to Windows HKCU\\Environment\\Path non-destructively if missing."""
    if platform.system() != "Windows":
        return False
    try:
        import winreg  # type: ignore

        target_str = str(bin_dir)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_READ | winreg.KEY_WRITE) as key:
            try:
                current_path, reg_type = winreg.QueryValueEx(key, "Path")
            except FileNotFoundError:
                current_path, reg_type = "", winreg.REG_EXPAND_SZ
            parts = [p.strip() for p in str(current_path).split(";") if p.strip()]
            norm_parts = {os.path.normcase(os.path.expandvars(p).rstrip("\\/")) for p in parts}
            if os.path.normcase(target_str.rstrip("\\/")) not in norm_parts:
                new_path = ";".join(parts + [target_str])
                winreg.SetValueEx(key, "Path", 0, reg_type, new_path)
                return True
    except Exception:
        return False
    return False


def install_terminal_launchers(repo_root: Path, hermes_roots: List[Path]) -> Dict[str, object]:
    """Install `hmfa`, `hermes-filmmaking`, and `cli-anything-filmmaking` launchers for CMD, PowerShell & Bash."""
    bin_dir = _cli_bin_dir()
    bin_dir.mkdir(parents=True, exist_ok=True)

    harness_dir = repo_root / "agent-harness"
    py_exe = shutil.which("python") or shutil.which("python3") or "python"

    cmd_dirs = [bin_dir] + [hr / "bin" for hr in hermes_roots if hr.is_dir()]
    written: List[str] = []

    for target_bin in cmd_dirs:
        try:
            target_bin.mkdir(parents=True, exist_ok=True)
            for cmd_name in ("hmfa", "hermes-filmmaking", "cli-anything-filmmaking"):
                if platform.system() == "Windows":
                    cmd_file = target_bin / f"{cmd_name}.cmd"
                    cmd_content = (
                        "@echo off\r\n"
                        "setlocal\r\n"
                        f'set "HMFA_REPO={repo_root}"\r\n'
                        f'set "PYTHONPATH={harness_dir};%PYTHONPATH%"\r\n'
                        "where python >nul 2>nul\r\n"
                        "if %ERRORLEVEL% EQU 0 (\r\n"
                        '    python -m cli_anything.filmmaking_advisor %*\r\n'
                        "    exit /b %ERRORLEVEL%\r\n"
                        ")\r\n"
                        "where py >nul 2>nul\r\n"
                        "if %ERRORLEVEL% EQU 0 (\r\n"
                        '    py -3 -m cli_anything.filmmaking_advisor %*\r\n'
                        "    exit /b %ERRORLEVEL%\r\n"
                        ")\r\n"
                        f'powershell -NoProfile -ExecutionPolicy Bypass -File "{repo_root / "update.ps1"}" %*\r\n'
                    )
                    cmd_file.write_text(cmd_content, encoding="utf-8")
                    written.append(str(cmd_file))

                sh_file = target_bin / cmd_name
                sh_content = (
                    "#!/usr/bin/env sh\n"
                    f'export HMFA_REPO="{repo_root.as_posix()}"\n'
                    f'export PYTHONPATH="{harness_dir.as_posix()}${{PYTHONPATH:+:$PYTHONPATH}}"\n'
                    "if command -v python3 >/dev/null 2>&1; then\n"
                    '  exec python3 -m cli_anything.filmmaking_advisor "$@"\n'
                    "elif command -v python >/dev/null 2>&1; then\n"
                    '  exec python -m cli_anything.filmmaking_advisor "$@"\n'
                    "else\n"
                    f'  exec sh "{(repo_root / "update.sh").as_posix()}" "$@"\n'
                    "fi\n"
                )
                sh_file.write_text(sh_content, encoding="utf-8", newline="\n")
                try:
                    sh_file.chmod(0o755)
                except OSError:
                    pass
        except OSError:
            continue

    path_added = _ensure_windows_user_path(bin_dir)
    return {
        "primary_bin_dir": str(bin_dir),
        "added_to_windows_user_path": path_added,
        "launchers_written_count": len(written),
        "commands_enabled": ["hmfa", "hermes-filmmaking", "cli-anything-filmmaking"],
    }


def install_skills_everywhere(
    repo_root: Optional[Path] = None,
    hermes_only: bool = False,
    core_only: bool = False,
    prefer_link: bool = True,
    explicit_hermes_home: Optional[str] = None,
    extra_skills_dirs: Optional[List[str]] = None,
    dry_run: bool = False,
) -> Dict[str, object]:
    """Auto-discover Hermes (#1) and all installed AI agents, then sync skills without touching model/provider."""
    root = repo_root or get_repo_root()
    skills_src = root / "skills"
    if not skills_src.is_dir():
        raise FileNotFoundError(f"Skills directory not found at {skills_src}")

    core_names = {
        "filmmaking-videography-photography-s2",
        "auto-curiousity-for-film-making",
        "cli-anything-filmmaking-bridge",
    }

    skill_dirs = sorted(
        [
            d
            for d in skills_src.iterdir()
            if d.is_dir() and (d / "SKILL.md").is_file() and (not core_only or d.name in core_names)
        ],
        key=lambda p: p.name.lower(),
    )

    hermes_list = discover_hermes_installations(deep_scan=True, explicit_home=explicit_hermes_home)
    other_agents = [] if hermes_only else [a for a in discover_other_agents() if a["detected"]]

    targets: List[Tuple[str, str, Path]] = []
    hermes_root_paths: List[Path] = []

    for h in hermes_list:
        h_root = Path(str(h["root"]))
        hermes_root_paths.append(h_root)
        targets.append(("hermes-root", f"Hermes Root ({h_root})", Path(str(h["skills_dir"]))))
        for prof in h.get("profiles", []):  # type: ignore[union-attr]
            p_path = Path(str(prof["path"]))
            # Sync into active bot profiles that maintain their own skills dir
            if (p_path / "skills").exists() or (p_path / "config.yaml").is_file():
                targets.append(
                    ("hermes-profile", f"Hermes Bot Profile [{prof['name']}]", Path(str(prof["skills_dir"])))
                )

    # If no Hermes installation exists yet on this user's machine, still support universal agents or fallback
    for ag in other_agents:
        targets.append((str(ag["agent_id"]), str(ag["label"]), Path(str(ag["skills_dir"]))))

    for extra in extra_skills_dirs or []:
        targets.append(("custom", f"Custom Skills Dir ({extra})", Path(extra).expanduser()))

    installed_summary: List[Dict[str, object]] = []
    for kind, label, dest_skills_dir in targets:
        if dry_run:
            installed_summary.append(
                {
                    "kind": kind,
                    "target": label,
                    "skills_dir": str(dest_skills_dir),
                    "skills_count": len(skill_dirs),
                    "mode": "dry_run",
                }
            )
            continue

        modes_used: Dict[str, int] = {}
        errors: List[str] = []
        for sdir in skill_dirs:
            try:
                m = _copy_or_link_skill(sdir, dest_skills_dir / sdir.name, prefer_link=prefer_link)
                modes_used[m] = modes_used.get(m, 0) + 1
            except Exception as exc:
                errors.append(f"{sdir.name}: {exc}")

        # Ensure non-destructive curiosity_ledger inside Hermes root so Eternal Student has persistent memory
        if kind == "hermes-root":
            from cli_anything.filmmaking_advisor.core.curiosity_engine import ensure_ledger

            ensure_ledger(dest_skills_dir.parent / "curiosity_ledger")

        installed_summary.append(
            {
                "kind": kind,
                "target": label,
                "skills_dir": str(dest_skills_dir),
                "skills_synced": sum(modes_used.values()),
                "methods": modes_used,
                **({"errors": errors} if errors else {}),
            }
        )

    launchers = {} if dry_run else install_terminal_launchers(root, hermes_root_paths)

    return {
        "ok": True,
        "provider_model_lock_preserved": True,
        "skills_selected_count": len(skill_dirs),
        "hermes_installations_found": len(hermes_list),
        "other_agents_found": len(other_agents),
        "targets": installed_summary,
        "terminal_cli": launchers,
    }


def self_update_from_github(
    repo_root: Optional[Path] = None,
    owner: str = DEFAULT_GITHUB_OWNER,
    repo: str = DEFAULT_GITHUB_REPO,
    branch: str = DEFAULT_BRANCH,
    force: bool = False,
    hermes_only: bool = False,
) -> Dict[str, object]:
    """Pull latest repository update via Git or HTTPS Zip and re-sync all detected agents automatically."""
    root = repo_root or get_repo_root()
    check_res = check_remote_update(root, owner=owner, repo=repo, branch=branch)
    if not check_res.get("ok"):
        return check_res

    if not check_res.get("update_available") and not force:
        sync_res = install_skills_everywhere(repo_root=root, hermes_only=hermes_only)
        return {
            "ok": True,
            "updated": False,
            "message": "Already at the latest version! Re-verified all local agent skill links.",
            "check": check_res,
            "sync": sync_res,
        }

    update_method = "none"
    if (root / ".git").exists() and shutil.which("git"):
        fetch_p = subprocess.run(
            ["git", "-C", str(root), "fetch", "origin", branch],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        pull_p = subprocess.run(
            ["git", "-C", str(root), "pull", "--ff-only", "origin", branch],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if fetch_p.returncode == 0 and pull_p.returncode == 0:
            update_method = "git_pull_ff_only"
        else:
            return {
                "ok": False,
                "error": "Git fast-forward pull stopped safely because local uncommitted edits exist.",
                "git_output": (pull_p.stderr or pull_p.stdout).strip(),
                "hint": "Commit or stash your local changes, or run `git pull --rebase`.",
            }
    else:
        # Git-less HTTPS archive download & safe overlay (preserves curiosity_ledger/)
        zip_url = f"https://codeload.github.com/{owner}/{repo}/zip/refs/heads/{branch}"
        with tempfile.TemporaryDirectory() as tmpd:
            zip_path = Path(tmpd) / "repo.zip"
            req = urllib.request.Request(zip_url, headers={"User-Agent": "hermes-filmmaking-cli/2.0"})
            with urllib.request.urlopen(req, timeout=45) as resp:
                zip_path.write_bytes(resp.read())
            extract_dir = Path(tmpd) / "extracted"
            with zipfile.ZipFile(zip_path, "r") as zf:
                zf.extractall(extract_dir)
            subdirs = [d for d in extract_dir.iterdir() if d.is_dir()]
            if not subdirs:
                return {"ok": False, "error": "Downloaded archive was empty."}
            src_extracted = subdirs[0]
            for item in src_extracted.iterdir():
                if item.name in {"curiosity_ledger", ".git"}:
                    continue
                dest_item = root / item.name
                if dest_item.is_dir():
                    shutil.rmtree(dest_item)
                elif dest_item.exists():
                    dest_item.unlink()
                if item.is_dir():
                    shutil.copytree(item, dest_item)
                else:
                    shutil.copy2(item, dest_item)
        remote_info = check_res.get("remote", {})
        if isinstance(remote_info, dict):
            (root / ".hmfa_install_meta.json").write_text(
                json.dumps(
                    {
                        "commit_sha": remote_info.get("commit_sha"),
                        "commit_date": remote_info.get("commit_date"),
                        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )
        update_method = "https_zip_archive"

    sync_res = install_skills_everywhere(repo_root=root, hermes_only=hermes_only)
    new_local = get_local_version_info(root)
    return {
        "ok": True,
        "updated": True,
        "update_method": update_method,
        "now_installed": new_local,
        "sync": sync_res,
    }


def export_chatgpt_bundle(repo_root: Optional[Path] = None, out_dir: Optional[Path] = None) -> Dict[str, object]:
    """Build ready-to-upload ChatGPT Custom GPT / ChatGPT Project files (instructions + consolidated knowledge)."""
    root = repo_root or get_repo_root()
    dest = out_dir or (root / "exports" / "chatgpt")
    dest.mkdir(parents=True, exist_ok=True)

    sys_inst_src = root / "adapters" / "chatgpt" / "CHATGPT_CUSTOM_INSTRUCTIONS.md"
    sys_inst_dst = dest / "01_PASTE_INTO_CHATGPT_INSTRUCTIONS.md"
    if sys_inst_src.is_file():
        shutil.copy2(sys_inst_src, sys_inst_dst)

    knowledge_parts: List[str] = [
        "# Consolidated Knowledge Bundle: S1-S2 Filmmaking Advisor, Eternal-Student Auto-Curiosity & Skill Synergy\n",
        "> Role: Research-based S1-S2 (BFA/MFA) Filmmaking, Cinematography & Photography Advisor (Human-in-the-Loop Co-Pilot, NOT a replacement for human filmmakers).\n\n",
    ]
    files_to_pack = [
        root / "skills" / "filmmaking-videography-photography-s2" / "SKILL.md",
        root / "skills" / "filmmaking-videography-photography-s2" / "references" / "mfa-directing-screenwriting.md",
        root / "skills" / "filmmaking-videography-photography-s2" / "references" / "mfa-cinematography-photography.md",
        root / "skills" / "filmmaking-videography-photography-s2" / "references" / "mfa-editing-color-sound-artcraft.md",
        root / "skills" / "auto-curiousity-for-film-making" / "SKILL.md",
        root / "skills" / "auto-curiousity-for-film-making" / "references" / "internet-trend-deconstruction.md",
        root / "skills" / "auto-curiousity-for-film-making" / "references" / "trend-forecasting-and-knowledge-evolution.md",
        root / "skills" / "auto-curiousity-for-film-making" / "references" / "cross-skill-synergy-mesh.md",
        root / "skills" / "cli-anything-filmmaking-bridge" / "SKILL.md",
    ]
    included = []
    for fp in files_to_pack:
        if fp.is_file():
            knowledge_parts.append(f"\n\n---\n## Source: `{fp.relative_to(root).as_posix()}`\n\n")
            knowledge_parts.append(fp.read_text(encoding="utf-8", errors="replace"))
            included.append(fp.relative_to(root).as_posix())

    kb_file = dest / "02_UPLOAD_AS_CHATGPT_KNOWLEDGE_BASE.md"
    kb_file.write_text("".join(knowledge_parts), encoding="utf-8")

    return {
        "ok": True,
        "output_dir": str(dest),
        "instructions_file": str(sys_inst_dst),
        "knowledge_base_file": str(kb_file),
        "sources_packed": included,
    }
