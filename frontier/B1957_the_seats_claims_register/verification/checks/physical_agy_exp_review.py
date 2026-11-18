"""B1957: the physical lane's package 'agy-exp review' (2026-11-15), its source and premise review of another seat's
X-FUNNEL campaign: the mathematics of its eight findings and of the derivations it retains, on main.  The other
seat's notes and scripts are read as text; nothing is run.
 R0  custody (needs that seat's branch fetched): the eight sentences the review quotes are at the lines it cites.
 R1  M = [[2, 1], [1, 1]] has order 4 modulo 3 (M^2 = -1), with two orbits of four on the non-zero points; its root
     J = [[1, 1], [1, 0]] has order 8 and joins them; det(M - 1) = -1; on the 4 x 8 points (the order-five line times
     the non-zero order-three points) M has eight orbits of four and J four orbits of eight; 192 points of order 15.
 R2  the area of the modular fundamental domain in dx dy/y^2 is pi/3.
 R4  a point source: r |log r|^2 is integrable at 0 and r |d/dr log r|^2 = 1/r is not.
 R5  averaging: two copies of H+ = [[2, 1], [1, 2]] + (1) average to eigenvalues (3, 1, 1); with the second fibre's frame
     changed by D = diag(1, -1, 1) the average is diag(2, 2, 1).
 R6  one loop, diagonal inputs with the down and lepton matrices coinciding: d/dt log[(d_i/d_j)/(e_i/e_j)] =
     -(3/(32 pi^2))(h_i - h_j), on main's own running (sm_rge_matrix.py); so H_u = diag(1/4, 1/16, 1) gives opposite
     consecutive skews.
 R7  a term kappa [H_u, H_d] Y_u vanishes on commuting inputs and changes d/dt Tr(H_u H_d) by kappa Tr([H_u, H_d]^2).
 R8  the two Zak formulas: successive ratios exp(2 pi i q b) and exp(-2 pi i q b/3) differ at q = 1, b = 2/5.
 R9  retained: modulo 5, (M + 1)^2 = 0 with kernel (k, 2k), w M^-1 = -w there, J^-1 takes k to 2k, the other twenty points
     have period ten; 1/15 = 2/5 - 1/3; sum over k of B6(k/N) = N^-5 B6(0); the means -26/625 and -781/3125 and the
     coefficients 17236/625 and 142166/3125; and sum over non-zero N-torsion of log det = 2 log N from zeta_0(0) = -1."""
import functools, itertools, subprocess, math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import sm_rge_matrix as RG

if __name__ == "__main__":
    C = "d6f77f7ff"; cites = [("relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_4_RESULTS.md", 62, "has order `8`"), ("relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_3_RESULTS.md", 44, "\\pi/3"), ("relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_1_RESULTS.md", 36, "I_L = +3"), ("relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_1_RESULTS.md", 36, "chiral generations by Riemann"),
                               ("relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_3_RESULTS.md", 44, "applied at every"), ("relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_4_RESULTS.md", 42, "generate opposite consecutive skew"), ("relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_4_RESULTS.md", 21, "matrices"), ("relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_2_RESULTS.md", 40, "(k + 3a)")]
    got = []
    for path, ln, frag in cites:
        b = subprocess.run(["git", "show", "%s:%s" % (C, path)], capture_output=True).stdout.decode("utf-8", "replace").split("\n"); got.append(bool(b) and ln <= len(b) and frag in b[ln - 1])
    print("R0: the eight quoted sentences at their cited lines: %d of %d" % (sum(got), len(got)) if any(got) or subprocess.run(["git", "cat-file", "-e", C], capture_output=True).returncode == 0 else "R0: that seat's branch is not fetched here; custody not checked")
    mul = lambda X, Y, n: tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) % n for j in range(2)) for i in range(2)); I2 = ((1, 0), (0, 1)); M = ((2, 1), (1, 1)); J = ((1, 1), (1, 0))
    def order(X, n):
        P = tuple(tuple(x % n for x in r) for r in X); k = 1
        while P != I2: P = mul(P, X, n); k += 1
        return k
    act = lambda w, X, n: tuple(sum(w[k] * X[k][j] for k in range(2)) % n for j in range(2))
    def orbits(pts, X, n):
        left = set(pts); out = []
        while left:
            w = left.pop(); o = [w]; v = act(w, X, n)
            while v != w: o.append(v); left.discard(v); v = act(v, X, n)
            out.append(len(o))
        return sorted(out)
    p3 = [(a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0)]; line5 = [(k, 2 * k % 5) for k in range(1, 5)]
    # the 32 points of order 15: pairs (w5, w3) by the Chinese remainder theorem
    def orb15(X):
        left = {(a, b) for a in line5 for b in p3}; out = []
        while left:
            w = left.pop(); n = 1; v = (act(w[0], X, 5), act(w[1], X, 3))
            while v != w: left.discard(v); n += 1; v = (act(v[0], X, 5), act(v[1], X, 3))
            out.append(n)
        return sorted(out)
    p5 = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]; N5 = tuple(tuple((M[i][j] + I2[i][j]) % 5 for j in range(2)) for i in range(2)); Minv5 = ((1, 4), (4, 2)); Jinv5 = ((0, 1), (1, 4))
    assert mul(M, Minv5, 5) == I2 and mul(J, Jinv5, 5) == I2
    print("R1: M^2 mod 3 = %s; orders mod 3: M %d, J %d; J^2 = M: %s; M's orbits on the non-zero points mod 3: %s, J's: %s; det(M - 1) = %d; on the 32 points M has orbits %s and J %s; points of exact order 15: %d" % (
        mul(M, M, 3), order(M, 3), order(J, 3), mul(J, J, 1000) == M, orbits(p3, M, 3), orbits(p3, J, 3), (M[0][0] - 1) * (M[1][1] - 1) - M[0][1] * M[1][0], orb15(M), orb15(J), 24 * 8))
    x = sp.symbols("x", real=True); area = sp.integrate(1 / sp.sqrt(1 - x ** 2), (x, -sp.Rational(1, 2), sp.Rational(1, 2)))
    r = sp.symbols("r", positive=True); eps = sp.symbols("epsilon", positive=True)
    print("R2: the area: %s. R4: int_0^eps r log(r)^2 dr = %s (finite); int_delta^eps dr/r = log(eps/delta), unbounded as delta -> 0" % (area, sp.simplify(sp.integrate(r * sp.log(r) ** 2, (r, 0, eps)))))
    Hp = np.array([[2, 1, 0], [1, 2, 0], [0, 0, 1.0]]); Dd = np.diag([1, -1, 1.0]); print("R5: eigenvalues of the average of two copies: %s; with the second frame changed: %s" % (np.round(np.linalg.eigvalsh(Hp), 6).tolist(), np.round(np.linalg.eigvalsh((Hp + Dd @ Hp @ Dd) / 2), 6).tolist()))
    hu = np.array([0.25, 0.0625, 1.0]); dd = np.array([0.02, 0.05, 0.11]); v = RG.pack([0.4, 0.6, 1.1], np.diag(np.sqrt(hu)).astype(complex), np.diag(dd).astype(complex), np.diag(dd).astype(complex), 0.2)
    g, Hm, FD, FL, lam = RG.unpack(v); gd, dH, dFD, dFL, dl = RG.unpack(RG.rhs(0.0, v, 1)); rate = lambda i, j: float(((dFD[i, i] / FD[i, i]) - (dFD[j, j] / FD[j, j]) - (dFL[i, i] / FL[i, i]) + (dFL[j, j] / FL[j, j])).real)
    hh = np.real(np.diag(Hm.conj().T @ Hm)); pred = lambda i, j: -3 / (32 * math.pi ** 2) * (hh[i] - hh[j])
    print("R6: on main's one-loop running: the rate of log[(d_i/d_j)/(e_i/e_j)] at (1, 2) and (2, 3): %.6e, %.6e; -(3/(32 pi^2))(h_i - h_j): %.6e, %.6e; they have opposite signs: %s" % (rate(0, 1), rate(1, 2), pred(0, 1), pred(1, 2), rate(0, 1) * rate(1, 2) < 0))
    rng = np.random.default_rng(51); herm = lambda: (lambda A: A + A.conj().T)(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))); Hu, Hd = herm(), herm(); cm = Hu @ Hd - Hd @ Hu
    lhs = np.trace((cm @ Hu + Hu @ cm.conj().T) @ Hd).real; Da, Db = np.diag(rng.normal(size=3)), np.diag(rng.normal(size=3))
    print("R7: Tr(delta(dH_u/dt) H_d) = %.6f against Tr([H_u, H_d]^2) = %.6f (kappa = 1); on commuting inputs the term is %.1e" % (lhs, np.trace(cm @ cm).real, np.abs(Da @ Db - Db @ Da).max()))
    q, b = 1, Fr(2, 5); print("R8: the two successive ratios as fractions of a turn: %s and %s" % (q * b % 1, (-q * b / 3) % 1))
    Nsq = mul(N5, N5, 5); ker = [w for w in p5 if act(w, N5, 5) == (0, 0)]; per = orbits([w for w in p5 if w not in ker], M, 5)
    B6 = lambda t: t ** 6 - 3 * t ** 5 + Fr(5, 2) * t ** 4 - Fr(1, 2) * t ** 2 + Fr(1, 42); mult = sum(B6(Fr(k, 5)) for k in range(5)) == Fr(1, 5 ** 5) * B6(Fr(0))
    m24 = (Fr(1, 5 ** 4) - 1) / 24; m4 = (Fr(1, 5 ** 5) - 1) / 4
    print("R9: (M + 1)^2 mod 5 = %s; its kernel: %s; w M^-1 = -w on it: %s; J^-1 on it: %s; the other twenty points' periods: %s; 2/5 - 1/3 = %s; the multiplication theorem at N = 5: %s; the two means %s and %s; the two coefficients %s and %s; d/ds[(N^(2s) - 1) zeta_0(s)] at 0 with zeta_0(0) = -1 is -2 log N, so the sum of log det is 2 log N" % (
        Nsq, sorted(ker), all(act(w, Minv5, 5) == tuple((-c) % 5 for c in w) for w in ker), {w[0]: act(w, Jinv5, 5)[0] for w in sorted(ker)}, per, Fr(2, 5) - Fr(1, 3), mult, m24, m4, 24 - 86 * m24, 24 - 86 * m4))
