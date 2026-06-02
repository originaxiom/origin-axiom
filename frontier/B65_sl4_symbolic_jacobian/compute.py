"""B65 -- reconstruct the symbolic SL(4) fixed-line Jacobian J(m) over Q[m] and
factor char(J(m)) over Z[m].  Diagnostic build (reports per-m reconstruction
quality and entry degrees before committing to the interpolation)."""

from __future__ import annotations

import sys
from fractions import Fraction

sys.path.insert(0, "frontier/B63_sl4_symbolic_m")
import probe  # noqa: E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

DIM = 15
DPS = 50
# tight, small-eps ladder for clean eps->0 extrapolation (SL(4) is gauge-clean)
EPSS = [mp.mpf(e) for e in ("0.003", "0.006", "0.009", "0.012", "0.015", "0.018", "0.021", "0.024")]
DEG = 7
SEED = 10
MS = list(range(1, 8))  # m = 1..7 (entries are degree 4 in m; over-determined by 2)


def dt0(m):
    mp.mp.dps = DPS
    h = mp.mpf(10) ** (-18)
    pp, pm = probe._perts(h)
    P, Q = probe._random_PQ(SEED)
    dts = []
    for eps in EPSS:
        A, B = probe.expm_mp(eps * P), probe.expm_mp(eps * Q)
        dx = probe._diff_matrix(A, B, False, pp, pm, h, m)
        dX = probe._diff_matrix(A, B, True, pp, pm, h, m)
        dts.append(dX * probe.svd_pinv(dx))
    M = mp.zeros(DIM, DIM)
    for i in range(DIM):
        for j in range(DIM):
            M[i, j] = mp.re(probe._extrap0(EPSS, [d[i, j] for d in dts], DEG))
    return M


def rr(x, max_den=420):
    x = mp.re(x)
    if abs(x) < mp.mpf("1e-7"):
        return Fraction(0), 0.0
    tol = max(mp.mpf("1e-4"), abs(x) * mp.mpf("1e-6"))
    best = None
    for q in range(1, max_den + 1):
        p = int(mp.nint(x * q))
        err = abs(x - mp.mpf(p) / q)
        if err < tol:
            return Fraction(p, q), float(err)
        if best is None or err < best[1]:
            best = (Fraction(p, q), err)
    return None, float(best[1])


def main():
    m, t = sp.symbols("m t")
    print(f"B65 diagnostic: m={MS}, dps={DPS}, tight ladder, seed={SEED}")
    mats = {}
    for mm in MS:
        mats[mm] = dt0(mm)
        # per-m reconstruction quality
        errs = []
        fails = 0
        maxabs = 0.0
        for i in range(DIM):
            for j in range(DIM):
                v = mats[mm][i, j]
                maxabs = max(maxabs, float(abs(v)))
                fr, e = rr(v)
                if fr is None:
                    fails += 1
                errs.append(e)
        print(f"  m={mm}: worst-recon={max(errs):.1e}  fails={fails}  max|entry|={maxabs:.1e}")

    # reconstruct all; find m that are fully clean
    rat = {}
    clean = []
    for mm in MS:
        ok = True
        grid = [[None] * DIM for _ in range(DIM)]
        for i in range(DIM):
            for j in range(DIM):
                fr, e = rr(mats[mm][i, j])
                if fr is None:
                    ok = False
                grid[i][j] = fr
        rat[mm] = grid
        if ok:
            clean.append(mm)
    print(f"fully-clean m values: {clean}")
    if len(clean) < 6:
        print("Not enough clean m to interpolate reliably; stopping with diagnostics.")
        return

    # determine per-entry degree by interpolating through ALL clean m
    fit = clean
    J = sp.zeros(DIM, DIM)
    maxdeg = 0
    for i in range(DIM):
        for j in range(DIM):
            pts = [(mm, sp.Rational(rat[mm][i][j])) for mm in fit]
            poly = sp.expand(sp.interpolate(pts, m))
            J[i, j] = poly
            d = sp.degree(poly, m) if poly.has(m) else 0
            maxdeg = max(maxdeg, int(d) if d != -sp.oo else 0)
    print(f"max entry degree in m (interpolant through {len(fit)} clean points): {maxdeg}")
    # over-determination: if maxdeg < len(fit)-1 the interpolant is over-determined -> trustworthy
    print(f"over-determined: {maxdeg} < {len(fit) - 1} = {maxdeg < len(fit) - 1}")

    # dump the reconstructed J(m) as a committed artifact (entry strings in m)
    import json
    table = [[str(J[i, j]) for j in range(DIM)] for i in range(DIM)]
    with open("frontier/B65_sl4_symbolic_jacobian/jacobian_m.json", "w") as fh:
        json.dump({"fit_m": fit, "max_degree": int(maxdeg), "J": table}, fh, indent=0)
    print("wrote jacobian_m.json")

    print("factoring char(J(m)) over Z[m] ...")
    cp = sp.expand(J.charpoly(t).as_expr())
    factored = sp.factor(cp)

    def Lk(kk):
        Mm = sp.Matrix([[m, 1], [1, 0]])
        Mk = Mm ** abs(kk) if kk >= 0 else Mm.inv() ** (-kk)
        return sp.expand(sp.trace(Mk))
    target = sp.expand(
        (t**2 - Lk(-1) * t - 1) * (t**2 - Lk(1) * t - 1) * (t**2 - Lk(2) * t + 1)
        * (t**2 - Lk(3) * t - 1) * (t**2 - Lk(4) * t + 1) * (t**2 + Lk(2) * t + 1)
        * (t - 1) ** 2 * (t + 1)
    )
    match = sp.expand(cp - target) == 0
    print("char(J(m)) =", factored)
    print("MATCHES B63/B64 factorization over Z[m]:", match)
    print("m=1 matches B59:", sp.expand(cp.subs(m, 1) - target.subs(m, 1)) == 0)
    print(f"\nB65 RESULT: {'SYMBOLIC FACTORIZATION CONFIRMED' if match else 'NEEDS REVIEW'}")


if __name__ == "__main__":
    main()
