"""B1957: the physical lane's package 'agy-exp endgame review' (2026-11-15), its review of another seat's X-ENDGAME
campaign: the mathematics of its findings, on main.  The lane's own checker and the other seat's scripts are not run;
that seat's notes are read as text.
 E0  custody (needs that seat's branch fetched): four sentences the review quotes are at the lines it cites.
 E1  the mapping torus of the punctured torus by M = [[2, 1], [1, 1]]: with one 0-cell, three 1-cells (a, b, t) and two
     2-cells, the boundary matrix is [[1, 1], [1, 0], [0, 0]], of rank 2: H_2 = 0, H_1 = Z, so H^2 = 0; the closed
     fibre's extra 2-cell gives one more class in degree 3 and leaves H_2 = Z.
 E2  M^4 - 1 = [[33, 21], [21, 12]]: gcd 3, determinant -45, Smith form (3, 15); its 45 fixed points split by exact
     order as 1 + 8 + 4 + 32 (orders 1, 3, 5, 15); M has 8 orbits and J four on the 32, and -1 sixteen.
 E3  the two orders of the mixed products differ by (3/4)[H_u, H_d] Y_u (and -(3/4)[H_u, H_d] Y_d), which changes the
     rate of Tr(H_u H_d) by (3/2) Tr([H_u, H_d]^2) and vanishes on commuting inputs.
 E4  S(A) = c A + 2 pi^2 I^2 / A is stationary at A = sqrt(2) pi |I| / sqrt(c): 6 pi, 6 sqrt 2 pi, 3 sqrt 2 pi at
     I = 3 and c = 1/2, 1/4, 1.
 E5  on [0, L] the normalised values of exp(k t) and exp(-k t) at L have ratio exp(k L).
 E6  arg det(Y U^dagger) = arg det Y - arg det U: the raw phase of det(Y_u Y_d) moves under right unitaries."""
import functools, itertools, subprocess, math
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
print = functools.partial(print, flush=True)

if __name__ == "__main__":
    C = "b05424e99"; cites = [("relays/AGY_EXP_TO_CC_2026-11-15_X_ENDGAME_1_RESULTS.md", 15, "H^2(M_3; \\mathbb{Z})"), ("relays/AGY_EXP_TO_CC_2026-11-15_X_ENDGAME_1_RESULTS.md", 19, "Requiring all three chiral Landau generations to close periodically around the base"),
                               ("relays/AGY_EXP_TO_CC_2026-11-15_X_ENDGAME_5_RESULTS.md", 16, "13/2"), ("relays/AGY_EXP_TO_CC_2026-11-15_X_ENDGAME_3_RESULTS.md", 25, "requires vector-like parity completion")]
    if subprocess.run(["git", "cat-file", "-e", C], capture_output=True).returncode == 0:
        got = []
        for path, ln, frag in cites:
            b = subprocess.run(["git", "show", "%s:%s" % (C, path)], capture_output=True).stdout.decode("utf-8", "replace").split("\n"); got.append(ln <= len(b) and frag in b[ln - 1])
        print("E0: the quoted sentences at their cited lines: %s" % got)
    else: print("E0: that seat's branch is not fetched here; custody not checked")
    d2 = sp.Matrix([[1, 1], [1, 0], [0, 0]]); r2 = d2.rank(); snf = smith_normal_form(sp.Matrix([[1, 1], [1, 0]]), domain=sp.ZZ)
    print("E1: the boundary matrix has rank %d of 2 columns: H_2 = Z^%d; H_1 = Z^%d plus torsion of order %d (Smith form %s); with the closed fibre's 2-cell (boundary 0, and M acts on it by det M = 1) H_2 gains one class: Z^%d" % (r2, 2 - r2, 3 - r2, abs(sp.Matrix([[1, 1], [1, 0]]).det()), [snf[i, i] for i in range(2)], 2 - r2 + 1))
    M = sp.Matrix([[2, 1], [1, 1]]); M4 = M ** 4 - sp.eye(2); s4 = smith_normal_form(M4, domain=sp.ZZ)
    # the fixed points of M^4 on the torus: the group Z/3 x Z/15
    cnt = {}
    for a in range(3):
        for b in range(15):
            o = sp.ilcm(3 // math.gcd(3, a) if a else 1, 15 // math.gcd(15, b) if b else 1); cnt[int(o)] = cnt.get(int(o), 0) + 1
    mul = lambda X, Y, n: tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) % n for j in range(2)) for i in range(2)); act = lambda w, X, n: tuple(sum(w[k] * X[k][j] for k in range(2)) % n for j in range(2))
    Mt, Jt, neg = ((2, 1), (1, 1)), ((1, 1), (1, 0)), ((-1, 0), (0, -1)); line5 = [(k, 2 * k % 5) for k in range(1, 5)]; p3 = [(a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0)]
    def norb(X):
        left = {(a, b) for a in line5 for b in p3}; n = 0
        while left:
            w = left.pop(); n += 1; v = (act(w[0], X, 5), act(w[1], X, 3))
            while v != w: left.discard(v); v = (act(v[0], X, 5), act(v[1], X, 3))
        return n
    print("E2: M^4 - 1 = %s; determinant %s; Smith form %s; fixed points by exact order: %s; orbits on the 32 points under M, J and -1: %d, %d, %d" % (M4.tolist(), M4.det(), sorted(abs(s4[i, i]) for i in range(2)), dict(sorted(cnt.items())), norb(Mt), norb(Jt), norb(neg)))
    rng = np.random.default_rng(52); herm = lambda: (lambda A: A @ A.conj().T)(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))); Hu, Hd = herm(), herm(); X = Hu @ Hd - Hd @ Hu
    diff_u = (-0.25 * Hu @ Hd - Hd @ Hu) - (-Hu @ Hd - 0.25 * Hd @ Hu); diff_d = (-0.25 * Hd @ Hu - Hu @ Hd) - (-Hd @ Hu - 0.25 * Hu @ Hd)
    dHu = 0.75 * (X @ Hu + Hu @ X.conj().T); dHd = -0.75 * (X @ Hd + Hd @ X.conj().T); rate = np.trace(dHu @ Hd + Hu @ dHd).real
    print("E3: the up-sector difference of the two orders minus (3/4)[H_u, H_d]: %.1e; the down-sector one plus it: %.1e; the change of the rate of Tr(H_u H_d): %.6f against (3/2) Tr([H_u, H_d]^2) = %.6f" % (np.abs(diff_u - 0.75 * X).max(), np.abs(diff_d + 0.75 * X).max(), rate, 1.5 * np.trace(X @ X).real))
    A, c, I = sp.symbols("A c I", positive=True); st = sp.solve(sp.diff(c * A + 2 * sp.pi ** 2 * I ** 2 / A, A), A)[0]
    print("E4: the stationary area: %s; at I = 3 and c = 1/2, 1/4, 1: %s" % (st, [sp.simplify(st.subs({I: 3, c: cv})) for cv in (sp.Rational(1, 2), sp.Rational(1, 4), 1)]))
    k, L, t = sp.symbols("k L t", positive=True); nrm = lambda f: sp.sqrt(sp.integrate(f ** 2, (t, 0, L))); ratio = sp.simplify((sp.exp(k * L) / nrm(sp.exp(k * t))) / (sp.exp(-k * L) / nrm(sp.exp(-k * t))) / sp.exp(k * L))
    print("E5: the ratio of the two normalised end values over exp(k L): %s" % sp.simplify(ratio))
    Y = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); U = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))[0]; ang = lambda z: np.angle(z)
    print("E6: arg det(Y U^dagger) - arg det Y + arg det U = %.1e (modulo 2 pi)" % abs(np.exp(1j * (ang(np.linalg.det(Y @ U.conj().T)) - ang(np.linalg.det(Y)) + ang(np.linalg.det(U)))) - 1))
