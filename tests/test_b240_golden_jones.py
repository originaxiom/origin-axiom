"""B240 locks -- the golden integrality of the figure-eight's colored Jones (object-specific, golden-specific).
Firewall: dimensionless quantum-invariant fact; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B240_golden_jones_integrality" / "golden_jones.py"
_spec = importlib.util.spec_from_file_location("b240_gj", _PATH)
b240 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b240)


def test_golden_integrality():
    pr = b240.products_at_root(5)
    assert b240.is_integer_vector(pr)
    assert [round(p.real) for p in pr] == [1, -2, -2, 1]


def test_J2_is_minus_two_over_phi():
    import cmath
    import numpy as np
    q = cmath.exp(2j * np.pi / 5)
    assert abs(b240.colored_jones_fig8(2, q) - (-2 / b240.PHI)) < 1e-9
    assert abs(b240.colored_jones_fig8(2, q) - (1 - 5 ** 0.5)) < 1e-9


def test_golden_and_amphicheiral_specific():
    import cmath
    import numpy as np
    assert not b240.is_integer_vector(b240.products_at_root(8))    # other root: not integral
    assert not b240.is_integer_vector(b240.products_at_root(13))
    q = cmath.exp(2j * np.pi / 5)
    tref = [b240.qdim(N, 3) * b240.colored_jones_trefoil(N, q) for N in range(1, 5)]
    assert not b240.is_integer_vector(tref)                        # chiral knot: complex -> not integral


# ---- closing sweep: pure-integer is figure-eight-specific, not an amphicheiral-class property ----
_SW = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B240_golden_jones_integrality" / "colored_jones_sweep.py"
_s = importlib.util.spec_from_file_location("b240_sweep", _SW)
sweep = importlib.util.module_from_spec(_s)
_s.loader.exec_module(sweep)


def test_rmatrix_reproduces_habiro_for_fig8():
    import cmath
    import numpy as np
    qH = cmath.exp(2j * np.pi / 5)
    for N in range(1, 5):
        rj = sweep.colored_jones(sweep.AMPHI["4_1"][0], 3, N, sweep.Q10)
        assert abs(rj - sweep.cj_fig8_habiro(N, qH)) < 1e-7


def test_pure_integer_is_figure_eight_specific():
    assert sweep.is_pure_integer(*sweep.AMPHI["4_1"])             # 4_1: pure Z
    for nm in ("6_3", "8_9", "8_18"):                            # others: real but in Z[phi]\Z
        bw, s = sweep.AMPHI[nm]
        a, b, real = sweep.galois_decomp(bw, s, 2)
        assert real and abs(b) > 1e-7
        assert not sweep.is_pure_integer(bw, s)


def test_chiral_controls_not_real():
    for nm in ("3_1", "5_2"):
        bw, s = sweep.CHIRAL[nm]
        _, _, real = sweep.galois_decomp(bw, s, 2)
        assert not real                                          # chiral -> not in the real field Q(sqrt5)
