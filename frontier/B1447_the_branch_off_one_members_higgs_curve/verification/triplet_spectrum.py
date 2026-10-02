#!/usr/bin/env python3
"""The spectrum of the monodromy on H^1(F; R (x) chi) for the rank-three representations R on the branch off the real
branch point, chi a character of the level: three eigenvalues per triplet."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
for _d in ("B1444_the_backgrounds_are_ends_of_periodic_curves", "B1445_the_mass_term_on_the_product_of_two_curves"):
    sys.path.insert(0, str(HERE.parents[1] / _d / "verification"))
sys.path.insert(0, str(HERE))
import sys, itertools
import curve_engine as ce
import branch_obstruction as bo
import branch_follow as bf
from mpmath import mp, mpf, mpc, matrix, zeros, eye, inverse, svd_c, nstr, norm, polyroots, eig, exp, pi, log, det
mp.dps = 60
Phi = bo.Phi
def monodromy_on_H1(h, T):
    n = T.rows; xx, xy, _ = ce.fox(Phi[1], h); yx, yy, _ = ce.fox(Phi[2], h); Ti = inverse(T)
    P = zeros(2 * n); blocks = ((Ti * xx, Ti * xy), (Ti * yx, Ti * yy))
    for I in range(2):
        for J in range(2):
            for a in range(n):
                for b in range(n): P[n * I + a, n * J + b] = blocks[I][J][a, b]
    Bm = zeros(2 * n, n)
    for a in range(n):
        for b in range(n): Bm[a, b] = h[1][a, b] - (a == b); Bm[n + a, b] = h[2][a, b] - (a == b)
    U, S, Vh = svd_c(Bm, full_matrices=True); assert abs(S[n - 1]) > mpf(10) ** (-20), "invariants on the fibre"
    Q = zeros(n, 2 * n)
    for r in range(n):
        for c in range(2 * n): Q[r, c] = U[c, n + r].conjugate()
    QP = Q * P; Pb = QP * (Q.H * inverse(Q * Q.H))
    assert max(abs((QP - Pb * Q)[i, j]) for i in range(n) for j in range(2 * n)) < mpf(10) ** (-25)
    E, _ = eig(Pb); return sorted(E, key=lambda e: (abs(e), e.real, e.imag)), det(eye(n) - Pb)
def branch_rep(s, phase=1):
    roots = polyroots([1, 0, -8, 12, 0, 0, 4], maxsteps=300, extraprec=300); ustar = sorted([r.real for r in roots if abs(r.imag) < mpf(10) ** (-40)])[1]
    R0 = bo.block_rep(ustar, (4, 3))
    if s == 0: return R0, R0
    M = bo.dG(R0)
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
    U = bo.unvec((cp + phase * cm) * s); R = {g: (eye(3) + U[g]) * R0[g] for g in (1, 2, 3)}
    R, res = bf.newton(R); assert res < mpf(10) ** (-40)
    return R, R0
if __name__ == "__main__":
    z4 = exp(2j * pi / 4)
    for s in (0, mpf("0.02"), mpf("0.05"), mpf("0.1"), mpf("0.2")):
        R, R0 = branch_rep(s)
        print("s = %s   (algebra dimension %d; tr lambda %s; tr T %s)" % (nstr(s, 3), bf.burnside(R), nstr(R[1].rows and (R[1] * R[2] * inverse(R[1]) * inverse(R[2]))[0, 0] + (R[1] * R[2] * inverse(R[1]) * inverse(R[2]))[1, 1] + (R[1] * R[2] * inverse(R[1]) * inverse(R[2]))[2, 2], 8), nstr(R[3][0, 0] + R[3][1, 1] + R[3][2, 2], 8)), flush=True)
        for (i, j) in itertools.product(range(4), repeat=2):
            h = {1: z4 ** i * R[1], 2: z4 ** j * R[2]}
            try: E, tau = monodromy_on_H1(h, R[3])
            except AssertionError as ex: print("   chi=(%d,%d): %s" % (i, j, str(ex)[:40])); continue
            print("   chi=(%d,%d): eigenvalues %s   |log| = %s   torsion %s" % (i, j, [nstr(e, 7) for e in E], [nstr(abs(log(e)), 5) for e in E], nstr(tau, 6)), flush=True)
