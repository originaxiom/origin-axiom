r"""Where does Q(sqrt-3) first acquire a class group -- and is it the cusp?

The companion arc showed the cusp lattice is Z + 4Z[omega], the order of
CONDUCTOR 4, and that this forces the congruence level from below.

The seam control then redirected: the largest family of separations in this
corpus is not being/hearing (15%) but FIELD / GALOIS / CONDUCTOR / LEVEL (33%).
So the arithmetic question is the one to push, and the sharpest available is:

    Q(sqrt-3) has class number 1. Its ORDERS need not. At which conductor does
    the class group first become nontrivial -- and is that the cusp's?

Computed by brute-force enumeration of reduced PRIMITIVE binary quadratic forms
of discriminant D = -3 f^2, which is the class number of the order of conductor
f. No table is consulted; the forms are counted.

Gate 5-Q. Structure only.
"""
from math import gcd


def reduced_primitive_forms(D):
    """All reduced primitive (a,b,c) with b^2 - 4ac = D < 0."""
    out = []
    a = 1
    while 3 * a * a <= -D:                      # a <= sqrt(-D/3) for reduced
        for b in range(-a + 1, a + 1):
            num = b * b - D
            if num % (4 * a):
                continue
            c = num // (4 * a)
            if c < a:
                continue
            if gcd(gcd(abs(a), abs(b)), abs(c)) != 1:      # primitive only
                continue
            # reduction boundary conventions: b >= 0 when a == c or |b| == a
            if (a == c or b == a) and b < 0:
                continue
            out.append((a, b, c))
        a += 1
    return out


def main():
    dK = -3
    print('CLASS NUMBER OF THE ORDERS OF Q(sqrt-3), BY CONDUCTOR')
    print('=' * 62)
    print(f'  {"f":>3}  {"disc = -3f^2":>13}  {"h":>3}   reduced primitive forms')
    first = None
    for f in range(1, 13):
        D = dK * f * f
        forms = reduced_primitive_forms(D)
        h = len(forms)
        if h > 1 and first is None:
            first = f
        mark = '   <== FIRST h > 1' if f == first and h > 1 else ''
        show = ', '.join(str(t) for t in forms[:4])
        if h > 4:
            show += ', ...'
        print(f'  {f:>3}  {D:>13}  {h:>3}   {show}{mark}')

    print()
    print(f'  first conductor with a nontrivial class group : f = {first}')
    assert first == 4, f'expected 4, got {first}'
    print('  the cusp lattice is the order of conductor     : f = 4')
    print('  the congruence level of Gamma_41 is            : (4)')
    print()
    print('  So the object sits at the SMALLEST conductor at which its own')
    print('  field acquires a class group at all -- h = 1, 1, 1, 2 for')
    print('  f = 1, 2, 3, 4 -- and the class group there is Z/2.')
    print('=' * 62)
    # the class group at f = 4, named
    forms4 = reduced_primitive_forms(-48)
    print(f'\n  Cl(O_4) has order {len(forms4)}: {forms4}')
    print('  principal form (1,0,12); the nontrivial class (3,0,4).')
    print('  Cl(O_4) = Z/2.')


if __name__ == '__main__':
    main()
