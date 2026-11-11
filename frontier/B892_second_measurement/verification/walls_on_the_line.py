"""B892: every wall on the line of the second measurement, from the joint eigenvalues (the audit's finding E5; main, 2026-11-11).

THE FAULT.  `../wall_search.py` scans y(theta) = cos(theta) x14 + sin(theta) x16 on 120 grid points for a joint nullity above
the generic 12, and refines by golden section only `if not found`.  The grid always finds the known plane stratum at pure
x16 (nullity 30), so the refinement never ran.  The findings said "120-point + golden-section ... no real nullity-14 point
exists there -- now a fact".  A 120-point grid cannot show that.

MAIN'S FIRST ATTEMPT, WHICH FAILED AND IS NOT KEPT: a fine scan in double precision with a bound on how fast a singular
value can move between grid points.  The matrices are scaled over thirteen orders of magnitude (the balancing below has
condition number 3.5e13), the bound was a hundred thousand times larger than the quantity it had to bound, and three of
that script's four checks failed.  A scan is the wrong instrument for this claim.

THE RIGHT INSTRUMENT.  s1, x14, x16 and x22 commute and are diagonalisable, so they have joint eigenvectors, and on each
one the four act by numbers (a weight).  The joint centraliser of s1 and y = x14 + t x16 is spanned by the eigenvectors
with weight(s1) = 0 and weight(x14) + t weight(x16) = 0.  So the nullity at EVERY t, real or complex, is read off the list
of weights: 12 where no further weight vanishes, and it jumps exactly at t = -weight(x14)/weight(x16).  No grid.

WHAT COULD FAIL.  The matrices not commuting, or not diagonalising together (the residual would show it); a wall value
with a real part; the count at a wall disagreeing with a direct rank computation at that complex point.

EXPECTATIONS, WRITTEN BEFORE THE FIRST RUN OF THIS FILE (main had seen the numbers in an exploration; not blind).
 W1  the four ad-matrices commute, and one change of basis diagonalises all four (residual below 1e-10).
 W2  ad(s1) has 46 vanishing weights; among them 12 vanish on x14 and x16 as well (the generic nullity) and 30 on x16 (the
     plane stratum at pure x16).
 W3  the walls at finite t are four, all purely imaginary: nullity 14 at a conjugate pair and nullity 18 at another.  So on
     the real line the nullity is 12 at every point but pure x16.
 W4  the solo seat's mechanism, recorded in B874's addendum of 2026-08-18 as theirs: the 34 active weights fall into seven
     proportionality classes of sizes 2, 2, 6, 6, 6, 6, 6; three are real and four form two conjugate pairs.
 W5  a direct rank computation at each wall value and at real points agrees with the count from the weights.
"""
import collections
import contextlib
import io
import json
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
B854 = (ARC.parent / "B854_centralizer_exact" / "e6_centralizer.py").resolve()
CUBIC = [500716339200, -159667200, -28224, 1]
OUT, RES = [], {}


def P(*a):
    s = " ".join(str(x) for x in a); OUT.append(s); print(s, flush=True)


def check(name, ok, detail=""):
    RES[name] = bool(ok)
    P("   [%s] %s%s" % ("ok" if ok else "FAILS", name, (" -- " + str(detail)) if detail else ""))


def build():
    """the ad-matrices of the invariants x8, x14, x16, x22 from B854's exact structure constants, as ../wall_search.py builds them"""
    g = {"__file__": str(B854), "__name__": "b854"}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(open(B854).read(), str(B854), "exec"), g)
    DIM, N = g["DIM"], g["N"]
    br, hvec, evec, ROOTS = g["br"], g["hvec"], g["evec"], g["ROOTS"]
    basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]
    triples = {}
    for p in range(DIM):
        for q in range(DIM):
            for r, c in enumerate(br(basis[p], basis[q])):
                if c:
                    triples.setdefault(p, []).append((q, r, c))
    def admat(vec):
        A = np.zeros((DIM, DIM))
        for p in range(DIM):
            if vec[p]:
                vp = float(vec[p])
                for q, r, c in triples.get(p, []):
                    A[r, q] += vp * float(c)
        return A
    return DIM, {n: admat(g["INV"][n]) for n in (8, 14, 16, 22)}


def balance(G, sweeps=60):
    """Osborne's diagonal balancing: d with D^-1 G D having rows and columns of equal norm.  A similarity: no eigenvalue moves."""
    n = len(G); d = np.ones(n); M = G.copy()
    for _ in range(sweeps):
        for i in range(n):
            c = np.linalg.norm(np.delete(M[:, i], i)); r = np.linalg.norm(np.delete(M[i, :], i))
            if c > 0 and r > 0:
                f = np.sqrt(r / c)
                M[:, i] *= f; M[i, :] /= f; d[i] *= f
    return d


def joint_weights():
    DIM, A = build()
    t1 = 13 * min(r.real for r in np.roots(CUBIC) if abs(r.imag) < 1e-9 * abs(r))
    X = {"s1": A[8] + t1 * A[16], "x14": A[14], "x16": A[16], "x22": A[22]}
    rel = lambda U, V: np.linalg.norm(U @ V - V @ U) / (np.linalg.norm(U) * np.linalg.norm(V))
    comm = max(rel(X[a], X[b]) for a in X for b in X if a < b)
    G = sum(c * X[k] / np.linalg.norm(X[k], 2) for k, c in (("s1", 1.0), ("x14", 0.731), ("x16", 0.417), ("x22", 0.593)))
    d = balance(G)
    Bal = {k: (M / d[:, None]) * d[None, :] for k, M in X.items()}        # D^-1 M D
    w, V = np.linalg.eig((G / d[:, None]) * d[None, :])
    Vi = np.linalg.inv(V)
    W, resid = {}, 0.0
    for k, M in Bal.items():
        D = Vi @ M @ V
        resid = max(resid, np.linalg.norm(D - np.diag(np.diag(D))) / np.linalg.norm(D))
        W[k] = np.diag(D)
    return DIM, X, Bal, W, dict(commutator=comm, residual=resid, cond_eigvec=float(np.linalg.cond(V)), cond_balance=float(d.max() / d.min()), t1=float(t1))


def nullity_direct(Bal, t, DIM):
    """the joint nullity of ad(s1) and ad(x14 + t x16), by singular values in the balanced basis, with the gap shown"""
    St = np.vstack([Bal["s1"] / np.linalg.norm(Bal["s1"], 2), (Bal["x14"] + t * Bal["x16"]) / np.linalg.norm(Bal["x14"] + t * Bal["x16"], 2)])
    s = np.linalg.svd(St, compute_uv=False)[::-1]
    n = int(np.sum(s < 1e-9))
    return n, float(s[n - 1]) if n else 0.0, float(s[n])


def main():
    DIM, X, Bal, W, info = joint_weights()
    P("B892: EVERY WALL ON THE LINE OF THE SECOND MEASUREMENT, FROM THE JOINT EIGENVALUES")
    P("   dimension %d; the balancing scales the basis over a factor %.1e; the joint eigenvectors' matrix has condition number %.1f" % (DIM, info["cond_balance"], info["cond_eigvec"]))
    check("W1 the four ad-matrices commute and one change of basis diagonalises all four", info["commutator"] < 1e-12 and info["residual"] < 1e-10 and info["cond_eigvec"] < 1e3,
          "largest relative commutator %.1e, off-diagonal part after diagonalising %.1e" % (info["commutator"], info["residual"]))
    sc = {k: np.abs(v).max() for k, v in W.items()}
    zero = lambda k, i: abs(W[k][i]) < 1e-7 * sc[k]
    Z = [i for i in range(DIM) if zero("s1", i)]
    gen = [i for i in Z if zero("x14", i) and zero("x16", i)]
    plane = [i for i in Z if zero("x16", i)]
    gap = min(abs(W["s1"][i]) for i in range(DIM) if i not in Z) / sc["s1"]
    check("W2 ad(s1) has 46 vanishing weights; 12 of them vanish on x14 and x16 too, and 30 on x16", (len(Z), len(gen), len(plane)) == (46, 12, 30) and gap > 1e-3,
          "%d, %d, %d; the smallest weight of s1 that does not vanish is %.3f of the largest" % (len(Z), len(gen), len(plane), gap))
    # the walls at finite t
    ts = [(-W["x14"][i] / W["x16"][i]) for i in Z if i not in plane]
    groups = collections.defaultdict(list)
    for t in ts:
        groups[(1 if t.imag > 0 else -1, float("%.7g" % abs(t)))].append(t)
    P("   the walls at finite t = -weight(x14)/weight(x16), in the normalisation of B854's invariants:")
    walls = []
    for (sgn, mod), members in sorted(groups.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        t_full = float(np.mean([t.imag for t in members]))          # the wall value at full precision: a rounded one is off the wall
        spread = float(max(abs(t - 1j * t_full) for t in members) / abs(t_full))
        walls.append((t_full, len(members), 12 + len(members)))
        P("      t = %+.10f i   (its weights agree to %.1e): %d weights, nullity %d" % (t_full, spread, len(members), 12 + len(members)))
    real_part = max(abs(t.real) / abs(t) for t in ts)
    check("W3 the walls at finite t are four, all purely imaginary: nullity 14 at a conjugate pair and nullity 18 at another; so on the real line the nullity is 12 at every point but pure x16",
          sorted((m, n) for _, m, n in walls) == [(2, 14), (2, 14), (6, 18), (6, 18)] and real_part < 1e-9 and abs(walls[0][0] + walls[1][0]) < 1e-9 and abs(walls[2][0] + walls[3][0]) < 1e-9,
          "largest real part over modulus %.1e" % real_part)
    # the seven proportionality classes of the active weights, as functionals on the three directions x14, x16, x22
    active = [i for i in Z if not (zero("x14", i) and zero("x16", i) and zero("x22", i))]
    def cls(i):
        v = np.array([W["x14"][i] / sc["x14"], W["x16"][i] / sc["x16"], W["x22"][i] / sc["x22"]])
        j = int(np.argmax(np.abs(v))); v = v / v[j]
        return tuple(np.round(v.real, 6) + 0.0) + tuple(np.round(v.imag, 6) + 0.0)
    classes = collections.Counter(cls(i) for i in active)
    is_real = lambda c: all(abs(x) < 1e-6 for x in c[3:])
    sizes = sorted(classes.values())
    reals = sorted(v for c, v in classes.items() if is_real(c)); nonreal = [c for c in classes if not is_real(c)]
    conj = lambda c: c[:3] + tuple(-x + 0.0 for x in c[3:])
    paired = all(conj(c) in classes and classes[conj(c)] == classes[c] for c in nonreal)
    P("   the active weights on z(s1): %d, in %d proportionality classes of sizes %s; real classes %s; the others in conjugate pairs: %s" % (len(active), len(classes), sizes, reals, paired))
    check("W4 the 34 active weights fall into seven proportionality classes of sizes 2, 2, 6, 6, 6, 6, 6: three real, four in two conjugate pairs (the mechanism B874's addendum records as the solo seat's)",
          len(active) == 34 and sizes == [2, 2, 6, 6, 6, 6, 6] and reals == [6, 6, 6] and len(nonreal) == 4 and paired)
    # a direct rank computation at each wall, beside it, and at real points
    rows, ok = [], True
    for t0, mult, want in walls:
        n, below, above = nullity_direct(Bal, 1j * t0, DIM)
        n_off, _, _ = nullity_direct(Bal, 1j * t0 * 1.001, DIM)
        rows.append(("t = %+.7f i" % t0, n, want)); ok = ok and n == want and n_off == 12 and above > 1e-6
    for tr in (0.0, 0.0515262, -0.046413, 1.0, -7.3, 1e3):
        n, below, above = nullity_direct(Bal, tr, DIM)
        rows.append(("t = %g (real)" % tr, n, 12)); ok = ok and n == 12
    n_inf, _, _ = nullity_direct({"s1": Bal["s1"], "x14": Bal["x16"], "x16": Bal["x14"]}, 0.0, DIM)        # pure x16
    rows.append(("pure x16", n_inf, 30)); ok = ok and n_inf == 30
    for name, n, want in rows:
        P("      direct rank at %-22s nullity %d (from the weights: %d)" % (name, n, want))
    check("W5 a direct rank computation agrees with the count from the weights: at the four walls, just beside each (12), at six real points (12) and at pure x16 (30)", ok)
    RES["numbers"] = dict(info, z_s1=len(Z), generic=len(gen), plane=len(plane), walls=[[float(t), int(m), int(n)] for t, m, n in walls], classes=sizes, real_classes=reals,
                          largest_real_part_over_modulus=float(real_part))
    n = sum(1 for v in RES.values() if isinstance(v, bool)); bad = [k for k, v in RES.items() if v is False]
    P(""); P("CHECKS: %d, FAILING: %d%s" % (n, len(bad), (" -- " + "; ".join(bad)) if bad else ""))
    (HERE / "walls_on_the_line.json").write_text(json.dumps(RES, indent=1) + "\n", encoding="utf-8")
    (HERE / "walls_on_the_line_run.txt").write_text("\n".join(OUT) + "\n", encoding="utf-8")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
