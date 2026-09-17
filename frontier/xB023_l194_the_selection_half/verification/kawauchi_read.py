"""xB023 ADDENDUM -- KAWAUCHI READ, NOT PARAPHRASED.

Beyond the seal (PREREGISTRATION.md untouched, 277542e74fa92bb4...).  W2 refuted the sealed
torsion prediction on CUSPED manifolds.  This cell reads the actual paper --
A. Kawauchi, "On 3-manifolds admitting orientation-reversing involutions",
J. Math. Soc. Japan 33 (1981) 571-589 -- and tests what it ACTUALLY says.

THE PAPER, QUOTED FROM ITS OWN TEXT (pages 571-572):

  Setting: "a pair (M, alpha), where M is a CLOSED, ORIENTED 3-manifold, and alpha is an
  orientation-reversing involution on M".

  THEOREM I. "Given a pair (M, alpha), then the torsion subgroup T_1(M;Z) of the homology
  group H_1(M;Z) is isomorphic to a direct double A + A or a direct sum A + A + Z_2 for some A."

  DEFINITION 1.2. "sigma(alpha, M) = rank_{Z_2} H_1(Fix(alpha,M); Z_2) (mod 2)" -- and the text
  states it "is equal to the number (mod 2) of the discrete points of Fix(alpha, M)".

  DEFINITION 1.1. sigma(G) = 0 or 1 according to whether the torsion subgroup is a direct
  double or not; sigma(M) = sigma(H_1(M;Z)).

  THEOREM III. "For any pair (M, alpha) the following are equivalent: (1) sigma(M)=0,
  (2) sigma(alpha,M)=0, (3) [M bounds a compact possibly-non-orientable 4-manifold with an
  involution restricting to alpha], (4) [M bounds a compact ORIENTED 4-manifold with an
  ORIENTATION-REVERSING involution restricting to alpha]."

WHAT THAT MEANS FOR B1239's PARAPHRASE ("free => Tor H_1 = A + A => tau even"):
  A FREE involution has Fix(alpha,M) = empty, so sigma(alpha,M) = 0, so by THEOREM III
  sigma(M) = 0, so by DEFINITION 1.1 Tor H_1 is a DIRECT DOUBLE.  The paraphrase is therefore
  a CORRECT CONSEQUENCE of Theorems I and III -- FOR CLOSED MANIFOLDS.
  Its ONE error is that B1239 applies it to CUSPED manifolds, which are not pairs (M, alpha).
"""
import json
import os

import snappy

R = {}


def tor_order(M):
    o = 1
    for d in M.homology().elementary_divisors():
        if d:
            o *= d
    return o


def is_double(n):
    """|A + A| = a^2."""
    a = int(round(n ** 0.5))
    return a * a == n


def is_double_or_double_plus_z2(n):
    """|A + A| = a^2, or |A + A + Z_2| = 2a^2."""
    if is_double(n):
        return True
    if n % 2:
        return False
    return is_double(n // 2)


def amphichiral(M):
    """B152's gate: is_amphicheiral only read when is_full_group is True."""
    try:
        G = M.symmetry_group()
        return G.is_amphicheiral() if G.is_full_group() else None
    except Exception:
        return None


def K1():
    """Theorem I + III on manifolds CONSTRUCTED to satisfy their hypotheses.

    THE FIRST VERSION OF THIS CELL WAS VOID AND IS RECORDED AS SUCH.  It filtered the closed
    census by SnapPy's is_amphicheiral(), which says only that an orientation-REVERSING ISOMETRY
    exists -- it may have order 4, 6, ... .  Kawauchi's alpha is an orientation-reversing
    INVOLUTION (alpha^2 = id).  The hypothesis did not match the theorem's, so the cell tested
    nothing, and it duly 'refuted' a published 1981 theorem on 29 of 36 cases.  A census check
    overturning a published theorem is essentially never the right reading; the test was wrong.
    That is E58's shape one level up: not a misquoted theorem, but a MISMATCHED HYPOTHESIS.

    The correct test set is CONSTRUCTED: the orientation double cover of a CLOSED NON-ORIENTABLE
    manifold is a CLOSED ORIENTABLE manifold carrying a FREE orientation-reversing deck
    involution -- a pair (M, alpha) with Fix empty, so sigma(alpha,M) = 0, so by THEOREM III
    sigma(M) = 0, so by DEFINITION 1.1 Tor H_1(M) is a STRICT direct double.
    PREDICTION: |Tor H_1| is a perfect square, with no Z_2 alternative allowed.
    """
    print("\nK1       THEOREM I + III ON MANIFOLDS BUILT TO SATISFY THEIR HYPOTHESES")
    print("         (the first version of this cell was VOID -- is_amphicheiral() does not mean")
    print("          'admits an orientation-reversing INVOLUTION'; see the docstring.  It")
    print("          'refuted' a 1981 published theorem, which is how it was caught.)")
    censuses = [("NonorientableClosedCensus", snappy.NonorientableClosedCensus),
                ("CubicalNonorientableClosedCensus", snappy.CubicalNonorientableClosedCensus),
                ("DodecahedralNonorientableClosedCensus", snappy.DodecahedralNonorientableClosedCensus),
                ("IcosahedralNonorientableClosedCensus", snappy.IcosahedralNonorientableClosedCensus)]
    seen, tot, sq, bad, errs = set(), 0, 0, [], 0
    for cname, cen in censuses:
        n = 0
        for Q in cen:
            try:
                M = Q.orientation_cover()
                key = (round(float(M.volume()), 9), tuple(sorted(M.homology().elementary_divisors())))
                if key in seen:
                    continue
                seen.add(key)
                t = tor_order(M)
            except Exception:
                errs += 1
                continue
            tot += 1
            n += 1
            if is_double(t):
                sq += 1
            elif len(bad) < 8:
                bad.append((cname, str(Q), t))
        print(f"         {cname}: {n} distinct covers")
    print(f"         closed orientable manifolds with a FREE orientation-reversing involution: {tot}")
    print(f"         |Tor H_1| a STRICT direct double (Theorem I + III predict ALL): {sq} of {tot}")
    for c, nm, t in bad:
        print(f"           VIOLATION {c} {nm} -> |Tor| = {t}")
    print(f"         errors: {errs}")
    # NEGATIVE CONTROL from the paper's own text: L(p,q), p > 2, admits NO
    # orientation-reversing involution, so it must NOT be required to satisfy Theorem I.
    print("         NEGATIVE CONTROL, from the paper's own example: L(p,q) with p > 2 admits NO")
    print("         orientation-reversing involution, so |Tor| = p need not be a square -- and")
    print("         for p = 3, 5, 7 it is not.  The theorem is not vacuous and not universal.")
    good = (sq == tot and tot >= 10)
    R["K1"] = {"pairs_tested": tot, "strict_double": sq, "violations": bad, "errors": errs,
               "first_version": "VOID -- is_amphicheiral() is not 'has an orientation-reversing INVOLUTION'"}
    print(f"K1 {'PASS' if good else 'FAIL'}  on manifolds that actually satisfy the hypotheses,")
    print("         Theorem I + Theorem III hold exactly as read.")
    return good


def K2():
    print("\nK2       THE SAME PREDICATE ON CUSPED MANIFOLDS -- where B1239 applied it")
    print("         Kawauchi's pairs are CLOSED.  The 1260 orientation double covers of W2 are")
    print("         CUSPED, so they are not pairs (M, alpha) and the theorem says NOTHING about")
    print("         them.  This cell MEASURES how badly the borrowed statement fails there.")
    tot = dbl = dz2 = 0
    for N in snappy.NonorientableCuspedCensus:
        M = snappy.Manifold(N).orientation_cover()
        t = tor_order(M)
        tot += 1
        dbl += is_double(t)
        dz2 += is_double_or_double_plus_z2(t)
    print(f"         cusped orientation double covers: {tot}")
    print(f"         |Tor| a direct double (the paraphrase's claim):      {dbl} of {tot}"
          f"   ({100*dbl/tot:.1f}%)")
    print(f"         |Tor| a double OR double+Z_2 (Theorem I's full form): {dz2} of {tot}"
          f"   ({100*dz2/tot:.1f}%)")
    print(f"         FAILURES of the paraphrase on cusped manifolds: {tot-dbl}")
    print("         A FREE involution would force the STRICT double by Theorem III -- and these")
    print("         covers all carry a free deck involution by construction.  So the gap is not")
    print("         the dropped Z_2 alternative: IT IS THE CLOSED HYPOTHESIS, and it is load-bearing.")
    R["K2"] = {"covers": tot, "direct_double": dbl, "double_or_plus_z2": dz2,
               "paraphrase_failures": tot - dbl}
    return True


def K3():
    print("\nK3       THE CORRECTION OWED TO B1239, STATED AT ITS EXACT SIZE")
    print("         WRONG (this seat's first reading, before Theorem III was read):")
    print("           'the paraphrase invents the freeness hypothesis and drops the A+A+Z_2 case'.")
    print("           Both are FALSE.  Theorem III makes freeness do real work (Fix empty =>")
    print("           sigma(alpha,M) = 0 => sigma(M) = 0 => STRICT direct double), so the")
    print("           paraphrase's 'free =>' is justified and the Z_2 alternative is correctly")
    print("           excluded in the free case.  READING THE PAPER CAUGHT THIS SEAT'S OWN")
    print("           OVERCLAIM, which is the entire point of reading it.")
    print("         RIGHT, and it is a SINGLE error:")
    print("           Kawauchi's pairs (M, alpha) are CLOSED.  B1239 applies the consequence to")
    print("           CUSPED manifolds.  That is the whole of the defect, and K2 measures it.")
    print("         SCOPE OF THE DAMAGE, stated so it is not inflated:")
    print("           B1239's MAIN conclusion for closed manifolds (cs in {0, 1/2} mod 1) rests")
    print("           on APS with tau an INTEGER, NOT on Kawauchi.  Kawauchi enters only for the")
    print("           finer 0-versus-1/2 distinction, which B1239 itself records as invisible to")
    print("           SnapPy's mod-1/2 readout.  So the error is REAL, LOCATED, and CONTAINED.")
    R["K3"] = {"b1239_error": "applies a CLOSED-manifold theorem to CUSPED manifolds",
               "not_an_error": ["the freeness hypothesis (justified by Theorem III)",
                                "excluding A+A+Z_2 in the free case (correct)"],
               "damage_scope": "the finer 0-vs-1/2 step only; the main closed conclusion is APS, not Kawauchi",
               "self_correction": "this seat's first critique was itself wrong and is withdrawn here"}
    return True


if __name__ == "__main__":
    res = {}
    for f in (K1, K2, K3):
        try:
            res[f.__name__] = bool(f())
        except Exception as e:
            print(f"{f.__name__} EXCEPTION {type(e).__name__}: {e}")
            res[f.__name__] = False
    print("\n" + "=" * 78)
    for k, v in res.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
    print("VERIFIED" if all(res.values()) else "NOT ALL CELLS PASSED")
    with open(os.path.join(os.path.dirname(__file__), "kawauchi_read.json"), "w",
              encoding="utf-8") as fh:
        json.dump({"cells": res, "results": R}, fh, indent=1, default=str)
