# Experiment Log

## Project Scaffold

The repository structure was created on branch `hakan/project-setup`.

Main folders:

- `src`
- `configs`
- `scripts`
- `docs`
- `results`
- `paper`
- `examples`

This step only prepared the project layout and placeholder code.

## Tracklet Statistics Analysis

Implemented tracking file loading, validation, and
`compute_tracklet_statistics`.

Test input:

```bash
examples/sample_tracks.txt
```

Main output before repair:

- `total_detections`: 11
- `num_tracklets`: 3
- `num_tracklets_with_gaps`: 1
- `total_internal_gaps`: 1
- `mean_tracklet_length`: 3.67

The sample contains one track with an internal frame gap.

## Short-Gap Interpolation

Implemented interpolation for small missing frame gaps inside the same
`track_id`.

Test command:

```bash
python -m src.postprocess.run_postprocess --input examples/sample_tracks.txt --output results/postprocess/sample_repaired.txt --max-gap 5
```

Result:

- original detections: 11
- repaired detections: 13
- interpolated detections: 2

Analysis after repair:

- `total_detections`: 13
- `num_tracklets`: 3
- `num_tracklets_with_gaps`: 0
- `total_internal_gaps`: 0
- `mean_tracklet_length`: 4.33

The synthetic sample gap was removed without changing the number of tracklets.
