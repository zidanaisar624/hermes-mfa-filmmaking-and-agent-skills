"""Deterministic S1-S2 (BFA/MFA) Cinematography, Photography & Audio Advisory Calculations.

Note: Synthesized from open film-school curriculum & internet literature as an Advisory Co-Pilot
for human creators — never a replacement for human directors, cinematographers, or editors.
"""

from __future__ import annotations

from typing import Dict


SENSOR_COC_MM: Dict[str, float] = {
    "full_frame": 0.029,
    "aps_c": 0.019,
    "super35": 0.021,
    "mft": 0.015,
    "medium_format": 0.038,
}


def focal_psychology_advisory(focal_mm: float) -> str:
    if focal_mm <= 20:
        return "Ultra-Wide (14-20mm): Expands spatial scale, exaggerates Z-axis motion speed, visceral/existential distortion up close."
    if focal_mm <= 28:
        return "Wide Environmental (24-28mm): Dynamic movement & environmental context while keeping full-body blocking readable."
    if focal_mm <= 42:
        return "Master Wide-Normal (35mm): Quintessential narrative cinema lens — balances room geography with natural facial proportions."
    if focal_mm <= 65:
        return "Standard Human Perspective (50mm): Neutral binocular compression, unforced documentary/slice-of-life intimacy."
    if focal_mm <= 115:
        return "Portrait Telephoto (85-105mm): Flattering facial perspective, background compression, creamy bokeh subject isolation."
    return "Long Telephoto (135mm+): Strong Z-axis background compression, observational/voyeuristic tension or epic isolation."


def compute_optics_and_audio_advisory(
    focal_mm: float = 35.0,
    f_stop: float = 2.8,
    fps: float = 24.0,
    shutter_angle_deg: float = 180.0,
    sensor: str = "full_frame",
    subject_distance_m: float = 2.5,
    ac_mains_hz: int = 50,
    platform: str = "youtube",
    lighting_style: str = "natural_drama",
) -> Dict[str, object]:
    """Return deterministic camera, optical, lighting, and audio mastering recommendations."""
    coc = SENSOR_COC_MM.get(sensor.lower(), 0.029)
    # Shutter speed: t = (shutter_angle / 360) / fps
    shutter_sec = (shutter_angle_deg / 360.0) / max(fps, 1.0)
    denom = round(1.0 / shutter_sec) if shutter_sec > 0 else 48
    flicker_safe = (
        f"1/{ac_mains_hz}s or 1/{ac_mains_hz * 2}s"
        if ac_mains_hz in (50, 60)
        else f"1/{denom}s"
    )

    # Hyperfocal distance H = f^2 / (N * c) + f  (in mm -> convert to m)
    hyperfocal_mm = ((focal_mm ** 2) / (max(f_stop, 0.7) * coc)) + focal_mm
    hyperfocal_m = hyperfocal_mm / 1000.0
    dist_mm = max(subject_distance_m * 1000.0, focal_mm + 1.0)

    near_mm = (hyperfocal_mm * dist_mm) / (hyperfocal_mm + (dist_mm - focal_mm))
    if dist_mm < hyperfocal_mm:
        far_mm = (hyperfocal_mm * dist_mm) / (hyperfocal_mm - (dist_mm - focal_mm))
        far_m: object = round(far_mm / 1000.0, 3)
        total_dof_m: object = round((far_mm - near_mm) / 1000.0, 3)
    else:
        far_m = "infinity"
        total_dof_m = "infinite (from near limit to infinity)"

    lighting_map = {
        "high_key": "2:1 Key-to-Fill (Soft Book-Light / 45-deg bounce + diffusion; warm, calm, beauty/educational).",
        "natural_drama": "4:1 Key-to-Fill (Motivated Key + subtle bounce fill, Rembrandt cheek triangle).",
        "low_key": "8:1 to 16:1 Key-to-Fill (Negative fill black flag, Chiaroscuro/Noir tension, specular rim separation).",
    }

    is_cinema = platform.lower() in {"cinema", "festival", "broadcast", "netflix", "tv"}
    audio_target = {
        "integrated_loudness": "-24.0 LKFS/LUFS (+/- 2.0 LU)" if is_cinema else "-14.0 LUFS (+/- 0.5 LU)",
        "true_peak_max": "-2.0 dBTP" if is_cinema else "-1.0 dBTP",
        "dialogue_peak_dbfs": "-12 to -6 dBFS" if is_cinema else "-6 to -3 dBFS",
        "music_sidechain_ducking": "-3 to -5 dB dynamic EQ ducking in 1kHz-4kHz vocal band",
    }

    return {
        "advisory_role": "Research-Based S1-S2 Filmmaking & Photography Advisor (Human-in-the-Loop Co-Pilot, NOT a replacement for human filmmakers)",
        "camera_and_shutter": {
            "fps": fps,
            "shutter_angle_deg": shutter_angle_deg,
            "ideal_shutter_speed": f"1/{denom}s",
            "mains_flicker_safe_note": f"In {ac_mains_hz}Hz regions, consider {flicker_safe} under non-cinema AC LEDs.",
            "nd_filter_note": "Outdoors, lock 180-deg shutter cadence with Variable/Fixed ND rather than raising shutter speed.",
        },
        "optics_and_dof": {
            "sensor": sensor,
            "circle_of_confusion_mm": coc,
            "focal_length_mm": focal_mm,
            "f_stop": f_stop,
            "subject_distance_m": subject_distance_m,
            "hyperfocal_distance_m": round(hyperfocal_m, 3),
            "dof_near_limit_m": round(near_mm / 1000.0, 3),
            "dof_far_limit_m": far_m,
            "total_dof_m": total_dof_m,
            "psychological_framing_advisory": focal_psychology_advisory(focal_mm),
        },
        "lighting_and_exposure": {
            "recommended_ratio": lighting_map.get(lighting_style.lower(), lighting_map["natural_drama"]),
            "inverse_square_law": "Intensity I ~ 1/d^2 (move softbox closer for rapid background falloff & softer facial wrap).",
            "false_color_ire_targets": {
                "black_clipping_guard": "> 5 IRE",
                "middle_gray_18pct": "38-42 IRE",
                "skin_tones_key_side": "55-70 IRE (Medium/SEA skin ~55-65 IRE; Light skin ~60-70 IRE; Deep skin ~45-55 IRE)",
                "highlight_clipping_guard": "< 95 IRE",
            },
        },
        "editing_murch_rule_of_six": [
            "1. Emotion (51%)",
            "2. Story (23%)",
            "3. Rhythm (10%)",
            "4. Eye-Trace (7%)",
            "5. 2D Plane of Screen (5%)",
            "6. 3D Continuity of Space (4%)",
        ],
        "audio_mastering_target": audio_target,
    }
