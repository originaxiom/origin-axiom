"""Referee: recompute masses from the stored N = 384 matrices (read-only), cross-check C1 against the two earlier outputs,
and test the two-forms algebra on random matrices and on the stored matrices."""
import json
import numpy as np

W = json.load(open("/home/claude/origin-axiom/relays/chat1_2026-10-14_step3/weights_cells.json"))
SEL = "/home/claude/origin-axiom/relays/chat1_2026-10-14_selection/"
PH = json.load(open(SEL + "post_hoc_invariant_masses.json"))["rows"]
LL = json.load(open(SEL + "lagrange_law.json"))["readouts"]["per thread"]
per = W["per thread"]

def M(x): return np.array([[complex(a, b) for a, b in row] for row in x])
def isqrt(K):
    ev, U = np.linalg.eigh(K)
    return U @ np.diag(ev ** -0.5) @ U.conj().T
def inv_form(KL, Y, KR): return np.sort(np.linalg.svd(isqrt(KL) @ Y @ isqrt(KR).T, compute_uv=False))
def old_form(K, Y): A = isqrt(K); return np.sort(np.linalg.svd(A.T @ Y @ A, compute_uv=False))

# 1. stored matrices reproduce stored masses
worst = (0, None)
for w, row in per.items():
    for c in ("C1", "C2", "C3"):
        mats = row[c]["matrices (N = 384)"]
        s = inv_form(M(mats["K_L"]), M(mats["Y"]), M(mats["K_R"]))
        m = np.array(row[c]["m"])
        dev = np.max(np.abs(s - m)) / m[2]
        if dev > worst[0]: worst = (dev, (w, c))
print("stored matrices -> stored masses, worst |dev|/m3:", worst)

# Y symmetric for C1? K Hermitian?
herm = max(np.max(np.abs(M(per[w][c]["matrices (N = 384)"][k]) - M(per[w][c]["matrices (N = 384)"][k]).conj().T)) /
           np.max(np.abs(M(per[w][c]["matrices (N = 384)"][k]))) for w in per for c in ("C1", "C2", "C3") for k in ("K_L", "K_R"))
symY1 = max(np.max(np.abs(M(per[w]["C1"]["matrices (N = 384)"]["Y"]) - M(per[w]["C1"]["matrices (N = 384)"]["Y"]).T)) for w in per)
print("K Hermitian to", herm, "; C1's Y symmetric to", symY1)

# 2. C1 (invariant form) vs post hoc 'new' and lagrange_law (old form), on admitted
d_new, d_old_sym, d_old_non = 0, 0, (0, None)
def rots(w): return {w[k:] + w[:k] for k in range(len(w))}
def refl(w): R = rots(w); return w[::-1] in R or w.translate(str.maketrans("LR", "RL")) in R
for w in per:
    if not per[w]["C1"]["admitted"]: continue
    for k in ("m2/m3", "m1/m3"):
        a = per[w]["C1"][k]
        d_new = max(d_new, abs(a - PH[w]["new " + k]) / abs(a))
        dv = abs(a - LL[w][k]) / abs(a)
        if refl(w): d_old_sym = max(d_old_sym, dv)
        elif dv > d_old_non[0]: d_old_non = (dv, w)
print("C1 vs post hoc invariant form (59 admitted):", d_new)
print("C1 vs lagrange_law.json, symmetric admitted:", d_old_sym, "; non-symmetric:", d_old_non)
q0a = max(abs(per[w]["C1"][k] - LL[w][k]) / abs(LL[w][k]) for w in ("LR", "LLR", "LLRR", "LLRLR", "LLLR") for k in ("m2/m3", "m1/m3"))
print("Q0(a) recomputed:", q0a, " JSON:", W["Q0"]["(a) C1 against lagrange_law.json, worst relative"])

# 3. old vs invariant form on the stored C1 matrices (N = 384), non-symmetric threads
worst = (0, None)
for w in per:
    mats = per[w]["C1"]["matrices (N = 384)"]
    K, Y = M(mats["K_L"]), M(mats["Y"])
    a, b = inv_form(K, Y, K), old_form(K, Y)
    dev = max(abs(a[1] / a[2] - b[1] / b[2]) / (b[1] / b[2]), abs(a[0] / a[2] - b[0] / b[2]) / (b[0] / b[2]))
    if dev > worst[0]: worst = (dev, w)
print("old vs invariant form recomputed from stored C1 matrices, worst relative:", worst)

# 4. algebra on random matrices
rng = np.random.default_rng(1)
def rand_herm_pd():
    X = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); return X @ X.conj().T + 0.1 * np.eye(3)
def rand_csym():
    X = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); return X + X.T
res = {"K real": 0, "Y real": 0, "both complex (max rel diff)": 0, "both complex (median)": []}
for _ in range(2000):
    Kc = rand_herm_pd(); Kr = Kc.real.copy(); Kr = (Kr + Kr.T) / 2 + 3 * np.eye(3)
    Yc = rand_csym(); Yr = Yc.real.copy()
    for tag, K, Y in (("K real", Kr, Yc), ("Y real", Kc, Yr)):
        a, b = inv_form(K, Y, K), old_form(K, Y)
        res[tag] = max(res[tag], np.max(np.abs(a - b)) / a[2])
    a, b = inv_form(Kc, Yc, Kc), old_form(Kc, Yc)
    r = np.max(np.abs(a - b)) / a[2]
    res["both complex (max rel diff)"] = max(res["both complex (max rel diff)"], r); res["both complex (median)"].append(r)
res["both complex (median)"] = float(np.median(res["both complex (median)"]))
print("random-matrix algebra:", res)
# basis invariance of the invariant form under GL (not only unitary) changes, and failure of the old form under unitary
G = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
Q = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))[0]
K, Y = rand_herm_pd(), rand_csym()
for tag, U in (("GL", G), ("unitary", Q)):
    a0, a1 = inv_form(K, Y, K), inv_form(U @ K @ U.conj().T, U @ Y @ U.T, U @ K @ U.conj().T)
    b0, b1 = old_form(K, Y), old_form(U @ K @ U.conj().T, U @ Y @ U.T)
    print(tag, "change: invariant form moves", np.max(np.abs(a0 - a1)) / a0[2], "; old form moves", np.max(np.abs(b0 - b1)) / b0[2])
