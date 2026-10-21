"""P-229 (B1652's FAILS cells F3 D3/D4): main's own check of the SM seat's W83 (the commutant of colour and SU(2)_w in e8 is
su(6); on its 6 = 3 (x) 2_q the trace-free Y commuting with the holonomy and the moves has dimension 0 through O, 1 through
S3, 8 if trivial) and of W81's branching (the 248 under the continuous SU(2)_q of the quaternion Cartan: 55 + 52 x 2 +
27 x 3 + 2 x 4; '2 (x) 56' only for Q8).  From the seat's read-outs (harvest rows 1157, 1166), not its scripts."""
import itertools, json, pathlib, importlib.util, io, contextlib
import numpy as np
from collections import Counter
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
out = {}

# ---- E8's roots; A2 + A1 and its commutant ----
R = []
for i, j in itertools.combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = np.zeros(8); v[i] = si; v[j] = sj; R.append(v)
for signs in itertools.product((0.5, -0.5), repeat=8):
    if sum(1 for s in signs if s < 0) % 2 == 0: R.append(np.array(signs))
R = np.array(R); assert len(R) == 240
a1 = R[0]; a2 = next(r for r in R if abs(r @ a1 + 1) < 1e-9)          # a simple pair of A2
E6 = [r for r in R if abs(r @ a1) < 1e-9 and abs(r @ a2) < 1e-9]
b = E6[0]                                                             # a root of the centraliser E6: SU(2)_w
A5 = [r for r in E6 if abs(r @ b) < 1e-9]
out["centraliser_of_A2_roots"] = len(E6)                              # 72 = E6
out["commutant_roots"] = len(A5); out["commutant_dim"] = len(A5) + 8 - 3
# its type: the simple roots of the commutant from a generic regular functional
f = np.array([1, 2, 3, 5, 7, 11, 13, 17.1]); pos = [r for r in A5 if r @ f > 0]
simple = [r for r in pos if not any(np.allclose(r, p + q) for p in pos for q in pos)]
C = np.array([[int(round(x @ y)) for y in simple] for x in simple])
out["commutant_simple_roots"] = len(simple)
out["commutant_cartan_is_A5"] = bool(len(simple) == 5 and sorted(Counter((C == -1).sum(1)).items()) == [(1, 2), (2, 3)]
                                     and np.linalg.matrix_rank(C) == 5 and abs(np.linalg.det(C) - 6) < 1e-9)

# ---- W83's dimensions on 6 = 3 (x) 2_q ----
def commutant_dim(gens, n):
    """dim of {X in M_n(C): X g = g X for all g}"""
    rows = [np.kron(np.eye(n), g.T) - np.kron(g, np.eye(n)) for g in gens]   # vec(X g - g X) in row-major
    A = np.vstack(rows) if rows else np.zeros((1, n * n))
    return n * n - np.linalg.matrix_rank(A, tol=1e-9)
spec = importlib.util.spec_from_file_location("hands", ROOT / "frontier/B1610_the_hands_on_the_founding_torsor/verification/hands_on_the_torsor.py")
Hm = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(Hm)
W = Hm.W
ML, MR = np.array(W.ML, complex), np.array(W.MR, complex)
# V = T + Tbar: T is B1610's Q-definite isotypic piece (an orthonormal basis Qp); the moves keep it
Qp = Hm.PIECES["T"]
for M in (ML, MR): assert np.allclose(M @ Qp, Qp @ (Qp.conj().T @ M @ Qp), atol=1e-8), "T not invariant"
LT, RT = Qp.conj().T @ ML @ Qp, Qp.conj().T @ MR @ Qp
out["moves_on_T_commutant_dim"] = int(commutant_dim([LT, RT], 3))
# the 6 = T (x) 2_q with Q8 acting on 2_q by rho_Q and the moves on T (any lift on 2_q: the commutant of rho_Q is scalar)
i2 = np.array([[1j, 0], [0, -1j]]); j2 = np.array([[0, 1], [-1, 0]], complex)
Q = [np.kron(np.eye(3), i2), np.kron(np.eye(3), j2)]
out["Y_dim_moves_through_O"] = int(commutant_dim(Q + [np.kron(LT, np.eye(2)), np.kron(RT, np.eye(2))], 6)) - 1
P3 = [np.eye(3)[[1, 0, 2]], np.eye(3)[[1, 2, 0]]]                     # S3 permuting the three
out["Y_dim_through_S3"] = int(commutant_dim(Q + [np.kron(p, np.eye(2)) for p in P3], 6)) - 1
out["Y_dim_trivial"] = int(commutant_dim(Q, 6)) - 1
# the moves' image on T: its order and whether it is the octahedral rotation group's 3-dim irrep
def closure(gens):
    key = lambda M: (np.round(M, 6) + 0.0).tobytes()
    els = [np.eye(3, dtype=complex)]; seen = {key(els[0])}; k = 0
    while k < len(els):
        for g in gens:
            P = g @ els[k]
            if key(P) not in seen: seen.add(key(P)); els.append(P)
        k += 1
    return els
GT = closure([LT, RT]); out["moves_on_T_order"] = len(GT)
out["moves_on_T_character_norm"] = float(np.real(sum(abs(np.trace(g)) ** 2 for g in GT) / len(GT)))   # 1 iff irreducible

# ---- W81: the 248 under SU(2)_q, by weights ----
# E8 > SU(3) x SU(2)_w x SU(6): 248 = (8,1,1)+(1,3,1)+(1,1,35)+(1,2,20)+(3,2,6b)+(3b,2,6)+(3,1,15)+(3b,1,15b)
# SU(6) > SU(2)_q x SU(3)_f with 6 = (2, 3): the weights of 6 under SU(2)_q are +1/2 (x3), -1/2 (x3)
w6 = [0.5] * 3 + [-0.5] * 3
def wedge(k): return [sum(c) for c in itertools.combinations(w6, k)]
reps = {"1": [0.0], "6": w6, "6b": [-x for x in w6], "15": wedge(2), "15b": [-x for x in wedge(2)], "20": wedge(3),
        "35": [a - b for a in w6 for b in w6]}
reps["35"].remove(0.0)                                                # minus the singlet
pieces = [(8 * 1, "1"), (3 * 1, "1"), (1 * 1, "35"), (1 * 2, "20"), (3 * 2, "6b"), (3 * 2, "6"), (3 * 1, "15"), (3 * 1, "15b")]
wt = Counter()
for mult, r in pieces:
    for x in reps[r]: wt[round(2 * x)] += mult
assert sum(wt.values()) == 248
spins = {}; c = Counter(wt)
for m2 in sorted(c, reverse=True):
    while c[m2] > 0 and m2 >= 0:
        n = c[m2]; spins[m2] = spins.get(m2, 0) + n
        for k in range(-m2, m2 + 1, 2): c[k] -= n
out["W81_SU2q_multiplicities_by_dim"] = {str(k + 1): v for k, v in sorted(spins.items())}
# Q8 in SU(2)_q: a spin-j irrep restricts to Q8 as: dim 1 -> trivial; 2 -> rho_Q; 3 -> the three non-trivial
# characters; 4 -> 2 rho_Q.  rho_Q's multiplicity:
out["W81_rhoQ_multiplicity_on_Q8"] = spins.get(1, 0) + 2 * spins.get(3, 0)
out["W81_each_character_multiplicity_on_Q8"] = spins.get(2, 0)
out["W81_trivial_on_Q8"] = spins.get(0, 0)
print(json.dumps(out, indent=1))
json.dump(out, open(HERE / "main_w81_w83.json", "w"), indent=1)
