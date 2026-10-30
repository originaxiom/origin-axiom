"""STEP B's generator, the grid's interpolation stencils (data-free).  Per node of the census grid: the 3 x 3 stencil's node
indices (row-major over (x, y)) -- per axis the three existing coordinates nearest the node, centred where possible,
one-sided at the band's edges and the sub-block's border -- and its biquadratic Lagrange weights.  The cells (grid.cell)
lie inside their stencils' ranges.  The search and its bounds are cells.py's (the Bernstein enclosure replaced the W x rho
bound of the fourth review's version, 2026-10-30)."""
from __future__ import annotations

import numpy as np

import grid as G
from interp import axis_nodes, lagrange_weights


class GridStencils:
    """per node of the grid: the 3 x 3 stencil's node indices (row-major over (x, y)) or None"""

    def __init__(self, points):
        self.pts = [(round(float(a), 4), round(float(b), 4)) for a, b in points]
        self.idx = {p: i for i, p in enumerate(self.pts)}
        self.st = []
        for (x, y) in self.pts:
            nx = axis_nodes(x, [a for (a, b) in self.pts if abs(b - y) < 1e-9])
            # the y-stencil stays on its cell's side of the sub-block's border (grid.cell: the border row Im = 1.5 owns the half
            # step below it, the main row at 1.55 reaches down to it), so the nine nodes exist and the cell lies in range
            side = (lambda b: b <= G.SUB_IM[1] + 1e-9) if y <= G.SUB_IM[1] + 1e-9 else (lambda b: b >= G.SUB_IM[1] - 1e-9)
            ny = axis_nodes(y, [b for (a, b) in self.pts if abs(a - x) < 1e-9 and side(b)])
            if nx is None or ny is None or any((a, b) not in self.idx for a in nx for b in ny):
                self.st.append(None); continue
            self.st.append((nx, ny, [self.idx[(a, b)] for a in nx for b in ny]))

    def weights(self, i, x, y):
        nx, ny, _ = self.st[i]
        wx, wy = lagrange_weights(x, nx), lagrange_weights(y, ny)
        return np.outer(wx, wy).ravel()
