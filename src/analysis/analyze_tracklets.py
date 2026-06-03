"""Command-line entry point for baseline tracklet analysis.

This module is intentionally simple for the initial project scaffold. Future
work should add real statistics, visualizations, and fragmentation diagnostics.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from src.utils.config import load_config
from src.utils.io import load_tracks


def summarize_tracklets(tracks) -> dict[str, int]:
    """Create basic tracklet summary statistics.

    Args:
        tracks: A pandas DataFrame containing tracking rows.

    Returns:
        A dictionary with simple counts.

    TODO:
        Add richer statistics, such as tracklet length histograms, gap counts,
        ID switch candidates, and per-camera summaries.
    """
    if tracks.empty:
        return {"num_rows": 0, "num_tracklets": 0, "num_frames": 0}

    return {
        "num_rows": int(len(tracks)),
        "num_tracklets": int(tracks["track_id"].nunique()),
        "num_frames": int(tracks["frame"].nunique()),
    }


def run_analysis(config_path: Path) -> dict[str, int]:
    """Load tracking data and run placeholder analysis."""
    config = load_config(config_path)
    tracker_output_path = Path(config["data"]["tracker_output_path"])

    tracks = load_tracks(tracker_output_path)
    summary = summarize_tracklets(tracks)

    print("Baseline tracklet analysis summary")
    for key, value in summary.items():
        print(f"- {key}: {value}")

    return summary


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Analyze baseline tracklets.")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/baseline.yaml"),
        help="Path to the baseline YAML config.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the analysis command."""
    args = parse_args()
    run_analysis(args.config)


if __name__ == "__main__":
    main()
