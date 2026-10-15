"""Explicit E8 Lie algebra (Frenkel-Kac sign cocycle, Kac 7.8) in the lane's coordinates; auditor's own code.
Checks with real brackets and the Killing form what chat1's condensate_in_M argued from root combinatorics,
plus the two-condensate bracket the folder did not compute."""
import itertools, json
from fractions import Fraction as Fr
import numpy as np

# ---------------- roots (lane coordinates, 0-indexed), chain, weights of the 6, h_Q, colour, weak
def vec(*p):
    v = [Fr(0)] * 8
    for i, x in p: v[i] = Fr(x)
    return tuple(v)
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def add(a, b, s=1): return tuple(x + s * y for x, y in zip(a, b))
R = set()
for i, j in itertools.combinations(range(8), 2):
    for s, t in itertools.product((1, -1), repeat=2): R.add(vec((i, s), (j, t)))
for sg in itertools.product((1, -1), repeat=8):
    if sg.count(-1) % 2 == 0: R.add(tuple(Fr(s, 2) for s in sg))
ROOTS = sorted(R)
CHAIN = [vec((6, 1), (7, -1)), vec((5, 1), (6, -1)), vec((6, 1), (7, 1)), tuple(Fr(-1, 2) for _ in range(8)), vec((3, 1), (4, 1))]
COL = [vec((0, 1), (1, -1)), vec((1, 1), (2, -1))]; WEAK = vec((3, 1), (4, -1))
Gm = np.array([[float(dot(a, b)) for b in CHAIN] for a in CHAIN])
c0 = np.linalg.solve(Gm, np.array([1., 0, 0, 0, 0]))
w1 = sum(c0[k] * np.array([float(x) for x in CHAIN[k]]) for k in range(5))
WS = [w1]
for c in CHAIN: WS.append(WS[-1] - np.array([float(x) for x in c]))
WS = [tuple(Fr(x).limit_denominator(12) for x in w) for w in WS]
HQ = tuple(sum(s * w[k] for s, w in zip((1, -1, 1, -1, 1, -1), WS)) for k in range(8))
BETA = [add(WS[2 * r], WS[2 * r + 1], -1) for r in range(3)]
assert all(b in R for b in BETA)

# ---------------- simple roots: positive w.r.t. a generic vector; express all roots in that base
gen = np.array([1.0, 2.1, 3.3, 4.7, 5.2, 6.9, 7.4, 9.1]) + np.sqrt(np.arange(8) + 2) * 1e-3
pos = [r for r in ROOTS if np.dot([float(x) for x in r], gen) > 0]
posset = set(pos)
simple = [r for r in pos if not any(add(r, p, -1) in posset for p in pos)]
assert len(simple) == 8
S = np.array([[float(x) for x in s] for s in simple])          # 8 x 8
coords = {r: np.rint(np.linalg.solve(S.T, np.array([float(x) for x in r]))).astype(int) for r in ROOTS}
assert all(np.allclose(S.T @ coords[r], [float(x) for x in r]) for r in ROOTS)
A = np.array([[int(dot(a, b)) for b in simple] for a in simple])
B = np.zeros((8, 8), dtype=int)
for i in range(8):
    B[i, i] = 1
    for j in range(i + 1, 8):
        if A[i, j] == -1: B[i, j] = 1
def eps(a, b): return -1 if (coords[a] @ B @ coords[b]) % 2 else 1

# ---------------- structure constants: basis = 8 Cartan (orthonormal e_k) + 240 root vectors
N = 248; idx = {r: 8 + n for n, r in enumerate(ROOTS)}
f = np.zeros((N, N, N))
for k in range(8):                                   # [e_k, E_a] = a_k E_a
    for r in ROOTS:
        f[k, idx[r], idx[r]] = float(r[k]); f[idx[r], k, idx[r]] = -float(r[k])
negr = {r: tuple(-x for x in r) for r in ROOTS}
for a in ROOTS:
    for b in ROOTS:
        s = add(a, b)
        if all(x == 0 for x in s):                    # [E_a, E_-a] = -a  (Kac's convention)
            for k in range(8): f[idx[a], idx[b], k] = -float(a[k])
        elif s in R:
            f[idx[a], idx[b], idx[s]] = eps(a, b)
def br(x, y): return np.einsum("i,j,ijk->k", x, y, f, optimize=True)
def ad(x): return np.einsum("i,ijk->kj", x, f, optimize=True)
def K(x, y): return np.trace(ad(x) @ ad(y))
def cart(v): z = np.zeros(N, complex); z[:8] = [float(t) for t in v]; return z
def E(r): z = np.zeros(N, complex); z[idx[r]] = 1; return z
def dag(x):                                          # compact-form adjoint: h -> conj h, E_a -> -conj(c) E_-a
    y = np.zeros(N, complex); y[:8] = np.conj(x[:8])
    for r in ROOTS: y[idx[negr[r]]] = -np.conj(x[idx[r]])
    return y
rng = np.random.default_rng(1)
def rnd(): return rng.normal(size=N) + 1j * rng.normal(size=N)
out = {}
# T1 Jacobi, T2 dagger is an anti-automorphism and K(x, x^dag) has one sign
jac = 0.0
for _ in range(4):
    x, y, z = rnd(), rnd(), rnd()
    J = br(x, br(y, z)) + br(y, br(z, x)) + br(z, br(x, y))
    jac = max(jac, np.abs(J).max() / (np.abs(x).max() * np.abs(y).max() * np.abs(z).max()))
out["T1_jacobi_rel"] = float(jac)
x, y = rnd(), rnd()
out["T2_dagger_antiautomorphism_resid"] = float(np.abs(dag(br(x, y)) - br(dag(y), dag(x))).max())
out["T2_K(x,x^dag)_samples"] = [complex(K(v, dag(v))) for v in (rnd(), rnd(), rnd())]
cas = K(cart(vec((0, 1))), cart(vec((0, 1))))
out["killing_normalisation_K(e0,e0)"] = float(np.real(cas))   # 60 for E8 with (alpha,alpha)=2

# ---------------- M = su(2)_Q: h_Q, E_Q = sum E_beta_r, F_Q = -sum E_-beta_r
hQ = cart(HQ); EQ = sum(E(b) for b in BETA); FQ = -sum(E(negr[b]) for b in BETA)
out["T3_sl2_relations"] = {"[h,E]-2E": float(np.abs(br(hQ, EQ) - 2 * EQ).max()), "[h,F]+2F": float(np.abs(br(hQ, FQ) + 2 * FQ).max()),
                           "[E,F]-h": float(np.abs(br(EQ, FQ) - hQ).max()), "F_Q - EQ^dag": float(np.abs(FQ - dag(EQ)).max())}
Mb = [hQ, EQ, FQ]; Gram = np.array([[K(a, b) for b in Mb] for a in Mb]); Ginv = np.linalg.inv(Gram)
def PiM(x): c = Ginv @ np.array([K(m, x) for m in Mb]); return c          # coefficients on (h_Q, E_Q, F_Q)
def Mvec(c): return c[0] * hQ + c[1] * EQ + c[2] * FQ
def nullness(c):                                          # |K(v,v)| / K(v, v^dag): 0 = null, 1 = complex multiple of a real vector
    v = Mvec(c); return float(abs(K(v, v)) / abs(K(v, dag(v)))) if np.abs(c).max() > 1e-12 else None
# A1a with real brackets: M commutes with colour roots, weak roots and every block-scalar Y
smroots = [COL[0], COL[1], add(COL[0], COL[1]), WEAK]
sm = [E(r) for r in smroots] + [E(negr[r]) for r in smroots]
def ycart(y):
    c = (y[0], y[0], y[1], y[1], y[2], y[2]); return tuple(sum(ci * w[k] for ci, w in zip(c, WS)) for k in range(8))
Ys = [ycart(p) for p in itertools.permutations((Fr(1, 6), Fr(-5, 6), Fr(2, 3)))]
out["A1a_[M,SM]_max"] = float(max(np.abs(br(m, s)).max() for m in Mb for s in sm + [cart(Y) for Y in Ys]))
# A1b / A1c with real brackets, all 112 p-odd roots
ODD = [r for r in ROOTS if dot(r, HQ) % 2 != 0]
out["n_odd"] = len(ODD)
out["A1b_max_|Pi_M(E_alpha)|"] = float(max(np.abs(PiM(E(r))).max() for r in ODD))
a1c = []
for r in ODD:
    Hc = br(E(r), dag(E(r)))                                 # the condensate's sl2 Cartan, [E, E^dag]
    c = PiM(Hc); pred = float(dot(r, HQ)) / 6
    a1c.append((abs(c[0] - pred) + abs(c[1]) + abs(c[2]), nullness(c), float(np.real(c[0]))))
out["A1c_max_dev_from_(alpha.hQ/6)hQ"] = max(t[0] for t in a1c)
out["A1c_nullness_range_(1=real_direction)"] = [min(t[1] for t in a1c), max(t[1] for t in a1c)]

# ---------------- the two-condensate bracket (not computed in the folder)
NAMES = ["b", "a", "ab"]
def higgs_like(Y):
    rows = []
    for r in ODD:
        if (dot(r, COL[0]), dot(r, COL[1])) != (0, 0): continue
        t3, yr = dot(r, WEAK) / 2, dot(r, Y)
        if abs(yr) == Fr(1, 2) and t3 + yr == 0: rows.append(r)
    return rows
pair_rows = []
for p in itertools.permutations((Fr(1, 6), Fr(-5, 6), Fr(2, 3))):
    Y = ycart(p); hl = higgs_like(Y)
    for a, b in itertools.combinations(hl, 2):
        c = PiM(br(E(a), E(b)))
        if np.abs(c).max() > 1e-12:
            pair_rows.append({"Y": [str(t) for t in p], "Y(a),Y(b)": [str(dot(a, Y)), str(dot(b, Y))],
                              "coeffs_on_(hQ,EQ,FQ)": [complex(np.round(t, 12)) for t in c], "nullness": nullness(c),
                              "commutes_with_SM": float(max(np.abs(br(Mvec(c), s)).max() for s in sm + [cart(Y)]))})
out["pairs_with_nonzero_M_part"] = pair_rows
# weak-singlet (epsilon-contracted) combination of the two doublets for one Y, to rule out a cancellation
p = (Fr(1, 6), Fr(2, 3), Fr(-5, 6)); Y = ycart(p); hl = higgs_like(Y)
a, b = [(a, b) for a, b in itertools.combinations(hl, 2) if add(a, b) in [tuple(-x for x in BETA[2]), BETA[2]]][0]
a2, b2 = add(a, WEAK, -1 if dot(a, WEAK) > 0 else 1), add(b, WEAK, -1 if dot(b, WEAK) > 0 else 1)   # partners in each doublet
assert a2 in R and b2 in R
# the doublet partner is the weak lowering/raising image: D_a = [E_-+weak, E_a]
Ew, Fw = E(WEAK), E(tuple(-x for x in WEAK))
Pa = br(Fw, E(a)) if dot(a, WEAK) > 0 else br(Ew, E(a)); Pb = br(Fw, E(b)) if dot(b, WEAK) > 0 else br(Ew, E(b))
singlet = br(E(a), Pb) - br(Pa, E(b))
cs = PiM(singlet); out["weak_singlet_combination"] = {"coeffs": [complex(np.round(t, 12)) for t in cs], "nullness": nullness(cs)}
out["weak_triplet_combination_M_part"] = [complex(np.round(t, 12)) for t in PiM(br(E(a), Pb) + br(Pa, E(b)))]

# ---------------- sl2-type superposition condensate q = E_a + E_b (a + b a root): is it an sl2, and its M-parts
q = E(a) + E(b); Hs = br(q, dag(q))
out["superposition"] = {"[H,q]-q": float(np.abs(br(Hs, q) - q).max()),
                        "sl2 (E=sqrt2 q, H=2[q,q^dag]) [H,E]-2E": float(np.abs(br(2 * Hs, np.sqrt(2) * q) - 2 * np.sqrt(2) * q).max()),
                        "Pi_M(q)": float(np.abs(PiM(q)).max()), "Pi_M(H) coeffs": [complex(np.round(t, 12)) for t in PiM(2 * Hs)],
                        "Pi_M(H) nullness": nullness(PiM(2 * Hs))}
# closure: the algebra generated by q and q^dag
span = [q, dag(q), Hs]
for _ in range(3):
    new = [br(u, v) for u in span for v in span]
    Mx = np.array(span + new); rnk = np.linalg.matrix_rank(Mx, tol=1e-9)
out["superposition_generated_algebra_dim"] = int(rnk)
# a generic p-odd superposition (not an sl2): quartic iterated bracket's M-part
cz = rng.normal(size=len(ODD)) + 1j * rng.normal(size=len(ODD))
qg = sum(c * E(r) for c, r in zip(cz, ODD))
v4 = br(qg, br(dag(qg), br(qg, dag(qg))))
c4 = PiM(v4); out["generic_superposition_quartic_M_part"] = {"coeffs": [complex(np.round(t, 6)) for t in c4], "nullness": nullness(c4),
                                                              "Pi_M(q)": float(np.abs(PiM(qg)).max()), "Pi_M([q,q^dag]) nullness": nullness(PiM(br(qg, dag(qg))))}
print(json.dumps(out, indent=1, default=str))
json.dump(out, open("e8_explicit.json", "w"), indent=1, default=str)
