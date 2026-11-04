"""POST HOC (after the doublet-index note's second referee, whose probe found the global flip invisible at leading order
on the slopes 1/2, 1/6 and 5/6): on which slopes does the global flip of the reading, (S~, S, S) against (S, S~, S~),
leave every sector's leading exponents unchanged, with the Higgs DR?  B1788's tropical predictor (PROVED at leading order
in Im tau, conditional on its section 5 hypotheses; m1/m3 rests on (c)), exact Fractions, every slope with denominator
<= 60 except the candidate family's (2/5, 3/5, refused).  Data-free; no measured value.

    python3 flip_slopes_posthoc.py <main checkout>     (main at 88c577896)
"""
import pathlib
import sys
from fractions import Fraction as Fr
from math import gcd

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1788_the_closed_form_of_the_exponents" / "verification"))
import tropical as T  # noqa: E402

SEC = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}
FAMILY = (Fr(2, 5), Fr(3, 5))

if __name__ == "__main__":
    P = {rd: T.polys(rd) for rd in ("S", "St")}
    NMAX = 60
    SL = [Fr(r, s) for s in range(1, NMAX + 1) for r in range(0, s) if gcd(r, s) == 1 and Fr(r, s) not in FAMILY]

    def ex(a, sec, rd):
        ql, qr = SEC[sec]
        return tuple(Fr(x) for x in T.predict(P[rd], T.E(ql * a, qr * a)))

    same, diff_sec = [], {"up": 0, "down": 0, "lep": 0}
    for a in SL:
        cand = {"up": ex(a, "up", "St"), "down": ex(a, "down", "S"), "lep": ex(a, "lep", "S")}
        flip = {"up": ex(a, "up", "S"), "down": ex(a, "down", "St"), "lep": ex(a, "lep", "St")}
        if cand == flip:
            same.append(a)
        for s in SEC:
            diff_sec[s] += cand[s] != flip[s]
    print("POST HOC: the global flip (S~, S, S) -> (S, S~, S~) with DR, leading exponents (B1788), %d slopes with denominator <= %d "
          "(the family's 2/5 and 3/5 refused)" % (len(SL), NMAX))
    print("    slopes where every sector's exponents are unchanged: %d: %s" % (len(same), ", ".join(str(a) for a in same)))
    print("    slopes where the sector's exponents change: up %d, down %d, leptons %d" % (diff_sec["up"], diff_sec["down"], diff_sec["lep"]))
