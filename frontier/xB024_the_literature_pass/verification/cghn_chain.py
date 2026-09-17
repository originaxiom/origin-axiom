"""xB024 ADDENDUM 1 -- CGHN OBTAINED. The UNREACHABLE grade was WRONG, and the chain closes.

THE PROCESS CORRECTION FIRST, because it is the most useful thing here.
xB024's banked FINDINGS graded CGHN **UNREACHABLE** after two failed routes (Project Euclid's
article page, and Neumann's KAIST survey returning HTTP 503 twice).  THE PAPER WAS FREELY
AVAILABLE THE WHOLE TIME -- at Project Euclid's own open archive for Experimental Mathematics, and
as `snappaper3.pdf` on Neumann's Columbia preprints page.  The first attempt failed only because
WebFetch's reader could not parse the PDF binary; extracting it locally with pypdf worked
immediately, exactly as it had for Kawauchi one arc earlier.

  **"UNREACHABLE" described this seat's search, not the source.**  A negative access result needs
  the same controls as a negative measurement: try the author's own page, try the journal's open
  archive, and parse the bytes yourself before concluding the door is shut.

CGHN = D. Coulson, O. A. Goodman, C. D. Hodgson, W. D. Neumann, "Computing Arithmetic Invariants
of 3-Manifolds", Experimental Mathematics 9 (2000) 127-152.  Read at source.

SECTION 5A, verbatim (the mod-1/2 statement B1239 quotes):

  "This leads to an invariant cs(M) of a hyperbolic 3-manifold M in R/(1/2)Z.  If M is closed the
   Chern-Simons invariant is well defined modulo 1, but Snap and SnapPea still only compute modulo
   1/2.  This is no real loss, since the Chern-Simons invariant of a closed manifold M modulo 1 can
   also be computed from the first homology of M together with the eta-invariant eta(M), both of
   which Snap can also compute."

  -> B1239's quotation is EXACT.

SECTION 5B, verbatim (the APS relation B1239 quotes):

  "The relation of eta(M) to cs(M) for a COMPACT 3-manifold M is
        3 eta(M) = 2 cs(M) + tau   (mod 2)
   (see [Atiyah et al. 1975]), where tau is the number of 2-primary summands of H_1(M; Z).  Thus
   eta(M) completely determines cs(M) if M has known homology."

  -> B1239's quotation is EXACT and CORRECTLY ATTRIBUTED to Atiyah-Patodi-Singer, "Spectral
     asymmetry and Riemannian geometry, II", Math. Proc. Cambridge Philos. Soc. 78:3 (1975) 405-432.
     (An earlier pass of this arc reported "Atiyah: 0 hits" -- that was a TEXT-EXTRACTION ARTIFACT;
     the PDF renders the name as "A tiy ah, P ato di and Singer".  Corrected before use.)

SECTION 5B, verbatim (what Meyerhoff-Ouyang actually does -- L194's blocker, described by a source
we CAN read):

  "There is also a cusped version of this: Meyerhoff and Ouyang [1997] extended the definition of
   eta(M) to cusped M FOR WHICH ONE HAS CHOSEN A BASIS OF HOMOLOGY AT EACH CUSP."

  and on the formula's provenance:

  "A formula for eta(M(p,q)) in terms of ideal triangulations ... was given in [Meyerhoff and
   Neumann 1992], where it was proved 'locally' ... It was proved globally in [Ouyang 1997]."

  -> GRADE: SECONDARY.  This is CGHN describing Meyerhoff-Ouyang.  MO itself remains UNREAD and
     this arc still cites it for nothing.  But L194's register entry has, since 2026-09-02, guessed
     at a "cusp-basis correction"; CGHN CONFIRMS that MO's cusped eta requires A CHOSEN BASIS OF
     HOMOLOGY AT EACH CUSP.

THE CHAIN THAT NOW CLOSES IN THE CLOSED CASE, every link read at source:

  (1) APS, as printed in CGHN 5B:         3 eta(M) = 2 cs(M) + tau  (mod 2)
  (2) eta is ODD under orientation reversal and is an isometry invariant, so for a CLOSED
      AMPHICHIRAL M, eta(M) = -eta(M), hence eta(M) = 0.
  (3) Therefore 2 cs(M) + tau = 0 (mod 2).
  (4) Kawauchi Theorems I + III (xB023, read at source): a FREE orientation-reversing involution
      has Fix empty, so sigma(alpha,M) = 0, so Tor H_1(M) is a STRICT direct double A + A,
      so tau -- the number of 2-primary summands -- is EVEN.
  (5) Hence 2 cs(M) = 0 (mod 2), i.e. cs(M) = 0 (mod 1).

  A CLOSED hyperbolic 3-manifold carrying a FREE orientation-reversing involution has cs = 0 MOD 1,
  not merely mod 1/2.  Both ingredients are now read at source; neither is paraphrased.

WHAT THIS DOES NOT DO.  It does NOT close L194, whose open half is CUSPED and needs MO's cusped
eta -- still unread.  Step (2) is standard and is NOT quoted from a source here; it is flagged as
the one unsourced link in the chain.
"""
import json
import os

import snappy
from mpmath import mp

mp.dps = 40
R = {}
TOL = mp.mpf(10) ** -9


def cs_class(M):
    """CS class mod 1/2.  Uses the manifold's own high-precision copy where available and falls
    back to standard precision; a FAILURE returns None and is COUNTED, never swallowed -- the
    swallowed-RuntimeError lesson from earlier in this session."""
    try:
        try:
            H = M.high_precision()
            s = repr(H.chern_simons()).replace(" ", "")
        except Exception:
            s = repr(M.chern_simons()).replace(" ", "")
    except Exception as e:
        return ("unavailable", f"{type(e).__name__}: {e}"[:90])
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


def tor_order(M):
    o = 1
    for d in M.homology().elementary_divisors():
        if d:
            o *= d
    return o


def tau_of(M):
    """tau = the number of 2-primary summands of H_1(M;Z), as CGHN 5B defines it."""
    return sum(1 for d in M.homology().elementary_divisors() if d and d % 2 == 0)


def C1():
    """The chain's prediction, tested on manifolds that satisfy its hypotheses."""
    print("\nC1       THE CLOSED-CASE CHAIN, tested where its hypotheses hold")
    print("         Prediction from the chain: a CLOSED hyperbolic 3-manifold with a FREE")
    print("         orientation-reversing involution has cs = 0 mod 1, hence certainly mod 1/2,")
    print("         and its tau (number of 2-primary summands of H_1) is EVEN.")
    censuses = [snappy.NonorientableClosedCensus,
                snappy.CubicalNonorientableClosedCensus,
                snappy.DodecahedralNonorientableClosedCensus,
                snappy.IcosahedralNonorientableClosedCensus]
    seen, tot, zero, other, tau_even, errs, why = set(), 0, 0, [], 0, 0, []
    for cen in censuses:
        for Q in cen:
            try:
                M = Q.orientation_cover()
                key = (round(float(M.volume()), 9),
                       tuple(sorted(M.homology().elementary_divisors())))
                if key in seen:
                    continue
                seen.add(key)
            except Exception:
                errs += 1
                continue
            tot += 1
            t = tau_of(M)
            if t % 2 == 0:
                tau_even += 1
            c = cs_class(M)
            if isinstance(c, tuple):
                errs += 1
                if len(why) < 3:
                    why.append((str(Q), c[1]))
            elif c == "zero":
                zero += 1
            else:
                other.append((str(Q), c, t))
    print(f"         closed manifolds with a free orientation-reversing involution: {tot}")
    print(f"         tau EVEN (Kawauchi step, read at source):        {tau_even} of {tot}")
    print(f"         cs class ZERO (the chain's conclusion, mod 1/2): {zero} of {tot}")
    for nm, c, t in other[:6]:
        print(f"           NOT ZERO: {nm} class={c} tau={t}")
    print(f"         cs UNAVAILABLE (instrument cannot compute it): {errs} of {tot}")
    for nm, msg in why:
        print(f"           {nm}: {msg}")
    cs_tested = tot - errs
    print()
    print("         THE CS HALF IS UNTESTED, AND THAT IS REPORTED AS UNTESTED, NOT AS A PASS.")
    print(f"         cs was computable for {cs_tested} of {tot} manifolds.  An earlier version of")
    print("         this cell accepted 'zero + errors == total', which PASSES WHEN EVERY")
    print("         MEASUREMENT FAILS -- a vacuous pass, and this record's own test-vacuity class.")
    print("         The cause is in CGHN itself (5B): Snap obtains these invariants only by")
    print("         bootstrapping along chains of hyperbolic drillings and fillings, and for a")
    print("         manifold not so linked it 'cannot compute' them.  The closed census covers")
    print("         built here are exactly such manifolds.")
    print("         FENCE: SnapPy reads cs mod 1/2 (CGHN 5A), so even where cs IS available this")
    print("         run could not see the chain's sharper mod-1 conclusion.  THE MOD-1 RESULT IS")
    print("         A READ-AT-SOURCE DERIVATION, NOT A MEASUREMENT, AND IS NOT CLAIMED AS ONE.")
    ok = (tau_even == tot) and tot >= 10      # ONLY the half that was actually measured
    R["C1"] = {"manifolds": tot, "tau_even": tau_even, "cs_zero": zero, "cs_tested": cs_tested,
               "not_zero": other, "cs_unavailable": errs, "why": why,
               "cs_half": "UNTESTED -- instrument cannot compute cs for these manifolds",
               "fence": "SnapPy reads cs mod 1/2; the mod-1 conclusion is DERIVED, not measured"}
    print(f"C1 {'PASS' if ok else 'FAIL'}  the KAWAUCHI step (tau even) is confirmed {tau_even}/{tot}.")
    print("         The CS step is UNTESTED here and is not counted as evidence.")
    return ok


def C2():
    print("\nC2       WHAT THE CHAIN DOES NOT REACH -- and the grade each source carries")
    rows = [
        ("APS relation 3eta = 2cs + tau (mod 2)", "CGHN 5B", "READ-AT-SOURCE"),
        ("cs mod 1/2 is SnapPy's readout limit", "CGHN 5A", "READ-AT-SOURCE"),
        ("free involution => Tor H_1 = A+A => tau even", "Kawauchi I + III", "READ-AT-SOURCE (xB023)"),
        ("eta is odd under orientation reversal", "standard", "NOT SOURCED HERE -- the one unsourced link"),
        ("cusped eta needs a chosen homology basis at each cusp", "CGHN 5B on Meyerhoff-Ouyang", "SECONDARY"),
        ("the cusped eta formula itself", "Meyerhoff-Ouyang 1997", "STILL UNREAD -- cited for nothing"),
    ]
    for what, src, grade in rows:
        print(f"           {grade:<34} {what}   [{src}]")
    print("         L194's OPEN HALF IS CUSPED.  The chain above is CLOSED-case only, so it does")
    print("         NOT close L194 -- exactly as xB023's seal declared before any cell ran.")
    R["C2"] = {"rows": rows, "l194_closed": False}
    return True


if __name__ == "__main__":
    res = {}
    for f in (C1, C2):
        try:
            res[f.__name__] = bool(f())
        except Exception as e:
            print(f"{f.__name__} EXCEPTION {type(e).__name__}: {e}")
            res[f.__name__] = False
    print("\n" + "=" * 78)
    for k, v in res.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
    print("VERIFIED" if all(res.values()) else "NOT ALL CELLS PASSED")
    with open(os.path.join(os.path.dirname(__file__), "cghn_chain.json"), "w",
              encoding="utf-8") as fh:
        json.dump({"cells": res, "results": R}, fh, indent=1, default=str)
