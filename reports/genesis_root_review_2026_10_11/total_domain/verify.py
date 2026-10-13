"""Finite exact safeguards for the authored total-domain proof."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
I4, I6, I24 = s.eye(4), s.eye(6), s.eye(24)
Z4 = s.zeros(4)


def simp(a):
    return a.applyfunc(s.simplify) if isinstance(a, s.MatrixBase) else s.simplify(a)


def zero(a):
    a = simp(a)
    return a == s.zeros(*a.shape) if isinstance(a, s.MatrixBase) else a == 0


def clifford():
    p1 = s.Matrix([[0, 1], [1, 0]])
    p2 = s.Matrix([[0, -s.I], [s.I, 0]])
    p3 = s.diag(1, -1)
    return [s.I*s.kronecker_product(p1, s.eye(2)),
            s.I*s.kronecker_product(p2, s.eye(2)),
            s.I*s.kronecker_product(p3, p1),
            s.I*s.kronecker_product(p3, p2)]


def trace_projector(P):
    cs = clifford()
    gv = s.I*cs[2]*cs[3]
    return s.kronecker_product((I4+gv)/2, P)+s.kronecker_product((I4-gv)/2, I6-P)


@lru_cache(None)
def checks():
    rows = {}
    def ck(label, yes):
        rows[label] = bool(yes)
        if not rows[label]:
            raise AssertionError(label)
    cs = clifford()
    spec = importlib.util.spec_from_file_location('sealed_total_metric', HERE.parent/'total_metric_dirac'/'verify.py')
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    ck('same_clifford_as_full_metric', cs == old.gammas())
    for i in range(4):
        ck(f'skew_{i}', zero(cs[i].H+cs[i]))
        for j in range(4):
            ck(f'clifford_{i}_{j}', zero(cs[i]*cs[j]+cs[j]*cs[i]+(2*I4 if i == j else Z4)))
    gv = s.I*cs[2]*cs[3]
    gt = -cs[0]*cs[1]*cs[2]*cs[3]
    ck('vertical_grading', zero(gv-s.diag(1, -1, 1, -1)))
    ck('total_grading', zero(gt*gt-I4))
    a0 = s.diag(s.I, -s.I)
    b0 = s.Matrix([[0, 1], [-1, 0]])
    aa = s.diag(-a0, a0, -a0)
    bb = s.diag(b0, -b0, -b0)
    ck('actual_puncture_coefficient', zero(aa*bb*aa.inv()*bb.inv()+I6))
    ck('combined_angular_periodic', zero((-I6)*(-I6)-I6))
    xi1, xi2 = s.symbols('xi1 xi2', real=True)
    m = s.Symbol('m', integer=True)
    r = s.Symbol('r', positive=True)
    mass = s.I*(xi1*cs[0]+xi2*cs[1])
    ck('horizontal_mass_hermitian', zero(mass.H-mass))
    ck('horizontal_mass_square', zero(mass*mass-(xi1**2+xi2**2)*I4))
    pot = s.I*m*cs[3]/r+mass
    ck('normal_square_first_derivative', zero(cs[2]*pot+pot*cs[2]))
    ck('normal_square_zeroth', zero(cs[2]*pot.diff(r)+pot*pot
        -((m*m*I4-m*gv)/r**2+(xi1**2+xi2**2)*I4)))
    ck('mass_anticommutes_radial', zero(mass*cs[2]+cs[2]*mass))
    ck('mass_anticommutes_angular', zero(mass*cs[3]+cs[3]*mass))
    for k in range(-8, 9):
        ck(f'angular_potentials_{k}', k*(k-1) >= 0 and k*(k+1) >= 0)
    ck('half_shift_control', s.Rational(1, 2)*(s.Rational(1, 2)-1) < 0)
    # Check the integrated scalar identity before any normal-family result.
    f, fp = s.symbols('f fp', real=True)
    radial_square = (fp-m*f/r)**2
    rhs = fp**2+m*(m-1)*f**2/r**2
    boundary_derivative = -m*(2*f*fp/r-f**2/r**2)
    ck('radial_integration_by_parts_plus', zero(radial_square-rhs-boundary_derivative))
    radial_square = (fp+m*f/r)**2
    rhs = fp**2+m*(m+1)*f**2/r**2
    boundary_derivative = m*(2*f*fp/r-f**2/r**2)
    ck('radial_integration_by_parts_minus', zero(radial_square-rhs-boundary_derivative))

    z = s.Symbol('z', real=True)
    directions = [('rational_circle', (1-z*z)/(1+z*z), 2*z/(1+z*z)),
                  ('omitted_circle_point', -s.Integer(1), s.Integer(0))]
    U = s.eye(6)
    for k in (0, 2, 4):
        U[k:k+2, k:k+2] = s.Matrix([[s.Rational(3, 5), 4*s.I/5], [4*s.I/5, s.Rational(3, 5)]])
    ck('complex_basis_unitary', zero(U.H*U-I6))
    for label, a, b in directions:
        M = s.I*(a*cs[0]+b*cs[1])
        Q = simp(cs[2]*M)
        C = simp((I4-Q)/2)
        ck(label+'_unit_covector', zero(a*a+b*b-1))
        ck(label+'_normal_involution', zero(Q*Q-I4))
        ck(label+'_normal_hermitian', zero(Q.H-Q))
        ck(label+'_stable_projection', zero(C*C-C))
        ck(label+'_decaying_equation', zero((-cs[2]+M)*C))
        C24 = s.kronecker_product(C, I6)
        R24 = s.kronecker_product(cs[2], I6)
        M24 = s.kronecker_product(M, I6)
        G24 = s.kronecker_product(gt, I6)
        V24 = s.kronecker_product(gv, I6)
        for rank in range(7):
            p = s.diag(*([1]*rank+[0]*(6-rank)))
            for basis, coeff in [('coordinate', p), ('complex_rotated', U*p*U.H)]:
                P = trace_projector(coeff)
                name = f'{label}_{rank}_{basis}'
                ck(name+'_projector', zero(P*P-P) and zero(P.H-P))
                ck(name+'_half_dimension', s.trace(P) == 12)
                ck(name+'_green', zero(P*R24*P))
                ck(name+'_radial_complement', zero(R24*P-(I24-P)*R24))
                ck(name+'_horizontal_domain', zero(P*M24-M24*P))
                ck(name+'_total_grade', zero(P*G24-G24*P))
                ck(name+'_vertical_grade', zero(P*V24-V24*P))
                ck(name+'_allowed_calderon_angle', zero(P*C24*P-P/2))
                ck(name+'_forbidden_calderon_angle', zero((I24-P)*C24*(I24-P)-(I24-P)/2))
                ck(name+'_energy_boundary_zero', zero(P*R24*M24*P))

    M0 = s.I*cs[0]
    bad = (I4-cs[2]*M0)/2
    ck('bad_plane_green_isotropic', zero(bad*cs[2]*bad))
    ck('bad_plane_half_dimension', bad.rank() == 2)
    ck('bad_plane_total_graded', zero(bad*gt-gt*bad))
    ck('bad_plane_not_vertical_graded', not zero(bad*gv-gv*bad))
    ck('bad_plane_not_horizontal_invariant', not zero(bad*M0-M0*bad))
    h = next(bad[:, j] for j in range(4) if bad[:, j] != s.zeros(4, 1))
    psi = s.exp(-r)*h
    ck('bad_plane_actual_zero_solution', zero(cs[2]*psi.diff(r)+M0*psi))
    ck('bad_plane_actual_trace', zero(bad*h-h))
    norm = s.integrate((psi.H*psi)[0], (r, 0, s.oo))
    ck('bad_plane_finite_positive_norm', bool(norm > 0) and norm.is_finite is True)
    ck('bad_plane_fails_angle', not zero(bad*bad*bad-bad/2))

    y, ell, R, slope = s.symbols('y ell R slope', positive=True)
    cutoff_norm2 = (y/ell)**2*(slope/(R*y))**2
    ck('full_metric_cusp_cutoff_bound', zero(cutoff_norm2-slope**2/(ell**2*R**2)))
    wrong_norm2 = (y*y/ell)**2*(slope/(R*y))**2
    ck('incomplete_metric_cutoff_control', zero(wrong_norm2-y*y*slope**2/(ell**2*R**2))
       and s.limit(wrong_norm2, y, s.oo) == s.oo)
    ck('complete_cusp_distance', s.integrate(ell/y, (y, 1, s.oo)) == s.oo)
    ck('incomplete_control_distance', s.integrate(ell/y**2, (y, 1, s.oo)) == ell)
    return rows


if __name__ == '__main__':
    rows = checks()
    print(json.dumps({'checks': rows, 'passed': len(rows),
        'scope': 'finite exact safeguards; authored closure argument in PROOF; no Fredholm index'}, indent=2))
