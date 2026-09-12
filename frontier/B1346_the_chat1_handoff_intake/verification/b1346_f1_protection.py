"""Verify F1's protection table independently, and Chat-2's nesting claim."""
import warnings; warnings.filterwarnings("ignore")
import snappy
print("F1 -- the protection table, recomputed")
print(f"{'object':9s} {'H1':22s} {'|Sym(M)|':>9s} {'|Sym(cover)|':>13s} {'abelian':>8s}  F1 says")
CLAIM = {"s958":"UNPROTECTED","v2873":"PROTECTED","t12833":"UNPROTECTED","t12835":"PROTECTED"}
for nm in CLAIM:
    M = snappy.Manifold(nm)
    h1 = M.homology()
    try: sg = M.symmetry_group(); n = sg.order()
    except Exception as e: n = f"?{type(e).__name__}"
    # the cusp-trivial Z/3 cover: index-3 cyclic covers
    best = None
    try:
        for C in M.covers(3, cover_type="cyclic"):
            try: o = C.symmetry_group().order()
            except Exception: o = None
            if o is not None and (best is None or o > best[0]): best = (o, C.symmetry_group())
    except Exception: pass
    ab = best[1].is_abelian() if best else "?"
    print(f"{nm:9s} {str(h1):22s} {str(n):>9s} {str(best[0]) if best else '?':>13s} {str(ab):>8s}  {CLAIM[nm]}")

print("\n  t12835's argument, checked with no computation:")
from itertools import permutations
orders = set()
for p in permutations(range(4)):
    # order of the permutation
    seen, o = list(p), 1
    q = list(p)
    while q != list(range(4)):
        q = [p[i] for i in q]; o += 1
    orders.add(o)
print(f"   element orders in S_4: {sorted(orders)} -- contains 6? {6 in orders}")
print("   so a group of order 6 inside S_4 cannot be cyclic; it is S_3, whose lift inverts => PROTECTED")

print("\nChat-2's NESTING claim: drill the shortest geodesic from m004 -> the silver bundle?")
M = snappy.Manifold("m004")
try:
    D = M.drill_word(M.length_spectrum(2.0)[0].word) if hasattr(M,'drill_word') else None
except Exception as e:
    D = None; print("   drill_word:", type(e).__name__, e)
if D is None:
    try:
        spec = M.length_spectrum(2.0)
        print(f"   shortest geodesic: length {spec[0].length}, word {spec[0].word}")
        D = M.drill_word(spec[0].word)
    except Exception as e:
        print("   ", type(e).__name__, e)
if D is not None:
    print(f"   drilled: {D}, vol = {float(D.volume()):.10f}, cusps = {D.num_cusps()}")
    print(f"   m136 vol = {float(snappy.Manifold('m136').volume()):.10f}")
    try: print(f"   isometric to m136? {D.is_isometric_to(snappy.Manifold('m136'))}")
    except Exception as e: print("   isometry test:", type(e).__name__, e)
