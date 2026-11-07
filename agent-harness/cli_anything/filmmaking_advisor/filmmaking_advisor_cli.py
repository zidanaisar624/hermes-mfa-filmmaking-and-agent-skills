"""Main CLI & Stateful REPL for `cli-anything-filmmaking` / `hmfa` / `hermes-filmmaking`.

Complies with HKUDS/CLI-Anything specifications:
- One-shot subcommands + stateful REPL default when no subcommand is given
- `--json` machine-readable output (accepted before or after subcommand)
- Zero mandatory external dependencies (pure Python 3.8+ stdlib)
"""

from __future__ import annotations

import argparse
import cmd
import json
import os
import shlex
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from cli_anything.filmmaking_advisor.core.advisor_optics import compute_optics_and_audio_advisory
from cli_anything.filmmaking_advisor.core.curiosity_engine import (
    discover_skill_synergy_mesh,
    ensure_ledger,
    list_ledger_summary,
    onboard_or_check_app,
    record_trend_forecast,
)
from cli_anything.filmmaking_advisor.core.discovery import (
    discover_hermes_installations,
    discover_other_agents,
    preflight_creative_toolchain,
)
from cli_anything.filmmaking_advisor.core.updater import (
    check_remote_update,
    export_chatgpt_bundle,
    get_local_version_info,
    get_repo_root,
    install_skills_everywhere,
    self_update_from_github,
)


def _emit(payload: Dict[str, Any], as_json: bool, human_lines: Optional[List[str]] = None) -> None:
    if as_json:
        sys.stdout.write(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
        return
    if human_lines is not None:
        for line in human_lines:
            sys.stdout.write(line + "\n")
    else:
        sys.stdout.write(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


class FilmmakingAdvisorREPL(cmd.Cmd):
    intro = (
        "====================================================================\n"
        " Hermes & Universal S1-S2 Filmmaking Advisor + Eternal Student REPL\n"
        " (CLI-Anything Compatible | Zero MCP Token Overhead)\n"
        " Type 'help' for commands, 'check' / 'update' for repo updates, or 'exit'.\n"
        "===================================================================="
    )
    prompt = "hmfa> "

    def __init__(self, repo_root: Path) -> None:
        super().__init__()
        self.repo_root = repo_root
        self.ledger_dir = repo_root / "curiosity_ledger"
        self.history_state: List[str] = []

    def do_status(self, arg: str) -> None:
        """Show local version, detected Hermes homes, and multi-agent installations."""
        main(["status"] + shlex.split(arg))
        self.history_state.append(f"status {arg}".strip())

    def do_discover(self, arg: str) -> None:
        """Scan all drives & memory paths for Hermes (root + profiles) and other AI agents."""
        main(["discover"] + shlex.split(arg))
        self.history_state.append("discover")

    def do_preflight(self, arg: str) -> None:
        """Check installed CLI-Anything harnesses and native video/photo CLIs."""
        main(["preflight"] + shlex.split(arg))
        self.history_state.append("preflight")

    def do_optics(self, arg: str) -> None:
        """Compute S1-S2 cinematography & audio targets, e.g.: optics --focal-mm 35 --f-stop 2.0 --fps 24"""
        main(["optics"] + shlex.split(arg))
        self.history_state.append(f"optics {arg}".strip())

    def do_check(self, arg: str) -> None:
        """Check GitHub for repository updates without leaving terminal."""
        main(["check"] + shlex.split(arg))
        self.history_state.append("check")

    def do_update(self, arg: str) -> None:
        """Pull latest GitHub updates and sync skills to Hermes & all agents."""
        main(["update"] + shlex.split(arg))
        self.history_state.append("update")

    def do_synergy(self, arg: str) -> None:
        """List all collaborative skills connected to Auto-Curiosity."""
        main(["curiosity", "synergy"] + shlex.split(arg))
        self.history_state.append("synergy")

    def do_history(self, _arg: str) -> None:
        """Show session command history."""
        for idx, item in enumerate(self.history_state, 1):
            print(f"  {idx}. {item}")

    def do_exit(self, _arg: str) -> bool:
        """Exit REPL."""
        return True

    def do_quit(self, _arg: str) -> bool:
        """Exit REPL."""
        return True

    def do_EOF(self, _arg: str) -> bool:
        print()
        return True


def _resolve_repo_root(explicit: Optional[str] = None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()
    env_repo = os.environ.get("HMFA_REPO")
    if env_repo and Path(env_repo).is_dir():
        return Path(env_repo).resolve()
    return get_repo_root()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hmfa",
        description=(
            "Hermes & Universal S1-S2 Filmmaking Advisor, Eternal-Student Auto-Curiosity, "
            "CLI-Anything Harness & Terminal Auto-Updater."
        ),
    )
    parser.add_argument("--json", action="store_true", help="Emit deterministic JSON output for AI agents.")
    parser.add_argument("--repo", default=None, help="Explicit repository checkout path.")

    sub = parser.add_subparsers(dest="subcommand")

    # check
    p_check = sub.add_parser("check", help="Check if a newer update is available on GitHub.")
    p_check.add_argument("--json", action="store_true", dest="sub_json")
    p_check.add_argument("--branch", default="main")

    # update
    p_upd = sub.add_parser("update", help="Download latest update from GitHub & sync to Hermes + all agents.")
    p_upd.add_argument("--json", action="store_true", dest="sub_json")
    p_upd.add_argument("--force", action="store_true", help="Force re-sync even if commit SHA matches.")
    p_upd.add_argument("--hermes-only", action="store_true", help="Update only Hermes installations.")
    p_upd.add_argument("--branch", default="main")

    # install
    p_inst = sub.add_parser("install", help="Auto-discover Hermes across all drives + other agents and install skills.")
    p_inst.add_argument("--json", action="store_true", dest="sub_json")
    p_inst.add_argument("--hermes-only", action="store_true", help="Install only to Hermes (root + bot profiles).")
    p_inst.add_argument("--core-only", action="store_true", help="Install only the 3 core filmmaking/curiosity/CLI skills.")
    p_inst.add_argument("--copy", action="store_true", help="Force full file copy instead of space-saving junctions/symlinks.")
    p_inst.add_argument("--hermes-home", default=None, help="Explicit Hermes root path override.")
    p_inst.add_argument("--skills-dir", action="append", default=[], help="Additional custom skills target folder.")
    p_inst.add_argument("--dry-run", action="store_true", help="Preview discovered targets without writing files.")

    # status / doctor
    for alias in ("status", "doctor"):
        p_st = sub.add_parser(alias, help="Inspect local version, discovered Hermes/Agent paths, and creative CLIs.")
        p_st.add_argument("--json", action="store_true", dest="sub_json")

    # discover
    p_disc = sub.add_parser("discover", help="Deep-scan drives & env for Hermes (#1) and all supported AI agents.")
    p_disc.add_argument("--json", action="store_true", dest="sub_json")
    p_disc.add_argument("--hermes-home", default=None)

    # preflight
    p_pre = sub.add_parser("preflight", help="Scan installed CLI-Anything harnesses and native video/photo CLIs.")
    p_pre.add_argument("--json", action="store_true", dest="sub_json")

    # optics
    p_opt = sub.add_parser("optics", help="Compute S1-S2 optical, shutter, lighting & LUFS audio advisory targets.")
    p_opt.add_argument("--json", action="store_true", dest="sub_json")
    p_opt.add_argument("--focal-mm", type=float, default=35.0)
    p_opt.add_argument("--f-stop", type=float, default=2.8)
    p_opt.add_argument("--fps", type=float, default=24.0)
    p_opt.add_argument("--shutter-angle", type=float, default=180.0)
    p_opt.add_argument("--sensor", default="full_frame", choices=["full_frame", "super35", "aps_c", "mft", "medium_format"])
    p_opt.add_argument("--distance-m", type=float, default=2.5)
    p_opt.add_argument("--mains-hz", type=int, default=50)
    p_opt.add_argument("--platform", default="youtube", choices=["youtube", "shorts", "cinema", "festival", "broadcast"])
    p_opt.add_argument("--lighting", default="natural_drama", choices=["high_key", "natural_drama", "low_key"])

    # curiosity
    p_cur = sub.add_parser("curiosity", help="Eternal-Student Auto-Curiosity ledger, new-app onboarding & trend prediction.")
    p_cur.add_argument("--json", action="store_true", dest="sub_json")
    p_cur.add_argument("action", choices=["init", "onboard-app", "forecast", "summary", "synergy"])
    p_cur.add_argument("--ledger", default="./curiosity_ledger", help="Path to curiosity_ledger directory.")
    p_cur.add_argument("--app", default=None, help="App binary or CLI-Anything command to onboard/check.")
    p_cur.add_argument("--category", default="creative-cli")
    p_cur.add_argument("--title", default=None, help="Trend forecast title.")
    p_cur.add_argument("--horizon", default="3-6 months")
    p_cur.add_argument("--confidence", type=float, default=0.72)
    p_cur.add_argument("--fatigue-signal", default="")
    p_cur.add_argument("--tooling-signal", default="")
    p_cur.add_argument("--advisory", default="")
    p_cur.add_argument("--falsification", default="")
    p_cur.add_argument("--skills-root", default=None)

    # export-chatgpt
    p_gpt = sub.add_parser("export-chatgpt", help="Export ready-to-upload ChatGPT Custom GPT / Project bundle.")
    p_gpt.add_argument("--json", action="store_true", dest="sub_json")
    p_gpt.add_argument("--out", default=None)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    # Ensure UTF-8 stdout on Windows terminals
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    parser = build_parser()
    args = parser.parse_args(argv)
    repo_root = _resolve_repo_root(args.repo)
    as_json = bool(getattr(args, "json", False) or getattr(args, "sub_json", False))

    if not args.subcommand:
        if as_json:
            _emit(get_local_version_info(repo_root), True)
            return 0
        FilmmakingAdvisorREPL(repo_root).cmdloop()
        return 0

    cmd_name = args.subcommand

    if cmd_name == "check":
        res = check_remote_update(repo_root, branch=args.branch)
        if not res.get("ok"):
            _emit(res, as_json, [f"[!] Update check failed: {res.get('error')}"])
            return 1
        loc = res["local"]
        rem = res["remote"]
        rem_ver_str = f"v{rem['version']}" if rem.get("version") and rem["version"] != "unknown" else "pre-v2.0"
        lines = [
            "============================================================",
            " HERMES FILMMAKING ADVISOR & SKILLS — TERMINAL UPDATE CHECK",
            "============================================================",
            f" Local Version  : v{loc['version']} ({loc['commit_short']})",
            f" Remote Version : {rem_ver_str} ({rem['commit_short']})",
            f" Latest Commit  : {rem.get('latest_commit_title') or 'N/A'}",
            f" Status         : {'UPDATE AVAILABLE! Run: hmfa update' if res['update_available'] else 'UP TO DATE (Latest)'}",
            "============================================================",
        ]
        _emit(res, as_json, lines)
        return 0

    if cmd_name == "update":
        res = self_update_from_github(
            repo_root,
            branch=args.branch,
            force=args.force,
            hermes_only=args.hermes_only,
        )
        if not res.get("ok"):
            _emit(res, as_json, [f"[!] Update error: {res.get('error')}", f"    Hint: {res.get('hint', '')}"])
            return 1
        sync_targets = res.get("sync", {}).get("targets", [])
        lines = [
            "============================================================",
            f" {'UPDATED SUCCESSFULLY!' if res.get('updated') else 'ALREADY UP TO DATE (SKILLS RE-VERIFIED)'}",
            "============================================================",
            f" Provider/Model Lock : PRESERVED (0 config.yaml changes)",
            f" Synced Agent Targets: {len(sync_targets)}",
        ]
        for t in sync_targets:
            lines.append(f"   - {t['target']} -> {t['skills_dir']} ({t.get('skills_synced', 0)} skills)")
        _emit(res, as_json, lines)
        return 0

    if cmd_name == "install":
        res = install_skills_everywhere(
            repo_root=repo_root,
            hermes_only=args.hermes_only,
            core_only=args.core_only,
            prefer_link=not args.copy,
            explicit_hermes_home=args.hermes_home,
            extra_skills_dirs=args.skills_dir,
            dry_run=args.dry_run,
        )
        lines = [
            "============================================================",
            " UNIVERSAL HERMES (#1) & MULTI-AGENT AUTO-INSTALLER",
            "============================================================",
            f" Skills Selected     : {res['skills_selected_count']}",
            f" Hermes Homes Found  : {res['hermes_installations_found']}",
            f" Other Agents Found  : {res['other_agents_found']}",
            f" Provider/Model Lock : 100% UNTOUCHED",
            "------------------------------------------------------------",
        ]
        for t in res["targets"]:
            lines.append(f" [OK] {t['target']} -> {t['skills_dir']}")
        cli_info = res.get("terminal_cli", {})
        if cli_info:
            lines.append("------------------------------------------------------------")
            lines.append(f" Terminal Commands   : hmfa check | hmfa update | hmfa status")
            lines.append(f" Launcher Bin Dir    : {cli_info.get('primary_bin_dir')}")
        _emit(res, as_json, lines)
        return 0

    if cmd_name in ("status", "doctor"):
        loc = get_local_version_info(repo_root)
        hermes_list = discover_hermes_installations(deep_scan=True)
        other_list = discover_other_agents()
        preflight = preflight_creative_toolchain()
        payload = {
            "role": "S1-S2 Filmmaking & Photography Research Advisor + Eternal Student (NOT a replacement for human filmmakers)",
            "local_repo": loc,
            "hermes_installations": hermes_list,
            "other_agents": other_list,
            "creative_cli_summary": preflight["summary"],
        }
        lines = [
            "============================================================",
            " HMFA DOCTOR — SYSTEM, HERMES & MULTI-AGENT STATUS",
            "============================================================",
            f" Repo Root      : {loc['repo_root']}",
            f" Version        : v{loc['version']} ({loc['commit_short']})",
            f" Hermes (#1)    : {len(hermes_list)} installation(s) auto-detected across drives",
        ]
        for h in hermes_list:
            prof_names = ", ".join(p["name"] for p in h["profiles"]) or "default only"
            lines.append(f"   * {h['root']} [source: {h['discovery_source']}] (profiles: {prof_names})")
        detected_others = [a for a in other_list if a["detected"]]
        lines.append(f" Other Agents   : {len(detected_others)} detected")
        for a in detected_others:
            lines.append(f"   * {a['label']} -> {a['skills_dir']}")
        s = preflight["summary"]
        lines.append(
            f" Creative CLIs  : {s['harnesses_ready']}/{s['harnesses_total_cataloged']} CLI-Anything harnesses, "
            f"{s['native_bins_ready']}/{s['native_bins_total_checked']} native bins, "
            f"{s.get('local_suite_cli_bins_ready', 0)} local suite CLIs"
        )
        lines.append("============================================================")
        _emit(payload, as_json, lines)
        return 0

    if cmd_name == "discover":
        hermes_list = discover_hermes_installations(deep_scan=True, explicit_home=args.hermes_home)
        other_list = discover_other_agents()
        payload = {"hermes": hermes_list, "other_agents": other_list}
        lines = [f"Discovered {len(hermes_list)} Hermes root(s):"]
        for h in hermes_list:
            lines.append(f"  - {h['root']} (via {h['discovery_source']}, {len(h['profiles'])} bot profiles)")
        for a in other_list:
            if a["detected"]:
                lines.append(f"  - [{a['agent_id']}] {a['skills_dir']}")
        _emit(payload, as_json, lines)
        return 0

    if cmd_name == "preflight":
        payload = preflight_creative_toolchain()
        lines = [f"Execution Mode: {payload['execution_paradigm']}", "--- CLI-Anything Harnesses ---"]
        for h in payload["cli_anything_harnesses"]:  # type: ignore[union-attr]
            mark = "READY" if h["installed"] else "missing"
            lines.append(f"  [{mark:7}] {h['command']:28} | {h['role']}")
        lines.append("--- Native Creative CLIs ---")
        for b in payload["native_creative_binaries"]:  # type: ignore[union-attr]
            mark = "READY" if b["installed"] else "missing"
            lines.append(f"  [{mark:7}] {b['binary']:28} | {b['role']}")
        _emit(payload, as_json, lines)
        return 0

    if cmd_name == "optics":
        payload = compute_optics_and_audio_advisory(
            focal_mm=args.focal_mm,
            f_stop=args.f_stop,
            fps=args.fps,
            shutter_angle_deg=args.shutter_angle,
            sensor=args.sensor,
            subject_distance_m=args.distance_m,
            ac_mains_hz=args.mains_hz,
            platform=args.platform,
            lighting_style=args.lighting,
        )
        cam = payload["camera_and_shutter"]  # type: ignore[index]
        opt = payload["optics_and_dof"]  # type: ignore[index]
        aud = payload["audio_mastering_target"]  # type: ignore[index]
        lines = [
            f"[Advisor] {payload['advisory_role']}",
            f"  Lens & DoF    : {opt['focal_length_mm']}mm f/{opt['f_stop']} @ {opt['subject_distance_m']}m -> "
            f"Hyperfocal={opt['hyperfocal_distance_m']}m, Near={opt['dof_near_limit_m']}m, Far={opt['dof_far_limit_m']}m",
            f"  Framing Note  : {opt['psychological_framing_advisory']}",
            f"  Shutter Rule  : {cam['ideal_shutter_speed']} ({cam['fps']} fps @ {cam['shutter_angle_deg']} deg)",
            f"  Audio Master  : {aud['integrated_loudness']} | Max {aud['true_peak_max']}",
        ]
        _emit(payload, as_json, lines)
        return 0

    if cmd_name == "curiosity":
        ledger_path = Path(args.ledger).expanduser()
        if args.action == "init":
            res = ensure_ledger(ledger_path)
            _emit(res, as_json, [f"Initialized Eternal-Student curiosity_ledger at {res['ledger_dir']}"])
            return 0
        if args.action == "onboard-app":
            if not args.app:
                parser.error("`curiosity onboard-app` requires `--app <binary-or-command>`")
            res = onboard_or_check_app(ledger_path, args.app, category=args.category)
            _emit(
                res,
                as_json,
                [
                    f"[Eternal Student] App: {res['app_command']} -> Status: {res['status']}",
                    f"  Binary   : {res['binary_path']}",
                    f"  Version  : {res['version_line']}",
                    f"  Next Step: {res['next_eternal_student_step']}",
                ],
            )
            return 0
        if args.action == "forecast":
            if not args.title:
                parser.error("`curiosity forecast` requires `--title <prediction-title>`")
            res = record_trend_forecast(
                ledger_dir=ledger_path,
                title=args.title,
                horizon=args.horizon,
                confidence=args.confidence,
                fatigue_signal=args.fatigue_signal,
                tooling_signal=args.tooling_signal,
                advisory_action=args.advisory,
                falsification_check=args.falsification,
            )
            _emit(res, as_json, [f"Recorded trend forecast [{res['forecast_id']}]: {res['title']} ({res['horizon']})"])
            return 0
        if args.action == "summary":
            res = list_ledger_summary(ledger_path)
            _emit(res, as_json)
            return 0
        if args.action == "synergy":
            s_root = Path(args.skills_root).expanduser() if args.skills_root else (repo_root / "skills")
            res = discover_skill_synergy_mesh(s_root)
            _emit(
                res,
                as_json,
                [
                    f"Collaborative Skill Mesh Root: {res['skills_root']}",
                    f"Total Interoperable Skills   : {res['total_collaborative_skills']}",
                ],
            )
            return 0

    if cmd_name == "export-chatgpt":
        out = Path(args.out).expanduser() if args.out else None
        res = export_chatgpt_bundle(repo_root, out)
        _emit(
            res,
            as_json,
            [
                "ChatGPT Custom GPT / Project Bundle exported:",
                f"  1. Instructions : {res['instructions_file']}",
                f"  2. Knowledge    : {res['knowledge_base_file']}",
            ],
        )
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
