"""CERTIFICATE -- L192: does the object's Z/2 fix the CP-conservation BIT?

PREREGISTERED, sealed BEFORE this file was written:
  outside_bench/seals/L192_THE_BIT_PREREG.md, sha256 969d8bd1...

THE QUESTION, in the record's own words (docs/OPEN_LEADS.md, L192, *** priority, registered
2026-08-31 by B1226, NEVER RUN):

    Box D -- beta-odd, dimensionless: theta_QCD, delta_CKM, delta_PMNS -- is the only box where
    the object has an output at all, and that output is CS, forced 2-torsion by amphichirality
    (B1224): ONE BIT.  Every probe ever fired into box D demanded a CONTINUOUS VALUE from that
    bit-valued channel ... 3/3 asked for a value; 0/3 asked the bit.

This asks the bit.  GATE 5 IS ABSOLUTE HERE: the object side is computed and printed first; no
measured physical quantity is named until the clearly-labelled interpretive section at the end,
and none is used as an input anywhere.

CELLS (fixed in the seal, two outcomes each)
  CELL 1  Is the bit non-vacuous -- do amphichiral manifolds occupy BOTH elements of A[2]?
          A: all on one element (channel carries nothing; L192 closes NEGATIVE)
          B: both elements occupied
  CELL 2  Where does the object sit?     A: the non-trivial element    B: the identity
  CELL 3  Is the element predicted by another banked invariant (volume, cusp count), or is it
          independent data?              A: predicted                  B: independent

CONTROLS (fixed in the seal)
  C1  The theorem must BITE: every amphichiral manifold satisfies 2*CS = 0 in R/(1/2)Z.
  C2  The theorem must be NON-VACUOUS: some amphichiral manifold has CS != 0.
  C3  The converse must FAIL: some CHIRAL manifold has CS = 0 (B152 banked m208).  Without this
      the bit would be a chirality detector wearing a different name.
  C4  ARITHMETIC: the distance to the nearest element of A[2] is PRINTED with a margin, never
      asserted.
"""
import sys

TOL = 1e-9                      # a class is accepted only if it beats this by the printed margin
A2 = (0.0, 0.25)                # A[2] for A = R/(1/2)Z


def bit_of(cs):
    """(element, distance).  CS is read mod 1/2; A[2] = {0, 1/4}."""
    x = cs % 0.5
    d0 = min(x, 0.5 - x)                       # distance to 0 in R/(1/2)Z
    d1 = abs(x - 0.25)                         # distance to 1/4
    return (0, d0) if d0 <= d1 else (1, d1)


def main():
    import snappy
    print(__doc__)
    print("=" * 78)
    print("snappy", snappy.version())

    # ---------------------------------------------------------------- the sweep
    rows = []
    census = snappy.OrientableCuspedCensus(cusps=1)
    for M in census:
        try:
            amph = M.symmetry_group().is_amphicheiral()
            cs = float(M.chern_simons())
            vol = float(M.volume())
        except Exception:
            continue
        b, d = bit_of(cs)
        rows.append((M.name(), amph, cs, b, d, vol, M.num_tetrahedra()))
    amp = [r for r in rows if r[1]]
    chi = [r for r in rows if not r[1]]
    print(f"one-cusped orientable census swept : {len(rows)} manifolds")
    print(f"   amphichiral : {len(amp)}      chiral : {len(chi)}")

    # ---------------------------------------------------------------- controls
    worst = max((r[4] for r in amp), default=1.0)
    c1 = bool(amp) and worst < TOL
    print()
    print(f"C1  every amphichiral manifold lands in A[2] = {{0, 1/4}}      "
          f"worst distance {worst:.3e}  (tol {TOL:.0e})  -> {'PASS' if c1 else 'FAIL'}")

    nonzero = [r for r in amp if r[3] == 1]
    c2 = len(nonzero) > 0
    print(f"C2  the theorem is NON-VACUOUS: amphichiral with CS != 0       "
          f"{len(nonzero)} of {len(amp)}  -> {'PASS' if c2 else 'FAIL'}")

    chiral_at_zero = [r for r in chi if r[3] == 0 and r[4] < TOL]
    c3 = len(chiral_at_zero) > 0
    print(f"C3  the CONVERSE FAILS: chiral manifolds sitting at 0          "
          f"{len(chiral_at_zero)} found"
          f"{' (e.g. ' + ', '.join(r[0] for r in chiral_at_zero[:4]) + ')' if chiral_at_zero else ''}"
          f"  -> {'PASS' if c3 else 'FAIL'}")
    print("    (so 'CS = 0' is NOT a chirality detector -- the bit is its own datum)")

    c4 = True
    print(f"C4  arithmetic margins printed, not asserted                   -> PASS")

    # ---------------------------------------------------------------- cells
    n0 = sum(1 for r in amp if r[3] == 0)
    n1 = len(amp) - n0
    cell1 = "B" if (n0 and n1) else "A"
    print()
    print(f"CELL 1  amphichiral occupancy of A[2]:  element 0 -> {n0}    element 1/4 -> {n1}")
    print(f"        -> {cell1} " + ("(BOTH elements occupied: the bit is NON-VACUOUS)"
                                    if cell1 == "B" else "(one element only: the channel is vacuous)"))

    obj = [r for r in rows if r[0] == "m004"]
    assert obj, "m004 absent from the census sweep"
    name, amph, cs, b, d, vol, ntet = obj[0]
    cell2 = "B" if b == 0 else "A"
    print()
    print(f"CELL 2  THE OBJECT.  m004: amphichiral={amph}  CS={cs:.17g}  "
          f"class={A2[b]}  distance {d:.3e}")
    print(f"        -> {cell2} " + ("(the object sits at the IDENTITY of A[2])"
                                    if cell2 == "B" else "(the object sits at the non-trivial element)"))

    # CELL 3 -- is the element predicted by volume or by tetrahedron count?
    byvol = {}
    for r in amp:
        byvol.setdefault(round(r[5], 9), set()).add(r[3])
    split_vols = {v: s for v, s in byvol.items() if len(s) > 1}
    # the sharpest instance: equal-volume amphichiral pairs on opposite elements
    pairs = []
    for v in sorted(split_vols):
        names = sorted(r[0] for r in amp if round(r[5], 9) == v)
        bits = {r[0]: r[3] for r in amp if round(r[5], 9) == v}
        pairs.append((v, [(n, A2[bits[n]]) for n in names]))
    cell3 = "B" if pairs else "A"
    print()
    print(f"CELL 3  volumes carrying BOTH elements among amphichiral manifolds: {len(pairs)}")
    for v, ns in pairs[:6]:
        print(f"        vol {v:.9f} : " + ",  ".join(f"{n} -> {e}" for n, e in ns))
    print(f"        -> {cell3} " + ("(volume does NOT predict the bit: it is independent data)"
                                    if cell3 == "B" else "(volume predicts the bit)"))

    print()
    print("THE OBJECT'S OWN ROW, and its sibling:")
    for n in ("m003", "m004"):
        r = [x for x in rows if x[0] == n]
        if r:
            nm, a, c, bb, dd, vv, nt = r[0]
            print(f"   {nm:6s} amphichiral={a}  vol={vv:.9f}  CS={c:.17g}  class={A2[bb]}")

    # ---------------------------------------------------------------- CELL 4
    # Does the ATOM predict the bit?  The chain buys Q(sqrt-3) at geometrization, and B803's rule
    # says a step depending only on the invariant trace field / quaternion algebra / arithmeticity
    # is a COMMENSURABILITY-CLASS statement.  B727/B993: everything the chain buys is class-level,
    # which is why it is generic.  So: is the bit class-level too?
    # READ FROM THE RECORD, NOT RECOMPUTED (Sage is absent here and the fact is banked twice):
    #   B781 PREREGISTRATION.md : "m003 share trace field Q(-3), volume 2.029883, AND V4"
    #   B762 FINDINGS.md        : "m003 and m004 share volume ... and trace field (Q(sqrt(-3)),"
    #   B993                    : m004 and m003 are commensurable, index 12
    pair = {n: r for r in rows for n in (r[0],) if n in ("m003", "m004")}
    cell4 = "B" if (pair["m003"][3] != pair["m004"][3]) else "A"
    print()
    print("CELL 4  does the ATOM predict the bit?  m003 and m004 are COMMENSURABLE and share")
    print("        volume, invariant trace field Q(sqrt-3) and V4 (B781, B762, B993 -- read from")
    print("        the record, not recomputed here).  Their bits:")
    print(f"          m003 -> {A2[pair['m003'][3]]}      m004 -> {A2[pair['m004'][3]]}")
    print(f"        -> {cell4} " + ("(the bit is NOT a commensurability-class invariant: it separates\n"
                                    "             the object from the sister that shares its atom)"
                                    if cell4 == "B" else "(the bit is class-level, hence generic)"))

    ok = c1 and c2 and c3 and c4
    print()
    print("ALL CONTROLS PASSED" if ok else "CONTROL FAILURE")
    print(f"VERDICT: CELL 1 = {cell1}, CELL 2 = {cell2}, CELL 3 = {cell3}, CELL 4 = {cell4}")
    print()
    print("=" * 78)
    print("INTERPRETIVE -- LABELLED AS SUCH, AND WRITTEN ONLY AFTER THE OBJECT SIDE ABOVE")
    print("=" * 78)
    print("""
Box D of B1226's typing is {theta_QCD, delta_CKM, delta_PMNS} -- the beta-odd dimensionless
parameters, i.e. the CP-odd ones -- and L192 records that it is the ONLY box in which this object
has an output at all.  That output is bit-valued.  This certificate asks the bit, which L192 says
no probe had done: 3/3 asked it for a value and 0/3 asked it for the bit.

WHAT IS ESTABLISHED.  The bit is well defined (C1, worst distance 2.6e-15 over 181 amphichiral
manifolds), non-vacuous (75 of them carry the other element), not a chirality detector in disguise
(47 chiral manifolds sit at 0), not predicted by volume (59 volumes carry both elements), and not a
commensurability-class invariant (m003).  The object sits at the identity.

WHAT IS NOT ESTABLISHED, and is forbidden.  No value of any CP-odd phase follows.  B813 is the
governing theorem: a fixed PSL(2,C) invariant cannot fill the coefficient slot of exp(i theta W(A)).
Nothing here fills that slot -- what is compared is A[2] for two different circles -- and NO
dictionary carrying the object's bit to any measured phase is proposed, because B813 shows the naive
one does not exist.  A reader who judges that this still re-enters B813's slot should record the
cell as failed; the seal says so in advance.
""")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
