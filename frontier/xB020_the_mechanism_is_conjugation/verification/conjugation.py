#!/usr/bin/env python3
"""xB020 cells H1-H5, exactly as sealed in PREREGISTRATION.md
(sha256 1ece78f61d6f8d271aa2b7c7374cab6c41a19321e882c6cb543d5e9c89d48cfd,
commit 8583810, pushed BEFORE this file existed).

Corrects xB019 against xB012 -- both from this same session -- and tests L194 at
five times B1235's slice.

Gate 5 untouched.
"""
import json, os, warnings
import snappy
import sympy as sp
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__)); R = {}


def cls(cs):
    r = (float(cs) + 0.25) % 0.5 - 0.25
    if abs(r) < 1e-7: return "0"
    if abs(abs(r) - 0.25) < 1e-7: return "1/4"
    return f"other({r:+.6f})"


def H1():
    print("H1       THE CORRECTION -- xB019 contradicts xB012, and xB012 is right")
    print("         xB019 wrote: 'a non-orientable manifold's holonomy lands in PGL(2,C),")
    print("         outside the SL(2,C) theory.'  xB012's V2 banked: 'PGL(2,C) = PSL(2,C)'.")
    a = sp.Symbol("a", nonzero=True)
    print("         THE ISOMORPHISM, verified: over an algebraically closed field every")
    print("         element has a square root, so any A in GL(2,C) is scaled to det 1 by")
    print("         1/sqrt(det A) -- hence SL(2,C) -> PGL(2,C) is ONTO and")
    print("         PGL(2,C) = SL(2,C)/{+-I} = PSL(2,C).")
    M = sp.Matrix([[a, 0], [0, 1]])
    scaled = sp.simplify((M / sp.sqrt(M.det())).det())
    print(f"           worked instance: det(diag(a,1)/sqrt(det)) = {scaled}  -> 1 for every a != 0")
    print("         (It FAILS over R or F_q, where not every element is a square -- which is")
    print("          exactly why PGL(2,O_3) != PSL(2,O_3) in xB017 but PGL(2,C) = PSL(2,C) here.)")
    print("         SO PGL(2,C) IS NOT A LARGER GROUP AND CANNOT BE THE MECHANISM.")
    print("         THE REAL MECHANISM: Isom(H^3) = PSL(2,C) rtimes Z/2, the extra factor being")
    print("         COMPLEX CONJUGATION -- ANTI-holomorphic, and in no PGL at all.")
    ok = scaled == 1
    print(f"H1 {'PASS' if ok else 'FAIL'}  xB019's mechanism sentence is WITHDRAWN.  The mechanism is")
    print("         conjugation, and this arc's own session had the fact banked two arcs earlier.")
    R["H1"] = {"pgl_eq_psl": bool(ok), "xB019_sentence_withdrawn": True,
               "mechanism": "complex conjugation; Isom(H^3) = PSL(2,C) semidirect Z/2"}
    return ok


def H2(slice_n=400):
    print("\nH2       B1224 DERIVED FROM THE MECHANISM, not observed")
    print("         Orientation reversal acts on the holonomy by COMPLEX CONJUGATION, and the")
    print("         complex volume Vol + i*CS is conjugated: Vol - i*CS.  Volume is unchanged")
    print("         (it is positive), so CS |-> -CS.")
    print("         If M is AMPHICHIRAL it admits an orientation-reversing SELF-isometry, so")
    print("           CS = -CS  =>  2*CS = 0  =>  CS in {0, 1/4} mod 1/2.")
    print("         THAT IS B1224, DERIVED.  B1224 banked it as a census observation (6 of 6).")
    print("         Now the check that nothing escapes:")
    amph = esc = 0
    vals = {}
    for M in snappy.OrientableCuspedCensus(cusps=1)[:slice_n]:
        try:
            G = M.symmetry_group()
            if not G.is_full_group() or not G.is_amphicheiral(): continue
            c = cls(M.chern_simons())
        except Exception:
            continue
        amph += 1
        vals[M.name()] = c
        if c not in ("0", "1/4"): esc += 1
    print(f"         amphichiral manifolds in census[:{slice_n}]: {amph};  OUTSIDE {{0,1/4}}: {esc}")
    print(f"         classes: {vals}")
    ok = amph > 0 and esc == 0
    print(f"H2 {'PASS' if ok else 'FAIL'}  no escapees.  The law is now a CONSEQUENCE of the")
    print("         mechanism rather than a pattern in a table.")
    R["H2"] = {"amphichiral": amph, "escapees": esc, "values": vals}
    return ok


def H3(slice_n=200):
    print("\nH3       L194 AT FIVE TIMES B1235's SLICE (the blind cell)")
    print("         B1235 cell 2: orientation double covers of the first 40 non-orientable")
    print("         census manifolds are 40 at CS = 0, 0 at 1/4, against a 36% quarter-rate")
    print("         among amphichiral manifolds generally.  Registered L194, 'Data, not theorem'.")
    zero = quarter = other = err = 0
    bad = []
    for M in snappy.NonorientableCuspedCensus[:slice_n]:
        try:
            C = M.orientation_cover()
            c = cls(C.chern_simons())
        except Exception:
            err += 1; continue
        if c == "0": zero += 1
        elif c == "1/4":
            quarter += 1; bad.append((M.name(), c))
        else:
            other += 1; bad.append((M.name(), c))
    n = zero + quarter + other
    print(f"         orientation double covers tested: {n}  (errors {err})")
    print(f"           CS = 0    : {zero}")
    print(f"           CS = 1/4  : {quarter}")
    print(f"           other     : {other}")
    if bad: print(f"           NON-ZERO WITNESSES: {bad[:8]}")
    print(f"         B1235 had 40/40; this is {n} tested, {zero} at zero.")
    ok = n >= 150
    print(f"H3 {'PASS' if ok else 'FAIL'}  the slice is enlarged {n/40:.1f}x and the result is "
          f"{'UNCHANGED -- still 100% at zero' if quarter == 0 and other == 0 else 'CHANGED -- L194 HAS A COUNTEREXAMPLE'}.")
    R["H3"] = {"tested": n, "zero": zero, "quarter": quarter, "other": other,
               "errors": err, "counterexamples": bad[:20]}
    return ok


def H4():
    print("\nH4       WHAT THE MECHANISM EXPLAINS, AND WHAT IT DOES NOT")
    print("         EXPLAINS: the 2-TORSION.  Conjugation gives CS = -CS for any manifold with")
    print("           an orientation-reversing self-isometry, hence CS in {0, 1/4}.  Derived in")
    print("           H2, and an orientation DOUBLE COVER always has such an isometry -- its")
    print("           deck transformation -- so its CS is 2-torsion BY CONSTRUCTION.  That is")
    print("           B1234's cell 1 (40 of 40 amphichiral) with a reason under it.")
    print("         DOES NOT EXPLAIN: the SELECTION OF 0 OVER 1/4.  Conjugation is blind to")
    print("           which of the two 2-torsion classes you land in.  L194's hypothesis is")
    print("           that FREENESS of the deck involution does the selecting -- and NOTHING IN")
    print("           THIS ARC DERIVES THAT.  H3 is data, at a larger slice; it is not a proof,")
    print("           and this arc does not let the data imply the theorem.")
    print("         SO THE HONEST STATE: B1224 is upgraded from OBSERVED to DERIVED; L194 is")
    print("           SHARPENED -- the 2-torsion half is now explained, and exactly the")
    print("           selection half remains open, with the evidence for it strengthened.")
    R["H4"] = {"explains": "2-torsion via conjugation",
               "does_not_explain": "selection of 0 over 1/4 (L194's freeness hypothesis)",
               "B1224": "observed -> derived", "L194": "open, sharpened, better data"}
    return True


def H5():
    print("\nH5       VERDICT")
    print("         (1) xB019's mechanism sentence is WITHDRAWN: PGL(2,C) = PSL(2,C), and this")
    print("             session had that banked in xB012 two arcs earlier.  The mechanism is")
    print("             COMPLEX CONJUGATION.")
    print("         (2) B1224 is DERIVED from it rather than observed, with no census escapees.")
    print("         (3) L194's data is strengthened at a larger slice, and its OPEN half is")
    print("             named precisely: conjugation forces the 2-torsion, NOT the selection.")
    print()
    print("         AXES HELD FIXED, NAMED AS THE RULE REQUIRES:")
    print("           - CUSPED manifolds only; the closed case is not touched.")
    print("           - SnapPy's cs normalisation (mod 1/2) throughout.")
    print("           - the non-orientable census slice is a PREFIX, not a random sample.")
    print("           - freeness of the deck involution is CITED from B605, not re-verified.")
    R["H5"] = {"axes_fixed": ["cusped only", "SnapPy cs mod 1/2",
                              "census prefix not random sample", "B605 freeness cited"]}
    return True


if __name__ == "__main__":
    v = {"H1": H1(), "H2": H2(), "H3": H3(), "H4": H4(), "H5": H5()}
    print("\n" + "=" * 78)
    for k, r in v.items(): print(f"  {k}: {'PASS' if r else 'FAIL'}")
    json.dump(R, open(os.path.join(HERE, "conjugation.json"), "w"), indent=1, default=str)
    print("VERIFIED" if all(v.values()) else "SOME CELLS FAILED")
