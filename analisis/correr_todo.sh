#!/usr/bin/env bash
# Reproduce todos los resultados y figuras desde data/.
set -euo pipefail
cd "$(dirname "$0")"
rm -rf resultados figuras
python3 consolidacion_porsche.py
python3 cournot_fusion.py
python3 peru_concentracion.py
