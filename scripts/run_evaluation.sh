#!/usr/bin/env bash
set -euo pipefail

python -m src.evaluation.evaluate_tracking \
  --baseline examples/sample_fragmented_tracks.txt \
  --repaired results/postprocess/fragmented_repaired.txt \
  --output-json results/evaluation/fragmented_comparison.json \
  --output-md results/evaluation/fragmented_comparison.md \
  --short-threshold 10
