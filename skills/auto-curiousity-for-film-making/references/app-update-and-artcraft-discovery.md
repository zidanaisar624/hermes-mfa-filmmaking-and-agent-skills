# Eternal-Student App Onboarding & Software Update Discovery Protocol

Use this reference during **Stage 1** of `auto-curiousity-for-film-making` whenever **a brand-new application is connected** OR **an existing creative tool updates**—using zero-MCP **CLI-Anything (`HKUDS/CLI-Anything`)** and native CLIs first.

## 1. Universal Creative Software Discovery Targets (No Hardcoded Paths)

Run `hmfa --json preflight` to detect what actually lives on the current user's machine across all drives (`C:`, `D:`, `/usr/local/bin`, `/Applications`, `~/.local/bin`, etc.) without altering any LLM provider or model configuration:

| Software Category | CLI-Anything Harnesses (`--json`) | Native / Local Suite CLIs | Primary Eternal-Student Learning Focus |
| :--- | :--- | :--- | :--- |
| **3D, Set & Previz** | `cli-anything-blender`, `cli-anything-freecad` | `blender --background`, `cadcraft-cli`, `solidcraft-cli` | New Geometry/Compositor nodes, Cycles/EEVEE shaders, AgX/ACES views, camera lens/rig constraints. |
| **NLE Video & VFX** | `cli-anything-kdenlive`, `cli-anything-shotcut`, `cli-anything-videocaptioner` | `ffmpeg`, `ffprobe`, `scenedetect`, `filmcraft-cli`, `effectcraft-cli` | New timeline transitions, ASS/kinetic subtitle capabilities, optical flow/speed-ramp curves, codecs. |
| **Photography, RAW & Color** | `cli-anything-gimp`, `cli-anything-krita`, `cli-anything-comfyui` | `darktable-cli`, `rawtherapee-cli`, `exiftool`, `magick`, `photocraft-cli`, `lightcraft-cli` | RAW demosaicing, tone-mappers (AgX/Sigmoid/Filmic), halation/grain modules, ICC/LUT pipelines. |
| **Vector, Layout & Diagrams** | `cli-anything-inkscape`, `cli-anything-drawio`, `cli-anything-mermaid` | `graphviz`, `designcraft-cli`, `figcraft-cli`, `vectorcraft-cli` | SVG typography, HUD callouts, storyboard frame grids, lighting & blocking topology diagrams. |
| **Audio & Loudness** | `cli-anything-audacity` | `ffmpeg` (`ebur128`/`loudnorm`), `sox`, `soundcraft-cli` | Spectral de-noisers, dynamic EQ sidechaining, compressor envelopes, EBU R128 / LUFS limiters. |
| **Capture & Docs** | `cli-anything-obs-studio`, `cli-anything-openscreen`, `cli-anything-libreoffice` | `wordcraft-cli`, `gridcraft-cli`, `deckcraft-cli`, `pdfcraft-cli` | Lossless screen/studio recording, Fountain screenplay export, stripboard/budget formulas. |

---

## 2. Protocol A: Onboarding ANY Newly Connected Application (*Tiap Tambah Aplikasi Baru*)

Whenever the user installs, links, or asks you to use **any new app** (even one never seen before, e.g., Natron, DaVinci Resolve CLI, VapourSynth, Nuke, Reaper, TouchDesigner, HyperFrames, Remotion, or a new GitHub tool):

1. **Step 1 — Fingerprint & Snapshot Registration**:
   ```bash
   hmfa --json curiosity onboard-app --app <app-binary-or-name> --ledger ./curiosity_ledger
   ```
   - Inspect `--version`, `--help`, subcommands, supported input/output file extensions, and exit codes.
2. **Step 2 — Check CLI-Anything Hub or Build a Lightweight CLI Wrapper**:
   - Check `cli-hub search <keyword>` (if `cli-anything-hub` is installed) to see if an agent-ready `--json` harness already exists.
   - If the app is an open-source codebase or scriptable app without a harness, collaborate with `cli-anything-filmmaking-bridge`, `analyze-project`, and `explore-code` (or `cli-anything-hermes`) to map its CLI/Python/Lua backend without requiring an MCP server.
3. **Step 3 — Documentation & Community Knowledge Study**:
   - Collaborate with `deep-research` / `github-research` / `firecrawl-deep-research` to study the app's official documentation, color/audio pipeline assumptions, and common gotchas (e.g., single-process database locks, color-space gamma shifts, headless flags).
4. **Step 4 — Safe "Hello Asset" Sandbox Calibration**:
   - Inside `curiosity_ledger/sandbox_tests/<app-name>/`, run a minimal non-destructive smoke test (e.g., render 1 test frame, transcode a 2-second test clip, or measure a 3-second WAV stem) and verify the output file with `ffprobe` / `exiftool`.
   - Record verified syntax and gotchas into `curiosity_ledger/connected_apps_registry.json` and `curiosity_ledger/app_and_update_learning_log.md`.

---

## 3. Protocol B: Learning Every Software Update (*Tiap Ada Update Aplikasi*)

1. **Automated Capability Diffing**:
   - Re-run `hmfa --json curiosity onboard-app --app <app> --ledger ./curiosity_ledger`.
   - If `status` returns `"updated_capabilities_detected"`, inspect release notes / `CHANGELOG.md` / `ffmpeg -filters` / `--help` diff to isolate newly added flags, filters, or nodes.
2. **Formulate an Testable Feature Hypothesis**:
   - Example: *"Version update added `halation_threshold` (`0.0–1.0`); hypothesis: isolates red-channel film scatter to specular highlights above `75 IRE` without muddying `60 IRE` skin tones."*
3. **3-Point Micro-Sandbox Parameter Sweep**:
   - Test on a disposable 2-second synthetic/reference asset in `curiosity_ledger/sandbox_tests/` at **Low (`20%`)**, **Default**, and **Extreme (`90–100%`)**:
     - Check highlight/black clipping (`<5 IRE` or `>95 IRE`),
     - Check Vectorscope skin-tone stability,
     - Check audio True Peak (`<= -1.0 dBTP`),
     - Measure render-time overhead per frame.
4. **Promote Sweet-Spot Recipe**:
   - Save the verified sweet-spot range to `curiosity_ledger/tested_recipes_registry.json` so `filmmaking-videography-photography-s2` can advise the creator immediately.
