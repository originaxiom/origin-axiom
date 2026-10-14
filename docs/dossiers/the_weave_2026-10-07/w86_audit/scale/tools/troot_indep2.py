"""Independent recomputation of T-ROOT's quantities from a thread table {word: [Vol, CS]}.
Differs from chat1's t_root.py in implementation: scipy logsumexp, brentq root-finding for thresholds,
exact integer binomials (math.comb) for the tail bound, explicit counting of syllable pairs, and a 40-digit
mpmath cross-check of the c = 6 headline numbers."""
import json, sys, math
from math import comb
import numpy as np
from scipy.special import logsumexp
from scipy.optimize import brentq
import mpmath as mp

T = json.load(open(sys.argv[1]))
words = sorted(T, key=lambda w: (len(w), w))
n_arr = np.array([len(w) for w in words], float)
vol = np.array([T[w][0] for w in words]); cs = np.array([T[w][1] for w in words])
Ln = {}
for w in words: Ln[len(w)] = Ln.get(len(w), 0) + 1
chiral = np.abs(cs) > 1e-6
iroot = words.index("LR")
V3 = float(mp.mpf(3) / 2 * mp.clsin(2, 2 * mp.pi / 3))
LOGW = {"A": -n_arr * math.log(2), "B": -n_arr * math.log(3),
        "C": -np.log(n_arr * (n_arr - 1) * np.array([Ln[len(w)] for w in words], float))}
def S(c, key):
    e = LOGW[key] - c * vol / (6 * math.pi)
    lZ = logsumexp(e)
    lp = e - lZ; p = np.exp(lp)
    return {"p": float(p[iroot]), "f": float(p[chiral].sum()), "Neff": float(np.exp(-(p * lp).sum())), "Z": float(np.exp(lZ))}
GRID = [0.5, 1, 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]
out = {"n": len(words), "L_of_n": Ln, "n_chiral": int(chiral.sum()), "n_amph": int((~chiral).sum())}
out["table"] = {k: {str(c): S(c, k) for c in GRID} for k in "ABC"}
def thr(level, key):
    f = lambda lc: S(math.exp(lc), key)["p"] - level
    lo, hi = math.log(1e-3), math.log(5000)
    if f(lo) >= 0: return ["p already >= level at c=1e-3", S(1e-3, key)["p"]]
    return math.exp(brentq(f, lo, hi, xtol=1e-14, rtol=1e-14))
out["thresholds"] = {k: {str(l): thr(l, k) for l in (0.5, 0.9, 0.99)} for k in "ABC"}
out["p_at_c0"] = {k: S(1e-12, k)["p"] for k in "ABC"}
# tail beyond length 18: number of Lyndon words of length n with k syllable pairs <= C(n-1, 2k-1)/k; Vol >= 2k v3
def tail(c, key, NT=600):
    x = math.exp(-c * 2 * V3 / (6 * math.pi))
    if key == "C": return x / 18
    beta = 2 if key == "A" else 3
    tot = 0.0
    for n in range(19, NT + 1):
        lb = -n * math.log(beta)
        terms = [math.log(comb(n - 1, 2 * k - 1)) - math.log(k) + k * math.log(x) + lb for k in range(1, n // 2 + 1)]
        m = max(terms); tot += math.exp(m) * sum(math.exp(t - m) for t in terms)
    y = math.sqrt(x); r = (1 + y) / beta
    return tot + (y / (1 + y)) * r ** (NT + 1) / (1 - r)
out["tails"] = {k: {str(c): tail(c, k) for c in (2, 6, 12, 24, 64, 128)} for k in "ABC"}
s6 = {k: S(6, k) for k in "ABC"}
out["p6_interval"] = {k: [s6[k]["p"] * s6[k]["Z"] / (s6[k]["Z"] + out["tails"][k]["6"]), s6[k]["p"]] for k in "ABC"}
eA = LOGW["A"] - 6 * vol / (6 * math.pi); pA = np.exp(eA - logsumexp(eA))
order = np.argsort(-pA, kind="stable")[:12]
out["top12_c6_A"] = [[words[i], float(pA[i]), float(vol[i]), float(cs[i])] for i in order]
Sn = {k: {n: float(np.exp(logsumexp((LOGW[k] - 6 * vol / (6 * math.pi))[n_arr == n]))) for n in range(2, 19)} for k in "ABC"}
out["S_n_c6"] = Sn
out["S_n_ratios"] = {k: [Sn[k][n + 1] / Sn[k][n] for n in range(2, 18)] for k in "ABC"}
wA = np.exp(eA)
out["footprint"] = {k: float(1 - (wA * np.cos(2 * math.pi * k * cs / math.pi ** 2)).sum() / wA.sum()) for k in range(1, 13)}
out["footprint_imag"] = {k: float((wA * np.sin(2 * math.pi * k * cs / math.pi ** 2)).sum() / wA.sum()) for k in (1, 2, 3)}
out["footprint_SL2_halfphase"] = {k: float(1 - (wA * np.cos(math.pi * k * cs / math.pi ** 2)).sum() / wA.sum()) for k in range(1, 7)}
out["min_abs_cs_chiral"] = float(np.abs(cs[chiral]).min()); out["max_abs_cs_amph"] = float(np.abs(cs[~chiral]).max())
cfine = np.exp(np.linspace(math.log(0.05), math.log(2000), 400))
out["Q1_fine_monotone"] = {k: bool(all(S(a, k)["p"] < S(b, k)["p"] for a, b in zip(cfine[:-1], cfine[1:]))) for k in "ABC"}
out["chiral_share_asymptotic_check"] = {str(c): [out["table"]["A"][str(c)]["f"], math.exp(-0.0338 * c)] for c in (24, 64, 128, 256)}
# 40-digit cross-check at c = 6
mp.mp.dps = 40
def mpS(key):
    lw = {"A": lambda n: -n * mp.log(2), "B": lambda n: -n * mp.log(3), "C": lambda n: -mp.log(n * (n - 1) * Ln[n])}[key]
    e = [lw(len(w)) - 6 * mp.mpf(T[w][0]) / (6 * mp.pi) for w in words]
    m = max(e); q = [mp.e ** (x - m) for x in e]; Z = mp.fsum(q)
    p = [x / Z for x in q]
    return {"p": float(p[iroot]), "f": float(mp.fsum(p[i] for i in range(len(words)) if chiral[i])),
            "Neff": float(mp.e ** (-mp.fsum(x * mp.log(x) for x in p if x > 0)))}
out["mp40_c6"] = {k: mpS(k) for k in "ABC"}
json.dump(out, open(sys.argv[2], "w"), indent=1, default=str)
print(json.dumps({k: out[k] for k in ("n", "n_chiral", "n_amph", "thresholds", "p_at_c0", "tails", "p6_interval", "footprint", "footprint_imag", "footprint_SL2_halfphase", "min_abs_cs_chiral", "max_abs_cs_amph", "Q1_fine_monotone", "mp40_c6", "chiral_share_asymptotic_check")}, indent=1, default=str))
