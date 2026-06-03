"""Command-line entry point for tracklet post-processing."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.postprocess.repair import interpolate_track_gaps
from src.utils.io import load_tracking_file, save_tracking_file


def run_postprocess(input_path: Path, output_path: Path, max_gap: int) -> None:
    """Run short-gap interpolation and save the repaired tracks."""
    tracks = load_tracking_file(str(input_path))
    repaired_tracks = interpolate_track_gaps(tracks, max_gap=max_gap)

    save_tracking_file(repaired_tracks, str(output_path))

    num_interpolated = int(repaired_tracks["is_interpolated"].sum())
    print(f"original detections: {len(tracks)}")
    print(f"repaired detections: {len(repaired_tracks)}")
    print(f"interpolated detections: {num_interpolated}")
    print(f"saved repaired tracks to {output_path}")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run tracklet post-processing.")
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to a comma-separated tracking text file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Path where the repaired tracking file should be saved.",
    )
    parser.add_argument(
        "--max-gap",
        type=int,
        default=5,
        help="Maximum number of missing frames to interpolate.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the post-processing command."""
    args = parse_args()
    run_postprocess(args.input, args.output, args.max_gap)


if __name__ == "__main__":
    main()
