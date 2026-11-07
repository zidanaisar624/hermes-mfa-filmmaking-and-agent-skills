"""Universal Disk & Memory Auto-Discovery Engine for Hermes Agent, OpenClaw, Claude, Codex, and CLI-Anything."""

from __future__ import annotations

import os
import platform
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

SKIP_DIRS_LOWER: Set[str] = {
    "$recycle.bin",
    "system volume information",
    "windows",
    "windowsapps",
    "wpsystem",
    "wudownloadcache",
    "program files",
    "program files (x86)",
    "programdata",
    "perflogs",
    "recovery",
    "msocache",
    "node_modules",
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".venv",
    "venv",
    "env",
    "hf-cache",
    "npm-cache",
    "pip-cache",
    "cache",
    "caches",
    "temp",
    "tmp",
    "steamlibrary",
    "xboxgames",
    "epic games",
    "onedrive",
    "googledrive",
    "library",
    "proc",
    "sys",
    "dev",
    "run",
    "snap",
}

CREATIVE_HARNESSES: List[Tuple[str, str, str]] = [
    ("cli-anything-filmmaking", "filmmaking_advisor", "S1-S2 Filmmaking Advisor, Optics, Auto-Curiosity & Self-Updater"),
    ("cli-hub", "cli-anything-hub", "CLI-Anything Hub & Matrix Manager"),
    ("cli-anything-blender", "blender", "3D Previz, Camera Optics & Lighting"),
    ("cli-anything-kdenlive", "kdenlive", "NLE Video Timeline & Editing"),
    ("cli-anything-shotcut", "shotcut", "NLE Video Assembly & Filtering"),
    ("cli-anything-gimp", "gimp", "Photo Retouching & High-CTR Thumbnails"),
    ("cli-anything-krita", "krita", "Digital Painting, Grading & Storyboards"),
    ("cli-anything-inkscape", "inkscape", "Vector Titles, HUD & Lower-Thirds"),
    ("cli-anything-audacity", "audacity", "Audio Cleanup, Stems & Dynamics"),
    ("cli-anything-obs-studio", "obs-studio", "Multi-Scene Capture & Live Production"),
    ("cli-anything-openscreen", "openscreen", "Clean Screen & UI Capture"),
    ("cli-anything-videocaptioner", "videocaptioner", "ASR Transcription & Subtitle Timing"),
    ("cli-anything-comfyui", "comfyui", "Node-Based Visual Concept Generation"),
    ("cli-anything-libreoffice", "libreoffice", "Screenplays (.docx/.pdf), Stripboards (.xlsx) & Decks (.pptx)"),
    ("cli-anything-drawio", "drawio", "Lighting Diagrams & Blocking Topologies"),
    ("cli-anything-mermaid", "mermaid", "Pipeline & Narrative Architecture Diagrams"),
]

NATIVE_CREATIVE_BINS: List[Tuple[str, str]] = [
    ("ffmpeg", "Universal Video/Audio Encoding, Filters & LUFS Metering"),
    ("ffprobe", "Deterministic Stream, Frame, Color & Loudness Inspector"),
    ("blender", "Native 3D Cinema Previz, Cycles/EEVEE & Headless Render"),
    ("yt-dlp", "Authorized Reference Video & Audio Acquisition"),
    ("darktable-cli", "Headless RAW Photography Development & LUT Grading"),
    ("rawtherapee-cli", "High-Precision RAW Demosaicing & Color Pipeline"),
    ("exiftool", "Camera Optical Metadata, ICC Profile & Lens Inspector"),
    ("magick", "ImageMagick Batch Raster Processing & Contact Sheets"),
    ("sox", "Precision Audio Signal Processing & Spectrograms"),
    ("scenedetect", "PySceneDetect Automated Cut & ASL Pacing Analyzer"),
]


def is_hermes_home(path: Path) -> bool:
    """Return True if ``path`` carries authentic Hermes Agent user/data home markers."""
    try:
        if not path.is_dir():
            return False
        config_markers = (
            (path / "config.yaml").is_file(),
            (path / "profile.yaml").is_file(),
            (path / "SOUL.md").is_file(),
            (path / "state.db").is_file(),
            (path / ".skills_prompt_snapshot.json").is_file(),
        )
        dir_markers = (
            (path / "skills").is_dir(),
            (path / "profiles").is_dir(),
            (path / "memories").is_dir(),
            (path / "hermes-agent").is_dir(),
            (path / "sessions").is_dir(),
        )
        # Either config+structure, or an explicit ~/.hermes folder with skills/config
        if any(config_markers) and any(dir_markers):
            return True
        if path.name.lower() in {".hermes", "hermesdata"} and (any(config_markers) or any(dir_markers)):
            return True
    except OSError:
        return False
    return False


def resolve_hermes_fleet_root(home: Path) -> Path:
    """If ``home`` points inside ``<root>/profiles/<bot>``, resolve up to ``<root>``."""
    try:
        lexical = Path(os.path.abspath(str(home)))
        if lexical.parent.name.lower() == "profiles" and is_hermes_home(lexical.parent.parent):
            return lexical.parent.parent
    except OSError:
        pass
    return home


def list_hermes_profiles(root: Path) -> List[Path]:
    """List active Bot Mode profiles under ``<root>/profiles/``."""
    profiles_dir = root / "profiles"
    result: List[Path] = []
    try:
        if not profiles_dir.is_dir():
            return result
        for child in sorted(profiles_dir.iterdir(), key=lambda p: p.name.lower()):
            if child.name.startswith("."):
                continue
            if is_hermes_home(child) or (child / "config.yaml").is_file() or (child / "SOUL.md").is_file():
                result.append(child)
    except OSError:
        pass
    return result


def _windows_registry_env_vars() -> Dict[str, str]:
    """Read User & Machine environment variables from Windows Registry even if current shell is stale."""
    found: Dict[str, str] = {}
    if platform.system() != "Windows":
        return found
    try:
        import winreg  # type: ignore

        targets = [
            (winreg.HKEY_CURRENT_USER, r"Environment"),
            (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"),
        ]
        for hive, subkey in targets:
            try:
                with winreg.OpenKey(hive, subkey) as key:
                    idx = 0
                    while True:
                        try:
                            name, val, _ = winreg.EnumValue(key, idx)
                            idx += 1
                            if isinstance(val, str) and ("HERMES" in name.upper() or "OPENCLAW" in name.upper()):
                                found.setdefault(name, os.path.expandvars(val))
                        except OSError:
                            break
            except OSError:
                continue
    except Exception:
        pass
    return found


def _mounted_roots() -> List[Path]:
    """Enumerate mounted drives/volumes across Windows, Linux, macOS, and WSL."""
    roots: List[Path] = []
    sys_name = platform.system()
    if sys_name == "Windows":
        for letter in "CDEFGHIJKLMNOPQRSTUVWXYZ":
            drive = Path(f"{letter}:\\")
            try:
                if drive.exists():
                    roots.append(drive)
            except OSError:
                continue
    else:
        for base in (Path("/mnt"), Path("/Volumes"), Path("/media"), Path("/run/media"), Path("/opt"), Path("/data")):
            try:
                if base.is_dir():
                    for child in sorted(base.iterdir()):
                        if child.is_dir():
                            roots.append(child)
            except OSError:
                continue
        roots.append(Path("/"))
    return roots


def _wsl_hermes_candidates() -> List[Path]:
    """On Windows, inspect active WSL distros gently if reachable without booting hung VMs."""
    candidates: List[Path] = []
    if platform.system() != "Windows":
        return candidates
    # Only probe if WSL env/distro hint exists to avoid cold-booting hypervisor unexpectedly
    wsl_probe_roots = [Path(r"\\wsl.localhost")]
    for unc_root in wsl_probe_roots:
        try:
            if not unc_root.exists():
                continue
            for distro in unc_root.iterdir():
                home_base = distro / "home"
                if home_base.is_dir():
                    for user_dir in home_base.iterdir():
                        cand = user_dir / ".hermes"
                        if is_hermes_home(cand):
                            candidates.append(cand)
        except OSError:
            continue
    return candidates


def _bounded_drive_scan(roots: List[Path], max_depth: int = 3, max_dirs_per_drive: int = 600) -> List[Path]:
    """Fast, memory-safe BFS scan across user drives to find custom Hermes installs (e.g., D:\\HermesData)."""
    discovered: List[Path] = []
    seen: Set[str] = set()

    for root in roots:
        # 1. Instant direct pattern hits first (0 traversal cost)
        instant_names = [
            "HermesData",
            "Hermes",
            ".hermes",
            "hermes-data",
            "HermesAgent",
            "AI/HermesData",
            "AI/Hermes",
        ]
        for rel in instant_names:
            cand = root / rel
            try:
                if is_hermes_home(cand):
                    norm = os.path.normcase(os.path.abspath(str(cand)))
                    if norm not in seen:
                        seen.add(norm)
                        discovered.append(cand)
            except OSError:
                continue

        # 2. Bounded BFS for nested user layouts (e.g. D:\Zidan\HermesData or E:\Workspace\HermesData)
        queue: List[Tuple[Path, int]] = [(root, 0)]
        inspected = 0
        while queue and inspected < max_dirs_per_drive:
            current, depth = queue.pop(0)
            if depth >= max_depth:
                continue
            try:
                with os.scandir(current) as it:
                    for entry in it:
                        inspected += 1
                        if inspected > max_dirs_per_drive:
                            break
                        try:
                            if not entry.is_dir(follow_symlinks=False):
                                continue
                        except OSError:
                            continue
                        name_low = entry.name.lower()
                        if name_low in SKIP_DIRS_LOWER:
                            continue
                        if entry.name.startswith(".") and name_low != ".hermes":
                            continue
                        entry_path = Path(entry.path)
                        if "hermes" in name_low and is_hermes_home(entry_path):
                            root_cand = resolve_hermes_fleet_root(entry_path)
                            norm = os.path.normcase(os.path.abspath(str(root_cand)))
                            if norm not in seen:
                                seen.add(norm)
                                discovered.append(root_cand)
                            continue
                        if depth + 1 < max_depth:
                            queue.append((entry_path, depth + 1))
            except OSError:
                continue
    return discovered


def discover_hermes_installations(deep_scan: bool = True, explicit_home: Optional[str] = None) -> List[Dict[str, object]]:
    """Find ALL Hermes installations across env vars, registry, standard paths, and multi-drive partitions."""
    raw_candidates: List[Tuple[Path, str]] = []
    env_all = {**_windows_registry_env_vars(), **os.environ}

    if explicit_home:
        raw_candidates.append((Path(explicit_home).expanduser(), "cli-flag:--hermes-home"))

    if env_all.get("HERMES_HOME"):
        raw_candidates.append((Path(env_all["HERMES_HOME"]).expanduser(), "env:HERMES_HOME"))

    if env_all.get("HERMES_INSTALL_DIR"):
        inst = Path(env_all["HERMES_INSTALL_DIR"]).expanduser()
        raw_candidates.append((inst.parent, "env:HERMES_INSTALL_DIR-parent"))

    if env_all.get("HERMES_SKILLS_PATH"):
        for part in env_all["HERMES_SKILLS_PATH"].split(os.pathsep):
            part = part.strip()
            if part:
                p = Path(part).expanduser()
                raw_candidates.append((p.parent if p.name.lower() == "skills" else p, "env:HERMES_SKILLS_PATH"))

    # Check hermes binary location on PATH
    hermes_bin = shutil.which("hermes")
    if hermes_bin:
        bin_path = Path(hermes_bin).resolve()
        if bin_path.parent.name.lower() == "bin":
            raw_candidates.append((bin_path.parent.parent, "path:hermes-bin-parent"))

    home = Path.home()
    raw_candidates.append((home / ".hermes", "standard:~/.hermes"))

    if platform.system() == "Windows":
        local_app = os.environ.get("LOCALAPPDATA")
        roaming_app = os.environ.get("APPDATA")
        if local_app:
            raw_candidates.append((Path(local_app) / "hermes", "windows:LOCALAPPDATA"))
        if roaming_app:
            raw_candidates.append((Path(roaming_app) / "hermes", "windows:APPDATA"))
    else:
        xdg_data = os.environ.get("XDG_DATA_HOME", str(home / ".local" / "share"))
        raw_candidates.append((Path(xdg_data) / "hermes", "xdg:XDG_DATA_HOME"))

    if deep_scan:
        for scanned in _bounded_drive_scan(_mounted_roots()):
            raw_candidates.append((scanned, "deep-drive-scan"))
        for wsl_cand in _wsl_hermes_candidates():
            raw_candidates.append((wsl_cand, "wsl-scan"))

    verified_roots: List[Dict[str, object]] = []
    seen_norms: Set[str] = set()

    for cand, source in raw_candidates:
        try:
            fleet_root = resolve_hermes_fleet_root(cand)
            norm = os.path.normcase(os.path.abspath(str(fleet_root)))
            if norm in seen_norms:
                continue
            # Accept explicit_home even if brand new, otherwise verify Hermes home signature
            if source == "cli-flag:--hermes-home" or is_hermes_home(fleet_root):
                seen_norms.add(norm)
                profiles = list_hermes_profiles(fleet_root)
                free_mb = None
                try:
                    usage = shutil.disk_usage(fleet_root if fleet_root.exists() else fleet_root.parent)
                    free_mb = round(usage.free / (1024 * 1024), 1)
                except OSError:
                    pass
                verified_roots.append(
                    {
                        "root": str(fleet_root),
                        "skills_dir": str(fleet_root / "skills"),
                        "discovery_source": source,
                        "has_config_yaml": (fleet_root / "config.yaml").is_file(),
                        "profiles": [
                            {
                                "name": p.name,
                                "path": str(p),
                                "skills_dir": str(p / "skills"),
                            }
                            for p in profiles
                        ],
                        "free_disk_mb": free_mb,
                    }
                )
        except OSError:
            continue

    return verified_roots


def discover_other_agents() -> List[Dict[str, object]]:
    """Detect OpenClaw, Claude Code, ChatGPT/Codex CLI, Cursor, Antigravity/Gemini, and Universal ~/.agents."""
    home = Path.home()
    env = os.environ
    specs = [
        (
            "openclaw",
            "OpenClaw Agent",
            Path(env["OPENCLAW_HOME"]).expanduser() if env.get("OPENCLAW_HOME") else home / ".openclaw",
            "skills",
        ),
        (
            "claude",
            "Claude Code / Anthropic CLI",
            Path(env["CLAUDE_CONFIG_DIR"]).expanduser() if env.get("CLAUDE_CONFIG_DIR") else home / ".claude",
            "skills",
        ),
        (
            "codex",
            "OpenAI Codex / ChatGPT CLI",
            Path(env["CODEX_HOME"]).expanduser() if env.get("CODEX_HOME") else home / ".codex",
            "skills",
        ),
        (
            "agents_universal",
            "Universal AgentSkills Standard (~/.agents)",
            home / ".agents",
            "skills",
        ),
        (
            "cursor",
            "Cursor AI Editor",
            home / ".cursor",
            "skills",
        ),
    ]

    results: List[Dict[str, object]] = []
    for agent_id, label, base_dir, skills_sub in specs:
        try:
            detected = base_dir.is_dir()
            results.append(
                {
                    "agent_id": agent_id,
                    "label": label,
                    "home": str(base_dir),
                    "skills_dir": str(base_dir / skills_sub),
                    "detected": detected,
                }
            )
        except OSError:
            continue
    return results


def _find_common_windows_blender() -> Optional[str]:
    if platform.system() != "Windows":
        return None
    for drive in _mounted_roots():
        for base in (
            drive / "Program Files" / "Blender Foundation",
            drive / "Program" / "Blender Foundation",
            drive / "Blender",
        ):
            try:
                if base.is_dir():
                    exes = sorted(base.glob("Blender*/blender.exe"), reverse=True)
                    if exes:
                        return str(exes[0])
            except OSError:
                continue
    return None


def preflight_creative_toolchain() -> Dict[str, object]:
    """Scan installed CLI-Anything harnesses and native videography/photography CLI binaries (zero MCP tokens)."""
    harnesses = []
    for cmd_name, pkg_name, role in CREATIVE_HARNESSES:
        resolved = shutil.which(cmd_name)
        harnesses.append(
            {
                "command": cmd_name,
                "hub_package": pkg_name,
                "role": role,
                "installed": resolved is not None,
                "path": resolved,
                "install_hint": (
                    "pip install cli-anything-hub"
                    if cmd_name == "cli-hub"
                    else f"cli-hub install {pkg_name}"
                ),
            }
        )

    native_bins = []
    for bin_name, role in NATIVE_CREATIVE_BINS:
        resolved = shutil.which(bin_name)
        if bin_name == "blender" and not resolved:
            resolved = _find_common_windows_blender()
        native_bins.append(
            {
                "binary": bin_name,
                "role": role,
                "installed": resolved is not None,
                "path": resolved,
            }
        )

    # Auto-discover optional local creative CLI suites across drives (zero-MCP direct CLI execution)
    local_cli_suites: List[Dict[str, object]] = []
    for root in _mounted_roots():
        for rel in ("ArtCraft", "ArtCraft Apps", "Program/ArtCraft Apps", "Program Files/ArtCraft Apps"):
            cand = root / rel
            try:
                if cand.is_dir():
                    cli_exes = sorted(str(p) for p in cand.glob("*/*-cli*") if p.is_file())
                    local_cli_suites.append(
                        {
                            "suite_dir": str(cand),
                            "cli_binaries_count": len(cli_exes),
                            "cli_binaries": cli_exes,
                        }
                    )
            except OSError:
                continue

    return {
        "execution_paradigm": "CLI-Anything + Native CLI First (Zero MCP Schema Token Overhead)",
        "cli_anything_harnesses": harnesses,
        "native_creative_binaries": native_bins,
        "optional_local_suites_detected": local_cli_suites,
        "summary": {
            "harnesses_ready": sum(1 for h in harnesses if h["installed"]),
            "harnesses_total_cataloged": len(harnesses),
            "native_bins_ready": sum(1 for b in native_bins if b["installed"]),
            "native_bins_total_checked": len(native_bins),
            "local_suite_cli_bins_ready": sum(int(s["cli_binaries_count"]) for s in local_cli_suites),
        },
    }
