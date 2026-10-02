#!/usr/bin/env python3
"""At a branch point u* of the first member's Higgs curve (root, three-fold cover): the rank-three block representation
R0 = (rho (x) b) + c, with b/c = a the doubly matched sector's character, and the second-order obstruction to
deforming it with both new classes switched on.

G(U) = the two relators evaluated on R(g) = (1 + U_g) R0(g), g in {x, y, t}.  dG is its derivative; first-order
deformations are ker dG; a first-order u1 extends to second order iff  G(eps u1)/eps^2  lies in the image of dG."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
for _d in ("B1444_the_backgrounds_are_ends_of_periodic_curves", "B1445_the_mass_term_on_the_product_of_two_curves"):
    sys.path.insert(0, str(HERE.parents[1] / _d / "verification"))
sys.path.insert(0, str(HERE))
import sys, itertools
import curve_engine as ce
from mpmath import mp, mpf, mpc, matrix, zeros, eye, inverse, sqrt, polyroots, nstr, exp, pi, svd_c, lu_solve, qr_solve, norm
mp.dps = 60
Phi = ce.monodromy(1, "LR", 3); sig = (1, -1, -1); z8 = exp(2j * pi / 8)

def block_rep(u, a, zsign=1, tsign=1):
    Z = zsign * sqrt(1 + 1 / u ** 2); p = (u - 1, -Z, Z); q = ce.tracemap(Phi, p)
    assert all(abs(q[i] - sig[i] * p[i]) < mpf(10) ** (-40) for i in range(3))
    g = ce.rep(p); T = tsign * ce.intertwiner(Phi, g, sig)
    ax, ay = z8 ** a[0], z8 ** a[1]; bx, by = ax ** 3, ay ** 3; cx, cy = ax ** 2, ay ** 2        # b = a^3, c = a^2: b/c = a, b^2 c = 1
    def blk(m2, s, c):
        M = zeros(3)
        for i in range(2):
            for j in range(2): M[i, j] = s * m2[i, j]
        M[2, 2] = c; return M
    R0 = {1: blk(g[1], bx, cx), 2: blk(g[2], by, cy), 3: blk(T, 1, 1)}
    return R0
def word(w, R):
    r = eye(3); inv = {}
    for c in w:
        if c > 0: r = r * R[c]
        else:
            if -c not in inv: inv[-c] = inverse(R[-c])
            r = r * inv[-c]
    return r
def G(R0, U):
    R = {g: (eye(3) + U[g]) * R0[g] for g in (1, 2, 3)}; Ti = inverse(R[3]); out = []
    for g in (1, 2):
        E = R[3] * R[g] * Ti - word(Phi[g], R)
        out += [E[i, j] for i in range(3) for j in range(3)]
    return matrix(out)
def unit(k):
    U = {g: zeros(3) for g in (1, 2, 3)}; g, r = divmod(k, 9); U[g + 1][r // 3, r % 3] = 1; return U
def scale(U, s): return {g: U[g] * s for g in U}
def add(U, V): return {g: U[g] + V[g] for g in U}
def vec(U): return matrix([U[g][i, j] for g in (1, 2, 3) for i in range(3) for j in range(3)])
def m3(vals): return matrix([[vals[3 * i + j] for j in range(3)] for i in range(3)])
def unvec(v): return {g + 1: m3([v[9 * g + k] for k in range(9)]) for g in range(3)}
def dG(R0, delta=mpf(10) ** (-28)):
    base = G(R0, {g: zeros(3) for g in (1, 2, 3)}); assert norm(base) < mpf(10) ** (-30), "R0 is not a representation"
    M = zeros(18, 27)
    for k in range(27):
        col = G(R0, scale(unit(k), delta)) / delta
        for i in range(18): M[i, k] = col[i]
    return M
def nullspace(M, tol=mpf(10) ** (-18)):
    U, S, Vh = svd_c(M, full_matrices=True); r = sum(1 for i in range(len(S)) if abs(S[i]) > tol * abs(S[0]))
    return [matrix([Vh[i, j].conjugate() for j in range(M.cols)]) for i in range(r, M.cols)], r, [abs(S[i]) for i in range(len(S))]
def coboundary(R0, X):
    return {g: X - R0[g] * X * inverse(R0[g]) for g in (1, 2, 3)}
def residual(M, o):
    """distance of o from the image of M, relative to |o|"""
    U, S, Vh = svd_c(M, full_matrices=True); rk = sum(1 for i in range(len(S)) if abs(S[i]) > mpf(10) ** (-18) * abs(S[0]))
    comp = [sum(U[i, k].conjugate() * o[i] for i in range(M.rows)) for k in range(rk, M.rows)]
    return sqrt(sum(abs(c) ** 2 for c in comp)), rk, comp
def analyse(u, a, zsign=1, tsign=1, quiet=False):
    R0 = block_rep(u, a, zsign, tsign); M = dG(R0); ns, rk, S = nullspace(M)
    # coboundaries
    cob = [vec(coboundary(R0, m3([mpc(1) if k == m else mpc(0) for k in range(9)]))) for m in range(9)]
    Cm = zeros(27, 9)
    for m in range(9):
        for i in range(27): Cm[i, m] = cob[m][i]
    Uc, Sc, Vc = svd_c(Cm); rc = sum(1 for i in range(len(Sc)) if abs(Sc[i]) > mpf(10) ** (-18) * abs(Sc[0]))
    h1 = len(ns) - rc; h2 = 18 - rk
    # classes supported in the off-diagonal blocks
    def block_class(entries):
        idx = [9 * g + 3 * i + j for g in range(3) for (i, j) in entries]
        Ms = zeros(18, len(idx))
        for c, k in enumerate(idx):
            for i in range(18): Ms[i, c] = M[i, k]
        nsb, rkb, Sb = nullspace(Ms)
        # remove coboundaries with X in the same block
        cb = [vec(coboundary(R0, m3([mpc(1) if (k // 3, k % 3) == e else mpc(0) for k in range(9)]))) for e in entries]
        full = []
        for v in nsb:
            w = matrix(27, 1)
            for c, k in enumerate(idx): w[k] = v[c]
            full.append(w)
        # class = a null vector not in the span of cb: project out
        B = zeros(27, len(cb))
        for m, c in enumerate(cb):
            for i in range(27): B[i, m] = c[i]
        Ub, Sb2, Vb = svd_c(B, full_matrices=True); rb = sum(1 for i in range(len(Sb2)) if abs(Sb2[i]) > mpf(10) ** (-18))
        best = None
        for w in full:
            comp = w - sum((Ub[:, k] * sum(Ub[i, k].conjugate() * w[i] for i in range(27)) for k in range(rb)), matrix(27, 1))
            if best is None or norm(comp) > norm(best): best = comp
        return len(full) - rb, (best / norm(best) if best is not None and norm(best) > mpf(10) ** (-15) else None)
    nplus, cplus = block_class([(0, 2), (1, 2)]); nminus, cminus = block_class([(2, 0), (2, 1)])
    out = dict(rank_dG=rk, kernel=len(ns), coboundaries=rc, h1=h1, h2=h2, classes_upper=nplus, classes_lower=nminus)
    if cplus is not None and cminus is not None:
        eps = mpf(10) ** (-14)
        def obs(v):
            return G(R0, scale(unvec(v), eps)) / eps ** 2
        for name, v in (("upper alone", cplus), ("lower alone", cminus), ("both", cplus + cminus), ("both, opposite sign", cplus - cminus)):
            o = obs(v); res, rk2, comp = residual(M, o)
            out[name] = dict(norm_of_second_order_term=nstr(norm(o), 8), distance_from_image=nstr(res, 8))
    if not quiet:
        print("u = %s a = %s: rank dG %d, kernel %d, coboundaries %d, h1 = %d, h2 = %d, classes in the upper block %d, in the lower block %d" % (nstr(u, 12), a, rk, len(ns), rc, h1, h2, nplus, nminus))
        for k in ("upper alone", "lower alone", "both", "both, opposite sign"):
            if k in out: print("    %-22s second-order term %s, distance from the image of dG %s" % (k, out[k]["norm_of_second_order_term"], out[k]["distance_from_image"]))
    return out
if __name__ == "__main__":
    roots = polyroots([1, 0, -8, 12, 0, 0, 4], maxsteps=300, extraprec=300)
    real = sorted([r.real for r in roots if abs(r.imag) < mpf(10) ** (-40)])
    print("generic point of the curve (control: no off-diagonal class expected)")
    analyse(mpf("-0.7"), (4, 3))
    print("the real branch point on the arc of real representations")
    analyse(real[1], (4, 3), zsign=1, tsign=1)
    analyse(real[1], (4, 5), zsign=1, tsign=1)
