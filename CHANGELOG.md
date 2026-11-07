# Changelog

All notable changes to **Hermes & Universal S1–S2 (BFA/MFA) Filmmaking Advisor, Eternal-Student Auto-Curiosity & 48 AI Agent Skills Suite** are documented in this file.

## [2.0.0] - 2026-11-07

### Added
- **CLI-Anything Native Compatibility (`HKUDS/CLI-Anything`)**:
  - Added new skill `skills/cli-anything-filmmaking-bridge` (`SKILL.md` + `references/cli-anything-creative-matrix.md`) for zero-MCP-token creative software control via `cli-hub`, `cli-anything-*` `--json` harnesses, and native CLIs (`ffmpeg`, `ffprobe`, `blender --background`, `darktable-cli`, `exiftool`, `magick`).
  - Added compliant `agent-harness/` (`cli_anything.filmmaking_advisor`) with `setup.py`, stateful REPL, `--json` output, optical/audio physics calculator, curiosity ledger CLI, and creative toolchain preflight scanner.
- **Universal Multi-Agent Compatibility**:
  - Full support for **Hermes Agent (#1 Priority)**, **OpenClaw**, **Claude (Claude Code, `.claude-plugin`, Projects)**, **ChatGPT (Custom GPTs, Projects, Custom Instructions & OpenAI Codex CLI)**, **Cursor (`.cursor-plugin`)**, and universal `agentskills.io` (`~/.agents/skills`) agents.
  - Added `AGENTS.md`, `.claude-plugin/marketplace.json`, `.cursor-plugin/marketplace.json`, `adapters/chatgpt/`, and `adapters/claude/`.
- **Smart Universal Disk & Memory Auto-Discovery Installer**:
  - Added `install.ps1`, `install.bat`, `install.sh`, and `install.py` that automatically locate Hermes across any drive (`C:`, `D:`, `E:`, custom partitions, WSL, AppData, `HERMES_HOME`, and multi-bot `profiles/`) plus OpenClaw, Claude, Codex, and `.agents`—without touching existing `provider` or `model` locks.
- **Terminal Auto-Check & Auto-Update CLI (`hmfa` / `hermes-filmmaking` + `update.ps1` / `update.bat` / `update.sh`)**:
  - Check for updates (`hmfa check`) and self-update (`hmfa update`) directly from PowerShell, CMD, or Bash anywhere without opening GitHub or `cd`-ing into the repository.
- **Eternal Student Auto-Curiosity & Trend Forecasting**:
  - Added dynamic **New App Onboarding Protocol** (learns every newly connected app & every app update), continuous domain knowledge expansion, and a **5-Signal Trend Forecasting Engine** (`curiosity_ledger/trend_forecasts.json`).
- **Universal Cross-Skill Collaboration Mesh**:
  - Connected all 48 bundled skills (and dynamically discovered external skills) into a unified collaboration network supporting `auto-curiousity-for-film-making` and `filmmaking-videography-photography-s2`.

### Changed
- **Ethical & Research-Based Advisory Framing**:
  - Updated repository and skill descriptions to clarify that the S1–S2 (BFA–MFA) filmmaking, videography, and photography knowledge is synthesized from open educational/internet research and acts strictly as a **Creative & Technical Advisor / Co-Pilot**—never as a replacement for human filmmakers, photographers, or film crews.
- Removed hardcoded single-user machine paths from skill workflows so every user on Windows, macOS, Linux, or WSL gets seamless out-of-the-box paths.

## [1.0.0] - 2026-11-07
- Initial release of S1–S2 Filmmaking, Auto-Curiosity, and 47 AI Agent Skills suite.
