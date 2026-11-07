# CLI-Anything Harness: `cli-anything-filmmaking` (`hmfa`)

This directory implements a native **[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)** agent harness (`cli_anything.filmmaking_advisor`) so AI agents (**Hermes Agent**, **OpenClaw**, **Claude Code**, **ChatGPT / Codex**, **Cursor**, etc.) can execute filmmaking advisory math, creative app preflight checks, Eternal-Student curiosity ledger operations, universal agent installation, and terminal self-updates with **zero MCP token bloat**.

## Design Principles

1. **Zero MCP Schema Overhead**: Instead of loading 16+ MCP server schemas (tens of thousands of prompt tokens per turn), agents invoke `cli-anything-filmmaking --json <subcommand>` (or `hmfa --json <subcommand>`) on demand via terminal.
2. **Dual Output (`--json` + Human Readable) & Stateful REPL**: Running `cli-anything-filmmaking` without subcommands launches an interactive stateful REPL; passing `--json` emits deterministic JSON for agent consumption.
3. **Zero External Dependency Requirement**: Works out-of-the-box on pure Python 3.8+ standard library (with optional `click` enhancement if installed).
4. **Advisory Philosophy**: Provides optical/cinematography/audio engineering calculations and creative software discovery to *advise* human creators—never claiming to replace human filmmakers.

## Quick Commands

```bash
# Install editable CLI harness
pip install -e ./agent-harness

# 1. Scan all drives & memory paths for Hermes (root + profiles), OpenClaw, Claude, Codex, etc.
cli-anything-filmmaking --json discover

# 2. Preflight scan installed creative CLIs & CLI-Anything harnesses (Blender, FFmpeg, GIMP, Kdenlive, etc.)
cli-anything-filmmaking --json preflight

# 3. Deterministic cinematography & audio advisor calculations (180-deg shutter, hyperfocal, lighting, LUFS)
cli-anything-filmmaking --json optics --focal-mm 35 --f-stop 2.0 --fps 24 --platform youtube

# 4. Eternal-Student Curiosity Ledger: onboard a newly connected app, list recipes, or log a trend forecast
cli-anything-filmmaking --json curiosity onboard-app --app blender --ledger ./curiosity_ledger
cli-anything-filmmaking --json curiosity list-forecasts --ledger ./curiosity_ledger

# 5. Check for GitHub repo updates & self-update all agents from terminal
hmfa check
hmfa update
```
