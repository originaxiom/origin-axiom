"""Review 86 mend (main, 2026-11-24): the census of B1971 at the points of exact order 10 that its filter dropped (largest
denominator 5 or 2, not 10): (1/2, k/5) and (k/5, 1/2), k = 1..4.  Same code and settings as B1971's bits.py (height 30,
column 0.13): each sector's left singular vectors' dominant null-basis directions and the least diagonal |V|."""
import sys, pathlib
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import bits as BT, nullbasis as NB
from fractions import Fraction as Fr
pts = [(Fr(1, 2), Fr(k, 5)) for k in range(1, 5)] + [(Fr(k, 5), Fr(1, 2)) for k in range(1, 5)]
from math import lcm
for (a, b) in pts:
    S = NB.snap(30.0, a, b); V = S["V"]
    ua = [BT.dom([S["up"]["Ub"][k][c] for k in range(3)]) for c in range(3)]; da = [BT.dom([S["down"]["Ub"][k][c] for k in range(3)]) for c in range(3)]
    diag = min(float(abs(V[k, k])) for k in range(3))
    print("(%s, %s) order %d: up %s down %s | least diagonal %.3f | %s" % (a, b, lcm(a.denominator, b.denominator), "/".join(x[0] for x in ua), "/".join(x[0] for x in da), diag, "aligned" if diag >= 0.9 else "NOT aligned"), flush=True)
