"""B1876 -- the integer hypotheses recomputed with this file's own code; the sealed run says what the findings quote; one
Chern-Simons value recomputed where SnapPy is installed."""
import itertools
import pathlib

import pytest

HERE = pathlib.Path(__file__).resolve().parent
RUN = (HERE / "attacks_on_main_run.txt").read_text(encoding="utf-8")
FINDINGS = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
L, R, P, ONE = (1, 1, 0, 1), (1, 0, 1, 1), (0, 1, 1, 0), (1, 0, 0, 1)


def _m(A, B, N=None):
    X = (A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3], A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3])
    return X if N is None else tuple(x % N for x in X)


F, F2 = _m(L, P), _m(P, L)


def test_h1_h2_the_four_atoms_and_the_grammar_of_l_and_f():
    S = [m for m in itertools.product(range(9), repeat=4) if m[0] * m[3] - m[1] * m[2] in (1, -1)]
    assert len(S) == 174
    rest = [m for m in S if m not in (ONE, P)]
    assert _m(P, P) == ONE and all(_m(m, m) != ONE and _m(_m(m, m), m) != ONE for m in rest)
    products = {_m(a, b) for a in rest for b in rest}
    assert sorted(m for m in rest if m not in products) == sorted([L, R, F, F2])
    assert _m(F, F) == _m(L, R) and _m(F, R) == _m(L, F) and _m(F, F2) == _m(L, L)
    seen = set()
    for n in range(1, 11):
        for t in itertools.product((L, F), repeat=n):
            M = ONE
            for x in t:
                M = _m(M, x)
            assert M not in seen and M != R
            seen.add(M)
    assert len(seen) == 2 ** 11 - 2


def test_h4_to_h8_every_history_as_a_ground():
    T = range(3, 61)
    arrow = lambda a, b: a != b and ((b - 2) % (a + 2) == 0 or (b + 2) % (a + 2) == 0)
    pairs = [(a, b) for a in T for b in T if a != b]
    assert (len(pairs), sum(arrow(a, b) for a, b in pairs), sum(arrow(a, b) and arrow(b, a) for a, b in pairs)) == (3306, 208, 0)
    assert [t for t in range(3, 500) if not any(arrow(a, t) for a in range(3, t))] == [3, 4, 5, 6]
    broken = [(a, b, c) for a in T for b in T for c in T if arrow(a, b) and arrow(b, c) and not arrow(a, c)]
    assert len(broken) == 209 and broken[0] == (3, 7, 11)
    reach, new = {3}, [3]
    while new:
        new = sorted({b for a in new for b in T if arrow(a, b)} - reach)
        reach.update(new)
    assert [t for t in T if t not in reach] == [4, 5, 6, 9, 10, 14]


def _group(gens, N):
    one = tuple(x % N for x in ONE)
    seen, front = {one}, [one]
    while front:
        nxt = []
        for g in front:
            for h in gens:
                x = _m(g, h, N)
                if x not in seen:
                    seen.add(x)
                    nxt.append(x)
        front = nxt
    return seen


def test_h11_h13_the_exchange_is_a_scalar_at_level_five():
    for N, same in ((3, False), (5, True), (7, False)):
        G, Gx = _group([L, R], N), _group([L, R, P], N)
        cls = lambda H: len({min(tuple((c * x) % N for x in g) for c in range(1, N) if (c, 0, 0, c) in H) for g in H})
        assert len(Gx) == 2 * len(G) and (cls(Gx) == cls(G)) == same
    assert len(_group([L, R], 5)) == 120
    v = (1, 2)                                             # the line of LR modulo 5: (LR + 1) v = 0
    LR = _m(L, R)
    assert ((LR[0] + 1) * v[0] + LR[1] * v[1]) % 5 == 0 and (LR[2] * v[0] + (LR[3] + 1) * v[1]) % 5 == 0
    assert ((F[0] * v[0] + F[1] * v[1]) % 5, (F[2] * v[0] + F[3] * v[1]) % 5) == ((3 * v[0]) % 5, (3 * v[1]) % 5)
    assert tuple((2 * x) % 5 for x in F) != (1, 0, 0, 1) and (2 * F[0] + 2 * F[3]) % 5 == 2      # F is 3 times a unipotent


def test_the_sealed_run_and_the_findings():
    for s in ("ALL CHECKS PASS", "entries to 8: 174", "all 32766 words to 14 letters are different matrices", "the traces with one are [3, 4, 5, 9, 21]",
              "counting primitive histories only they are [3, 4, 5, 7, 9, 21]", "17 of them", "N =  5:   120 and   240;  up to scalars   60 and   60  (the same)",
              "allowed: 35 with sign +, 50 with either sign, 330 by the line", "-0.07360, -0.07519, -0.07552", "-0.075610", "on all 16",
              "77 of 77 cyclic words to 8 letters"):
        assert s in RUN, s
    for s in ("The repo sweep:", "**All sixteen hypotheses come out on main as the seat reports them,**", "records them with its opinion (§ 6) and rules on neither.",
              "Main banks the sixteen computed facts and no clause.", "| H16 |"):
        assert s in FINDINGS, s


def test_the_run_of_six_has_a_hand_where_snappy_is_installed():
    snappy = pytest.importorskip("snappy")
    a = float(snappy.Manifold("b++LLLLLLRLR").chern_simons())
    b = float(snappy.Manifold("b++RRRRRRLRL").chern_simons())
    assert abs(abs(a) - 0.073598) < 1e-5 and abs(a + b) < 1e-9
    assert abs(float(snappy.Manifold("b++LR").chern_simons())) < 1e-10


def test_mains_addition_the_settling_rate():
    """post hoc, labelled: the derivative of the root's monodromy on the fibre's characters, at the hyperbolic point, has
    characteristic polynomial (t - 1)(t^2 - 5t + 1) = t^3 - 6 t^2 + 6 t - 1; recomputed here in plain complex arithmetic"""
    z = complex(1.5, 3 ** 0.5 / 2)                         # z^2 - 3z + 3 = 0
    assert abs(z * z - 3 * z + 3) < 1e-14
    x, y = z / (z - 1), z                                   # the fixed point of (x, y, z) -> (xz - y, z, x z^2 - x - yz)
    assert abs(x * z - y - x) < 1e-13 and abs(x * z * z - x - y * z - z) < 1e-13
    assert abs(x * x + y * y + z * z - x * y * z - 2 + 2) < 1e-13            # tr [a, b] = -2
    J = [[z, -1, x], [0, 0, 1], [z * z - 1, -z, 2 * x * z - y]]
    trace = J[0][0] + J[1][1] + J[2][2]
    minors = (J[0][0] * J[1][1] - J[0][1] * J[1][0]) + (J[0][0] * J[2][2] - J[0][2] * J[2][0]) + (J[1][1] * J[2][2] - J[1][2] * J[2][1])
    det = (J[0][0] * (J[1][1] * J[2][2] - J[1][2] * J[2][1]) - J[0][1] * (J[1][0] * J[2][2] - J[1][2] * J[2][0]) + J[0][2] * (J[1][0] * J[2][1] - J[1][1] * J[2][0]))
    assert abs(trace - 6) < 1e-12 and abs(minors - 6) < 1e-12 and abs(det - 1) < 1e-12
    run = (HERE / "settling_rate_run.txt").read_text(encoding="utf-8")
    for s in ("ALL CHECKS PASS", "(t - 1)(t^2 - 5t + 1)", "4.791288", "observed, not proved"):
        assert s in run, s
    assert "observed to four digits on three departures and is not proved" in FINDINGS
