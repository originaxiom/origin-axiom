"""The tau cells tile the band exactly (their areas sum to the band's hyperbolic area 3/8, and their Euclidean areas to
1.5), with the refined census's own 991 points."""
import pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import grid as G

MAIN = [(round(0.05 * i, 4), round(1.0 + 0.05 * k, 4)) for i in range(11) for k in range(61)]
SUB = sorted({(round(0.025 * i, 4), round(1.0 + 0.025 * k, 4)) for i in range(21) for k in range(21)} - set(MAIN))
PTS = MAIN + SUB


def test_the_census_grid():
    assert len(MAIN) == 671 and len(SUB) == 320 and len(PTS) == 991


def test_cells_tile_the_band():
    eu = sum((x1 - x0) * (y1 - y0) for x0, x1, y0, y1 in (G.cell(*p) for p in PTS))
    hy = sum((x1 - x0) * (1 / y0 - 1 / y1) for x0, x1, y0, y1 in (G.cell(*p) for p in PTS))
    assert abs(eu - 0.5 * 3.0) < 1e-9, eu
    assert abs(hy - G.band_area()) < 1e-9, hy


def test_no_overlaps_on_a_fine_sample():
    rng = np.random.default_rng(1); xs = rng.uniform(0, 0.5, 4000); ys = rng.uniform(1, 4, 4000)
    cells = [G.cell(*p) for p in PTS]
    counts = [sum(1 for x0, x1, y0, y1 in cells if x0 <= x < x1 and y0 <= y < y1) for x, y in zip(xs, ys)]
    assert set(counts) == {1}


def test_weights_normalised():
    w = G.area_weights(PTS)
    assert abs(w.sum() - 1) < 1e-12 and (w > 0).all()
