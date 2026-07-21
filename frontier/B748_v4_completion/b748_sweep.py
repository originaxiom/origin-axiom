"""B748 -- the V4-completion sweep (prereg a59ac036): sqrt(-15) meeting-face
containment over the 78-slope grid, with per-slope sqrt(-3) consistency
re-derivation against B740's verdicts.  Run: sage b748_sweep.py"""
import json, os, sys
from sage.all import NumberField, PolynomialRing, QQ
import snappy

HERE = os.getcwd()
Rx = PolynomialRing(QQ, "x"); x = Rx.gen()

def has_root(K, poly):
    return len(poly.change_ring(K).roots()) > 0

def controls():
    ok = True
    K = NumberField(x**2 + 15, "a"); t = has_root(K, x**2 + 15); ok &= t
    print(f"[ctrl] Q(sqrt-15) contains sqrt-15: {t}")
    K = NumberField(x**2 - 5, "a"); t = has_root(K, x**2 + 15); ok &= (not t)
    print(f"[ctrl] Q(sqrt5) contains sqrt-15: {t} (must be False)")
    K = NumberField(x**2 + 3, "a"); t = has_root(K, x**2 + 15); ok &= (not t)
    print(f"[ctrl] Q(sqrt-3) contains sqrt-15: {t} (must be False)")
    M = snappy.Manifold("m004")
    K = M.invariant_trace_field_gens().find_field(prec=600, degree=8, optimize=True)[0]
    t3, t15 = has_root(K, x**2 + 3), has_root(K, x**2 + 15)
    ok &= t3 and (not t15)
    print(f"[ctrl] m004: sqrt-3 {t3} (True), sqrt-15 {t15} (False)")
    return ok

def trace_field(p, q, sealed_deg):
    ladder = ((600, sealed_deg), (1200, sealed_deg), (2000, sealed_deg + 4),
              (3000, sealed_deg + 4), (6000, sealed_deg + 4))
    for prec, degcap in ladder:
        M = snappy.Manifold("4_1(%d,%d)" % (p, q))
        try:
            F = M.invariant_trace_field_gens().find_field(prec=prec, degree=degcap,
                                                          optimize=True)
        except Exception:
            F = None
        if F is not None:
            return F[0]
    return None

def main():
    rows = json.load(open(os.path.join(HERE, "door1_final_sealed_input.json")))
    print("B748 -- V4 completion (sealed input 77818016, prereg a59ac036)")
    if not controls():
        print("CONTROLS FAILED -- ABORT"); sys.exit(1)
    odd = [r for r in rows if r["degree"] % 2 == 1]
    even = [r for r in rows if r["degree"] % 2 == 0]
    print(f"STAGE 1 (theorem): {len(odd)} odd-degree slopes -- sqrt-15 EXCLUDED by parity")
    hits, unresolved, incons = [], [], []
    for r in even:
        p, q = (int(v) for v in r["slope"].split(","))
        K = trace_field(p, q, r["degree"])
        if K is None or int(K.degree()) != r["degree"]:
            unresolved.append(r["slope"]); print(f"  ({p},{q}) UNRESOLVED"); continue
        h15 = has_root(K, x**2 + 15)
        h3 = has_root(K, x**2 + 3)
        if h3 != bool(r["contains_sqrt_m3"]):
            incons.append(r["slope"])
        if h15:
            hits.append(r["slope"])
        print(f"  ({p},{q}) deg {K.degree()}: sqrt-15 = {h15}; sqrt-3 consistency "
              f"{h3} == sealed {r['contains_sqrt_m3']}: {h3 == bool(r['contains_sqrt_m3'])}")
    print(f"TALLY: {len(odd)} parity + {len(even)-len(hits)-len(unresolved)} exact-negative"
          f" + {len(hits)} HITS + {len(unresolved)} unresolved; consistency failures: {incons}")
    if incons:
        print("VERDICT: ABORT -- consistency failure vs B740"); sys.exit(1)
    if hits:
        print("VERDICT: MEETING-ALIVE -- hits:", hits)
    elif not unresolved:
        print("VERDICT: V4-SILENT -- 0/78 on the meeting face; the ENTIRE V4 is interface-only")
    else:
        print("VERDICT: PENDING --", unresolved)
    print("B748 SWEEP COMPLETE")

main()
