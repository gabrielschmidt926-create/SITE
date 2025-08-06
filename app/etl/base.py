"""ETL adapters."""

from __future__ import annotations

import pandas as pd


class BaseAdapter:
    """Base class for administrator adapters."""

    def fetch_raw(self) -> pd.DataFrame:  # pragma: no cover
        """Fetch raw data. Placeholder."""
        raise NotImplementedError

    def normalize(self, df: pd.DataFrame) -> pd.DataFrame:  # pragma: no cover
        """Normalize raw data."""
        return df
