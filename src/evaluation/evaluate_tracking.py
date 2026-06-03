"""Command-line entry point for tracking evaluation.

The full metric implementation is intentionally left as future work. This file
keeps the expected interface visible from the start of the project.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from src.utils.config import load_config
from src.utils.io import load_tracks


def compute_placeholder_metrics(num_predictions: int, num_ground_truth: int) -> dict[str, float]:
    """Compute simple placeholder metrics.

    Args:
        num_predictions: Number of predicted tracking rows.
        num_ground_truth: Number of ground-truth rows.

    Returns:
        A dictionary with basic counts.

    TODO:
        Replace this with MOT metrics such as MOTA, IDF1, HOTA, ID switches,
        false positives, and false negatives.
    """
    return {
        "num_predictions": float(num_predictions),
        "num_ground_truth": float(num_ground_truth),
    }


def run_evaluation(config_path: Path) -> dict[str, float]:
    """Load predictions and ground truth, then compute placeholder metrics."""
    config = load_config(config_path)

    predictions = load_tracks(Path(config["data"]["input_tracks_path"]))
    ground_truth = load_tracks(Path(config["data"].get("ground_truth_path", "data/ground_truth.csv")))

    metrics = compute_placeholder_metrics(
        num_predictions=len(predictions),
        num_ground_truth=len(ground_truth),
    )

    print("Evaluation summary")
    for key, value in metrics.items():
        print(f"- {key}: {value}")

    return metrics


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Evaluate tracking outputs.")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/postprocess.yaml"),
        help="Path to a YAML config containing prediction and ground-truth paths.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the evaluation command."""
    args = parse_args()
    run_evaluation(args.config)


if __name__ == "__main__":
    main()
