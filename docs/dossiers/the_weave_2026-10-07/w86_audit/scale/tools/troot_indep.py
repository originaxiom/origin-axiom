"""Independent recomputation of T-ROOT's quantities from the committed thread table (Vol, CS per Lyndon word), with
mpmath at 40 digits: root share, chiral share, N_eff on the grid; thresholds by root-finding; tail bounds by direct
evaluation (exact binomials, mpmath); footprint; top 10 at c = 6 (A); per-length sum ratios. Writes JSON to argv[2]."""
import json, sys, math
import mpmath as mp
mp.mp.dps = 40
T = json.load(open(sys.argv[1]))
words = sorted(T, key=lambda w: (len(w), w))
vol = {w: mp.mpf(T[w][0]) for w in words}; cs = {w: T[w][1] for w in words}
Ln = {}
for w in words: Ln[len(w)] = Ln.get(len(w), 0) + 1
V3 = mp.mpf(3) / 2 * mp.clsin(2, 2 * mp.pi / 3); V8 = 4 * mp.catalan
def logw(key, w):
    n = len(w)
    return {"A": -n * mp.log(2), "B": -n * mp.log(3), "C": -mp.log(n * (n - 1) * Ln[n])}[key]
LW = {key: {w: logw(key, w) for w in words} for key in "ABC"}
chiral = {w: abs(cs[w]) > 1e-6 for w in words}
def stats(c, key):
    c = mp.mpf(c)
    e = {w: LW[key][w] - c * vol[w] / (6 * mp.pi) for w in words}
    m = max(e.values())
    q = {w: mp.e ** (e[w] - m) for w in words}
    Z = mp.fsum(q.values())
    p = {w: q[w] / Z for w in words}
    H = -mp.fsum(p[w] * mp.log(p[w]) for w in words if p[w] > 0)
    return {"p": p["LR"], "f": mp.fsum(p[w] for w in words if chiral[w]), "Neff": mp.e ** H, "Z": Z * mp.e ** m, "_p": p}
GRID = [0.5, 1, 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]
out = {"n": len(words), "L_of_n": Ln, "n_chiral": sum(chiral.values()), "n_amph": len(words) - sum(chiral.values())}
tab = {}
for key in "ABC":
    tab[key] = {}
    for c in GRID:
        s = stats(c, key)
        tab[key][str(c)] = {k: float(v) for k, v in s.items() if k != "_p"}
out["table"] = tab
def thr(level, key):
    f = lambda c: stats(c, key)["p"] - level
    lo, hi = mp.mpf("1e-3"), mp.mpf(5000)
    if f(lo) >= 0: return ("already", float(stats(lo, key)["p"]))
    for _ in range(60):
        mid = mp.sqrt(lo * hi)
        if f(mid) >= 0: hi = mid
        else: lo = mid
    return float(hi)
out["thresholds"] = {key: {str(l): thr(l, key) for l in (0.5, 0.9, 0.99)} for key in "ABC"}
# tail bounds, independent: exact binomials, k syllable pairs, n from 19 to NMAX_T, plus geometric remainder
def tail(c, key, NT=1500):
    x = mp.e ** (-mp.mpf(c) * 2 * V3 / (6 * mp.pi))
    if key == "C": return float(x / 18)
    beta = 2 if key == "A" else 3
    s = mp.mpf(0)
    for n in range(19, NT + 1):
        s += mp.fsum(mp.binomial(n - 1, 2 * k - 1) / k * x ** k for k in range(1, n // 2 + 1)) / mp.mpf(beta) ** n
    y = mp.sqrt(x); r = (1 + y) / beta
    rem = (y / (1 + y)) * r ** (NT + 1) / (1 - r)
    return float(s + rem)
out["tails"] = {key: {str(c): tail(c, key) for c in (2, 6, 12, 24, 64, 128)} for key in "ABC"}
s6 = {key: stats(6, key) for key in "ABC"}
out["p6_interval"] = {key: [float(s6[key]["p"] * s6[key]["Z"] / (s6[key]["Z"] + out["tails"][key]["6"])), float(s6[key]["p"])] for key in "ABC"}
pA = s6["A"]["_p"]
out["top12_c6_A"] = [[w, float(pA[w]), float(vol[w]), cs[w]] for w in sorted(words, key=lambda w: -pA[w])[:12]]
# per-length sums at c = 6 and their successive ratios
Sn = {}
for key in "ABC":
    Sn[key] = {n: float(mp.fsum(mp.e ** (LW[key][w] - 6 * vol[w] / (6 * mp.pi)) for w in words if len(w) == n)) for n in range(2, 19)}
out["S_n_c6"] = Sn
out["S_n_ratios"] = {key: [Sn[key][n + 1] / Sn[key][n] for n in range(2, 18)] for key in "AB"}
# footprint 1 - Re Z(k)/Z(0) at c = 6 under (A), phase exp(2 pi i k CS / pi^2)
wA = {w: mp.e ** (LW["A"][w] - 6 * vol[w] / (6 * mp.pi)) for w in words}
Z0 = mp.fsum(wA.values())
out["footprint"] = {k: float(1 - mp.fsum(wA[w] * mp.cos(2 * mp.pi * k * cs[w] / mp.pi ** 2) for w in words) / Z0) for k in range(1, 13)}
# imaginary part (mirror pairs make it vanish)
out["footprint_imag"] = {k: float(mp.fsum(wA[w] * mp.sin(2 * mp.pi * k * cs[w] / mp.pi ** 2) for w in words) / Z0) for k in (1, 2, 3)}
# smallest |CS| among chiral threads, largest among CS~0
out["min_abs_cs_chiral"] = min(abs(cs[w]) for w in words if chiral[w])
out["max_abs_cs_amph"] = max(abs(cs[w]) for w in words if not chiral[w])
# Q1 monotonicity on a fine grid
out["Q1_fine"] = {key: all(stats(c1, key)["p"] < stats(c2, key)["p"] for c1, c2 in zip([0.5 * 1.5 ** i for i in range(16)], [0.5 * 1.5 ** (i + 1) for i in range(16)])) for key in "ABC"}
json.dump(out, open(sys.argv[2], "w"), indent=1, default=str)
print(json.dumps({k: out[k] for k in ("n", "n_chiral", "n_amph", "thresholds", "tails", "p6_interval", "footprint", "footprint_imag", "min_abs_cs_chiral", "max_abs_cs_amph", "Q1_fine")}, indent=1, default=str))
