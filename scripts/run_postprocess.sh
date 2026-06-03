#!/usr/bin/env bash
set -euo pipefail

python -m src.postprocess.run_postprocess \
  --input examples/sample_tracks.txt \
  --output results/postprocess/sample_repaired.txt \
  --max-gap 5
