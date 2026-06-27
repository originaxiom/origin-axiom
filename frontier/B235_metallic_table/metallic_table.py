"""B235 -- the metallic family table (L49, the paper's section-4 backbone) + the L47 trace-1-ladder
closure + the F4 footprint correction (H24). From the chat1/chat2 handoff follow-ups. Nothing to CLAIMS.md.

(1) L49 -- one clean artifact for m=1..6: minimal model, central charge, SUSY, trace field, McKay match
    (with the B234 field-vs-group distinction), Seifert dual, |H1|. Collects scattered B-results
    (B204/B218/B224/B227/B228/B231/B234).
(2) L47 -- the Q(sqrt-7) probe RESOLVED: CLOSED. SnapPy (l47_snappy_probe.py, sage-python) finds every
    cover of 4_1 up to degree 6 has invariant trace field Q(sqrt-3) -- because 4_1 is ARITHMETIC
    (Bianchi group PSL(2,O_3)), covers don't enlarge the invariant trace field. And ALGEBRAICALLY the
    trace-1 ladder disc=1-4det is realized only at the two UNIT determinants det in {+1 (holonomy/SL2C ->
    sqrt-3), -1 (homological monodromy/GL(2,Z) -> sqrt5)}; the sqrt-7 rung needs det=2 (non-unimodular),
    which neither structure provides. So the ladder CLOSES at {sqrt5, sqrt-3}, with a reason (unimodularity
    + arithmeticity), NOT generative.
(3) H24 CORRECTED -- the exceptional footprint is 3/5 (G2, E6, E8), not 4/5: there is NO conformal
    embedding SU(3)_k in (F4)_1 for any integer k (c(SU(3)_k)=8k/(k+3) never equals c((F4)_1)=26/5), so
    the SU(3)2->F4 route is void. (The genuine F4 fact is the generic (G2)_1 x (F4)_1 in (E8)_1, c=8 --
    not object-specific.) Retracts chat1 D3's F4 line.

Run: python metallic_table.py (pyenv). The SnapPy probe is l47_snappy_probe.py (sage-python).
"""
from fractions import Fraction as Fr
from sympy import factorint, isprime


def squarefree_part(d):
    sf = 1
    for p, e in factorint(d).items():
        if e % 2 == 1:
            sf *= p
    return sf


def c_minimal(q):
    """unitary minimal model M(q,q+1): c = 1 - 6/(q(q+1))."""
    return Fr(1) - Fr(6, q * (q + 1))


def mckay_match(sf, n):
    """trace field Q(sqrt sf): which binary McKay group, and does the GROUP close (B234 field-vs-group)?"""
    if sf == 5:
        grp = "2I=E8"
        closes = isprime(n) and n == 5            # the congruence GROUP SL(2,F5)=2I only when n=5 prime
        return f"{grp} ({'GROUP+field' if closes else 'field only'})"
    if sf == 2:
        return "2O=E7 (field only -- no group; the field golden excludes)"
    return "none"


def metallic_row(m):
    n = m * m + 4
    q = m * m + 3
    sf = squarefree_part(n)
    return {
        "m": m,
        "n": n,                                   # metallic discriminant
        "minimal_model": f"M({q},{n})",
        "c": c_minimal(q),
        "susy": (q == 4),                         # = TCI (the unique ordinary&super model) only at m=1
        "trace_field": f"Q(sqrt{sf})",
        "mckay": mckay_match(sf, n),
        "seifert_dual": f"S^2({n},{q},3)",        # B227 ordinary Seifert dual
        "H1": (2 * m * m + 7) ** 2 + 2,           # |H1| = 4m^4+28m^2+51 = (2m^2+7)^2+2 (B227)
    }


def trace1_ladder_closure():
    """the L47 algebraic closure: disc=1-4det at the unit determinants det in {+1,-1} gives exactly
    {-3 (geometry), +5 (monodromy)}; det=2 (-> -7) is non-unimodular, absent from the object."""
    return {det: 1 - 4 * det for det in (-1, 1, 2)}   # -1->5, +1->-3, 2->-7 (the unreachable rung)


def f4_no_conformal_embedding():
    """H24: no integer k has c(SU(3)_k)=8k/(k+3) equal to c((F4)_1)=26/5."""
    c_F4 = Fr(52, 1 + 9)                          # (F4)_1: 1*dim/(1+hdual)=52/10
    sols = [k for k in range(1, 200) if Fr(8 * k, k + 3) == c_F4]
    return c_F4, sols


if __name__ == "__main__":
    print("=" * 100)
    print("B235  (1) L49 -- THE METALLIC FAMILY TABLE  (m=1..6)")
    print("=" * 100)
    hdr = f"{'m':>2} {'n':>4} {'minimal model':>14} {'c':>9} {'SUSY':>5} {'trace fld':>10} {'McKay match':>40} {'Seifert':>13} {'|H1|':>7}"
    print(hdr)
    rows = [metallic_row(m) for m in range(1, 7)]
    for r in rows:
        print(f"{r['m']:>2} {r['n']:>4} {r['minimal_model']:>14} {str(r['c']):>9} "
              f"{str(r['susy']):>5} {r['trace_field']:>10} {r['mckay']:>40} {r['seifert_dual']:>13} {r['H1']:>7}")
    # locks on the headline cells
    assert rows[0]["c"] == Fr(7, 10) and rows[0]["susy"] and rows[0]["mckay"].startswith("2I=E8 (GROUP")
    assert rows[1]["c"] == Fr(25, 28) and (not rows[1]["susy"]) and "2O=E7" in rows[1]["mckay"]
    assert rows[3]["trace_field"] == "Q(sqrt5)" and "field only" in rows[3]["mckay"]   # m=4: E8 field, no group
    assert [r["m"] for r in rows if r["susy"]] == [1]
    assert rows[0]["H1"] == 83                                                          # B227/B229 cross-check

    print("\n" + "=" * 100)
    print("B235  (2) L47 -- the Q(sqrt-7) probe: CLOSED")
    print("=" * 100)
    lad = trace1_ladder_closure()
    print(f"  trace-1 ladder disc=1-4det:  det=-1 -> {lad[-1]} (Q(sqrt5), monodromy/GL(2,Z));"
          f"  det=+1 -> {lad[1]} (Q(sqrt-3), holonomy/SL(2,C));  det=2 -> {lad[2]} (Q(sqrt-7))")
    print("  the object's elements are UNIMODULAR (det in {+1,-1}) => only {5,-3} realized; det=2 absent.")
    print("  SnapPy (l47_snappy_probe.py): every cover of 4_1 up to degree 6 has invariant trace field")
    print("  Q(sqrt-3) (4_1 is ARITHMETIC, Bianchi PSL(2,O_3)) -> sqrt-7 does NOT appear.")
    print("  VERDICT: the trace-1 ladder CLOSES at {sqrt5, sqrt-3} (reason: unimodularity + arithmeticity),")
    print("           NOT generative. (chat2's 'closure is itself a fact' -> explained.)")
    assert lad[-1] == 5 and lad[1] == -3 and lad[2] == -7

    print("\n" + "=" * 100)
    print("B235  (3) H24 CORRECTED -- exceptional footprint is 3/5, not 4/5 (F4 retracted)")
    print("=" * 100)
    c_F4, sols = f4_no_conformal_embedding()
    print(f"  c((F4)_1) = {c_F4};  integer k with c(SU(3)_k)==c((F4)_1): {sols or 'NONE'}")
    print("  => NO conformal embedding SU(3)_k in (F4)_1 for any integer k => the SU(3)2->F4 route is VOID.")
    print("  exceptional-group footprint = 3/5: G2 (Fibonacci=(G2)_1), E6 (Q(sqrt-3)), E8 (Q(sqrt5)); E7 excluded;")
    print("  F4 RETRACTED. (The genuine F4 fact (G2)_1 x (F4)_1 in (E8)_1 [c=8] is generic CFT, not object-specific.)")
    assert sols == []

    print("\nALL CHECKS PASS")
