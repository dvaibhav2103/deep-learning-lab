"""Placeholder logic for conservative tracklet merging."""

from __future__ import annotations

import pandas as pd


def conservative_merge(tracks: pd.DataFrame, min_similarity_score: float) -> pd.DataFrame:
    """Merge tracklets only when the evidence is strong.

    Args:
        tracks: Tracking output as a DataFrame.
        min_similarity_score: Required similarity score for a future merge.

    Returns:
        A copy of the input tracks. No merging is implemented yet.

    TODO:
        Combine temporal, spatial, appearance, and camera-specific constraints
        into a conservative merge decision.
    """
    _ = min_similarity_score
    return tracks.copy()
