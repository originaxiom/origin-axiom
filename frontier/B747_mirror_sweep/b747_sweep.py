"""B747 -- the sqrt5 MIRROR sweep over the 78-slope child grid (prereg 09cef416).

Stage 1: odd-degree theorem on the sealed two-seat degree table (54 slopes).
Stage 2: even-degree slopes (24): recompute the invariant trace field via the
B740 pipeline, cross-check the degree against the sealed table, then exact
containment of sqrt5 (does x^2-5 have a root in K?).  Controls run FIRST and
abort the sweep on any failure.

Run with:  sage b747_sweep.py   (Sage env; __file__ traps avoided via getcwd)
"""
import json
import os
import sys

from sage.all import NumberField, PolynomialRing, QQ
import snappy

HERE = os.getcwd()
SEALED = os.path.join(HERE, "door1_final_sealed_input.json")

Rx = PolynomialRing(QQ, "x")
x = Rx.gen()


def contains_sqrt5(K):
    return len((x**2 - 5).change_ring(K).roots()) > 0


def controls():
    ok = True
    K = NumberField(x**2 - 5, "a")
    t = contains_sqrt5(K); ok &= t
    print(f"[ctrl] Q(sqrt5) contains sqrt5: {t}")
    K = NumberField(x**4 - x**2 - 1, "a")
    t = contains_sqrt5(K); ok &= t
    print(f"[ctrl] Q(sqrt(phi)) (x^4-x^2-1) contains sqrt5: {t}")
    K = NumberField(x**2 + 3, "a")
    t = contains_sqrt5(K); ok &= (not t)
    print(f"[ctrl] Q(sqrt-3) contains sqrt5: {t} (must be False)")
    K = NumberField(x**3 - 2, "a")
    t = contains_sqrt5(K); ok &= (not t)
    print(f"[ctrl] Q(cbrt2) contains sqrt5: {t} (must be False)")
    M = snappy.Manifold("m004")
    F = M.invariant_trace_field_gens().find_field(prec=600, degree=8, optimize=True)
    K = F[0]
    has_m3 = len((x**2 + 3).change_ring(K).roots()) > 0
    has_5 = contains_sqrt5(K)
    ok &= has_m3 and (not has_5)
    print(f"[ctrl] m004 pipeline: contains sqrt-3 {has_m3} (True), sqrt5 {has_5} (False)")
    return ok


def trace_field(slope, sealed_deg):
    p, q = slope
    for prec, degcap in ((600, sealed_deg), (1200, sealed_deg), (2000, sealed_deg + 4),
                         (3000, sealed_deg + 4)):
        M = snappy.Manifold("4_1(%d,%d)" % (p, q))
        try:
            F = M.invariant_trace_field_gens().find_field(prec=prec, degree=degcap,
                                                          optimize=True)
        except Exception as exc:
            print(f"  ({p},{q}) prec={prec}: error {exc}")
            F = None
        if F is not None:
            return F[0]
    return None


def main():
    rows = json.load(open(SEALED))
    print("=" * 78)
    print("B747 -- the sqrt5 mirror sweep (sealed input sha 77818016, prereg 09cef416)")
    print("=" * 78)
    if not controls():
        print("CONTROLS FAILED -- ABORT")
        sys.exit(1)
    print("-" * 78)
    odd = [r for r in rows if r["degree"] % 2 == 1]
    even = [r for r in rows if r["degree"] % 2 == 0]
    print(f"STAGE 1 (theorem): {len(odd)} odd-degree slopes -- no quadratic subfield, "
          "sqrt5 EXCLUDED by parity:")
    print("  " + " ".join(f"({r['slope']})d{r['degree']}" for r in odd))
    print("-" * 78)
    print(f"STAGE 2 (exact): {len(even)} even-degree slopes")
    hits, unresolved = [], []
    for r in even:
        p, q = (int(v) for v in r["slope"].split(","))
        K = trace_field((p, q), r["degree"])
        if K is None:
            unresolved.append(r["slope"])
            print(f"  ({p},{q}) sealed-deg {r['degree']}: UNRESOLVED (field not recovered)")
            continue
        deg = int(K.degree())
        if deg != r["degree"]:
            unresolved.append(r["slope"])
            print(f"  ({p},{q}) DEGREE MISMATCH computed {deg} vs sealed {r['degree']} "
                  "-- flagged UNRESOLVED per prereg")
            continue
        hit = contains_sqrt5(K)
        if hit:
            hits.append(r["slope"])
        print(f"  ({p},{q}) deg {deg} (matches sealed): contains sqrt5 = {hit}")
    print("=" * 78)
    print(f"TALLY: {len(odd)} excluded by parity + {len(even) - len(hits) - len(unresolved)}"
          f" exact-negative + {len(hits)} HITS + {len(unresolved)} unresolved")
    if unresolved:
        print("UNRESOLVED:", unresolved)
    if hits:
        print("VERDICT: MIRROR-ALIVE -- hits:", hits, " (E20 gate before any reading)")
    elif not unresolved:
        print("VERDICT: MIRROR-SILENT -- 0/78: closing silences BOTH columns")
    else:
        print("VERDICT: PENDING -- unresolved slopes remain")
    print("B747 SWEEP COMPLETE")


main()
