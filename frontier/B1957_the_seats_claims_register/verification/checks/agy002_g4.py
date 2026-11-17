"""B1957: agy-002's gate 4, recomputed by main.  Data-free: the inputs are the seat's stated matrices and counts.
G4.1  the mixing angle of a rank-one top and bottom under the two-loop Yukawa flow, at several angles, on main's own
      running (sm_rge_matrix.py, transcribed from Luo and Xiao): d ln(tan theta)/dt = (3/2)(yt^2 + yb^2) at one loop and
      -(13/2)(yt^4 + yb^4) - (11/2) yt^2 yb^2 at two loops, the same at every angle.
G4.2  strong CP: Hermitian Yukawa matrices with a complex phase in the mixing, run down 30 e-folds.
G4.3  the linear algebra of the seat's section 2, each item recomputed, in general form where the item is general.
G4.4  the anomaly polynomials of one 16 of Spin(10) on the plane of the two abelian charges.
G4.5  the Casimir count for E6 -> SU(4) x SU(2) x SU(2), and the curve."""
import sys, pathlib, math, itertools
from fractions import Fraction as F
import functools, numpy as np, sympy as sp, mpmath as mp
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import sm_rge_matrix as R
K = R.K

if __name__ == "__main__":
    # G4.1
    e_t = np.array([0, 0, 1.0]); yt, yb = 0.9, 0.6; worst1 = worst2 = 0.0; want1 = 1.5 * (yt ** 2 + yb ** 2); want2 = -6.5 * (yt ** 4 + yb ** 4) - 5.5 * yt ** 2 * yb ** 2
    def lntan(v):
        g, H, FD, FL, lam = R.unpack(v); tu = np.linalg.eigh(H.conj().T @ H)[1][:, -1]; td = np.linalg.eigh(FD.conj().T @ FD)[1][:, -1]
        c = min(1.0, abs(np.vdot(tu, td))); return math.log(math.sqrt(1 - c * c) / c)
    for th in (0.2, 0.7, 1.2, 1.5):
        e_b = np.array([0, np.sin(th), np.cos(th)]); v = R.pack([0, 0, 0], yt * np.outer(e_t, e_t), yb * np.outer(e_b, e_b), np.zeros((3, 3)), 0.0); e = 1e-3
        d = lambda loops, sw=False: (lntan(v + e * R.rhs(0, v, loops, sw)) - lntan(v - e * R.rhs(0, v, loops, sw))) / (2 * e)
        one = d(1) / K; two = (d(2) - d(1)) / K ** 2; worst1 = max(worst1, abs(one - want1)); worst2 = max(worst2, abs(two - want2))
    print("G4.1: d ln(tan theta)/dt at angles 0.2, 0.7, 1.2, 1.5: one loop against (3/2)(yt^2 + yb^2): %.1e; two loops against -(13/2)(yt^4 + yb^4) - (11/2) yt^2 yb^2 = %.4f: %.1e" % (worst1, want2, worst2))
    # G4.2
    rng = np.random.default_rng(20261117)
    def herm_pos():
        q, r = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))); return q @ np.diag(rng.uniform(0.05, 0.6, 3)) @ q.conj().T
    worst = 0.0; jmin = 1.0
    for _ in range(5):
        Yu, Yd = herm_pos(), herm_pos(); v0 = R.pack([0.5, 0.55, 0.6], Yu, Yd, herm_pos(), 0.3); v1 = R.run(v0, -30.0, rtol=1e-12)
        g, H, FD, FL, lam = R.unpack(v1); worst = max(worst, abs(np.angle(np.linalg.det(H) * np.linalg.det(FD))))
        Vu = np.linalg.eigh(H.conj().T @ H)[1]; Vd = np.linalg.eigh(FD.conj().T @ FD)[1]; V = Vu.conj().T @ Vd
        jmin = min(jmin, abs((V[0, 0] * V[1, 1] * V[0, 1].conj() * V[1, 0].conj()).imag))
    print("G4.2: five random pairs of Hermitian positive Yukawa matrices (so arg det = 0 at the start), run down 30 e-folds: |arg det(Y_u Y_d)| at the end at most %.1e; the Jarlskog invariant at the end at least %.1e" % (worst, jmin))
    # G4.3
    n = 3; A = sp.Matrix(n, n, lambda i, j: sp.Symbol("a%d%d" % (i, j))); z = sp.Matrix(n, 1, lambda i, j: sp.Symbol("z%d" % i)); w = sp.Matrix(n, 1, lambda i, j: sp.Symbol("w%d" % i))
    bil = sp.simplify(((A * z).T * (A.inv().T * w))[0] - (z.T * w)[0])
    print("G4.3: for a general invertible 3 x 3 matrix, (A z)^T (A^-T w) = z^T w: %s (the Gram identity is the same statement with the adjoint)" % (bil == 0))
    I2 = sp.eye(2); qi = sp.Matrix([[sp.I, 0], [0, -sp.I]]); qj = sp.Matrix([[0, 1], [-1, 0]]); qk = qi * qj; Q8 = [I2, -I2, qi, -qi, qj, -qj, qk, -qk]
    print("      ordered pairs of the quaternion group that do not commute: %d (the seat: 24); the profile z/(1 + z^2) is odd and a half-turn on a spinor squares to -1: elementary" % sum(1 for g in Q8 for h in Q8 if g * h != h * g))
    t = sp.Symbol("t"); D0 = sp.Matrix([[3, 1, 0], [0, 4, 2], [1, 0, 5]]); D1 = sp.Matrix([[1, 2, -1], [3, 0, 1], [0, -2, 2]])
    V1 = sp.Matrix([[2, 0, 1], [0, 3, 0], [0, 0, 0]]); V2 = sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 2, 1]]); Bm = sp.Matrix([[1, 0, 2], [0, 1, -1], [2, 1, 1]]); Cm = sp.Matrix([[1, 1, 0], [-1, 2, 1], [0, 1, 3]])
    M6 = sp.Matrix(sp.BlockMatrix([[t * V1 + t ** 2 * V2, t * Bm], [t * Cm, D0 + t * D1]])); Y2 = V2 - Bm * D0.inv() * Cm; Y3 = Bm * D0.inv() * D1 * D0.inv() * Cm
    Meff = t * V1 + t ** 2 * Y2 + t ** 3 * Y3
    exact = all(sp.Rational(M6.subs(t, tv).det()) == (D0 + tv * D1).det() * (tv * V1 + tv ** 2 * V2 - tv ** 2 * Bm * (D0 + tv * D1).inv() * Cm).det() for tv in (sp.Rational(1, 7), sp.Rational(-2, 5), sp.Rational(3, 11), sp.Rational(1, 100), sp.Rational(5, 3), sp.Rational(-7, 9), sp.Rational(2, 13)))   # degree at most 6 in t: seven points decide it
    low = sp.series(sp.expand(M6.det() - Meff.det() * (D0 + t * D1).det()), t, 0, 6).removeO() == 0
    print("      the seat's 6 x 6 block matrix: det M = det D(t) det(t V1 + t^2 V2 - t^2 B D(t)^-1 C) at seven rational t (both sides, cleared of det D(t)^2, are polynomials of degree at most 12; see the note): %s; and the third-order M_eff reproduces det M through t^5: %s" % (exact, low))
    p3 = sum(x ** 2 for x in (Y2 - (V2 - Bm * D0.T.inv() * Cm))); p4 = sum(x ** 2 for x in (Y3 - Bm * D1 * D0.inv() * D0.inv() * Cm))
    print("      planted: the transposed inverse changes Y2 by %s in squared norm (the seat: 1245/1922); the reversed order changes Y3 by %s (the seat: 698707/1847042)" % (p3, p4))
    mp.mp.dps = 80; l = mp.matrix([0, 0, 1]); r = mp.matrix([1, 0, -2]) / mp.sqrt(5); pred = abs((l.T * mp.matrix(Y2.tolist()) * r)[0])
    for ex in (5, 6):
        Mn = mp.matrix(M6.subs(t, sp.Rational(1, 10 ** ex)).tolist()); smin = min(mp.svd_r(Mn, compute_uv=False)); print("      least singular value of M at t = 1e-%d, over t^2, against |l^T Y2 r| = %s: relative difference %s (80 digits; the seat's double precision gave 5.4e-5 against its bar 1e-5)" % (ex, mp.nstr(pred, 8), mp.nstr(abs(smin * 10 ** (2 * ex) - pred) / pred, 3)))
    qI = np.array([[1j, 0], [0, -1j]]); qJ = np.array([[0, 1], [-1, 0]], complex); qK = qI @ qJ; eps = qJ; blocks = [qJ, qI, qK]
    E = lambda i, j: np.array([[1.0 if (a, b) == (i, j) else 0.0 for b in range(2)] for a in range(2)], complex)
    tl = [E(0, 0) - E(1, 1), E(0, 1), E(1, 0)]; fb = [E(0, 0), E(0, 1), E(1, 0), E(1, 1)]
    y3 = lambda S, M: np.array([np.trace(M.T @ (ca.T @ eps @ S @ cb)) for ca in blocks for cb in blocks])
    rk = lambda rows: int(np.linalg.matrix_rank(np.array(rows), tol=1e-10))
    s1 = rk([y3(S, M) for S in tl for M in fb]); s2 = rk([y3(fb[i] + fb[j], eps @ (fb[i] + fb[j])) for i in range(4) for j in range(i, 4)]); s3 = rk([y3(tl[i] + tl[j], eps @ (tl[i] + tl[j])) for i in range(3) for j in range(i, 3)])
    def nullity(e33):
        mats = [(0, 2), (1, 2), (2, 0), (2, 1)] + ([(2, 2)] if e33 else []); rows = []
        for (rr, cc) in mats:
            Mv = np.zeros((3, 3)); Mv[rr, cc] = 1
            for i in range(3):
                for j in range(3):
                    row = np.zeros(18)
                    for k in range(3): row[3 * i + k] += Mv[k, j]; row[9 + 3 * k + j] -= Mv[i, k]
                    rows.append(row)
        return 18 - int(np.linalg.matrix_rank(np.array(rows), tol=1e-10))
    print("      spans of the nine contractions: independent pair %d, linked pair on all four %d, on the traceless three %d (the seat: 9, 5, 4); pairs (A_L, A_R) with A_L V = V A_R: %d with the E_33 vertex, %d without (the seat: 1, 2)" % (s1, s2, s3, nullity(True), nullity(False)))
    # G4.4
    a, b = sp.symbols("a b"); st = [(1, 0, 0, 0), (3, sp.Rational(1, 2), 0, 2 * a), (6, 1, sp.Rational(3, 2), a + b), (1, 0, 0, 2 * b), (3, sp.Rational(1, 2), 0, 2 * a + 2 * b), (2, 0, sp.Rational(1, 2), 3 * a + b)]
    dims = sum(d for d, *_ in st); cub = sp.factor(sum(d * q ** 3 for d, _, _, q in st)); sh = -(3 * a + 2 * b) / 2
    an = [sp.simplify(sum(t3 * (q + sh) for _, t3, _, q in st)), sp.simplify(sum(t2 * (q + sh) for _, _, t2, q in st)), sp.simplify(sum(d * (q + sh) for d, _, _, q in st)), sp.simplify(sum(d * (q + sh) ** 3 for d, _, _, q in st))]
    print("G4.4: the seat's six blocks have %d states; the cubic sum of the unshifted charges is %s; shifted by -(3a + 2b)/2 the four anomaly sums are %s" % (dims, cub, an))
    sub = {a: sp.Rational(1, 3), b: -sp.Rational(1, 2)}; print("      at (a, b) = (1/3, -1/2) the shifted charges of the six blocks (1, 3, 6, 1, 3, 2) are %s: minus the hypercharges of nu^c, u^c, Q, e^c, d^c, L" % [str((q + sh).subs(sub)) for *_, q in st])
    # G4.5
    cg = 2 * (-F(21) + F(7, 8) * 57); cf = 2 * (F(48) - F(7, 8) * 33); cs = 2 * (-F(13) + F(7, 8) * 14); cir = 2 * (-21 - 13 + 48)
    print("G4.5: counts: E6's 78 = 21 + 57; one 27 = 16 + 11 = (8 + 8) + (6 + 4 + 1); weights %s + %s + %s = %s at short distance and %d with the massless modes alone (the seat: 231/4, 153/4, -3/2, 189/2, 28)" % (cg, cf, cs, cg + cf + cs, cir))
    from scipy.special import kv
    from scipy.optimize import brentq
    def tower(C, m, tw, fer, d=0):
        """one real mode's energy on a circle of length C, or its derivative in C (d = 1): the massless closed form, or the Bessel sum, whose terms fall as exp(-k C m)"""
        s = 1.0 if fer else -1.0
        if m == 0:
            c0 = s * (-7 / 8 if tw else 1.0) * math.pi ** 2 / 90; return c0 / C ** 4 if d == 0 else -4 * c0 / C ** 5
        k = np.arange(1, int(60 / (C * m)) + 2); x = k * C * m; sg = (-1.0) ** k if tw else 1.0
        return s * (sg * m ** 4 * kv(2, x) / x ** 2).sum() / (2 * math.pi ** 2) if d == 0 else s * (sg * m ** 4 * (-kv(3, x) / x ** 2) * k * m).sum() / (2 * math.pi ** 2)   # d/dx [K_2(x)/x^2] = -K_3(x)/x^2
    VA = lambda L, d=0: (4 if d else 1) * (68 * tower(4 * L, 0, False, False, d) + 96 * tower(4 * L, 0, False, True, d) + 142 * tower(4 * L, 1, True, False, d) + 66 * tower(4 * L, 1, True, True, d))
    VB = lambda L, d=0: (4 if d else 1) * (4 * tower(4 * L, 0, False, False, d) + 64 * tower(4 * L, 1, False, False, d) + 96 * tower(4 * L, 1, False, True, d) + 142 * tower(4 * L, 1, True, False, d) + 66 * tower(4 * L, 1, True, True, d))
    chk = abs((VA(1.0 + 1e-5) - VA(1.0 - 1e-5)) / 2e-5 / VA(1.0, 1) - 1); dA = [VA(k / 4, 1) for k in range(1, 21)]; fine = max(VA(L, 1) for L in np.linspace(0.02, 12, 3000))
    Ls = brentq(lambda L: VB(L, 1), 0.5, 3.0, xtol=1e-14); d2 = (VB(Ls + 1e-5, 1) - VB(Ls - 1e-5, 1)) / 2e-5
    print("      the curve as the seat defines it (every gapped mode at mass 1, the interval read as a circle of length 4 L; the slope by the closed derivative, checked against a difference: %.1e):" % chk)
    print("      branch A's slope at L = 1/4 ... 5 is negative throughout, its largest value %.6e (the seat: -1.5353e-05), and negative at 3000 points from 0.02 to 12 (largest %.1e); V at L = 1/1000 against (189/2) pi^2 / (90 (4L)^4): %.1e" % (max(dA), fine, abs(VA(1e-3) / (94.5 * math.pi ** 2 / (90 * 0.004 ** 4)) - 1)))
    print("      branch B (the fermions gapped by hand): the minimum is at L = %.12f with second derivative %.8f (the seat: 1.682569148980953 and 0.0014443827)" % (Ls, d2))
    print("      branch A is 28 massless (positive, falling) plus 76 net twisted bosons at one mass (positive, falling): the runaway holds for these counts and this single mass; nothing of the manifold enters beyond the counts")
