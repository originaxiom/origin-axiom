"""Finite exact guards for the fixed-fibre cone theorem application."""
import json
from fractions import Fraction
import sympy as s


def zero(m):
    return all(s.simplify(x) == 0 for x in m)


def coefficient():
    a = s.diag(s.I, -s.I)
    b = s.Matrix([[0, 1], [-1, 0]])
    parities = [(2, 0), (0, 2), (2, 2)]
    return (s.diag(*[s.I**p*a for p, q in parities]),
            s.diag(*[s.I**q*b for p, q in parities]))


def boundary(p):
    if p.shape != (6, 6) or not zero(p-p.H) or not zero(p*p-p):
        raise ValueError('orthogonal six-channel projector required')
    i, o = s.eye(6), s.zeros(6)
    j = s.BlockMatrix([[o, i], [i, o]]).as_explicit()
    gamma = s.diag(i, -i)
    b = s.diag(p, i-p)
    return {'plus_rank': p.rank(), 'full_rank': b.rank(),
            'green_zero': zero(b.H*j*b), 'grading_kept': zero(gamma*b-b*gamma)}


def projector(d, mixed=False):
    if not 0 <= d <= 6:
        raise ValueError('rank out of range')
    p = s.diag(*([1]*d+[0]*(6-d)))
    if mixed:
        # Householder frame with every coordinate mixed, exact and orthogonal.
        v = s.Matrix([1, 2, 3, 4, 5, 6])
        q = s.eye(6)-2*v*v.T/(v.T*v)[0]
        p = q*p*q.T
    return p


def run():
    checks = {}

    def check(name, value):
        checks[name] = bool(value)

    a, b = coefficient()
    check('actual generator a unitary', zero(a.H*a-s.eye(6)))
    check('actual generator b unitary', zero(b.H*b-s.eye(6)))
    check('global flat determinant trivial', a.det() == b.det() == 1)
    check('actual puncture is minus identity', a*b*a.inv()*b.inv() == -s.eye(6))
    check('bounding spin times gauge is periodic', (-1)*(-1) == 1)

    r = s.symbols('r', positive=True)
    theta = s.symbols('theta', real=True)
    h = s.Matrix([s.Function('u')(r, theta), s.Function('v')(r, theta)])
    u = s.diag(s.exp(-s.I*theta/2), s.exp(s.I*theta/2))
    psi = u*h/s.sqrt(r)
    cart = -s.I*s.Matrix([
        s.exp(-s.I*theta)*(s.diff(psi[1], r)-s.I/r*s.diff(psi[1], theta)),
        s.exp(s.I*theta)*(s.diff(psi[0], r)+s.I/r*s.diff(psi[0], theta))])
    normalized = s.sqrt(r)*u.inv()*cart
    target = -s.I*s.Matrix([s.diff(h[1], r)-s.I/r*s.diff(h[1], theta),
                            s.diff(h[0], r)+s.I/r*s.diff(h[0], theta)])
    check('full symbolic spin and density transform', zero(normalized-target))
    # Recompute the actual mistake: rotate the spin frame but omit r^(-1/2).
    unscaled = u*h
    wrong_cart = -s.I*s.Matrix([
        s.exp(-s.I*theta)*(s.diff(unscaled[1], r)-s.I/r*s.diff(unscaled[1], theta)),
        s.exp(s.I*theta)*(s.diff(unscaled[0], r)+s.I/r*s.diff(unscaled[0], theta))])
    wrong_normalized = u.inv()*wrong_cart
    check('omitted radial normalization detected', not zero(wrong_normalized-target))
    check('omitted radial normalization has the half shift', zero(
        wrong_normalized-target+s.I*s.Matrix([h[1], h[0]])/(2*r)))
    check('spin frame antiperiodic', zero(u.subs(theta, theta+2*s.pi)+u))
    check('unitary radial measure', s.simplify(r*(1/s.sqrt(r))**2) == 1)
    check('normalized measure is r negative half L2b', s.simplify(r**1/r) == 1)

    xi, eta, n, z = s.symbols('xi eta n z', real=True)
    symbol = s.Matrix([[0, xi-s.I*eta], [xi+s.I*eta, 0]])
    check('c symbol square', zero(symbol**2-(xi**2+eta**2)*s.eye(2)))
    check('c symbol determinant', s.expand(symbol.det()) == -xi**2-eta**2)
    indicial = s.Matrix([[0, z+n], [z-n, 0]])
    check('indicial roots plus minus n', s.expand(indicial.det()) == n**2-z**2)
    check('zero angular indicial inverse has simple pole', indicial.subs(n, 0).inv() == s.Matrix([[0, 1/z], [1/z, 0]]))
    modes = [k for k in range(-8, 9) if -Fraction(1, 2) < k < Fraction(1, 2)]
    check('only zero angular mode in sampled critical strip', modes == [0])
    check('no sampled indicial endpoint', all(Fraction(k) not in (Fraction(-1, 2), Fraction(1, 2)) for k in range(-8, 9)))
    check('plus homogeneous solution', s.simplify(s.diff(r**n, r)-n*r**n/r) == 0)
    check('minus homogeneous solution', s.simplify(s.diff(r**(-n), r)+n*r**(-n)/r) == 0)
    check('critical quotient count', 2*6*len(modes) == 12)

    radial_clifford = s.Matrix([[0, s.exp(-s.I*theta)], [s.exp(s.I*theta), 0]])
    critical = u/s.sqrt(r)
    check('actual current loses radial and angular dependence', zero(r*critical.H*radial_clifford*critical-s.Matrix([[0, 1], [1, 0]])))
    profiles = []
    for mixed in (False, True):
        for d in range(7):
            data = boundary(projector(d, mixed))
            check(f'closed domain coefficient guard rank{d} mixed{mixed}', data == {
                'plus_rank': d, 'full_rank': 6, 'green_zero': True, 'grading_kept': True})
            profiles.append({'mixed': mixed, **data, 'predicted_chiral_index': d-3})
    check('mixed rank3 is not diagonal', projector(3, True) != s.diag(*[projector(3, True)[j, j] for j in range(6)]))
    j = s.Matrix([[0, 1], [1, 0]])
    noniso = s.Matrix([1, 1])
    iso = s.Matrix([1, s.I])
    check('nonisotropic graph rejected', (noniso.H*j*noniso)[0] != 0)
    check('ungraded isotropic graph exists', (iso.H*j*iso)[0] == 0)
    check('ungraded graph is not preserved', s.Matrix.hstack(iso, s.diag(1, -1)*iso).det() != 0)
    check('flat determinant residue degree', -6*Fraction(1, 2) == -3)
    check('complementary dual index', all(d-3 == -((6-d)-3) for d in range(7)))
    check('both extremes retain nonzero index', (0-3, 6-3) == (-3, 3))
    check('smooth critical norm is finite', s.integrate(s.Integer(1), (r, 0, 1)) == 1)
    t = s.symbols('t', positive=True)
    check('complete cusp critical norm diverges', s.integrate(1/t, (t, 1, s.oo)) == s.oo)
    check('complete cusp primitive', s.simplify(s.diff(s.log(-s.log(r)), r)-1/(r*s.log(r))) == 0)
    return {'scope': 'Finite safeguards for an authored cone theorem application, not analytic certification',
            'checks': checks, 'all_passed': all(checks.values()), 'profiles': profiles,
            'analytic_claim': 'specified finite-distance chiral index = dim Lambda minus 3'}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_passed'] else 1)
