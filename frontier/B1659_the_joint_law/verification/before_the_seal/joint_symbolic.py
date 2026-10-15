"""EXPLORATION (P-168): the joint law, symbolically. Y(S, M) as in B1658 (bilinear). Prove:
 (1) det Y = 4 det S det M tr(eps S M^T);
 (2) adj Y = det S A(M) + det M At(S), with A(M) the quadratic extension of B1658's q~ p~^T and At(S) its mirror;
 and print A, At explicitly."""
import sympy as sp
s = sp.symbols('s0:4'); m = sp.symbols('m0:4')
S = sp.Matrix(2, 2, s); M = sp.Matrix(2, 2, m)
I = sp.I
QI = sp.Matrix([[I, 0], [0, -I]]); QJ = sp.Matrix([[0, 1], [-1, 0]]); QK = QI*QJ; EPS = QJ; BL = [QJ, QI, QK]
def Ymat(S, M): return sp.Matrix(3, 3, lambda a, b: sum(((BL[a].T*EPS*S*BL[b]).multiply_elementwise(M))))
Y = Ymat(S, M).applyfunc(sp.expand)
dS, dM = S.det(), M.det()
l = 4*(EPS*S*M.T).trace()
r1 = sp.expand(Y.det() - dS*dM*l)
print("(1) det Y - 4 det S det M tr(eps S M^T) =", r1)
adj = Y.adjugate().applyfunc(sp.expand)
# A(M): adj Y at S with det S = 1 is not linear-separable directly; obtain A as the coefficient: adj is bihomogeneous (2,2).
# Write adj = dS*A(M) + dM*At(S) + rem; get A by polynomial division in the S-variables modulo the ideal? Use: A(M) := adj Y(S*, M)
# for S* = identity-like with det 1 and null-S part removed: choose A by reduction of adj w.r.t. dS (lex in s) then read.
G = sp.groebner([dS], *s, order='lex')
A = sp.zeros(3, 3); At = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        q, rem = sp.reduced(adj[i, j], [dS], *s, order='lex')   # adj = q*dS + rem, rem free of the leading monomial of dS
        q = sp.expand(q[0]); rem = sp.expand(rem)
        # rem must vanish on det S = 0 only through dM: rem = dM * At(S)
        qq, rr = sp.reduced(rem, [dM], *m, order='lex')
        At[i, j] = sp.expand(qq[0]); assert sp.expand(rr) == 0, (i, j, rr)
        A[i, j] = q
ok = sp.expand(adj - dS*A - dM*At) == sp.zeros(3, 3)
print("(2) adj Y = det S A + det M At exactly:", ok)
print("    A depends only on M:", all(not (A[i, j].free_symbols & set(s)) for i in range(3) for j in range(3)))
print("    At depends only on S:", all(not (At[i, j].free_symbols & set(m)) for i in range(3) for j in range(3)))
print("A(M) ="); sp.pprint(A.applyfunc(sp.factor))
print("At(S) ="); sp.pprint(At.applyfunc(sp.factor))
