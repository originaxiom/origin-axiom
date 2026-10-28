"""Referee B1805, r1: claims (a) and (b) in an explicit Spin(10) (32x32 Clifford matrices; the 16 = chirality +1).
Independent of the draft's weight bookkeeping: W is built as exp of an su(5) element, realified into so(10), lifted by
the spin representation, and every statement is read off matrices.
(a) W in Spin(10): order, image in SO(10), eigenvalues on 16, centraliser in so(10) (dimension AND block structure),
    the group-level centraliser (does the non-identity component of C_SO(10)(R) = S(O(6)xO(4)) lift into C(W)?),
    and whether W and z2 W are conjugate.
(b) z2 (kernel of Spin -> SO), Q_X = -2i rho(J) (J = complex structure), exp(i pi Q_X) = z2, z4 = exp(i pi Q_X / 2) central."""
import itertools
import numpy as np
from scipy.linalg import expm

np.set_printoptions(precision=4, suppress=True)
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]).astype(complex)
I2 = np.eye(2, dtype=complex)
def kron(*ms):
    out = np.array([[1]], complex)
    for m in ms: out = np.kron(out, m)
    return out
# Cl(10) hermitian generators, gamma_a^2 = 1 (Jordan-Wigner)
G = []
for k in range(5):
    G.append(kron(*([s3] * k + [s1] + [I2] * (4 - k))))
    G.append(kron(*([s3] * k + [s2] + [I2] * (4 - k))))
G = [g for g in G]
for a in range(10):
    for b in range(10):
        ac = G[a] @ G[b] + G[b] @ G[a]
        assert np.allclose(ac, 2 * np.eye(32) * (a == b))
chir = (-1j) ** 5 * np.linalg.multi_dot(G)
assert np.allclose(chir @ chir, np.eye(32))
P16 = np.linalg.eigh(chir)[1][:, np.isclose(np.linalg.eigvalsh(chir), 1)]   # 32x16 basis of the 16
def rho(X):            # spin rep of X in so(10) (real antisymmetric): (1/4) sum X_ab gamma_a gamma_b
    return 0.25 * sum(X[a, b] * G[a] @ G[b] for a in range(10) for b in range(10) if a != b)
# check the intertwining: [rho(X), gamma_c] = sum_d X_dc gamma_d  (fix convention)
rng = np.random.default_rng(1)
A = rng.normal(size=(10, 10)); X = A - A.T
lhs = [rho(X) @ G[c] - G[c] @ rho(X) for c in range(10)]
ok_plus = all(np.allclose(lhs[c], sum(X[d, c] * G[d] for d in range(10))) for c in range(10))
ok_minus = all(np.allclose(lhs[c], -sum(X[d, c] * G[d] for d in range(10))) for c in range(10))
sgn = 1 if ok_plus else -1
assert ok_plus or ok_minus
def rho_(X): return sgn * rho(X) if sgn == 1 else rho(-X)     # so that rho_(X) gamma rho_(X)^-1 = sum X gamma (vector rep)
def act_on_vector(S):  # the SO(10) image R of a spin element S: S gamma_c S^-1 = sum_d R_dc gamma_d
    Si = np.linalg.inv(S)
    return np.array([[np.real(np.trace(G[d] @ S @ G[c] @ Si)) / 32 for c in range(10)] for d in range(10)])
def realify(M):
    n = M.shape[0]; R = np.zeros((2 * n, 2 * n))
    R[0::2, 0::2] = M.real; R[0::2, 1::2] = -M.imag; R[1::2, 0::2] = M.imag; R[1::2, 1::2] = M.real
    return R
def restrict16(S): return P16.conj().T @ S @ P16
print("Clifford checks passed; spin-rep convention sign", sgn)

# ---------- (a) ----------
T = 1j * np.pi * np.diag([0, 0, 0, 1, -1])                 # su(5): traceless, anti-hermitian; exp(T) = diag(1,1,1,-1,-1)
assert np.allclose(expm(T), np.diag([1, 1, 1, -1, -1]))
XT = realify(T)                                           # so(10) element (real antisymmetric)
assert np.allclose(XT, -XT.T)
W = expm(rho_(XT))
R = act_on_vector(W)
print("(a) W lifted to Spin(10):  W^2 = 1 ?", np.allclose(W @ W, np.eye(32)), "; W commutes with chirality ?",
      np.allclose(W @ chir, chir @ W))
print("    image in SO(10) equals realify(diag(1,1,1,-1,-1)) ?", np.allclose(R, realify(np.diag([1, 1, 1, -1, -1]).astype(complex))),
      "; diag of image:", np.round(np.diag(R)).astype(int))
ev16 = np.round(np.linalg.eigvals(restrict16(W)).real).astype(int)
print("    W on the 16: eigenvalue +1 x", int((ev16 == 1).sum()), ", -1 x", int((ev16 == -1).sum()), "; trace", int(ev16.sum()))
# centraliser in so(10) via the spin rep (group element W), real-linear algebra done correctly (vstack of re/im)
basis = []
for a in range(10):
    for b in range(a + 1, 10):
        E = np.zeros((10, 10)); E[a, b] = 1; E[b, a] = -1; basis.append((a, b, E))
cols = [ (rho_(E) @ W - W @ rho_(E)).ravel() for _, _, E in basis ]
Amat = np.array(cols).T
Ar = np.vstack([Amat.real, Amat.imag])
kdim = len(basis) - np.linalg.matrix_rank(Ar, tol=1e-9)
plus = [i for i in range(10) if R[i, i] > 0]; minus = [i for i in range(10) if R[i, i] < 0]
inblock = [(a, b) for a, b, E in basis if (a in plus) == (b in plus)]
comm_ok = all(np.allclose(rho_(E) @ W, W @ rho_(E)) for a, b, E in basis if (a, b) in inblock)
print("    centraliser of W in so(10) (spin rep, re/im stacked as rows): dim", kdim,
      "; the", len(inblock), "block-diagonal generators M_ab (a,b both in the +1 block", plus, "or both in the -1 block", minus,
      ") all commute:", comm_ok, "-> so(6)+so(4) = su(4)+su(2)+su(2) exactly (not only dim 21)")
# group level: C_SO(10)(R) = S(O(6) x O(4)) has two components; take the element reflecting one +1 axis and one -1 axis.
i, j = plus[0], minus[0]
g = G[i] @ G[j]                                            # in Spin(10) (even, unitary up to sign), image = reflection in e_i and e_j
Rg = act_on_vector(g)
print("    g = gamma_%d gamma_%d: image diag" % (i, j), np.round(np.diag(Rg)).astype(int), "(in S(O(6)xO(4)), det -1 on each block)")
gWg = g @ W @ np.linalg.inv(g)
print("    g W g^-1 = W ?", np.allclose(gWg, W), "; = -W (= z2 W) ?", np.allclose(gWg, -W),
      "-> the non-identity component conjugates W to z2 W, so C_Spin(10)(W) = preimage of SO(6)xSO(4) = (Spin(6)xSpin(4))/Z2,",
      "CONNECTED, = (SU(4)xSU(2)xSU(2))/Z2; and W ~ z2 W are conjugate (the lift's sign is immaterial)")
# ---------- (b) ----------
E12 = np.zeros((10, 10)); E12[0, 1] = 1; E12[1, 0] = -1
z2 = expm(rho_(2 * np.pi * E12))
print("(b) z2 = lift of the 2 pi rotation in one plane: = -1 on the spinor ?", np.allclose(z2, -np.eye(32)),
      "; image in SO(10) is 1 ?", np.allclose(act_on_vector(z2), np.eye(10)))
J = realify(1j * np.eye(5))                                # u(1)_X generator: the complex structure
QX = -2j * rho_(J)
assert np.allclose(QX, QX.conj().T)
q16 = np.round(np.linalg.eigvalsh(restrict16(QX))).astype(int)
from collections import Counter
print("    Q_X = -2i rho(J) on the 16:", dict(Counter(q16.tolist())), "; on the vector:", sorted(set(np.round(np.linalg.eigvals(-2j * J).real).astype(int).tolist())))
print("    exp(i pi Q_X) = z2 on the full spinor ?", np.allclose(expm(1j * np.pi * QX), z2),
      "; its vector image = 1 ?", np.allclose(expm(np.pi * J * 2), np.eye(10)))
z4 = expm(1j * np.pi * QX / 2)
z4_16 = restrict16(z4)
print("    z4 = exp(i pi Q_X / 2): on the 16 a scalar?", np.allclose(z4_16, z4_16[0, 0] * np.eye(16)), "value", np.round(z4_16[0, 0], 6),
      "; vector image = -1 ?", np.allclose(expm(np.pi * J), -np.eye(10)), "; z4^2 = z2 ?", np.allclose(z4 @ z4, z2))
# z4 central: commutes with every rho(M_ab)
print("    z4 commutes with all 45 generators ?", all(np.allclose(z4 @ rho_(E), rho_(E) @ z4) for _, _, E in basis))
# U(1)_X lies in the Pati-Salam centraliser (J is block diagonal for W's blocks)
print("    J (U(1)_X) commutes with W ?", np.allclose(rho_(J) @ W, W @ rho_(J)))
print("r1 exit 0")
