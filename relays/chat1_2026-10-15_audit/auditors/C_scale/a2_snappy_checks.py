"""Audit A2 (independent SnapPy checks; run from scratch, writes nothing into the repo).
 (1) spot-check 400 saved (Vol, CS) values from t_root_threads.json;
 (2) swap-symmetric enumeration to 18, CS = 0 on all of them, no chiral thread at 0 or pi^2/2 (from the data);
 (3) T-SIGN N1 extended: minus bundles of every swap-symmetric word to length 16;
     N2 extended: every Lyndon word to length 12 (plus a random sample of length 13-16);
 (4) triangulation independence of the bit (randomize / canonize, several retriangulations);
 (5) the double-cover relation CS(b++WW) = 2 CS(b++W) = 2 CS(b+-W) mod pi^2;
 (6) reversal: b++rev(W) has W's Vol and CS (B1456), and mirror: b++swap(W) has -CS.
"""
import json, math, random, sys, warnings
warnings.filterwarnings("ignore")
import snappy

PI2 = math.pi ** 2
DATA = sys.argv[1]
d = json.load(open(DATA))
random.seed(20261015)

def red(x):
    y = math.fmod(x, PI2)
    if y > PI2 / 2: y -= PI2
    if y <= -PI2 / 2: y += PI2
    return y
def lr(w): return min(w[i:] + w[:i] for i in range(len(w)))
def swap(w): return w.translate(str.maketrans("LR", "RL"))
def is_lyndon(w): return all(w < w[i:] + w[:i] for i in range(1, len(w)))
def lyndon_upto(N):
    out = []
    def gen(n):   # Duval
        w = [-1]
        while w:
            w[-1] += 1
            m = len(w)
            if m >= 2: out.append("".join("LR"[i] for i in w))
            while len(w) < n: w.append(w[len(w) - m])
            while w and w[-1] == 1: w.pop()
    gen(N)
    return out
def meas(name, retri=0):
    M = snappy.Manifold(name)
    for _ in range(retri): M.randomize()
    cv = complex(M.complex_volume())
    return cv.real, red(cv.imag), M.solution_type()
def sym(w): return lr(swap(w)) in (w, lr(w[::-1]))

res = {}
# (1)
words = list(d)
byn = {}
for w in words: byn.setdefault(len(w), []).append(w)
sample = []
for n_, ws in byn.items(): sample += random.sample(ws, min(len(ws), 25))
bad = []
for w in sample:
    v, c, s = meas("b++" + w)
    if abs(v - d[w][0]) > 1e-9 or abs(red(c - d[w][1])) > 1e-6: bad.append([w, v, d[w][0], c, d[w][1]])
res["1_spotcheck"] = {"n": len(sample), "mismatches": bad}
print("(1)", res["1_spotcheck"], flush=True)

# (2)
L18 = lyndon_upto(18)
assert sorted(L18) == sorted(words)
S18 = [w for w in L18 if sym(w)]
cnt = {N: sum(1 for w in S18 if len(w) <= N) for N in (12, 14, 16, 18)}
s_cs_nonzero = [w for w in S18 if abs(d[w][1]) > 1e-6]
ch_at_bits = [w for w in L18 if not sym(w) and (abs(d[w][1]) < 1e-6 or abs(abs(d[w][1]) - PI2 / 2) < 1e-6)]
mins = sorted(abs(d[w][1]) for w in L18 if not sym(w))[:3]
minq = sorted(abs(abs(d[w][1]) - PI2 / 2) for w in L18 if not sym(w))[:3]
res["2_census"] = {"swap_sym_counts": cnt, "sym_with_CS_nonzero": s_cs_nonzero[:5],
                   "chiral_at_0_or_half": ch_at_bits[:5], "chiral_min_|CS|": mins, "chiral_min_dist_to_pi2/2": minq}
print("(2)", res["2_census"], flush=True)

# (3) N1 to 16, N2 to 12 + sample
n1_bad, n1_geo = [], []
for w in [w for w in S18 if len(w) <= 16]:
    v, c, s = meas("b+-" + w)
    if abs(abs(c) - PI2 / 2) > 1e-6: n1_bad.append([w, c])
    if s != "all tetrahedra positively oriented": n1_geo.append([w, s])
res["3_N1_to16"] = {"n": sum(1 for w in S18 if len(w) <= 16), "violations": n1_bad[:10], "non_geometric": n1_geo[:10]}
print("(3a)", res["3_N1_to16"], flush=True)
n2_words = [w for w in L18 if len(w) <= 12] + random.sample([w for w in L18 if 13 <= len(w) <= 16], 300)
n2_bad, n2_vol = [], []
for w in n2_words:
    vm, cm, sm = meas("b+-" + w)
    vp, cp = d[w][0], d[w][1]
    if abs(abs(red(cm - cp)) - PI2 / 2) > 1e-6: n2_bad.append([w, cp, cm])
    if abs(vm - vp) > 1e-8: n2_vol.append([w, vp, vm])
res["3_N2"] = {"n": len(n2_words), "violations": n2_bad[:10], "vol_mismatch": n2_vol[:10]}
print("(3b)", res["3_N2"], flush=True)

# (4) triangulation independence of the bit
tri = []
for w in ["LR", "LLRR", "LLRLRR", "LLLRRR", "LLRRLR", "LLR", "LLLLRRRLR"]:
    for sign in ("b++", "b+-"):
        vals = []
        for k in range(6):
            M = snappy.Manifold(sign + w)
            for _ in range(k * 3): M.randomize()
            if k == 5:
                try: M.canonize()
                except Exception: pass
            vals.append(round(red(complex(M.complex_volume()).imag), 9))
        tri.append([sign + w, sorted(set(vals))])
res["4_retriangulation"] = tri
for r in tri: print("(4)", r, flush=True)

# (5) double covers: M_{W^2} covers M_W and M_{-W} with degree 2
cov = []
for w in ["LR", "LLR", "LLRR", "LLLR", "LLRLR", "LLRLRR", "LLLRR"]:
    cWW = meas("b++" + w + w)[1]
    cp, cm = meas("b++" + w)[1], meas("b+-" + w)[1]
    cov.append([w, round(cWW, 9), round(red(2 * cp), 9), round(red(2 * cm), 9)])
res["5_double_cover"] = cov
for r in cov: print("(5) W, CS(WW), 2CS(+W), 2CS(-W):", r, flush=True)

# (6) reversal and mirror
rv, mi = [], []
for w in random.sample([w for w in L18 if 4 <= len(w) <= 14], 60):
    v, c, _ = meas("b++" + lr(w[::-1]))
    if abs(v - d[w][0]) > 1e-9 or abs(red(c - d[w][1])) > 1e-6: rv.append([w, c, d[w][1]])
    v2, c2, _ = meas("b++" + lr(swap(w)))
    if abs(v2 - d[w][0]) > 1e-9 or abs(red(c2 + d[w][1])) > 1e-6: mi.append([w, c2, d[w][1]])
res["6_reversal_same_mirror_opposite"] = {"reversal_bad": rv, "mirror_bad": mi}
print("(6)", res["6_reversal_same_mirror_opposite"], flush=True)
json.dump(res, open(sys.argv[2], "w"), indent=1, default=str)
