---
name: cli-anything-filmmaking-bridge
description: Zero-MCP-token execution bridge connecting S1-S2 Filmmaking & Photography Advisory and Auto-Curiosity to HKUDS/CLI-Anything harnesses (cli-hub, Blender, GIMP, Krita, Inkscape, Kdenlive, Shotcut, Audacity, OBS, VideoCaptioner, ComfyUI, LibreOffice) and native CLIs (FFmpeg, Darktable, ExifTool, local *-cli binaries) across Hermes, OpenClaw, Claude, ChatGPT/Codex, and universal agents.
version: 2.0.0
---

# CLI-Anything Filmmaking & Photography Zero-Token Bridge

Execute creative software workflows (3D previz, RAW photography, color grading, NLE video assembly, captioning, and audio mastering) through deterministic **CLI-Anything (`HKUDS/CLI-Anything`)** harnesses and native command-line interfaces (`--json`) instead of connecting heavy MCP servers that consume tens of thousands of prompt tokens per turn.

> **Role & Philosophy**: This bridge empowers your AI Advisor to assist human creators with repeatable technical commands, optical calculations, and non-destructive project setup—acting as a **Technical Co-Pilot**, never replacing human directors, cinematographers, photographers, or editors.

## Why CLI-Anything Instead of Multi-Server MCP?

1. **Zero Idle Context Bloat**: Loading 15+ creative MCP servers injects hundreds of JSON tool schemas into every turn (~15,000–40,000 tokens wasted). CLI harnesses cost **0 tokens** until invoked via shell/terminal.
2. **Deterministic `--json` Output & Stateful Undo/Redo**: Every `cli-anything-<app>` harness supports `--json` structured output and stateful session files.
3. **Universal Agent Portability**: Works identically in **Hermes Agent (#1)**, **OpenClaw**, **Claude Code**, **OpenAI Codex**, **Cursor**, and any terminal-capable AI agent.

## Step 1: Run Zero-Token Creative Preflight

Before proposing or executing any creative software command, run a lightweight preflight check once per session:

```bash
# Built-in harness preflight (checks CLI-Anything harnesses, native binaries, and local *-cli suites)
hmfa --json preflight

# Or via official CLI-Anything Hub (if installed: pip install cli-anything-hub)
cli-hub matrix preflight video-creation --json
cli-hub matrix preflight image-design --json
```

Never assume an application is installed without checking `preflight` or `which`/`Get-Command`.

## Step 2: Map Filmmaking & Photography Stages to CLI-Anything Harnesses

Select the lightest available local CLI provider for each production stage (see `references/cli-anything-creative-matrix.md` for exact commands):

| Creative Stage | Primary CLI-Anything Harness (`--json`) | Native / Local CLI Alternatives (Zero-MCP) |
| :--- | :--- | :--- |
| **1. Advisory Math, Discovery & Updates** | `cli-anything-filmmaking --json optics` (`hmfa`) | Pure Python stdlib (`agent-harness/`) |
| **2. Script, Stripboard, Budget & Deck** | `cli-anything-libreoffice --json`, `cli-anything-obsidian --json` | Markdown `.fountain`, CSV, or local `wordcraft-cli` / `gridcraft-cli` / `deckcraft-cli` |
| **3. Blocking Diagrams & Storyboards** | `cli-anything-drawio --json`, `cli-anything-mermaid --json` | `graphviz` (`dot`), or local `designcraft-cli` / `figcraft-cli` |
| **4. 3D Camera Previz & Lighting Physics** | `cli-anything-blender --json` | `blender --background scene.blend --python script.py` |
| **5. RAW Photo, Retouch & Thumbnails** | `cli-anything-gimp --json`, `cli-anything-krita --json`, `cli-anything-comfyui --json` | `darktable-cli`, `rawtherapee-cli`, `exiftool`, `magick`, or `photocraft-cli` / `lightcraft-cli` |
| **6. Vector Titles, HUD & Lower-Thirds** | `cli-anything-inkscape --json` | `cairosvg`, `svgwrite`, or local `vectorcraft-cli` |
| **7. Studio Capture & Screen Recording** | `cli-anything-obs-studio --json`, `cli-anything-openscreen --json` | `ffmpeg` (`gdigrab` / `avfoundation` / `x11grab`) |
| **8. NLE Video Assembly & Captions** | `cli-anything-kdenlive --json`, `cli-anything-shotcut --json`, `cli-anything-videocaptioner --json` | `ffmpeg` (`filter_complex`, ASS subtitles), `scenedetect`, or `filmcraft-cli` / `effectcraft-cli` |
| **9. Sound Design & `-14 LUFS` Master** | `cli-anything-audacity --json` | `ffmpeg` (`ebur128`, `loudnorm`, `acompressor`, `sidechaincompress`), `sox`, or `soundcraft-cli` |

## Step 3: On-Demand Harness Installation or Custom CLI Generation

1. **Install Missing Pre-Built Harnesses Scope-by-Scope**:
   - Do not bulk-install 15 packages if the user only needs Blender and FFmpeg. Ask permission first, then install only the needed harness:
     ```bash
     pip install cli-anything-hub
     cli-hub info blender
     cli-hub install blender
     ```
2. **Build a Custom CLI-Anything Harness for Any Newly Connected App**:
   - When the user connects a new open-source or scriptable creative app without an existing harness, collaborate with `auto-curiousity-for-film-making` (and `cli-anything-hermes` if installed) to wrap its real backend/CLI into a `cli_anything.<software>` Click + `--json` + REPL package following `https://github.com/HKUDS/CLI-Anything`.

## Cross-Skill Collaboration Protocol

- **With `filmmaking-videography-photography-s2`**: Translates S1-S2 creative advisory plans (35mm lens previz, 4-node color balance, J/L-cuts, `-14 LUFS` audio targets) into concrete zero-MCP CLI commands.
- **With `auto-curiousity-for-film-making`**: Supplies `--version`, `--help`, and `cli-hub` capability diffs whenever an app updates or a new app is connected, and runs 2-second isolated micro-sandbox tests.
- **With All Research, Coding & Analysis Skills (`analyze-project`, `explore-code`, `explore-run`, `data-analysis`, `github-research`)**: Collaborates to inspect new software repositories, benchmark render times, and validate CLI outputs.

## Gotchas

- **Real Software Required**: A `cli-anything-<app>` harness wraps the real underlying application (e.g., Blender, GIMP, Kdenlive); verify the base binary is installed via `hmfa preflight`.
- **Optional MCP Coexistence**: If a user explicitly prefers an active MCP server they already configured, respect it—but never require MCP when CLI execution is available.
- **Hard Lock Safety**: Installing or running CLI harnesses must never alter the user's agent `provider` or `model` configuration.
