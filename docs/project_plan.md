# Project Plan

## Title

Tracklet Fragmentation Analysis and Repair for Single-Camera Tracking

## Motivation

Single-camera tracking quality strongly affects the later multi-camera
association stage. Fragmented tracklets and avoidable ID switches can create
noisy identity candidates across cameras.

## Current Contribution

This project currently provides a lightweight post-processing pipeline for
single-camera tracking outputs, starting with tracklet analysis and short-gap
interpolation.

The implemented result is verified on a synthetic sample. No improvement on real
tracking data is claimed yet.

## Main Questions

- Which tracking failures appear most often in the baseline output?
- Can short gaps be repaired without introducing many false links?
- Can fragmented tracklets be merged conservatively enough to improve stability?
- Which metrics best capture the improvement for this project?

## Completed Work

- Created the project scaffold on branch `hakan/project-setup`.
- Added MOT-style tracking file loading and validation.
- Added basic tracklet statistics.
- Added short-gap interpolation for internal gaps within the same `track_id`.

## Planned Next Steps

1. Conservative tracklet merging.
2. Baseline vs repaired comparison script.
3. Visual failure-case examples.
4. Real BoT-SORT output or project dataset integration.
5. Final evaluation tables for paper and presentation.

## Risks

- Over-aggressive merging may create identity errors.
- Missing appearance embeddings may limit reliable merge decisions.
- Improvements in simple statistics may not always improve standard MOT metrics.

## TODO

- Decide final dataset and file format.
- Add dataset-specific notes.
- Define the exact evaluation protocol with the lab supervisor.
