#!/usr/bin/env python3
"""
F4 track-S verify: INDEPENDENT recompute of B649 stage 3a's headline
dimensions (solo h0=1,h1=3; double h0=1,h1=5), via a NUMERIC route that
shares NOTHING with cc's exact Fraction-vector quotient-ring / Gaussian
elimination code path in b649_stage3a.py:

  - arithmetic: numpy complex128 (floating point), not exact Q(s,i)
  - matrix exponential: scipy.linalg.expm (library Pade approximant),
    not a hand-rolled nilpotent Taylor series
  - rank/dimension: numpy.linalg.svd singular-value counting, not
    Gaussian elimination over a field

Inputs: only the hash-verified, persisted entries_L.json (exact SL2(L)
generators) and e6_principal_rational.json (exact rational E_PR/F_PR/H_PR)
from frontier/B649_silver_holonomy -- the construction (weld equations,
Bruhat lift formula, Fox calculus) follows the preregistered conventions
(PREREG_STAGE2B.md / PREREG_STAGE3A.md), since that IS the correct/only
construction, not an implementation trick to reproduce.

If the numeric singular-value spectrum shows a clean gap (>=1e6) between
"zero" and "nonzero" singular values, the numeric rank is a faithful,
independent stand-in for the exact rank cc computed symbolically.
"""
import json
import time

import numpy as np
from scipy.linalg import expm

SRC = "<seat-workdir>/origin-axiom/frontier/B649_silver_holonomy"
RESULTS = {}

# ----------------------------------------------------------------------------
# 0. s (real root of s^4 - 8 s^2 - 16), i -- numeric embedding of L into C
# ----------------------------------------------------------------------------
s_num = (4 + 4 * 2 ** 0.5) ** 0.5
print("s_num =", s_num, " quartic residual:", s_num ** 4 - 8 * s_num ** 2 - 16)


def frac(x):
    if "/" in x:
        n, d = x.split("/")
        return float(n) / float(d)
    return float(x)


def L_eval(re_c, im_c):
    re = sum(frac(c) * s_num ** k for k, c in enumerate(re_c))
    im = sum(frac(c) * s_num ** k for k, c in enumerate(im_c))
    return complex(re, im)


# ----------------------------------------------------------------------------
# 1. Load the exact SL2(L) generators (entries_L.json) numerically
# ----------------------------------------------------------------------------
d2 = json.load(open(f"{SRC}/entries_L.json"))


def gen2_num(nm):
    return np.array([[L_eval(*d2[f"{nm}{i}{j}"]) for j in range(2)] for i in range(2)],
                     dtype=complex)


G2 = {nm: gen2_num(nm) for nm in "abc"}
for nm in "abc":
    M = G2[nm]
    adj = np.array([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]])
    G2[nm.upper()] = adj
    print(f"  det({nm}) numeric = {np.linalg.det(M):.3e} (should be ~1)")

# ----------------------------------------------------------------------------
# 2. Load E_PR, F_PR, H_PR (rational, exact) as complex128 numpy arrays
# ----------------------------------------------------------------------------
pr = json.load(open(f"{SRC}/e6_principal_rational.json"))


def to_arr(rows):
    return np.array([[frac(x) for x in row] for row in rows], dtype=complex)


E_PR = to_arr(pr["e_pr"])
F_PR = to_arr(pr["f_pr"])
H_PR = to_arr(pr["h_pr"])
weights = [int(H_PR[i, i].real) for i in range(27)]
print("weights:", weights)


def lift_sl2(g):
    p, q, r, s = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    det = p * s - q * r
    if abs(p) < 1e-300:
        w27 = expm(E_PR) @ expm(-F_PR) @ expm(E_PR)
        return w27 @ lift_sl2(np.array([[-r, -s], [p, q]], dtype=complex))
    lower = expm((r / p) * F_PR)
    upper = expm((q / p) * E_PR)
    t2 = (p * p) / det
    D = np.diag([t2 ** (wgt / 2) for wgt in weights])
    return lower @ D @ upper


t0 = time.time()
S1 = {nm: lift_sl2(G2[nm]) for nm in "abcABC"}
print(f"lifted 6 side-1 letters to 27x27 (numeric) in {time.time()-t0:.2f}s")

# sanity: relators = I27 numerically (own numeric recheck of S2b-G1)
for rel in ("aBAbcc", "aaCbcB"):
    M = np.eye(27, dtype=complex)
    for ch in rel:
        M = M @ S1[ch]
    resid = np.max(np.abs(M - np.eye(27)))
    print(f"  numeric check {rel} = I27: max residual = {resid:.3e}")
    RESULTS[f"numeric_relator_{rel}_resid"] = resid

# ----------------------------------------------------------------------------
# 3. Weld solve, numerically (SVD nullspace of an 8x4 complex system)
# ----------------------------------------------------------------------------
def word2(w):
    M = None
    for ch in w:
        M = G2[ch] if M is None else M @ G2[ch]
    return M


MU2 = word2("CCB")
LAM2 = word2("caCA")
LAM2i = np.array([[LAM2[1, 1], -LAM2[0, 1]], [-LAM2[1, 0], LAM2[0, 0]]])


def weld_rows(Mc, T):
    """rows (as real/imag pairs) for u @ conj(Mc) - T @ u = 0, u a 2x2 unknown."""
    rows = []
    # u has unknowns u[0,0],u[0,1],u[1,0],u[1,1]; (u@Mc)[i,j] = sum_k u[i,k] Mc[k,j]
    # (T@u)[i,j] = sum_k T[i,k] u[k,j]
    for i in range(2):
        for j in range(2):
            row = np.zeros(4, dtype=complex)
            for p in range(2):
                for q in range(2):
                    coef = 0j
                    if p == i:
                        coef += Mc[q, j]
                    if q == j:
                        coef -= T[i, p]
                    row[2 * p + q] = coef
            rows.append(row)
    return np.array(rows)


rows = np.vstack([weld_rows(MU2.conj(), MU2), weld_rows(LAM2.conj(), LAM2i)])
print("weld system shape:", rows.shape)
U, Sv, Vh = np.linalg.svd(rows)
print("weld system singular values:", Sv)
u_vec = Vh[-1].conj()
u = u_vec.reshape(2, 2)
detu = np.linalg.det(u)
print("weld u (numeric):\n", u, "\ndet(u) =", detu)
resid_check = np.max(np.abs(rows @ u_vec))
print("residual of u in weld system:", resid_check)
RESULTS["weld_singular_values"] = Sv.tolist()
RESULTS["weld_det_u"] = str(detu)
RESULTS["weld_residual"] = float(resid_check)

U27 = lift_sl2(u)
U27i = np.linalg.inv(U27)
print("U27 . U27i - I max resid:", np.max(np.abs(U27 @ U27i - np.eye(27))))

S2 = {nm: U27 @ S1[nm].conj() @ U27i for nm in "abcABC"}

LETS = {"a": S1["a"], "b": S1["b"], "c": S1["c"],
        "A": S1["A"], "B": S1["B"], "C": S1["C"],
        "d": S2["a"], "e": S2["b"], "f": S2["c"],
        "D": S2["A"], "E": S2["B"], "F": S2["C"]}

# sanity: side-2 relators
prim2 = {"d": "a", "e": "b", "f": "c", "D": "A", "E": "B", "F": "C"}
for rel in ("dEDeff", "ddFefE"):
    M = np.eye(27, dtype=complex)
    for ch in rel:
        M = M @ LETS[ch]
    resid = np.max(np.abs(M - np.eye(27)))
    print(f"  numeric check side-2 relator {rel} = I27: max residual = {resid:.3e}")
    RESULTS[f"numeric_side2_relator_{rel}_resid"] = resid

# ----------------------------------------------------------------------------
# 4. Fox calculus rows (own fresh implementation), numeric, DOUBLE + SOLO
# ----------------------------------------------------------------------------
def fox_rows(relators, gens, lets):
    n = 27
    rows = []
    for w in relators:
        Lb = {g: np.zeros((n, n), dtype=complex) for g in gens}
        P = np.eye(n, dtype=complex)
        for ch in w:
            g = ch.lower()
            if ch.islower():
                term = P
            else:
                term = -(P @ lets[ch])
            Lb[g] = Lb[g] + term
            P = P @ lets[ch]
        for i in range(n):
            rows.append(np.concatenate([Lb[g][i, :] for g in gens]))
    return np.array(rows)


def coboundary(gens, lets):
    n = 27
    cols = []
    for j in range(n):
        v = np.zeros(n, dtype=complex)
        v[j] = 1.0
        col = []
        for g in gens:
            gv = lets[g] @ v
            col.append(gv - v)
        cols.append(np.concatenate(col))
    return np.array(cols).T  # rows = 6*27, cols = 27


def numeric_rank(M, tag):
    if M.size == 0:
        return 0, []
    sv = np.linalg.svd(M, compute_uv=False)
    smax = sv[0] if len(sv) else 0.0
    thresh = smax * 1e-9 if smax > 0 else 1e-9
    rk = int(np.sum(sv > thresh))
    print(f"  [{tag}] singular values (top 8): {sv[:8]}")
    print(f"  [{tag}] singular values (bottom 8): {sv[-8:]}")
    print(f"  [{tag}] numeric rank (thresh {thresh:.3e}) = {rk}")
    return rk, sv


print("\n== DOUBLE dimensions (numeric, own Fox-calculus code) ==")
RELATORS = ["aBAbcc", "aaCbcB", "dEDeff", "ddFefE", "CCBeff", "caCAfdFD"]
GENS = list("abcdef")
rows27 = fox_rows(RELATORS, GENS, LETS)
print("rows27 shape:", rows27.shape)
rk_rows, sv_rows = numeric_rank(rows27, "double Z1 rows")
z1 = rows27.shape[1] - rk_rows
cob = coboundary(GENS, LETS)
print("cob shape:", cob.shape)
rk_cob, sv_cob = numeric_rank(cob, "double coboundary")
h0 = 27 - rk_cob
h1 = z1 - rk_cob
print(f"DOUBLE: dim Z1 = {z1}; rank B1 = {rk_cob}; h0 = {h0}; h1 = {h1}")
print(f"  CLAIMED: dim Z1 = 31; rank B1 = 26; h0 = 1; h1 = 5")
RESULTS["double_z1"] = z1
RESULTS["double_rankB1"] = rk_cob
RESULTS["double_h0"] = h0
RESULTS["double_h1"] = h1

print("\n== SOLO dimensions (numeric, own Fox-calculus code) ==")
RELATORS_S = ["aBAbcc", "aaCbcB"]
GENS_S = list("abc")
LETS_S = {g: S1[g] for g in "abcABC"}
rows_solo = fox_rows(RELATORS_S, GENS_S, LETS_S)
print("rows_solo shape:", rows_solo.shape)
rk_rows_s, _ = numeric_rank(rows_solo, "solo Z1 rows")
z1s = rows_solo.shape[1] - rk_rows_s
cob_s = coboundary(GENS_S, LETS_S)
rk_cob_s, _ = numeric_rank(cob_s, "solo coboundary")
h0s = 27 - rk_cob_s
h1s = z1s - rk_cob_s
print(f"SOLO: dim Z1 = {z1s}; rank B1 = {rk_cob_s}; h0 = {h0s}; h1 = {h1s}")
print(f"  CLAIMED: dim Z1 = 29; rank B1 = 26; h0 = 1; h1 = 3")
RESULTS["solo_z1"] = z1s
RESULTS["solo_rankB1"] = rk_cob_s
RESULTS["solo_h0"] = h0s
RESULTS["solo_h1"] = h1s

with open("<seat-workdir>/seat-work/finisher_queue/f4_receipt/stage3_numeric_results.json", "w") as f:
    json.dump(RESULTS, f, indent=2, default=str)
print("\nWrote stage3_numeric_results.json")
