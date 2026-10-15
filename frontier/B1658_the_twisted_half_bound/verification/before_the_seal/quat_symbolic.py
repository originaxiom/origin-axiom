"""EXPLORATION (main): symbolic checks of the twisted half bound. (1) adj Y(S, M) = det S * A(M) when det M = 0; (2) ||A||_F^2
= 4 ||M||_F^4 on null M; (3) the range of ||Y(S, M)||_F^2 over unit null S, M, by parametrising null 2x2 matrices as
rank-one outer products S = u v^T, M = p q^T."""
import sympy as sp
I = sp.I
QI = sp.Matrix([[I, 0], [0, -I]]); QJ = sp.Matrix([[0, 1], [-1, 0]]); QK = QI*QJ; EPS = QJ; BLOCKS = [QJ, QI, QK]
def coupling(S, M):
    return sp.Matrix(3, 3, lambda a, b: sum(((BLOCKS[a].T*EPS*S*BLOCKS[b]).multiply_elementwise(M))))
u0, u1, v0, v1, p0, p1, q0, q1 = sp.symbols("u0 u1 v0 v1 p0 p1 q0 q1")
S = sp.Matrix([u0, u1])*sp.Matrix([[v0, v1]]); M = sp.Matrix([p0, p1])*sp.Matrix([[q0, q1]])
Y = coupling(S, M)
print("Y(uv^T, pq^T) =")
sp.pprint(sp.factor(Y))
# general S (not null) with null M: adjugate factorisation
s = sp.symbols("s0:4"); Sg = s[0]*sp.eye(2) + s[1]*QI + s[2]*QJ + s[3]*QK
Yg = coupling(Sg, M)
adj = Yg.adjugate()
detS = sp.expand(Sg.det())
ratio = [sp.simplify(sp.factor(adj[i, j])/detS) for i in range(3) for j in range(3)]
print("adj Y / det S free of s?", all(not (r.free_symbols & set(s)) for r in ratio))
print("adj Y / det S (first row):", [sp.factor(r) for r in ratio[:3]])
