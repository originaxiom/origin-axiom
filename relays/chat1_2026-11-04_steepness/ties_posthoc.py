"""POST HOC (after the steepness map's output 6ccd2a69c and its referee): under the equal readings (S, S) and the Higgs DR,
on the slopes where up is steeper in m2/m3 (||4a|| > 1/3, i.e. t = ||a|| in (1/12, 1/6) or (1/3, 5/12)), the referee's
closed form for the m1/m3 gap e_up(m1/m3) - e_down(m1/m3):
    min(0, 2t - 1/4) on t in (1/12, 1/6),    min(0, 3/4 - 2t) on t in (1/3, 5/12),
checked exactly against B1788's tropical predictor on every slope with denominator <= 200; and the tie class (gap 0),
t in [1/8, 1/6) or (1/3, 3/8], counted.  Exact arithmetic; no measured value; leading order, generic b.

    python3 ties_posthoc.py <main checkout>     (main at 2d0419d3c)
"""
import pathlib
import sys
from fractions import Fraction as Fr
from math import gcd

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1788_the_closed_form_of_the_exponents" / "verification"))
import tropical as T  # noqa: E402


def nd(x):
    x = Fr(x) % 1
    return min(x, 1 - x)


if __name__ == "__main__":
    P = T.polys("S")
    NMAX = 200
    SL = [Fr(r, s) for s in range(1, NMAX + 1) for r in range(0, s) if gcd(r, s) == 1]
    steep = mism = ties = tie_pred = pos = 0
    for a in SL:
        if not nd(4 * a) > Fr(1, 3):
            continue
        steep += 1
        eu = T.predict(P, T.E(1 * a, -4 * a))[1]
        ed = T.predict(P, T.E(1 * a, 2 * a))[1]
        g = Fr(eu) - Fr(ed)
        t = nd(a)
        form = min(Fr(0), 2 * t - Fr(1, 4)) if t < Fr(1, 4) else min(Fr(0), Fr(3, 4) - 2 * t)
        mism += g != form
        pos += g > 0
        ties += g == 0
        tie_pred += (Fr(1, 8) <= t < Fr(1, 6)) or (Fr(1, 3) < t <= Fr(3, 8))
    print("POST HOC: (S, S), the Higgs DR; slopes with denominator <= %d: %d; m2-steep (||4a|| > 1/3): %d" % (NMAX, len(SL), steep))
    print("    the m1/m3 gap against the closed form min(0, 2t - 1/4) / min(0, 3/4 - 2t): %d mismatches" % mism)
    print("    m1/m3 gap > 0 on %d of the m2-steep slopes; = 0 (ties) on %d; the tie class t in [1/8, 1/6) or (1/3, 3/8] holds %d" % (pos, ties, tie_pred))
