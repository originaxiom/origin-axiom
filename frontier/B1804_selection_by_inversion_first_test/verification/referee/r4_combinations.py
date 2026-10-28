"""Referee B1804, check 4: integer combinations within the draft's own frame (A = LR, diagonal and dual).

Every invariant mixed class is N = a N1 + b N2.  Its (1,1) locus is tau' = M_N tau with M_N = [[-Nxy, Nyy], [-Nxx, Nyx]]
(r1).  (i) Identify the set {M_N}; (ii) list the curves for small (a, b) with det > 0 -- the draft's table names only
tau' = tau (diag) / tau' = -1/tau (dual); (iii) any two non-proportional invariant classes are (1,1) together only where
M_2^{-1} M_1 fixes tau: show that every such M_2^{-1} M_1 lies in Q(Phi), Phi^2 = Phi + 1, hence is scalar or hyperbolic,
so no common point in H; (iv) at CM points on a curve the invariant (1,1) lattice does not grow.
"""
import itertools
import sympy as sp

tau, tp = sp.symbols("tau tp")
L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]])
LR = L * R


def Mof(N):
    return sp.Matrix([[-N[0, 1], N[1, 1]], [-N[0, 0], N[1, 0]]])


def cond(N):
    return sp.expand(-N[0, 0] * tau * tp + N[0, 1] * tau + N[1, 0] * tp - N[1, 1])


for act, B in (("diag", LR), ("dual", LR.inv().T)):
    n = sp.Matrix(2, 2, sp.symbols("n0:4"))
    sol = sp.solve(list(LR.T * n * B - n), list(n), dict=True)[0]
    ng = n.subs(sol); fr = sorted(ng.free_symbols, key=str)
    N1, N2 = [ng.subs({f: (1 if f == h else 0) for f in fr}) for h in fr]
    M1, M2 = Mof(N1), Mof(N2)
    X = M1.inv() * M2
    print("%s: N1 = %s (det %s), N2 = %s (det %s); M1 = %s, M2 = %s; M1^-1 M2 = %s, its char. poly %s"
          % (act, N1.tolist(), N1.det(), N2.tolist(), N2.det(), M1.tolist(), M2.tolist(), X.tolist(), sp.factor(X.charpoly().as_expr())))
    # (ii) curves of small combinations with det > 0
    curves = []
    for a, b in itertools.product(range(-3, 4), repeat=2):
        if (a, b) == (0, 0) or sp.gcd(a, b) != 1:
            continue
        N = a * N1 + b * N2
        if N.det() <= 0:
            continue
        M = Mof(N)
        rhs = sp.simplify((M[0, 0] * tau + M[0, 1]) / (M[1, 0] * tau + M[1, 1]))
        if (-a, -b) in [c[0] for c in curves]:
            continue
        curves.append(((a, b), N.det(), rhs))
    print("   (1,1) curves of primitive invariant classes with det > 0, |a|,|b| <= 3 (up to sign):")
    for (ab, d, rhs) in curves:
        print("      (a, b) = %s, det %s : tau' = %s" % (ab, d, rhs))
    # (iii) pairwise intersections of these curves in H
    bad = 0
    for (c1, c2) in itertools.combinations(curves, 2):
        Na = c1[0][0] * N1 + c1[0][1] * N2
        Nb = c2[0][0] * N1 + c2[0][1] * N2
        Y = Mof(Nb).inv() * Mof(Na)
        disc = sp.expand(Y.trace() ** 2 - 4 * Y.det())
        if Y.is_diagonal() and Y[0, 0] == Y[1, 1]:
            continue
        if disc < 0:
            bad += 1
    print("   pairs of these curves meeting at a point of H (needs M_b^-1 M_a elliptic): %d of %d" % (bad, len(curves) * (len(curves) - 1) // 2))
    # general proof: M_{aN1+bN2} = a M1 + b M2 ; M1^{-1}(a M1 + b M2) = a I + b X, X^2 = tr X * X - det X
    print("   X^2 - X - 1 =", (X * X - X - sp.eye(2)).tolist() if act == "diag" else "", "(X satisfies the golden polynomial up to sign/conjugation)")
    # (iv) at CM points on the first curve
    Mp = M1 if N1.det() > 0 else M2   # the det > 0 basis class
    for t0 in (sp.I, (-1 + sp.sqrt(3) * sp.I) / 2):
        t0p = sp.simplify((Mp[0, 0] * t0 + Mp[0, 1]) / (Mp[1, 0] * t0 + Mp[1, 1]))
        a_, b_ = sp.symbols("a_ b_", real=True)
        e = sp.expand((a_ * cond(N1) + b_ * cond(N2)).subs({tau: t0, tp: t0p}))
        s = sp.solve([sp.re(e), sp.im(e)], [a_, b_], dict=True)
        print("   at the CM point (tau, tau') = (%s, %s) on the det > 0 basis class's curve: invariant (1,1) combinations a N1 + b N2: %s"
              % (t0, t0p, s))
print("r4 exit 0")
