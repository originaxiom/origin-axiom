"""xB023 ADDENDUM 1 cell -- does Meyerhoff-Ouyang Corollary 2.5 govern the 0-vs-1/4 split?

MO Cor 2.5: an AMPHICHEIRAL hyperbolic KNOT OR LINK IN S^3 has eta(L) = 0.
A knot complement in S^3 has H_1 = Z; an h-component link complement has Z^h.  BOTH TORSION-FREE.
So torsion-free H_1 is NECESSARY (not sufficient) for the corollary to reach a manifold.

PREDICTION, SEALED at 44463e70 before this file existed: among the quarter-class amphichiral
one-cusped census manifolds, NONE has H_1 = Z.
KILL: one that does is the headline.
CONTROL: the zero-class side must be checked too -- if neither class has any, the test is VACUOUS.
"""
import json
import os
import warnings

warnings.filterwarnings("ignore")
import snappy
from mpmath import mp

mp.dps = 30
TOL = mp.mpf(10) ** -9
R = {}


def cs_class(M):
    try:
        s = repr(snappy.ManifoldHP(M.isometry_signature()).chern_simons()).replace(" ", "")
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
    return "other"


def h1sig(M):
    H = M.homology()
    return (H.betti_number(), tuple(sorted(d for d in H.elementary_divisors() if d)))


def M1():
    print("\nM1       MO COROLLARY 2.5 AGAINST THE 0-vs-1/4 SPLIT")
    print("         Cor 2.5 needs L in S^3.  A knot complement has H_1 = Z, a link complement Z^h;")
    print("         both TORSION-FREE.  So torsion-free H_1 is NECESSARY, not sufficient.")
    OC = snappy.OrientableCuspedCensus(num_cusps=1)
    zero_Z = quarter_Z = 0
    zero_n = quarter_n = other_n = errs = 0
    zex, qex = [], []
    for M in OC:
        try:
            G = M.symmetry_group()
            if not G.is_full_group() or not G.is_amphicheiral():
                continue
        except Exception:
            errs += 1
            continue
        c = cs_class(M)
        if c is None:
            errs += 1
            continue
        sig = h1sig(M)
        free_Z = (sig == (1, ()))          # H_1 = Z exactly
        if c == "zero":
            zero_n += 1
            zero_Z += free_Z
            if free_Z and len(zex) < 6:
                zex.append(str(M))
        elif c == "quarter":
            quarter_n += 1
            quarter_Z += free_Z
            if free_Z and len(qex) < 6:
                qex.append(str(M))
        else:
            other_n += 1
    print(f"         amphichiral one-cusped: zero {zero_n}, quarter {quarter_n}, "
          f"other {other_n}; errors {errs}")
    print(f"         with H_1 = Z exactly --  ZERO class: {zero_Z} of {zero_n}")
    print(f"                                  QUARTER class: {quarter_Z} of {quarter_n}")
    print(f"         zero-class examples with H_1 = Z: {zex}")
    print(f"         quarter-class examples with H_1 = Z: {qex}")
    vacuous = (zero_Z == 0 and quarter_Z == 0)
    print(f"         CONTROL -- is the test vacuous (neither class has any)? {vacuous}")
    if vacuous:
        print("         REPORTED VACUOUS: the predicate discriminates nothing and no conclusion")
        print("         may be drawn from it either way.")
    elif quarter_Z == 0:
        print("         *** THE PREDICTION HOLDS: no quarter-class amphichiral manifold has H_1 = Z,")
        print("         while the zero class does.  Consistent with MO Cor 2.5 governing the split.")
        print("         FENCE: H_1 = Z is NECESSARY, NOT SUFFICIENT -- the zero-class members that")
        print("         pass it are CANDIDATES for being S^3 knot complements, not proven ones.")
    else:
        print("         *** THE KILL CONDITION FIRED: a quarter-class amphichiral manifold has")
        print("         H_1 = Z.  Either it is not an S^3 knot complement despite the homology, or")
        print("         the cusped eta-cs relation carries slack the closed one does not.")
    # the object and its sister, explicitly
    print("         THE OBJECT AND ITS SISTER:")
    for nm in ("m004", "m003"):
        Mx = snappy.Manifold(nm)
        print(f"           {nm}: H_1 = {Mx.homology()}  torsion-free: {h1sig(Mx) == (1, ())}  "
              f"CS class {cs_class(Mx)}")
    print("         m004 IS S^3 minus the figure-eight knot and the knot IS amphichiral, so")
    print("         Cor 2.5 gives eta(m004) = 0 outright.  m003's H_1 HAS TORSION, so it is not a")
    print("         knot or link complement in S^3 and Cor 2.5 is SILENT on it.")
    R["M1"] = {"zero_n": zero_n, "quarter_n": quarter_n, "other_n": other_n, "errors": errs,
               "zero_with_H1_Z": zero_Z, "quarter_with_H1_Z": quarter_Z,
               "zero_examples": zex, "quarter_examples": qex,
               "vacuous": bool(vacuous),
               "prediction_holds": bool(quarter_Z == 0 and not vacuous)}
    ok = not vacuous and quarter_Z == 0
    print(f"M1 {'PASS' if ok else 'FAIL'}  (the cell ran correctly; its CONTENT is the verdict above)")
    return ok


if __name__ == "__main__":
    res = {}
    try:
        res["M1"] = bool(M1())
    except Exception as e:
        print(f"M1 EXCEPTION {type(e).__name__}: {e}")
        res["M1"] = False
    print("\n" + "=" * 78)
    print("VERIFIED" if all(res.values()) else "NOT ALL CELLS PASSED")
    with open(os.path.join(os.path.dirname(__file__), "mo_corollary.json"), "w",
              encoding="utf-8") as fh:
        json.dump({"cells": res, "results": R}, fh, indent=1, default=str)
