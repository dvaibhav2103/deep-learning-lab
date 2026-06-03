#!/usr/bin/env bash
set -euo pipefail

python -m src.postprocess.run_postprocess \
  --input examples/sample_fragmented_tracks.txt \
  --output results/postprocess/fragmented_repaired.txt \
  --max-gap 5 \
  --enable-merge \
  --max-merge-gap 5 \
  --max-center-distance 80 \
  --max-size-ratio 1.5
