"""Eternal-Student Auto-Curiosity Engine: New-App Onboarding, Update Diffing, Recipes & Trend Forecasting."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional


def _now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def ensure_ledger(ledger_dir: Path) -> Dict[str, str]:
    """Initialize the Eternal-Student curiosity_ledger structure non-destructively."""
    ledger_dir.mkdir(parents=True, exist_ok=True)
    sandbox = ledger_dir / "sandbox_tests"
    sandbox.mkdir(parents=True, exist_ok=True)

    defaults: Dict[str, object] = {
        "connected_apps_registry.json": {
            "schema_version": "2.0.0",
            "philosophy": "Eternal Student — learns every newly connected app and every software update safely in sandbox.",
            "apps": {},
        },
        "app_capabilities_snapshot.json": {
            "schema_version": "2.0.0",
            "updated_at": _now_iso(),
            "snapshots": {},
        },
        "tested_recipes_registry.json": {
            "schema_version": "2.0.0",
            "recipes": [],
        },
        "trend_forecasts.json": {
            "schema_version": "2.0.0",
            "methodology": "5-Signal Predictive Horizon (Fatigue Pendulum, Tooling Democratization Lag, Platform Spec Shift, Medium Cross-Pollination, Velocity Score)",
            "forecasts": [],
        },
    }

    created_or_verified: Dict[str, str] = {}
    for filename, payload in defaults.items():
        fpath = ledger_dir / filename
        if not fpath.is_file():
            fpath.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            created_or_verified[filename] = "created"
        else:
            created_or_verified[filename] = "exists"

    for md_name, title in (
        ("app_and_update_learning_log.md", "# Eternal Student — App Onboarding & Update Learning Log\n\n"),
        ("internet_trend_and_forecast_playbook.md", "# Eternal Student — 6-Layer Trend Deconstruction & Forecasts\n\n"),
    ):
        md_path = ledger_dir / md_name
        if not md_path.is_file():
            md_path.write_text(title, encoding="utf-8")
            created_or_verified[md_name] = "created"
        else:
            created_or_verified[md_name] = "exists"

    return {
        "ledger_dir": str(ledger_dir.resolve()),
        "sandbox_dir": str(sandbox.resolve()),
        "files": created_or_verified,
    }


def _probe_binary_output(cmd: List[str], timeout: int = 6) -> str:
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            check=False,
        )
        return (proc.stdout or "").strip()
    except Exception as exc:
        return f"<probe-error: {exc}>"


def onboard_or_check_app(ledger_dir: Path, app_command: str, category: str = "creative-cli") -> Dict[str, object]:
    """Fingerprint a newly connected or updated app, diff against snapshot, and register in Eternal-Student ledger."""
    ensure_ledger(ledger_dir)
    reg_file = ledger_dir / "connected_apps_registry.json"
    snap_file = ledger_dir / "app_capabilities_snapshot.json"

    reg = json.loads(reg_file.read_text(encoding="utf-8"))
    snap = json.loads(snap_file.read_text(encoding="utf-8"))

    resolved = shutil.which(app_command)
    cli_hub_bin = shutil.which("cli-hub")
    harness_cand = shutil.which(f"cli-anything-{app_command}")

    if not resolved and Path(app_command).is_file():
        resolved = str(Path(app_command).resolve())

    version_out = _probe_binary_output([resolved, "--version"]) if resolved else ""
    if resolved and ("unknown" in version_out.lower() or "unrecognized" in version_out.lower() or not version_out):
        version_out = _probe_binary_output([resolved, "-version"])
    help_out = _probe_binary_output([resolved, "--help"]) if resolved else ""

    help_hash = hashlib.sha256(help_out.encode("utf-8", errors="ignore")).hexdigest()[:16] if help_out else None
    prev = snap.get("snapshots", {}).get(app_command)

    if not resolved and not harness_cand:
        status = "not_installed_yet"
    elif prev is None:
        status = "newly_onboarded_app"
    elif prev.get("help_hash") != help_hash or prev.get("version_line") != (version_out.splitlines()[0] if version_out else ""):
        status = "updated_capabilities_detected"
    else:
        status = "unchanged_up_to_date"

    version_line = version_out.splitlines()[0][:200] if version_out else "unknown"
    help_lines = help_out.splitlines() if help_out else []

    app_sandbox = ledger_dir / "sandbox_tests" / Path(app_command).stem
    app_sandbox.mkdir(parents=True, exist_ok=True)

    entry = {
        "app_command": app_command,
        "category": category,
        "binary_path": resolved,
        "cli_anything_harness": harness_cand,
        "cli_hub_available": cli_hub_bin is not None,
        "version_line": version_line,
        "help_line_count": len(help_lines),
        "help_hash": help_hash,
        "supports_json_flag": "--json" in help_out,
        "sandbox_dir": str(app_sandbox),
        "last_checked_at": _now_iso(),
        "status": status,
        "next_eternal_student_step": (
            f"Run 3-Point Micro-Sandbox Sweep inside {app_sandbox} before using in live production."
            if status in {"newly_onboarded_app", "updated_capabilities_detected"}
            else (
                f"Install via `cli-hub install {app_command}` (if available) or connect native CLI binary."
                if status == "not_installed_yet"
                else "Capabilities verified; ready for advisory & CLI execution."
            )
        ),
    }

    reg.setdefault("apps", {})[app_command] = entry
    snap.setdefault("snapshots", {})[app_command] = {
        "version_line": version_line,
        "help_hash": help_hash,
        "help_line_count": len(help_lines),
        "checked_at": _now_iso(),
    }
    snap["updated_at"] = _now_iso()

    reg_file.write_text(json.dumps(reg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    snap_file.write_text(json.dumps(snap, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return entry


def record_trend_forecast(
    ledger_dir: Path,
    title: str,
    horizon: str,
    confidence: float,
    fatigue_signal: str,
    tooling_signal: str,
    advisory_action: str,
    falsification_check: str,
) -> Dict[str, object]:
    """Store an evidence-backed visual/cinematography trend prediction in trend_forecasts.json."""
    ensure_ledger(ledger_dir)
    fc_file = ledger_dir / "trend_forecasts.json"
    data = json.loads(fc_file.read_text(encoding="utf-8"))
    forecast_id = f"fc_{int(time.time())}_{hashlib.md5(title.encode('utf-8')).hexdigest()[:6]}"
    item = {
        "forecast_id": forecast_id,
        "created_at": _now_iso(),
        "title": title,
        "horizon": horizon,
        "confidence_score": round(max(0.0, min(1.0, confidence)), 2),
        "signals": {
            "audience_fatigue_pendulum": fatigue_signal,
            "software_democratization_lag": tooling_signal,
        },
        "creator_advisory_action": advisory_action,
        "falsification_criteria": falsification_check,
        "status": "active_hypothesis",
    }
    data.setdefault("forecasts", []).append(item)
    fc_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return item


def list_ledger_summary(ledger_dir: Path) -> Dict[str, object]:
    ensure_ledger(ledger_dir)
    reg = json.loads((ledger_dir / "connected_apps_registry.json").read_text(encoding="utf-8"))
    rec = json.loads((ledger_dir / "tested_recipes_registry.json").read_text(encoding="utf-8"))
    fc = json.loads((ledger_dir / "trend_forecasts.json").read_text(encoding="utf-8"))
    return {
        "ledger_dir": str(ledger_dir.resolve()),
        "connected_apps_count": len(reg.get("apps", {})),
        "connected_apps": list(reg.get("apps", {}).keys()),
        "verified_recipes_count": len(rec.get("recipes", [])),
        "trend_forecasts_count": len(fc.get("forecasts", [])),
        "latest_forecasts": fc.get("forecasts", [])[-5:],
    }


def discover_skill_synergy_mesh(skills_root: Optional[Path] = None) -> Dict[str, object]:
    """Dynamically index all peer skills (bundled 48 + any external installed skills) for cross-skill synergy."""
    if skills_root is None:
        # Default to repository's skills/ folder
        repo_skills = Path(__file__).resolve().parents[4] / "skills"
        skills_root = repo_skills

    skills_found: List[Dict[str, str]] = []
    if skills_root.is_dir():
        for child in sorted(skills_root.iterdir(), key=lambda p: p.name.lower()):
            skill_md = child / "SKILL.md"
            if skill_md.is_file():
                desc = ""
                try:
                    for line in skill_md.read_text(encoding="utf-8", errors="replace").splitlines()[:15]:
                        if line.lower().startswith("description:"):
                            desc = line.split(":", 1)[1].strip().strip('"').strip("'")
                            break
                except OSError:
                    pass
                skills_found.append(
                    {
                        "name": child.name,
                        "description": desc[:220],
                        "path": str(skill_md),
                    }
                )

    return {
        "skills_root": str(skills_root),
        "total_collaborative_skills": len(skills_found),
        "hub_skills": [
            "auto-curiousity-for-film-making",
            "filmmaking-videography-photography-s2",
            "cli-anything-filmmaking-bridge",
        ],
        "skills": skills_found,
    }
