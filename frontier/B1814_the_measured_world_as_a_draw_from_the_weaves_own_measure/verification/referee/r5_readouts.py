"""Referee R5: read-out checks.  (a) the A1 unforced cloud's own nearest-distance quantiles (what "typical" means in sigma);
(b) the three-deep share conditioned on resolved draws (the sealed read-out counts floored and capped draws as deep);
(c) the by-hand nearest draw re-derived with its actual configuration (the JSON's "configuration" field is the unforced
sequence's entry); (d) random hierarchies: in which direction are they atypical under A0 (deep or shallow)?
(e) anarchy p at its floor 1/(N+1); (f) per-number distances of the D1 nearest draw."""
import json, math, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import r3_independent as R
t6, s6, t9, s9 = R.target(); arms = R.load_census(); cf = R.cfg_seq(); out = {}
A1u = R.Typ(R.model(arms["A1"], cf), s6); A0u = R.Typ(R.model(arms["A0"], cf), s6); A1h = R.Typ(R.model(arms["A1"], cf, fixed=(1, 0, 0), c=3), s6)
for k, ty in (("A1u", A1u), ("A1h", A1h), ("A0u", A0u)):
    out["nn quantiles " + k] = {q: float(np.quantile(ty.dref, q)) for q in (0.25, 0.5, 0.75, 0.9, 0.93, 0.95, 0.99)}
# (b) three deep, conditioned vs unconditioned
for arm in ("A0", "A1"):
    Xall = []; Xres = []
    for r, (h, ru, rd, rl) in zip(arms[arm], cf):
        v = R.six(r, h, ru, rd, rl, 1)
        v = [1e-12] * 6 if v is None else [max(x, 1e-12) for x in v]
        Xall.append(v)
        if all(x > 1e-12 for x in v) and r["Im_tau"] <= 60: Xres.append(v)
    Xall, Xres = np.array(Xall), np.array(Xres)
    out["three deep " + arm] = {"unconditioned (sealed read-out's base)": float(np.mean(np.all(Xall[:, [1, 3, 5]] < 1e-2, 1))),
                                "among resolved": float(np.mean(np.all(Xres[:, [1, 3, 5]] < 1e-2, 1))), "n resolved": len(Xres)}
# (c) the by-hand nearest draw
rs = arms["A1"]; best = None
for j, (r, (h, ru, rd, rl)) in enumerate(zip(rs, cf)):
    v = R.six(r, h, 1, 0, 0, 3)
    if v is None or not all(x > 1e-12 for x in v): continue
    d = np.abs(np.log(v) - t6) / s6
    if best is None or d.max() < best[0]: best = (float(d.max()), j, h, d.tolist(), r["Re_tau"], r["Im_tau"], r["alpha"], r["b"], r["order"], r["trace"], r["word"][:12] + "...", len(r["word"]))
out["by-hand nearest (actual configuration: readings (S~,S,S), c = 3, horocycle index h)"] = best
# (d) direction of random hierarchies' atypicality under A0 (p_F <= 0.05): mean share of A0 draws below each target ratio
Rh = R.rand_hier(1741); pf = A0u.pF(Rh)[0]; at = Rh[pf <= 0.05]
below = np.array([[np.mean(A0u.X[:, k] < t[k]) for k in range(6)] for t in at[:500]])
out["random hierarchies atypical under A0 by p_F (seed 1741)"] = {"share": float(np.mean(pf <= 0.05)),
    "mean share of A0 draws below the target, per ratio": below.mean(0).tolist(),
    "fraction of them with c/t-like (up m2/m3) below 5% of A0": float(np.mean(below[:, 0] < 0.05)),
    "fraction with any ratio below 2.5% of A0 (deep side)": float(np.mean((below < 0.025).any(1))),
    "fraction with any ratio above 97.5% of A0 (shallow side)": float(np.mean((below > 0.975).any(1)))}
out["data's A0 share below, per ratio"] = [float(np.mean(A0u.X[:, k] < t6[k])) for k in range(6)]
out["anarchy p floor 1/(N+1)"] = 1 / 4001
(HERE / "r5_out.json").write_text(json.dumps(out, indent=1)); print(json.dumps(out, indent=1))
