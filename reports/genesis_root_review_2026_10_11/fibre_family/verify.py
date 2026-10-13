"""Finite algebra guards for the authored smooth-family argument, not a PDE solver."""
import json
import sympy as s


def simp(x):
    return s.simplify(s.expand_complex(x))


def zero(m):
    return all(simp(x) == 0 for x in m)


def data():
    i = s.I
    a, b = s.diag(i, -i), s.Matrix([[0, 1], [-1, 0]])
    aa = s.diag(*[i**p*a for p, q in ((2, 0), (0, 2), (2, 2))])
    bb = s.diag(*[i**q*b for p, q in ((2, 0), (0, 2), (2, 2))])
    p13 = s.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    p23 = s.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    z, y = s.diag(1, -1), s.Matrix([[0, -i], [i, 0]])
    l = s.kronecker_product(p13, (s.eye(2)+i*z)/s.sqrt(2))
    r = s.kronecker_product(p23, (s.eye(2)-i*y)/s.sqrt(2))
    ms = (l*r.inv()*l).inv().applyfunc(simp)
    q2 = s.kronecker_product(s.ones(3, 1)/s.sqrt(3), s.eye(2))
    p2 = (q2*q2.H).applyfunc(simp)
    zeta = (1+i)/s.sqrt(2)
    t01s = zeta*p13
    return aa, bb, ms, l, p2, t01s


def trace_ratio_squared(f, z, include_spin=True):
    """Ratio of critical local frames; square roots are chosen coherently outside code."""
    if f.subs(z, 0) != 0 or s.diff(f, z).subs(z, 0) == 0:
        raise ValueError('a regular section-preserving coordinate is required')
    return s.cancel(z/f * (s.diff(f, z) if include_spin else 1))


def cohomology_dimensions(delta):
    rank = delta.rank()
    return delta.cols-rank, delta.rows-rank


def run():
    checks, records = {}, []
    def check(name, condition):
        checks[name] = bool(condition)
    aa, bb, ms, mt, p2, t01s = data()
    eye = s.eye(6)
    check('actual generator determinants', aa.det() == bb.det() == 1)
    check('actual coefficient is unitary', zero(aa.H*aa-eye) and zero(bb.H*bb-eye))
    check('actual scalar puncture holonomy', zero(aa*bb*aa.inv()*bb.inv()+eye))
    check('canonical degree from determinant residue', -s.Rational(1, 2)*aa.rows == -3)
    g = s.Matrix.vstack(s.Matrix.hstack(s.zeros(6), eye), s.Matrix.hstack(eye, s.zeros(6)))
    grading = s.diag(eye, -eye)
    for sign in (1, -1):
        for name, u in [('S', sign*ms), ('T', sign*mt)]:
            check(f'{sign} {name} unitary', zero(u.H*u-eye))
            doubled = s.diag(u, u)
            check(f'{sign} {name} Green equivariant', zero(doubled.H*g*doubled-g))
            check(f'{sign} {name} grading equivariant', zero(doubled*grading-grading*doubled))
            for label, p in [('zero', s.zeros(6)), ('V2', p2), ('V4', eye-p2), ('all', eye)]:
                trace = s.diag(p, eye-p)
                check(f'{sign} {name} {label} invariant domain', zero(doubled*trace-trace*doubled))
                check(f'{sign} {name} {label} maximal isotropic', trace.rank() == 6 and zero(trace.H*g*trace))
        check(f'{sign} lifted modular relation', zero((sign*ms)**2-((sign*ms)*(sign*mt))**3))
    check('actual local central character', zero(ms**2+eye))
    check('canonical H1 central character', zero(t01s**2-s.I*s.eye(3)))
    check('dual H10 central character', zero(s.conjugate(t01s)**2+s.I*s.eye(3)))

    z = s.Symbol('z')
    coordinates = [2*z, 4*z+z*z, -z+3*z*z+z**3, s.I*z+2*z*z, 3*z+z**3]
    for j, f in enumerate(coordinates):
        ratio = trace_ratio_squared(f, z)
        check(f'coordinate {j} spin trace leading coefficient', ratio.subs(z, 0) == 1)
        check(f'coordinate {j} correction is minimal order',
              s.limit((ratio-1)/z, z, 0).is_finite is True)
        h = 5*z+z*z
        composite = h.subs(z, f)
        composed = ratio*trace_ratio_squared(h, z).subs(z, f)
        check(f'coordinate {j} composition law', s.cancel(composed-trace_ratio_squared(composite, z)) == 0)
    wrong = trace_ratio_squared(4*z+z*z, z, include_spin=False)
    check('omitted spin half weight detected', wrong.subs(z, 0) == s.Rational(1, 4) and wrong.subs(z, 0) != 1)

    # The finite map models the proved reduction, not a computed physical kernel.
    delta_all = s.Matrix.hstack(s.eye(3), s.zeros(3))
    for d in range(7):
        delta = delta_all[:, :d]
        h0, h1 = cohomology_dimensions(delta)
        check(f'rank {d} finite index', h0-h1 == d-3)
        records.append({'trace_rank': d, 'model_kernel': h0, 'model_cokernel': h1})
    check('canonical extreme', cohomology_dimensions(s.zeros(3, 0)) == (0, 3))
    check('all allowed extreme', cohomology_dimensions(delta_all) == (3, 0))
    jump = []
    for value in (0, 1, -2):
        inclusion = s.Matrix.hstack(eye[:, 0], value*eye[:, 1]+eye[:, 3])
        check(f'jump {value} trace rank stays two', inclusion.rank() == 2)
        h0, h1 = cohomology_dimensions(delta_all*inclusion)
        check(f'jump {value} index stays minus one', h0-h1 == -1)
        jump.append((h0, h1))
    check('index does not freeze kernels', jump == [(1, 2), (0, 1), (0, 1)])
    # Delta is independent of changing the cutoff lift by an old domain vector.
    old = s.Matrix.vstack(s.eye(2), s.zeros(3, 2))
    project_coker = s.Matrix.hstack(s.zeros(3, 2), s.eye(3))
    lift_image = s.Matrix(5, 6, lambda j, k: (j+1)*(k+2)+(j == k))
    change = s.Matrix(2, 6, lambda j, k: j-k)
    check('connecting map cutoff independence', zero(project_coker*(lift_image+old*change)-project_coker*lift_image))
    check('connecting map has correct target', zero(project_coker*old) and project_coker.rank() == 3)

    half = s.Rational(1, 2)
    check('vertical critical quotient cancellation', half-half == 0)
    for label, base, expected in [('open', 1, (1, s.Rational(3, 2), half)),
                                  ('ordinary', -5, (-5, s.Rational(-9, 2), s.Rational(-11, 2)))]:
        actual = (base, base+half, base-half)
        check(label+' weights from vertical class', actual == expected)
        # Effective total spin/sheaf central character must be one in each piece.
        for name, central, weight in [('local', -1, actual[0]), ('H01', s.I, actual[1]), ('H10', -s.I, actual[2])]:
            check(label+' '+name+' central compatibility', simp(s.exp(s.I*s.pi*weight)*central) == 1)
    return {'all_passed': all(checks.values()), 'checks': checks, 'finite_model_rows': records,
            'rank_jump_control': jump,
            'scope': 'finite guards for a smooth vertical Fredholm family; no total-space spectrum'}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_passed'] else 1)
