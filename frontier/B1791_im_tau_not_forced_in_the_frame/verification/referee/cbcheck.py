"""Route A (cA, numpy polar quadrature, as the note uses) against route B (cB, mpmath strip quadrature, B1656's own second
route) for the channel norms at large Im tau, where the note's monotonicity claims run (Im tau to 8)."""
import sys, pathlib, importlib.util
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
spec = importlib.util.spec_from_file_location("c26", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C); B = C._modules()["B"]
for (re, im) in ((0.3, 3.0), (0.3, 6.0), (0.3, 8.0)):
    t = complex(re, im); w = 0.4 * t + 0.1
    x, yy = B.sector_twists(w, t, B.SIXY["Q"], B.SIXY["d"]); R = B.residues(x, yy, t); cA = B.cA(x, yy, t, R)
    out = []
    for s in ("1", "j"):
        cb = B.cB(x, yy, t, s, R[s], n=24)
        out.append((s, round(cA[s], 6), round(cb, 6)))
    print("tau", t, "down on (2/5,1/10): (channel, cA, cB)", out, flush=True)
print("cbcheck exit 0")
