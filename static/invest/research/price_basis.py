"""Split-only price basis; recorded thesis prices remain immutable."""
from datetime import date
import math


def split_adjusted_price(price, anchor, events, basis_date):
    anchor = date.fromisoformat(anchor)
    basis = date.fromisoformat(basis_date)
    factor = 1.0
    seen = set()
    for event in events:
        day = date.fromisoformat(event["date"])
        ratio = event["ratio"]
        if isinstance(ratio, bool) or not isinstance(ratio, (int, float)) or not math.isfinite(ratio) or ratio <= 0:
            raise ValueError("split ratio must be positive and finite")
        if day in seen or day > basis:
            raise ValueError("duplicate split date or split after price basis")
        seen.add(day)
        if day > anchor:
            factor *= ratio
            if not math.isfinite(factor) or factor <= 0:
                raise ValueError("invalid cumulative split factor")
    result = float(price) / factor
    if not math.isfinite(result) or result <= 0:
        raise ValueError("invalid split-adjusted price")
    return result
