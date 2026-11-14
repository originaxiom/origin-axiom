"""Does frame C's read-out depend on the flat line's gauge group? (the dictionary run's flatness item (a)). The read-out
on the whole (B1928's ergodic integral, B1932's exact-weight grid, canonical end L_2) computed separately on words that
fix the mark's vector mod 5 (M v = v: a U(1) flat line extends), words that send it to -v (only Pin(2)/O(2)), and words
that do neither. Expectation, written before the run: the three agree within sampling error, because the congruence
class is a finite-index condition and B1928's limit is the same at every point. Prints ln ratios and z only."""
import sys, math, random, pathlib, json
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
EB = next((ROOT / "frontier").glob("B1932_*")) / "verification"
sys.path.insert(0, str(EB))
import ergodic_both_worlds as E
T = E.T
I1 = E.build(EB / "fiber_grid_t90.json")
v = np.array([1, 2])
def cls(w):
    u = tuple((T.word_matrix(w) @ v) % 5)
    return "U1" if u == (1, 2) else ("Pin" if u == (4, 3) else "none")
rng = random.Random(1937); want = int(sys.argv[1]) if len(sys.argv) > 1 else 600
bins = {"U1": [], "Pin": [], "none": []}
while min(len(b) for b in bins.values()) < want:
    w = "".join(rng.choice("LR") for _ in range(40))
    if "L" not in w or "R" not in w: continue
    c = cls(w)
    if len(bins[c]) < want: bins[c].append(w)
res = {}
for c, ws in bins.items():
    A, wt = [], []
    for w in ws:
        pts, ell = E.thread(w); A.append(E.interp(I1, pts).mean(0)); wt.append(ell)
    A, wt = np.array(A), np.array(wt); R = (wt[:, None] * A).sum(0) / wt.sum()
    jk = []
    for bl in np.array_split(np.arange(len(ws)), 30):
        m = np.ones(len(ws), bool); m[bl] = False; jk.append((wt[m][:, None] * A[m]).sum(0) / wt[m].sum())
    se = np.sqrt(29 * np.mean((np.array(jk) - R) ** 2, 0)) / R
    res[c] = (R, se)
for a, b in (("U1", "Pin"), ("U1", "none"), ("Pin", "none")):
    d = np.log(res[a][0] / res[b][0]); z = d / np.sqrt(res[a][1] ** 2 + res[b][1] ** 2)
    print("%-4s vs %-4s: max |d ln| %.4f, max |z| %.1f, rms z %.2f" % (a, b, np.max(np.abs(d)), np.max(np.abs(z)), math.sqrt(np.mean(z ** 2))))
print("per-class relative sampling error, median: " + ", ".join("%s %.1e" % (c, float(np.median(res[c][1]))) for c in res))
print("words per class:", want)
