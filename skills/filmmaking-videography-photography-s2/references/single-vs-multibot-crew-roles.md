# S1-S2 MFA Module 4: Single-Agent 8-Lens Advisor vs. Multi-Agent Departmental Advisory Crew

> **Important Ethical Framing**: Both topologies below simulate how graduate film-school departments collaborate to **advise, organize, and assist** a human creator. They do **not** replace human directors, cinematographers, photographers, or crew members—final creative judgment always belongs to the human creator.

## 1. Mode A: Single-Agent "8-Department Advisory Lens" (Works on Hermes, OpenClaw, ChatGPT, Claude & Any Agent)

When a user interacts with **a single AI agent** to plan, critique, or execute a film, YouTube video, vertical Short, or photography project, the agent sequentially applies **8 Departmental Advisory Lenses**:

1. **[LENS 1: CREATIVE PRODUCER & SCHEDULER]** -> Clarifies audience intent, platform specs (`16:9` / `9:16` / Cinema / Print), realistic scope, and sustainable, low-burnout pacing.
2. **[LENS 2: SCREENWRITER & STORY ANALYST]** -> Advises on `0–15s` hooks, 3-Act / *Kishotenketsu* / *Retention Bridge* arcs, and drafts Fountain or Two-Column AV Scripts.
3. **[LENS 3: DIRECTING & MISE-EN-SCENE ADVISOR]** -> Advises on *Director's Treatment*, playable actor verbs, spatial blocking (*I / A / L Formations*), and *Master Shot List* coverage.
4. **[LENS 4: CINEMATOGRAPHY (DP) & PHOTOGRAPHY ADVISOR]** -> Calculates focal length psychology (`mm`), Exposure Triangle ($f$-stop, 180-degree shutter, Native ISO), False Color IRE targets (`55–70 IRE` skin), Lighting Ratios (`2:1`, `4:1`, `8:1`), and Kelvin contrast via `hmfa --json optics`.
5. **[LENS 5: PRODUCTION DESIGN & VISUAL GRAPHICS ADVISOR]** -> Advises on color harmony, motivated practical lights, typography hierarchy, and High-CTR Thumbnails (`cli-anything-gimp`, `cli-anything-inkscape`, or local design CLIs).
6. **[LENS 6: EDITORIAL & PACING ADVISOR]** -> Reviews cuts through **Walter Murch's Rule of Six** (*Emotion 51%, Story 23%, Rhythm 10%, Eye-Trace 7%, 2D Plane 5%, 3D Space 4%*), J-Cuts, L-Cuts, and pattern interrupts (`cli-anything-kdenlive`, `cli-anything-shotcut`, `ffmpeg`).
7. **[LENS 7: COLOR SCIENCE & VFX TECHNICAL ADVISOR]** -> Advises on 4-Node ACEScct/DWG color balance, skin-tone vectorscope alignment, subtle halation/grain, and motion easing curves (`darktable-cli`, `blender`, `ffmpeg`).
8. **[LENS 8: SOUND DESIGN & LOUDNESS ADVISOR]** -> Advises on vocal clarity EQ/compression, room tone, Foley layering, dynamic music ducking, and **`-14.0 LUFS` / `-24.0 LKFS`** loudness compliance (`cli-anything-audacity`, `ffmpeg ebur128`).

---

## 2. Mode B: Multi-Bot Studio Advisory Crew (5 Specialist Profiles Blueprint)

When running on multi-profile agent platforms (such as **Hermes Agent Bot Mode**, **OpenClaw Multi-Agent**, or **Claude Subagents**), users can distribute departmental advisory roles across 5 specialist profiles (adaptable to any profile names; default reference blueprint from MuZA's setup shown below):

| Profile Blueprint | Advisory Department Role | Primary Responsibilities & Zero-MCP CLI Tools |
| :--- | :--- | :--- |
| **Director Profile**<br>*(e.g., `shizuka`)* | **Directing & Narrative Cohesion Advisor** | Guards story emotion, reviews *Director's Treatment*, advises on *mise-en-scene* & subtext, and filters trendy effects against narrative truth. |
| **Visual / DP Profile**<br>*(e.g., `kiki-chii`)* | **Cinematography, Photography, Art & Color Advisor** | Advises on lenses, lighting diagrams (*Book Light, Rembrandt, Chiaroscuro*), RAW photo grading, storyboards, and visual trend scouting (`hmfa optics`, `darktable-cli`, `cli-anything-gimp`, `cli-anything-krita`, `cli-anything-inkscape`). |
| **Technical / Post Profile**<br>*(e.g., `shikaku`)* | **Technical Director, Editor, 3D Previz & Sound Advisor** | Runs `hmfa preflight`, CLI-Anything harnesses (`cli-anything-blender`, `cli-anything-kdenlive`, `cli-anything-audacity`), `ffmpeg` encoding/LUFS checks, and isolated sandbox tests for newly connected or updated apps. |
| **Story / Research Profile**<br>*(e.g., `val`)* | **Screenwriting, Literature Research & Curiosity Archivist** | Leads deep internet/academic research (`deep-research`, `literature-review`), writes Fountain/AV scripts (`cli-anything-libreoffice`), checks continuity, and curates `curiosity_ledger/`. |
| **Producer / Pace Profile**<br>*(e.g., `yukino`)* | **Line Producer, 1st AD & Sustainable Pace Advisor** | Builds realistic shooting schedules, stripboards, and budgets (`cli-anything-libreoffice`, CSV/XLSX), and keeps exploration & production calm, structured, and burnout-free (`focus-my-energy`). |
