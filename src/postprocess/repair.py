"""Placeholder logic for repairing fragmented tracklets."""

from __future__ import annotations

import pandas as pd


def repair_short_gaps(tracks: pd.DataFrame, max_gap_frames: int) -> pd.DataFrame:
    """Repair short gaps inside otherwise plausible tracklets.

    Args:
        tracks: Tracking output as a DataFrame.
        max_gap_frames: Maximum gap length that may be considered repairable.

    Returns:
        A copy of the input tracks. No repair is implemented yet.

    TODO:
        Interpolate missing boxes for short gaps when motion and confidence
        constraints indicate that the same object was temporarily lost.
    """
    _ = max_gap_frames
    return tracks.copy()
