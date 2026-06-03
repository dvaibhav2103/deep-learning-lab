# Method Notes

## Baseline

The baseline is assumed to be a single-camera tracker that outputs one row per
object detection and frame.

## Tracklet Analysis

Initial analysis should inspect:

- Number of tracklets per camera.
- Tracklet length distribution.
- Temporal gaps inside tracklets.
- Spatial jumps between consecutive boxes.
- Candidate fragments that may belong to the same identity.

## Gap Repair

Future repair logic should only fill short and plausible gaps. Possible checks:

- Gap length below a configured threshold.
- Smooth object motion before and after the gap.
- Similar bounding box size.
- No obvious conflict with another active tracklet.

## Conservative Merging

Merging should be intentionally strict. Possible evidence:

- Non-overlapping time ranges or very short temporal gap.
- Spatial continuity.
- Similar motion direction.
- Similar appearance embedding, if available.
- No duplicate identity conflict in the same frame.

## TODO

- Add equations or pseudocode after the first implemented version.
- Record examples of successful and failed repairs.
- Compare conservative and less conservative merge settings.
