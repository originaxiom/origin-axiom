"""B440 (C3 foreign control) -- verify the SL(2,C) vacuum spectra of K(5,1) (charvar.json,
the raw tr(A)-elimination computed in sage from pi_1) and read the tier-3 verdict.

CORRECTED 2026-07-05 (adversarial review): the first cut mis-read 5_2's degree-6 tr(A)
polynomial as "6 irreducible vacua incl. a golden factor" and inferred a "golden inversion."
That was WRONG on two counts, both fixed here:
  * the golden factor x^2+x-1 is the REDUCIBLE abelian Z/5 characters (A,B diagonal with
    5th-root eigenvalues => [A,B]=I => tr[A,B]=2), NOT an irreducible vacuum;
  * those golden abelian characters are UNIVERSAL -- H_1=Z/5 forces them for EVERY K(5,1)
    (4_1, 5_2, 3_1, 6_1), verified below by the abelianization exponent-sums. They surfaced in
    the raw tr(A)-elimination only for 5_2 (whose abelian rep has B=I) -- a parametrization
    artifact of the A-upper/B-lower chart, not a figure-eight-vs-5_2 distinction.

THE CORRECTED SPECTRA (irreducible SL(2,C) characters; reducible = golden abelian trace):
  4_1(5,1) [child]     : 4 irreducible, all -283   (x^4-3x^3+x^2+3x-1)
  5_2(5,1) [neighbour] : 4 irreducible, all -283   (x^4-4x^3+4x^2+x-1) -- SAME field, same count
  3_1(5,1) [Seifert]   : 5 irreducible (disc 11^4)
  6_1(5,1)             : 11 irreducible
  golden Q(sqrt5)      : REDUCIBLE abelian Z/5 characters, present for ALL FOUR (universal).

CROSS-VALIDATION (stands): the child's tr(A) quartic x^4-3x^3+x^2+3x-1 is IDENTICAL to B439's
Cooper-Long A-polynomial quartic -- two independent methods agree exactly.

TIER-3 VERDICT (corrected -- a CLEANER negative): NO figure-eight-unique feature.
  * 4_1 and 5_2 have the SAME irreducible count (4) in the SAME -283 field (different minimal
    polynomials -> same field by mutual containment). Commensurability-shared, nothing finer.
  * the vacuum count across knots (4/4/5/11) tracks A-poly degree = genericity.
  * the golden Q(sqrt5) characters are numerator-forced (H_1=Z/5) and universal, NOT a
    parent-fingerprint. (The retracted "golden inversion" was an artifact.)
The Inversion Law's 4th instance, at the SL(2) floor, tested against the commensurability
neighbour -- and the corrected reading strengthens it: surgery launders identity so thoroughly
that the child and its neighbour share even the irreducible vacuum count and field.

Firewall: hyperbolic geometry + character-variety arithmetic. No physics claim.
"""
import os, json
import sympy as sp

x = sp.Symbol('x')
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, "charvar.json")))
GOLDEN = x**2 + x - 1                                  # the only abelian trace field (5th roots)
B439_CHILD_QUARTIC = x**4 - 3*x**3 + x**2 + 3*x - 1


def poly(name):
    return sp.sympify(DATA[name]["trace_poly"])


def irreducible_split(name):
    """separate the reducible abelian-golden factor (roots of x^2+x-1) from the irreducible
    vacua. A character is reducible <=> its meridian trace is a Z/5 abelian trace (golden)."""
    facs = sp.factor_list(poly(name), x)[1]
    irr, red = [], []
    for f, _ in facs:
        d = sp.Poly(f, x).degree()
        (red if (d == 2 and sp.rem(f, GOLDEN, x) == 0) else irr).append((f, d))
    return sum(d for _, d in irr), sum(d for _, d in red), irr


def _expsum(word):
    p = {'a': 0, 'b': 0}
    for ch in word:
        if ch == 'a': p['a'] += 1
        elif ch == 'A': p['a'] -= 1
        elif ch == 'b': p['b'] += 1
        elif ch == 'B': p['b'] -= 1
    return p['a'], p['b']


def golden_abelian_is_universal():
    """H_1=Z/5 forces a nontrivial abelian SL(2) rep with meridian eigenvalue zeta5^k (golden
    trace) for EVERY K(5,1). Verified from snappy relators' abelianization exponent-sums."""
    import snappy
    for name in DATA:
        rels = snappy.Manifold(name).fundamental_group().relators()
        rows = [_expsum(w) for w in rels]
        has_golden = any(xk % 5 != 0 and all((Pa*xk + Pb*yk) % 5 == 0 for Pa, Pb in rows)
                         for xk in range(5) for yk in range(5) if (xk, yk) != (0, 0))
        if not has_golden:
            return False
    return True


def child_charvar_matches_b439():
    return sp.expand(poly("4_1(5,1)") - B439_CHILD_QUARTIC) == 0


def neg283_field_shared():
    """the child's and 5_2's irreducible -283 quartics generate the SAME field: the child root
    beta = -r^3+3r^2-r-1 (r a root of 5_2's quartic) satisfies the child quartic."""
    a = sp.Symbol('a')
    child = x**4 - 3*x**3 + x**2 + 3*x - 1
    foreign = [f for f, _ in irreducible_split("5_2(5,1)")[2] if sp.Poly(f, x).degree() == 4][0]
    beta = -a**3 + 3*a**2 - a - 1
    return sp.rem(sp.expand(beta**4 - 3*beta**3 + beta**2 + 3*beta - 1), foreign.subs(x, a), a) == 0


if __name__ == "__main__":
    split = {k: irreducible_split(k) for k in DATA}
    irr_counts = {k: split[k][0] for k in DATA}
    print("irreducible vacuum counts:", irr_counts)
    print("child irreducible == B439 A-poly quartic:", child_charvar_matches_b439())
    print("4_1 & 5_2 irreducible -283 field shared  :", neg283_field_shared())
    print("golden abelian characters UNIVERSAL (all K(5,1)):", golden_abelian_is_universal())

    assert irr_counts == {"4_1(5,1)": 4, "5_2(5,1)": 4, "6_1(5,1)": 11, "3_1(5,1)": 5}
    assert child_charvar_matches_b439()
    assert neg283_field_shared()
    assert golden_abelian_is_universal()

    verdict = dict(
        irreducible_counts=irr_counts,
        child_matches_b439=True, neg283_field_shared=True,
        golden_is_reducible_and_universal=True,
        retracted="the 'golden inversion' (golden only in 5_2's child) -- artifact of unfiltered "
                  "reducibles + the A-upper/B-lower parametrization; golden abelian chars are "
                  "universal (H_1=Z/5)",
        tier3="NO figure-eight-unique feature; 4_1 and 5_2 share the -283 field AND the "
              "irreducible count 4; golden Q(sqrt5) is numerator-forced reducible, universal => "
              "Inversion Law 4th instance at the SL(2) floor (a cleaner, stronger negative)",
    )
    json.dump(verdict, open(os.path.join(HERE, "verdict.json"), "w"), indent=1)
    print("[written] verdict.json (corrected)")
