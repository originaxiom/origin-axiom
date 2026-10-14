"""T-ROOT (T_ROOT_PREREGISTRATION.md, sealed at 13d31f042, sha256 3fd25436...).

The action-weighted weave: threads = Lyndon words in L < R of length 2..18 (31,040), bundle 'b++' + word (SnapPy 3.3.2),
action factor exp(-c Vol / 6 pi), word weights (A) 2^-n, (B) 3^-n, (C) 1/(n(n-1) L(n)). Root share, chiral share,
N_eff, thresholds, per-length sums, Gueritaud-Futer tail bounds; the level's footprint as a read-out.
"""
import json, math, pathlib, sys, time, warnings
from math import lgamma
warnings.filterwarnings("ignore")
import numpy as np
import mpmath as mp
import snappy

HERE = pathlib.Path(__file__).resolve().parent
PI2 = math.pi ** 2
V3 = float(mp.mpf(3) / 2 * mp.clsin(2, 2 * mp.pi / 3))
V8 = float(4 * mp.catalan)
NMAX = 18
GRID = [0.5, 1, 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]
t0 = time.time()


def red(x):
    y = math.fmod(x, PI2)
    if y > PI2 / 2: y -= PI2
    if y <= -PI2 / 2: y += PI2
    return y


def lyndon(n, alphabet="LR"):                     # Duval: all Lyndon words of length <= n
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1
        m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n:
            w.append(w[len(w) - m])
        while w and w[-1] == k - 1:
            w.pop()


def n_R_syllables(w):
    return sum(1 for i in range(len(w)) if w[i] == "R" and w[i - 1] == "L")


words = [w for w in lyndon(NMAX) if len(w) >= 2]
words.sort(key=lambda w: (len(w), w))
L_of_n = {}
for w in words:
    L_of_n[len(w)] = L_of_n.get(len(w), 0) + 1

vols, css, sols, fails = {}, {}, {}, []
for i, w in enumerate(words):
    try:
        M = snappy.Manifold("b++" + w)
        vols[w] = float(M.volume())
        css[w] = red(complex(M.complex_volume()).imag)
        sols[w] = M.solution_type()
    except Exception as e:
        fails.append([w, repr(e)])
    if i % 3000 == 0:
        print(f"  measured {i}/{len(words)}  t={time.time() - t0:.0f}s", file=sys.stderr, flush=True)
good = [w for w in words if w in vols]
out = {"snappy": snappy.__version__, "n_threads": len(words), "L_of_n": L_of_n, "failures": fails,
       "seconds_measuring": round(time.time() - t0, 1)}

# ---------------------------------------------------------------- Q0
prev = json.loads((HERE / "the_scale_check.json").read_text())["threads"]
q0_bad = []
for w, (v, c, s) in prev.items():
    if w not in vols or abs(vols[w] - v) > 1e-9 or abs(red(css[w] - c)) > 1e-6:
        q0_bad.append([w, v, vols.get(w), c, css.get(w)])
geo_bad = [w for w in good if sols[w] != "all tetrahedra positively oriented"]
gf_bad = [w for w in good if not (2 * n_R_syllables(w) * V3 - 1e-9 <= vols[w] < 2 * n_R_syllables(w) * V8)]
out["Q0"] = {"reproduced_745": len(prev) - len(q0_bad), "mismatches": q0_bad[:20], "non_geometric": geo_bad[:20],
             "n_non_geometric": len(geo_bad), "gf_violations": gf_bad[:20], "n_gf_violations": len(gf_bad),
             "holds": bool(len(words) == 31040 and not fails and not q0_bad and not geo_bad and not gf_bad)}

# ---------------------------------------------------------------- arrays and weights
n_arr = np.array([len(w) for w in good], dtype=float)
vol = np.array([vols[w] for w in good])
cs = np.array([css[w] for w in good])
chiral = np.abs(cs) > 1e-6
iroot = good.index("LR")
logw = {"A": -n_arr * math.log(2), "B": -n_arr * math.log(3),
        "C": np.array([-math.log(len(w) * (len(w) - 1) * L_of_n[len(w)]) for w in good])}


def dist(c, key):
    e = logw[key] - c * vol / (6 * math.pi)
    m = e.max()
    q = np.exp(e - m)
    Z = q.sum()
    return q / Z, math.exp(m) * Z            # normalised distribution, Z itself


def stats(c, key):
    q, Z = dist(c, key)
    nz = q[q > 0]
    return {"p_root": float(q[iroot]), "f_chiral": float(q[chiral].sum()), "N_eff": float(math.exp(-(nz * np.log(nz)).sum())),
            "Z": Z}


table = {key: {str(c): stats(c, key) for c in GRID} for key in ("A", "B", "C")}
out["table"] = table

# Q1: p increasing along the grid
q1 = {key: all(table[key][str(GRID[i + 1])]["p_root"] > table[key][str(GRID[i])]["p_root"] for i in range(len(GRID) - 1))
      for key in table}
out["Q1"] = {"increasing": q1, "holds": bool(all(q1.values()))}


# thresholds by bisection (p is monotone)
def threshold(level, key, lo=1e-3, hi=5000.0):
    plo, phi = stats(lo, key)["p_root"], stats(hi, key)["p_root"]
    if plo >= level:
        return {"c": None, "note": f"p already {plo:.4f} >= {level} at c = {lo}"}
    if phi < level:
        return {"c": None, "note": f"p only {phi:.4f} < {level} at c = {hi}"}
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if stats(mid, key)["p_root"] >= level: hi = mid
        else: lo = mid
    return {"c": hi}


thr = {key: {str(lv): threshold(lv, key) for lv in (0.5, 0.9, 0.99)} for key in ("A", "B", "C")}
out["thresholds"] = thr


# ---------------------------------------------------------------- tail bounds beyond length 18
def tail_bound(c, key, nmax=4000):
    x = math.exp(-c * 2 * V3 / (6 * math.pi))
    if key == "C":
        return (1.0 / NMAX) * x
    beta = 2.0 if key == "A" else 3.0
    logs = []
    for n in range(NMAX + 1, nmax + 1):
        ks = np.arange(1, n // 2 + 1)
        lt = (-n * math.log(beta) + lgamma(n) - np.array([lgamma(2 * k) + lgamma(n - 2 * k + 1) for k in ks])
              - np.log(ks) + ks * math.log(x))
        mx = lt.max()
        logs.append(mx + math.log(np.exp(lt - mx).sum()))
    logs = np.array(logs); mx = logs.max()
    s = math.exp(mx) * np.exp(logs - mx).sum()
    y = math.sqrt(x); r = (1 + y) / beta                      # geometric remainder for n > nmax (drops the 1/k)
    rem = (y / (1 + y)) * r ** (nmax + 1) / (1 - r) if r < 1 else float("inf")
    return s + rem


tails = {key: {str(c): tail_bound(c, key) for c in (2, 6, 12, 24, 64, 128)} for key in ("A", "B", "C")}
out["tails"] = tails
p6 = {key: table[key]["6"]["p_root"] for key in ("A", "B", "C")}
Z6 = {key: table[key]["6"]["Z"] for key in ("A", "B", "C")}
out["p_root_6_interval_with_tail"] = {key: [p6[key] * Z6[key] / (Z6[key] + tails[key]["6"]), p6[key]] for key in p6}

# ---------------------------------------------------------------- cells
th = thr
c99 = {key: th[key]["0.99"]["c"] for key in th}
out["cells"] = {
    "Q0": out["Q0"]["holds"],
    "Q1": out["Q1"]["holds"],
    "T1": bool(0.15 <= p6["A"] <= 0.40),
    "T2": bool(0.35 <= p6["B"] <= 0.65),
    "T3": bool(0.50 <= p6["C"] <= 0.80),
    "T4": bool(table["A"]["6"]["f_chiral"] > 0.5),
    "T5": bool(table["A"]["6"]["N_eff"] >= 5),
    "T6": bool(all(v is not None and 80 <= v <= 250 for v in c99.values())),
    "T7": bool(th["A"]["0.5"]["c"] is not None and 10 <= th["A"]["0.5"]["c"] <= 40),
    "T8": bool(tails["B"]["6"] < 0.01 * Z6["B"]),
}

# ---------------------------------------------------------------- read-outs
qA, ZA = dist(6, "A")
order = np.argsort(-qA)[:10]
S_n = {}
for key in ("A", "B", "C"):
    q, Z = dist(6, key)
    S_n[key] = {int(n): float(Z * q[n_arr == n].sum()) for n in range(2, NMAX + 1)}
foot = {}
for k in range(1, 13):
    e = logw["A"] - 6 * vol / (6 * math.pi)
    wts = np.exp(e)
    foot[k] = float(1 - (wts * np.cos(2 * math.pi * k * cs / PI2)).sum() / wts.sum())
out["readouts"] = {
    "top10_c6_A": [[good[i], float(qA[i]), vols[good[i]], css[good[i]]] for i in order],
    "S_n_c6": S_n,
    "chiral_share_c6": {key: table[key]["6"]["f_chiral"] for key in table},
    "N_eff_c6": {key: table[key]["6"]["N_eff"] for key in table},
    "level_footprint_c6_A_[1-ReZk/Z0]": foot,
    "n_chiral": int(chiral.sum()), "n_amphichiral": int((~chiral).sum()),
    "seconds_total": round(time.time() - t0, 1),
}
(HERE / "t_root.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
(HERE / "t_root_threads.json").write_text(json.dumps({w: [vols[w], css[w]] for w in good}) + "\n")
print(json.dumps({k: out[k] for k in ("n_threads", "seconds_measuring", "Q0", "Q1", "thresholds", "tails",
                                      "p_root_6_interval_with_tail")}, indent=1, default=str))
for key in ("A", "B", "C"):
    print(key, " c: p_root  f_chiral  N_eff")
    for c in GRID:
        r = table[key][str(c)]
        print(f"   {c:>6}: {r['p_root']:.4f}  {r['f_chiral']:.4f}  {r['N_eff']:8.2f}")
print(json.dumps(out["readouts"], indent=1, default=str))
print(json.dumps(out["cells"], indent=1))
