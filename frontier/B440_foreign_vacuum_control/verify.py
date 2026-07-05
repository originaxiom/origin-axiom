"""B440 (C3 foreign control) -- verify the SL(2,C) vacuum spectra of K(5,1) (charvar.json,
computed in sage from pi_1) and read the tier-3 verdict. Pure sympy; runs in pyenv.

THE COMPLETE VACUUM SPECTRA (irreducible SL(2,C) characters of the closed manifolds):
  4_1(5,1) [child]     : 4 vacua, all in the -283 field         x^4-3x^3+x^2+3x-1
  5_2(5,1) [neighbour] : 6 vacua = 2 in Q(sqrt5) + 4 in the SAME -283 field
                                    (x^2+x-1)(x^4-4x^3+4x^2+x-1)
  3_1(5,1) [Seifert]   : 5 vacua (disc 11^4)
  6_1(5,1)             : 11 vacua

CROSS-VALIDATION: the child's charvar quartic x^4-3x^3+x^2+3x-1 is IDENTICAL to B439's
A-polynomial quartic -- two independent methods (closed-manifold character variety vs
Cooper-Long A-poly on L=M^-5) agree exactly.

TIER-3 VERDICT (applying the C3 break criterion): NO figure-eight-unique feature.
  * the -283 field is COMMENSURABILITY-SHARED: both 4_1 and 5_2 have -283-field vacua in the
    SAME quartic field (different minimal polynomials, mutually containing => equal field).
  * the vacuum COUNT (4/6/5/11) tracks A-polynomial degree = GENERICITY (fails break crit (c):
    not traceable to the parent's sqrt5/sqrt-3, only to knot complexity).
  * the GOLDEN inversion: Q(sqrt5) vacua -- which the GOLDEN parent (Delta_41 golden) might be
    expected to transmit -- are ABSENT in the child and PRESENT in the NON-golden 5_2's child.
    The child is golden-free (shared with 3_1, 6_1). The golden echo, where it appears at all,
    is FOREIGN, never the figure-eight's. Surgery launders identity (Inversion Law, 4th
    instance, at the SL(2) floor -- the sharpest: tested against the commensurability neighbour).

Firewall: hyperbolic geometry + character-variety arithmetic. No physics claim.
"""
import os, json
import sympy as sp

x, a = sp.symbols('x a')
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, "charvar.json")))

B439_CHILD_QUARTIC = x**4 - 3*x**3 + x**2 + 3*x - 1   # from B439 (Cooper-Long A-poly on L=M^-5)


def poly(name):
    return sp.sympify(DATA[name]["trace_poly"])


def same_field(p, q):
    """degree-4 fields Q[x]/p and Q[x]/q are equal iff p has a root in Q[x]/q."""
    pf, qf = sp.Poly(p, x), sp.Poly(q, x)
    if pf.degree() != qf.degree():
        return False
    return len(sp.factor_list(p, x, extension=sp.CRootOf(q, 0))[1]) > 1 or \
        any(sp.Poly(f, x, extension=sp.CRootOf(q, 0)).degree() == 1
            for f, _ in sp.factor_list(p, x, extension=sp.CRootOf(q, 0))[1])


def child_charvar_matches_b439():
    return sp.expand(poly("4_1(5,1)") - B439_CHILD_QUARTIC) == 0


def golden_vacua_only_in_5_2():
    def has_golden(nm):
        return any(deg == 2 and disc == 5 for _, deg, disc in DATA[nm]["factors"])
    return has_golden("5_2(5,1)") and not any(
        has_golden(k) for k in ["4_1(5,1)", "3_1(5,1)", "6_1(5,1)"])


def neg283_field_shared():
    child = poly("4_1(5,1)")
    foreign = sp.sympify([f[0] for f in DATA["5_2(5,1)"]["factors"] if f[2] == -283][0])
    # child root beta = -r^3+3r^2-r-1 (r a root of foreign): check child(beta)=0 mod foreign
    beta = -a**3 + 3*a**2 - a - 1
    return sp.rem(sp.expand(beta**4 - 3*beta**3 + beta**2 + 3*beta - 1),
                  foreign.subs(x, a), a) == 0


if __name__ == "__main__":
    counts = {k: DATA[k]["total_vacua"] for k in DATA}
    print("vacuum counts:", counts)
    print("child charvar == B439 A-poly quartic:", child_charvar_matches_b439())
    print("-283 field shared 4_1 <-> 5_2       :", neg283_field_shared())
    print("golden Q(sqrt5) vacua only in 5_2   :", golden_vacua_only_in_5_2())
    assert counts == {"4_1(5,1)": 4, "5_2(5,1)": 6, "6_1(5,1)": 11, "3_1(5,1)": 5}
    assert child_charvar_matches_b439()
    assert neg283_field_shared()
    assert golden_vacua_only_in_5_2()
    verdict = dict(
        counts=counts,
        child_matches_b439=True, neg283_field_shared=True, golden_only_in_foreign=True,
        tier3="NO figure-eight-unique feature; -283 field commensurability-shared; count is "
              "genericity; golden inversion (golden parent's child is golden-free, foreign 5_2's "
              "child carries golden) => Inversion Law 4th instance at the SL(2) floor",
    )
    json.dump(verdict, open(os.path.join(HERE, "verdict.json"), "w"), indent=1)
    print("[written] verdict.json")
