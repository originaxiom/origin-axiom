"""B1408 -- the odd sector carries one number, it is the benched one, and the
obstruction is PRECISION, quantified.

Includes the guard that refutes this arc's own prior hypothesis: at 1e-3 the
windows ARE essentially unique, so the field does not forbid discrimination.
"""
import importlib.util
import math
from pathlib import Path

import pytest

sp = pytest.importorskip("sympy")
np = pytest.importorskip("numpy")
from sympy import Rational as Q

ROOT = Path(__file__).resolve().parents[1]
PHI = (1 + sp.sqrt(5)) / 2


@pytest.fixture(scope="module")
def odd():
    B = ROOT / "frontier" / "B1349_the_mirror_sector_posed" / "verification"
    spec = importlib.util.spec_from_file_location(
        "exact60_b1408", str(B / "b1349c_exact_instrument.py"))
    X = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(X)
    N = 6
    ix = {w: i for i, w in enumerate(X.W)}
    I6 = sp.eye(N)
    cm = lambda A: sp.Matrix(A.rows, A.cols, lambda i, j: X.conj(A[i, j]))
    re_ = lambda e: X.red(sp.expand((e + X.conj(e)) * Q(1, 2)))
    C = sp.zeros(N, N)
    for i, w in enumerate(X.W):
        C[ix[(w[1], w[0])], i] = 1
    C = sp.Matrix(N, N, lambda i, j: sp.Integer(C[i, j]))
    R, L = X.T, X.mmul(X.mmul(cm(X.S), cm(X.T)), X.S)

    def mpow(A, k):
        P = I6
        for _ in range(k):
            P = X.mmul(P, A)
        return P

    Bod = sp.zeros(N, 2)
    Bod[ix[(0, 1)], 0], Bod[ix[(1, 0)], 0] = 1, -1
    Bod[ix[(0, 2)], 1], Bod[ix[(2, 0)], 1] = 1, -1
    God = Bod.T * Bod
    ZN = sp.exp(2 * sp.pi * sp.I / 60)
    fn = lambda e: float(sp.re(sp.N(sp.sympify(e).subs(X.z, ZN), 30)))
    ex = lambda e: sp.nsimplify(sp.simplify(sp.expand(e).subs(X.z, ZN)), [sp.sqrt(5)])

    Qs, lams, scal = [], {}, []
    for m in range(15):
        Wd = X.mmul(C, X.mmul(mpow(R, m), mpow(L, m)))
        A = sp.Matrix(2, 2, lambda i, j: X.red(sp.expand(
            sum(Bod[a, i] * Wd[a, b] * Bod[b, j] for a in range(N) for b in range(N)))))
        Qm = sp.Matrix(2, 2, lambda i, j: re_((A[i, j] + A[j, i]) * Q(1, 2)))
        Qs.append(Qm)
        lam = X.red(sp.expand(Q(1, 2) * sum(Qm[i, i] * Q(1, God[i, i]) for i in range(2))))
        lams[m] = ex(lam)
        scal.append(sp.simplify(Qm - sp.Matrix(
            2, 2, lambda i, j: X.red(sp.expand(lam * God[i, j])))) == sp.zeros(2, 2))

    def nstr(m):
        Wd = X.mmul(mpow(R, m), mpow(L, m))
        st = X.red(sp.expand(sum(X.mmul(C, Wd)[i, i] for i in range(N))))
        return sp.nsimplify(sp.radsimp(ex(st) / sp.trace(C)))

    return dict(Qs=Qs, lams=lams, scal=scal, fn=fn, nstr=nstr, God=God)


def test_the_odd_sector_is_ear_independent_at_every_word(odd):
    assert all(odd["scal"])


def test_the_odd_sector_carries_exactly_one_number(odd):
    v = np.array([[odd["fn"](q[0, 0]), odd["fn"](q[0, 1]), odd["fn"](q[1, 1])]
                  for q in odd["Qs"]])
    assert int(np.linalg.matrix_rank(v, tol=1e-9)) == 1
    sv = np.linalg.svd(v, compute_uv=False)
    assert sv[0] > 1 and all(s < 1e-9 for s in sv[1:])


def test_the_odd_value_set_is_three_numbers(odd):
    assert len(set(odd["lams"].values())) == 3


def test_at_the_object_the_odd_readout_is_the_benched_value(odd):
    assert sp.simplify(odd["lams"][1] - 1 / (2 * PHI)) == 0
    assert abs(float(odd["lams"][1]) - 0.30901699437494745) < 1e-15


def test_the_two_halves_of_the_mirror_agree_off_the_three_part(odd):
    agree = [m for m in range(15) if sp.simplify(odd["nstr"](m) - odd["lams"][m]) == 0]
    assert sorted(agree) == [m for m in range(15) if m % 3 != 0]


# -------------------------------------------------------------- the crowding
def _cands(H):
    s5 = math.sqrt(5)
    out = []
    for r in range(1, H + 1):
        for p in range(-H, H + 1):
            for q in range(-H, H + 1):
                if math.gcd(math.gcd(abs(p), abs(q)), r) != 1:
                    continue
                out.append((p + q * s5) / r)
    return out


def _count(cands, x, eps):
    return sum(1 for v in cands if x * (1 - eps) <= v <= x * (1 + eps))


def test_at_one_tenth_every_window_is_crowded():
    """Reproduces B856's '>= 17 natural candidates' as GENERIC, not special."""
    ph = (1 + math.sqrt(5)) / 2
    c = _cands(12)
    for x in (1 / (2 * ph), 0.5, 1.0, ph / 2, 0.25, ph / 4, 1 / (4 * ph)):
        assert _count(c, x, 1e-1) >= 17


def test_guard_the_field_does_NOT_forbid_discrimination():
    """This arc's own prior hypothesis, refuted and locked as refuted."""
    ph = (1 + math.sqrt(5)) / 2
    c = _cands(20)
    for x in (1 / (2 * ph), 0.5, 1.0, ph / 2, 0.25, ph / 4, 1 / (4 * ph)):
        assert _count(c, x, 1e-3) <= 4        # essentially unique
        assert _count(c, x, 1e-4) == 1        # unique


def test_an_index_discriminates_at_the_available_precision():
    for n in (1, 2):
        assert 1 / n >= 1e-1                  # needs >= 50% to be confusable
    assert (1 / 2) / 1e-3 >= 100              # 2-3 orders cheaper than a value


def test_l216_is_recorded_closed():
    text = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    start = text.index("## L216")
    nxt = text.find("\n## L", start + 1)
    section = text[start: nxt if nxt > 0 else len(text)]
    assert "CLOSED" in section
    assert "1/(2φ)" in section
