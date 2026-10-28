"""P-419 first computation (exact, data-free; exploratory, audit room). On T^4 = E_tau x E_tau' with real coordinates
(x1, y1, x2, y2), z1 = x1 + tau y1, z2 = x2 + tau' y2, a real 2-form F is (1,1) iff F ^ dz1 ^ dz2 = 0. The monodromy A acts on
H^1 of each factor; actions tried on the second factor: A (diagonal) and A^{-T} (dual). Find the A-invariant classes in
H^2(T^4; Q), the locus where each is (1,1), and whether two independent invariant mixed classes can be (1,1) at once with
tau, tau' in the upper half-plane."""
import itertools
import sympy as sp

t, tp = sp.symbols("tau taup")
x1, y1, x2, y2 = range(4)


def wedge_coeff(N):
    # F_N = sum N[a][b] da1 ^ db2 (a in x1,y1; b in x2,y2); Omega = dz1 ^ dz2. Coefficient of dx1 dy1 dx2 dy2 in F_N ^ Omega.
    Om = {(0, 0): 1, (0, 1): tp, (1, 0): t, (1, 1): t * tp}       # Omega's mixed coefficients (a, b): da1 ^ db2
    sign = {((0, 0), (1, 1)): -1, ((0, 1), (1, 0)): 1, ((1, 0), (0, 1)): 1, ((1, 1), (0, 0)): -1}
    return sp.expand(sum(N[a, b] * Om[c] * sign[((a, b), c)] for (a, b), c in sign))


def invariant_mixed(A, act):
    n = sp.symbols("n0:4"); N = sp.Matrix(2, 2, n)
    B = A if act == "diag" else A.inv().T
    eqs = list(A.T * N * B - N)
    sol = sp.solve(eqs, n, dict=True)[0]
    Ng = N.subs(sol)
    free = sorted(Ng.free_symbols, key=str)
    return [Ng.subs({f: (1 if f == g else 0) for f in free}) for g in free]


L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]])
for name, A in (("LR", L * R), ("RL", R * L)):
    for act in ("diag", "dual"):
        basis = invariant_mixed(A, act)
        print("A = %s = %s, action %s: invariant mixed classes (%d): %s" % (name, A.tolist(), act, len(basis), [b.tolist() for b in basis]))
        conds = []
        for Nb in basis:
            c = wedge_coeff(Nb)
            s = sp.solve(c, tp)
            print("   N = %s: (1,1) iff %s = 0 -> tau' = %s ; det N = %s" % (Nb.tolist(), c, s, Nb.det()))
            conds.append(c)
        if len(conds) >= 2:
            sols = sp.solve(conds[:2], [t, tp], dict=True)
            for s0 in sols:
                tv, tpv = sp.nsimplify(s0[t]), sp.nsimplify(s0[tp])
                print("   both (1,1): tau = %s, tau' = %s ; Im tau = %s, Im tau' = %s" % (tv, tpv, sp.im(sp.N(tv)), sp.im(sp.N(tpv))))
print("c1 exit 0")
