#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

VENV_DIR="$SCRIPT_DIR/../venvs/karel"

if ! [[ -f "${VENV_DIR}/bin/python" ]]
then
  virtualenv -p python3 "${VENV_DIR}"
fi

"${VENV_DIR}/bin/pip" install --upgrade -r "${SCRIPT_DIR}/../common/karel/requirements.txt"

"${VENV_DIR}/bin/python" "${SCRIPT_DIR}/../common/karel/run.py"
