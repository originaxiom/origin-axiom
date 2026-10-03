"""R82 separate rational jets; no SymPy or native producer imports."""
from fractions import Fraction as F
import itertools
import json


def run():
    checks = []
    fixtures = []
    for x, f, derivatives, orient in itertools.product(
            (F(-2), F(0), F(3)), (F(1, 2), F(1), F(2)),
            ((F(0), F(0), F(0)), (F(2), F(-1), F(3))), (F(-1), F(1))):
        fx, fy, fz = derivatives
        components = (F(0), x*f, orient*f)
        curl = (orient*fy - x*fz, -orient*fx, f + x*fx)
        density = -2*sum(a*b for a, b in zip(components, curl))
        expected = -2*orient*f*f
        predicates = [density == expected, density != 0, any(curl),
                      2*density == -4*orient*f*f,
                      -2*(components[1]*curl[1]+components[2]*curl[2]) == expected]
        checks.extend(map(bool, predicates))
        fixtures.append(dict(x=str(x), f=str(f), orientation=str(orient),
                             density=str(density), pass_=all(predicates)))
    for c, v in ((F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5)),
                 (F(5, 13), F(12, 13))):
        # Components (0,cos x,sin x), curl (0,-cos x,-sin x).
        density = -2*(c*(-c) + v*(-v))
        checks.extend([c*c + v*v == 1, density == 2, bool(c or v)])
    principal_dimension = sum(2*m+1 for m in (1, 4, 5, 7, 8, 11))
    # Closed form sum of squares; native sums each weight separately.
    principal_trace = -sum(F(4, 3)*m*(m+1)*(2*m+1) for m in (1, 4, 5, 7, 8, 11))
    hessian_phi = ((0, 1, 0), (1, 0, 0), (0, 0, 2))
    gradient_curl = (hessian_phi[1][2]-hessian_phi[2][1],
                     hessian_phi[2][0]-hessian_phi[0][2],
                     hessian_phi[0][1]-hessian_phi[1][0])
    checks.extend([principal_dimension == 78, principal_trace == -7488,
                   gradient_curl == (0, 0, 0)])
    return dict(scope='Rational formal jets only; not a smooth bump, contour or quantum integral',
                contact_fixtures=fixtures, periodic_fixtures=4, checks=len(checks),
                passed=sum(checks), all_checks_pass=all(checks),
                principal_trace=str(principal_trace))


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
