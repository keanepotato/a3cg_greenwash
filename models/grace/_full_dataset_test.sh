#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./run_ate_asc.sh /abs/path/to/ate_asc_run_config.json
#
# If you want it hardcoded, replace "${1:?...}" with the actual path and remove the usage check.

CONFIG_PATH="configs/aspect_action/full_test.json"
PYTHON_BIN="${PYTHON_BIN:-python3}"

# Resolve script directory and call the Python file that lives next to it
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PY_FILE="${SCRIPT_DIR}/ate_asc_run.py"   # <-- rename to the actual filename

# Run: we only set the config path; everything else comes from the JSON
exec "${PYTHON_BIN}" "${PY_FILE}" --config_path "${CONFIG_PATH}"
