# Hermes S1–S2 (MFA) Filmmaking, Auto-Curiousity & 47 AI Agent Skills Suite

![Hermes MFA Filmmaking & Auto-Curiousity Banner](./assets/hero_banner.png)

[![Architected by Google Gemini](https://img.shields.io/badge/Architected_%26_Written_by-Google_Gemini-4285F4?style=flat-square&logo=google-gemini&logoColor=white)](https://gemini.google.com)
[![Initiated by MuZA](https://img.shields.io/badge/Initiated_%26_Experimented_by-Muhammad_Zidan_Aisar_(MuZA)-F59E0B?style=flat-square)](https://github.com/)
[![Skills Included](https://img.shields.io/badge/Modular_Skills-47_Agent_Skills-10B981?style=flat-square)](./skills)
[![MCP Servers](https://img.shields.io/badge/MCP_Integration-15_ArtCraft_+_Blender_5.2+-8B5CF6?style=flat-square)](#arsitektur-integrasi-16-server-mcp-artcraft--blender-52)
[![License: MIT](https://img.shields.io/badge/License-MIT-3B82F6?style=flat-square)](./LICENSE)

Repositori ini berisi paket **47 Modular AI Agent Skills** standar produksi (`SKILL.md` beserta modul referensi teknisnya) untuk **Hermes Agent**, **Claude Code**, **OpenClaw**, **Cursor**, dan ekosistem agen berbasis MCP. Fokus utama repositori ini adalah menyatukan **kurikulum produksi film, penyutradaraan, videografi, dan fotografi setara S1–S2 Master of Fine Arts (MFA)** dengan **mesin pembelajaran mandiri (*Autonomous R&D / Auto-Curiousity*)** yang secara kontinu mempelajari fitur baru dari pembaruan aplikasi kreatif serta membedah tren visual internet ke dalam parameter teknis terukur.

> **Asal-Usul Proyek (Attribution)**: Proyek ini berawal dari eksperimen dan keisengan **Muhammad Zidan Aisar (MuZA)** untuk menguji sejauh mana satu agen AI (atau kru multi-agen) dapat menguasai seluruh disiplin produksi film dari jenjang sarjana hingga pascasarjana sekaligus berevolusi sendiri mengikuti pembaruan perangkat lunak dan tren sinematografi internet. Seluruh kurikulum teknis, arsitektur sistem, rumus fisika optik/audio, dan ke-47 *skill* di dalam repositori ini dirancang, diteliti, dan ditulis oleh **Google Gemini**.

---

## 🎬 HERMES — Your AI Film Crew

![HERMES AI Film Crew](./assets/cinema_ai_social_preview.png)

*From idea to final cut — autonomously.*

---

## Daftar Isi

1. [Arsitektur Duet Skill Utama (`Auto-Curiousity` ↔ `MFA Filmmaking`)](#1-arsitektur-duet-skill-utama-auto-curiousity--mfa-filmmaking)
2. [Spesifikasi Teknis `filmmaking-videography-photography-s2`](#2-spesifikasi-teknis-filmmaking-videography-photography-s2)
3. [Spesifikasi Teknis `auto-curiousity-for-film-making`](#3-spesifikasi-teknis-auto-curiousity-for-film-making)
4. [Arsitektur Integrasi 16 Server MCP (ArtCraft & Blender 5.2+)](#4-arsitektur-integrasi-16-server-mcp-artcraft--blender-52)
5. [Mode Eksekusi Kru Produksi (Single-Bot vs Multi-Bot Crew)](#5-mode-eksekusi-kru-produksi-single-bot-vs-multi-bot-crew)
6. [Katalog Lengkap 47 Skills di Dalam Repositori](#6-katalog-lengkap-47-skills-di-dalam-repositori)
7. [Instalasi & Penggunaan](#7-instalasi--penggunaan)

---

## 1. Arsitektur Duet Skill Utama (`Auto-Curiousity` ↔ `MFA Filmmaking`)

![Dual Skill Architecture](./assets/dual_skill_architecture.png)

Sistem sinematik di repositori ini dibagi menjadi dua *skill* independen yang beroperasi dalam siklus tertutup (*closed-loop*):

| Komponen Skill | Direktori | Fungsi Inti | Output Utama |
| :--- | :--- | :--- | :--- |
| **`auto-curiousity-for-film-making`** | [`skills/auto-curiousity-for-film-making/`](./skills/auto-curiousity-for-film-making/SKILL.md) | Mesin R&D otonom yang mendeteksi pembaruan fitur/parameter aplikasi (ArtCraft, Blender, FFmpeg, dll.), mengujinya di kotak pasir (*sandbox*), dan melakukan *reverse-engineering* tren visual internet ke dalam 6 lapisan metrik kuantitatif. | `curiosity_ledger/tested_recipes_registry.json` (*Cinematic Recipe Cards*) |
| **`filmmaking-videography-photography-s2`** | [`skills/filmmaking-videography-photography-s2/`](./skills/filmmaking-videography-photography-s2/SKILL.md) | Mesin eksekusi produksi film pendek, film panjang, YouTube Long-Form (`16:9`), vertikal Shorts/Reels/TikTok (`9:16`), dan fotografi profesional melalui 5 fase produksi terstandarisasi. | Naskah Fountain/AV, *Shot List*, Previz 3D `.blend`, Proyek NLE `.fcproj`, VFX `.ecproj`, Audio `.soundcraft` |

---

## 2. Spesifikasi Teknis `filmmaking-videography-photography-s2`

Skill [`filmmaking-videography-photography-s2`](./skills/filmmaking-videography-photography-s2/SKILL.md) mengodekan standar kurikulum sekolah film pascasarjana (*USC School of Cinematic Arts, AFI Conservatory, NYU Tisch*) ke dalam aturan deterministik yang dapat dieksekusi oleh agen AI:

### A. Penyutradaraan & Penulisan Skenario (*Directing & Screenwriting*)
- **Arsitektur Naratif**: Struktur 3-Babak (*Setup 25%, Confrontation 50%, Resolution 25%*), *Dan Harmon's 8-Step Story Circle*, *Blake Snyder's 15-Beat Save the Cat*, struktur 4-Babak Asia Timur *Kishōtenketsu* (tanpa konflik konvensional), serta *YouTube Retention Architecture* (*0–15s Hook, 15–45s Retention Bridge, Pattern Interrupt tiap 60–90 detik, Payoff*).
- **Format Dokumen Standar Industri**: Penulisan skenario bioskop dalam sintaks **Fountain** (`1 halaman ≈ 1 menit layar`) dan penulisan video YouTube/komersial dalam **Two-Column Audio-Visual (AV) Script** dengan durasi per baris terukur.
- **Tata Kamera & *Blocking* Aktor**: Pemetaan topologi lantai *I-Formation* (konfrontasi langsung), *A-Formation* (dominasi hierarkis), dan *L-Formation* (introspeksi paralel) dengan kepatuhan ketat terhadap **180-Degree Axis of Action** dan **30-Degree Rule**.

### B. Sinematografi (Videografi) & Fotografi Master
- **Fisika Eksposur & *Shutter Angle***:
  - Rumus **180-Degree Shutter Rule**: $t = \frac{1}{2 \times \text{FPS}}$ (`24 fps → 1/48s` atau `1/50s`; `60 fps → 1/120s`).
  - Penempatan zona eksposur menggunakan **False Color (IRE)**: *Caucasian/Light Skin* pada `60–70 IRE`, *Medium/Olive/Southeast Asian Skin* pada `55–65 IRE`, *Deep/Dark Skin* pada `45–55 IRE`, dan *Clipping Guard* pada `< 95 IRE`.
- **Optik Lensa & *Hyperfocal Distance***:
  - Kalkulasi jarak hiperfokal: $H = \frac{f^2}{N \cdot c} + f$ (dengan $f$ = panjang fokus dalam mm, $N$ = bukaan *f-number*, dan $c$ = *circle of confusion* `0.029 mm` untuk Full-Frame).
  - Pemetaan psikologi panjang fokus dari `14mm–20mm` (distorsi ruang eksistensial), `35mm–50mm` (perspektif natural manusia), hingga `85mm–200mm` (kompresi latar dan isolasi potret).
- **Desain Pencahayaan & *Inverse Square Law***:
  - Hukum penurunan intensitas cahaya: $I \propto \frac{1}{d^2}$.
  - Rasio kontras **Key-to-Fill**: `2:1` (*High-Key / Soft Book-Light* melalui pantulan 45° dan difusi ganda), `4:1` (*Naturalistic Drama / Rembrandt*), dan `8:1+` (*Low-Key Chiaroscuro / Film Noir*).

### C. Penyuntingan (*Editing*), *Color Science*, & *Psychoacoustic Audio*
- **Walter Murch's Rule of Six**: Prioritas pemotongan gambar berdasarkan bobot: **(1) Emosi `51%`**, **(2) Alur Cerita `23%`**, **(3) Ritme `10%`**, **(4) *Eye-Trace* `7%`**, **(5) Bidang 2D `5%`**, dan **(6) Kontinuitas Ruang 3D `4%`**.
- **Pohon *Color Grading* 4-Node (ACEScct / DaVinci Wide Gamut)**:
  - `Node 1`: Koreksi Primer & Eksposur (Waveform `5–95 IRE`, RGB Parade).
  - `Node 2`: *Color Balance* (Lift/Gamma/Gain/Offset).
  - `Node 3`: *HSL Qualifier & Skin-Tone Isolation* (mengunci rona kulit pada **Vectorscope Skin-Tone Line** pukul `10:30–11:00`).
  - `Node 4`: *Creative Look*, *Halation*, *Highlight Bloom*, & *Film Emulation LUT* (Rec.709 Gamma 2.4 / sRGB).
- **Standar *Audio Mastering***:
  - **YouTube / Shorts / TikTok / Streaming Web**: **`-14.0 LUFS` Integrated** (`±0.5 LU`), **True Peak `-1.0 dBTP`**, dialog pada `-12` s/d `-18 dBFS`, musik latar di-*sidechain ducking* `-3` s/d `-5 dB` pada rentang vokal `1–4 kHz`.
  - **Cinema / Festival Broadcast (EBU R128 / ATSC A/85)**: **`-24.0 LKFS` Integrated** (`±2.0 LU`), **True Peak `-2.0 dBTP`**.

---

## 3. Spesifikasi Teknis `auto-curiousity-for-film-making`

Skill [`auto-curiousity-for-film-making`](./skills/auto-curiousity-for-film-making/SKILL.md) memberi agen kemampuan eksplorasi mandiri melalui 4 tahapan sistematis:

1. **Stage 1 — App Update & MCP Schema Introspection**:
   - Memeriksa skema JSON *tool* MCP, *changelog*, `git log`, dan daftar filter (`ffmpeg -filters`, *node* Blender, modul ArtCraft) lalu membandingkannya dengan `curiosity_ledger/app_capabilities_snapshot.json`.
   - Menjalankan **Eksperimen Mikro Kotak Pasir (`curiosity_ledger/sandbox_tests/`)** menggunakan **3-Point Parameter Sweep** (*Low 20%, Default, Extreme 95%*) pada klip uji sintetis berdurasi 2 detik untuk memverifikasi perilaku fitur baru tanpa menyentuh proyek utama.
2. **Stage 2 — 6-Layer Internet Trend Reverse-Engineering**:
   - Membedah referensi video viral atau karya sinema dari internet ke dalam 6 metrik teknis:
     1. *Hook & Pacing Math* (*Average Shot Length* / ASL dalam detik, *frame offset* J-Cut/L-Cut).
     2. *Camera & Lens Optics* (estimasi panjang fokus `mm`, *shutter angle*, kurva gerak kamera).
     3. *Lighting & Exposure Topology* (rasio *Key-to-Fill*, kontras Kelvin, target IRE kulit).
     4. *Color Science & Texture* (pergeseran HSL, radius *halation*, *bloom*, tekstur *grain*).
     5. *VFX & Motion Design* (fungsi kecepatan `cubic-bezier(x1, y1, x2, y2)`, *masking*, proyeksi kamera 3D).
     6. *Psychoacoustic Audio* (penempatan *sub-drop* `40–65 Hz`, *riser*, *whoosh*, dan target LUFS).
3. **Stage 3 — Recipe Synthesis (`tested_recipes_registry.json`)**:
   - Mengonversi hasil eksperimen menjadi **Kartu Resep Sinematik (*Recipe Card*)** berformat JSON/Markdown yang berisi urutan perintah siap pakai.
4. **Stage 4 — Bidirectional Production Handoff**:
   - Menyuplai resep terverifikasi secara otomatis ke `filmmaking-videography-photography-s2` saat memulai praproduksi atau menjawab kebutuhan efek visual baru di tengah produksi.

---

## 4. Arsitektur Integrasi 16 Server MCP (ArtCraft & Blender 5.2+)

![ArtCraft & Blender 5.2+ MCP Pipeline](./assets/artcraft_blender_pipeline.png)

Kedua *skill* utama dirancang untuk mengorkestrasi 15 aplikasi lokal **ArtCraft Suite** dan **Blender 5.2+ LTS MCP** secara berurutan:

| Tahap Produksi | Server MCP | Format Proyek / Ekspor | Peran Teknis dalam Alur Kerja |
| :--- | :--- | :--- | :--- |
| **1. Pengembangan & Praproduksi** | `craft_anything`, `wordcraft`, `gridcraft`, `deckcraft` | `.docx`, `.md`, `.xlsx`, `.pptx` | Pembuatan *creative brief*, naskah Fountain & AV Script, *Shot List*, jadwal *Stripboard*, rincian anggaran, dan *Pitch Deck*. |
| **2. Desain Visual & 3D Previz** | `designcraft`, `figcraft`, `vectorcraft`, `cadcraft`, `solidcraft`, `blender` | `.svg`, `.png`, `.blend` | Pembuatan panel *storyboard*, aset tipografi kinetik/HUD, konstruksi set 3D, serta simulasi kamera dan pencahayaan fisik di Blender (`127.0.0.1:9876`). |
| **3. Fotografi & Laboratorium Warna** | `photocraft`, `lightcraft` | `.png`, `.jpg`, `.tiff`, `.cube` | Pemrosesan RAW, *retouching* *frequency separation*, pembuatan *lut* warna 4-Node, simulasi *halation/grain*, dan desain *thumbnail* rasio klik (CTR) tinggi. |
| **4. Pascaproduksi & Mastering** | `filmcraft`, `effectcraft`, `soundcraft`, `pdfcraft` | `.fcproj`, `.ecproj`, `.soundcraft`, `.mp4`, `.wav`, `.pdf` | Penyuntingan *timeline* multi-trek, komposisi VFX & *speed-ramping*, *mixing/mastering* audio `-14 LUFS` / `-24 LKFS`, dan pencetakan buku produksi PDF. |

---

## 5. Mode Eksekusi Kru Produksi (Single-Bot vs Multi-Bot Crew)

Sistem mendukung dua topologi eksekusi yang diatur di dalam [`references/single-vs-multibot-crew-roles.md`](./skills/filmmaking-videography-photography-s2/references/single-vs-multibot-crew-roles.md):

1. **Mode A — Single-Bot "One-Man Studio"**:
   - Satu agen menjalankan seluruh **8 peran departemen film** secara berurutan (*Showrunner, Screenwriter, Director, Director of Photography / Master Photographer, Production Designer, Lead Editor, Colorist & VFX Artist, Sound Designer*) dengan melewati gerbang kendali mutu (*Quality Gates*) di setiap pergantian fase.
2. **Mode B — Multi-Bot Studio Crew (5 Spesialis Paralel)**:
   - Mendistribusikan beban kerja secara paralel ke 5 agen spesialis:
     - **Director & Showrunner (`shizuka`)**: Mengarahkan visi kreatif, struktur dramatis, psikologi adegan, dan persetujuan akhir (*final cut*).
     - **DP, Master Photographer, Art Director & Colorist (`kiki-chii`)**: Merancang komposisi lensa, skema pencahayaan, *color grading*, fotografi, dan eksplorasi tren visual.
     - **Technical Director, Lead Editor, VFX/3D & Sound Engineer (`shikaku`)**: Mengelola integrasi MCP, perakitan *timeline* `.fcproj`, *compositing* `.ecproj`, *rigging* 3D Blender, *mastering* audio `.soundcraft`, dan pengujian kotak pasir *app update*.
     - **Screenwriter, Researcher & Archivist (`val`)**: Menyusun riset dokumenter, penulisan naskah Fountain/AV, dan dokumentasi `curiosity_ledger/`.
     - **Executive / Line Producer & 1st AD (`yukino`)**: Mengatur jadwal produksi, *shot list*, anggaran di `gridcraft`, dan kelancaran alur kerja antar-departemen.

---

## 6. Katalog Lengkap 47 Skills di Dalam Repositori

Seluruh *skill* berada di dalam direktori [`skills/`](./skills/) dan mengikuti spesifikasi YAML frontmatter standar:

| Kategori | Daftar Skill (`skills/<nama-skill>/`) |
| :--- | :--- |
| **Filmmaking, Videography & Photography (2)** | `filmmaking-videography-photography-s2`, `auto-curiousity-for-film-making` |
| **AI Research & Deep Learning Lifecycle (14)** | `autoresearch`, `ai-research-explore`, `ai-research-reproduction`, `analyze-project`, `explore-code`, `explore-run`, `paper-context-resolver`, `brainstorming-research-ideas`, `creative-thinking-for-research`, `idea-generation`, `novelty-assessment`, `deep-research`, `literature-review`, `github-research` |
| **Academic Writing, LaTeX & Visualization (8)** | `research-paper-writing`, `paper-writing-section`, `paper-revision`, `rebuttal-writing`, `academic-plotting`, `table-generation`, `slide-generation`, `backward-traceability` |
| **Mathematics, Data Science & Symbolic AI (4)** | `math-reasoning`, `data-analysis`, `symbolic-equation`, `notebooklm-thinking-datascience` |
| **LLM Benchmarking & Observability (5)** | `evaluating-code-models`, `evaluating-llms-harness`, `nemo-evaluator-sdk`, `langsmith-observability`, `phoenix-observability` |
| **Web Intelligence & Firecrawl Suite (5)** | `firecrawl-deep-research`, `firecrawl-research-papers`, `firecrawl-competitive-intel`, `firecrawl-dashboard-reporting`, `firecrawl-knowledge-base` |
| **Productivity, Strategy & Persona Architecture (9)** | `focus-my-energy`, `generate-fresh-ideas`, `get-more-perspectives`, `match-my-writing-style`, `prep-for-meetings`, `prep-for-meetings-2`, `parenting-6d-gad-mdd`, `persona-shizuka-yukino-shikaku`, `chatgpt-hermes-portability-kit` |

---

## 7. Instalasi & Penggunaan

### Opsi A — Instalasi via `npx skills` CLI
```bash
# Menginstal skill S1-S2 MFA Filmmaking
npx skills add <username-github>/<nama-repositori> --skill filmmaking-videography-photography-s2

# Menginstal skill Auto-Curiousity for Film Making
npx skills add <username-github>/<nama-repositori> --skill auto-curiousity-for-film-making
```

### Opsi B — Instalasi Langsung ke Hermes Agent
```powershell
# Salin seluruh 47 skills ke direktori skills Hermes Agent
Copy-Item -Path ".\skills\*" -Destination "D:\HermesData\skills\" -Recurse -Force
```

### Opsi C — Mengunggah Repositori Ini ke Akun GitHub Anda
Jalankan skrip PowerShell otomatis yang sudah disertakan di akar repositori:
```powershell
./push_to_github.ps1 -RepoUrl "https://github.com/<username-github>/<nama-repositori>.git"
```

---

## Lisensi & Kredit

Dirilis di bawah lisensi [MIT License](./LICENSE).
- **Inisiator Konsep & Eksperimen Sistem**: **Muhammad Zidan Aisar (MuZA)**
- **Perancang Arsitektur, Penulis Kurikulum & Engineer Skill**: **Google Gemini**
