#!/usr/bin/env bash
set -euo pipefail

python -m pip install --disable-pip-version-check -q -r requirements-dev.txt
pytest -q
python -m compileall -q pocket_consumer examples tests
printf '\nClean-environment validation passed.\n'
