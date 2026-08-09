r"""Is the cusp's CM conductor the SAME 4 as the congruence level?

Two 4s were observed: the boundary torus has CM by the order of conductor 4 in
Q(sqrt-3), and Gamma_41 is a congruence subgroup of level exactly (4). The prior
was "the same fact seen twice". This decides it.

THE ARGUMENT, and it is elementary once stated:

  * the peripheral (cusp) lattice is  Lambda = Z + Z*2sqrt(-3)
  * Gamma(n) <= Gamma_41 requires the translations of Gamma(n) at the cusp to
    lie in Lambda, i.e.  n*Z[omega] <= Lambda
  * so the LEVEL IS BOUNDED BELOW BY THE CUSP: any n with n*Z[omega] not
    contained in Lambda is excluded, with no reference to the rest of the group

So if 4Z[omega] <= Lambda and 2Z[omega] is NOT <= Lambda, the cusp alone forbids
level 1 and 2 -- and the banked level 4 is then forced from below by the cusp's
own arithmetic rather than being an independent coincidence.

Everything below is exact arithmetic in Z[omega], omega = (-1 + sqrt-3)/2.

Gate 5-Q. Structure only.
"""
import sympy as sp

w = sp.Rational(-1, 2) + sp.sqrt(-3) / 2          # omega, primitive cube root
tau = 2 * sp.sqrt(-3)                              # the banked cusp shape


def in_lattice(z):
    """Is z in Lambda = Z + Z*tau?  Solve z = a + b*tau over the rationals."""
    a, b = sp.symbols('a b', rational=True)
    sol = sp.solve(sp.Eq(sp.expand(a + b * tau - z), 0), [a, b], dict=True)
    if not sol:
        # split into rational and sqrt(-3) parts by hand
        z = sp.expand(z)
        re = sp.simplify((z + sp.conjugate(z)) / 2)
        im = sp.simplify((z - sp.conjugate(z)) / (2 * sp.sqrt(-3)))
        # z = re + im*sqrt(-3);  tau = 2 sqrt(-3)  =>  b = im/2, a = re
        return sp.ask(sp.Q.integer(re)) and sp.ask(sp.Q.integer(im / 2))
    s = sol[0]
    return all(sp.ask(sp.Q.integer(v)) for v in s.values())


def parts(z):
    """z = re + im*sqrt(-3), returned as exact rationals."""
    z = sp.expand(z)
    re = sp.nsimplify(sp.simplify((z + sp.conjugate(z)) / 2))
    im = sp.nsimplify(sp.simplify((z - sp.conjugate(z)) / (2 * sp.sqrt(-3))))
    return re, im


def in_Lambda(z):
    re, im = parts(z)
    return re.is_Integer and (im * 2).is_Integer and (im / sp.Rational(1, 1)) \
        and sp.Rational(im).q == 1 and sp.Rational(im) % 2 == 0 \
        if im.is_Rational else False


def in_Lambda_clean(z):
    """z in Z + Z*(2 sqrt-3)  <=>  re integer and im an EVEN integer."""
    re, im = parts(z)
    return bool(re.is_Integer and im.is_Integer and (im % 2 == 0))


def main():
    print('IS THE CUSP CONDUCTOR THE CONGRUENCE LEVEL?')
    print('=' * 62)
    print(f'  omega = {sp.nsimplify(w)}      tau = {tau} = 2 sqrt(-3)')

    # --- step 1: identify Lambda as an ideal-theoretic object
    print('\n1. WHAT Lambda IS')
    # tau = 2 sqrt-3 and sqrt-3 = 2w + 1, so tau = 4w + 2
    assert sp.simplify(tau - (4 * w + 2)) == 0
    print('   sqrt(-3) = 2w + 1   =>   tau = 4w + 2')
    print('   Lambda = Z + Z(4w + 2) = Z + 4Zw = Z + 4Z[omega]')
    # verify: a + b(4w+2) = (a+2b) + 4b w, and a+2b sweeps all of Z
    print('   (since a + b(4w+2) = (a+2b) + 4b*w and a+2b sweeps Z)')
    print('   => Lambda is exactly the order of CONDUCTOR 4:  Z + 4Z[omega]')

    # --- step 2: the containment test that bounds the level
    print('\n2. WHICH n*Z[omega] FIT INSIDE Lambda')
    for n in (1, 2, 3, 4, 6, 8):
        gens = [sp.expand(n * 1), sp.expand(n * w)]
        ok = all(in_Lambda_clean(g) for g in gens)
        why = '' if ok else f'   (n*omega = {sp.nsimplify(n*w)} is not in Lambda)'
        print(f'   n = {n}:  n*Z[omega] <= Lambda ?  {ok}{why}')

    # --- step 3: the conclusion
    print('\n3. THE CONCLUSION')
    assert not in_Lambda_clean(sp.expand(2 * w)), '2w must NOT be in Lambda'
    assert in_Lambda_clean(sp.expand(4 * w)), '4w must be in Lambda'
    assert in_Lambda_clean(sp.expand(4 * 1)), '4 must be in Lambda'
    print('   4*Z[omega] <= Lambda        : TRUE')
    print('   2*Z[omega] <= Lambda        : FALSE  (2*omega is not in Lambda)')
    print()
    print('   Gamma(n) <= Gamma_41 requires n*Z[omega] <= Lambda at the cusp.')
    print('   So the CUSP ALONE excludes n = 1 and n = 2, with no input from')
    print('   the rest of the group. The banked level is exactly (4), and the')
    print('   cusp forces it FROM BELOW.')
    print()
    print('   VERDICT: the same 4. NOT a coincidence.')
    print('   The congruence level is the cusp lattice\'s own conductor.')
    print('=' * 62)


if __name__ == '__main__':
    main()
