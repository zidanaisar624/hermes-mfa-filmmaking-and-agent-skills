# AGENTS.md — Universal Agent Instructions & Repository Map

> Compatible with **Hermes Agent (#1 Priority)**, **OpenClaw**, **Claude Code**, **OpenAI Codex / ChatGPT**, **Cursor**, **Windsurf**, **Cline**, **Gemini CLI**, **Antigravity**, and all `agentskills.io`-compliant runtimes.

## 1. Purpose & Ethical Positioning (Advisor, NOT Replacement)

This repository provides **48 interoperable AI Agent Skills** centered around an **S1–S2 (BFA/MFA) Filmmaking, Directing, Videography & Photography Curriculum Synthesis** paired with an **Eternal-Student Auto-Curiosity & Trend Forecasting Engine**.

- **Origin**: Built by researching and synthesizing publicly available undergraduate (S1/BFA) and graduate (S2/MFA) film/photography curricula and open technical knowledge on the internet.
- **Role**: Acts strictly as a **Creative & Technical Advisor / Research Co-Pilot**—helping human creators reason through narrative structure, optical physics, lighting ratios, color science, psychoacoustic loudness, and repeatable CLI workflows. **It is NOT a replacement for human directors, cinematographers, photographers, editors, or film crews.**

## 2. Core Execution Rules for Any Agent Reading This Repo

1. **Zero-MCP Token Execution First (`CLI-Anything` + Native CLIs)**:
   - Do **not** require heavy multi-server MCP connections that bloat prompt context tokens.
   - Use [`skills/cli-anything-filmmaking-bridge/SKILL.md`](./skills/cli-anything-filmmaking-bridge/SKILL.md) and the bundled [`agent-harness/`](./agent-harness/FILMMAKING_ADVISOR.md) (`hmfa` / `cli-anything-filmmaking --json`), **HKUDS/CLI-Anything** (`cli-hub`, `cli-anything-blender`, `cli-anything-kdenlive`, `cli-anything-gimp`, `cli-anything-inkscape`, `cli-anything-audacity`, etc.), and native CLIs (`ffmpeg`, `ffprobe`, `blender --background`, `darktable-cli`, `exiftool`, or local `*-cli` binaries).
2. **Eternal-Student Behavior (`auto-curiousity-for-film-making`)**:
   - Whenever an app updates OR **a brand-new app is connected**, onboard it via `hmfa --json curiosity onboard-app --app <name>`, inspect `--help` / docs, and run a safe 2-second / 1-frame sandbox test inside `curiosity_ledger/sandbox_tests/`—never on live user project files.
   - Continuously acquire new domain knowledge and forecast upcoming 1–12 month visual trends (`curiosity_ledger/trend_forecasts.json`) using the 5-Signal Predictive Model.
3. **Universal Inter-Skill Collaboration**:
   - All 48 skills in [`skills/`](./skills/) (plus any external skills installed in the user's agent) collaborate as a unified mesh (`hmfa --json curiosity synergy`). See [`skills/auto-curiousity-for-film-making/references/cross-skill-synergy-mesh.md`](./skills/auto-curiousity-for-film-making/references/cross-skill-synergy-mesh.md).
4. **Configuration Safety Lock**:
   - Never alter a user's existing agent `config.yaml`, LLM `provider`, `model` (Main Agent, Sub-Agent, or MoA), `SOUL.md`, or credentials when installing, updating, or running skills.

## 3. Terminal Commands (`hmfa` / `hermes-filmmaking`)

- Check for updates from GitHub anytime in PowerShell, CMD, or Bash: `hmfa check`
- Pull updates & sync all agents automatically: `hmfa update`
- Inspect discovered Hermes homes, profiles & creative CLIs: `hmfa status`
