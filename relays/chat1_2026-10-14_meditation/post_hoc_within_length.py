"""POST HOC (labelled), after the meditation's referee: at fixed word length, how do volume and height relate, and which
way does the action push the height? No prediction is scored.

On T-ROOT's 31,040 threads (t_root_threads.json; volumes from SnapPy), with the exact Lagrange value of each thread's
periodic cutting sequence (as in meditation_checks.py):
  W1  Spearman(Vol, Lagrange) within each length 4..18;
  W2  at each length, the mean Lagrange value weighted by exp(-c Vol / 6 pi) at c = 0 (plain), 6 and 24.

Run once:  python3 -B post_hoc_within_length.py > post_hoc_within_length_run.txt 2>&1
"""
import json, math, pathlib
import numpy as np
from scipy.stats import spearmanr

HERE = pathlib.Path(__file__).resolve().parent
thr = json.loads((HERE.parent / "chat1_2026-10-14_the_scale" / "t_root_threads.json").read_text())


def runs(w):
    k = 0
    while w[k] == w[k - 1]: k += 1
    u = w[k:] + w[:k]
    rl, cur, n = [], u[0], 0
    for ch in u:
        if ch == cur: n += 1
        else: rl.append(n); cur, n = ch, 1
    rl.append(n)
    return rl


def cf(seq):
    x = 0.0
    for a in reversed(seq[1:]):
        x = 1.0 / (a + x)
    return seq[0] + x


def lagrange(w):
    a = runs(w); n = len(a); rep = 60 // n + 4
    return max(cf([a[(i + j) % n] for j in range(n * rep)]) + 1.0 / cf([a[(i - 1 - j) % n] for j in range(n * rep)])
               for i in range(n))


out = {"status": "post hoc (labelled), after the meditation's referee; no prediction", "by length": {}}
for n in range(4, 19):
    ws = [w for w in thr if len(w) == n]
    v = np.array([thr[w][0] for w in ws]); L = np.array([lagrange(w) for w in ws])
    row = {"n threads": len(ws), "Spearman(Vol, Lagrange)": float(spearmanr(v, L).correlation)}
    for c in (0, 6, 24):
        q = np.exp(-c * (v - v.min()) / (6 * math.pi)); q /= q.sum()
        row[f"mean Lagrange at c = {c}"] = float((q * L).sum())
    out["by length"][str(n)] = row
    print(n, json.dumps(row), flush=True)
(HERE / "post_hoc_within_length.json").write_text(json.dumps(out, indent=1) + "\n")
