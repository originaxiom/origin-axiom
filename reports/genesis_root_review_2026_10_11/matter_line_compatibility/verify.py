"""Exact safeguards for a fixed-parent flavour pairing, not a physical spectrum."""
import json
import sympy as s

facts = {}


def check(name, value):
    if name in facts:
        raise AssertionError('duplicate predicate: ' + name)
    facts[name] = bool(value)
    if not facts[name]:
        raise AssertionError(name)


def equal(a, b):
    if isinstance(a, s.MatrixBase):
        return all(s.simplify(x) == 0 for x in a-b)
    return s.simplify(a-b) == 0


def comm(a, b):
    return a*b-b*a


def norm(a):
    return s.trace(a.H*a)


J = s.Matrix([[0, 1], [-1, 0]])
a, b, c, d = s.symbols('a b c d')
U = s.Matrix([[a, b], [c, d]])
check('arbitrary_pairing_determinant', equal(U.T*J*U, U.det()*J))
Q = s.Matrix(2, 2, s.symbols('q0:4'))
R = s.Matrix(2, 2, s.symbols('r0:4'))
check('arbitrary_nonabelian_commutator', equal(
    comm(a*Q+b*R, c*Q+d*R), U.det()*comm(Q, R)))

Q = s.Matrix([[1+s.I, 2], [0, -1-s.I]])
R = s.Matrix([[s.I, 0], [3, -s.I]])
check('noncommuting_fixture', not equal(comm(Q, R), s.zeros(2)))
samples = (s.eye(2), s.diag(s.I, -s.I), J,
           s.Matrix([[1, 1], [-1, 1]])/s.sqrt(2), -s.eye(2))
for i, V in enumerate(samples):
    q, r = V[0, 0]*Q+V[0, 1]*R, V[1, 0]*Q+V[1, 1]*R
    check(f'su2_unitary_{i}', equal(V.H*V, s.eye(2)))
    check(f'su2_determinant_{i}', equal(V.det(), 1))
    check(f'su2_pairing_{i}', equal(V.T*J*V, J))
    check(f'su2_kinetic_{i}', equal(norm(q)+norm(r), norm(Q)+norm(R)))
    check(f'su2_moment_{i}', equal(
        comm(q, q.H)+comm(r, r.H), comm(Q, Q.H)+comm(R, R.H)))
    check(f'su2_cubic_{i}', equal(comm(q, r), comm(Q, R)))

V = s.diag(s.I, 1)
check('u2_non_su2_unitary', equal(V.H*V, s.eye(2)))
check('u2_non_su2_kinetic', equal(norm(s.I*Q)+norm(R), norm(Q)+norm(R)))
check('u2_non_su2_bosonic_cubic_norm', equal(norm(comm(s.I*Q, R)), norm(comm(Q, R))))
check('u2_non_su2_pairing_rejected', not equal(V.T*J*V, J))
x, dx = s.Matrix([1, 2]), s.Matrix([3, 5])
check('superpotential_witness_nonzero', (x.T*J*dx)[0] != 0)
check('superpotential_phase_detected', not equal((x.T*V.T*J*V*dx)[0], (x.T*J*dx)[0]))
V = s.diag(2, s.Rational(1, 2))
check('sl2_pairing_kept', equal(V.T*J*V, J))
check('sl2_nonunitary_rejected', not equal(V.H*V, s.eye(2)))
check('sl2_kinetic_changes', not equal(norm(2*Q)+norm(R/2), norm(Q)+norm(R)))

alpha, beta, f = s.symbols('alpha beta f', real=True)
H = s.diag(alpha, beta)
check('infinitesimal_charge_sum', equal(H.T*J+J*H, (alpha+beta)*J))
check('opposite_charge_pairing', equal((H.T*J+J*H).subs(beta, -alpha), s.zeros(2)))
check('common_charge_rejected', not equal((H.T*J+J*H).subs({alpha: 1, beta: 1}), s.zeros(2)))
check('paired_curvature_trace', equal(s.trace(s.diag(alpha*f, -alpha*f)), 0))
check('common_curvature_defect', equal(s.diag(f, f).T*J+J*s.diag(f, f), 2*f*J))
check('common_nonzero_curvature_rejected', not equal((2*f*J).subs(f, 1), s.zeros(2)))
check('common_zero_curvature_control', equal((2*f*J).subs(f, 0), s.zeros(2)))

t = s.symbols('t', real=True)
theta = s.Function('theta', real=True)(t)
bg = s.Function('bg', real=True)(t)
q, r = s.Function('q')(t), s.Function('r')(t)
phase = s.exp(s.I*theta)
def cov(field, charge, connection):
    return s.diff(field, t)+s.I*charge*connection*field
newbg = bg-s.diff(theta, t)
check('local_q_covariance', equal(cov(phase*q, 1, newbg), phase*cov(q, 1, bg)))
check('local_r_covariance', equal(cov(r/phase, -1, newbg), cov(r, -1, bg)/phase))
check('omitted_connection_compensator_detected', equal(
    cov(phase*q, 1, bg)-phase*cov(q, 1, bg), s.I*s.diff(theta, t)*phase*q))
check('omitted_compensator_nonzero', not equal(
    (s.I*s.diff(theta, t)*phase*q).subs(theta, t).doit().subs(q, 1), 0))
old = q*cov(r, -1, bg)-r*cov(q, 1, bg)
new = phase*q*cov(r/phase, -1, newbg)-r/phase*cov(phase*q, 1, newbg)
check('local_paired_bilinear_covariance', equal(new, old))

X, Y = s.Matrix([[0, 1], [0, 0]]), s.Matrix([[0, 0], [1, 0]])
Z = s.diag(1, -1)
scalar = s.symbols('scalar')
defect = scalar*comm(X, Y)-comm(scalar*X, Y)-comm(X, scalar*Y)
check('nonabelian_bracket_witness', not equal(comm(X, Y), s.zeros(2)))
check('scalar_derivation_defect', equal(defect, -scalar*comm(X, Y)))
check('nonzero_scalar_not_derivation', not equal(defect.subs(scalar, 1), s.zeros(2)))
check('zero_scalar_derivation', equal(defect.subs(scalar, 0), s.zeros(2)))
check('inner_derivation_control', equal(comm(Z, comm(X, Y)),
                                      comm(comm(Z, X), Y)+comm(X, comm(Z, Y))))
check('inner_derivation_not_uniform', comm(Z, X) == 2*X and comm(Z, Y) == -2*Y)

if len(facts) != 60:
    raise AssertionError(('unexpected predicate count', len(facts)))
print(json.dumps({'status': 'PASS', 'checks': len(facts), 'facts': facts,
                 'scope': 'fixed-parent bulk pairing and local connection covariance',
                 'physical_domain_certified': False, 'nonzero_flux_selected': False,
                 'genesis_parent_derived': False}, indent=2))
