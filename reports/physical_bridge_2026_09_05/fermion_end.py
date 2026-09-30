"""R61 exact local cone-channel controls; not a global physical end law."""
import itertools
import json
import sympy as s


def clean(m):
    return m.applyfunc(lambda x: s.simplify(s.expand_complex(x)))


def zero(m):
    return clean(m) == s.zeros(*m.shape)


def same(a, b):
    return a.rank() == b.rank() == a.row_join(b).rank()


def clifford():
    basis = [b for n in range(4) for b in itertools.combinations(range(3), n)]
    e = []
    for i in range(3):
        mat = s.zeros(8)
        for col, b in enumerate(basis):
            if i not in b:
                mat[basis.index(tuple(sorted((i,)+b))), col] = (-1)**sum(j < i for j in b)
        e.append(mat)
    c = [a-a.T for a in e]
    h = [a+a.T for a in e]
    J = c[0]*c[1]*c[2]
    star = s.zeros(8)
    for col, b in enumerate(basis):
        other = tuple(i for i in range(3) if i not in b)
        word = b+other
        sign = (-1)**sum(word[i] > word[j] for i in range(3) for j in range(i+1, 3))
        star[basis.index(other), col] = sign
    signs = s.diag(*[(1, -1, -1, 1)[len(b)] for b in basis])
    indices = [basis.index(b) for b in ((1,), (2,), (0, 1), (0, 2))]
    S = s.Matrix([[0, -1], [1, 0]])
    critical_star = s.BlockMatrix([[s.zeros(2), S], [-S, s.zeros(2)]]).as_explicit()
    p = s.symbols('p0:3', real=True)
    f = s.symbols('f0:3', real=True)
    plus = sum((p[i]*c[i]+f[i]*h[i] for i in range(3)), s.zeros(8))
    minus = sum((p[i]*c[i]-f[i]*h[i] for i in range(3)), s.zeros(8))
    checks = dict(clifford_volume_involution=J*J == s.eye(8),
                  signed_hodge_transport=J == star*signs,
                  full_mass_reversal=J*plus == minus*J,
                  bare_conjugation_mass_reversal_fails=plus != minus,
                  critical_hodge_map=star.extract(indices, indices) == critical_star,
                  critical_clifford_phase=J.extract(indices, indices) == -critical_star)
    return checks


OMEGA = s.Matrix([[0, 1], [-1, 0]])


def domain(w, H):
    complement = (w.H*H).nullspace()
    b = s.Matrix.hstack(*complement) if complement else s.zeros(2, 0)
    return s.BlockMatrix([[w, s.zeros(2, b.cols)], [s.zeros(2, w.cols), b]]).as_explicit()


def boundary(kind):
    if kind == 'hexagonal':
        raw = s.Matrix([[2, -1], [-1, 2]])
        R = s.Matrix([[0, -1], [1, -1]])
        F = s.Matrix([[0, 1], [1, 0]])
    elif kind == 'square':
        raw = s.eye(2)
        R = s.Matrix([[0, -1], [1, 0]])
        F = s.diag(1, -1)
    else:
        raise ValueError('square or hexagonal link required')
    H = raw/s.sqrt(raw.det())
    S = -OMEGA*H
    T = s.BlockMatrix([[s.zeros(2), S], [-S, s.zeros(2)]]).as_explicit()
    green = s.BlockMatrix([[s.zeros(2), H], [-H, s.zeros(2)]]).as_explicit()
    w = clean((S-s.I*s.eye(2)).nullspace()[0])
    other = w.conjugate()
    D = domain(w, H)
    Dother = domain(other, H)
    Dreal = domain(s.Matrix([1, 0]), H)
    Dzero = domain(s.zeros(2, 0), H)
    Dfull = domain(s.eye(2), H)
    rotate, reflect = s.diag(R, R), s.diag(F, F)
    wrong = s.BlockMatrix([[w, s.zeros(2, 1)], [s.zeros(2, 1), w]]).as_explicit()
    P = clean(w*(w.H*H*w).inv()*w.H*H)
    checks = dict(
        metric_and_rotation=zero(R.T*H*R-H) and H[0, 0] > 0 and H.det() == 1,
        star_square=zero(S*S+s.eye(2)),
        real_line_control=same(Dreal, T*Dreal.conjugate()) and zero(Dreal.H*green*Dreal),
        helicity_line_is_not_real=not same(w, other),
        maximal_current_cancellation=D.rank() == 2 and zero(D.H*green*D),
        conjugate_line_current_cancellation=Dother.rank() == 2 and zero(Dother.H*green*Dother),
        combined_reality=same(D, T*D.conjugate()),
        combined_reality_involution=zero(T*T.conjugate()-s.eye(4)),
        bare_star_fails=not same(D, T*D),
        bare_conjugation_fails=not same(D, D.conjugate()),
        wrong_complement_rejected=not zero(wrong.H*green*wrong),
        rotation_preserves_complex_domain=same(D, rotate*D),
        reflection_exchanges_domains=same(Dother, reflect*D) and not same(D, reflect*D),
        anti_reflection_model_preserves_domain=same(D, reflect*D.conjugate()),
        extremes_fail_reality=not same(Dzero, T*Dzero.conjugate()) and not same(Dfull, T*Dfull.conjugate()),
        extremes_still_cancel_current=zero(Dzero.H*green*Dzero) and zero(Dfull.H*green*Dfull),
        holomorphic_projector=zero(P*P-P) and zero(P*w-w),
        real_gauge_derivative_restricted=not zero((s.eye(2)-P)*s.Matrix([1, 0])) and s.Matrix.hstack(w.applyfunc(s.re), w.applyfunc(s.im)).rank() == 2,
        common_line_boundary_variation_zero=zero(w.T*OMEGA*w),
        opposite_line_boundary_variation_nonzero=not zero(w.T*OMEGA*other),
    )
    # A same-projector chiral multiplet respects coefficient-linear variations;
    # the extra covariant derivative in delta H is NOT automatically projected.
    a, b, c, gauge = s.symbols('phi psi aux gauge', real=True)
    multiplet = s.Matrix.hstack(a*w, b*w, c*w)
    checks['coefficient_multiplet_constraint'] = zero((s.eye(2)-P)*multiplet)
    checks['susy_derivative_countercontrol'] = not zero((s.eye(2)-P)*s.Matrix([gauge, 0]))
    return dict(checks={k: bool(v) for k, v in checks.items()},
                H=H, S=S, line=w, domain=D, projector=P,
                opposite_wedge=clean(w.T*OMEGA*other),
                real_gauge_derivative_residual=clean((s.eye(2)-P)*s.Matrix([1, 0])))


def serial(value):
    if isinstance(value, s.MatrixBase):
        return [[str(x) for x in row] for row in value.tolist()]
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    return value


def run():
    checks = clifford()
    links = {kind: boundary(kind) for kind in ('square', 'hexagonal')}
    for kind, data in links.items():
        checks.update({kind+'_'+k: v for k, v in data['checks'].items()})
    return serial(dict(scope='Local complex critical channel, not full supersymmetric gauge domain or physical chirality',
                       checks=checks, all_checks_pass=all(checks.values()), links=links))


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
