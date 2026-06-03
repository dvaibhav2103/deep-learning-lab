"""Command-line entry point for tracklet post-processing."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.postprocess.merge import conservative_merge
from src.postprocess.repair import repair_short_gaps
from src.utils.config import load_config
from src.utils.io import load_tracks, save_tracks


def run_postprocess(config_path: Path) -> None:
    """Run the placeholder repair and merge pipeline."""
    config = load_config(config_path)

    input_path = Path(config["data"]["input_tracks_path"])
    output_path = Path(config["data"]["output_tracks_path"])

    tracks = load_tracks(input_path)

    if config["repair"]["enabled"]:
        tracks = repair_short_gaps(
            tracks,
            max_gap_frames=int(config["repair"]["max_gap_frames"]),
        )

    if config["merge"]["enabled"]:
        tracks = conservative_merge(
            tracks,
            min_similarity_score=float(config["merge"]["min_similarity_score"]),
        )

    save_tracks(tracks, output_path)
    print(f"Saved post-processed tracks to {output_path}")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run tracklet post-processing.")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/postprocess.yaml"),
        help="Path to the post-processing YAML config.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the post-processing command."""
    args = parse_args()
    run_postprocess(args.config)


if __name__ == "__main__":
    main()
