"""Paper III, Proposition 4.1 and Scope 4.2: the n=2 factor at the abscissa.

R(s, sigma_2) = prod_gamma (1 - e^{2 i theta} e^{-s l}) converges absolutely for s > 2.
The n = 2 factor of the graviton product therefore sits AT the abscissa, and is the one
factor Pfaff's ratio formula cannot reach.  This script approaches the abscissa from above
and tracks the dependence on the geodesic cutoff.

THE BITE CONTROL IS THE POINT.  A smooth curve above the abscissa means nothing unless the
same instrument visibly fails below it, where divergence is certain.  That control runs
first, and the run aborts if it does NOT diverge -- an instrument that cannot report failure
is not evidence.

Requires snappy.  Run: python3 check_n2_abscissa.py
"""
import math
import sys

try:
    import snappy
except ImportError:
    print("SKIP: snappy not available in this environment")
    sys.exit(0)

FAIL = []
CUTOFFS = (4.5, 5.0, 5.5)


def check(name, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)
    return ok


M = snappy.Manifold("m004")


def geodesics(cut):
    """(complex length, multiplicity) for primitive closed geodesics up to cutoff."""
    return [(complex(g.length), g.multiplicity) for g in M.length_spectrum(cut)]


def logR(s, cut, k=2):
    """log |R(s, sigma_k)| = sum_gamma mult * log|1 - e^{i k theta} e^{-s l}|."""
    tot = 0.0
    for L, mult in geodesics(cut):
        ell, th = L.real, L.imag
        z = complex(math.cos(k * th), math.sin(k * th)) * math.exp(-s * ell)
        tot += mult * math.log(abs(1.0 - z))
    return tot


def absR(s, cut):
    return math.exp(logR(s, cut))


def spread(s):
    vals = [absR(s, c) for c in CUTOFFS]
    return max(vals) - min(vals), vals


print("A  BITE CONTROL -- below the abscissa the instrument MUST diverge")
base_spread, _ = spread(2.0)
below = [(1.90, None), (1.80, None), (1.60, None), (1.40, None)]
ratios = []
for s, _ in below:
    sp, _v = spread(s)
    ratios.append(sp / base_spread)
    print("      s = %.2f   cutoff spread = %.3e   = %5.1fx the s=2 spread" % (s, sp, sp / base_spread))
ok = all(ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1)) and ratios[-1] > 5.0
check("the spread grows monotonically and sharply below s = 2", ok,
      "final ratio %.1fx" % ratios[-1])
if not ok:
    print("\nABORT: the instrument cannot report failure, so nothing above the abscissa is evidence.")
    sys.exit(1)

print("\nB  approach from above -- is there any breakdown at s = 2?")
rows = []
for s in (2.6, 2.4, 2.2, 2.1, 2.05, 2.02, 2.0):
    sp, vals = spread(s)
    rows.append((s, sp, vals[-1]))
    print("      s = %-5.2f  |R| = %.6f   cutoff spread = %.2e" % (s, vals[-1], sp))

vals = [r[2] for r in rows]
sprs = [r[1] for r in rows]
check("|R(s, sigma_2)| is monotone increasing as s decreases to 2",
      all(vals[i] < vals[i + 1] for i in range(len(vals) - 1)),
      "%.4f at s=2.6 -> %.4f at s=2.0" % (vals[0], vals[-1]))
check("no pole or discontinuity: every value finite and O(1)",
      all(math.isfinite(v) and 0.5 < v < 5.0 for v in vals))
check("the cutoff spread stays small and grows smoothly, not explosively",
      all(sprs[i] < sprs[i + 1] for i in range(len(sprs) - 1)) and sprs[-1] < 1e-2,
      "max spread %.2e" % sprs[-1])
check("banked values reproduced: 1.1075 at s=2.6 and 1.1936 at s=2.0",
      abs(vals[0] - 1.1075) < 5e-4 and abs(vals[-1] - 1.1936) < 5e-4,
      "got %.4f and %.4f" % (vals[0], vals[-1]))

print("\nC  what is NOT established")
print("      Convergence is NOT proved.  Three cutoffs; the cutoff -> infinity limit is")
print("      untested, and a spread small at 5.5 can still fail to converge.  What is")
print("      established is the ABSENCE OF OBSERVABLE BREAKDOWN at s = 2, on an instrument")
print("      shown above to be capable of reporting one.")

print("\n%d/%d checks passed" % (5 - len(FAIL), 5))
sys.exit(1 if FAIL else 0)
