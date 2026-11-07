---
name: filmmaking-videography-photography-s2
description: Research-based S1-S2 (BFA/MFA) filmmaking, directing, cinematography, videography, photography, editing, color science, and sound design advisor skill. Synthesized from open film-school curricula and internet knowledge as a Creative & Technical Advisor (NOT a replacement for human filmmakers), executing via zero-token CLI-Anything harnesses, native CLIs, or optional MCP across Hermes, OpenClaw, ChatGPT, and Claude.
version: 2.0.0
---

# Filmmaking, Directing, Videography & Photography Advisor (S1–S2 BFA/MFA Research Synthesis)

Provide structured, research-backed creative and technical advisory grounded in **undergraduate (S1 / BFA) and graduate (S2 / MFA) filmmaking, cinematography, videography, and still photography curricula** alongside open industry knowledge on the internet.

> **Ethical Role & Positioning (Advisor, NOT Replacement)**:
> This skill was built by researching and synthesizing what S1 and S2 film/photography graduates study across narrative cinema, documentary, YouTube (`16:9`), vertical media (`9:16`), and still photography. **It is NOT a replacement for human filmmakers, directors, cinematographers, photographers, editors, colorists, or sound designers.** Instead, it serves as an objective **Creative & Technical Advisor / Co-Pilot** that helps human creators reason through story structure, optical physics, lighting ratios, color pipelines, audio loudness, and repeatable CLI workflows—while artistic intuition, lived human emotion, on-set judgment, and final creative authorship remain 100% human.

## Universal Agent & Zero-Token CLI Compatibility

- **Supported Agents**: Optimized #1 for **Hermes Agent** (Single-Bot & Multi-Bot Profiles), and 100% compatible with **OpenClaw**, **Claude (Claude Code & Claude Projects)**, **ChatGPT (Custom GPTs, Projects & Codex CLI)**, **Cursor**, and any `agentskills.io` agent.
- **Zero-MCP Token Execution First**: Prioritize **CLI-Anything (`HKUDS/CLI-Anything` / `cli-hub`)** harnesses (`cli-anything-blender`, `cli-anything-kdenlive`, `cli-anything-shotcut`, `cli-anything-gimp`, `cli-anything-krita`, `cli-anything-inkscape`, `cli-anything-audacity`, `cli-anything-videocaptioner`, `cli-anything-libreoffice`, `hmfa`) and native CLIs (`ffmpeg`, `ffprobe`, `blender --background`, `darktable-cli`, `exiftool`, or local `*-cli` binaries) via `cli-anything-filmmaking-bridge` so you consume **0 idle MCP schema tokens**. Use MCP servers only as an optional secondary path if the user explicitly requests them.

## When to Use

- The user wants research-grounded S1–S2 film/photography advice to plan, write, storyboard, light, shoot, edit, color-grade, or master a short film, feature concept, YouTube video, documentary, commercial, or photography series.
- The user wants either **Single-Advisor Full-Department Review (Mode A)** or **Multi-Agent Departmental Advisory Perspectives (Mode B)** reviewing their project from Directing, Cinematography, Editing, Screenwriting, and Production lenses.
- The user needs deterministic optical, lighting, color, or audio calculations (`hmfa --json optics`) or zero-MCP CLI execution across creative desktop software.

## Step 1: Select Advisory Crew Topology (Mode A vs. Mode B)

Determine whether the session runs in **Mode A (Single-Agent 8-Lens Advisor)** or **Mode B (Multi-Bot Departmental Advisory Crew)**:

1. **Mode A — Single-Agent "8-Department Advisory Lens"**:
   - One agent sequentially advises the human creator through 8 classical film-school department perspectives: (1) Creative Producer / Scheduler, (2) Screenwriter, (3) Director, (4) Director of Photography (DP) / Photographer, (5) Production Designer / Gaffer, (6) Film Editor, (7) Colorist & VFX Technical Advisor, and (8) Sound Designer / Mastering Engineer.

2. **Mode B — Multi-Bot Studio Advisory Crew (e.g., 5 Specialist Hermes / Multi-Agent Profiles)**:
   - Divides departmental advisory and technical assistance across specialist profiles (customizable to any user's bot names; default blueprint includes):
     - **Director & Showrunner Advisor (`shizuka` / Director Profile)**: Advises on dramatic arc, Director's Treatment, emotional subtext, mise-en-scene, and cut review.
     - **DP, Photography, Art & Color Advisor (`kiki-chii` / Visual Profile)**: Advises on focal lengths, exposure physics, lighting ratios, composition, thumbnails, and 4-node color grading (`cli-anything-gimp`, `cli-anything-krita`, `cli-anything-inkscape`, `darktable-cli`, or `photocraft-cli` / `lightcraft-cli`).
     - **Technical Director, Editor, 3D Previz & Sound Advisor (`shikaku` / Tech Profile)**: Assists with CLI-Anything preflight, NLE assembly, 3D camera/lighting previz, keyframes, and `-14 LUFS` / `-24 LKFS` mastering (`cli-anything-blender`, `cli-anything-kdenlive`, `cli-anything-audacity`, `ffmpeg`, or `filmcraft-cli` / `effectcraft-cli` / `soundcraft-cli`).
     - **Screenwriter, Researcher & Continuity Advisor (`val` / Story Profile)**: Assists with literature/context research, 3-Act / Kishotenketsu / Retention scripts, Fountain & Two-Column AV formatting, and `curiosity_ledger/` documentation.
     - **Line Producer & Sustainable Pacing Advisor (`yukino` / Producer Profile)**: Assists with stripboards, shot lists, budgets, and calm, sustainable creative pacing (`cli-anything-libreoffice`, CSV/XLSX, or `gridcraft-cli`).

Read `references/single-vs-multibot-crew-roles.md` for full departmental handoff templates.

## Step 2: Advise & Assist Across the 5-Phase S1–S2 Curriculum Pipeline

### Phase 1: Development & Screenwriting (Story Architecture)

1. Recommend a narrative structure matched to the creator's medium and intent:
   - **Short-Form Vertical (`9:16`, 15–60s)**: Hook (`0–3s` visual + verbal disruption) -> Stakes (`3–10s`) -> Escalating Beats (`10–45s`, visual shift every `2–3s`) -> Payoff & Seamless Loop (`45–60s`).
   - **Long-Form YouTube / Documentary (`16:9`, 8–30+ min)**: Cold Open Hook (`0–15s` confirming click promise) -> Retention Bridge & Thesis Stakes (`15–45s`) -> Chaptered Segments with Mini-Cliffhangers and Pattern Interrupts every `60–90s` -> Climax Payoff.
   - **Narrative Cinema / Indie / Anime Short or Feature**: Classical 3-Act Structure (*Setup 25%, Confrontation 50%, Resolution 25%*), *Dan Harmon's 8-Step Story Circle*, *Blake Snyder's 15 Beats*, or East Asian 4-Act **Kishotenketsu** (*Ki, Sho, Ten, Ketsu* — conflict-independent perspective shift).
2. Draft or review scripts in **Fountain Screenplay Format** (`1 page ≈ 1 minute`) or **Two-Column Audio/Visual (AV) Script** (`~130–150 WPM` spoken pacing paired with Shot Size, Lens, Movement, and B-Roll).

Read `references/mfa-directing-screenwriting.md` for full curriculum notes and templates.

### Phase 2: Pre-Production & Directing (Mise-en-Scene, Coverage & Scheduling)

1. Help the human director translate subtext into physical staging (**Actionable Verbs & Blocking Topologies**: *I-Formation* confrontation, *A-Formation* hierarchy, *L-Formation* unspoken tension).
2. Advise on a **Master Shot List & Coverage Plan** (EWS/WS geography -> MS/OTS anchor -> CU/ECU reserved for emotional turning points) respecting the **180-Degree Axis of Action** and **30-Degree Rule** (unless intentionally broken for psychological disorientation).
3. Organize the **1st AD Stripboard** by location, lighting direction, and focal length rather than chronological script page order to save on-set turnaround time.

### Phase 3: Cinematography (Videography) & Still Photography Physics

Ground camera recommendations in optical and sensor physics (run `hmfa --json optics` for exact numbers):

1. **Exposure Triangle & Shutter Cadence**:
   - **Aperture ($f$-stop)**: Controls Depth of Field and light intake ($f/1.4 - f/2.8$ shallow isolation; $f/5.6 - f/11$ deep spatial context).
   - **180-Degree Shutter Rule**: $t = \frac{1}{2 \times \text{FPS}}$ (`24 fps -> 1/48s` or `1/50s` in 50Hz PAL regions; `60 fps -> 1/120s`). Advise Neutral Density (ND) filters outdoors rather than cranking shutter speed.
   - **Native ISO & False Color (IRE)**: Expose at Base/Dual-Native ISO. Guide skin-tone key placement to **`55–70 IRE`** (`45–55 IRE` deep skin, `55–65 IRE` medium/SEA skin, `60–70 IRE` light skin) while guarding highlights `< 95 IRE`.
2. **Optics, Hyperfocal Math ($H = \frac{f^2}{N \cdot c} + f$) & Focal Psychology**:
   - `14mm–24mm` (spatial expansion & dynamic tension), `35mm–50mm` (grounded human perspective), `85mm–135mm+` (background compression & intimate isolation).
3. **Lighting Design & Inverse Square Law ($I \propto 1/d^2$)**:
   - Advise **Motivated Lighting** with intentional **Key-to-Fill Ratios**: **`2:1`** (*High-Key / Soft Book-Light*), **`4:1`** (*Naturalistic Drama / Rembrandt*), **`8:1+`** (*Low-Key Chiaroscuro / Negative Fill*), plus Kelvin color contrast (e.g., `3200K` warm key vs `5600K` cool fill/rim).

Read `references/mfa-cinematography-photography.md` for formulas, diagrams, and still-photography shutter rules.

### Phase 4: Post-Production Advisory (Editing, Color Science & Psychoacoustic Audio)

1. **Film Editing — Walter Murch's Rule of Six**:
   Evaluate cuts in strict priority: **(1) Emotion `51%`**, **(2) Story `23%`**, **(3) Rhythm `10%`**, **(4) Eye-Trace `7%`**, **(5) 2D Screen Plane `5%`**, **(6) 3D Space `4%`**, smoothing dialogue transitions with `4–15 frame` **J-Cuts** and **L-Cuts**.
2. **4-Stage Color Pipeline (ACEScct / DaVinci Wide Gamut -> Rec.709 / sRGB)**:
   - Stage 1: CST In & Primary Waveform Balance (`5–95 IRE`) -> Stage 2: RGB Parade Neutralization & Contrast Pivot -> Stage 3: Vectorscope Skin-Tone Line Isolation -> Stage 4: Creative Palette, Halation, Bloom & Organic Grain.
3. **Sound Design & Loudness Mastering**:
   - Dialogue chain (HPF `80 Hz`, subtractive boxiness cut `250–400 Hz`, de-esser, two-stage FET+Opto compression), `-3` to `-5 dB` dynamic music ducking in `1–4 kHz`, mastered to **`-14.0 LUFS` (`-1.0 dBTP`)** for Web/YouTube/Shorts or **`-24.0 LKFS` (`-2.0 dBTP`)** for Cinema/Broadcast.

### Phase 5: Zero-MCP CLI-Anything & Cross-Skill Execution

When the user asks to generate project files, previz renders, edits, or grades on their machine:
1. Run `hmfa --json preflight` (via `cli-anything-filmmaking-bridge`) to detect available tools in the user's actual environment (never hardcode personal drive paths).
2. Execute non-destructively inside a dedicated project folder (`projects/<project-name>/`), saving editable source files (`.fountain`, `.blend`, `.kdenlive`, `.xcf`, `.kra`, `.svg`, `.aup3`, or `.fcproj`/`.ecproj`/`.soundcraft`) alongside exported deliverables (`.mp4`, `.png`, `.wav`, `.pdf`).
3. Pull fresh verified **Cinematic Recipe Cards** and **Trend Forecasts** from `auto-curiousity-for-film-making` (`curiosity_ledger/`), and collaborate with peer skills (`deep-research`, `literature-review`, `data-analysis`, `creative-thinking-for-research`, `novelty-assessment`, `slide-generation`, `match-my-writing-style`, `focus-my-energy`) whenever deeper research, data validation, or pitch materials are needed.

Read `references/mfa-editing-color-sound-artcraft.md` for full post-production and CLI-Anything / native CLI workflows.

## Gotchas

- **Advisor Humility**: Always frame creative suggestions with *why* they work optically, dramatically, or psychoacoustically, and offer options so the human creator makes the final artistic call.
- **Emotion Over Gimmicks**: Never sacrifice **Emotion (51%)** and **Story (23%)** for trendy transitions that contradict the scene's tone.
- **Provider/Model Lock**: Never alter any user agent `provider` or `model` settings during production or tool setup.
