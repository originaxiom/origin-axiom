"""Independent recomputation of chat1's condensate-in-M cells (auditor's code; does not import w70_lib).
Input data only: the lane's A5 chain, colour and weak axes as W70 states them (0-indexed coordinates)."""
import itertools, json
from fractions import Fraction as F
from collections import Counter
import numpy as np

def v(*pairs):
    x = [F(0)] * 8
    for i, a in pairs: x[i] = F(a)
    return tuple(x)
dot = lambda a, b: sum(p * q for p, q in zip(a, b))
roots = set()
for i, j in itertools.combinations(range(8), 2):
    for a, b in itertools.product((-1, 1), repeat=2): roots.add(v((i, a), (j, b)))
for s in itertools.product((-1, 1), repeat=8):
    if s.count(-1) % 2 == 0: roots.add(tuple(F(x, 2) for x in s))
assert len(roots) == 240
chain = [v((6, 1), (7, -1)), v((5, 1), (6, -1)), v((6, 1), (7, 1)), tuple(F(-1, 2) for _ in range(8)), v((3, 1), (4, 1))]
colour = [v((0, 1), (1, -1)), v((1, 1), (2, -1))]
weak = v((3, 1), (4, -1))
# fundamental weight of A5 by the inverse Cartan matrix: omega_1 = (5 a1 + 4 a2 + 3 a3 + 2 a4 + a5)/6
w1 = tuple(sum(F(5 - k, 6) * chain[k][c] for k in range(5)) for c in range(8))
ws = [w1]
for c in chain: ws.append(tuple(a - b for a, b in zip(ws[-1], c)))
gram_ok = all(dot(ws[i], ws[j]) == (F(5, 6) if i == j else F(-1, 6)) for i in range(6) for j in range(6))
hQ = tuple(sum(sg * w[c] for sg, w in zip((1, -1, 1, -1, 1, -1), ws)) for c in range(8))
out = {"gram_ok": gram_ok, "h_Q": [str(x) for x in hQ], "h_Q_is_c0+c2+c4": hQ == tuple(a + b + c for a, b, c in zip(chain[0], chain[2], chain[4]))}
odd = sorted(r for r in roots if dot(r, hQ) % 2 == 1)
out["p_odd"] = len(odd)
out["p_odd_equals_weak_doublets"] = set(odd) == {r for r in roots if abs(dot(r, weak)) == 1}
# su(2)_Q: raising roots beta_r = ws_{2r} - ws_{2r+1} = chain[0], chain[2], chain[4]
beta = [tuple(a - b for a, b in zip(ws[2 * r], ws[2 * r + 1])) for r in range(3)]
out["beta_are_chain_0_2_4"] = beta == [chain[0], chain[2], chain[4]]
rootsQ = beta + [tuple(-x for x in b) for b in beta]
# SM: colour roots (all roots in span of colour simple roots), weak roots +-weak, and the six block-scalar Y
col_roots = [r for r in roots if all(r[k] == 0 for k in range(3, 8)) and sum(r[:3]) == 0]
Ys = [tuple(sum(c * w[k] for c, w in zip((y[0], y[0], y[1], y[1], y[2], y[2]), ws)) for k in range(8))
      for y in itertools.permutations((F(1, 6), F(-5, 6), F(2, 3)))]
def commutes(b):   # root vector E_b commutes with E_g iff b+g is not a root and b != -g (simply laced)
    return all(tuple(x + y for x, y in zip(b, g)) not in roots and tuple(-x for x in b) != g for g in col_roots + [weak, tuple(-x for x in weak)])
out["A1a_su2Q_roots_commute_with_colour_and_weak_roots"] = all(commutes(b) for b in rootsQ)
out["A1a_su2Q_roots_orthogonal_to_SM_Cartan"] = all(dot(b, c) == 0 for b in rootsQ for c in colour + [weak] + Ys)
out["A1a_hQ_orthogonal_to_SM_roots_and_Cartan"] = all(dot(hQ, g) == 0 for g in col_roots + [weak] + Ys)
out["A1b_odd_roots_in_su2Q"] = sum(1 for r in odd if r in rootsQ)
hq2 = dot(hQ, hQ)
out["A1c_coeff_distribution"] = dict(Counter(str(dot(r, hQ) / hq2) for r in odd))
# B1: SU(3)_B weight of each odd root = (r.H_b, r.H_a, r.H_ab), H_block = sum of the block's two weights, minus trace
def bw(r):
    raw = [dot(r, ws[2 * k]) + dot(r, ws[2 * k + 1]) for k in range(3)]
    t = sum(raw) / 3
    return tuple(x - t for x in raw)
SU3_roots = {(F(1), F(-1), F(0)), (F(1), F(0), F(-1)), (F(0), F(1), F(-1))}
SU3_roots |= {tuple(-x for x in r) for r in SU3_roots}
cls = Counter()
blockroot_set = set()
for r in odd:
    w = bw(r)
    if w in SU3_roots: cls["block root"] += 1; blockroot_set.add(r)
    elif w == (0, 0, 0): cls["block zero weight"] += 1
    elif sorted(w) in (sorted((F(2, 3), F(-1, 3), F(-1, 3))), sorted((F(-2, 3), F(1, 3), F(1, 3)))): cls["fundamental weight (3 or 3bar)"] += 1
    else: cls["other " + str(w)] += 1
out["B1_classes"] = dict(cls)
# B2 and the 24 = 24 read-out: Higgs-like = colour singlet, weak doublet, |Y| = 1/2, T3 + Y = 0
names = ["b", "a", "ab"]
hl_union = set(); b2_ok = True; b2 = {}
for y, Y in zip(itertools.permutations((F(1, 6), F(-5, 6), F(2, 3))), Ys):
    rows = [r for r in odd if dot(r, colour[0]) == 0 and dot(r, colour[1]) == 0 and abs(dot(r, Y)) == F(1, 2)
            and dot(r, weak) / 2 + dot(r, Y) == 0]
    hl_union |= set(rows)
    notm56 = sorted(n for n, yy in zip(names, y) if yy != F(-5, 6))
    pairs = []
    for r in rows:
        w = bw(r)
        if w not in SU3_roots: b2_ok = False; continue
        r_, s_ = names[w.index(F(1))], names[w.index(F(-1))]
        pairs.append(sorted([r_, s_]))
        b2_ok &= sorted([r_, s_]) == notm56
    b2[",".join(map(str, y))] = {"n": len(rows), "pairs": pairs, "not_-5/6": notm56}
out["B2_ok"] = b2_ok; out["B2"] = b2
out["higgs_like_union"] = len(hl_union)
out["higgs_like_union_equals_block_roots"] = hl_union == blockroot_set
out["n_block_roots"] = len(blockroot_set)

# read-out: Reading B's axis as B1644's a = e_unit; m = s2/s1 of Y(a) = aR^T + Ra^T - (a.R)1 on tau = iy
def R_np(t, K=60):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])
mtab = {}
for u, k in (("i", 0), ("j", 1), ("k", 2)):
    a = np.zeros(3); a[k] = 1
    vals = []
    for yy in (1, 2, 4, 8):
        R = R_np(1j * yy); Y = np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)
        s = np.linalg.svd(Y, compute_uv=False); vals.append(round(float(s[1] / s[0]), 6))
    mtab[u] = vals
out["readout_m_at_tau=iy_(y=1,2,4,8)"] = mtab
print(json.dumps(out, indent=1, default=str))
