#!/usr/bin/env python3
"""Construct representations of rank three near the block representation at the real branch point, by Gauss-Newton on
the relator equations from the first-order direction with both off-diagonal classes on; test irreducibility
(Burnside: the matrices generate all of M_3) and read the peripheral holonomy."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
for _d in ("B1444_the_backgrounds_are_ends_of_periodic_curves", "B1445_the_mass_term_on_the_product_of_two_curves"):
    sys.path.insert(0, str(HERE.parents[1] / _d / "verification"))
sys.path.insert(0, str(HERE))
import sys
import curve_engine as ce
import branch_obstruction as bo
from mpmath import mp, mpf, mpc, matrix, zeros, eye, inverse, svd_c, nstr, norm, polyroots, det, sqrt
mp.dps = 60
def jac(R, delta=mpf(10) ** (-28)):
    Z = {g: zeros(3) for g in (1, 2, 3)}; base = bo.G(R, Z); M = zeros(18, 27)
    for k in range(27):
        col = (bo.G(R, bo.scale(bo.unit(k), delta)) - base) / delta
        for i in range(18): M[i, k] = col[i]
    return M, base
def pinv_step(M, b, tol=mpf(10) ** (-14)):
    U, S, Vh = svd_c(M, full_matrices=True); x = matrix(27, 1)
    for k in range(len(S)):
        if abs(S[k]) > tol * abs(S[0]):
            c = sum(U[i, k].conjugate() * b[i] for i in range(18)) / S[k]
            for j in range(27): x[j] += c * Vh[k, j].conjugate()
    return x
def newton(R, iters=40):
    for it in range(iters):
        M, base = jac(R); nb = norm(base)
        if nb < mpf(10) ** (-45): break
        x = pinv_step(M, -base); U = bo.unvec(x); R = {g: (eye(3) + U[g]) * R[g] for g in (1, 2, 3)}
    return R, nb
def burnside(R):
    gens = [R[1], R[2], R[3]]; words = [eye(3)]; span = []
    def rank(vs):
        if not vs: return 0
        M = zeros(len(vs), 9)
        for i, v in enumerate(vs):
            for k in range(9): M[i, k] = v[k // 3, k % 3]
        S = svd_c(M, compute_uv=False); return sum(1 for i in range(len(S)) if abs(S[i]) > mpf(10) ** (-20) * abs(S[0]))
    cur = [eye(3)]; allw = [eye(3)]
    for depth in range(4):
        cur = [w * g for w in cur for g in gens]; allw += cur
        if rank(allw[:120]) == 9: return 9
    return rank(allw[:200])
def periph(R):
    lam = R[1] * R[2] * inverse(R[1]) * inverse(R[2]); T = R[3]
    cp = lambda A: (A[0, 0] + A[1, 1] + A[2, 2], (A * A)[0, 0] + (A * A)[1, 1] + (A * A)[2, 2], det(A))
    return cp(lam), cp(T), lam * T - T * lam
if __name__ == "__main__":
    roots = polyroots([1, 0, -8, 12, 0, 0, 4], maxsteps=300, extraprec=300); ustar = sorted([r.real for r in roots if abs(r.imag) < mpf(10) ** (-40)])[1]
    R0 = bo.block_rep(ustar, (4, 3)); M = bo.dG(R0)
    # the two off-diagonal classes, as in branch_obstruction.analyse
    def cls(entries):
        idx = [9 * g + 3 * i + j for g in range(3) for (i, j) in entries]; Ms = zeros(18, len(idx))
        for c, k in enumerate(idx):
            for i in range(18): Ms[i, c] = M[i, k]
        ns, rk, S = bo.nullspace(Ms); cb = [bo.vec(bo.coboundary(R0, bo.m3([mpc(1) if (k // 3, k % 3) == e else mpc(0) for k in range(9)]))) for e in entries]
        B = zeros(27, len(cb))
        for m, c in enumerate(cb):
            for i in range(27): B[i, m] = c[i]
        Ub, Sb, Vb = svd_c(B, full_matrices=True); rb = sum(1 for i in range(len(Sb)) if abs(Sb[i]) > mpf(10) ** (-18)); best = None
        for v in ns:
            w = matrix(27, 1)
            for c, k in enumerate(idx): w[k] = v[c]
            comp = w - sum((Ub[:, k] * sum(Ub[i, k].conjugate() * w[i] for i in range(27)) for k in range(rb)), matrix(27, 1))
            if best is None or norm(comp) > norm(best): best = comp
        return best / norm(best)
    cp, cm = cls([(0, 2), (1, 2)]), cls([(2, 0), (2, 1)])
    for s in (mpf("0.02"), mpf("0.05"), mpf("0.1")):
        for phase in (1, mpc(0, 1)):
            U = bo.unvec((cp + phase * cm) * s); R = {g: (eye(3) + U[g]) * R0[g] for g in (1, 2, 3)}
            R, res = newton(R)
            off = max(abs(R[g][i, 2]) for g in (1, 2, 3) for i in (0, 1)), max(abs(R[g][2, j]) for g in (1, 2, 3) for j in (0, 1))
            (tl, tl2, dl), (tt, tt2, dt), comm = periph(R)
            print("s = %s phase %s: residual %s | generated algebra has dimension %d | off-diagonal blocks %s, %s | tr lambda %s tr lambda^2 %s | tr T %s | dets %s %s %s" % (
                nstr(s, 3), nstr(phase, 2), nstr(res, 3), burnside(R), nstr(off[0], 4), nstr(off[1], 4), nstr(tl, 10), nstr(tl2, 10), nstr(tt, 10), nstr(det(R[1]), 6), nstr(det(R[2]), 6), nstr(dt, 6)), flush=True)
