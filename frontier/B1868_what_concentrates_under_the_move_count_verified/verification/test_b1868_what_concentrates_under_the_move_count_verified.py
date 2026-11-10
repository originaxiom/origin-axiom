"""B1868 -- the verification's decisive numbers are recomputed here with this file's own short code (smaller depths), and the
sealed run says what the findings quote.  No random numbers anywhere."""
import itertools
import math
import pathlib
from fractions import Fraction

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
RUN = (HERE / "move_count_tau_side_run.txt").read_text(encoding="utf-8")


def _logs(n):
    q = np.array([1], dtype=np.int64)
    r = np.array([1], dtype=np.int64)
    for _ in range(n):
        m = q + r
        q, r = np.concatenate([q, m]), np.concatenate([m, r])
    return np.log(q.astype(float)) + np.log(r.astype(float))


def test_the_exponent_per_move_and_the_correlation_dimension():
    """the regression lock the register asked for (P-480): 0.792425 from the Stern-Brocot intervals, by main's own sums"""
    a, b = _logs(17), _logs(18)
    assert abs((b.mean() - a.mean()) - 0.792425) < 5e-6
    def growth(beta):
        return math.log(np.exp(beta * (b - b.max())).sum()) + beta * b.max() - math.log(np.exp(beta * (a - a.max())).sum()) - beta * a.max()
    lo, hi = 0.5, 1.2
    for _ in range(50):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if growth(mid) < math.log(4) else (lo, mid)
    d2 = (lo + hi) / 2
    assert abs(d2 - 0.844609) < 5e-6 and d2 < math.log(2) / 0.792425
    # the control: the same construction at order 1 gives growth 2 at beta = 0 (the count of intervals), not 4
    assert abs(growth(0.0) - math.log(2)) < 1e-12


def _qmark(x):
    res = np.zeros_like(x)
    frac = x.copy()
    expo = np.zeros_like(x)
    sign = 1.0
    alive = frac > 0
    for _ in range(70):
        if not alive.any():
            break
        inv = np.where(alive, 1.0 / np.where(alive, frac, 1.0), 0.0)
        a = np.floor(inv)
        expo = expo + np.where(alive, a, 0.0)
        res = res + sign * np.where(alive & (expo < 1000), np.exp2(1.0 - np.minimum(expo, 1000.0)), 0.0)
        frac = np.where(alive, inv - a, 0.0)
        alive = alive & (frac > 1e-15) & (expo < 80)
        sign = -sign
    return res


def _F(x):
    out = np.empty_like(x)
    s = x <= 1.0
    out[s] = _qmark(np.clip(x[s], 0.0, 1.0)) / 2
    with np.errstate(divide="ignore"):
        out[~s] = 1.0 - _qmark(np.where(np.isinf(x[~s]), 0.0, 1.0 / x[~s])) / 2
    return out


def _mid(n):
    a, b, c, d = (np.array([v], dtype=np.int64) for v in (0, 1, 1, 0))
    for _ in range(n):
        ma, mb = a + c, b + d
        a, b, c, d = np.concatenate([a, ma]), np.concatenate([b, mb]), np.concatenate([ma, c]), np.concatenate([mb, d])
    return (a + c).astype(float) / (b + d).astype(float)


def test_minkowskis_function_against_exact_arithmetic():
    def exact(fr):
        res, sign, expo, p, q = Fraction(0), 1, 0, fr.numerator, fr.denominator
        while p:
            a = q // p
            expo += a
            res += sign * Fraction(2, 2 ** expo)
            p, q = q - a * p, p
            sign = -sign
        return res
    assert [exact(Fraction(1, 2)), exact(Fraction(1, 3)), exact(Fraction(2, 3))] == [Fraction(1, 2), Fraction(1, 4), Fraction(3, 4)]
    frs = [Fraction(k, 997) for k in range(1, 997, 13)]
    got = _qmark(np.array([float(f) for f in frs]))
    assert max(abs(float(exact(f)) - g) for f, g in zip(frs, got)) < 1e-12


def test_the_weight_near_points_of_the_axis():
    """the exponent of the weight of histories within a distance of iy: D2 at i, 0.923 at i sqrt 2, 1 at i sqrt 3 (depth 14 here)"""
    xi = _mid(14)
    ks = range(5, 12)
    def C(y, s):
        lo = np.maximum((y * y - s * y * xi) / (xi + s * y), 0.0)
        with np.errstate(divide="ignore", invalid="ignore"):
            hi = np.where(xi > s * y, (y * y + s * y * xi) / np.where(xi > s * y, xi - s * y, 1.0), np.inf)
        return float((_F(hi) - _F(lo)).mean())
    def expo(y):
        xs = [-k * math.log(2) for k in ks]
        ys = [math.log(C(y, 2.0 ** -k)) for k in ks]
        mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
        return sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
    e1, e2, e3 = expo(1.0), expo(math.sqrt(2)), expo(math.sqrt(3))
    assert abs(e1 - 0.844609) < 0.005 and abs(e2 - 0.9234) < 0.005 and abs(e3 - 1.0) < 0.02
    assert e1 < e2 < e3 and e1 < 1                                  # sharpest at i; below 1 means the density against area rises
    assert abs(C(1.0, 1e9) - 1.0) < 1e-12                           # no restriction: all the weight


def test_the_walk_at_level_five_and_the_attack_results_facts():
    G = [(a, b, c, d) for a, b, c, d in itertools.product(range(5), repeat=4) if (a * d - b * c) % 5 == 1]
    idx = {g: i for i, g in enumerate(G)}
    mul = lambda A, B: ((A[0] * B[0] + A[1] * B[2]) % 5, (A[0] * B[1] + A[1] * B[3]) % 5, (A[2] * B[0] + A[3] * B[2]) % 5, (A[2] * B[1] + A[3] * B[3]) % 5)
    P = np.zeros((120, 120))
    for g in G:
        P[idx[mul(g, (1, 1, 0, 1))], idx[g]] += 0.5
        P[idx[mul(g, (1, 0, 1, 1))], idx[g]] += 0.5
    mods = np.sort(np.abs(np.linalg.eigvals(P)))[::-1]
    assert len(G) == 120 and abs(mods[0] - 1) < 1e-9 and abs(mods[1] - math.sqrt(3) / 2) < 1e-9 and int(np.sum(np.abs(mods - mods[1]) < 1e-9)) == 8
    p = np.zeros(120)
    p[idx[(1, 0, 0, 1)]] = 1.0
    for _ in range(80):
        p = P @ p
    assert 0.5 * np.abs(p - 1 / 120).sum() < 2e-5
    # the attack result's facts, in integers
    m2 = lambda A, B: ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]), (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))
    inv = lambda A: ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))
    def wd(w):
        M = ((1, 0), (0, 1))
        for c in w:
            M = m2(M, ((1, 1), (0, 1)) if c == "L" else ((1, 0), (1, 1)))
        return M
    def ctr(w):
        W, Gd = wd(w), wd("LR")
        X = m2(m2(W, Gd), m2(inv(W), inv(Gd)))
        return X[0][0] + X[1][1] - 2
    assert sorted({ctr(w) for w in ("LLR", "LRL", "RLL")}) == [-11, 1] and ctr("LLLLLLRLR") == 25 and ctr("LLRRLLRLR") == 25
    assert ctr("LLLLLRLR") % 25 != 0                               # the control: the run of 5 does not commute with the ground at level 5
    g = range(-6, 7)
    assert all(z * z + y * y + (z * y - x) ** 2 - z * y * (z * y - x) == x * x + y * y + z * z - x * y * z for x in g for y in g for z in g)


def test_the_sealed_run_and_the_findings_agree():
    for s in ("-> 0.792425", "-> 0.844609", "main: -0.1555 at i against D2 - 1 = -0.1554; -0.0766 at i sqrt 2",
              "the second modulus of the step is 0.866025", "8 times", "349 commute with the ground at level 5",
              "N: eigenlines fixed by S, by ST, for N = 2 .. 13: 2:1,0 3:0,1 4:0,0 5:2,0 6:0,0 7:0,2 8:0,0 9:0,0 10:2,0 11:0,0 12:0,0 13:2,2"):
        assert s in RUN, s
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("The repo sweep:", "Not verified by main", "closes\n  nothing", "Main read the seat's numbers before computing", "relayed sentences"):
        assert s in f, s
