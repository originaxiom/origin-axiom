"""STEP B's generator, the one-axis interpolation helpers (data-free): Lagrange weights on three nodes, and the three
coordinates to use around a point (centred where possible)."""
from __future__ import annotations

import numpy as np


def lagrange_weights(x: float, nodes) -> np.ndarray:
    nodes = list(nodes); w = []
    for a in range(3):
        p = 1.0
        for b in range(3):
            if a != b:
                p *= (x - nodes[b]) / (nodes[a] - nodes[b])
        w.append(p)
    return np.array(w)


def axis_nodes(v: float, have: list):
    """the three coordinates of `have` (sorted, existing for the row's choice) to use around v: centred if possible"""
    have = sorted(have)
    i = min(range(len(have)), key=lambda j: abs(have[j] - v))
    if len(have) < 3:
        return None
    if 0 < i < len(have) - 1:
        return have[i - 1], have[i], have[i + 1]
    if i == 0:
        return have[0], have[1], have[2]
    return have[-3], have[-2], have[-1]
