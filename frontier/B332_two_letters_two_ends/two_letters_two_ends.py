"""B332 -- the two arithmetic ends are the PRODUCT and the RATIO of the founding substitution's two letters.

Chat-1 handoff (2026-07-01), verify-don't-trust. The founding substitution sigma builds two 2x2
letters R = [[1,1],[0,1]], L = [[1,0],[1,1]] (generators of SL(2,Z)). Their two simplest length-2
combinations land on the two arithmetic ends of the whole program:

    PRODUCT  R*L = [[2,1],[1,1]]  trace 3  charpoly x^2-3x+1  disc  5  -> Q(sqrt5)  -> golden -> 2I -> E8
    RATIO   -R*L^-1 = g = [[0,-1],[1,-1]] order 3  charpoly x^2+x+1  disc -3  -> Q(sqrt-3) -> 2T -> E6

VERIFIED EXACT (the clean identity Chat-1 found):
    g = -R * L^-1        (the commensurator's order-3 element = the signed ratio of the letters)
    g^-1 * a = -L        (a = R)

CORRECTION (verify-don't-trust on Chat-1): Chat-1 labelled 'product -> E6 gauge, ratio -> generations'.
That is WRONG-ended -- the product RL has disc 5 (Q(sqrt5) -> E8, the golden/monodromy end); the
ratio g has disc -3 (Q(sqrt-3) -> E6, which carries BOTH the gauge center Z/3 (Level 3) and the
commensurator generation Z/3 (Level 4)). So: PRODUCT = the sqrt5/E8 end; RATIO = the sqrt-3/E6 end.
Also the founding-chain conflation 'golden ratio -> Q(sqrt-3)' is wrong: the golden ratio is in
Q(sqrt5), omega in Q(sqrt-3); two distinct fields (they coexist in Delta=x^2-3x+1 per B326, neither
produces the other).

NOT BANKED (flagged, honest): the overlap index [Gamma : Gamma cap g Gamma g^-1] = 3 (reported by
Chat-1) -- here g commensurates Gamma (gag^-1 = L^-1, not obviously in <a,b>), so index >1 is
plausible, but =3 is NOT verified (needs the Bianchi-group computation). The '1/4 suppression' and
'16 = 4 + h(E6)' hooks are DEAD (null test failed; internal-arithmetic inconsistent).

Firewalled: an exact algebraic structural fact tying the axiom's letters to the two ends; no value.
Nothing to CLAIMS. Needs only sympy.
"""
import sympy as sp

R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])
g = sp.Matrix([[0, -1], [1, -1]])
a = R                                     # Chat-1's Riley generator a = [[1,1],[0,1]]
lam = sp.Symbol('lambda')


def identity_g_is_signed_ratio():
    """g = -R L^-1  and  g^-1 a = -L, exact."""
    return (sp.simplify(g - (-(R * L.inv()))) == sp.zeros(2),
            sp.simplify(g.inv() * a - (-L)) == sp.zeros(2))


def end_of(M):
    """(trace, disc of charpoly) -> which end. disc 5 = Q(sqrt5)/E8; disc -3 = Q(sqrt-3)/E6."""
    disc = sp.discriminant(sp.Poly(M.charpoly(lam).as_expr(), lam), lam)
    return int(M.trace()), int(disc)


def product_and_ratio_ends():
    return {"product RL": end_of(R * L), "ratio g=-RL^-1": end_of(g)}


def g_commensurates_not_normalizes():
    """gag^-1 = L^-1 (a real SL(2,Z) element) -> g is commensurating, not a normalizer."""
    return sp.simplify(g * a * g.inv())


if __name__ == "__main__":
    i1, i2 = identity_g_is_signed_ratio()
    print("g = -R L^-1 :", i1, "   g^-1 a = -L :", i2)
    print("ends (trace, disc):", product_and_ratio_ends())
    print("  product RL: disc 5 -> Q(sqrt5) -> E8 (golden);  ratio g: disc -3 -> Q(sqrt-3) -> E6 (Eisenstein)")
    print("gag^-1 =", g_commensurates_not_normalizes().tolist(), "= L^-1  (g commensurates; overlap index NOT verified =3)")
