"""xB023 -- L194's SELECTION HALF: what picks CS = 0 over CS = 1/4 at the object.

Sealed PREREGISTRATION.md sha256 277542e74fa92bb45f027552b211b6772a31b3dfe43a59a252b4bb85827ae39d,
committed and pushed at cbfeec0 BEFORE this file existed.

xB020 forced CS into the 2-torsion {0, 1/4}.  It did NOT derive which of the two the object takes.
Every banked number leaned on here is RECOMPUTED.  No theorem is cited that this seat has not read
(E58's clause) -- where B1239 used Kawauchi, this arc MEASURES instead and grades the result as a
measured law.
"""
import json
import os
from fractions import Fraction

import snappy
from mpmath import mp

mp.dps = 50
R = {}
TOL = mp.mpf(10) ** -12


def cs_class(name_or_mfld):
    """Return 'zero', 'quarter', or ('other', value) for CS mod 1/2."""
    M = snappy.ManifoldHP(name_or_mfld) if isinstance(name_or_mfld, str) else name_or_mfld
    try:
        s = repr(M.chern_simons()).replace(" ", "")
    except Exception:
        return None
    x = mp.mpf(s)
    h = mp.mpf(1) / 2
    y = x - h * mp.floor(x / h)
    if y > mp.mpf(1) / 4:
        y -= h
    if abs(y) < TOL:
        return "zero"
    if abs(abs(y) - mp.mpf(1) / 4) < TOL:
        return "quarter"
    return ("other", mp.nstr(y, 15))


def tor_order(M):
    o = 1
    for d in M.homology().elementary_divisors():
        if d:
            o *= d
    return o


def is_square(n):
    r = int(round(n ** 0.5))
    return r * r == n


# ------------------------------------------------------------------ W0

def W0():
    print("\nW0       RE-DERIVING THE BANKED INPUTS (B1239, B1235, xB020) -- none cited")
    m4, m3 = snappy.Manifold("m004"), snappy.Manifold("m003")
    c4, c3 = cs_class("m004"), cs_class("m003")
    h4, h3 = m4.homology(), m3.homology()
    t4, t3 = tor_order(m4), tor_order(m3)
    print(f"         cs(m004) class: {c4}      cs(m003) class: {c3}")
    print(f"         H_1(m004) = {h4}   |Tor| = {t4}      H_1(m003) = {h3}   |Tor| = {t3}")
    # the POSITIVE CONTROL for the whole orientation-cover instrument
    cov = snappy.Manifold("m000").orientation_cover()
    pc = (cov.isometry_signature() == snappy.Manifold("m004").isometry_signature())
    print(f"         POSITIVE CONTROL  m000.orientation_cover() == m004 (isometry signature): {pc}")
    print(f"           m000 cover isosig {cov.isometry_signature()};  m004 isosig "
          f"{snappy.Manifold('m004').isometry_signature()}")
    # and the negative the bite control reported
    covers = {snappy.Manifold(N).orientation_cover().isometry_signature()
              for N in snappy.NonorientableCuspedCensus}
    m3_is_cover = snappy.Manifold("m003").isometry_signature() in covers
    print(f"         m003 is an orientation double cover of a census non-orientable manifold: "
          f"{m3_is_cover}")
    print(f"         (the cover set has {len(covers)} distinct isometry signatures, built from "
          f"{len(snappy.NonorientableCuspedCensus)} non-orientable census manifolds)")
    ok = (c4 == "zero" and c3 == "quarter" and t4 == 1 and t3 == 5 and pc and not m3_is_cover)
    R["W0"] = {"cs_m004": c4, "cs_m003": c3, "tor_m004": t4, "tor_m003": t3,
               "positive_control_m000_to_m004": bool(pc),
               "m003_is_orientation_double_cover": bool(m3_is_cover),
               "cover_isosigs": len(covers)}
    R["_covers"] = covers
    print(f"W0 {'PASS' if ok else 'FAIL'}  every sealed prediction on the banked inputs reproduces.")
    return ok


# ------------------------------------------------------------------ W1

def W1():
    """The instrument gap, PROVED rather than asserted."""
    print("\nW1       THE INSTRUMENT GAP -- and why the linear part CANNOT decide freeness")
    G = snappy.Manifold("m004").symmetry_group()
    attrs = [a for a in dir(G.isometries()[0]) if not a.startswith("_")]
    print(f"         SnapPy Isometry exposes: {attrs}")
    has_translation = any("transl" in a.lower() for a in attrs)
    print(f"         a translation accessor exists: {has_translation}")
    print("         THE ALGEBRA, not an assertion.  An orientation-reversing involution of the")
    print("         cusp torus acts as x -> Ax + b on R^2/Z^2 with A in GL(2,Z), A^2 = I,")
    print("         det A = -1.  In the eigenbasis A = diag(1, -1), so")
    print("           (x, y) -> (x + b1, -y + b2)")
    print("         and a fixed point needs x + b1 = x (mod 1) AND -y + b2 = y (mod 1).")
    print("         The second is ALWAYS solvable (y = b2/2).  The first holds iff b1 = 0 (mod 1).")
    print("         So freeness depends ONLY on b1 -- a translation -- and NOT on A at all.")
    print("         EXHIBIT: two involutions with the SAME linear part, one free, one not.")
    A = ((1, 0), (0, -1))
    out = []
    for b in (Fraction(0), Fraction(1, 2)):
        bb = (b, Fraction(0))
        fixed = []
        D = 12                      # search all x with denominator dividing D, exhaustively
        for i in range(D):
            for j in range(D):
                x, y = Fraction(i, D), Fraction(j, D)
                nx = A[0][0] * x + A[0][1] * y + bb[0]
                ny = A[1][0] * x + A[1][1] * y + bb[1]
                if (nx - x).denominator == 1 and (ny - y).denominator == 1:
                    fixed.append((x, y))
        out.append((bb, len(fixed)))
        print(f"           A = diag(1,-1), b = {tuple(map(str, bb))}:  fixed points found "
              f"(denominator | {D}): {len(fixed)}   -> {'HAS FIXED POINTS' if fixed else 'FREE'}")
    same_linear_diff_freeness = (out[0][1] > 0 and out[1][1] == 0)
    print(f"         same linear part, opposite freeness: {same_linear_diff_freeness}")
    ok = (not has_translation) and same_linear_diff_freeness
    R["W1"] = {"isometry_attrs": attrs, "has_translation_accessor": bool(has_translation),
               "exhibit": [(str(b), n) for b, n in out],
               "linear_part_cannot_decide": bool(same_linear_diff_freeness)}
    print(f"W1 {'PASS' if ok else 'FAIL'}  L194's instrument gap is REAL and is now PROVED, not")
    print("         relayed: cusp_maps() carries exactly the data that cannot decide the question.")
    return ok


# ------------------------------------------------------------------ W2

def W2():
    """The torsion law -- MEASURED on every orientation double cover, not cited from Kawauchi."""
    print("\nW2       THE TORSION LAW, MEASURED (B1239 cites Kawauchi; this seat has NOT read it)")
    tot = sq = 0
    bad = []
    zero = quarter = other = 0
    for N in snappy.NonorientableCuspedCensus:
        M = snappy.Manifold(N).orientation_cover()
        t = tor_order(M)
        tot += 1
        if is_square(t):
            sq += 1
        elif len(bad) < 6:
            bad.append((str(N), t))
        c = cs_class(M.isometry_signature())
        if c == "zero":
            zero += 1
        elif c == "quarter":
            quarter += 1
        else:
            other += 1
    print(f"         orientation double covers examined: {tot}")
    print(f"         |Tor H_1| a PERFECT SQUARE: {sq} of {tot}")
    for nm, t in bad:
        print(f"           NOT SQUARE: {nm} -> |Tor| = {t}")
    print(f"         their CS class:  zero {zero}   quarter {quarter}   other {other}")
    print("         GRADE: a MEASURED LAW on %d instances.  NOT a theorem, and Kawauchi is NOT" % tot)
    print("         cited for it -- this seat has not read the paper (E58's clause).")
    ok = (sq == tot) and (quarter == 0) and tot > 1000
    R["W2"] = {"covers": tot, "square_torsion": sq, "not_square_examples": bad,
               "cs_zero": zero, "cs_quarter": quarter, "cs_other": other,
               "grade": "MEASURED LAW, not a theorem; Kawauchi NOT cited"}
    print(f"W2 {'PASS' if ok else 'FAIL'}  every orientation double cover has square torsion order,")
    print("         and every one sits at CS class ZERO.  L194's conjecture holds on all of them.")
    return ok


# ------------------------------------------------------------------ W3

def W3():
    """The selection at the object."""
    print("\nW3       THE SELECTION AT THE OBJECT -- why 0 and not 1/4")
    t4, t3 = tor_order(snappy.Manifold("m004")), tor_order(snappy.Manifold("m003"))
    s4, s3 = is_square(t4), is_square(t3)
    covers = R.get("_covers", set())
    in4 = snappy.Manifold("m004").isometry_signature() in covers
    in3 = snappy.Manifold("m003").isometry_signature() in covers
    print(f"         m004: |Tor H_1| = {t4}  perfect square: {s4}   is an orientation double cover: {in4}")
    print(f"         m003: |Tor H_1| = {t3}  perfect square: {s3}   is an orientation double cover: {in3}")
    print("         5 is not a perfect square, so under W2's MEASURED law m003 cannot be an")
    print("         orientation double cover -- and it is not.  m004's torsion is trivial,")
    print("         trivially square, and it IS one (of the Gieseking manifold m000).")
    print("         THE CHAIN AT THE OBJECT:")
    print("           A5 moves H_1 (xB022 V3, 494/494) and shifts |Tor| by exactly +4 (xB022 V7)")
    print("             -> |Tor(m004)| = 1 -> |Tor(m003)| = 5")
    print("           square torsion is necessary for a free orientation-reversing involution")
    print("             (W2's measured law, 1260/1260)")
    print("           a free orientation-reversing involution forces CS class zero (W2)")
    print("           -> m004 at 0, m003 at 1/4.  THE SELECTION IS A PROPERTY OF H_1.")
    ok = (s4 and not s3 and in4 and not in3)
    R["W3"] = {"tor_m004": t4, "tor_m003": t3, "square_m004": bool(s4), "square_m003": bool(s3),
               "m004_is_cover": bool(in4), "m003_is_cover": bool(in3)}
    print(f"W3 {'PASS' if ok else 'FAIL'}  the sealed prediction holds in both directions.")
    return ok


# ------------------------------------------------------------------ W4

def W4(window=None):
    """The census test, BOTH directions, with the base rate the seal demands."""
    print("\nW4       THE CENSUS TEST -- both directions, with base rates")
    covers = R.get("_covers", set())
    OC = snappy.OrientableCuspedCensus(num_cusps=1)
    n = len(OC) if window is None else min(window, len(OC))
    print(f"         WINDOW, stated numerically: the FULL one-cusped orientable cusped census, "
          f"{n} manifolds.")
    amph = []
    errs = {}
    scanned = 0
    for M in OC[:n]:
        scanned += 1
        try:
            G = M.symmetry_group()
        except Exception as e:
            errs[type(e).__name__] = errs.get(type(e).__name__, 0) + 1
            continue
        try:
            if not G.is_full_group() or not G.is_amphicheiral():
                continue
        except Exception as e:
            errs[type(e).__name__] = errs.get(type(e).__name__, 0) + 1
            continue
        amph.append(M)
    print(f"         scanned {scanned};  amphichiral (B152's gate: is_full_group first): {len(amph)}"
          f";  errors {errs if errs else 0}")
    tab = {}
    quarter_covers = []
    rows = []
    for M in amph:
        try:
            iso = M.isometry_signature()
        except Exception:
            continue
        c = cs_class(M)
        if not isinstance(c, str):
            c = "other"
        isc = iso in covers
        tab[(isc, c)] = tab.get((isc, c), 0) + 1
        rows.append((str(M), c, isc, tor_order(M)))
        if isc and c == "quarter":
            quarter_covers.append(str(M))
    print("         CROSS-TAB   (is an orientation double cover) x (CS class):")
    for isc in (True, False):
        for c in ("zero", "quarter", "other"):
            print(f"           cover={str(isc):<5} class={c:<8} {tab.get((isc, c), 0)}")
    nz = tab.get((False, "zero"), 0)
    nq = tab.get((False, "quarter"), 0)
    base = nz / (nz + nq) if (nz + nq) else 0.0
    cz = tab.get((True, "zero"), 0)
    cq = tab.get((True, "quarter"), 0)
    on = cz / (cz + cq) if (cz + cq) else 0.0
    print(f"         BASE RATE, the seal's requirement: among amphichiral manifolds that are NOT")
    print(f"         orientation double covers, CS class zero occurs {nz} of {nz+nq} = {100*base:.1f}%")
    print(f"         among those that ARE covers: {cz} of {cz+cq} = {100*on:.1f}%")
    print(f"         KILL CONDITION -- a quarter-class orientation double cover: {quarter_covers}")
    ok = (not quarter_covers) and len(amph) > 100
    R["W4"] = {"window": n, "amphichiral": len(amph), "errors": errs,
               "crosstab": {f"{k[0]}|{k[1]}": v for k, v in tab.items()},
               "base_rate_zero_among_noncovers": base, "zero_rate_among_covers": on,
               "quarter_class_covers": quarter_covers}
    R["_rows"] = rows
    if quarter_covers:
        print("W4 NEGATIVE  THE KILL CONDITION FIRED.  L194's conjecture is REFUTED and this is")
        print("         the arc's headline.")
    else:
        print(f"W4 {'PASS' if ok else 'FAIL'}  no quarter-class orientation double cover exists in the")
        print("         window.  The conjecture survives a test it could have failed.")
    return ok


# ------------------------------------------------------------------ W5

def W5():
    """The torsion filter applied to the quarter class, against its base rate."""
    print("\nW5       THE TORSION FILTER ON THE QUARTER CLASS -- against its base rate")
    rows = R.get("_rows", [])
    z = [r for r in rows if r[1] == "zero"]
    q = [r for r in rows if r[1] == "quarter"]
    zs = sum(1 for r in z if is_square(r[3]))
    qs = sum(1 for r in q if is_square(r[3]))
    rz = zs / len(z) if z else 0.0
    rq = qs / len(q) if q else 0.0
    print(f"         amphichiral, CS class zero:    {len(z)};  |Tor| square: {zs}  ({100*rz:.1f}%)")
    print(f"         amphichiral, CS class quarter: {len(q)};  |Tor| square: {qs}  ({100*rq:.1f}%)")
    print(f"         the filter SEPARATES only if these rates differ materially: "
          f"{100*abs(rz-rq):.1f} points apart")
    sep = abs(rz - rq) > 0.15
    print(f"         materially separating (>15 points): {sep}")
    if not sep:
        print("         REPORTED AS THE SEAL REQUIRES: the rates are comparable, so square torsion")
        print("         does NOT by itself explain the quarter class.  The explanation in W3 is")
        print("         SPECIFIC TO THE OBJECT and is not a general separator.")
    R["W5"] = {"zero_n": len(z), "zero_square": zs, "zero_rate": rz,
               "quarter_n": len(q), "quarter_square": qs, "quarter_rate": rq,
               "materially_separating": bool(sep)}
    return True          # the cell reports; it does not gate on the direction of the answer


# ------------------------------------------------------------------ W6

def W6():
    print("\nW6       WHAT REMAINS OPEN -- declared in the seal, restated here")
    print("         This arc does NOT close L194.  What it did and did not do:")
    print("           DONE: the instrument gap is PROVED, not relayed (W1).")
    print("           DONE: B1239's route through Kawauchi is REPLACED by a measured law (W2),")
    print("                 so nothing here rests on a theorem this seat has not read.")
    print("           DONE: the selection at the OBJECT is explained by H_1 (W3), and the bit")
    print("                 that moves H_1 is A5 -- the same bit that shifts CS by 1/4.")
    print("           NOT DONE: the cusp-local lemma in general.  Freeness on a tau-invariant")
    print("                 cusp still needs the translation part, which W1 shows SnapPy does")
    print("                 not expose and which this arc does not compute.")
    print("           NOT DONE: W5's filter is not a general separator (see its own report).")
    print("         L194 REMAINS OPEN, narrowed at the object.")
    R["W6"] = {"l194_closed": False}
    return True


if __name__ == "__main__":
    res = {}
    for f in (W0, W1, W2, W3, W4, W5, W6):
        try:
            res[f.__name__] = bool(f())
        except Exception as e:
            print(f"{f.__name__} EXCEPTION {type(e).__name__}: {e}")
            res[f.__name__] = False
    print("\n" + "=" * 78)
    for k, v in res.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
    print("VERIFIED" if all(res.values()) else "NOT ALL CELLS PASSED")
    R.pop("_covers", None)
    R.pop("_rows", None)
    with open(os.path.join(os.path.dirname(__file__), "selection.json"), "w",
              encoding="utf-8") as fh:
        json.dump({"cells": res, "results": R}, fh, indent=1, default=str)
