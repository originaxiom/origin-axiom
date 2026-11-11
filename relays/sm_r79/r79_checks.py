#!/usr/bin/env python3
"""SM-R79: this seat's own recomputations behind the numeric findings of its Review 79 reading. Everything is read as git
objects at main 323f92327; nothing is compared with a measured value (B1882's targets are random ones only).

Usage: r79_checks.py OUT.json [REPO]

B1882  the threshold 2rn for the second null; the exact 95% intervals at the 1% depth, over r; the stage-1 control files'
       differing interval endpoints; the top layer's hits in each tail; the last two layers at 0.1% and 0.01%; the
       free-menu read-out's margin at 1%.
B1881  run sequences counted as tuples and as cycles (necklaces) for even length to 6, runs to 5.
B1884  the points of P^1(Z/N) that LR (rows (1,1),(1,2), acting on row vectors) fixes, N = 2..30; the levels the
       multiplicativity check covers.
B1887  D24+ (D24 with the glue (1/2, ..., 1/2)): even, determinant 1, and the glue coset's least norm 6, so its roots are
       those of D24 only.
B1879  words in L and the tick F = L P rewritten as L/R words times a power of P: the first letter, and the run law."""
import json
import subprocess
import sys
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path

import numpy as np
from scipy.stats import beta

C = "323f923278181ffbe69f8c3124182549ab0e3163"
REPO = sys.argv[2] if len(sys.argv) > 2 else "."
show = lambda p: subprocess.run(["git", "-C", REPO, "show", f"{C}:{p}"], capture_output=True, check=True).stdout
out = {"commit": C}

# ---------------- B1882 ----------------
A = "frontier/B1882_the_v1_card_run_on_main"
d = json.loads(show(f"{A}/card/v1_null.json"))
I = d["instruments"]
r2 = I["N2"]["cells"]["chi2|seat"]["all_seeds"]["rows_share"]["top layer 1"]
b = {"second_null_top_share": r2, "as_fraction": str(Fraction(r2).limit_denominator(1000)), "threshold_2rn": 2 * r2 * 1000}
ints = {}
for inst, cell in (("N1", "wf|seat"), ("N2", "chi2|seat"), ("N2", "wf|seat")):
    c = I[inst]["cells"][cell]["leave_out"]["best 1%"]["top layer 1"]
    k, n, r = c["lost"], c["n"], c["rows_share"]
    lo, hi = beta.ppf(0.025, k, n - k + 1), beta.ppf(0.975, k + 1, n - k)
    ints[f"{inst} {cell}"] = {"lost": k, "n": n, "ratio": k / n / r, "interval_over_r": [lo / r, hi / r],
                              "rounded": [round(lo / r, 2), round(hi / r, 2)], "script_ci_matches": abs(lo - c["ci95"][0]) < 1e-12 and abs(hi - c["ci95"][1]) < 1e-12}
b["intervals_at_1pct"] = ints
ca = json.loads(show(f"{A}/card/v1_controls.json"))
cb = json.loads(show(f"{A}/the_seats_stage_1/v1_controls.json"))
diffs = []


def walk(x, y, path=""):
    if isinstance(x, dict):
        for k in sorted(set(x) | set(y)):
            walk(x.get(k), y.get(k), path + "/" + str(k))
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        for i, (u, v) in enumerate(zip(x, y)):
            walk(u, v, path + f"[{i}]")
    elif x != y:
        diffs.append([path, x, y])


walk(ca, cb)
b["control_files_interval_endpoints_differing"] = [x for x in diffs if "ci95" in x[0]]
b["control_files_interval_endpoints_count"] = len(b["control_files_interval_endpoints_differing"])
pops = I["N1"]["cells"]["wf|seat"]["all_seeds"]["populations"]
b["N1_top_layer_hits_by_tail"] = {p: [pops[p]["share"]["top layer 1"]["hits"], pops[p]["n"],
                                      round(pops[p]["share"]["top layer 1"]["ratio_to_rows_share"], 3)]
                                  for p in ("all", "best 5%", "best 1%", "best 0.1%", "best 0.01%")}
lay = {}
for inst, cell in (("N1", "wf|seat"), ("N2", "chi2|seat"), ("N2", "wf|seat")):
    P = I[inst]["cells"][cell]["all_seeds"]["populations"]
    for depth in ("best 0.1%", "best 0.01%"):
        s = P[depth]["share"]
        lay[f"{inst} {cell} {depth}"] = {k: [s[k]["hits"], round(s[k]["ratio_to_rows_share"], 2)] for k in ("top layer 2", "top layer 1")}
b["last_two_layers"] = lay
c = I["N2"]["cells"]["wf|free"]["leave_out"]["best 1%"]["top layer 1"]
b["free_menu_wf_at_1pct"] = {"lost": c["lost"], "line_2rn": 2 * c["rows_share"] * c["n"], "margin": c["lost"] - 2 * c["rows_share"] * c["n"],
                             "ratio": c["lost"] / c["n"] / c["rows_share"]}
out["B1882"] = b

# ---------------- B1881 ----------------
tuples = sum(5 ** n for n in (2, 4, 6))
phi = lambda m: sum(1 for k in range(1, m + 1) if gcd(k, m) == 1)
neck = lambda n, k: sum(phi(dd) * k ** (n // dd) for dd in range(1, n + 1) if n % dd == 0) // n
out["B1881"] = {"run_sequences_as_tuples": tuples, "as_cycles_up_to_rotation": sum(neck(n, 5) for n in (2, 4, 6))}

# ---------------- B1884 ----------------


def proj_points(N):
    pts = set()
    units = [u for u in range(1, N) if gcd(u, N) == 1]
    for a, bb in product(range(N), repeat=2):
        if gcd(gcd(a, bb), N) == 1:
            pts.add(min(((a * u) % N, (bb * u) % N) for u in units))
    return pts, units


fixed = {}
for N in range(2, 31):
    pts, units = proj_points(N)
    f = sorted(p for p in pts if min((((p[0] + p[1]) * u) % N, ((p[0] + 2 * p[1]) * u) % N) for u in units) == p)
    if f:
        fixed[N] = f
allN = {a * bb for a in range(2, 201) for bb in range(2, 201) if gcd(a, bb) == 1 and a * bb <= 200}
cov = {a * bb for a in range(2, 15) for bb in range(2, 15) if gcd(a, bb) == 1 and a * bb <= 200}
out["B1884"] = {"LR_fixed_points_of_P1_ZN_to_30": {str(k): v for k, v in fixed.items()},
                "coprime_composite_levels_to_200": len(allN), "covered_by_parts_to_14": len(cov), "first_missed": min(allN - cov)}

# ---------------- B1887 ----------------
n = 24
glue = [Fraction(1, 2)] * n
# D24+ = D24 u (D24 + glue); D24 = integer vectors of even sum. Determinant: [Z^n : D_n] = 2, glue index 2 -> det 4 / 4 = 1.
glue_norm = sum(x * x for x in glue)
least_coset_norm = Fraction(n, 4)          # (+-1/2, ..., +-1/2) has the least norm in the coset
out["B1887"] = {"rank": n, "glue_norm": str(glue_norm), "glue_norm_even_integer": glue_norm.denominator == 1 and glue_norm % 2 == 0,
                "det_D24": 4, "det_D24_plus": 4 // (2 * 2), "least_norm_in_glue_coset": str(least_coset_norm),
                "roots_only_D24": least_coset_norm > 2}

# ---------------- B1879 ----------------
L = np.array([[1, 0], [1, 1]]); R = np.array([[1, 1], [0, 1]]); Pm = np.array([[0, 1], [1, 0]])
assert (Pm @ L @ Pm == R).all()


def rewrite(word):
    s, par = [], 0
    for ch in word:
        s.append("L" if par == 0 else "R")
        par ^= ch == "F"
    return "".join(s), par


def first_run(s):
    k = 1
    while k < len(s) and s[k] == s[0]:
        k += 1
    return k


nw = 12
first = Counter()
for w in product("LF", repeat=nw):
    s, par = rewrite(w)
    M = np.eye(2, dtype=int)
    for ch in w:
        M = M @ (L if ch == "L" else L @ Pm)
    W = np.eye(2, dtype=int)
    for ch in s:
        W = W @ (L if ch == "L" else R)
    assert (M == W @ np.linalg.matrix_power(Pm, par)).all()
    first[s[0]] += 1
out["B1879"] = {"words": 2 ** nw, "first_letter_L_and_tick": dict(first),
                "first_letter_L_and_R": dict(Counter(w[0] for w in product("LR", repeat=nw))),
                "first_run_law_equal": Counter(first_run(rewrite(w)[0]) for w in product("LF", repeat=nw))
                == Counter(first_run("".join(w)) for w in product("LR", repeat=nw))}
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, ensure_ascii=False, default=str)[:6000])
