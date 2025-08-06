"""Business logic for return calculations."""

from __future__ import annotations

from dataclasses import dataclass


def accumulation_factor(return_series: list[float]) -> float:
    """Compute accumulation factor from a list of daily returns.

    Args:
        return_series: list of daily return percentages (e.g., 0.01 for 1%).

    Returns:
        float: accumulated factor.
    """
    factor = 1.0
    for r in return_series:
        factor *= 1 + r
    return factor


@dataclass
class KPI:
    """Simple KPI dataclass."""

    patrimonio: float
    rent_mes: float
    rent_ano: float
