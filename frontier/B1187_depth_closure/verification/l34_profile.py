#!/usr/bin/env python3
"""B1187 / TOMB-L34 stabilization, matched to B742/V37's own design.

B742's reconfirmation tested the ONE-CUT PROFILE S(L) at fixed N (N=1597) and
found it LOGARITHMIC, with controls (random word -> area law). The depth gap:
one N. Closed here: the S(L)-profile slope a(N) fitted over ~40 cuts at EACH
N in {233..4181} (+ a window shift), with random + periodic controls at N=2584.
V37 model: on-site Fibonacci potential +-W/2 (W=1), hopping t=1, half filling.
Bug fenced from the first attempt: word windows must lie inside the built base
word (the shift=20000 rows were empty slices, S=0 -- discarded, rebuilt here).
"""
import json, sys
import numpy as np

def fib_word(n_min):
    a, b = [1], [1, 0]
    while len(b) < n_min:
        a, b = b, b + a
    return b

def S_profile(word, W=1.0, ncuts=40):
    N = len(word)
    H = np.zeros((N, N))
    for i, c in enumerate(word):
        H[i, i] = W / 2 if c == 1 else -W / 2
    for i in range(N - 1):
        H[i, i + 1] = H[i + 1, i] = 1.0
    _, evecs = np.linalg.eigh(H)
    psi = evecs[:, : N // 2]
    Ls = np.unique(np.geomspace(8, N // 2, ncuts).astype(int))
    out = []
    for L in Ls:
        Cm = psi[:L] @ psi[:L].T
        lam = np.linalg.eigvalsh(Cm)
        lam = lam[(lam > 1e-12) & (lam < 1 - 1e-12)]
        S = float(-np.sum(lam * np.log(lam) + (1 - lam) * np.log(1 - lam)))
        out.append((int(L), S))
    return out

def fit_slope(prof):
    Ls = np.array([p[0] for p in prof], dtype=float)
    Ss = np.array([p[1] for p in prof], dtype=float)
    X = np.vstack([np.log(Ls), np.ones_like(Ls)]).T
    (a, b), *_ = np.linalg.lstsq(X, Ss, rcond=None)
    return float(a), float(b)

SIZES = [233, 377, 610, 987, 1597, 2584, 4181]
base = fib_word(10000 + max(SIZES))
res = {"model": "V37: onsite +-1/2, t=1, half filling", "fib": [], "controls": {}}
for shift in (0, 1000):
    for N in SIZES:
        word = base[shift: shift + N]
        assert len(word) == N
        prof = S_profile(word)
        a, b = fit_slope(prof)
        res["fib"].append({"N": N, "shift": shift, "a": round(a, 4), "b": round(b, 4)})
        print(f"fib N={N} shift={shift}: a={a:.4f} b={b:.4f}", flush=True)
rng = np.random.default_rng(7)
for name, word in [("random", list(rng.integers(0, 2, 2584))),
                   ("periodic", [1, 0] * 1292)]:
    prof = S_profile(word)
    a, b = fit_slope(prof)
    res["controls"][name] = {"a": round(a, 4), "b": round(b, 4)}
    print(f"control {name}: a={a:.4f} b={b:.4f}", flush=True)

fib_a = [r["a"] for r in res["fib"]]
big = [r["a"] for r in res["fib"] if r["N"] >= 987]
res["verdict"] = {
    "a_all": [round(min(fib_a), 4), round(max(fib_a), 4)],
    "a_bigN": [round(min(big), 4), round(max(big), 4)],
    "bigN_spread": round(max(big) - min(big), 4),
    "log_class_stable": bool(min(big) > 3 * abs(res["controls"]["random"]["a"])
                             and (max(big) - min(big)) < 0.35 * max(big)),
}
print("verdict:", res["verdict"], flush=True)
json.dump(res, open("l34_profile.json", "w"), indent=1)
print("DONE", flush=True)
