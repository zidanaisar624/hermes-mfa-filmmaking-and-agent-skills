#!/usr/bin/env sh
# ==============================================================================
# TERMINAL AUTO-CHECK & SELF-UPDATE ENGINE (POSIX / LINUX / MACOS / WSL)
# Usage:
#   ./update.sh check
#   ./update.sh update
#   ./update.sh status
# ==============================================================================
set -e

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd || pwd)"
CMD="${1:-update}"
if [ $# -gt 0 ]; then shift; fi

export PYTHONPATH="${SCRIPT_DIR}/agent-harness${PYTHONPATH:+:$PYTHONPATH}"

if command -v python3 >/dev/null 2>&1; then
    exec python3 -m cli_anything.filmmaking_advisor --repo "${SCRIPT_DIR}" "${CMD}" "$@"
elif command -v python >/dev/null 2>&1; then
    exec python -m cli_anything.filmmaking_advisor --repo "${SCRIPT_DIR}" "${CMD}" "$@"
else
    echo "[!] Python 3 is required to run update.sh." >&2
    exit 1
fi
