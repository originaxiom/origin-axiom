"""Stage 1c (the owner's question: do the two clocks interact?; data-free): count threads move by move (all primitive
positive words of word length n, both letters) and weight each thread by exp(-beta * its geometric length) -- the Farey
coding's thermodynamic family. beta = 0 is the move clock (stage 1); beta = 1 is where the geometric clock sits (the
family's phase transition, B852's plateau). Reports P(Im tau > Y) along beta, at n = 12 and 14, with each thread's geodesic
sampled in arclength as in stage 1.
    python3 stage1c_two_clocks.py      # writes stage1c_two_clocks.json beside itself"""
import json, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "stage1_threads_measure.py").read_text().split("words = sorted(")[0]
ns = {"__file__": str(HERE / "stage1_threads_measure.py"), "__name__": "s1"}; exec(compile(src, "s1", "exec"), ns)
TG, geodesic_heights, hyp = ns["TG"], ns["geodesic_heights"], ns["hyp_cdf_above"]
BETAS = (0.0, 0.25, 0.5, 0.75, 0.9, 1.0, 1.1, 1.25, 1.5)
YS = (1.5, 2.0, 3.0, 4.0, 6.0)
out = {"hyperbolic area": {str(Y): round(hyp(Y), 4) for Y in YS}}
for n in (12, 14):
    per = []
    for w in TG.necklaces(n, n):                                  # threads of exactly length n
        hs, ell = geodesic_heights(TG.mat(w)); hs = np.array(hs)
        per.append((ell, {Y: float((hs > Y).mean()) for Y in YS}))
    row = {}
    for b in BETAS:
        wts = np.array([ell * math.exp(-b * ell) for ell, _ in per])   # arclength (ell) times the geometric weight
        wts = wts / wts.sum()
        row[str(b)] = {str(Y): round(float(sum(wt * fr[Y] for wt, (_, fr) in zip(wts, per))), 4) for Y in YS}
    out["n = %d (threads of exactly that length: %d)" % (n, len(per))] = row
    print(n, len(per), json.dumps(row), flush=True)
(HERE / "stage1c_two_clocks.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print(out["hyperbolic area"])
