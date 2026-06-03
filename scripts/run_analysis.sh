#!/usr/bin/env bash
set -euo pipefail

python -m src.analysis.analyze_tracklets \
  --input examples/sample_tracks.txt \
  --output results/analysis/sample_stats.json
