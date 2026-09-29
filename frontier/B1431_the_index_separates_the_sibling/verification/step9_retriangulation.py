"""
Step 9.  Retriangulation invariance, redone with the corrected truncation.

GHRS Theorem 5.2: the sum converges iff the ideal triangulation is 1-efficient.
GHRS Theorem 5.3: a 2-3 move preserves the index only if BOTH triangulations
are 1-efficient.  SnapPy's randomize() gives no 1-efficiency guarantee, so
disagreements here are expected in principle; the point of the test is to see
whether the answer is stable over many triangulations of the same manifold.
"""
import sys, random, collections
import snappy
from tet_index import s_str, s_eq, s_trunc
from step7_fixed_gluing import index_zero

X = int(sys.argv[1]) if len(sys.argv) > 1 else 26
CUT = X - 6

print("=" * 78)
print(f"STEP 9: retriangulation stability (to q^{CUT//2})")
print("=" * 78)
random.seed(2026)
for name in ["m004", "m009", "m015"]:
    base, npts, mx = index_zero(name, X)
    seen = collections.Counter()
    sizes = collections.Counter()
    fails = 0
    for trial in range(30):
        M = snappy.Manifold(name)
        M.randomize()
        n = M.num_tetrahedra()
        if n > 5:
            continue
        try:
            s, _p, _m = index_zero(M, X)
        except AssertionError:
            fails += 1
            continue
        sizes[n] += 1
        seen[s_eq(base, s, CUT)] += 1
    print(f"\n  {name}: base = {s_str(base, min(CUT, 20))}")
    print(f"     {sum(sizes.values())} random retriangulations computed, sizes {dict(sizes)}"
          f"{', %d skipped (box)' % fails if fails else ''}")
    print(f"     agreeing with the base: {seen[True]} / {sum(seen.values())}")
