#!/usr/bin/env bash
set -e

THIS="$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

PYTHON3="$THIS/.venv/bin/python3"

if [ ! -f "$PYTHON3" ]; then
  PYTHON3=$(which python3)
fi

SOURCE="$THIS/src/"

PYTHONPATH="$PYTHONPATH:$SOURCE" "$PYTHON3" -X utf8 -X faulthandler -BO -m jarklin "$@"
