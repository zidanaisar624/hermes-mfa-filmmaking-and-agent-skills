"""Unit tests for cli_anything.filmmaking_advisor core modules."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

_HARNESS_ROOT = Path(__file__).resolve().parents[3]
if str(_HARNESS_ROOT) not in sys.path:
    sys.path.insert(0, str(_HARNESS_ROOT))

from cli_anything.filmmaking_advisor.core.advisor_optics import compute_optics_and_audio_advisory
from cli_anything.filmmaking_advisor.core.curiosity_engine import (
    discover_skill_synergy_mesh,
    ensure_ledger,
    onboard_or_check_app,
    record_trend_forecast,
)
from cli_anything.filmmaking_advisor.core.discovery import is_hermes_home, preflight_creative_toolchain


class TestFilmmakingAdvisorHarness(unittest.TestCase):
    def test_optics_180_shutter_and_lufs(self) -> None:
        res = compute_optics_and_audio_advisory(focal_mm=35, f_stop=2.0, fps=24, platform="youtube")
        self.assertIn("NOT a replacement for human filmmakers", str(res["advisory_role"]))
        self.assertEqual(res["camera_and_shutter"]["ideal_shutter_speed"], "1/48s")
        self.assertIn("-14.0 LUFS", res["audio_mastering_target"]["integrated_loudness"])
        self.assertGreater(res["optics_and_dof"]["hyperfocal_distance_m"], 20.0)

    def test_hermes_signature_detection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "CustomHermesDrive"
            (root / "skills").mkdir(parents=True)
            (root / "config.yaml").write_text("model: locked\n", encoding="utf-8")
            self.assertTrue(is_hermes_home(root))

    def test_eternal_student_ledger_and_forecast(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp) / "curiosity_ledger"
            ensure_ledger(ledger)
            app_info = onboard_or_check_app(ledger, "python")
            self.assertEqual(app_info["status"], "newly_onboarded_app")
            app_info_2 = onboard_or_check_app(ledger, "python")
            self.assertEqual(app_info_2["status"], "unchanged_up_to_date")

            fc = record_trend_forecast(
                ledger_dir=ledger,
                title="Tactile Imperfection & Natural Halation Resurgence",
                horizon="3-6 months",
                confidence=0.81,
                fatigue_signal="Viewer habituation to hyper-cut 1s AI captions",
                tooling_signal="Open-source physical halation & AgX nodes landing in Blender/CLI tools",
                advisory_action="Pair 35mm 4-6s pacing with subtle edge halation and genuine room tone",
                falsification_check="Track ASL & color palette of top 50 Vimeo/YouTube narrative essays",
            )
            self.assertEqual(fc["confidence_score"], 0.81)
            stored = json.loads((ledger / "trend_forecasts.json").read_text(encoding="utf-8"))
            self.assertEqual(len(stored["forecasts"]), 1)

    def test_preflight_and_skill_mesh(self) -> None:
        pre = preflight_creative_toolchain()
        self.assertIn("cli_anything_harnesses", pre)
        mesh = discover_skill_synergy_mesh()
        self.assertGreaterEqual(mesh["total_collaborative_skills"], 47)


if __name__ == "__main__":
    unittest.main()
