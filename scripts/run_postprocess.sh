#!/usr/bin/env bash
set -euo pipefail

python -m src.postprocess.run_postprocess --config configs/postprocess.yaml
