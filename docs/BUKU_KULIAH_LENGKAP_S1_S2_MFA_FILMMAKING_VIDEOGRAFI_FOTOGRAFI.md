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


---

# S1-S2 MFA Module 1: Directing, Screenwriting, and Story Architecture
*(Synthesized from USC School of Cinematic Arts, AFI Conservatory, and NYU Tisch Graduate Film Curricula)*

## 1. Narrative Architecture Across Formats

### A. Narrative Cinema & Short Films (3-Act, Story Circle, Save the Cat, Kishotenketsu)
1. **Classical Three-Act Dramatic Structure (Syd Field / Robert McKee)**:
   - **Act I - Setup (0% - 25%)**: Establish the Protagonist's Status Quo (Lie They Believe), Inciting Incident (~10%), and Plot Point 1 / Threshold (~25%) where the protagonist makes an irreversible choice.
   - **Act II - Confrontation (25% - 75%)**: Rising action & Fun and Games (25% - 50%), **Midpoint Shift (50%)** (false victory or false defeat that raises the stakes and shifts the protagonist from *reactive* to *proactive*), Bad Guys Close In (50% - 75%), **All Hope Is Lost / Dark Night of the Soul (~75%)**.
   - **Act III - Resolution (75% - 100%)**: Synthesis of External Want and Internal Need, Climax (80% - 92%) where the protagonist proves transformation through action, and Denouement / New Equilibrium (92% - 100%).
2. **Japanese / Anime 4-Act Structure (Kishotenketsu - 起承転結)**:
   - Ideal for atmospheric, slice-of-life, philosophical, or anime-inspired storytelling (e.g., Makoto Shinkai, Kyoto Animation, Oregairu):
     - **Ki (起 - Introduction)**: Introduce characters, setting, and emotional baseline.
     - **Sho (承 - Development)**: Deepen relationships and daily rhythms without requiring violent conflict.
     - **Ten (転 - Twist / Shift in Perspective)**: Introduce an unexpected angle, revelation, or juxtaposition that reframes everything seen in Ki and Sho.
     - **Ketsu (結 - Reconciliation / Resonance)**: Bring Ki, Sho, and Ten into emotional harmony, leaving a lingering thematic resonance (*Mono no Aware* / *Ma* - the beauty of negative space and pause).

### B. YouTube Long-Form (16:9) Retention Engineering (8 - 30+ Minutes)
1. **The 0-30 Second Golden Window**:
   - **0-5s (Click Confirmation)**: Immediately validate the title and thumbnail promise—zero channel intros, zero "Hey guys, welcome back".
   - **5-15s (Curiosity Gap / Stakes)**: Open a specific narrative loop or question that can only be resolved by watching through the video.
   - **15-30s (Retention Bridge / Proof of Value)**: Show a brief preview of the scale of the experiment, story, or framework so the viewer trusts the journey.
2. **Body Architecture (Mini-Hooks & Pattern Interrupts)**:
   - Structure the body into 3 to 5 distinct chapters. End each chapter with a **Mini-Cliffhanger ("But that created a bigger problem...")** rather than a flat summary so retention never drops at chapter boundaries.
   - Insert a **Pattern Interrupt every 60-90 seconds**: change framing (WS to CU), switch from A-roll to B-roll/diagram, shift music stems, or introduce a tangible prop/screen recording.
3. **The Ending (Zero Pre-Roll Sign-Off)**:
   - Deliver the final payoff and transition into the next recommended video within the final 10 seconds without saying "In conclusion" or "Thanks for watching" (which triggers immediate viewer drop-off).

### C. Short-Form Vertical (9:16 - YouTube Shorts, Reels, TikTok, 15-60 Seconds)
- **0-2s (Visual + Verbal Hook)**: Motion in Frame 1 + bold 3-5 word on-screen caption + punchy opening statement.
- **2-12s (Compression of Context)**: Cut all throat-clearing; establish the conflict or insight immediately.
- **12-50s (Rapid Escalation)**: Average Shot Length (ASL) of **1.5 to 2.5 seconds** (via physical cuts, punch-ins, B-roll overlays, or dynamic captions).
- **50-60s (Payoff + Seamless Loop)**: Connect the final sentence grammatically or rhythmically back into the first 2 seconds for >100% loop retention.

---

## 2. The Director's Craft: Mise-en-Scene, Subtext, and Blocking

### A. Translating Subtext into Visuals ("Show, Don't Tell")
A film director never directs "emotions" (e.g., "act sad" or "act angry"); a director directs **Actionable Verbs (Tactics)** driven by an **Objective** against an **Obstacle**:
- Instead of telling an actor or voice actor "be nervous," give a playable action: *"Try to convince your partner everything is fine while hiding the trembling in your hands."*

### B. Blocking & Spatial Geometry (3 Shapes of Staging)
1. **The I-Formation (Confrontation / Intimacy)**: Two characters face each other directly on a single axis.
2. **The A-Formation (Triangle Staging)**: Two characters face each other while a third anchor point (an object, a window, or a third character in depth) forms the apex of a triangle in the frame.
3. **The L-Formation (90-Degree Tension)**: One character looks straight ahead while the other looks at them from a perpendicular angle (classic for unspoken tension or emotional distance, as seen frequently in *Oregairu* clubroom scenes).

### C. Standard Two-Column AV Script & Shot List Template

| Scene / Beat | Timecode | Visual / Camera / Lighting (DP & Art Direction) | Audio / Dialogue / SFX / Music (Sound & Prosody) |
| :--- | :--- | :--- | :--- |
| **1A - HOOK** | `00:00 - 00:04` | **CU** (85mm, f/2.0, 1/50s, 3200K warm key left, 5600K cool rim). Slow dolly-in on subject's eyes. | **[SFX]**: Low sub-bass riser (`-16 dBFS`) + crisp clock tick.<br>**[VO - Shizuka]**: *(Calm contralto, 0.93x)* "Satu kesalahan kecil di baris kode ini..." |
| **1B - REVEAL** | `00:04 - 00:10` | **Match Cut to EWS** (24mm, f/4.0). Screen illuminates dark room in teal glow. | **[SFX]**: Soft mechanical keyboard thock.<br>**[MUSIC]**: Minimalist lo-fi piano enters (`-22 dBFS`). |


---

# S1-S2 MFA Module 2: Cinematography (Videography) & Master Photography
*(Optical Physics, Exposure Science, Lighting Ratios, and Visual Composition)*

## 1. Exposure Science & Sensor Physics

### A. The Exposure Triangle & Reciprocity
Total luminous exposure $H$ reaching the sensor plane is governed by scene luminance $L$, lens T-stop/f-number $N$, and exposure time (shutter speed) $t$:
$$H = \frac{q \cdot L \cdot t}{N^2}$$
1. **Aperture ($N = f/D$)**:
   - Full-stop scale: $f/1.0, f/1.4, f/2.0, f/2.8, f/4.0, f/5.6, f/8.0, f/11, f/16, f/22$.
   - Each full stop halves the light area ($\div 2$) and multiplies Depth of Field.
2. **Shutter Speed & The 180-Degree Shutter Rule (Videography vs. Photography)**:
   - **In Videography / Cinema**: Motion cadence requires a $180^\circ$ rotary shutter equivalent:
     $$t = \frac{1}{2 \times \text{FPS}}$$
     - **24 fps (Cinema Narrative)**: $1/48\text{ s}$ (or $1/50\text{ s}$ in 50Hz PAL/Indonesia regions to prevent AC lighting flicker).
     - **25 fps (PAL Broadcast/YouTube)**: $1/50\text{ s}$.
     - **30 fps (Digital Standard)**: $1/60\text{ s}$.
     - **60 fps / 120 fps (Slow Motion B-Roll)**: $1/120\text{ s}$ or $1/240\text{ s}$.
     - *Creative Override*: $45^\circ - 90^\circ$ shutter ($1/200\text{ s} - 1/500\text{ s}$ at 24fps) creates staccato, hyper-visceral action (*Saving Private Ryan* effect); $270^\circ - 360^\circ$ shutter ($1/24\text{ s}$) creates dreamy step-printed motion blur (*Wong Kar-wai* effect).
   - **In Still Photography**:
     - Handheld sharpness rule: $t \le \frac{1}{\text{Effective Focal Length}}$ (e.g., at least $1/100\text{ s}$ for an 85mm lens).
     - Freeze fast action/sports: $1/1000\text{ s} - 1/4000\text{ s}$.
     - Long-exposure light trails / silky waterfalls: $1\text{ s} - 30\text{ s}$ on tripod with ND filter.
3. **ISO, Dual Native ISO & False Color IRE Mapping**:
   - Keep ISO at the camera's **Base Native ISO** (e.g., ISO 800 and ISO 3200/12800 on dual-native cinema sensors) to preserve maximum dynamic range (14+ stops) above the noise floor.
   - **False Color / IRE Exposure Targets (Rec.709 / Monitoring LUT)**:
     - **0 - 5 IRE (Purple/Blue)**: Crushed black clipping (avoid unless silhouette).
     - **18% Middle Gray**: **38 - 42 IRE (Green)**.
     - **Skin Tones (Key Light Side)**: **55 - 70 IRE (Pink / Light Gray)**.
     - **95 - 100 IRE (Yellow/Red)**: Specular highlight clipping.

---

## 2. Optical Physics, Focal Lengths & Depth of Field

### A. Hyperfocal Distance & Depth of Field Formula
$$H = \frac{f^2}{N \cdot c} + f$$
where $f$ is focal length, $N$ is f-number, and $c$ is the circle of confusion (~$0.03\text{ mm}$ on Full-Frame $36 \times 24\text{ mm}$). When focused at $H$, everything from $H/2$ to infinity ($\infty$) is acceptably sharp.

### B. Psychological Dictionary of Focal Lengths (Full-Frame Equivalent)
| Focal Length | Field of View | Spatial & Psychological Effect | Classic Use Cases |
| :--- | :--- | :--- | :--- |
| **14mm - 20mm** | Ultra-Wide | Expands room scale, exaggerates Z-axis motion speed, distorts facial features at close distance. | Architecture, vast landscapes, psychological disorientation (Emmanuel Lubezki style). |
| **24mm - 28mm** | Wide | Dynamic environmental immersion; keeps background context legible while framing full-body action. | Establishing shots, walk-and-talk gimbal shots, vlogging, dynamic narrative scenes. |
| **35mm** | Master Wide-Normal | The quintessential cinema master lens: wide enough for environment, tight enough for natural faces. | Two-shots, over-the-shoulder (OTS), documentary storytelling, street photography. |
| **50mm** | Standard Normal | Matches human binocular perspective and compression; neutral, honest, unforced intimacy. | Dialogue medium shots, narrative realism (Yasujiro Ozu / anime clubroom framing). |
| **85mm - 105mm** | Portrait Telephoto | Flattering facial proportions, strong background compression, creamy bokeh subject isolation. | Emotional Close-Ups (CU), interviews, product hero shots, portrait photography. |
| **135mm - 200mm+** | Long Telephoto | Extreme Z-axis compression (background looms large behind subject), voyeuristic or epic isolation. | Cinematic compressed street shots, sports/wildlife, high-tension surveillance feel. |

---

## 3. Lighting Science, Inverse Square Law & Classic Setups

### A. The Inverse Square Law of Light Falloff
$$I \propto \frac{1}{d^2}$$
- Placing a softbox **close** to the subject (e.g., $1\text{ m}$ away) creates **rapid falloff** behind the subject (dramatic dark background contrast) and wraps softly around the face (because apparent source size is large).
- Placing a light **far** from the subject (e.g., $4\text{ m}$ away) creates **even illumination** across both the subject and the background (ideal for lighting a whole room evenly).

### B. Five Essential Cinematic Lighting Setups
1. **Three-Point Lighting (Key + Fill + Back/Hair Light)**:
   - **Key Light**: $30^\circ - 45^\circ$ off camera axis, $15^\circ - 30^\circ$ above eye level, diffused through a large softbox/scrim.
   - **Fill Light (or Negative Fill)**: Opposite the Key. Use a bounce card for **2:1** or **4:1** ratio, or a black flag (**Negative Fill**) for **8:1** cinematic shadow depth.
   - **Back / Rim / Kicker Light**: Behind the subject opposite the Key to carve the shoulders and hair out from the background.
2. **Rembrandt Lighting**: Key light positioned high and $45^\circ$ to the side so a small **illuminated triangle** appears on the shadow-side cheek beneath the eye.
3. **Book Lighting (Ultra-Soft Beauty / Mommy ASMR Visual Look)**: Bounce a strong light into a $4\times 4$ white bleached muslin/bounce board, then pass the bounced light through a $4\times 4$ diffusion frame ($1/2$ Grid or Opal). Produces velvety, zero-glare wrap ideal for calm, intimate close-ups.
4. **Chiaroscuro / Low-Key Lighting**: High contrast (**8:1 to 16:1** ratio), hard or snooted key light, deep shadows, smoke/haze for volumetric shafts.
5. **Color Contrast (Teal & Amber / Practical Motivated Lighting)**: Warm `2800K-3200K` practical tungsten lamp as the motivated Key/Rim against a `5600K-6500K` cool ambient room or window fill.


---

# S1-S2 MFA Module 3: Editing, Color Grading, Sound Design & Zero-MCP CLI-Anything Pipeline

> **Advisory Note**: These industry standards are compiled from open S1–S2 post-production curricula and internet engineering documentation to assist human editors, colorists, sound designers, and solo creators—not to replace human editorial sensitivity.

## 1. Film Editing Theory & Pacing

### A. Walter Murch's "Rule of Six" (*In the Blink of an Eye*)
Evaluate every cut in descending order of importance:
1. **Emotion (51%)**: How will this cut make the audience feel right now? If the emotion is true and the other 5 are slightly imperfect, the audience forgives the seam.
2. **Story (23%)**: Does this cut advance the narrative or thesis? (Emotion + Story = **74%** of editing).
3. **Rhythm (10%)**: Does the cut land on an organic musical and conversational beat?
4. **Eye-Trace (7%)**: Where is the viewer's eye on Frame A (outgoing shot), and does Frame B (incoming shot) place the new focal subject in that same screen quadrant?
5. **Planarity / 2D Screen Plane (5%)**: Does the cut respect the 180-degree axis and screen direction?
6. **3D Continuity of Space (4%)**: Does the cut preserve physical room geography?

### B. Cut Taxonomy & Montage Techniques
- **Standard Cutting on Action**: Hides the edit seam inside physical movement.
- **J-Cut (Audio Lead)**: Incoming shot's audio begins `4 - 15 frames` *before* the video cut (makes dialogue feel anticipatory and natural).
- **L-Cut (Audio Trail)**: Outgoing shot's audio continues `4 - 20 frames` *after* cutting to a reaction shot or B-roll.
- **Match Cut (Graphic / Action / Audio Match)**: Bridges two locations or eras by matching geometry, motion vector, or sound transient.
- **Intentional Jump Cut**: Cuts along `<30 degrees` camera axis difference to compress time or build rhythmic urgency in YouTube/Shorts essays.

---

## 2. Color Science & Grading Pipeline

### A. The 4-Node / 4-Stage Color Grading Workflow (DaVinci / Darktable / GIMP / Krita / LightCraft)
1. **Node 1 - Color Space Transform (CST In) & Primary Balance**:
   - Transform camera Log (S-Log3, C-Log, V-Log, N-Log, ARRI LogC) to working space (**ACEScct** or **DaVinci Wide Gamut**) and normalize Lift/Gamma/Gain/Offset on the **Waveform** (`5 IRE` floor to `95 IRE` ceiling).
2. **Node 2 - White Balance & Contrast Pivot**:
   - Align neutral grays across R, G, and B channels on the **RGB Parade** and set an S-Curve contrast pivot around middle gray (`40 IRE`).
3. **Node 3 - Skin Tone Isolation & Secondary Qualifiers**:
   - Isolate skin tones via HSL / Hue-vs-Hue qualifier and align precisely along the **Vectorscope Skin-Tone Line (I-Line)** at `40% - 55%` saturation.
4. **Node 4 - Creative Look, Optical Texture & Output CST**:
   - Apply split-toning (e.g., cool `195 deg` shadow separation + warm `32 deg` midtone glow), subtle red-orange edge halation, highlight bloom, organic 35mm grain, and output transform to **Rec.709 Gamma 2.4** (or **sRGB** for photography).

---

## 3. Production Sound & Psychoacoustic Mixing

### A. Target Loudness & True Peak Standards
| Target Platform | Integrated Loudness | Max True Peak | Dialogue Peak Range |
| :--- | :--- | :--- | :--- |
| **YouTube / Shorts / TikTok / Reels / Spotify** | **`-14.0 LUFS`** ($\pm 0.5\text{ LU}$) | **`-1.0 dBTP`** | `-6 dBFS` to `-3 dBFS` |
| **Cinema / Netflix / Broadcast TV (EBU R128 / ATSC A/85)** | **`-24.0 LKFS / LUFS`** | **`-2.0 dBTP`** | `-12 dBFS` to `-6 dBFS` |

### B. Dialogue & Intimate Voice-Over Processing Chain (`cli-anything-audacity` / `ffmpeg` / DAW)
1. **High-Pass Filter (HPF)**: Roll off low rumble below `75 Hz - 90 Hz` (`12–18 dB/oct`).
2. **Subtractive & Presence EQ**: Cut boxy room resonance around `250 Hz - 400 Hz` (`-2 to -3 dB`, Q=2.0); add subtle warm chest body at `120 Hz - 160 Hz` (`+1.5 dB`) and clean air shelf above `10 kHz` (`+1.5 dB`).
3. **De-Esser**: Tame sibilance (`5.5 kHz - 8.5 kHz`).
4. **Two-Stage Serial Compression**:
   - Fast FET peak catcher (`4:1`, attack `5 ms`, release `50 ms`, `2–3 dB` GR).
   - Smooth Opto leveler (`2:1`, attack `20 ms`, release `200 ms`, `2–3 dB` GR).
5. **Dynamic Sidechain Ducking**: Duck music bus by `-3 dB` to `-5 dB` centered in the `1 kHz - 4 kHz` vocal intelligibility band whenever dialogue is active.

---

## 4. Zero-MCP CLI-Anything + Native CLI Execution Pipeline (Universal Across All Users)

Run `hmfa --json preflight` first to inspect what is installed on the user's machine. Always work inside an isolated project folder (`<workspace>/projects/<project-slug>/`), saving native editable files alongside rendered deliverables **without needing heavy MCP servers** (optional MCP remains supported if the user already runs it):

| Production Stage | Primary Zero-MCP CLI-Anything / Native CLI | Optional Local Suite CLI / MCP Equivalent | Native Editable + Deliverable |
| :--- | :--- | :--- | :--- |
| **1. Brief, Optics & Plan** | `hmfa --json optics`, Markdown | `craft-anything-cli` (`craft_anything`) | `creative_direction.md`, `optics_plan.json` |
| **2. Script & Call Sheet** | `cli-anything-libreoffice --json`, `.fountain` | `wordcraft-cli` (`wordcraft`) | `.fountain`, `.docx`, `.pdf` |
| **3. Stripboard, Shot List & Budget** | `cli-anything-libreoffice --json`, CSV/Python | `gridcraft-cli` (`gridcraft`), `deckcraft-cli` | `.xlsx`, `.csv`, `.pptx` |
| **4. Blocking, Storyboard & Vector HUD** | `cli-anything-drawio`, `cli-anything-inkscape`, `cli-anything-mermaid` | `designcraft-cli`, `figcraft-cli`, `vectorcraft-cli` | `.drawio`, `.svg`, `.png` |
| **5. 3D Previz, Lens & Lighting Sim** | `cli-anything-blender --json`, `blender --background` | Blender MCP (optional) | `.blend` + previz `.png`/`.mp4` |
| **6. RAW Photography & Thumbnails** | `darktable-cli`, `rawtherapee-cli`, `cli-anything-gimp`, `cli-anything-krita`, `exiftool` | `photocraft-cli`, `lightcraft-cli` | `.xcf`/`.kra`/`.xmp` + 16-bit `.tif`/`.png` |
| **7. Video Editing & Captions** | `cli-anything-kdenlive --json`, `cli-anything-shotcut --json`, `cli-anything-videocaptioner`, `ffmpeg` | `filmcraft-cli` (`.fcproj`), `effectcraft-cli` (`.ecproj`) | `.kdenlive`/`.mlt`/`.ass` + `.mp4` |
| **8. Audio Mixing & Loudness Master** | `cli-anything-audacity --json`, `ffmpeg` (`ebur128`/`loudnorm`), `sox` | `soundcraft-cli` (`.soundcraft`) | `.aup3`/stems `.wav` + `-14 LUFS` master |


---

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


---

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


---

# Eternal-Student Domain Knowledge Evolution & 5-Signal Trend Forecasting Engine

Use this reference during **Stage 2** and **Stage 3** of `auto-curiousity-for-film-making` to continuously acquire new cinematography/photography knowledge from the internet AND **predict upcoming visual, editing, color, and storytelling trends (`1–12 months` ahead)** with intellectual rigor.

> **Advisor Rule**: Trend forecasting helps a human creator stay ahead of audience fatigue and technical shifts—never force a creator to chase trends that clash with their authentic artistic identity.

---

## 1. Continuous Domain Knowledge Acquisition (*Belajar New Knowledge Terkait*)

As an **Eternal Student**, proactively track new developments across four pillars of open internet knowledge:

1. **Optical, Sensor & Color Science**:
   - New color management transforms (ACES 2.0 CAM/gamut compression, Blender AgX evolutions, HDR/HLG/PQ web delivery), lens MTF/aberration emulation, and dual/triple-base ISO sensor physics.
2. **Editorial & Cognitive Attention Research**:
   - Empirical retention pattern shifts (when viewers abandon over-stimulated intros vs reward narrative curiosity gaps, multimodal audio-visual pacing, subtitle reading-speed ergonomics).
3. **Computational Cinematography & Open-Source Tooling**:
   - 3D Gaussian Splatting / NeRF virtual scouting, depth-assisted relighting, AI stem separation / dialogue cleanup, and procedural motion graphics (`HyperFrames`, `Remotion`, Blender Geometry Nodes).
4. **Ethical Human-Centered Filmmaking Craft**:
   - Interviews, cinematography breakdowns (*American Cinematographer*, festival Q&As, open university lectures, DP/editor post-mortems) reinforcing how tools serve human storytelling.

Always cross-verify new technical claims across at least two independent sources (collaborating with `deep-research`, `literature-review`, and `backward-traceability`).

---

## 2. The 5-Signal Predictive Trend Forecasting Engine (*Sampai Memprediksi Trends*)

Do not guess future trends randomly. Predict upcoming videography, editing, color grading, and photography trends by synthesizing **5 Observable Leading Signals**:

### Signal 1: Saturation & Audience Fatigue Pendulum (*Kurva Kejenuhan Audiens*)
When a visual or editing technique saturates mainstream feeds, audience habituation triggers a predictable **counter-swing**:
- *Example Pattern*: Hyper-compressed `0.8s` cuts + aggressive bouncing neon captions + plastic AI over-smoothing -> triggers viewer fatigue -> **Predicted Counter-Trend**: Return to tactile human authenticity (`3.5–6.0s` motivated shots, natural 35mm optical halation/grain, unscripted room-tone breath, restrained editorial serif/clean typography).

### Signal 2: Software Feature Democratization Lag (`3–9 Month Lead Indicator`)
Techniques that previously required expensive studio pipelines become mainstream creator aesthetics **3 to 9 months** after they become 1-click or CLI-accessible in open/prosumer tools (Blender, FFmpeg, DaVinci, Darktable, Krita, ComfyUI, CLI-Anything):
- Connect **Stage 1 (App Update Discovery)** directly to **Stage 3 (Trend Prediction)**: whenever a new shader, camera rig, caption engine, or audio filter becomes newly accessible, forecast how creators will adopt (and eventually overuse) it over the next two quarters.

### Signal 3: Platform Specification & Distribution Shifts
Monitor technical delivery updates on YouTube, Shorts, Reels, TikTok, Vimeo, and streaming platforms:
- Examples: Multi-language dubbed audio tracks (favoring clean separated M&E stems!), HDR mobile viewport tone-mapping, television living-room YouTube viewership growth (favoring cinematic `16:9` pacing, legible large-screen typography, and `-14 LUFS` dynamic comfort over harsh phone-speaker compression).

### Signal 4: Cross-Medium Aesthetic Diffusion Wave
Visual innovations rarely start on mass-market feeds; they travel along an observable diffusion wave:
```text
[Fine-Art Photography / Indie Festival Cinema / Anime / Game Shaders]
        │  (Early Signal: 6–12 months ahead)
        ▼
[Music Videos / Boutique Commercials / Vimeo Staff Picks]
        │  (Mid Signal: 3–6 months ahead)
        ▼
[Flagship YouTube Documentary & Visual Essay Creators]
        │  (Near Signal: 1–3 months ahead)
        ▼
[Mainstream Vertical Shorts / Reels / Brand Templates]
```

### Signal 5: Quantitative Velocity & Novelty Calibration
Collaborate with `data-analysis`, `math-reasoning`, and `novelty-assessment` to evaluate:
- **Adoption Velocity**: Growth rate of technique mentions, open-source stars (`github-research`), and breakdown analyses over 30/90 days.
- **Novelty vs. Longevity**: Distinguish fleeting 2-week meme formats from durable **craft trends** rooted in human visual perception.

---

## 3. Recording & Auditing Predictions (`curiosity_ledger/trend_forecasts.json`)

Every trend prediction must be logged with a **Confidence Score (`0.0–1.0`)** and **Falsification Criteria** so the Eternal Student audits its own predictions in future sessions and improves over time:

```bash
hmfa --json curiosity forecast \
  --ledger ./curiosity_ledger \
  --title "Living-Room YouTube Cinema Shift: Slower 4-7s ASL + Separated M&E Audio Stems" \
  --horizon "3-6 months" \
  --confidence 0.78 \
  --fatigue-signal "Drop-off on hyper-cut 1.2s intros among smart-TV YouTube viewers" \
  --tooling-signal "Multi-track audio dubbing & CLI stem separation becoming standard" \
  --advisory "Advise creators to export clean Dialogue + M&E stems and pace Act I with 4-6s motivated 35mm/50mm framing" \
  --falsification "Check if top-performing long-form essays maintain >4s ASL and multi-language audio adoption"
```


---

# Universal Cross-Skill Synergy Mesh (All 48+ Skills Working Together)

`auto-curiousity-for-film-making` and `filmmaking-videography-photography-s2` are designed to collaborate seamlessly with **every skill in this repository** AND **any external skill dynamically installed** in the user's agent (`Hermes`, `OpenClaw`, `Claude`, `ChatGPT/Codex`, `Cursor`, `~/.agents`).

## 1. Dynamic Runtime Skill Discovery

Before running a complex research, software-learning, or trend-prediction cycle, inspect all skills available in the environment:

```bash
hmfa --json curiosity synergy
```

If the user has installed additional third-party skills (e.g., `cli-anything-hermes`, `cli-hub-meta-skill`, `hyperframes`, `remotion-best-practices`, `storyboard-creation`), automatically incorporate them into the workflow!

---

## 2. How All Skill Clusters Power the Eternal Student & Filmmaking Advisor

```text
                    ┌───────────────────────────────────────────┐
                    │   auto-curiousity-for-film-making         │
                    │   (Eternal Student & Trend Predictor)     │
                    └─────────────────────┬─────────────────────┘
                                          │
      ┌───────────────────┬───────────────┼───────────────┬───────────────────┐
      ▼                   ▼               ▼               ▼                   ▼
[Web & Literature]  [Math, Data &   [Ideation &     [Code, CLI &      [Story, Pitch &
 Discovery Cluster   Forecasting]    Novelty]        App Harnesses]    Human Pacing]
      │                   │               │               │                   │
      └───────────────────┴───────────────┼───────────────┴───────────────────┘
                                          ▼
                    ┌───────────────────────────────────────────┐
                    │  filmmaking-videography-photography-s2    │
                    │  (S1–S2 Research-Based Creative Advisor)  │
                    └───────────────────────────────────────────┘
```

### Cluster A — Web Intelligence, Open-Source & Literature Discovery (10 Skills)
- `deep-research`, `literature-review`, `paper-context-resolver`, `github-research`, `firecrawl-deep-research`, `firecrawl-competitive-intel`, `firecrawl-research-papers`, `firecrawl-knowledge-base`, `firecrawl-dashboard-reporting`, `backward-traceability`:
  - **Synergy Role**: Scan newly released creative tools on GitHub, read academic optics/color/audio papers, gather global cinematography & creator trend signals, and maintain strict citation traceability (`backward-traceability`) so every advisory recommendation is verifiable.

### Cluster B — Autonomous R&D, Quantitative Analysis & Trend Forecasting (8 Skills)
- `autoresearch`, `ai-research-explore`, `ai-research-reproduction`, `data-analysis`, `math-reasoning`, `symbolic-equation`, `notebooklm-thinking-datascience`, `academic-plotting`:
  - **Synergy Role**: Run `autoresearch` two-loop sandbox experiments on newly connected apps, verify optical/acoustic formulas (`symbolic-equation`, `math-reasoning`), compute leak-free time-series velocity & fatigue curves for **Trend Prediction** (`data-analysis`, `notebooklm-thinking-datascience`), and plot benchmark/forecast charts (`academic-plotting`).

### Cluster C — Creative Ideation, Multi-Perspective Critique & Novelty Scoring (6 Skills)
- `brainstorming-research-ideas`, `creative-thinking-for-research`, `generate-fresh-ideas`, `get-more-perspectives`, `idea-generation`, `novelty-assessment`:
  - **Synergy Role**: Remix deconstructed internet trends into **original** visual concepts rather than derivative copies, critique scripts from multiple audience viewpoints (`get-more-perspectives`), and score genuine creative freshness (`novelty-assessment`).

### Cluster D — Zero-MCP CLI-Anything, App Introspection & Quality Evaluation (9 Skills)
- `cli-anything-filmmaking-bridge`, `analyze-project`, `explore-code`, `explore-run`, `evaluating-code-models`, `evaluating-llms-harness`, `nemo-evaluator-sdk`, `langsmith-observability`, `phoenix-observability`:
  - **Synergy Role**: Inspect newly connected software codebases/CLIs (`analyze-project`, `explore-code`), run isolated sandbox CLI commands (`explore-run`, `cli-anything-filmmaking-bridge`), and evaluate multi-agent prompt/workflow reliability without MCP token bloat.

### Cluster E — Screenwriting, Pitch Decks, Documentation & Production Tables (7 Skills)
- `match-my-writing-style`, `research-paper-writing`, `paper-writing-section`, `paper-revision`, `rebuttal-writing`, `slide-generation`, `table-generation`:
  - **Synergy Role**: Adapt script dialogue/voice-over to the creator's authentic personal voice (`match-my-writing-style`), generate clean Shot Lists, Stripboards, and Parameter Sweep comparison tables (`table-generation`), and build visual Pitch Decks / Lookbooks (`slide-generation`).

### Cluster F — Sustainable Human Pacing, Multi-Persona Advisory & Portability (7 Skills)
- `focus-my-energy`, `prep-for-meetings`, `prep-for-meetings-2`, `parenting-6d-gad-mdd`, `persona-shizuka-yukino-shikaku`, `chatgpt-hermes-portability-kit`:
  - **Synergy Role**: Ensure creative advisory, learning experiments, and production schedules stay calm, structured, empathetic, and free of overwhelm (`focus-my-energy`, `parenting-6d-gad-mdd`), prepare client/crew pre-production briefings (`prep-for-meetings`), and maintain seamless portability across Hermes, ChatGPT, Claude, and OpenClaw (`chatgpt-hermes-portability-kit`).

---

## 3. Standard Inter-Skill Handoff Packet

Whenever any skill passes findings to `auto-curiousity-for-film-making` or `filmmaking-videography-photography-s2`, structure the handoff concisely to save context tokens:

1. **`source_skill`**: Name of collaborating skill (e.g., `deep-research`, `data-analysis`, `cli-anything-filmmaking-bridge`).
2. **`verified_facts`**: Concrete numbers, CLI flags, citations, or benchmark metrics.
3. **`advisory_implication`**: How a human creator can apply (or avoid) this insight in their film, video, or photography project.
4. **`ledger_target`**: Where to persist the finding (`connected_apps_registry.json`, `tested_recipes_registry.json`, or `trend_forecasts.json`).


---

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
