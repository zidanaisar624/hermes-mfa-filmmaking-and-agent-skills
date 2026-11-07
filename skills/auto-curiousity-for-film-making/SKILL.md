---
name: auto-curiousity-for-film-making
description: Eternal-Student autonomous learning, app-onboarding, knowledge discovery, trend reverse-engineering, and trend-prediction skill for filmmaking, videography, and photography. Learns every newly connected creative app and software update via zero-token CLI-Anything sandboxes, acquires new domain research, predicts upcoming visual trends, and collaborates across all installed skills as a Creative & Technical Advisor across Hermes, OpenClaw, ChatGPT, and Claude.
version: 2.0.0
---

# Auto-Curiousity for Film Making (The Eternal Student & Trend Predictor)

Transform the AI agent into an **Eternal Student (*Pembelajar Abadi*)** of filmmaking, videography, photography, creative software, and visual culture—continuously learning whenever an app updates, whenever a brand-new app is connected, whenever new technical knowledge emerges on the internet, and forecasting where visual trends are heading next so it can better **advise** human creators.

> **Advisory Philosophy**: This skill exists to research, test safely in sandboxes, synthesize internet knowledge, and forecast trends as a **Creative & Technical Research Advisor**—never to replace human directors, cinematographers, photographers, or editors.

## Universal Agent & Zero-MCP CLI-Anything Compatibility

- **Works Across All Agents**: Native #1 support for **Hermes Agent**, plus **OpenClaw**, **Claude**, **ChatGPT / Codex**, **Cursor**, and any `agentskills.io` agent.
- **CLI-Anything Zero-Token Execution First**: Probes apps, changelogs, and sandboxes via `cli-anything-filmmaking-bridge` (`hmfa`, `cli-hub`, `cli-anything-* --json`, `ffmpeg`, `blender --background`, `darktable-cli`, or local `*-cli` binaries) without needing heavy MCP servers that consume prompt tokens.

## When to Use

- **New App Connected**: Whenever the user installs, mentions, or connects **any new creative application, CLI tool, plugin, or CLI-Anything harness** (3D, NLE video, RAW photo, color, VFX, audio, diagramming, or scriptwriting).
- **App Updated**: Whenever an existing connected tool updates its version, CLI flags, filters, nodes, shaders, or capabilities.
- **New Domain Knowledge**: When researching emerging camera/optical science, color pipelines (ACES 2.0, AgX, HDR), psychoacoustic standards, or academic/industry filmmaking techniques.
- **Trend Deconstruction & Trend Prediction**: When analyzing why a viral YouTube video, Short/Reel/TikTok, festival film, or photograph works—or **predicting upcoming 1–12 month visual, editing, color, and storytelling trends**.
- **Cross-Skill R&D**: Before or during a project in `filmmaking-videography-photography-s2`, orchestrating peer skills (`deep-research`, `autoresearch`, `data-analysis`, `firecrawl-deep-research`, `novelty-assessment`, `creative-thinking-for-research`, etc.) to generate verified **Cinematic Recipe Cards**.

## Core Architecture: The 5-Stage Eternal Student Loop

### Stage 1: Dynamic App Onboarding & Continuous Update Learning

Never treat creative software knowledge as static. Learn both **brand-new apps** and **updates to existing apps**:

1. **Trigger A — Newly Connected App Onboarding (*Tiap Tambah Aplikasi Baru*)**:
   - Fingerprint the new app immediately:
     ```bash
     hmfa --json curiosity onboard-app --app <app-name-or-path> --ledger ./curiosity_ledger
     ```
   - Check `cli-hub search <app>` (`HKUDS/CLI-Anything`) for an existing `--json` harness; if none exists and source/scripting APIs are available, collaborate with `cli-anything-filmmaking-bridge` (or `cli-anything-hermes`) to wrap it cleanly.
   - Read official CLI `--help`, scripting docs, and supported import/export formats, then run a non-destructive **"Hello Asset" Calibration Test** (1 frame, 2-second clip, or 3-second audio stem) inside `curiosity_ledger/sandbox_tests/<app>/` and register its profile in `curiosity_ledger/connected_apps_registry.json`.
2. **Trigger B — Existing App Update Diffing (*Tiap Update Aplikasi Belajar*)**:
   - Compare `--version`, `--help`, filter registries (`ffmpeg -filters`), node lists, and release notes against `curiosity_ledger/app_capabilities_snapshot.json`.
   - Test every newly added parameter in `curiosity_ledger/sandbox_tests/` using a **3-Point Parameter Sweep** (*Low 20%, Default, Extreme 95%*), recording sweet spots and artifact limits.
   - Read `references/app-update-and-artcraft-discovery.md` for full onboarding & update introspection protocols.

### Stage 2: Continuous Related Knowledge Expansion (*Belajar New Knowledge*)

Proactively expand theoretical and practical knowledge beyond training cutoffs:
1. Search open academic, engineering, and filmmaker communities (collaborating with `deep-research`, `literature-review`, `firecrawl-deep-research`, `github-research`) for new advances in optical physics, sensor readout/dynamic range, color appearance models, computational photography, neural VFX tools, and viewer retention psychology.
2. Verify claims with `backward-traceability` and `math-reasoning` / `symbolic-equation` so advisory guidance stays grounded in real physics and cited internet sources rather than rumors.

### Stage 3: 6-Layer Trend Deconstruction & 5-Signal Trend Prediction (*Sampai Memprediksi Trends*)

1. **Deconstruct Current Trends Across 6 Quantitative Layers**:
   - Extract exact numbers rather than vague adjectives (see `references/internet-trend-deconstruction.md`):
     1. *Hook & Pacing Math* (ASL in seconds, `0–3s` hook cadence, J/L-cut frame offsets).
     2. *Camera & Lens Physics* (focal length `mm`, T-stop/DoF, shutter angle, motion curve).
     3. *Lighting & Exposure Topology* (Key-to-Fill ratio, Kelvin separation, skin IRE `55–70`).
     4. *Color Science & Optical Texture* (Lift/Gamma/Gain, HSL vector shifts, halation, bloom, grain).
     5. *VFX & Motion Design* (`cubic-bezier` velocity curves, masking, 3D camera projection).
     6. *Psychoacoustic Audio* (`40–65 Hz` sub-drops, risers, foley texture, `-14 LUFS` / `-24 LKFS`).
2. **Predict Upcoming Visual & Editing Trends (`1–3m`, `3–6m`, `6–12m` Horizons)**:
   - Apply the **5-Signal Predictive Horizon Model** (read `references/trend-forecasting-and-knowledge-evolution.md`):
     - **Signal 1 — Audience Fatigue & Pendulum Counter-Trend**: Detect hyper-saturated tropes causing viewer habituation and forecast the aesthetic counter-swing.
     - **Signal 2 — Software Democratization Lag (`3–9 months`)**: High-end studio techniques that just landed as accessible CLI/open-source features (Stage 1) predict the next creator visual wave.
     - **Signal 3 — Platform Delivery & Algorithm Shifts**: Track HDR, aspect ratio, audio-track, and watch-satisfaction changes across YouTube, Shorts/Reels/TikTok, and festivals.
     - **Signal 4 — Cross-Medium Diffusion Wave**: Track aesthetics migrating from *Indie Festival Cinema / Anime / Fine-Art Photo -> Music Videos -> Flagship YouTube -> Mainstream Shorts*.
     - **Signal 5 — Quantitative Velocity & Novelty Scoring**: Collaborate with `data-analysis` and `novelty-assessment` to score confidence (`0.0–1.0`) and log explicit falsification criteria in `curiosity_ledger/trend_forecasts.json` via `hmfa curiosity forecast`.

### Stage 4: Universal Cross-Skill Synergy Mesh (*Kolaborasi Semua Skills*)

Never work in isolation—dynamically discover and collaborate with **all installed skills** (both the 48 bundled skills in this repo and any external skills in the user's agent directory):
```bash
hmfa --json curiosity synergy
```
- **Research & Web Discovery**: `deep-research`, `literature-review`, `github-research`, `firecrawl-deep-research`, `firecrawl-competitive-intel`, `firecrawl-research-papers`, `firecrawl-knowledge-base`.
- **Experimentation, Data & Forecasting**: `autoresearch`, `ai-research-explore`, `ai-research-reproduction`, `data-analysis`, `math-reasoning`, `symbolic-equation`, `academic-plotting`, `table-generation`, `notebooklm-thinking-datascience`.
- **Ideation & Novelty Filtering**: `brainstorming-research-ideas`, `creative-thinking-for-research`, `generate-fresh-ideas`, `get-more-perspectives`, `idea-generation`, `novelty-assessment`.
- **Code, App & Harness Inspection**: `cli-anything-filmmaking-bridge`, `analyze-project`, `explore-code`, `explore-run`, `evaluating-code-models`, `evaluating-llms-harness`.
- **Writing, Pitching & Human Pacing**: `filmmaking-videography-photography-s2`, `backward-traceability`, `match-my-writing-style`, `slide-generation`, `focus-my-energy`, `parenting-6d-gad-mdd`, `persona-shizuka-yukino-shikaku`.

Read `references/cross-skill-synergy-mesh.md` for complete multi-skill orchestration workflows.

### Stage 5: Recipe Synthesis & Bidirectional Advisory Handoff

Save every verified app capability, newly learned concept, deconstructed trend, and trend prediction into `curiosity_ledger/` (`tested_recipes_registry.json` and `trend_forecasts.json`), then supply tailored **Cinematic Recipe Cards** and **Early-Mover Trend Advisories** directly to `filmmaking-videography-photography-s2` (in both Single-Agent Mode A and Multi-Bot Mode B). Read `references/curiosity-sandbox-and-handoff.md`.

## Reference Modules

Read these relative markdown files inside `references/` as needed:
- `references/app-update-and-artcraft-discovery.md` — Dynamic new-app onboarding, update schema diffing, CLI-Anything probing, and 3-point sandbox testing.
- `references/internet-trend-deconstruction.md` — 6-Layer quantitative trend reverse-engineering & anti-fatigue energy tiers.
- `references/trend-forecasting-and-knowledge-evolution.md` — Eternal-Student domain learning & 5-Signal Trend Prediction methodology.
- `references/cross-skill-synergy-mesh.md` — Collaboration protocols connecting Auto-Curiosity with all 48+ bundled and external skills.
- `references/curiosity-sandbox-and-handoff.md` — `curiosity_ledger/` JSON schemas and bidirectional handoff with `filmmaking-videography-photography-s2`.

## Gotchas

- **Sandbox Isolation**: Never test unfamiliar app flags or newly connected software directly on a user's live project file; always test inside `curiosity_ledger/sandbox_tests/` first.
- **Predictions Are Hypotheses, Not Dogma**: Present trend forecasts with confidence scores, supporting signals, and ways to adapt them to the creator's personal voice rather than chasing hype blindly.
- **Provider/Model Hard Lock**: Exploring or onboarding new tools must never modify the user's configured LLM `provider` or `model`.
