# Curiosity Ledger Schema & Bidirectional Handoff to `filmmaking-videography-photography-s2`

Use this reference when executing **Stage 5** of `auto-curiousity-for-film-making` to persist Eternal-Student discoveries and connect them seamlessly (`berkesinambungan`) with `filmmaking-videography-photography-s2` and all peer skills.

## 1. Persistent Eternal-Student Knowledge Base (`curiosity_ledger/`)

Initialize or inspect anytime via `hmfa --json curiosity init --ledger ./curiosity_ledger`:

```text
curiosity_ledger/
├── connected_apps_registry.json          # Dynamically onboarded creative apps, versions, CLI-Anything harnesses & sandbox paths
├── app_capabilities_snapshot.json        # Version & --help hashes to detect updates across any connected app
├── app_and_update_learning_log.md        # Human-readable log of newly learned apps, updates & 3-point sandbox sweeps
├── internet_trend_and_forecast_playbook.md # 6-Layer deconstructed trends + 5-Signal horizon analyses
├── tested_recipes_registry.json          # Verified Cinematic Recipe Cards ready for filmmaking-videography-photography-s2
├── trend_forecasts.json                  # Predicted 1-12 month trends with confidence scores & falsification criteria
└── sandbox_tests/                        # Isolated 2-second test clips, 16-bit test frames & parameter sweeps (never live files)
```

---

## 2. Standardized Cinematic Recipe Card Schema (`tested_recipes_registry.json`)

Every verified app capability or deconstructed/predicted trend is stored as a portable, zero-MCP-ready **Recipe Card**:

```json
{
  "recipe_id": "trend_warm_halation_booklight_intro",
  "title": "Warm 35mm Halation + Soft Book-Light Retention Hook",
  "source_type": "hybrid_trend_and_app_update",
  "energy_tier": "Tier 1 (Calm / Intimate) or Tier 2 (Balanced Narrative)",
  "target_formats": ["youtube_16_9", "shorts_9_16", "short_film"],
  "deconstruction_6_layers": {
    "pacing_asl_sec": 3.8,
    "j_cut_lead_frames": 8,
    "lens_mm": 35,
    "shutter_angle_deg": 180,
    "lighting_ratio": "2:1 Book Light (3400K Key + 4800K Soft Fill, Skin at 62 IRE)",
    "color_recipe": "Film print curve + 4px Red-Orange Edge Halation + 8% Highlight Bloom",
    "vfx_motion": "Slow 1.00x to 1.06x cubic-bezier(0.22, 1.0, 0.36, 1.0) push-in over 3.8s",
    "audio_master": "-14.0 LUFS dialogue, -28 LUFS room tone, -4dB sidechain ducking at 2.5kHz"
  },
  "zero_mcp_cli_execution": {
    "optics_check": "hmfa --json optics --focal-mm 35 --f-stop 2.0 --fps 24 --lighting high_key",
    "blender_previz": "cli-anything-blender / blender --background: 35mm DOF F/2.0, 45-deg bounce Area Light",
    "photo_color": "darktable-cli / cli-anything-gimp / lightcraft-cli: Halation r=4.0, Skin IRE=62",
    "nle_timeline": "cli-anything-kdenlive / ffmpeg / filmcraft-cli: 8-frame J-cut audio lead + cubic-bezier push-in",
    "audio_master": "cli-anything-audacity / ffmpeg loudnorm=I=-14:TP=-1.0 / soundcraft-cli"
  },
  "sandbox_verified": true,
  "advisory_notes": "Tested in sandbox_tests/; zero highlight clipping and preserves clean caption legibility."
}
```

---

## 3. Bidirectional Continuity Loop (`Eternal Student` <-> `Filmmaking Advisor`)

```text
[auto-curiousity-for-film-making]                      [filmmaking-videography-photography-s2]
  1. Onboards new apps & tests app updates     --->      Advises creator with verified CLI parameters
  2. Deconstructs & predicts visual trends     --->      Offers optional Recipe Cards & Early-Mover insights
  3. Collaborates across all 48+ peer skills   <---      Escalates novel creative/technical R&D questions
```

### Execution Across Single-Agent vs. Multi-Bot Topologies

- **Mode A — Single-Agent Advisor (Hermes, OpenClaw, ChatGPT, Claude, Codex)**:
  1. **Pre-Advisory Check**: Inspects `curiosity_ledger/` (and runs `hmfa preflight` if local execution is requested) before advising across the 8 film-school department lenses.
  2. **Post-Session Learning**: Logs any newly connected tool, discovered parameter sweet spot, or trend insight back into `curiosity_ledger/`.
- **Mode B — Multi-Bot Advisory Crew (e.g., 5 Specialist Profiles)**:
  - **Visual / DP Bot (`kiki-chii`)**: Leads visual trend scouting, color/photography tests, and creative remixing (`creative-thinking-for-research`, `novelty-assessment`).
  - **Technical / Post Bot (`shikaku`)**: Leads `hmfa curiosity onboard-app`, CLI-Anything harness checks, 3-point sandbox sweeps, and `ffmpeg`/Blender benchmarks.
  - **Director Bot (`shizuka`)**: Filters discovered tools and predicted trends through **Walter Murch's 51% Emotion rule** so advice always serves human story truth.
  - **Research / Story Bot (`val`)**: Coordinates `deep-research`, `literature-review`, and `data-analysis` to document `curiosity_ledger/` logs and trend forecasts.
  - **Producer / Pace Bot (`yukino`)**: Paces R&D in calm, low-cognitive-load micro-steps (`focus-my-energy`) so continuous learning stays restorative and enjoyable.
