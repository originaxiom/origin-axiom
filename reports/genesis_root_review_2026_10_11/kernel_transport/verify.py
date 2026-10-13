"""Exact controls for the authored flag complex comparison, not a PDE solver."""
from itertools import combinations
import json
import sympy as s


def zero(matrix):
    return all(s.simplify(x) == 0 for x in matrix)


def exterior_group(matrix):
    pairs = list(combinations(range(matrix.rows), 2))
    return s.Matrix([[matrix.extract(i, j).det() for j in pairs] for i in pairs])


def exterior_lie(matrix):
    pairs = list(combinations(range(matrix.rows), 2))
    z = s.symbols('z')
    return exterior_group(s.eye(matrix.rows) + z*matrix).diff(z).subs(z, 0)


def spin_lift(matrix):
    basis = [s.eye(2), s.Matrix([[0, 1], [1, 0]]),
             s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
    return s.Matrix.hstack(*[s.Matrix([
        s.simplify(s.trace(b*(matrix*x+x*matrix.H))/2) for b in basis
    ]) for x in basis])


def translated_log_difference(r, ell, b, c, alpha, charge, exponent=2):
    bp = b*s.exp(2*c/ell)
    log_k = lambda at, amplitude: -2*at*alpha + ell*amplitude*(
        s.exp(exponent*at/ell)-1)*charge
    return s.simplify(log_k(r+c, b)-log_k(r, bp)
                      - (-2*c*alpha+ell*(bp-b)*charge))


def finite_comparator():
    d0 = s.Matrix([1, 0, 0])
    d1 = s.Matrix([[0, 1, 0], [0, 0, 0]])
    g = s.Matrix([[2, 0, 1], [0, 3, 1], [1, 1, 4]])
    delta0 = d0.T*g
    delta1 = g.inv()*d1.T
    lap = d0*delta0+delta1*d1
    old = d0*d0.T+d1.T*d1
    harmonic = s.Matrix([-s.Rational(1, 2), 0, 1])
    changed = s.Matrix([[0, 1, 0], [0, 0, 1]])
    return d0, d1, g, delta0, delta1, lap, old, harmonic, changed


def run():
    checks = {}

    def ck(name, condition):
        if name in checks:
            raise AssertionError('duplicate: '+name)
        checks[name] = bool(condition)
        if not checks[name]:
            raise AssertionError(name)

    r, c = s.symbols('r c', real=True)
    ell, b, z = s.symbols('ell b z', positive=True)
    n = s.Matrix([[0, 1], [0, 0]])
    a = s.diag(spin_lift(s.diag(1, -1)/(2*ell)), 0)
    nx, ny = [s.diag(spin_lift(x), 0) for x in (-n, -s.I*n)]
    xi = s.diag(1, 1, 1, 1, -4)
    e = s.eye(5)
    u = s.Matrix.hstack((e[:, 0]+e[:, 3])/s.sqrt(2), e[:, 1],
                       e[:, 2], (e[:, 0]-e[:, 3])/s.sqrt(2), e[:, 4])
    ck('orthonormal_frame', zero(u.H*u-e))
    ck('actual_radial_generator', a[0, 3] == 1/ell and a[3, 0] == 1/ell
       and zero(a-(e[:, 0]*e[:, 3].T+e[:, 3]*e[:, 0].T)/ell))
    ad = s.simplify(u.H*a*u)
    xd = s.simplify(u.H*xi*u)
    ck('simultaneous_radial_diagonal', ad == s.diag(1, 0, 0, -1, 0)/ell)
    ck('simultaneous_flag_diagonal', xd == xi)
    ck('radial_flag_commute', zero(a*xi-xi*a))
    for label, t in [('X', nx), ('Y', ny)]:
        ck('nonzero_nonabelian_'+label, not zero(t))
        ck('flag_commutes_'+label, zero(t*xi-xi*t))
        ck('flat_radial_'+label, zero(a*t-t*a-t/ell))
        # Radial temporal transport: exp(-r A) becomes z^(-ell A).
        g = s.diag(*[z**(-ell*ad[i, i]) for i in range(5)])
        td = s.simplify(u.H*t*u)
        ck('full_temporal_tangent_'+label, zero(g.inv()*td*g/z-td))
    ck('flat_tangential', zero(nx*ny-ny*nx))

    f = ell*b*(s.exp(2*r/ell)-1)/2
    for i in range(5):
        scalar = s.exp(-r*ad[i, i]+f*xd[i, i])
        ck('temporal_radial_'+str(i), s.simplify(s.diff(scalar, r)
           +(ad[i, i]-b*s.exp(2*r/ell)*xd[i, i])*scalar) == 0)
    aw, xw = exterior_lie(ad), exterior_lie(xi)
    ck('wedge_flag_multiplicities', list(xw.diagonal()).count(2) == 6
       and list(xw.diagonal()).count(-3) == 4)
    ck('wedge_flag_not_defining', xw.rows == 10 and set(xw.diagonal()) == {2, -3})
    for label, aa, xx in [('W', ad, xd), ('wedge', aw, xw)]:
        for i in range(aa.rows):
            ck('translation_'+label+'_'+str(i), translated_log_difference(
                r, ell, b, c, aa[i, i], xx[i, i]) == 0)
            ck('translation_dual_'+label+'_'+str(i), translated_log_difference(
                r, ell, b, c, -aa[i, i], -xx[i, i]) == 0)
    c2 = s.symbols('c2', real=True)
    ck('amplitude_composition', s.simplify(
        b*s.exp(2*c/ell)*s.exp(2*c2/ell)-b*s.exp(2*(c+c2)/ell)) == 0)
    ck('amplitude_inverse', s.simplify(b*s.exp(2*c/ell)*s.exp(-2*c/ell)-b) == 0)
    ck('zero_stays_zero_under_finite_translation', (b*s.exp(2*c/ell)).subs(b, 0) == 0)
    ck('finite_translation_preserves_positive_sign', (b*s.exp(2*c/ell)).is_positive is True)
    ck('wrong_radial_exponent_detected', translated_log_difference(
        r, ell, b, c, 1/ell, 1, exponent=1) != 0)
    omitted = ell*b*(s.exp(2*c/ell)-1)
    ck('omitted_constant_flag_factor_detected', s.simplify(omitted) != 0)
    log_same_point_ratio = ell*b*(z-1)  # b'=2b, Xi weight +1, z=exp(2r/ell).
    ck('identity_comparison_unbounded', s.limit(log_same_point_ratio, z, s.oo) == s.oo)
    ck('identity_inverse_unbounded_in_fifth', s.limit(4*log_same_point_ratio, z, s.oo) == s.oo)
    for j in range(3):
        density = s.exp((2*j-2)*r/ell)
        ck('base_density_degree_'+str(j), s.simplify(density.subs(r, r+c)/density
           - s.exp((2*j-2)*c/ell)) == 0)

    d0, d1, gram, delta0, delta1, lap, old, harmonic, changed = finite_comparator()
    ck('finite_nilpotent', zero(d1*d0))
    ck('finite_positive_nondiagonal_norm', all(gram[:i, :i].det() > 0 for i in (1, 2, 3)))
    ck('finite_adjoint_zero_slot', delta0 == s.Matrix([[2, 0, 1]]))
    ck('finite_adjoint_one_slot', zero(gram*delta1-d1.T))
    ck('finite_harmonic_closed', zero(d1*harmonic))
    ck('finite_harmonic_coclosed', zero(delta0*harmonic))
    ck('finite_changed_harmonic_representative', not zero(harmonic-s.Matrix([0, 0, 1]))
       and zero((harmonic-s.Matrix([0, 0, 1]))+d0/2))
    ck('finite_old_representative_not_new_harmonic', delta0*s.Matrix([0, 0, 1]) != s.zeros(1, 1))
    ck('finite_same_cohomology_dimension', 3-d1.rank()-d0.rank() == 1
       and len(lap.nullspace()) == len(old.nullspace()) == 1)
    ck('finite_positive_spectral_trace_changes', s.trace(old) == 2
       and s.trace(lap) == s.Rational(45, 19))
    ck('finite_changed_D_still_nilpotent', zero(changed*d0))
    ck('finite_changed_D_changes_cohomology', 3-changed.rank()-d0.rank() == 0)
    # Exterior Gram matrices from actual determinants, not assigned eigenvalues.
    g5 = s.diag(gram, 2, 3)
    exterior = exterior_group(g5)
    ck('exterior_gram_positive', all(exterior[:i, :i].det() > 0 for i in range(1, 11)))
    ck('exterior_inverse_functor', zero(exterior_group(g5.inv())-exterior.inv()))
    ck('exterior_not_entrywise_square', exterior[0, 0] == 6 and exterior[0, 0] != g5[0, 0]**2)
    return {'checks': checks, 'passed': sum(checks.values()),
            'scope': 'exact algebra and countercontrols for an authored complete-complex comparison',
            'global_mode_count_computed': False, 'analytic_proof_machine_certified': False,
            'physical_parent_or_end_selection_derived': False}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
