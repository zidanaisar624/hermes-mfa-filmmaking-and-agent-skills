#!/usr/bin/env python3
"""Universal Auto-Discovery Installer for Hermes (#1), OpenClaw, Claude, ChatGPT/Codex & Agents.

Usage:
    python install.py                  # Auto-discover Hermes across all drives + all agents & install
    python install.py --dry-run        # Preview discovered agent folders without modifying disk
    python install.py --hermes-only    # Install only into discovered Hermes root(s) & bot profiles
    python install.py --core-only      # Install only the 3 core filmmaking/curiosity/CLI skills
    python install.py --export-chatgpt # Also generate ready-to-upload ChatGPT Custom GPT bundle
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
HARNESS_DIR = REPO_ROOT / "agent-harness"
if str(HARNESS_DIR) not in sys.path:
    sys.path.insert(0, str(HARNESS_DIR))

from cli_anything.filmmaking_advisor.filmmaking_advisor_cli import main as cli_main  # noqa: E402
from cli_anything.filmmaking_advisor.core.updater import export_chatgpt_bundle  # noqa: E402


def main() -> int:
    args = list(sys.argv[1:])
    do_export_gpt = False
    if "--export-chatgpt" in args:
        args.remove("--export-chatgpt")
        do_export_gpt = True

    rc = cli_main(["--repo", str(REPO_ROOT), "install"] + args)
    if rc == 0 and do_export_gpt:
        bundle = export_chatgpt_bundle(REPO_ROOT)
        print(f" [OK] ChatGPT Custom GPT / Project Bundle -> {bundle['output_dir']}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
