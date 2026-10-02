#!/usr/bin/env python3
"""On the irreducible rank-three branch: the points where the meridian has a single eigenvalue (parabolic up to a
scalar).  Homotopy: solve  G = 0,  f(T) = (1 - tau) f0  for tau from 0 to 1, f = (c1^2 - 3 c2, c1 c2 - 9 c3) the two
conditions for a triple root of the characteristic polynomial of T."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
for _d in ("B1444_the_backgrounds_are_ends_of_periodic_curves", "B1445_the_mass_term_on_the_product_of_two_curves"):
    sys.path.insert(0, str(HERE.parents[1] / _d / "verification"))
sys.path.insert(0, str(HERE))
import sys, itertools
import curve_engine as ce
import branch_obstruction as bo, branch_follow as bf, triplet_spectrum as ts
from mpmath import mp, mpf, mpc, matrix, zeros, eye, inverse, svd_c, nstr, norm, det, exp, pi, log, eig
mp.dps = 60
def coeffs(T):
    c1 = T[0, 0] + T[1, 1] + T[2, 2]; T2 = T * T; c2 = (c1 * c1 - (T2[0, 0] + T2[1, 1] + T2[2, 2])) / 2; return c1, c2, det(T)
def f(R):
    c1, c2, c3 = coeffs(R[3]); return [c1 * c1 - 3 * c2, c1 * c2 - 9 * c3]
def step(R, target, delta=mpf(10) ** (-28)):
    Z = {g: zeros(3) for g in (1, 2, 3)}; base = bo.G(R, Z); f0 = f(R); M = zeros(20, 27)
    for k in range(27):
        U = bo.scale(bo.unit(k), delta); Rk = {g: (eye(3) + U[g]) * R[g] for g in (1, 2, 3)}
        col = (bo.G(R, U) - base) / delta; fk = f(Rk)
        for i in range(18): M[i, k] = col[i]
        for i in range(2): M[18 + i, k] = (fk[i] - f0[i]) / delta
    b = matrix(20, 1)
    for i in range(18): b[i] = -base[i]
    for i in range(2): b[18 + i] = target[i] - f0[i]
    U_, S, Vh = svd_c(M, full_matrices=True); x = matrix(27, 1)
    for k in range(len(S)):
        if abs(S[k]) > mpf(10) ** (-12) * abs(S[0]):
            c = sum(U_[i, k].conjugate() * b[i] for i in range(20)) / S[k]
            for j in range(27): x[j] += c * Vh[k, j].conjugate()
    U = bo.unvec(x); return {g: (eye(3) + U[g]) * R[g] for g in (1, 2, 3)}, norm(b), norm(x)
def solve(R, target, iters=12):
    for it in range(iters):
        R, nb, nx = step(R, target)
        if nb < mpf(10) ** (-45): break
        if nx > 5: raise AssertionError("step too large")
    return R, nb
def homotopy(R, K=24):
    f0 = f(R)
    for k in range(1, K + 1):
        tgt = [(1 - mpf(k) / K) * c for c in f0]
        R, nb = solve(R, tgt)
        print("      step %d/%d residual %s  f = %s" % (k, K, nstr(nb, 3), [nstr(c, 5) for c in f(R)]), flush=True)
        if nb > mpf(10) ** (-30): raise AssertionError("not converged at step %d: %s" % (k, nstr(nb, 3)))
    return R
def report(R, tag):
    lam = R[1] * R[2] * inverse(R[1]) * inverse(R[2]); ET, _ = eig(R[3]); EL, _ = eig(lam)
    comm = norm(lam * R[3] - R[3] * lam); dim = bf.burnside(R)
    N1 = R[3] - ET[0] * eye(3); rkN = sum(1 for sv in svd_c(N1, compute_uv=False) if abs(sv) > mpf(10) ** (-15))
    print("%s: algebra dimension %d | eigenvalues of T %s (rank of T - t0: %d) | eigenvalues of lambda %s | residual %s" % (tag, dim, [nstr(e, 9) for e in ET], rkN, [nstr(e, 9) for e in EL], nstr(norm(bo.G(R, {g: zeros(3) for g in (1, 2, 3)})), 3)), flush=True)
    z4 = exp(2j * pi / 4); out = []
    for (i, j) in ((0, 0), (1, 0), (1, 1), (2, 0), (0, 2), (0, 1)):
        try:
            E, tau = ts.monodromy_on_H1({1: z4 ** i * R[1], 2: z4 ** j * R[2]}, R[3] / (det(R[3]) ** (mpf(1) / 3)))
            print("     chi=(%d,%d): eigenvalues %s   |log| = %s   torsion %s" % (i, j, [nstr(e, 9) for e in E], [nstr(abs(log(e)), 7) for e in E], nstr(tau, 9)), flush=True)
        except AssertionError as ex: print("     chi=(%d,%d): %s" % (i, j, str(ex)[:50]))
if __name__ == "__main__":
    for s, phase in ((mpf("0.2"), 1), (mpf("0.2"), mpc(0, 1)), (mpf("0.3"), -1), (mpf("0.15"), mpc(0, -1))):
        try:
            R, R0 = ts.branch_rep(s, phase); f0 = f(R)
            print("start s = %s phase %s: f = %s" % (nstr(s, 3), nstr(phase, 2), [nstr(c, 6) for c in f0]), flush=True)
            Rp = homotopy(R); report(Rp, "   parabolic point")
        except AssertionError as ex:
            print("   start s = %s phase %s: %s" % (nstr(s, 3), nstr(phase, 2), str(ex)[:80]), flush=True)
