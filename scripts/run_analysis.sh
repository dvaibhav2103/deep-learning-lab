#!/usr/bin/env bash
set -euo pipefail

python -m src.analysis.analyze_tracklets --config configs/baseline.yaml
