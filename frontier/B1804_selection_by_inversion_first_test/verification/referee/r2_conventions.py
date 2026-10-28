"""Referee B1804, check 2: the transformation law and the conventions.

The class F_N = sum N_ab da1 ^ db2.  If the diffeomorphism acts on coordinates by v1 -> A v1, v2 -> B v2, the pullback
is F_N -> F_{A^T N B} (derived here from the exterior algebra, not assumed).  Other conventions an author could use:
A N B^T, A^{-1}..., i.e. the transformation law with A replaced by A^T or A^{-1}.  For A = LR, RL (symmetric) all
coincide; to show what the choice controls, the same is run for a NON-symmetric conjugate g LR g^-1.

Consistency test of the law (independent of any convention): if phi^* F = F then F is (1,1) for J iff it is (1,1) for
phi^* J, so the (1,1) locus of an invariant class must be stable under the moduli action phi^*: (tau, tau') -> (A.tau,
B.tau') computed from the pullback of dz.  A wrong law fails this test.
"""
import itertools
import sympy as sp

tau, tp = sp.symbols("tau tp")
L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]])
LR, RL = L * R, R * L
g = sp.Matrix([[1, 2], [0, 1]])
LRc = g * LR * g.inv()   # non-symmetric conjugate


def cond(N, t, s):
    return sp.expand(-N[0, 0] * t * s + N[0, 1] * t + N[1, 0] * s - N[1, 1])


# (a) derive the pullback law from components: phi^* da1 = sum_c A[a,c] dc1 (v1 -> A v1)
def pullback_N(N, A, B):
    out = sp.zeros(2, 2)
    for a, b in itertools.product(range(2), repeat=2):
        for c, d in itertools.product(range(2), repeat=2):
            out[c, d] += N[a, b] * A[a, c] * B[b, d]
    return out


Ns = sp.Matrix(2, 2, sp.symbols("n0:4"))
A0 = sp.Matrix(2, 2, sp.symbols("a0:4")); B0 = sp.Matrix(2, 2, sp.symbols("b0:4"))
print("(a) pullback law: phi^*F_N = F_{A^T N B}:", sp.simplify(pullback_N(Ns, A0, B0) - A0.T * Ns * B0) == sp.zeros(2, 2))


def moebius_from_pullback(A, t):
    # phi^* dz = (1, t) A (dx, dy)^T = p dx + q dy  ->  new tau = q / p
    row = sp.Matrix([[1, t]]) * A
    return sp.simplify(row[1] / row[0])


def invariant_space(A, B, law):
    N = sp.Matrix(2, 2, sp.symbols("m0:4"))
    if law == "A^T N B":
        E = A.T * N * B - N
    elif law == "A N B^T":
        E = A * N * B.T - N
    elif law == "A^-T N B^-1":
        E = A.inv().T * N * B.inv() - N
    elif law == "A^-1 N B^-T":
        E = A.inv() * N * B.inv().T - N
    sol = sp.solve(list(E), list(N), dict=True)[0]
    Ng = N.subs(sol)
    free = sorted(Ng.free_symbols, key=str)
    return [Ng.subs({f: (1 if f == h else 0) for f in free}) for h in free]


def det_signature(basis):
    c = sp.symbols("c0:%d" % len(basis))
    Ngen = sum((ci * b for ci, b in zip(c, basis)), sp.zeros(2, 2))
    q = sp.expand(Ngen.det())
    H = sp.hessian(q, c) / 2
    ev = [sp.re(sp.N(e)) for e in H.eigenvals(multiple=True)]
    return (sum(1 for e in ev if e > 1e-12), sum(1 for e in ev if e < -1e-12), sum(1 for e in ev if abs(e) <= 1e-12))


laws = ["A^T N B", "A N B^T", "A^-T N B^-1", "A^-1 N B^-T"]
for name, A in (("LR", LR), ("RL", RL), ("g.LR.g^-1 (non-symmetric)", LRc)):
    for act in ("diag", "dual"):
        B = A if act == "diag" else A.inv().T
        spaces = {}
        for law in laws:
            bas = invariant_space(A, B, law)
            spaces[law] = sp.Matrix.hstack(*[b.reshape(4, 1) for b in bas])
        same = {law: spaces[law].rank() == spaces["A^T N B"].rank() == sp.Matrix.hstack(spaces[law], spaces["A^T N B"]).rank()
                for law in laws}
        bas = invariant_space(A, B, "A^T N B")
        print("A = %s %s, action %s: dim %d, det signature (+,-,0) = %s; law gives the same space as A^T N B: %s"
              % (name, A.tolist(), act, len(bas), det_signature(bas), same))
        # stability test of the (1,1) locus of each invariant class under the moduli action, for each law
        for law in laws:
            ok = True
            for Nb in invariant_space(A, B, law):
                if Nb.det() == 0:
                    continue
                sols = sp.solve(cond(Nb, tau, tp), tp)
                if not sols:
                    continue
                t0 = sp.Rational(3, 7) + sp.I * sp.Rational(5, 4)
                tp0 = sols[0].subs(tau, t0)
                t1, tp1 = moebius_from_pullback(A, t0), moebius_from_pullback(B, tp0)
                if sp.simplify(cond(Nb, t1, tp1)) != 0:
                    ok = False
            print("     law %-12s: every invariant class's (1,1) locus stable under the induced moduli action: %s" % (law, ok))

# (c) LR's fixed points on tau under the draft's coordinate convention (z = x + tau y, v -> A v)
for name, A in (("LR", LR), ("RL", RL)):
    m = moebius_from_pullback(A, tau)
    print("(c) %s: induced tau -> %s ; fixed points %s" % (name, m, sp.solve(sp.numer(sp.together(m - tau)), tau)))
    Aplain = (A[0, 0] * tau + A[0, 1]) / (A[1, 0] * tau + A[1, 1])
    print("    %s as a plain Moebius map (a tau + b)/(c tau + d): fixed points %s" % (name, sp.solve(sp.numer(sp.together(Aplain - tau)), tau)))
print("r2 exit 0")
