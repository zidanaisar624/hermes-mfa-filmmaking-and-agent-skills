from pathlib import Path
from setuptools import setup, find_namespace_packages

ROOT = Path(__file__).resolve().parent
VERSION_FILE = ROOT.parent / "VERSION"
VERSION = VERSION_FILE.read_text(encoding="utf-8").strip() if VERSION_FILE.is_file() else "2.0.0"

setup(
    name="cli-anything-filmmaking-advisor",
    version=VERSION,
    description=(
        "CLI-Anything compatible zero-MCP-token harness for S1-S2 Filmmaking & Photography "
        "Advisory, Eternal-Student Auto-Curiosity, Multi-Agent Auto-Discovery, and Terminal Self-Update."
    ),
    long_description=(ROOT / "FILMMAKING_ADVISOR.md").read_text(encoding="utf-8")
    if (ROOT / "FILMMAKING_ADVISOR.md").is_file()
    else "",
    long_description_content_type="text/markdown",
    author="Muhammad Zidan Aisar (MuZA) & Google Gemini",
    url="https://github.com/zidanaisar624/hermes-mfa-filmmaking-and-agent-skills",
    license="MIT",
    python_requires=">=3.8",
    packages=find_namespace_packages(include=["cli_anything.*"]),
    install_requires=[],
    extras_require={
        "click": ["click>=8.0"],
    },
    entry_points={
        "console_scripts": [
            "cli-anything-filmmaking=cli_anything.filmmaking_advisor.filmmaking_advisor_cli:main",
            "hmfa=cli_anything.filmmaking_advisor.filmmaking_advisor_cli:main",
            "hermes-filmmaking=cli_anything.filmmaking_advisor.filmmaking_advisor_cli:main",
        ],
    },
)
