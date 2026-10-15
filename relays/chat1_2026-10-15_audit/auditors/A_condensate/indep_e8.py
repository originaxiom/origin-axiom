"""Independent re-derivation (auditor's own code; does NOT import w70_lib) of the E8 facts behind
chat1's condensate_in_M negatives. Exact rationals throughout.  Lane coordinates, 0-indexed."""
import itertools, json
from fractions import Fraction as F
from collections import Counter

def dot(a, b): return sum(x * y for x, y in zip(a, b))
def add(a, b, s=1): return tuple(x + s * y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
def e(*idx_val):
    v = [F(0)] * 8
    for i, x in idx_val: v[i] = F(x)
    return tuple(v)

# --- E8 roots: D8 roots + half-integer vectors with an even number of minus signs (the chain's -1/2(1..1) is in this set)
ROOTS = set()
for i, j in itertools.combinations(range(8), 2):
    for s, t in itertools.product((1, -1), repeat=2):
        ROOTS.add(e((i, s), (j, t)))
for sg in itertools.product((1, -1), repeat=8):
    if sg.count(-1) % 2 == 0:
        ROOTS.add(tuple(F(s, 2) for s in sg))
assert len(ROOTS) == 240 and all(dot(r, r) == 2 for r in ROOTS)

CHAIN = [e((6, 1), (7, -1)), e((5, 1), (6, -1)), e((6, 1), (7, 1)), tuple(F(-1, 2) for _ in range(8)), e((3, 1), (4, 1))]
COL = [e((0, 1), (1, -1)), e((1, 1), (2, -1))]
WEAK = e((3, 1), (4, -1))
out = {}
gram = [[dot(a, b) for b in CHAIN] for a in CHAIN]
out["A5_cartan_ok"] = all(gram[i][j] == (2 if i == j else (-1 if abs(i - j) == 1 else 0)) for i in range(5) for j in range(5))
out["chain_perp_colour_weak"] = all(dot(c, x) == 0 for c in CHAIN for x in COL + [WEAK])

# --- weights of the 6, derived independently: omega_1 in span(CHAIN) with omega_1.c_k = delta_k0 (solve 5x5 Gram exactly)
import sympy as sp
G = sp.Matrix(5, 5, lambda i, j: sp.Rational(gram[i][j].numerator, gram[i][j].denominator))
coef = G.inv() * sp.Matrix([1, 0, 0, 0, 0])
w1 = tuple(sum(F(int(sp.fraction(coef[k])[0]), int(sp.fraction(coef[k])[1])) * CHAIN[k][m] for k in range(5)) for m in range(8))
WS = [w1]
for c in CHAIN: WS.append(add(WS[-1], c, -1))
out["six_weight_gram_ok"] = all(dot(WS[i], WS[j]) == (F(5, 6) if i == j else F(-1, 6)) for i in range(6) for j in range(6))
out["sum_ws_zero"] = all(x == 0 for x in [sum(w[k] for w in WS) for k in range(8)])

# --- the puncture's Cartan h_Q and the lane's integer coweight h = a1+2a2+3a3+4a4+5a5
HQ = tuple(sum(s * w[k] for s, w in zip((1, -1, 1, -1, 1, -1), WS)) for k in range(8))
h_lane = tuple(sum(m * c[k] for m, c in zip((1, 2, 3, 4, 5), CHAIN)) for k in range(8))
out["h_lane"] = [str(x) for x in h_lane]
out["hQ_eigen_on_6"] = [str(dot(HQ, w)) for w in WS]
out["hQ.hQ"] = str(dot(HQ, HQ))
out["alpha.hQ_integer_all_roots"] = all(dot(r, HQ).denominator == 1 for r in ROOTS)
out["parity_hQ_equals_parity_h_lane"] = all((dot(r, HQ) - dot(r, h_lane)) % 2 == 0 for r in ROOTS)
out["parity_hQ_equals_weak_centre"] = all((dot(r, HQ) - dot(r, WEAK)) % 2 == 0 for r in ROOTS)
ODD = sorted(r for r in ROOTS if dot(r, HQ) % 2 != 0)
out["n_p_odd"] = len(ODD)
out["p_odd_equals_weak_doublets"] = set(ODD) == {r for r in ROOTS if abs(dot(r, WEAK)) == 1}

# --- su(2)_Q (Reading A): beta_r = ws_{2r} - ws_{2r+1}; h_Q = sum beta_r
BETA = [add(WS[2 * r], WS[2 * r + 1], -1) for r in range(3)]
out["beta_are_roots"] = all(b in ROOTS for b in BETA)
out["sum_beta_equals_hQ"] = tuple(sum(b[k] for b in BETA) for k in range(8)) == HQ
out["beta.hQ"] = [str(dot(b, HQ)) for b in BETA]
out["beta_mutually_orthogonal"] = all(dot(BETA[i], BETA[j]) == 0 for i in range(3) for j in range(3) if i != j)
out["beta_colour_weak_orthogonal"] = all(dot(b, x) == 0 for b in BETA for x in COL + [WEAK]) and all(dot(HQ, x) == 0 for x in COL + [WEAK])
QROOTS = BETA + [neg(b) for b in BETA]
out["A1b_p_odd_roots_in_su2Q_roots"] = sum(1 for r in ODD if r in QROOTS)
out["A1c_alpha.hQ_distribution"] = dict(Counter(str(dot(r, HQ)) for r in ODD))

# --- block-scalar Y: Y = sum c_k ws_k with c = (y0,y0,y1,y1,y2,y2). beta_r.Y = c_2r - c_2r+1 = 0 for EVERY block-scalar Y
def ycart(y):
    c = (y[0], y[0], y[1], y[1], y[2], y[2]); return tuple(sum(ci * w[k] for ci, w in zip(c, WS)) for k in range(8))
sym = sp.symbols("y0 y1 y2")
# symbolic check that beta_r . Y == 0 identically
def ycart_sym():
    c = (sym[0], sym[0], sym[1], sym[1], sym[2], sym[2])
    return [sum(ci * sp.Rational(w[k].numerator, w[k].denominator) for ci, w in zip(c, WS)) for k in range(8)]
Ys = ycart_sym()
out["beta.Y_identically_zero_for_any_block_scalar_Y"] = all(sp.simplify(sum(sp.Rational(b[k].numerator, b[k].denominator) * Ys[k] for k in range(8))) == 0 for b in BETA)

# --- independent admissible-Y search on finer grids (W70 used k/6, |k|<=12)
THREE = {(1, 0), (-1, 1), (0, -1)}; THREEBAR = {(0, 1), (1, -1), (-1, 0)}
def colour(r): return (dot(r, COL[0]), dot(r, COL[1]))
def sm_ok(y):
    Y = ycart(y); need = {"Q": 0, "uc": 0, "dc": 0, "L": 0, "ec": 0}
    for r in ROOTS:
        yr, c, w = dot(r, Y), colour(r), abs(dot(r, WEAK))
        if c in THREE and w == 1 and yr == F(1, 6): need["Q"] = 1
        if c in THREEBAR and w == 0 and yr == F(-2, 3): need["uc"] = 1
        if c in THREEBAR and w == 0 and yr == F(1, 3): need["dc"] = 1
        if c == (0, 0) and w == 1 and yr == F(-1, 2): need["L"] = 1
        if c == (0, 0) and w == 0 and yr == 1: need["ec"] = 1
    return all(need.values())
grids = {}
for den, K in ((6, 12), (12, 24)):
    sols = []
    for a in range(-K, K + 1):
        for b in range(-K, K + 1):
            if abs(a + b) <= K:
                y = (F(a, den), F(b, den), F(-a - b, den))
                if sm_ok(y): sols.append(y)
    grids[f"k/{den},|k|<={K}"] = sorted({tuple(str(x) for x in s) for s in sols})
out["admissible_Y_by_grid"] = grids
ADM = [tuple(F(x) for x in s) for s in grids["k/6,|k|<=12"]]
target = {p for p in itertools.permutations((F(1, 6), F(-5, 6), F(2, 3)))}
out["admissible_are_perms_of_(1/6,-5/6,2/3)"] = set(ADM) == target and len(ADM) == 6

# --- SU(6) content and Reading-B block classes of the 112
BLOCK = {0: "b", 1: "b", 2: "a", 3: "a", 4: "ab", 5: "ab"}
def su6(r):
    v = [dot(r, w) for w in WS]
    if sorted(v) == sorted([F(5, 6)] + [F(-1, 6)] * 5): return "6", (v.index(F(5, 6)),)
    if sorted(v) == sorted([F(-5, 6)] + [F(1, 6)] * 5): return "6bar", (v.index(F(-5, 6)),)
    if all(x in (F(1, 2), F(-1, 2)) for x in v) and v.count(F(1, 2)) == 3: return "20", tuple(j for j in range(6) if v[j] == F(1, 2))
    return "other", tuple(v)
cls = Counter(); blockroot = set(); blockcartan = set()
for r in ODD:
    k, S = su6(r)
    if k in ("6", "6bar"): cls[k] += 1
    elif k == "20":
        c = Counter(BLOCK[j] for j in S)
        if max(c.values()) == 2: cls["20:block-root"] += 1; blockroot.add(r)
        else: cls["20:one-per-block"] += 1; blockcartan.add(r)
    else: cls["other"] += 1
out["B1_classes"] = dict(cls)

# --- Higgs-like neutral roots per admissible Y (colour singlet, p-odd, |Y| = 1/2, T3 + Y = 0)
def higgs_like(y):
    Y = ycart(y); rows = []
    for r in ODD:
        if colour(r) != (0, 0): continue
        t3, yr = dot(r, WEAK) / 2, dot(r, Y)
        if abs(yr) == F(1, 2) and t3 + yr == 0: rows.append(r)
    return rows
HL = {y: higgs_like(y) for y in ADM}
out["higgs_like_counts"] = {",".join(map(str, y)): len(v) for y, v in HL.items()}
union = set().union(*HL.values())
out["union_size"] = len(union)
out["union_equals_block_roots_SET"] = union == blockroot
# each Y's four = two +- pairs?
out["each_Y_four_are_two_pm_pairs"] = all(all(neg(r) in v for r in v) for v in HL.values())
# B2 check: block root of each Higgs-like root is +-(e_r - e_s) with {r,s} the blocks whose Y != -5/6
NAMES = ["b", "a", "ab"]
ok = True
for y, v in HL.items():
    lab = dict(zip(NAMES, y)); pair = sorted(n for n in NAMES if lab[n] != F(-5, 6))
    for r in v:
        k, S = su6(r); c = Counter(BLOCK[j] for j in S)
        two = [n for n in NAMES if c.get(n, 0) == 2]; zero = [n for n in NAMES if c.get(n, 0) == 0]
        ok &= (len(two) == 1 and len(zero) == 1 and sorted(two + zero) == pair)
out["B2_independent"] = bool(ok)

# --- the pair test the folder did not run: pairs of Higgs-like roots whose SUM is a root of su(2)_Q
pairs = {}
for y, v in HL.items():
    Y = ycart(y); rows = []
    for a, b in itertools.combinations(v, 2):
        s = add(a, b)
        if s in QROOTS:
            rows.append({"alpha": [str(x) for x in a], "beta": [str(x) for x in b], "Y": [str(dot(a, Y)), str(dot(b, Y))],
                         "T3": [str(dot(a, WEAK) / 2), str(dot(b, WEAK) / 2)], "sum_is": "beta_%d" % QROOTS.index(s) if QROOTS.index(s) < 3 else "-beta_%d" % (QROOTS.index(s) - 3),
                         "sum.hQ": str(dot(s, HQ))})
    pairs[",".join(map(str, y))] = rows
out["higgs_like_pairs_summing_to_su2Q_root"] = pairs
# all p-odd pairs (any colour) summing to an su(2)_Q root
allp = Counter()
for a, b in itertools.combinations(ODD, 2):
    s = add(a, b)
    if s in QROOTS: allp["colour-singlet" if colour(a) == (0, 0) and colour(b) == (0, 0) else "coloured"] += 1
out["all_p_odd_pairs_summing_to_su2Q_root"] = dict(allp)
# single-root weight argument: k*alpha in {0, +-beta_r} only for k = 0
out["single_root_multiples_hit_su2Q_root"] = any(tuple(kk * x for x in r) in QROOTS for r in ODD for kk in range(-4, 5) if kk != 0)

# the lane's alpha = e3 + e5
ALPHA = e((3, 1), (5, 1))
out["lane_alpha_in_union"] = ALPHA in union
out["lane_alpha_hQ"] = str(dot(ALPHA, HQ))

print(json.dumps(out, indent=1, default=str))
json.dump(out, open("indep_e8.json", "w"), indent=1, default=str)
