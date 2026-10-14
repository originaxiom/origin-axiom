"""POST HOC (labelled), after post_hoc_reversal.py: the weave's CP symmetry in the thread frame, on T-ROOT's data.

post_hoc_reversal.py found (read-out, not a prediction): a thread's reversed word carries exactly the complex-conjugate
couplings (K, Y), its mirror (L <-> R) too, and their composition W^T the same couplings. By hand:
  rev(W) = J W^T J and W^T = S W^-1 S^-1, so rev(W) is conjugate to W^-1 by J S (det -1). The mapping torus of
  g V g^-1 is that of V through the fibre map g (orientation-reversing when det g = -1), and that of W^-1 is that of W
  with the base reversed (orientation-reversing). So M(rev W) = M(W) with orientation kept: equal Vol, equal CS.
  W^T is conjugate to W^-1 in SL(2, Z): the same closed geodesic as W, reversed, and M(W^T) is M(W)'s mirror: CS flips.
This script checks those identities on every thread of T-ROOT's census (t_root_threads.json: 31,040 threads to length
18, SnapPy volumes and CS mod pi^2), and reads out how much of the weave's weight sits on threads that are their own
reverse (real couplings in the thread frame) under T-ROOT's measure.

  C1  Vol(rev W) = Vol(W) to 1e-9 and CS(rev W) = CS(W) mod pi^2 to 1e-6, for every W
  C2  Vol(W^T) = Vol(W) and CS(W^T) = -CS(W) mod pi^2, for every W (W^T = mirror of rev W)
  R1  the number of threads that are their own reverse, by length; their weight share at T-ROOT's c grid, (A), (B), (C)

Run once:  python3 -B post_hoc_reversal_census.py > post_hoc_reversal_census_run.txt 2>&1
"""
import json, math, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SCALE = HERE.parent / "chat1_2026-10-14_the_scale"
PI2 = math.pi ** 2
GRID = [0.5, 1, 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]


def red(x):
    y = math.fmod(x, PI2)
    if y > PI2 / 2: y -= PI2
    if y <= -PI2 / 2: y += PI2
    return y


canon = lambda w: min(w[k:] + w[:k] for k in range(len(w)))
rev = lambda w: canon(w[::-1])
mirr = lambda w: canon(w.translate(str.maketrans("LR", "RL")))
transp = lambda w: mirr(rev(w))

thr = json.loads((SCALE / "t_root_threads.json").read_text())
words = list(thr)
c1_bad, c2_bad, missing = [], [], []
for w in words:
    v, c = thr[w]
    r, t = rev(w), transp(w)
    if r not in thr or t not in thr:
        missing.append(w); continue
    if abs(thr[r][0] - v) > 1e-9 or abs(red(thr[r][1] - c)) > 1e-6:
        c1_bad.append([w, r, v, thr[r][0], c, thr[r][1]])
    if abs(thr[t][0] - v) > 1e-9 or abs(red(thr[t][1] + c)) > 1e-6:
        c2_bad.append([w, t, v, thr[t][0], c, thr[t][1]])
out = {"status": "post hoc (labelled), after post_hoc_reversal.py", "n_threads": len(words),
       "C1": {"violations": c1_bad[:10], "n_violations": len(c1_bad), "holds": not c1_bad and not missing},
       "C2": {"violations": c2_bad[:10], "n_violations": len(c2_bad), "holds": not c2_bad and not missing},
       "missing partners": missing[:10]}

selfrev = np.array([rev(w) == w for w in words])
by_len = {}
for w, s in zip(words, selfrev):
    d = by_len.setdefault(len(w), [0, 0]); d[0] += int(s); d[1] += 1
out["R1"] = {"own reverse / all, by length": {str(k): v for k, v in sorted(by_len.items())},
             "own reverse, total": int(selfrev.sum())}
L_of_n = {}
for w in words:
    L_of_n[len(w)] = L_of_n.get(len(w), 0) + 1
n_arr = np.array([len(w) for w in words], dtype=float)
vol = np.array([thr[w][0] for w in words])
logw = {"A": -n_arr * math.log(2), "B": -n_arr * math.log(3),
        "C": np.array([-math.log(len(w) * (len(w) - 1) * L_of_n[len(w)]) for w in words])}
shares = {}
for key in ("A", "B", "C"):
    shares[key] = {}
    for c in GRID:
        e = logw[key] - c * vol / (6 * math.pi)
        q = np.exp(e - e.max()); q /= q.sum()
        shares[key][str(c)] = float(q[selfrev].sum())
out["R1"]["weight share of threads that are their own reverse"] = shares
(HERE / "post_hoc_reversal_census.json").write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps({k: out[k] for k in ("n_threads", "C1", "C2", "missing partners")}, indent=1))
print(json.dumps(out["R1"]["own reverse / all, by length"]))
print("own reverse share at c = 6:", {k: round(shares[k]["6"], 4) for k in shares},
      " at c = 24:", {k: round(shares[k]["24"], 4) for k in shares})
