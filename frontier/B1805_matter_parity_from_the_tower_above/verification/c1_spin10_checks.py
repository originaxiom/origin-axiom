"""P-414 checks (exact where possible; data-free). (a) the centraliser of the fillings' order-2 line W = diag(1,1,1,-1,-1) in
su(5) and in so(10) (via SU(5) in SO(10) by z_k = x_k + i y_k); (b) Spin(10)'s order-2 central element on the 16 and the 10, by
weights, and as exp(i pi Q_X) with Q_X = 2 sum(lambda); (c) matter parity is not an element of S(U(3)xU(2)); (d) W's eigenvalues
on the 10 of SO(10) and on the 16 (which components it splits)."""
import itertools
import numpy as np
import sympy as sp

# (a) centralisers
W5 = np.diag([1, 1, 1, -1, -1]).astype(complex)
def centraliser_dim(basis, M):
    A = np.array([(X @ M - M @ X).ravel() for X in basis]).T
    return len(basis) - np.linalg.matrix_rank(np.hstack([A.real, A.imag]) if np.iscomplexobj(A) else A, tol=1e-9)
su5 = []
for i in range(5):
    for j in range(5):
        if i < j:
            E = np.zeros((5, 5), complex); E[i, j] = 1; E[j, i] = -1; su5.append(E)
            E = np.zeros((5, 5), complex); E[i, j] = 1j; E[j, i] = 1j; su5.append(E)
for k in range(4):
    E = np.zeros((5, 5), complex); E[k, k] = 1j; E[k + 1, k + 1] = -1j; su5.append(E)
print("(a) dim su(5) =", len(su5), "; centraliser of W in su(5):", centraliser_dim(su5, W5), "(s(u(3)+u(2)) = 12)")
def realify(M):
    n = M.shape[0]; R = np.zeros((2 * n, 2 * n))
    R[0::2, 0::2] = M.real; R[0::2, 1::2] = -M.imag; R[1::2, 0::2] = M.imag; R[1::2, 1::2] = M.real
    return R
W10 = realify(W5)
so10 = []
for i in range(10):
    for j in range(i + 1, 10):
        E = np.zeros((10, 10)); E[i, j] = 1; E[j, i] = -1; so10.append(E)
print("    W on the vector 10 of SO(10): eigenvalues", sorted(np.round(np.linalg.eigvals(W10).real).astype(int)), "; det", round(np.linalg.det(W10)))
print("    dim so(10) =", len(so10), "; centraliser of W in so(10):", centraliser_dim(so10, W10), "(so(6)+so(4) = 15+6 = 21: Pati-Salam)")

# (b) the centre on weights
half = sp.Rational(1, 2)
spinor = [w for w in itertools.product((half, -half), repeat=5) if sum(1 for x in w if x < 0) % 2 == 0]
vector = [tuple((1 if k == i else 0) * s for k in range(5)) for i in range(5) for s in (1, -1)]
z2 = lambda w: sp.exp(2 * sp.pi * sp.I * w[0])                      # exp(2 pi i <e1, lambda>)
qx = lambda w: 2 * sum(w)                                              # Q_X = 2 sum(lambda)
print("(b) 16 weights:", len(spinor), "; z2 on them:", set(sp.simplify(z2(w)) for w in spinor),
      "; on the 10:", set(sp.simplify(z2(w)) for w in vector))
print("    Q_X on the 16:", sorted(set(qx(w) for w in spinor)), "(multiplicities", {q: sum(1 for w in spinor if qx(w) == q) for q in set(qx(w) for w in spinor)}, ")")
print("    Q_X on the 10:", sorted(set(qx(w) for w in vector)), "; exp(i pi Q_X) on the 16:", set(sp.exp(sp.I * sp.pi * qx(w)) for w in spinor),
      "on the 10:", set(sp.exp(sp.I * sp.pi * qx(w)) for w in vector), " -> z2 = exp(i pi Q_X) = matter parity")

# (c) matter parity in the SM group? elements diag(a,a,a,b,b) times SU(3)/SU(2) centres act by scalars on irreps.
a, b = sp.symbols("a b")
conds = {"d^c (5bar triplet)": 1 / a, "L (5bar doublet)": 1 / b, "Q (10: ab)": a * b, "u^c (10: a^2)": a ** 2, "e^c (10: b^2)": b ** 2,
         "H_u (5 doublet)": b}
eqs = [sp.Eq(v, -1) for k, v in conds.items() if not k.startswith("H")] + [sp.Eq(conds["H_u (5 doublet)"], 1)]
print("(c) diag(a,a,a,b,b) acting as -1 on every matter field and +1 on H_u: solutions", sp.solve(eqs, [a, b], dict=True),
      "-> matter parity is not in S(U(3)xU(2))")

# (d) W on the 16 = 1 + 10 + 5bar (eigenvalues of diag(1,1,1,-1,-1) on Lambda^k)
w = [1, 1, 1, -1, -1]
lam2 = {("Q" if (i < 3) != (j < 3) else ("u^c" if i < 3 else "e^c")): w[i] * w[j] for i in range(5) for j in range(i + 1, 5)}
print("(d) W on the 10 of SU(5) (Lambda^2): Q ->", lam2["Q"], ", u^c ->", lam2["u^c"], ", e^c ->", lam2["e^c"],
      "; on the 5bar: d^c -> +1, L -> -1; on the 1: +1  => W splits a 16 (not a common charge)")
print("    W on the Higgs 10 of SO(10) = 5 + 5bar: colour triplets +1 (the (6,1,1)), doublets -1 (the (1,2,2)) -> doublet-triplet split persists")
print("c1 exit 0")
