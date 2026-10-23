#!/usr/bin/env python3
"""W139 — the E6 breaking arc: can any vev of the families' 27s split the charged leptons from the down quarks?
(the rule: W139_RULE.md, committed and pushed before this script existed).

  E0  the instrument: the linear maps A of C^27 with grad N(X) . A X = 0 at 1 500 random integer points; the rank of
      that 1 500 x 729 system over Q, exact (rank mod p as the lower bound; the reduced-row-echelon nullspace basis
      lifted to Q by rational reconstruction, checked exactly on the 1 500 rows and as a polynomial identity, as the
      upper bound). Predicted nullity 78
  E1  the embedding: T3 and Y on the 27's components; the multiset of (colour, Q, Y) against 16 + 10 + 1; the five
      neutral colourless components
  E2  the extended charge -1/3 quark and charged-lepton 6 x 6 matrices from W's second derivatives, three families,
      symmetric lambda, vevs in the fifteen neutral directions: equal singular values at ten random points (40 digits)
  E3  hierarchical vevs (singlets 10^4 times the doublets): the three lightest agree at five random points, and D
  E4  the control: det L's coefficient 2 - the lepton singular values double, the quarks' stay, and the symmetry
      algebra's dimension (predicted 24)
  E5  the read-out: the by-hand form M_l = -kappa (1 (x) J^T) M_q^T (1 (x) J), and the numbers the record needs

    python3 -B the_e6_breaking.py      # writes the_e6_breaking.json beside itself
"""
import itertools
import json
import platform
import random
import sys
import time
import traceback
from collections import Counter
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path

import flint
import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_e6_breaking.json"
P = 2**61 - 1  # a prime
mp.mp.dps = 40

# ------------------------------------------------------------------ the 27 in the trinification basis
# Q^a_alpha (colour 3, SU(3)_L 3bar), L^alpha_alpha' (SU(3)_L 3, SU(3)_R 3bar), Qc_alpha' a (colour 3bar, SU(3)_R 3)


def iQ(a, al):
    return 3 * a + al


def iL(al, ap):
    return 9 + 3 * al + ap


def iQc(ap, a):
    return 18 + 3 * ap + a


def sign(s):
    return (-1) ** sum(1 for i, j in itertools.combinations(range(len(s)), 2) if s[i] > s[j])


PERMS = [(s, sign(s)) for s in itertools.permutations(range(3))]


def monomials(kappa=1):
    """N = det Q + kappa det L + det Qc - tr(Q L Qc), as (coefficient, (i, j, k)) with distinct i, j, k."""
    out = []
    for s, sg in PERMS:
        out.append((sg, tuple(iQ(r, s[r]) for r in range(3))))
        out.append((kappa * sg, tuple(iL(r, s[r]) for r in range(3))))
        out.append((sg, tuple(iQc(r, s[r]) for r in range(3))))
    for a, al, ap in itertools.product(range(3), repeat=3):
        out.append((-1, (iQ(a, al), iL(al, ap), iQc(ap, a))))
    assert all(len(set(m)) == 3 for _, m in out)
    return out


def N_of(mons, X):
    return sum(c * X[i] * X[j] * X[k] for c, (i, j, k) in mons)


def grad(mons, X):
    g = [0] * 27
    for c, (i, j, k) in mons:
        g[i] += c * X[j] * X[k]
        g[j] += c * X[i] * X[k]
        g[k] += c * X[i] * X[j]
    return g


def self_check(mons, kappa, rng, n=5):
    """N from the monomial list against det and trace of the three matrices (sympy, exact)."""
    worst = 0
    for _ in range(n):
        X = [rng.randint(-4, 4) for _ in range(27)]
        Qm = sp.Matrix(3, 3, lambda a, al: X[iQ(a, al)])
        Lm = sp.Matrix(3, 3, lambda al, ap: X[iL(al, ap)])
        Cm = sp.Matrix(3, 3, lambda ap, a: X[iQc(ap, a)])
        direct = Qm.det() + kappa * Lm.det() + Cm.det() - (Qm * Lm * Cm).trace()
        worst = max(worst, abs(int(direct) - N_of(mons, X)))
    return worst


# ------------------------------------------------------------------ E0 / E4: the symmetry algebra, exact
def ratrec(a, m=P):
    """r/s = a mod m with |r|, |s| <= sqrt(m/2), or None."""
    a %= m
    bound = isqrt(m // 2)
    r0, r1, s0, s1 = m, a, 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound or gcd(r1, abs(s1)) != 1:
        return None
    return F(r1, s1)


def poly_identity_zero(mons, A):
    """grad N(X) . A X as a polynomial in X: True if every coefficient is 0 (A as {p: {q: int}})."""
    coef = Counter()
    for c, m in mons:
        for t, p in enumerate(m):
            if p not in A:
                continue
            others = tuple(x for u, x in enumerate(m) if u != t)
            for q, aq in A[p].items():
                coef[tuple(sorted(others + (q,)))] += c * aq
    return all(v == 0 for v in coef.values())


def symmetry_algebra(kappa, seed=139, npts=1500):
    mons = monomials(kappa)
    rng = random.Random(seed)
    rows = []
    for _ in range(npts):
        X = [rng.randint(-3, 3) for _ in range(27)]
        g = grad(mons, X)
        rows.append([g[p] * X[q] for p in range(27) for q in range(27)])
    Mz = flint.fmpz_mat(rows)
    Mp = flint.nmod_mat(npts, 729, [v % P for r in rows for v in r], P)
    rank_p = Mp.rank()
    R, rk = Mp.rref()
    assert rk == rank_p
    piv = []
    for r in range(rk):
        c = next(c for c in range(729) if int(R[r, c]) != 0)
        piv.append(c)
    free = [c for c in range(729) if c not in set(piv)]
    basis, failed = [], 0
    maxden = 1
    for f in free:
        v = [F(0)] * 729
        v[f] = F(1)
        for r, c in enumerate(piv):
            e = int(R[r, f])
            if e:
                q = ratrec(-e)
                if q is None:
                    failed += 1
                    q = F(0)
                v[c] = q
        den = 1
        for x in v:
            den = den * x.denominator // gcd(den, x.denominator)
        maxden = max(maxden, den)
        basis.append([int(x * den) for x in v])
    nullity_p = len(free)
    out = {"kappa": kappa, "points": npts, "seed": seed, "unknowns": 729, "rank mod p": rank_p,
           "nullity mod p": nullity_p, "reconstruction failures": failed, "largest denominator": maxden}
    if failed == 0 and basis:
        B = flint.fmpz_mat(729, nullity_p, [basis[j][i] for i in range(729) for j in range(nullity_p)])
        on_rows = (Mz * B).is_zero()
        Bp = flint.nmod_mat(729, nullity_p, [basis[j][i] % P for i in range(729) for j in range(nullity_p)], P)
        indep = Bp.rank() == nullity_p
        ident = all(poly_identity_zero(mons, {p: {q: b[27 * p + q] for q in range(27) if b[27 * p + q]}
                                              for p in range(27) if any(b[27 * p:27 * p + 27])}) for b in basis)
        out.update({"basis satisfies the 1 500 rows exactly": bool(on_rows), "basis independent": bool(indep),
                    "basis satisfies grad N . A X = 0 as a polynomial identity": bool(ident)})
        exact = on_rows and indep
        out["rank over Q (exact)"] = 729 - nullity_p if exact else None
        out["dimension of the symmetry algebra (exact)"] = nullity_p if (exact and ident) else None
    else:
        out["rank over Q (exact)"] = None
        out["dimension of the symmetry algebra (exact)"] = None
    return out


def E0():
    t = time.time()
    rng = random.Random(1390)
    r = symmetry_algebra(1)
    worst = self_check(monomials(1), 1, rng)
    r["monomial table against det and trace (worst |difference|)"] = worst
    r["seconds"] = round(time.time() - t, 1)
    return r, r["dimension of the symmetry algebra (exact)"] == 78 and worst == 0


# ------------------------------------------------------------------ E1: the embedding
T3 = (F(1, 2), F(-1, 2), F(0))
TL = (F(-1, 6), F(-1, 6), F(1, 3))
TR = (F(-2, 3), F(1, 3), F(1, 3))


def components():
    """(index, block, colour, T3, Y) for every one of the 27."""
    out = []
    for a, al in itertools.product(range(3), repeat=2):
        out.append((iQ(a, al), "Q", "3", -T3[al], -TL[al], a))
    for al, ap in itertools.product(range(3), repeat=2):
        out.append((iL(al, ap), "L", "1", T3[al], TL[al] - TR[ap], 0))
    for ap, a in itertools.product(range(3), repeat=2):
        out.append((iQc(ap, a), "Qc", "3b", F(0), TR[ap], a))
    return out


def expected_multiset():
    h = F(1, 2)
    sixteen = [("3", F(2, 3), F(1, 6)), ("3", F(-1, 3), F(1, 6)), ("3b", F(-2, 3), F(-2, 3)),
               ("3b", F(1, 3), F(1, 3)), ("1", F(0), -h), ("1", F(-1), -h), ("1", F(1), F(1)), ("1", F(0), F(0))]
    ten = [("3", F(-1, 3), F(-1, 3)), ("3b", F(1, 3), F(1, 3)), ("1", F(1), h), ("1", F(0), h), ("1", F(0), -h),
           ("1", F(-1), -h)]
    one = [("1", F(0), F(0))]
    return Counter(sixteen + ten + one)


def E1():
    comps = components()
    got = Counter((col, t3 + y, y) for _, _, col, t3, y, a in comps if a == 0)
    exp = expected_multiset()
    neutral = sorted(((i - 9) // 3 + 1, (i - 9) % 3 + 1) for i, blk, col, t3, y, a in comps
                     if col == "1" and t3 + y == 0)
    listed = sorted([(2, 1), (1, 2), (1, 3), (3, 2), (3, 3)])
    # checks, not cells: T3, Y and SU(2)_L's raising operator are symmetries of N
    mons = monomials(1)
    charge = {i: (t3, y) for i, _, _, t3, y, _ in comps}
    t3_ok = all(sum(charge[i][0] for i in m) == 0 for _, m in mons)
    y_ok = all(sum(charge[i][1] for i in m) == 0 for _, m in mons)
    rng = random.Random(1391)
    raise_ok = True
    for _ in range(50):
        X = [rng.randint(-5, 5) for _ in range(27)]
        TX = [0] * 27
        for ap in range(3):
            TX[iL(0, ap)] = X[iL(1, ap)]
        for a in range(3):
            TX[iQ(a, 1)] = -X[iQ(a, 0)]
        raise_ok &= sum(g * t for g, t in zip(grad(mons, X), TX)) == 0
    r = {"multiset (colour, Q, Y), colour triplets once": sorted([list(map(str, k)) + [v] for k, v in got.items()]),
         "equals 16 + 10 + 1": got == exp, "components counted": sum(got.values()),
         "neutral colourless components (alpha, alpha'), 1-indexed": neutral,
         "equal to the five listed": neutral == listed,
         "checks (not cells)": {"T3 preserves N": t3_ok, "Y preserves N": y_ok,
                                "SU(2)_L raising preserves N (50 points)": bool(raise_ok)}}
    return r, r["equals 16 + 10 + 1"] and r["equal to the five listed"]


# ------------------------------------------------------------------ E2-E4: the extended mass matrices
NEUTRAL = [iL(1, 0), iL(0, 1), iL(0, 2), iL(2, 1), iL(2, 2)]  # h_u0; the two Y = -1/2 doublets; the two singlets
QROWS = [iQ(0, 0), iQ(0, 2)]  # d, D (colour a = 0)
QCOLS = [iQc(1, 0), iQc(2, 0)]  # the two charge 1/3 antitriplets
LROWS = [iL(1, 1), iL(1, 2)]  # charge -1
LCOLS = [iL(0, 0), iL(2, 0)]  # charge +1


def hessian_table(kappa):
    tab = {}
    for c, m in monomials(kappa):
        for p, q in itertools.permutations(m, 2):
            r = next(x for x in m if x != p and x != q)
            tab.setdefault((p, q), []).append((c, r))
    return tab


def H(tab, v, p, q):
    return sum((c * v.get(r, 0) for c, r in tab.get((p, q), [])), mp.mpc(0))


def mass_matrices(kappa, lam, vevs):
    tab = hessian_table(kappa)
    Mq, Ml = mp.matrix(6, 6), mp.matrix(6, 6)
    for a, b in itertools.product(range(3), repeat=2):
        for s, t in itertools.product(range(2), repeat=2):
            Mq[2 * a + s, 2 * b + t] = sum((lam[a][b][j] * H(tab, vevs[j], QROWS[s], QCOLS[t]) for j in range(3)),
                                           mp.mpc(0))
            Ml[2 * a + s, 2 * b + t] = sum((lam[a][b][j] * H(tab, vevs[j], LROWS[s], LCOLS[t]) for j in range(3)),
                                           mp.mpc(0))
    return Mq, Ml


def svals(M):
    S = mp.svd_c(M, compute_uv=False)
    return sorted(S[i] for i in range(S.rows))


def crand(rng, scale=1):
    return mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1)) * scale


def random_point(rng, singlet_scale=1):
    vals = {}
    for c in itertools.combinations_with_replacement(range(3), 3):
        vals[c] = crand(rng)
    lam = [[[vals[tuple(sorted((i, j, k)))] for k in range(3)] for j in range(3)] for i in range(3)]
    vevs = []
    for _ in range(3):
        v = {}
        for n, idx in enumerate(NEUTRAL):
            v[idx] = crand(rng, singlet_scale if n >= 3 else 1)
        vevs.append(v)
    return lam, vevs


def rel(x, y):
    return max(abs(a - b) / abs(b) for a, b in zip(x, y))


def byhand_residual(Mq, Ml, kappa):
    J = mp.matrix([[0, 1], [-1, 0]])
    IJ = mp.matrix(6, 6)
    for a in range(3):
        for s, t in itertools.product(range(2), repeat=2):
            IJ[2 * a + s, 2 * a + t] = J[s, t]
    pred = -kappa * (IJ.T * Mq.T * IJ)
    return float(mp.mnorm(Ml - pred, 1) / mp.mnorm(Ml, 1))


def E2_E4():
    rng = random.Random(1392)
    pts = [random_point(rng) for _ in range(10)]
    e2, e4, resid = [], [], []
    for lam, vevs in pts:
        Mq, Ml = mass_matrices(1, lam, vevs)
        sq, sl = svals(Mq), svals(Ml)
        e2.append(float(rel(sq, sl)))
        resid.append(byhand_residual(Mq, Ml, 1))
        Mq2, Ml2 = mass_matrices(2, lam, vevs)
        sq2, sl2 = svals(Mq2), svals(Ml2)
        e4.append({"leptons: max |sigma(2)/sigma(1) - 2|": float(max(abs(a / b - 2) for a, b in zip(sl2, sl))),
                   "quarks: max relative change": float(rel(sq2, sq)),
                   "by-hand form at kappa = 2": byhand_residual(Mq2, Ml2, 2)})
    first = pts[0]
    Mq, Ml = mass_matrices(1, *first)
    e2r = {"points": 10, "seed": 1392, "digits": mp.mp.dps,
           "max relative difference of the six singular values, per point": e2,
           "worst": max(e2), "singular values at the first point (quarks)": [mp.nstr(x, 12) for x in svals(Mq)],
           "singular values at the first point (leptons)": [mp.nstr(x, 12) for x in svals(Ml)]}
    ok2 = max(e2) < 1e-10
    alg2 = symmetry_algebra(2)
    ok4 = (all(d["leptons: max |sigma(2)/sigma(1) - 2|"] < 1e-10 and d["quarks: max relative change"] < 1e-10
               for d in e4) and alg2["dimension of the symmetry algebra (exact)"] == 24)
    e4r = {"kappa": 2, "per point": e4, "symmetry algebra at kappa = 2": alg2}
    return e2r, ok2, e4r, ok4, resid


def E3():
    rng = random.Random(1393)
    rows, ok = [], True
    for _ in range(5):
        lam, vevs = random_point(rng, singlet_scale=10**4)
        Mq, Ml = mass_matrices(1, lam, vevs)
        sq, sl = svals(Mq), svals(Ml)
        lq, ll = sq[:3], sl[:3]
        r = float(rel(lq, ll))
        D = (ll[1] * lq[0]) / (lq[1] * ll[0])
        rows.append({"light quarks": [mp.nstr(x, 10) for x in lq], "light leptons": [mp.nstr(x, 10) for x in ll],
                     "max relative difference (light three)": r, "|ln D|": float(abs(mp.log(D))),
                     "lightest heavy / heaviest light": float(sq[3] / sq[2])})
        ok &= r < 1e-8
    return {"points": 5, "seed": 1393, "singlets over doublets": 10**4, "rows": rows}, bool(ok)


def guarded(fn):
    try:
        return fn(), None
    except Exception:  # a failed part is a failed launch of that part (the rule's discipline)
        return None, traceback.format_exc()


def main():
    t0 = time.time()
    cells, out, errors = {}, {"arc": "W139", "rule": "W139_RULE.md", "status": "one run"}, {}
    r, err = guarded(E0)
    if err:
        errors["E0"], cells["E0"] = err, False
    else:
        out["E0"], cells["E0"] = r
    r, err = guarded(E1)
    if err:
        errors["E1"], cells["E1"] = err, False
    else:
        out["E1"], cells["E1"] = r
    r, err = guarded(E2_E4)
    resid = None
    if err:
        errors["E2/E4"], cells["E2"], cells["E4"] = err, False, False
    else:
        out["E2"], cells["E2"], out["E4"], cells["E4"], resid = r
    r, err = guarded(E3)
    if err:
        errors["E3"], cells["E3"] = err, False
    else:
        out["E3"], cells["E3"] = r
    out["E5 (read-out)"] = {
        "by-hand form M_l = -(1 (x) J^T) M_q^T (1 (x) J), relative residual at the E2 points": resid,
        "E0's dimension": (out.get("E0") or {}).get("dimension of the symmetry algebra (exact)"),
        "E4's dimension": ((out.get("E4") or {}).get("symmetry algebra at kappa = 2") or {}).get(
            "dimension of the symmetry algebra (exact)")}
    out["cells"] = {k: bool(cells[k]) for k in ("E0", "E1", "E2", "E3", "E4")}
    out["every cell holds"] = bool(all(out["cells"].values()))
    out["errors"] = errors
    out["environment"] = {"python": platform.python_version(), "python-flint": flint.__version__,
                          "mpmath": mp.__version__, "sympy": sp.__version__}
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])
    if errors:
        print("errors:", ", ".join(errors), file=sys.stderr)


if __name__ == "__main__":
    main()
