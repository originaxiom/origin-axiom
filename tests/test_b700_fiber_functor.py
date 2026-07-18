"""B700 cell 1 lock — the golden measurement torsor (pyenv-pure, sympy).
The two golden 2-dim irreps of 2I=SL(2,5) (character rows sage-verified,
stored as zeta_5 polynomials) are swapped simply-transitively by the Galois
automorphism tau: zeta5 -> zeta5^2 = the nontrivial elt of Gal(Q(sqrt5)/Q).
=> {golden irreps} is a Z/2 torsor = the fiber-functor ambiguity."""
import sympy as sp

z = sp.symbols('z')                       # zeta_5, root of 1+z+z^2+z^3+z^4
cyc = 1 + z + z**2 + z**3 + z**4

def reduce5(expr):
    """reduce a polynomial in z modulo the 5th cyclotomic (z^4 = -(1+z+z^2+z^3))."""
    p = sp.Poly(sp.expand(expr), z)
    r = p.rem(sp.Poly(cyc, z))
    return sp.expand(r.as_expr())

# the two golden irreps' character rows (sage-verified, in Q(zeta5))
rA = [2, z**3+z**2+1, -z**3-z**2, -2, -z**3-z**2-1, z**3+z**2, -1, 1, 0]
rB = [2, -z**3-z**2, z**3+z**2+1, -2, z**3+z**2, -z**3-z**2-1, -1, 1, 0]

def tau(expr):                            # zeta5 -> zeta5^2
    return reduce5(expr.subs(z, z**2) if hasattr(expr, 'subs') else expr)


def test_two_golden_irreps_swapped_simply_transitively():
    # tau(A) == B  (swap) and tau(A) != A (no fixed point) -> simply-transitive torsor
    tA = [tau(sp.sympify(v)) for v in rA]
    Bred = [reduce5(sp.sympify(v)) for v in rB]
    Ared = [reduce5(sp.sympify(v)) for v in rA]
    assert tA == Bred, "tau must swap irrep A -> irrep B (the torsor)"
    assert tA != Ared, "tau must NOT fix A (no Galois-fixed golden irrep)"
    # tau is an involution on the pair (order 2)
    ttA = [tau(v) for v in tA]
    assert ttA == Ared, "tau^2 = id on the pair (Z/2)"


def test_golden_values_are_the_sqrt5_orbit():
    # z^3+z^2 = (-1-sqrt5)/2 ; so z^3+z^2+1 = (1-sqrt5)/2 = -1/phi ; -(z^3+z^2)=(1+sqrt5)/2=phi
    s = sp.sqrt(5)
    val_phi = sp.Rational(1, 2) * (1 + s)          # phi
    val_neg_inv = sp.Rational(1, 2) * (1 - s)      # -1/phi
    # numeric identification of z^3+z^2 with (-1-sqrt5)/2
    zc = sp.exp(2*sp.pi*sp.I/5)
    approx = complex((zc**3 + zc**2))
    assert abs(approx - complex((-1 - 5**0.5)/2)) < 1e-9
    # phi * (-1/phi) = -1 (golden), and phi + (-1/phi) = 1 (the trace pair)
    assert sp.simplify(val_phi * val_neg_inv) == -1
    assert sp.simplify(val_phi + val_neg_inv) == 1
