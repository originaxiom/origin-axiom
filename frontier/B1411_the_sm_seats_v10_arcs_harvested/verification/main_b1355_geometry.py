"""Main's exact check of B1355's geometry (2026-09-15): 2T generated in SU(2) over Q(i) (order 24, orders {1,2,3,4,6}),
irreducible on C^2 (commutant = scalars), so on C^4 = C^2_std (+) C^2_triv the 2T-fixed locus of CP^3 is exactly P(C^2_triv),
one twistor line; -1 acts as diag(-1,-1,1,1) so its fixed set is P(C^2_std) u P(C^2_triv), two disjoint lines meeting only at
the cone apex; the normal action along the E6 line is the standard 2T (the E6 singularity); b_2(CP^3/2T) = 1 since 2T lies in
the connected SU(4) and acts trivially on H^*(CP^3; Q). The inflow statement is Witten's, cited by the seat, not derived here."""
import sympy as sp
I = sp.I
def M(a,b,c,d): return sp.ImmutableMatrix([[a,b],[c,d]])
i_ = M(I,0,0,-I); j_ = M(0,1,-1,0); k_ = i_*j_; w6 = sp.ImmutableMatrix(((sp.eye(2)+i_+j_+k_)/2).applyfunc(sp.nsimplify))
gens = [i_, w6]; G = {sp.ImmutableMatrix(sp.eye(2))}; fr = list(G)
while fr:
    nxt = []
    for g in fr:
        for h in gens:
            m = sp.ImmutableMatrix((g*h).applyfunc(sp.nsimplify))
            if m not in G: G.add(m); nxt.append(m)
    fr = nxt
orders = sorted({next(k for k in range(1,13) if g**k == sp.ImmutableMatrix(sp.eye(2))) for g in G})
X = sp.Matrix(2,2, sp.symbols('x0:4')); comm = sp.solve([e for g in gens for e in (X*g - g*X)], list(X.free_symbols), dict=True)
minus = sp.diag(-1,-1,1,1)
print("|2T| =", len(G), "orders", orders, "| commutant on C^2:", comm, "(scalars => irreducible; 2T-fixed locus = P(C^2_triv))")
print("(-1) on C^4:", list(minus.diagonal()), "=> fixed set P(C^2_std) u P(C^2_triv), complementary subspaces, disjoint in CP^3")
assert len(G) == 24 and orders == [1,2,3,4,6] and comm == [{sp.Symbol('x1'): 0, sp.Symbol('x2'): 0, sp.Symbol('x3'): sp.Symbol('x0')}]
print("VERIFIED")
