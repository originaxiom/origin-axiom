"""SEALED-DIGEST CHECK c5 (value-free algebra; first principles).
Claim (agy Theorem 20 Part C.2; relay l.274): for all 84 words w of length 1..3 in {g_L, g_R, g_L^-1, g_R^-1}
(g_L = (1+i)/sqrt2, g_R = (1-j)/sqrt2), the 12x12 'physical mass operator' M(Q, R) satisfies
    M(rho(w)Phi) T_in(rho(w)) = T_out(rho(w)) M(Phi),  T_in(U) = I6 (+) U(x)I3,  T_out(U) = I6 (+) conj(U)(x)I3,
with rho(w)Phi = (U00 Q + U01 R, U10 Q + U11 R).
The operator's block pattern is the lane's (visible through the mask); its scalar coefficients are masked, so they are
left GENERIC here (random complex c, rt, om, pb, pz): the identity is tested as a statement about the pattern.
Expected (derivation in the report): it holds for EVERY U in SU(2) and every coefficient choice, because
eps U eps^-1 = conj(U) on SU(2); it fails for U in U(2) with det U != 1.  The word list is then immaterial."""
import itertools, math
import numpy as np
rng = np.random.default_rng(5)
E = np.array([[0, 1], [0, 0]], complex); Fm = np.array([[0, 0], [1, 0]], complex); H = np.diag([1, -1]).astype(complex)
def ad(x): return np.column_stack([np.array([(x @ b - b @ x)[0, 1], (x @ b - b @ x)[1, 0], (x @ b - b @ x)[0, 0]]) for b in (E, Fm, H)])
def M12(Q, R, om, pb, pz, rt, c):
    aq, ar, aqd, ard = ad(Q), ad(R), ad(Q.conj().T), ad(R.conj().T); I3, Z3 = np.eye(3), np.zeros((3, 3))
    return np.block([[Z3, -pz * I3 / (rt * om ** 2), rt * 1j * aqd / om, rt * 1j * ard / om],
                     [rt * pz * I3, Z3, -c * 1j * ar, c * 1j * aq],
                     [-rt * 1j * aqd, 1j * ar / om, Z3, pb * I3 / om],
                     [-rt * 1j * ard, -1j * aq / om, -pb * I3 / om, Z3]])
def Tin(U): return np.block([[np.eye(6), np.zeros((6, 6))], [np.zeros((6, 6)), np.kron(U, np.eye(3))]])
def Tout(U): return np.block([[np.eye(6), np.zeros((6, 6))], [np.zeros((6, 6)), np.kron(U.conj(), np.eye(3))]])
def haar_su2():
    v = rng.normal(size=4); v /= np.linalg.norm(v); a, b = v[0] + 1j * v[1], v[2] + 1j * v[3]
    return np.array([[a, b], [-b.conjugate(), a.conjugate()]])
def err(U, conv):
    Q, R = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)), rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    om, pb, pz, rt, c = [complex(*rng.normal(size=2)) for _ in range(5)]
    if conv == "U": Qp, Rp = U[0, 0] * Q + U[0, 1] * R, U[1, 0] * Q + U[1, 1] * R
    else: Qp, Rp = U[0, 0] * Q + U[1, 0] * R, U[0, 1] * Q + U[1, 1] * R
    L = M12(Qp, Rp, om, pb, pz, rt, c) @ Tin(U); Rr = Tout(U) @ M12(Q, R, om, pb, pz, rt, c)
    return np.abs(L - Rr).max() / np.abs(Rr).max()
for conv in ("U", "U^T"):
    e_su2 = max(err(haar_su2(), conv) for _ in range(200))
    e_u2 = min(err(np.exp(1j * rng.uniform(0.3, 2.8)) * haar_su2(), conv) for _ in range(200))
    print("convention %-4s: worst over 200 Haar SU(2), generic coefficients: %.1e ; best over 200 U(2) with det != 1: %.2e" % (conv, e_su2, e_u2))
gL = (np.eye(2) + np.array([[1j, 0], [0, -1j]])) / math.sqrt(2); gR = (np.eye(2) - np.array([[0, 1], [-1, 0]], complex)) / math.sqrt(2)
gens = [gL, gR, gL.conj().T, gR.conj().T]; worst, n = 0.0, 0
for m in (1, 2, 3):
    for seq in itertools.product(range(4), repeat=m):
        U = np.eye(2, dtype=complex)
        for s in seq: U = U @ gens[s]
        worst = max(worst, err(U, "U")); n += 1
print("the lane's word list: %d words, worst %.1e ; T_in multiplicative on words: trivially (block Kronecker)" % (n, worst))
print("orders: g_L %d, g_R %d (in SU(2))" % tuple(next(k for k in range(1, 20) if np.abs(np.linalg.matrix_power(g, k) - np.eye(2)).max() < 1e-12) for g in (gL, gR)))
