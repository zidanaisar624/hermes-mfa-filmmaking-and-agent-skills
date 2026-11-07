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
