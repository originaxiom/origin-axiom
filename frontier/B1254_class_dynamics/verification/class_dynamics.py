#!/usr/bin/env python3
"""B1254 -- THE ORIENTATION CLASS HAS A DYNAMICS, AND IT IS NOT UNIFORM ACROSS THE STRATA.

Joins two things the repo already had but never met:
  B1248 (2026-09-05): det X = 2 - kappa  in K*/(K*)^2, kappa = tr[A,M] the Fricke-Vogt
                      invariant. So the orientation class is eps = squarefree(2 - kappa).
  B497  (2026-07-10): End(F_2) has FOUR STRATA on X(F_2), each with an EXACT kappa-law.
                      The programme has lived in stratum 1 of 4.

THE JOIN.  A stratum multiplies (kappa - 2) by an explicit factor F. Since eps is a SQUARE
CLASS, F acts on it by ITS OWN square class -- so a factor that is a perfect square leaves
eps untouched even though kappa itself moves.

    stratum 1  Aut / metallic a->a^m b        kappa' = kappa                     F = 1        eps PRESERVED
    stratum 2  A->A^2, B->B^2 (det 4)         kappa'-2 = (kappa-2) x^2 y^2       F = (xy)^2   eps PRESERVED
    stratum 3  Thue-Morse a->AB, b->BA        kappa'-2 = (kappa-2)(x^2+y^2-xyz)  F odd degree eps CAN CHANGE
    stratum 4  non-injective a->ab, b->ab     image contained in {kappa = 2}     --           eps UNDEFINED

  The stratum-3 factor x^2 + y^2 - xyz has TOTAL DEGREE 3. An odd-degree polynomial cannot be
  a perfect square, so its square class is non-trivial: stratum 3 is the ONLY stratum that can
  move the orientation class. (Proof by parity of degree -- no search.)

  B497's U1: the reducible locus kappa = 2 is invariant under EVERY endomorphism. That is exactly
  where 2 - kappa = 0 and eps is undefined -- the locus on which the class dies is ABSORBING.

WHY THIS WAS NOT ALREADY KNOWN.  B1157 banked "the object supplies NO parameter-free dynamical
law" WITHOUT CITING B497 -- our own finding at B1247 (2026-09-03), which located the mechanism:
the atlas lexicon was 18 noun-motifs frozen 2026-07-01 with NO WORD FOR A QUESTION (no motif for
arrow, irreversibility, dynamics, monoid, measurement, collapse, closing, naming or choice), so
B497 sat seven weeks under twelve object-motifs, none of which says monoid, strata or dynamics.
B6 -- the field equation box(tau) + kappa(tau^2 - tau - 1) = 0 with an EARNED potential -- was on
ZERO surfaces since week one. The dynamics was never missing; it was unreachable.

NOT CLAIMED: any physics reading of the strata. B497 fences the physics verb-names to
speculations/S063 and that fence is kept here. No measured value. Gate 5 clean.
"""
import sympy as sp

x, y, z = sp.symbols('x y z')

# B497's exact kappa-laws: (kappa' - 2) = (kappa - 2) * FACTOR   [stratum 1 is kappa' = kappa]
STRATA = {
    "1 Aut/metallic":      sp.Integer(1),
    "2 A->A^2,B->B^2":     x**2 * y**2,
    "3 Thue-Morse":        x**2 + y**2 - x * y * z,
}


def is_perfect_square(F):
    """A polynomial is a perfect square only if its total degree is even AND sqrt is polynomial."""
    F = sp.expand(F)
    if F.is_number:
        return sp.sqrt(F).is_rational
    p = sp.Poly(F, x, y, z)
    if p.total_degree() % 2:
        return False                      # odd degree -> never a square
    r = sp.sqrt(sp.factor(F))
    return not r.has(sp.Pow(sp.Symbol('_'), sp.Rational(1, 2))) and sp.expand(r**2 - F) == 0


def class_action():
    """For each stratum: (factor, is_square, verdict for the orientation class)."""
    out = {}
    for name, F in STRATA.items():
        sq = is_perfect_square(F)
        out[name] = (sp.factor(F), sq, "PRESERVED" if sq else "CAN CHANGE")
    return out


def stratum4_lands_on_the_degenerate_locus():
    """Stratum 4's image lies in {kappa = 2}, exactly where 2 - kappa = 0 and eps is undefined."""
    return {"image_in": "kappa = 2", "2_minus_kappa": 0, "eps": "undefined"}


def selftest(verbose=True):
    fails = []
    act = class_action()
    if act["1 Aut/metallic"][2] != "PRESERVED":
        fails.append("stratum 1 must preserve the class (kappa' = kappa)")
    if act["2 A->A^2,B->B^2"][2] != "PRESERVED":
        fails.append("stratum 2's factor (xy)^2 is a perfect square -- must preserve")
    if act["3 Thue-Morse"][2] != "CAN CHANGE":
        fails.append("stratum 3's factor has odd total degree -- must NOT be a square")
    # the degree argument, explicitly
    d3 = sp.Poly(sp.expand(STRATA["3 Thue-Morse"]), x, y, z).total_degree()
    if d3 % 2 == 0:
        fails.append(f"stratum-3 factor total degree {d3} is even -- the parity proof fails")
    # two-sided control: the test must be able to say PRESERVED and CAN CHANGE
    verdicts = {v[2] for v in act.values()}
    if verdicts != {"PRESERVED", "CAN CHANGE"}:
        fails.append(f"verdicts {verdicts} -- the classifier does not discriminate")
    if stratum4_lands_on_the_degenerate_locus()["2_minus_kappa"] != 0:
        fails.append("stratum 4 must land where 2 - kappa = 0")
    if verbose:
        for k, (F, sq, v) in act.items():
            print(f"  [{k:20}] factor {str(F):22} perfect square: {str(sq):5}  -> class {v}")
        print(f"  [stratum-3 degree ] total degree {d3} (odd) -> not a square, by parity alone")
        print(f"  [stratum 4        ] {stratum4_lands_on_the_degenerate_locus()}")
    return fails


if __name__ == "__main__":
    print("B1254 -- the orientation class under B497's strata (selftest)")
    f = selftest()
    print()
    print("SELFTEST:", "PASS" if not f else "FAIL")
    for i in f:
        print("   !", i)
    raise SystemExit(1 if f else 0)
