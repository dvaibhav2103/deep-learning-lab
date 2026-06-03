#!/usr/bin/env bash
set -euo pipefail

python -m src.evaluation.evaluate_tracking --config configs/postprocess.yaml
