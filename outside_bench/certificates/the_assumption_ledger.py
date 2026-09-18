#!/usr/bin/env python3
"""THE ASSUMPTION LEDGER -- compute the computable necessary conditions.

Seal: outside_bench/seals/THE_ASSUMPTION_LEDGER_PREREG.md
      sha256 3fd9117e0da47d50c0cda3db9ff420d60c0625c53d2e8e314a30ca8a8d519fd0
      committed e657e0d8 BEFORE this file was written.

THE FENCE, repeated here because it is the one overreach this cell exists to
avoid: A FAILED NECESSARY CONDITION CLOSES THE ROUTE FOR THAT OBJECT, NEVER
THE ROUTE ITSELF.  Any sentence of the form "the G2 route is closed" is
forbidden output.
"""
from __future__ import annotations
import snappy

CANDIDATES = [
    ("m004",    "the object"),
    ("m003",    "the sister"),
    ("m202",    "cell 8: scores 4/4"),
    ("s959",    "cell 8: scores 4/4"),
    ("v2873",   "B1330 best-case"),
    ("t12833",  "B1330 best-case"),
    ("t12835",  "B1330 best-case"),
]


def rule(t):
    print("\n" + "-" * 78); print(" " + t); print("-" * 78)


def betti(M):
    return M.homology().betti_number()


def main():
    ok = {}

    rule("CONTROL K1 -- the banked value must reproduce on the rebuilt environment")
    M = snappy.Manifold("m004")
    C = M.covers(3, cover_type="cyclic")[0].copy(); C.dehn_fill((1, 0), 0)
    h, v, b = C.homology(), float(C.volume()), betti(C)
    print(f"  Y_3 = filled 3-fold cyclic cover of m004")
    print(f"    H_1 = {h}   b_1 = {b}   volume = {v:.3e}")
    print(f"    banked (three independent routes: Smith form on F(2,6); the")
    print(f"    Alexander module; SnapPy's filled cover): H_1 = Z/4 + Z/4, b_1 = 0")
    ok["K1 -- b_1(Y_3) = 0 reproduces"] = (b == 0 and str(h).replace(" ", "") == "Z/4+Z/4")

    rule("CONTROL K2 -- the routine must be able to RETURN b_1 > 0 (memo 164)")
    pos = []
    for nm in ["m003", "m125", "m129"]:
        A = snappy.Manifold(nm); pos.append((nm, betti(A), str(A.homology())))
        print(f"    {nm}: b_1 = {pos[-1][1]}   H_1 = {pos[-1][2]}")
    ok["K2 -- routine returns b_1 > 0 somewhere"] = any(p[1] > 0 for p in pos)

    rule("CONTROL K4 -- POPULATION, printed before any verdict")
    print(f"  candidates: {len(CANDIDATES)}, named individually:")
    for nm, why in CANDIDATES:
        try:
            A = snappy.Manifold(nm)
            print(f"    {nm:<8s} cusps={A.num_cusps()}  vol={float(A.volume()):.6f}  "
                  f"H_1={A.homology()}   [{why}]")
        except Exception as e:
            print(f"    {nm:<8s} LOAD ERROR {type(e).__name__} [{why}]")
    ok["K4 -- population printed first"] = True

    # ---------------------------------------------------------------- A4 / A8
    rule("A4 + A8 -- b_1(Q) and the deck-Z/3 structure, per candidate")
    print("  A4: Joyce-Karigiannis resolution needs a nowhere-vanishing harmonic")
    print("      1-form on the singular locus, i.e. b_1(Q) > 0.")
    print("  FRAME: the construction needs a KNOT COMPLEMENT IN S^3 (H_1 = Z)")
    print("      -- see the note in the source; testing only the cusp count")
    print("      produced an artifact on the first run.")
    print("  A8: the deck Z/3 of the branched cover -- its fixed set is the")
    print("      preimage of the branch locus, hence NOT free where that is")
    print("      nonempty; reported, not assumed.")
    print()
    rows = []
    for nm, why in CANDIDATES:
        try:
            A = snappy.Manifold(nm)
        except Exception as e:
            rows.append((nm, "LOAD-ERROR", "-", "-", "-")); continue
        ncusp = A.num_cusps()
        h1 = str(A.homology()).replace(" ", "")
        # THE FRAME CONDITION, and the one this cell first got wrong.
        # B1273's construction is: Y_3 = the 3-fold CYCLIC BRANCHED COVER OF
        # S^3 ALONG THE KNOT, obtained by filling the LIFTED MERIDIAN (1,0).
        # That needs the manifold to be a knot complement in S^3, i.e.
        # H_1 = Z EXACTLY.  With torsion or extra rank there is still a map
        # to Z/3 and a cover exists, but the ambient is not S^3 and (1,0) is
        # not canonically the meridian -- so the filling is a CHOICE, not the
        # construction.  A first run of this cell tested only the cusp count,
        # applied (1,0) anyway, and produced b_1 = 2 for v2873 and b_1 = 3
        # for t12835 -- an artifact.  t12833 came back with NEGATIVE VOLUME
        # (-1.37e-05), the numerical signature of the degeneracy, which is
        # what exposed it.
        if h1 != "Z":
            rows.append((nm, "FRAME-DOES-NOT-REACH", f"H_1={A.homology()}",
                         "not a knot complement in S^3; (1,0) is not the "
                         "lifted meridian", "-"))
            continue
        covs = A.covers(3, cover_type="cyclic")
        if not covs:
            rows.append((nm, "FRAME-DOES-NOT-REACH", f"{ncusp} cusps",
                         "no 3-fold cyclic cover", "-"))
            continue
        if ncusp != 1:
            # the branched-cover construction along "the knot" is not defined
            # for a multi-cusped manifold; report rather than substitute.
            rows.append((nm, "FRAME-DOES-NOT-REACH", f"{ncusp} cusps",
                         f"{len(covs)} cyclic cover(s); branched cover along a"
                         f" knot undefined", "-"))
            continue
        best = None
        for Cv in covs:
            D = Cv.copy()
            if D.num_cusps() != 1:
                continue
            D.dehn_fill((1, 0), 0)
            best = (str(D.homology()), betti(D), float(D.volume()))
            break
        if best is None:
            rows.append((nm, "FRAME-DOES-NOT-REACH", f"{ncusp} cusps",
                         "cover is multi-cusped; fill ambiguous", "-"))
        else:
            H1, b1, vol = best
            rows.append((nm, "COMPUTED", f"H_1={H1}", f"b_1={b1}",
                         f"vol={vol:.3e}"))

    w = max(len(r[0]) for r in rows)
    for r in rows:
        print(f"  {r[0]:<{w}s}  {r[1]:<22s} {r[2]:<28s} {r[3]:<34s} {r[4]}")

    reached = [r for r in rows if r[1] == "COMPUTED"]
    unreached = [r for r in rows if r[1] == "FRAME-DOES-NOT-REACH"]
    print(f"\n  frame REACHES {len(reached)} of {len(CANDIDATES)}; "
          f"does NOT reach {len(unreached)}")
    ok["A4 -- at least one candidate reached"] = len(reached) >= 1

    # ---------------------------------------------------------------- verdict
    rule("CONTROLS")
    for k, v_ in ok.items():
        print(f"  {'PASS' if v_ else 'FAIL'}   {k}")

    rule("THE OUTCOME")
    passA4 = [r for r in reached if r[3] != "b_1=0"]
    failA4 = [r for r in reached if r[3] == "b_1=0"]
    print(f"  A4 (b_1(Q) > 0) HOLDS for: {[r[0] for r in passA4] or 'NONE'}")
    print(f"  A4 FAILS  (b_1(Q) = 0) for: {[r[0] for r in failA4] or 'NONE'}")
    print(f"  frame does not reach:      {[r[0] for r in unreached] or 'NONE'}")
    m004_fails = any(r[0] == "m004" for r in failA4)
    alt_holds = [r[0] for r in passA4 if r[0] != "m004"]
    if m004_fails and alt_holds:
        out = "A"
    elif reached and not passA4:
        out = "B"
    elif not m004_fails:
        out = "C"
    else:
        out = "indeterminate"
    print(f"\n  -> OUTCOME {out}")
    print("""
  THE FENCE, and it governs how every line above may be read:
  A FAILED NECESSARY CONDITION CLOSES THE ROUTE FOR THAT OBJECT, NEVER THE
  ROUTE ITSELF.  b_1(Q) = 0 says JOYCE-KARIGIANNIS CANNOT RESOLVE THAT
  LOCUS.  It says nothing about whether some other construction can, and
  nothing about the G2 route as such.

  A6 -- the sum rule's b_2(X) >= 2 with the Z/3 moving the harmonic forms --
  IS NOT COMPUTED HERE AND CANNOT BE: it lives on X, which is not
  constructed.  That is the honest residue of the decomposition.

  I-26 remains UNEARNED; no generation count is licensed.  No value.""")
    print()
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
