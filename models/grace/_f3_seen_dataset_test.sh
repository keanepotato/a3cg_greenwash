#!/usr/bin/env bash
set -euo pipefail

CONFIG_PATH="configs/aspect_action/f3_seen_test.json"
PYTHON_BIN="${PYTHON_BIN:-python3}"

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PY_FILE="${SCRIPT_DIR}/ate_asc_run.py"

exec "${PYTHON_BIN}" "${PY_FILE}" --config_path "${CONFIG_PATH}"
