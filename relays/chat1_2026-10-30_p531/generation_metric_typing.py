"""The seat's check for P-531 (data-free; numpy only; written independently of B1822's code).

Setting (B1822; B1600's W10 conventions): the doublet rho_Q(a) = i, rho_Q(b) = j (quaternion units as 2x2 matrices);
three parity blocks p = j, i, k with characters (chi(a), chi(b)) = (-1,+1), (+1,-1), (-1,-1) and intertwiners
C_p = QJ, QI, QK (C_p rho C_p^-1 = chi_p rho). A move m with lift g (rho o m = Ad(g) rho) sends block p to the block p'
with chi_p' = chi_p o m, acting on the doublet by g^-1. Moves: L (a, b) -> (a, ab), g = (1+i)/sqrt2;
R (a, b) -> (ab, b), g = (1-j)/sqrt2; sign (a, b) -> (a^-1, b^-1), g = k; swap a <-> b, g = (i+j)/sqrt2.

It counts the hermitian forms X on C^3 (x) C^2 (generation outer, doublet inner) invariant under the flat holonomy
and the chosen moves (real dimension), and the real dimension of the generation metrics H they restrict to on the zero
modes psi_p = C_p F, H_pq = (1/2) tr(C_p^dag X_pq C_q) (B1822's restriction). LR is the product of the two actions
(the thread m004's monodromy).
"""
import itertools
import numpy as np

one = np.eye(2, dtype=complex)
Qi = np.array([[1j, 0], [0, -1j]]); Qj = np.array([[0, 1], [-1, 0]], dtype=complex); Qk = Qi @ Qj
rho = {"a": Qi, "b": Qj}
blocks = ["j", "i", "k"]
C = {"j": Qj, "i": Qi, "k": Qk}
char = {"j": {"a": -1, "b": 1}, "i": {"a": 1, "b": -1}, "k": {"a": -1, "b": -1}}
for p in blocks:
    for x in "ab":
        assert np.allclose(C[p] @ rho[x] @ np.linalg.inv(C[p]), char[p][x] * rho[x])

s = 1 / np.sqrt(2)
moves = {  # images of a and b as words (capital = inverse), and the lift g
    "L": ({"a": "a", "b": "ab"}, (one + Qi) * s),
    "R": ({"a": "ab", "b": "b"}, (one - Qj) * s),
    "sign": ({"a": "A", "b": "B"}, Qk),
    "swap": ({"a": "b", "b": "a"}, (Qi + Qj) * s),
}

def word_rho(w):
    M = one.copy()
    for c in w:
        M = M @ (rho[c] if c.islower() else np.linalg.inv(rho[c.lower()]))
    return M

def word_char(p, w):
    v = 1
    for c in w:
        v *= char[p][c.lower()]
    return v

for name, (img, g) in moves.items():  # the lift really satisfies rho o m = Ad(g) rho
    for x in "ab":
        assert np.allclose(word_rho(img[x]), g @ rho[x] @ np.linalg.inv(g)), name

def target(p, img):
    v = {x: word_char(p, img[x]) for x in "ab"}
    for q in blocks:
        if char[q] == v:
            return q
    raise ValueError

def M6(name):
    img, g = moves[name]; gi = np.linalg.inv(g); M = np.zeros((6, 6), dtype=complex)
    for ip, p in enumerate(blocks):
        iq = blocks.index(target(p, img)); M[2 * iq:2 * iq + 2, 2 * ip:2 * ip + 2] = gi
    return M

flat = [np.kron(np.diag([char[p][x] for p in blocks]).astype(complex), rho[x]) for x in "ab"]

def herm_basis(n):
    out = []
    for i in range(n):
        E = np.zeros((n, n), complex); E[i, i] = 1; out.append(E)
    for i, j in itertools.combinations(range(n), 2):
        E = np.zeros((n, n), complex); E[i, j] = E[j, i] = 1; out.append(E)
        E = np.zeros((n, n), complex); E[i, j] = 1j; E[j, i] = -1j; out.append(E)
    return out

def invariant_forms(gens, n):
    B = herm_basis(n)
    cols = [np.concatenate([np.concatenate([(g.conj().T @ E @ g - E).real.ravel(), (g.conj().T @ E @ g - E).imag.ravel()]) for g in gens]) for E in B]
    A = np.array(cols).T
    _, sv, Vh = np.linalg.svd(A)
    r = int(np.sum(sv > 1e-10 * max(sv.max(), 1)))
    return [sum(c * E for c, E in zip(v, B)) for v in Vh[r:]]

def restricted_dim(forms):
    Hs = [np.array([[0.5 * np.trace(C[blocks[p]].conj().T @ X[2*p:2*p+2, 2*q:2*q+2] @ C[blocks[q]]) for q in range(3)] for p in range(3)]) for X in forms]
    if not Hs:
        return 0
    return int(np.linalg.matrix_rank(np.array([np.concatenate([H.real.ravel(), H.imag.ravel()]) for H in Hs]), tol=1e-9))

# the inner automorphisms (conjugation by a and by b), with lifts rho(a), rho(b): on H they act as the parity grading
moves["c_a"] = ({"a": "a", "b": "abA"}, rho["a"])
moves["c_b"] = ({"a": "baB", "b": "b"}, rho["b"])
for nm in ("c_a", "c_b"):
    img, lift = moves[nm]
    for x in "ab":
        assert np.allclose(word_rho(img[x]), lift @ rho[x] @ np.linalg.inv(lift)), nm
M = {k: M6(k) for k in moves}
Li, Ri = np.linalg.inv(M["L"]), np.linalg.inv(M["R"])
centre = M["L"] @ Ri @ M["L"]; centre = centre @ centre          # (L R^-1 L)^2: the sign GM5b generates, Delta^2
at_i = M["R"] @ Li @ M["R"]                                         # the stabiliser of tau = i (B1634's P3)
at_w = M["L"] @ Ri                                                  # the stabiliser of tau = omega
LR = M["L"] @ M["R"]                                                # one thread's monodromy (m004); the 6x6 actions
                                                                    # compose in reverse, which is conjugate: same count
par = [M["c_a"], M["c_b"]]
iota = [M["sign"]]                                                  # W10's sign: (a, b) -> (a^-1, b^-1), lift k

def dimH(gens):
    return restricted_dim(invariant_forms(list(flat) + gens, 6))

print("Table A: the ruled branch's group <L, R> (real dimension of the generation metrics H kept)")
for label, gens in [("the flat holonomy alone (B1822's family)", []), ("L", [M["L"]]), ("R", [M["R"]]),
                    ("LR (one thread's monodromy)", [LR]), ("L and R", [M["L"], M["R"]]),
                    ("the stabiliser of a generic tau: the centre", [centre]), ("the stabiliser of tau = i: R L^-1 R", [at_i]),
                    ("the stabiliser of tau = omega: L R^-1", [at_w]), ("a 2-torsion line's stabiliser: L^2 and R", [M["L"] @ M["L"], M["R"]]),
                    ("GM5b's sign, (L R^-1 L)^2", [centre])]:
    print(f"  {label:48s} {dimH(gens)}")
print("Table B: with the inner automorphisms (the parity grading) and W10's sign iota")
for label, gens in [("the parity grading alone", par), ("the parity grading and a generic tau", par + [centre]),
                    ("the parity grading and tau = i", par + [at_i]), ("the parity grading and tau = omega", par + [at_w]),
                    ("the parity grading and one thread (LR)", par + [LR]), ("iota and a generic tau", iota + [centre]),
                    ("iota and tau = i", iota + [at_i]), ("iota and tau = omega", iota + [at_w]), ("L, R and iota", [M["L"], M["R"]] + iota),
                    ("L, R and the swap", [M["L"], M["R"], M["swap"]])]:
    print(f"  {label:48s} {dimH(gens)}")

# under L and R the kept line is H = I, and H = I is kept by every element used here
F = invariant_forms(list(flat) + [M["L"], M["R"]], 6)
X = F[0]
H = np.array([[0.5 * np.trace(C[blocks[p]].conj().T @ X[2*p:2*p+2, 2*q:2*q+2] @ C[blocks[q]]) for q in range(3)] for p in range(3)])
print("under L and R: H / H_11 equals the identity:", bool(np.allclose(H / H[0, 0], np.eye(3), atol=1e-12)))
print("H = I kept by L, R, sign, swap, c_a, c_b:", all(np.allclose(M[m].conj().T @ M[m], np.eye(6)) for m in M))
# W10's sign acts on H as one element of the parity grading: C_p^-1 k^-1 C_p = s_p k^-1
ki = np.linalg.inv(Qk)
print("iota on the generation index, s_p for p = j, i, k:",
      [int(round(np.real(np.trace(np.linalg.inv(C[p]) @ ki @ C[p] @ np.linalg.inv(ki)) / 2))) for p in blocks],
      " (the characters of a b^-1:", [char[p]["a"] * char[p]["b"] for p in blocks], ")")
