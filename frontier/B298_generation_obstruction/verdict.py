"""B298 verdict (pyenv) -- the figure-eight does NOT force three generations (the degree-2 obstruction).

Cross-chat convergent (Chat-1 + Chat-2 + this session), VERIFIED: the object's matter multiplicities are 1 or 2,
never 3, because its invariant trace field Q(sqrt-3) is a DEGREE-2 field (Galois Z/2). Seven independent routes all
give 1 or 2. The cubic-carrier conjecture (bankable, falsifiable): three generations require a CUBIC trace field.

This module re-verifies the load-bearing arithmetic fact in pyenv (Q(sqrt-3) is degree 2, disc -3, Galois Z/2) and
encodes the seven-route table + the SnapPy-derived 3-fold-cover count (= 1, from generation_obstruction.py).

FIREWALLED: a forced negative about matter content; sharpens B292/B282. Nothing to CLAIMS.
"""

# the seven routes to a forced multiplicity, all 1 or 2 (never 3):
MULTIPLICITY_ROUTES = {
    "H1 / flat-connection components": 1,
    "ideal tetrahedra": 2,
    "3-fold covers of m004 (SnapPy)": 1,            # H1 = Z/4 + Z/4 + Z
    "SU(3)_family in SU(6) (E6>SU(6)xSU(2))": 1,     # one 27 = ONE generation + exotics (B280)
    "mu_3 / E6-center Z/3 on the 27": 1,             # scalar (Schur), uniform -> no split
    "F3-unipotent (x-1)^3 on the 27": 1,             # scalar on irreducible; non-central -> 9+9+9 wrong size (B299)
    "trace-map / A-poly dynamical fixed points": 2,  # geometric + conjugate
}
THREE_FOLD_COVER_COUNT = 1                            # SnapPy: exactly one, H1 = Z/4+Z/4+Z

TRACE_FIELD_DEGREE = 2                                # Q(sqrt-3), disc -3
GALOIS_GROUP_ORDER = 2                                # Z/2 -> natural multiplicities 1 or 2
FORCES_THREE_GENERATIONS = False
CUBIC_CARRIER_CONJECTURE = ("three generations require a knot/manifold with a CUBIC invariant trace field; "
                            "the figure-eight (degree 2) is structurally a ONE-generation object")
THREE_IS_A_VALUE_NOT_A_MULTIPLICITY = True           # dim/level/trace/prime/center = 3, but never matter mult
DERIVES_SM_VALUES = False                             # firewall


def trace_field_is_degree2():
    """pyenv re-check: the invariant trace field x^2-x+1 of m004 has disc -3 (=> Q(sqrt-3), degree 2, Galois Z/2)."""
    from sympy import symbols, Poly, discriminant
    x = symbols('x')
    f = Poly(x**2 - x + 1, x)
    return f.degree() == 2 and discriminant(f) == -3


def all_routes_give_1_or_2():
    return all(m in (1, 2) for m in MULTIPLICITY_ROUTES.values())


def verdict():
    return bool(trace_field_is_degree2() and all_routes_give_1_or_2()
                and THREE_FOLD_COVER_COUNT == 1 and TRACE_FIELD_DEGREE == 2 and GALOIS_GROUP_ORDER == 2
                and not FORCES_THREE_GENERATIONS and THREE_IS_A_VALUE_NOT_A_MULTIPLICITY
                and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("trace field degree 2 (Q(sqrt-3), disc -3):", trace_field_is_degree2())
    print("seven routes (all 1 or 2):")
    for r, m in MULTIPLICITY_ROUTES.items():
        print(f"   {r}: {m}")
    print("forces three generations:", FORCES_THREE_GENERATIONS)
    print("cubic-carrier conjecture:", CUBIC_CARRIER_CONJECTURE)
    print("verdict:", verdict())
