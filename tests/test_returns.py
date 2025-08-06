"""Tests for return calculations."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.services.returns import accumulation_factor


def test_accumulation_factor():
    series = [0.01, -0.02, 0.03]
    assert round(accumulation_factor(series), 6) == round((1.01 * 0.98 * 1.03), 6)
