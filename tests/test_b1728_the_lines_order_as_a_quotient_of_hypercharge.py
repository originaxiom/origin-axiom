"""B1728 -- the line's order as a quotient of hypercharge (P-296; B1703's law derived), PROVED. Live: the theta shift
identity; the swap's transposes (bil, and Y for both readings, with the control S = 1 failing); the negation identity; the
law's charge arithmetic. Stored: every identity at machine precision and 59 of 59 unmasked sector pairs agreeing with the law."""
import json, pathlib, importlib.util
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1728_the_lines_order_as_a_quotient_of_hypercharge"


def _m():
    spec = importlib.util.spec_from_file_location("b1728_quotient", A / "verification" / "the_quotient.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_identities_live():
    m = _m(); B = m.frame(); t = m.TAU; T = 2 * t; u = 0.01 * np.exp(2j * np.pi * np.arange(8) / 8)
    a, b = 0.37, -0.81
    assert np.max(np.abs(B.thc(a + 2, b - 4, u, T) - np.exp(4j * np.pi * (-2) * a) * B.thc(a, b, u, T))) < 1e-10
    x, y, uu = (0.21, -0.4), (-0.33, 0.7), 0.11 + 0.05j
    assert np.max(np.abs(B.bil(y, x, uu, t) - B.bil(x, y, uu, t).T)) < 1e-12
    assert np.max(np.abs(B.bil((-x[0], -x[1]), (-y[0], -y[1]), uu, t) + B.bil(x, y, -uu, t))) < 1e-10


def test_the_swap_transposes_Y_live():
    m = _m(); B = m.frame(); x, y = (0.21, -0.4), (-0.33, 0.7)
    Mxy, Myx = m.M_of(x, y), m.M_of(y, x)
    assert np.max(np.abs(Myx - Mxy.T)) / np.max(np.abs(Mxy)) < 1e-12
    for S in m.higgs().values():
        Y1, Y2 = B.coupling(S, Mxy), B.coupling(S, Myx)
        assert np.max(np.abs(Y2 - Y1.T)) / np.max(np.abs(Y1)) < 1e-12
    Y1, Y2 = B.coupling(np.eye(2, dtype=complex), Mxy), B.coupling(np.eye(2, dtype=complex), Myx)
    assert np.max(np.abs(Y2 - Y1.T)) / np.max(np.abs(Y1)) > 0.5


def test_the_law_arithmetic():
    m = _m()
    want = {N: {"up=down": N in (1, 2, 3, 6), "down=lep": N in (1, 2, 4, 5), "up=lep": N in (1, 2, 7)} for N in range(1, 13)}
    assert all(m.law(N) == want[N] for N in range(1, 13))


def test_the_stored_output():
    d = json.loads((A / "verification" / "the_quotient.json").read_text(encoding="utf-8"))
    assert d["A"]["thc_shift_identity_max_rel"] < 1e-12 and d["A"]["charge_shift_by_N_ratio_dlog_max"] < 1e-10
    assert max(d["B"][k] for k in ("bil_T", "M_T", "Y_T_S", "Y_T_St", "bil_neg", "M_neg", "Y_neg_S", "Y_neg_St")) < 1e-13
    assert d["B"]["control_S_eq_1"] > 1
    assert d["C"]["unmasked_pairs"] == 59 and d["C"]["agree_with_law"] == 59
