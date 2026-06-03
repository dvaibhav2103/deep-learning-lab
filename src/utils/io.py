"""Input and output helpers for tracking files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


TRACK_COLUMNS = ["frame", "track_id", "x", "y", "w", "h", "score", "camera_id"]


def load_tracks(path: Path) -> pd.DataFrame:
    """Load tracking data from a CSV file.

    Args:
        path: Path to a CSV tracking file.

    Returns:
        A pandas DataFrame with the expected tracking columns. If the file does
        not exist yet, an empty DataFrame is returned so starter scripts remain
        runnable before data is added.

    TODO:
        Add support for MOTChallenge text files and stricter schema validation.
    """
    if not path.exists():
        print(f"Warning: tracking file not found, returning empty data: {path}")
        return pd.DataFrame(columns=TRACK_COLUMNS)

    tracks = pd.read_csv(path)
    missing_columns = [column for column in TRACK_COLUMNS if column not in tracks.columns]
    if missing_columns:
        raise ValueError(f"Missing required tracking columns in {path}: {missing_columns}")

    return tracks


def save_tracks(tracks: pd.DataFrame, path: Path) -> None:
    """Save tracking data to a CSV file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tracks.to_csv(path, index=False)
