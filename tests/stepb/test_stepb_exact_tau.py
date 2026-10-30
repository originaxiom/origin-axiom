"""The grid's stencils (exact_tau.GridStencils): almost every node has a full 3 x 3 stencil, and every cell lies inside its
stencil's range (grid.cell's retiling: no extrapolation)."""
import pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import grid as G
from exact_tau import GridStencils
from synth import PTS


def test_stencils_exist_and_contain_their_cells():
    gs = GridStencils(PTS); n_none = sum(1 for x in gs.st if x is None)
    assert n_none == 0, n_none
    for i, p in enumerate(gs.pts):
        nx, ny, idx = gs.st[i]
        x0, x1, y0, y1 = G.cell(*p)
        assert min(nx) - 1e-12 <= x0 and x1 <= max(nx) + 1e-12 and min(ny) - 1e-12 <= y0 and y1 <= max(ny) + 1e-12, (p, nx, ny)
        assert i in idx


def test_weights_reproduce_quadratics():
    gs = GridStencils(PTS); rng = np.random.default_rng(0)
    for i in rng.choice(len(PTS), 50, replace=False):
        nx, ny, idx = gs.st[int(i)]; x0, x1, y0, y1 = G.cell(*gs.pts[int(i)])
        f = lambda x, y: 1 + 2 * x - 3 * y + x * y + 5 * x * x * y * y - y * y
        vals = np.array([f(*gs.pts[j]) for j in idx])
        for x, y in ((x0, y0), (x1, y1), (0.5 * (x0 + x1), y1)):
            assert abs(gs.weights(int(i), x, y) @ vals - f(x, y)) < 1e-9
