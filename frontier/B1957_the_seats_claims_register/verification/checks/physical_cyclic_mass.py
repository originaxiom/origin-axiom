"""B1957: the physical lane's package 'cyclic charged mass' (P-C3f, 2026-11-16): the algebra of its three hand proofs,
rebuilt on main.  Nothing of the lane's is run.  What is NOT verified here: that the lane's physical operator on the
complete surface is this compact complex of line bundles (its local L2 solvability, its global corner contraction,
its Hermitian stationary response), and the normalisation sqrt 2 of its mass map.
 C1  on an elliptic curve the section of the non-trivial flat line of order two with one pole allowed at p: the
     function theta_3/theta_1 has both multipliers -1, a simple pole at 0 and exactly one zero in a cell, at the
     half-period (pi + pi tau)/2, which is not p.  So in Hom degree two the two maps have divisors 2p and p + q.
 C2  the local computation: for A --(f0, f1)--> B + C --(-f1, f0)--> D over k[w], the first map is injective and the two
     cohomology modules have length deg gcd(f0, f1); by exact linear algebra on truncated polynomial spaces, in the
     generic case (common divisor p: length 1) and on the two axes (2p and p + q: length 2).
 C3  the pole test: r^(a - 1 - 2n) log(1/r)^(a - 2) is integrable at 0 for n up to -2, 0, 2 at a = -3, 1, 5, so the
     compact extensions have degrees -2, 0, 0, 2.
 C4  the corner reduction: the matrix with three non-zero pivots and one corner is a direct sum of an isomorphism and
     the corner, the corner's products with the pivot homotopy vanish in both orders, and the two-factor Koszul complex
     has the cohomology of the four-line complex: dimensions 1, 2, 1 when both corners vanish and 0 otherwise.
 C5  the count: the first page from Riemann-Roch on an elliptic curve (h0 of a line of degree d > 0 is d, of degree
     0 is 1 or 0 as it is trivial or not; h1 by duality) gives 3 or 2 per gauge component at the origin (one trivial
     middle line, or none); off the origin the kernel is the length of C2: 2 on an axis, 1 at a generic point; the
     totals over the 128 are 18, 16, 8 (or 16, 16, 8).  The two counts together fix the rank left for the secondary
     map: 1 at a generic point when both middle lines are acyclic, 0 otherwise.
     The exact sequence 0 -> A(p) -> B + C -> D(-p) -> 0: degrees -1, 0, 0, 1; h1(A(p)) = h0(D(-p)) = 1, so the
     secondary map H1(A) -> H0(D), between two-dimensional spaces, has rank 1.
 C6  the secondary map in a finite graded model (S = k[x, y], the two-term complex S(-2)^2 --(x^2, y^2)--> S, whose
     graded piece of degree 3 is acyclic; A, B = C, D its pieces of degrees 1, 3, 5; F0, F1 two quadrics):
     K = F0 G F1 - F1 G F0 lands in the kernel of D's differential, the opposite sign does not; and the total complex
     at t = 1 has first cohomology of dimension dim H1(A) - rank K, for independent, dependent and vanishing quadrics.
 C7  the second-order Schur coefficient: for M(t) = M0 + t V1 + t^2 V2 with the first-order projection zero, the
     small singular values are t^2 times those of P V2 P - P V1 Q C^-1 Q V1 P."""
import functools, itertools
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
import mpmath as mp
print = functools.partial(print, flush=True)


def h0(d, trivial):
    return d if d > 0 else (1 if (d == 0 and trivial) else 0)


def h1(d, trivial):
    return h0(-d, trivial)                                   # Serre duality on a curve with trivial canonical line


def trunc_complex(f0, f1, N):
    """the matrices of a -> (f0 a, f1 a) on polynomials of degree < N and (b, c) -> -f1 b + f0 c on degree < N + d"""
    w = sp.symbols("w"); d = max(sp.degree(f, w) if f != 0 else 0 for f in (f0, f1)); M = N + d
    def mult(f, n_in, n_out):
        A = sp.zeros(n_out, n_in)
        for j in range(n_in):
            p = sp.Poly(sp.expand(f * w ** j), w) if f != 0 else None
            if p is not None:
                for (k,), c in p.terms(): A[k, j] = c
        return A
    d1 = sp.Matrix.vstack(mult(f0, N, M), mult(f1, N, M)); d2 = sp.Matrix.hstack(mult(-f1, M, M + d), mult(f0, M, M + d))
    assert (d2 * d1).is_zero_matrix
    return d1, d2, (N, 2 * M, M + d)


if __name__ == "__main__":
    mp.mp.dps = 30; tau = mp.mpf("0.31") + mp.mpf("1.17") * 1j; q = mp.exp(1j * mp.pi * tau)
    f = lambda z: mp.jtheta(3, z, q) / mp.jtheta(1, z, q); z0 = mp.mpf("0.37") + mp.mpf("0.21") * 1j
    m1 = f(z0 + mp.pi) / f(z0); m2 = f(z0 + mp.pi * tau) / f(z0); half = (mp.pi + mp.pi * tau) / 2
    # zeros minus poles in a cell by the argument principle, the cell shifted off the pole
    c0 = -mp.mpf("0.4") - mp.mpf("0.3") * 1j; corners = [c0, c0 + mp.pi, c0 + mp.pi + mp.pi * tau, c0 + mp.pi * tau, c0]
    dlog = lambda z: mp.diff(f, z) / f(z); count = sum(mp.quad(dlog, [corners[i], corners[i + 1]]) for i in range(4)) / (2j * mp.pi)
    res = mp.quad(lambda th: f(mp.mpf("0.05") * mp.exp(1j * th)) * 1j * mp.mpf("0.05") * mp.exp(1j * th), [0, 2 * mp.pi]) / (2j * mp.pi)
    print("C1: theta_3/theta_1: multipliers %s and %s; zeros minus poles in a cell: %s; its residue at 0 is %s (a simple pole); |f| at the half-period (pi + pi tau)/2: %s, and |f'| there: %s (a simple zero)" % (
        mp.nstr(m1, 8), mp.nstr(m2, 8), mp.nstr(count, 6), mp.nstr(res, 8), mp.nstr(abs(f(half)), 3), mp.nstr(abs(mp.diff(f, half)), 6)))
    w = sp.symbols("w"); rows = []
    for name, f0, f1, want in (("both coefficients (common divisor p)", w ** 2, w * (w - 1), 1), ("the first alone (2p)", w ** 2, sp.Integer(0), 2), ("the second alone (p + q)", sp.Integer(0), w * (w - 1), 2), ("a control with no common zero", w ** 2, (w - 1) * (w - 2), 0)):
        d1, d2, (n0, n1, n2) = trunc_complex(f0, f1, 9); r1, r2 = d1.rank(), d2.rank(); H0, H1, H2 = n0 - r1, n1 - r2 - r1, n2 - r2
        g = sp.gcd(f0, f1); rows.append((name, H0, H1, H2, sp.degree(g, w) if g != 0 else None)); assert (H0, H1, H2) == (0, want, want)
    print("C2: (case, H0, H1, H2, degree of the gcd): %s" % rows)
    def max_pole(a):
        ok = []
        for n in range(-6, 7):
            p_, q_ = a - 1 - 2 * n, a - 2
            if p_ > -1 or (p_ == -1 and q_ < -1): ok.append(n)
        return max(ok)
    print("C3: the largest admitted pole order at a = -3, 1, 5: %s; so the degrees of the four compact lines are %s and the Hom degree is %d" % ([max_pole(a) for a in (-3, 1, 5)], [max_pole(-3), max_pole(1), max_pole(1), max_pole(5)], max_pole(1) - max_pole(-3)))
    rng = np.random.default_rng(46)
    def Qm(c, fz):
        A = np.zeros((4, 4), dtype=complex); A[0, 1], A[1, 2], A[2, 3], A[3, 0] = c[0], c[1], c[2], fz; return A
    c = rng.normal(size=3) + 1j * rng.normal(size=3); fz = 0.7 - 0.2j; Q = Qm(c, fz)
    hom = np.zeros((4, 4), dtype=complex); hom[1, 0], hom[2, 1], hom[3, 2] = 1 / c[0], 1 / c[1], 1 / c[2]            # the pivot homotopy: targets 0, 1, 2 back to sources 1, 2, 3
    corner = np.zeros((4, 4), dtype=complex); corner[3, 0] = fz; pivot = Q - corner
    ok4 = np.allclose(pivot @ hom @ pivot, pivot) and np.allclose(corner @ hom, 0) and np.allclose(hom @ corner, 0)
    def koszul_dims(fa, fb):
        Q1 = np.kron(Qm(c, fa), np.eye(4)); Q2 = np.kron(np.eye(4), Qm(c[::-1], fb)); d1 = np.vstack([Q1, Q2]); d2 = np.hstack([-Q2, Q1]); assert np.allclose(d2 @ d1, 0)
        r1, r2 = int(np.linalg.matrix_rank(d1, tol=1e-9)), int(np.linalg.matrix_rank(d2, tol=1e-9)); return (16 - r1, 32 - r1 - r2, 16 - r2)
    print("C4: the pivot block is inverted by the homotopy and the corner's products with it vanish in both orders: %s; the two-factor complex's cohomology at corners (0, 0), (f, 0), (0, f), (f, f'): %s" % (ok4, [koszul_dims(*p) for p in ((0, 0), (fz, 0), (0, fz), (fz, 0.3 + 1j))]))
    degs = {"A": -2, "B": 0, "C": 0, "D": 2}; length = {"axis": rows[1][2], "generic": rows[0][2]}; assert rows[2][2] == rows[1][2]
    def counts(trivB):
        e1 = h1(degs["A"], False) + h0(0, trivB) + h0(0, False)                # total degree one of the first page: H1(A) + H0(B) + H0(C)
        out = {"origin": (e1, None)}
        for case, nonzero in (("axis", 1), ("generic", 2)):
            d1rank = nonzero if trivB else 0                                   # multiplication by a non-zero section is injective on H0 of the trivial line, and dually onto its H1
            out[case] = (length[case], e1 - d1rank - length[case])             # the kernel is the length of C2; what is left for the secondary map to remove
        return out
    al, ac = counts(True), counts(False); kal = [al[s_][0] for s_ in ("origin", "axis", "generic")]; kac = [ac[s_][0] for s_ in ("origin", "axis", "generic")]
    tot = [2 * kal[i] + 6 * kac[i] for i in range(3)]; mis = [8 * kac[i] for i in range(3)]
    print("C5: kernel per gauge component (origin, an axis, generic): one trivial middle line %s, none %s; totals over the 128: %s, and with no trivial line %s; the rank left for the secondary map (an axis, generic): one trivial line %s, none %s; the sequence's degrees %s with h1(A(p)) = %d and h0(D(-p)) = %d (so the rank is 1 when both middle lines are acyclic), h1(A) = %d, h0(D) = %d, h0(A(p)) = %d" % (
        kal, kac, tot, mis, [al["axis"][1], al["generic"][1]], [ac["axis"][1], ac["generic"][1]], [degs["A"] + 1, 0, 0, degs["D"] - 1], h1(-1, False), h0(1, False), h1(-2, False), h0(2, False), h0(-1, False)))
    # C6
    x, y = sp.symbols("x y"); mono = lambda d: [x ** i * y ** (d - i) for i in range(d + 1)] if d >= 0 else []
    def vec(p, d):
        P = sp.Poly(sp.expand(p), x, y); return sp.Matrix([P.coeff_monomial(m) for m in mono(d)]) if d >= 0 else sp.zeros(0, 1)
    def bmat(d):                                                             # S_(d-2)^2 -> S_d, (u, v) -> x^2 u + y^2 v
        cols = [vec(x ** 2 * m, d) for m in mono(d - 2)] + [vec(y ** 2 * m, d) for m in mono(d - 2)]; return sp.Matrix.hstack(*cols) if cols else sp.zeros(d + 1, 0)
    def mul_mat(fq, d):                                                      # S_d -> S_(d+2)
        return sp.Matrix.hstack(*[vec(fq * m, d + 2) for m in mono(d)]) if d >= 0 else sp.zeros(d + 3, 0)
    two = lambda Mx: sp.diag(Mx, Mx)
    def model(f0, f1):
        bA, bB, bD = bmat(1), bmat(3), bmat(5); G = bB.inv()                 # the middle piece is acyclic
        F_A1 = lambda fq: mul_mat(fq, 1); F_B0 = lambda fq: two(mul_mat(fq, 1))    # on the degree-one parts: S_1 -> S_3; on the degree-zero parts of the middle: S_1^2 -> S_3^2
        K = F_B0(f0) * G * F_A1(f1) - F_B0(f1) * G * F_A1(f0); Kp = F_B0(f0) * G * F_A1(f1) + F_B0(f1) * G * F_A1(f0)
        closed = (bD * K).is_zero_matrix; closed_p = (bD * Kp).is_zero_matrix
        # the total complex at t = 1: T1 = A^1 + B^0 + C^0 -> T2 = B^1 + C^1 + D^0 -> T3 = D^1 (A^0 = 0)
        nA1, nB0, nB1, nD0, nD1 = 2, 4, 4, 8, 6
        d1 = sp.zeros(nB1 + nB1 + nD0, nA1 + nB0 + nB0)
        d1[0:4, 0:2] = F_A1(f0); d1[4:8, 0:2] = F_A1(f1)                    # A^1 -> B^1, C^1
        d1[0:4, 2:6] = -bB; d1[4:8, 6:10] = -bB                             # B^0 -> B^1, C^0 -> C^1 (the sign of the totalisation)
        d1[8:16, 2:6] = -F_B0(f1); d1[8:16, 6:10] = F_B0(f0)                # B^0 -> D^0 by -f1, C^0 -> D^0 by f0
        d2 = sp.zeros(nD1, nB1 + nB1 + nD0); d2[:, 0:4] = -mul_mat(f1, 3); d2[:, 4:8] = mul_mat(f0, 3); d2[:, 8:16] = bD
        assert (d2 * d1).is_zero_matrix
        H1 = d1.shape[1] - d1.rank(); return K.rank(), closed, closed_p, H1
    out = [(name,) + model(f0, f1) for name, f0, f1 in (("independent quadrics", x * y + x ** 2, x * y - 3 * y ** 2), ("a common linear factor", x * (x + y), x * (x - 2 * y)), ("proportional", x * y, 5 * x * y), ("the second zero", x * y + y ** 2, sp.Integer(0)))]
    print("C6: (quadrics, rank K, K closed, the opposite sign closed, dim of the first total cohomology; dim H1(A) = 2): %s" % out)
    n, k = 9, 2; U, _, Vh = np.linalg.svd(rng.normal(size=(n, n))); sv = np.concatenate([np.zeros(k), 1 + rng.random(n - k)]); M0 = U @ np.diag(sv) @ Vh
    PL = U[:, :k]; PR = Vh[:k].T; QL = U[:, k:]; QR = Vh[k:].T; V1 = rng.normal(size=(n, n)); V1 -= PL @ (PL.T @ V1 @ PR) @ PR.T; V2 = rng.normal(size=(n, n))
    Y2 = PL.T @ V2 @ PR - PL.T @ V1 @ QR @ np.linalg.inv(QL.T @ M0 @ QR) @ QL.T @ V1 @ PR; t = 1e-3
    small = np.sort(np.linalg.svd(M0 + t * V1 + t * t * V2, compute_uv=False))[:k] / t ** 2
    print("C7: the two small singular values over t^2 at t = 0.001: %s; those of the Schur coefficient: %s" % (np.round(small, 4).tolist(), np.round(np.sort(np.linalg.svd(Y2, compute_uv=False)), 4).tolist()))
