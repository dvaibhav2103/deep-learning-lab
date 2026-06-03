# Method Notes

## Baseline

The baseline is assumed to be a single-camera tracker that outputs one row per
object detection and frame.

The current input format is a comma-separated MOT-style file:

```text
frame_id, track_id, x, y, width, height, score, class_id
```

## Current Pipeline

1. Load MOT-style tracking output.
2. Compute tracklet-level statistics.
3. Detect small internal gaps inside each `track_id`.
4. Fill short gaps with linear interpolation of `x`, `y`, `width`, and `height`.
5. Save repaired tracking output in the same standard format.

## Tracklet Analysis

The analysis currently reports simple counts and gap statistics:

- Number of detections and tracklets.
- Tracklet length summary.
- Number of tracklets with internal frame gaps.
- Total internal gap count.
- Per-class tracklet counts.

The current result is verified on a small synthetic sample, not on real tracker
output yet.

## Short-Gap Interpolation

For each `track_id`, the repair step checks consecutive detections. If the
number of missing frames is at most `max_gap`, it creates interpolated detections
between the two boxes.

Interpolated fields:

- `x`, `y`, `width`, `height`: linear interpolation.
- `score`: average of the previous and next scores.
- `track_id`, `class_id`: copied from the same track.

This step helps with missed detections or very short occlusions where the same
`track_id` continues later.

It does not solve fragmented identities where the object receives a new
`track_id` after an occlusion.

## Conservative Merging

The next method step is conservative tracklet merging. Merging should be strict
because incorrect merges create identity errors. Possible evidence:

- Non-overlapping time ranges or very short temporal gap.
- Spatial continuity.
- Similar motion direction.
- Similar appearance embedding, if available.
- No duplicate identity conflict in the same frame.

## TODO

- Record examples of successful and failed repairs.
- Implement conservative merging.
- Compare baseline and repaired outputs on real tracking data.
