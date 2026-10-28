"""Referee B1804, check 3: other natural actions of the monodromy on T^4 = R^4/Z^4, coordinates v = (x1, y1, x2, y2),
complex structure z1 = x1 + tau y1, z2 = x2 + tau' y2 (the draft's product frame, tau, tau' in H).

A diffeomorphism v -> g v (g in SL(4, Z)) pulls back a 2-form (antisymmetric matrix F, F = sum_{i<j} F_ij e_i ^ e_j)
to g^T F g.  Invariant classes: g^T F g = F.  The (1,1) condition of F depends only on its mixed block N = F[0:2, 2:4]
(area forms wedge dz1 ^ dz2 to zero; r1).  On H x H the (1,1) mixed classes at a point span a space on which det N is
positive definite (Hodge index; r1: F_N ^ F_N = -2 det N), and conversely two rational classes with det positive
definite on their span are (1,1) together at exactly one point of H x H (tau the fixed point of the elliptic
M2^-1 M1, tau' = M1 tau).  So: the invariant fluxes can force a POINT of H x H iff det restricted to the invariant
mixed space has at least two positive directions (n_+ >= 2), and a single flux can force at most a curve otherwise.

Actions surveyed (A = LR unless said), in the ordering (x1, y1, x2, y2) = (w1 x h, w1 x y, w2 x h, w2 x y):
  the draft's two: A + A (diagonal: A on each factor's H^1), A + A^{-T} (dual);
  A + I, I + A, A + A^2, A + A^{-2};
  I_H (x) A_W  -- the monodromy acting on the FACTOR INDEX: T^4 = E (x) Z^2 = Hom(H_1(fibre), E), i.e. (P, Q) -> (aP + bQ,
                  cP + dQ); holomorphic on E_tau x E_tau for every tau;
  A_H (x) A_W, A_H (x) A^{-T}_W.
Controls (diagonal action): S (order 4) and ST (order 6) elliptic -- must force CM points; T parabolic -- must not.
"""
import itertools
import sympy as sp

tau, tp = sp.symbols("tau tp")
L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]])
LR, RL = L * R, R * L
I2 = sp.eye(2)
S = sp.Matrix([[0, -1], [1, 0]]); T = sp.Matrix([[1, 1], [0, 1]])


def blk(A, B):
    return sp.diag(A, B)


def kronW(AW, AH):  # ordering (w1 x, w1 y, w2 x, w2 y): g = AW (x) AH
    return sp.Matrix(sp.BlockMatrix([[AW[i, j] * AH for j in range(2)] for i in range(2)]))


def invariant_2forms(g):
    fs = sp.symbols("f0:6")
    F = sp.zeros(4, 4)
    for k, (i, j) in enumerate(itertools.combinations(range(4), 2)):
        F[i, j] = fs[k]; F[j, i] = -fs[k]
    sol = sp.solve(list(g.T * F * g - F), fs, dict=True)[0]
    Fg = F.subs(sol)
    free = sorted(Fg.free_symbols, key=str)
    return [Fg.subs({f: (1 if f == h else 0) for f in free}) for h in free]


def cond(N):
    return sp.expand(-N[0, 0] * tau * tp + N[0, 1] * tau + N[1, 0] * tp - N[1, 1])


def analyse(name, g, show=True):
    basis = invariant_2forms(g)
    mixed = [F[0:2, 2:4] for F in basis]
    Mmat = sp.Matrix.hstack(*[m.reshape(4, 1) for m in mixed]) if mixed else sp.zeros(4, 0)
    r = Mmat.rank() if mixed else 0
    # det form on the invariant space (pulled back), its signature
    if basis:
        c = sp.symbols("c0:%d" % len(basis))
        Ngen = sum((ci * m for ci, m in zip(c, mixed)), sp.zeros(2, 2))
        q = sp.expand(Ngen.det())
        Hs = sp.hessian(q, c) / 2
        ev = [sp.re(sp.N(e)) for e in Hs.eigenvals(multiple=True)]
        sig = (sum(1 for e in ev if e > 1e-12), sum(1 for e in ev if e < -1e-12), sum(1 for e in ev if abs(e) <= 1e-12))
    else:
        q, sig = 0, (0, 0, 0)
    verdict = "POINT possible (n_+ >= 2)" if sig[0] >= 2 else ("at most a curve per flux, no point" if sig[0] == 1 else "no (1,1) mixed class in H x H: no condition")
    print("%-34s inv H^2 dim %d, mixed rank %d, det form %s, signature (+,-,0) %s -> %s"
          % (name, len(basis), r, q, sig, verdict))
    if show:
        for F in basis:
            N = F[0:2, 2:4]
            print("      class %s : mixed N = %s, (1,1) iff %s = 0" % ([F[i, j] for i, j in itertools.combinations(range(4), 2)], N.tolist(), cond(N)))
    return basis


print("== the draft's frame and its neighbours (A = LR) ==")
analyse("diag  A + A", blk(LR, LR))
analyse("dual  A + A^-T", blk(LR, LR.inv().T))
analyse("A + I", blk(LR, I2))
analyse("I + A", blk(I2, LR))
analyse("A + A^2", blk(LR, LR ** 2), show=False)
analyse("A + A^-2", blk(LR, LR.inv() ** 2), show=False)
print("== actions on the factor index / tensor actions (A = LR) ==")
Wmix = kronW(LR, I2)
basW = analyse("I_H (x) A_W  (factor-index action)", Wmix)
analyse("A_H (x) A_W", kronW(LR, LR))
analyse("A^-T_H (x) A_W", kronW(LR, LR.inv().T))
analyse("I_H (x) RL_W", kronW(RL, I2), show=False)
print("== controls (diagonal action) ==")
for nm, A in (("S (order 4)", S), ("ST (order 6)", S * T), ("T (parabolic)", T), ("-LR", -LR)):
    b = analyse("diag %s" % nm, blk(A, A), show=False)
    if len(b) >= 2:
        cs = [cond(F[0:2, 2:4]) for F in b]
        cs = [x for x in cs if x != 0]
        if len(cs) >= 2:
            sols = sp.solve(cs[:2], [tau, tp], dict=True)
            print("      joint (1,1): %s" % [(sp.nsimplify(s[tau]), sp.nsimplify(s[tp])) for s in sols])

# == the factor-index action in detail ==
print("== I_H (x) LR_W in detail ==")
g = Wmix
# holomorphic on tau' = tau?  pull back dz1, dz2 and test whether they stay in span(dz1, dz2)
t = sp.symbols("t")
dz = sp.Matrix([[1, t, 0, 0], [0, 0, 1, t]])
pulled = dz * g
print("  pullbacks of (dz1, dz2) at tau = tau' = t lie in span(dz1, dz2):", sp.Matrix.vstack(dz, pulled).rank() == 2)
dzg = sp.Matrix([[1, tau, 0, 0], [0, 0, 1, tp]])
print("  ... and at tau != tau' (generic):", sp.simplify(sp.Matrix.vstack(dzg, dzg * g).subs({tau: sp.I, tp: 2 * sp.I})).rank() == 2)
# every mixed block is realised: solve for the invariant class with a prescribed mixed part
fs = sp.symbols("f0:6")
pairs = list(itertools.combinations(range(4), 2))


def invariant_with_mixed(g, N):
    F = sp.zeros(4, 4)
    for k, (i, j) in enumerate(pairs):
        F[i, j] = fs[k]; F[j, i] = -fs[k]
    eqs = list(g.T * F * g - F) + [F[0, 2] - N[0, 0], F[0, 3] - N[0, 1], F[1, 2] - N[1, 0], F[1, 3] - N[1, 1]]
    sol = sp.solve(eqs, fs, dict=True)
    if not sol:
        return None
    Fs = F.subs(sol[0])
    return Fs.subs({f: 0 for f in Fs.free_symbols})


eps = sp.Matrix([[0, -1], [1, 0]])
F_gold = invariant_with_mixed(g, eps)
print("  invariant class with mixed part eps (tau' = tau):", [F_gold[i, j] for i, j in pairs], "; invariant:", g.T * F_gold * g == F_gold,
      "; (1,1) iff", cond(F_gold[0:2, 2:4]), "= 0")
print("    (its area part -2 dx1^dy1 + 2 dx2^dy2 and mixed part -dx1^dy2 + dy1^dx2 = sum Q_ab dx_a ^ dy_b with Q = [[-2,-1],[-1,2]],"
      " LR's golden form on the factor index, disc", sp.Matrix([[-2, -1], [-1, 2]]).det() * -4, ")")
# random mixed blocks: all realised?
import random
random.seed(1)
ok = all(invariant_with_mixed(g, sp.Matrix(2, 2, [random.randint(-5, 5) for _ in range(4)])) is not None for _ in range(20))
print("  20 random integer mixed blocks all realised by LR-invariant classes:", ok)


def sym_class(a, b, c):
    F = sp.zeros(4, 4)
    for (i, j), v in (((0, 2), a), ((0, 3), b), ((1, 2), b), ((1, 3), c)):
        F[i, j] += v; F[j, i] -= v
    return F


for (a, b, c) in ((1, 0, 1), (2, -1, 2), (1, 0, 3), (1, 0, 12), (2, 1, 1)):
    F = sym_class(a, b, c)
    assert g.T * F * g == F
    sols = sp.solve([cond(F_gold[0:2, 2:4]), cond(F[0:2, 2:4])], [tau, tp], dict=True)
    pts = [(sp.simplify(s[tau]), sp.simplify(s[tp])) for s in sols if sp.im(sp.N(s[tau])) > 0 and sp.im(sp.N(s[tp])) > 0]
    print("  eps-class + sym(a=%d, b=%d, c=%d) [both LR-invariant; det N = %d]: forced point(s) in H x H: %s"
          % (a, b, c, a * c - b * b, pts))
# a pair of LR-invariant classes forcing an off-diagonal CM pair (tau, tau') = (i, 2i):  tau' = 2 tau  and  tau' = -4/tau... use mixed parts
N1 = sp.Matrix([[0, -1], [2, 0]])   # -tau tau'*0 ... : -1*tau + 2 tau' -> check
N2 = sp.Matrix([[1, 0], [0, 2]])
F1, F2 = invariant_with_mixed(g, N1), invariant_with_mixed(g, N2)
sols = sp.solve([cond(N1), cond(N2)], [tau, tp], dict=True)
print("  mixed parts", N1.tolist(), "and", N2.tolist(), ": conditions", cond(N1), ",", cond(N2), "; both LR-invariant classes exist:",
      F1 is not None and F2 is not None, "; joint:", [(s[tau], s[tp]) for s in sols])
# the invariant Neron-Severi rank on the slice tau' = tau where LR acts holomorphically: an invariant class is fixed by
# its mixed part (mixed rank 4 = dim), and N is (1,1) at (t0, t0) iff -Nxx t0^2 + (Nxy + Nyx) t0 - Nyy = 0 over Q.
# The rank of that lattice is 1 (the antisymmetric part, eps) + the number of Q-relations among 1, t0, t0^2.
x = sp.symbols("x")
for t0 in (sp.I, (-1 + sp.sqrt(3) * sp.I) / 2, sp.Rational(1, 3) + sp.sqrt(2) * sp.I, 2 ** sp.Rational(1, 3) + sp.I):
    mp = sp.Poly(sp.minimal_polynomial(t0, x), x)
    d = mp.degree()
    vecs = []
    for k in range(3):
        rem = sp.Poly(x ** k, x).rem(mp)
        vecs.append([rem.coeff_monomial(x ** j) for j in range(d)])
    rels = 3 - sp.Matrix(vecs).rank()
    print("  on tau' = tau = %s (minimal polynomial degree %d): LR-invariant (1,1) mixed lattice rank = %d" % (t0, d, 1 + rels))
print("r3 exit 0")
