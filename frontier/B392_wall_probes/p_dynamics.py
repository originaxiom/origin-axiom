"""B392 P-DYNAMICS -- exact comparison: our sector twist exponents vs TIM's T-spectrum."""
import json, os
from fractions import Fraction as Fr
ours = [Fr(3,10), Fr(7,10)]
c = Fr(7,10)
tim_h = [Fr(0), Fr(1,10), Fr(3,5), Fr(3,2), Fr(7,16), Fr(3,80)]
tim_T = sorted(set((h - c/24) % 1 for h in tim_h))
hits = {str(o): (o % 1) in tim_T for o in ours}
print("ours:", [str(x) for x in ours])
print("TIM T-exponents (h - c/24 mod 1):", [str(x) for x in tim_T])
print("matches:", hits, "-> verdict:", "MATCH" if any(hits.values()) else "NO-MATCH (as registered)")
json.dump(dict(ours=[str(x) for x in ours], tim=[str(x) for x in tim_T],
               match=any(hits.values())),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "p_dynamics.json"), "w"), indent=1)
