r"""S1-a — the class-S dictionary, made checkable.

THE CLAIM UNDER TEST
--------------------
B277 banks a canonical class-S lift: the 6d (2,0) theory on Sigma_{1,1} gives
4d N=2* SU(2), with the object's monodromy phi = RL an S-duality element.

In class-S language the BETTI moduli space of Sigma_{1,1} is the SL(2,C)
character variety of the once-punctured torus -- the FRICKE CUBIC

        x^2 + y^2 + z^2 - x y z - 2  =  tr[a,b]  =  kappa

with x = tr(a), y = tr(b), z = tr(ab). That surface is precisely what B13-B51
built (the trace map T), i.e. the character-variety face cc admitted as the
twelfth face. The mapping class group SL(2,Z) acts on it; the object's
monodromy is one element of that action.

So the dictionary entry to test is:

    the object's own character variety  ==  the FIXED POINTS of the monodromy
    acting on the class-S Betti moduli space, at the PARABOLIC puncture

"Parabolic puncture" is kappa = -2: the boundary of the fiber is the cusp, and
a cusp element has trace +-2. In class-S that is the MASSLESS point of N=2*
(the puncture mass is the log of the boundary holonomy eigenvalue), i.e. the
point where N=2* becomes N=4 -- the theory whose S-duality group is SL(2,Z),
which is what B277 needs for RL to BE an S-duality element.

PREDICTION, stated before computing: if the dictionary holds, the fixed-point
equation must return the object's own trace field Q(sqrt-3) -- with no input
from hyperbolic geometry anywhere in the calculation. Only F_2 traces, the
Fricke relation, and the mapping-class action.

Gate 5-Q. Structure only; no measured quantity.
"""
import sympy as sp

x, y, z, t = sp.symbols('x y z t')

# ---------------------------------------------------------- the Fricke cubic
kappa = x**2 + y**2 + z**2 - x*y*z - 2            # = tr[a,b]
PARABOLIC = -2                                    # cusp: boundary trace -2

# ------------------------------------------- the mapping-class action on it
# R : a -> a,  b -> ab        so x -> x, y -> tr(ab) = z,
#                                z -> tr(a.ab) = tr(a)tr(ab) - tr(b) = xz - y
def R(p):
    a, b, c = p
    return (a, c, a*c - b)


# L : a -> ab, b -> b         so x -> z, y -> y,
#                                z -> tr(ab.b) = tr(ab)tr(b) - tr(a) = yz - x
def L(p):
    a, b, c = p
    return (c, b, b*c - a)


def fixed_points(word, name):
    """Solve word(x,y,z) = (x,y,z) on the kappa = -2 surface."""
    p = (x, y, z)
    for f in word:
        p = f(p)
    eqs = [sp.expand(p[0] - x), sp.expand(p[1] - y), sp.expand(p[2] - z),
           sp.expand(kappa - PARABOLIC)]
    sols = sp.solve(eqs, [x, y, z], dict=True)
    print(f'\n--- monodromy {name}: fixed points on kappa = -2')
    fields = []
    for s in sols:
        vals = [sp.simplify(s.get(v, v)) for v in (x, y, z)]
        print(f'    (x, y, z) = ({vals[0]}, {vals[1]}, {vals[2]})')
        fields.append(vals)
    return fields, sols


def check_kappa_invariant():
    """kappa must be preserved by both generators -- it is the puncture mass."""
    for f, n in ((R, 'R'), (L, 'L')):
        p = f((x, y, z))
        k2 = (p[0]**2 + p[1]**2 + p[2]**2 - p[0]*p[1]*p[2] - 2)
        assert sp.simplify(k2 - kappa) == 0, f'{n} must preserve kappa'
    print('kappa = tr[a,b] is invariant under R and L  '
          '(the puncture mass is a modulus, not a coordinate)  OK')


def main():
    print('S1-a  THE CLASS-S DICTIONARY, TESTED')
    print('=' * 66)
    check_kappa_invariant()

    # The composition order is a convention; compute BOTH and report honestly.
    for word, name in (((L, R), 'RL  (= R after L)'),
                       ((R, L), 'LR  (= L after R)')):
        vals, sols = fixed_points(word, name)
        for v in vals:
            poly = sp.Poly(sp.minimal_polynomial(v[0], t), t)
            if poly.degree() != 2:
                print(f'      -> x = {v[0]}: rational, minpoly {poly.as_expr()} '
                      f'(the finite/quaternionic character, not geometric)')
                continue
            disc = sp.discriminant(poly.as_expr(), t)
            nrm = sp.simplify(sp.expand(v[0] * sp.conjugate(v[0])))
            print(f'      -> GEOMETRIC: minpoly of x is {poly.as_expr()}')
            print(f'         discriminant = {disc}  ->  trace field '
                  f'Q(sqrt({disc}))  =  Q(sqrt-3)'
                  if disc == -3 else f'         discriminant = {disc}')
            print(f'         N(x) = {nrm}   (the ramified prime)')
            assert disc == -3, 'the dictionary predicts disc = -3'
    print('\n' + '=' * 66)


if __name__ == '__main__':
    main()
