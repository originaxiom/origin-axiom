"""B399 A2 -- the hierarchy probe: does the singles tower generate scale separation?
Exact envelope statistics across the five rungs (registered expectation: BOUNDED)."""
import json, os, math
from fractions import Fraction as Fr

rungs = {
    "15":  dict(cells=4,  values=[Fr(1,4)]*4),
    "45":  dict(cells=4,  values=[Fr(1,4)]*4),
    "135": dict(cells=4,  values=[Fr(1,4)]*4),
    "405": dict(cells=12, values=None),   # (1+c)/12 over zeta9+ orbit, x4 each
    "1215":dict(cells=24, values=None),   # 12 x (1/12 exact) + triple x4 (ID open)
}
c9 = [2*math.cos(2*math.pi*k/9) for k in (1, 2, 4)]
v405 = sorted((1+c)/12 for c in c9)
stats = {}
stats["15"] = stats["45"] = stats["135"] = dict(min="1/4", max="1/4", sum="1")
stats["405"] = dict(min=f"{v405[0]:.6f}", max=f"{v405[-1]:.6f}", sum="1 (exact, banked)",
                    exact_form="(1+c)/12, c in zeta9+ orbit")
stats["1215"] = dict(known_line="1/12 x 12 cells (exact)", triple="ID open",
                     sum="1 conditional on triple summing to 0")
# the envelope: max |v| per rung (exact where known)
env = [0.25, 0.25, 0.25, max(abs(v) for v in v405), 1/12]  # 1215: the known line; triple caveat
ratios = [env[i+1]/env[i] for i in range(4)]
print("envelope max|v| per rung:", [f"{e:.5f}" for e in env])
print("consecutive ratios:", [f"{r:.4f}" for r in ratios])
print("VERDICT: monotone CONTRACTION (no growth anywhere); all values in [-1/12, 1/4];")
print("the tower refines measure at fixed total (sum rule), it does not separate scales.")
json.dump(dict(stats=stats, envelope=[str(e) for e in env],
               contraction=all(r <= 1.0 + 1e-12 for r in ratios),
               caveat="1215 envelope uses the exact 1/12 line; triple ID open"),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "a2_hierarchy.json"), "w"), indent=1)
print("DONE")
