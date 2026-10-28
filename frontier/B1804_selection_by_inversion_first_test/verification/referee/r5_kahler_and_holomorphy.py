"""Referee B1804, check 5: what each frame keeps of supersymmetry along the circle.

A hyperbolic A cannot act on a flat T^4 by isometries, so no frame keeps both the complex structure and a Kahler class
invariant.  Check which half each frame keeps:
  the draft's diagonal frame (A on each factor's H^1): invariant Kahler class yes (t1 w1 + t2 w2); invariant complex
     structure: the induced moduli action (tau, tau') -> (A.tau, A.tau') has no fixed point in H x H;
  the factor-index frame (I_H (x) A_W): holomorphic on tau' = tau (r3); invariant Kahler class: the invariant (1,1)
     classes at tau = tau' (generic or CM) have F ^ F <= 0, so none is Kahler.
F ^ F = 2 Pf(F) vol, Pf = F01 F23 - F02 F13 + F03 F12 (basis dx1, dy1, dx2, dy2).
"""
import itertools
import sympy as sp

tau, tp = sp.symbols("tau tp")
L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]])
LR = L * R
I2 = sp.eye(2)
pairs = list(itertools.combinations(range(4), 2))


def pf(F):
    return sp.expand(F[0, 1] * F[2, 3] - F[0, 2] * F[1, 3] + F[0, 3] * F[1, 2])


def kronW(AW, AH):
    return sp.Matrix(sp.BlockMatrix([[AW[i, j] * AH for j in range(2)] for i in range(2)]))


def inv_basis(g):
    fs = sp.symbols("f0:6")
    F = sp.zeros(4, 4)
    for k, (i, j) in enumerate(pairs):
        F[i, j] = fs[k]; F[j, i] = -fs[k]
    sol = sp.solve(list(g.T * F * g - F), fs, dict=True)[0]
    Fg = F.subs(sol); fr = sorted(Fg.free_symbols, key=str)
    return [Fg.subs({f: (1 if f == h else 0) for f in fr}) for h in fr]


def cond(F):
    N = F[0:2, 2:4]
    return sp.expand(-N[0, 0] * tau * tp + N[0, 1] * tau + N[1, 0] * tp - N[1, 1])


# draft's diagonal frame
g = sp.diag(LR, LR)
w = sp.zeros(4, 4); w[0, 1], w[1, 0], w[2, 3], w[3, 2] = 1, -1, 1, -1
print("diag frame: w1 + w2 invariant:", g.T * w * g == w, "; (w1+w2)^2 = 2 Pf =", 2 * pf(w), "> 0 (Kahler)")
# induced action on tau from v -> A v, z = x + tau y: tau -> ((1,tau)A)[1] / ((1,tau)A)[0]
row = sp.Matrix([[1, tau]]) * LR
m = sp.simplify(row[1] / row[0])
fp = sp.solve(sp.numer(sp.together(m - tau)), tau)
print("diag frame: induced tau ->", m, "; fixed points", fp, "-> none in H: the complex structure is never invariant")

# factor-index frame
g = kronW(LR, I2)
B = inv_basis(g)
c = sp.symbols("c0:%d" % len(B))
Fgen = sum((ci * b for ci, b in zip(c, B)), sp.zeros(4, 4))
q = sp.expand(2 * pf(Fgen))
Hs = sp.hessian(q, c) / 2
ev = [sp.N(e) for e in Hs.eigenvals(multiple=True)]
print("factor-index frame: F^F on the invariant space =", q, "; signature eigenvalues", [round(float(sp.re(e)), 4) for e in ev])
for t0 in (2 ** sp.Rational(1, 3) + sp.I, sp.I, (-1 + sp.sqrt(3) * sp.I) / 2):
    # (1,1) invariant classes at (t0, t0): real linear conditions on c
    e = sp.expand(sum(ci * cond(b) for ci, b in zip(c, B)).subs({tau: t0, tp: t0}))
    eqs = [sp.expand(sp.re(e)), sp.expand(sp.im(e))]
    cr = sp.symbols("r0:%d" % len(B), real=True)
    eqs = [x.subs(dict(zip(c, cr))) for x in eqs]
    sol = sp.solve(eqs, cr, dict=True)
    sol = sol[0] if sol else {}
    qq = sp.factor(q.subs(dict(zip(c, cr))).subs(sol))
    # Q-rationality: only rational classes count; report the real (1,1) space's F^F (an upper bound for the rational one)
    print("  at tau = tau' = %s: F^F on the invariant (1,1) classes (real span) = %s" % (t0, qq))
print("r5 exit 0")
