"""B1932, a regression lock (2026-11-18): fiber_grid_t90 replaces B1924's channel norm for the whole process when it is
imported. Outside fbar_t90 the replacement must change nothing. On a clean clone it had raised a TypeError in other
arcs' tests that ran after it in one worker (the fresh-clone suite of Review 84: 29 failures, most of them this)."""
import pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fiber_grid_t90 as G

T = complex(0.13, 1.5)


def _plain_frame(t, a, b):
    L = G.CR.canon(t); L.pop("_extrapolated")
    return {k: np.array(v) for k, v in G.C.frame(t, a, b, L).items() if "conjS" not in k and "L_2" in k}


def test_outside_its_function_the_replacement_is_the_original():
    assert G.L2_NOW[0] is None and G.Bm.cA is G.cA_t90
    a, b = G.FG.POINTS[0]; got = _plain_frame(T, a, b)
    G.Bm.cA = G.FAST
    try: want = _plain_frame(T, a, b)
    finally: G.Bm.cA = G.cA_t90
    assert all(np.array_equal(got[k], want[k]) for k in want)


def test_inside_it_the_exact_weight_acts_and_is_switched_off_after():
    exact = {k: np.array(v) for k, v in G.fbar_t90(T).items()}
    assert G.L2_NOW[0] is None                                                  # switched off again
    plain = None
    for a, b in G.FG.POINTS:
        o = _plain_frame(T, a, b); plain = {k: v / len(G.FG.POINTS) for k, v in o.items()} if plain is None else {k: plain[k] + o[k] / len(G.FG.POINTS) for k in plain}
    assert max(float(np.max(np.abs(exact[k] - plain[k]))) for k in plain) > 1e-9   # the control: the exact weight is not a no-op
