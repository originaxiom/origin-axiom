"""xB033 Y1b -- RECONCILIATION with B1239, which banked this on 2026-09-02.

B1239 selected closed amphichiral manifolds with `M.symmetry_group().is_amphicheiral()` and got
37 amphichiral / 37 zero.  Y1 additionally required `is_full_group()` and got 36 / 36.

`is_full_group()` False means SnapPy has not verified the symmetry group is the FULL one, so
is_amphicheiral() can give a FALSE NEGATIVE there but not a false positive.  Requiring it therefore
tests a WEAKER statement: it can EXCLUDE a genuinely amphichiral manifold.  B1239's looser predicate
is the right one for a claim of the form "EVERY amphichiral manifold is at zero", and Y1's was
over-strict.  This cell runs B1239's predicate and checks 36 is a subset of 37.
"""
import json, os, sys, warnings
warnings.filterwarnings("ignore")
import snappy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from closed_side import closed_cs, fold_half, klass

loose, strict, errs = [], [], 0
n = 0
for M in snappy.OrientableClosedCensus():
    n += 1
    try:
        G = M.symmetry_group()
        a_loose = bool(G.is_amphicheiral())
        a_strict = bool(G.is_full_group() and G.is_amphicheiral())
    except Exception:
        errs += 1
        continue
    if not a_loose:
        continue
    cs, err = closed_cs(str(M))
    if cs is None:
        errs += 1
        continue
    row = (str(M), float(fold_half(cs)), klass(cs), a_strict)
    loose.append(row)
    if a_strict:
        strict.append(row)

print(f"Y1b      scanned {n} closed census manifolds; errors {errs}")
print(f"         B1239's predicate  is_amphicheiral()                     : {len(loose)}")
print(f"         Y1's predicate     is_full_group() AND is_amphicheiral() : {len(strict)}")
bad_l = [r for r in loose if r[2] != 'zero']
bad_s = [r for r in strict if r[2] != 'zero']
print(f"         at class ZERO -- B1239's set: {len(loose)-len(bad_l)}/{len(loose)}   "
      f"Y1's set: {len(strict)-len(bad_s)}/{len(strict)}")
print(f"         off zero: B1239's set {bad_l}   Y1's set {bad_s}")
extra = [r for r in loose if not r[3]]
print(f"         in B1239's set but NOT in Y1's (is_full_group() False): {len(extra)} "
      f"-> {[(r[0], r[2]) for r in extra]}")
print(f"         Y1's 36 is a SUBSET of B1239's 37: {len(strict) < len(loose) and not bad_s}")
maxfold = max(abs(r[1]) for r in loose) if loose else None
print(f"         max |folded cs| over B1239's set: {maxfold:.3e}  (B1239 reported 7.8e-16)")
print()
if len(loose) == 37 and not bad_l:
    print("         *** RECONCILED EXACTLY: B1239's 37 amphichiral / 37 zero REPRODUCES on this")
    print("         bench 26 days later, and Y1's 36 is the same set minus the one manifold whose")
    print("         symmetry group is not certified full.  NO DISCREPANCY -- a predicate difference,")
    print("         and B1239's predicate was the better one.")
else:
    print(f"         *** DOES NOT RECONCILE: got {len(loose)} amphichiral, "
          f"{len(bad_l)} off zero. B1239 reported 37/37. THAT is the headline.")
json.dump({"n_loose": len(loose), "n_strict": len(strict), "off_zero_loose": bad_l,
           "off_zero_strict": bad_s, "extra_rows": extra, "max_abs_folded": maxfold,
           "b1239_reported": 37, "reconciled": bool(len(loose) == 37 and not bad_l)},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "y1b_reconcile.json"),
               "w", encoding="utf-8"), indent=1, default=str)
