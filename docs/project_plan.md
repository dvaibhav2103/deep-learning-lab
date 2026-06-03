# Project Plan

## Title

Tracklet Repair and Conservative Merging for More Stable Single-Camera Tracking

## Motivation

Single-camera tracking quality strongly affects the later multi-camera
association stage. Fragmented tracklets and avoidable ID switches can create
noisy identity candidates across cameras.

## Main Questions

- Which tracking failures appear most often in the baseline output?
- Can short gaps be repaired without introducing many false links?
- Can fragmented tracklets be merged conservatively enough to improve stability?
- Which metrics best capture the improvement for this project?

## Milestones

1. Prepare data loading and baseline analysis.
2. Measure tracklet fragmentation and simple consistency statistics.
3. Implement short-gap repair.
4. Implement conservative merging.
5. Evaluate baseline versus repaired outputs.
6. Write final report and summarize limitations.

## Risks

- Over-aggressive merging may create identity errors.
- Missing appearance embeddings may limit reliable merge decisions.
- Improvements in simple statistics may not always improve standard MOT metrics.

## TODO

- Decide final dataset and file format.
- Add dataset-specific notes.
- Define the exact evaluation protocol with the lab supervisor.
