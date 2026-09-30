"""R68 actual matrix cone operator and exact neutral sector; no particle census."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s


def local(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


old = local('r68_cone_source', 'nilpotent_cone.py')
metric_source = local('r68_metric_source', 'charged_domain.py')
domain_source = local('r68_domain_source', 'fermion_end.py')
N, P, Z, H = old.N, old.P, old.D, old.H
alpha, t = s.symbols('alpha t', positive=True)
k, beta, kap, xi, zeta, sigma = s.symbols('k beta kap xi zeta sigma', real=True)
LINK = ((), (1,), (2,), (1, 2))
ORDER = LINK+tuple((0,)+b for b in LINK)
M = s.diag(-1, 0, 0, 1)
GAMMA = s.BlockMatrix([[s.zeros(4), -s.eye(4)], [s.eye(4), s.zeros(4)]]).as_explicit()


def clean(v):
    return v.applyfunc(s.simplify) if isinstance(v, s.MatrixBase) else s.simplify(v)


def zero(v):
    a = clean(v)
    return a == s.zeros(*a.shape) if isinstance(a, s.MatrixBase) else a == 0


def comm(a, b):
    return a*b-b*a


def ad(a):
    n = a.rows
    return s.kronecker_product(a, s.eye(n))-s.kronecker_product(s.eye(n), a.T)


def vec(a):
    return s.Matrix(list(a))


def project(a):
    return clean(Z*s.trace(Z*a)/12)


def link_wedge(zx, zy):
    ex = s.Matrix([[0, 0, 0, 0], [1, 0, 0, 0],
                   [0, 0, 0, 0], [0, 0, 1, 0]])
    ey = s.Matrix([[0, 0, 0, 0], [0, 0, 0, 0],
                   [1, 0, 0, 0], [0, -1, 0, 0]])
    return s.kronecker_product(ex, zx)+s.kronecker_product(ey, zy)


def operators(power=sigma, radial=True):
    eye = s.eye(4)
    zx = s.sqrt(alpha)*(s.I*xi*eye+t*N)
    zy = (s.I*zeta*eye+k*Z+beta*t*t*P)/s.sqrt(alpha)
    e = link_wedge(zx, zy)
    m = s.kronecker_product(M, eye)
    K = s.kronecker_product(s.eye(4), kap*H if radial else s.zeros(4))
    identity, null = s.eye(16), s.zeros(16)
    d = s.BlockMatrix([[e, null], [power*identity+m+K, -e]]).as_explicit()
    delta = s.BlockMatrix([[e.H, -power*identity+m+K.H], [null, -e.H]]).as_explicit()
    angular = s.BlockMatrix([[m+K, -e-e.H], [-e-e.H, -m-K.H]]).as_explicit()
    return d, delta, angular


@lru_cache(None)
def metric_controls():
    r, x, y = metric_source.COORDS
    metric = metric_source.MetricForms((1, r/s.sqrt(alpha), r*s.sqrt(alpha)))
    weights = [r**(len(b)-1)*s.prod(1/s.sqrt(alpha) if j == 1 else s.sqrt(alpha) for j in b)
               for b in LINK]*2
    phase = r**sigma*s.exp(s.I*(xi*x+zeta*y))
    fd, fa = s.zeros(8), s.zeros(8)
    wedges, contractions = [s.zeros(8) for _ in range(3)], [s.zeros(8) for _ in range(3)]
    for col, basis in enumerate(ORDER):
        form = {basis: phase*weights[col]}
        for target_matrix, out in ((fd, metric_source.exterior(form)), (fa, metric.delta(form))):
            for row, target in enumerate(ORDER):
                target_matrix[row, col] = s.simplify(out.get(target, 0)*r/(phase*weights[row]))
        for j in range(3):
            outs = (metric_source.wedge({(j,): 1}, form), metric.contract_gradient(form, {(j,): 1}))
            for target_matrix, out in zip((wedges[j], contractions[j]), outs):
                for row, target in enumerate(ORDER):
                    target_matrix[row, col] = s.simplify(out.get(target, 0)*r/(phase*weights[row]))
    coeff = (kap*H/r, t*N, k*Z+beta*t*t*P)
    direct_d = s.kronecker_product(fd, s.eye(4))
    direct_a = s.kronecker_product(fa, s.eye(4))
    for j in range(3):
        direct_d += s.kronecker_product(wedges[j], coeff[j])
        direct_a += s.kronecker_product(contractions[j], coeff[j].H)
    d, delta, angular = operators()
    gamma = s.kronecker_product(GAMMA, s.eye(4))
    wrong = s.kronecker_product(fa, s.eye(4))+sum(
        (s.kronecker_product(contractions[j], coeff[j]) for j in range(3)), s.zeros(32))
    checks = dict(metric_d=zero(direct_d-d), metric_adjoint=zero(direct_a-delta),
                  full_operator=zero(d+delta-gamma*(sigma*s.eye(32)+angular)),
                  actual_angular_Hermitian=zero(angular-angular.H),
                  actual_Green_anticommutation=zero(gamma*angular+angular*gamma),
                  wrong_coefficient_adjoint_fails=not zero(wrong-direct_a),
                  normalized_measure=all(s.simplify(metric.volume*weights[j]**2/metric.basis_length(b)**2)==1
                                         for j, b in enumerate(ORDER)),
                  radial_Hermitian=zero(coeff[0]-coeff[0].H))
    return dict(checks=checks, components=32, coefficient_dimension=4)


@lru_cache(None)
def flat_controls():
    d, delta, _ = operators()
    jd = s.BlockMatrix([[s.zeros(16), s.zeros(16)], [s.eye(16), s.zeros(16)]]).as_explicit()
    ja = -jd.T
    derivative = lambda matrix: -kap*t*matrix.diff(t)
    dsq = operators(sigma-1)[0]*d+jd*derivative(d)
    asq = operators(sigma-1)[1]*delta+ja*derivative(delta)
    absent = operators(radial=False)[0]
    wrong = operators(sigma-1, radial=False)[0]*absent+jd*derivative(absent)
    return dict(checks=dict(variable_d_squared=zero(dsq), variable_adjoint_squared=zero(asq),
                            frozen_t_fails=not zero(operators(sigma-1)[0]*d),
                            omitted_radial_fails=not zero(wrong),
                            coefficient_flat_xy=zero(comm(t*N, k*Z+beta*t*t*P)),
                            radial_x=zero(-kap*t*N+comm(kap*H, t*N)),
                            radial_y=zero(-2*kap*beta*t*t*P+comm(kap*H, k*Z+beta*t*t*P))))


@lru_cache(None)
def reducing_controls():
    trace = vec(s.eye(4)).T
    reducing_system = s.Matrix.vstack(ad(N), ad(N.H), trace)
    holonomy_system = s.Matrix.vstack(ad(N), ad(Z), trace)
    reduce_basis = reducing_system.nullspace()
    holo_basis = holonomy_system.nullspace()
    zvec = vec(Z)
    proj = zvec*zvec.H/12
    X = s.Matrix(4, 4, s.symbols('x0:16', complex=True))
    coeff = (kap*H, t*N, k*Z+beta*t*t*P)
    matrices = [ad(a) for a in coeff]
    checks = dict(reducing_dimension=len(reduce_basis)==1 and reducing_system.rank()==15,
                  reducing_line=zero(reducing_system*zvec) and
                  s.Matrix.hstack(reduce_basis[0], zvec).rank()==1,
                  holonomy_only_dimension=len(holo_basis)==3,
                  holonomy_only_contains_nilpotents=zero(holonomy_system*vec(N)) and zero(holonomy_system*vec(P)),
                  holonomy_is_not_reducing=not zero(comm(N, N.H)) and not zero(comm(P, N.H)),
                  projection_orthogonal=zero(proj*proj-proj) and zero(proj-proj.H),
                  projection_matches_trace=zero(proj*vec(X)-vec(project(X))),
                  reduction_both_sides=all(zero(proj*a) and zero(a*proj) and zero(proj*a.H) and zero(a.H*proj) for a in matrices),
                  adjoint_trace_representation=all(zero(ad(a).H-ad(a.H)) for a in coeff),
                  vectorization_action=zero(ad(N)*vec(X)-vec(comm(N, X))),
                  positive_Z_norm=s.trace(Z.H*Z)==12,
                  local_reality=Z.H==Z)
    return dict(checks=checks, reducing_dimension=len(reduce_basis), holonomy_dimension=len(holo_basis))


@lru_cache(None)
def trace_controls():
    e0 = link_wedge(s.zeros(1), s.zeros(1))
    angular = s.diag(M, -M)
    indices = (1, 2, 5, 6)
    inject = s.eye(8)[:, list(indices)]
    gamma = s.BlockMatrix([[s.zeros(2), -s.eye(2)], [s.eye(2), s.zeros(2)]]).as_explicit()
    Hlink = s.diag(alpha, 1/alpha)
    green = s.BlockMatrix([[s.zeros(2), Hlink], [-Hlink, s.zeros(2)]]).as_explicit()
    eps, R, radius = s.symbols('epsilon R radius', positive=True)
    capacity = 1/s.integrate(1, (radius, eps, R))
    density2 = 12*alpha
    density4 = density2**2/radius**2
    a0, a1, a2, a3 = s.symbols('a0:4', complex=True)
    b0, b1, b2, b3 = s.symbols('b0:4', complex=True)
    avec, bvec = s.Matrix([a0, a1, a2, a3]), s.Matrix([b0, b1, b2, b3])
    derivative_green = (avec.H*green*bvec)[0]
    checks = dict(neutral_angular_zero=zero(angular*inject),
                  neutral_derivative_exact=zero(GAMMA*inject-inject*gamma),
                  four_independent_traces=inject.rank()==4,
                  Green_nondegenerate=green.rank()==4 and green.det()==1,
                  Green_skew=zero(green.H+green),
                  nonzero_pairing=(s.eye(4)[:, 0].T*green*s.eye(4)[:, 2])[0]==alpha,
                  derivative_Green_sign=zero(-s.diag(Hlink, Hlink)*gamma-green),
                  critical_L2=zero(s.integrate(density2, (radius, 0, R))-12*alpha*R),
                  critical_L4_diverges=s.limit(s.integrate(density4, (radius, eps, R)), eps, 0, dir='+')==s.oo,
                  cutoff_capacity_nonzero=s.limit(capacity, eps, 0, dir='+')==1/R,
                  neutral_link_exact=zero(e0),
                  nontrivial_boundary_form=derivative_green!=0)
    return dict(checks=checks, Green=green, kinetic_density=density2, quartic_density=density4,
                local_apex_trace_dimension_lower_bound=4)


@lru_cache(None)
def domain_controls():
    Hlink = s.diag(alpha, 1/alpha)
    Omega = domain_source.OMEGA
    star = -Omega*Hlink
    reality = s.BlockMatrix([[s.zeros(2), star], [-star, s.zeros(2)]]).as_explicit()
    green = trace_controls()['Green']
    plus = s.Matrix([1, -s.I*alpha])
    minus = plus.conjugate()
    domains = [domain_source.domain(w, Hlink) for w in (plus, minus, s.Matrix([1, 0]))]
    parity = s.diag(-1, -1, 1, 1)
    gamma = s.BlockMatrix([[s.zeros(2), -s.eye(2)], [s.eye(2), s.zeros(2)]]).as_explicit()
    de = s.BlockMatrix([[s.zeros(2), s.zeros(2)], [s.eye(2), s.zeros(2)]]).as_explicit()
    da = -de.T
    q2 = s.I*(de-da)
    wrong = s.BlockMatrix([[plus, s.zeros(2, 1)], [s.zeros(2, 1), plus]]).as_explicit()
    checks = dict(link_star=zero(star*star+s.eye(2)),
                  positive_metric=Hlink.det()==1 and alpha.is_positive,
                  helicity_eigenline=zero(star*plus-s.I*plus),
                  distinct_helicities=not domain_source.same(plus, minus),
                  all_maximal_current=all(d.rank()==2 and zero(d.H*green*d) for d in domains),
                  all_combined_reality=all(domain_source.same(d, reality*d.conjugate()) for d in domains),
                  reality_involution=zero(reality*reality.conjugate()-s.eye(4)),
                  reality_commutes_Q=zero(reality*gamma-gamma*reality),
                  separate_star_fails=not domain_source.same(domains[0], reality*domains[0]),
                  separate_conjugation_fails=not domain_source.same(domains[0], domains[0].conjugate()),
                  wrong_Hermitian_complement_fails=not zero(wrong.H*green*wrong),
                  degree_preserves_domains=all(domain_source.same(d, parity*d) for d in domains),
                  linear_d_squared=zero(de*de) and zero(da*da),
                  linear_supercharge_squares=zero(gamma*gamma-q2*q2),
                  linear_supercharge_anticommutator=zero(gamma*q2+q2*gamma),
                  no_zero_boundary_extension=green.rank()!=0,
                  collar_degree_pair=[domains[0][:2, :].rank(), domains[0][2:, :].rank()]==[1, 1])
    return dict(checks=checks, plus_line=plus, plus_domain=domains[0], minus_domain=domains[1])


@lru_cache(None)
def nonlinear_controls():
    X, Y = s.zeros(4), s.zeros(4)
    X[0, 1], Y[1, 0] = 1, 1
    c = s.Symbol('c', real=True)
    fields = old.fields()
    modified = [fields[0], fields[1]+c*Z, fields[2]]
    before_F, before_I = old.residuals(fields, old.metric())
    after_F, after_I = old.residuals(modified, old.metric())
    c_nonzero = s.Symbol('c_nonzero', positive=True)
    expCZ = s.diag(s.exp(c), s.exp(-3*c), s.exp(c), s.exp(c))
    meridian = s.eye(4)+N+P/2
    checks = dict(complementary_coefficients=zero(project(X)) and zero(project(Y)),
                  complementary_bracket_sources_Z=zero(project(comm(X, Y))-Z/3) and not zero(project(comm(X, Y))),
                  neutral_not_ideal=not zero(comm(Z, X)),
                  commuting_deformation_flat=all(zero(after_F[j]-before_F[j]) for j in before_F),
                  commuting_deformation_moment=zero(after_I-before_I),
                  meridian_changes=not zero(expCZ*meridian-meridian),
                  real_positive_deformation_not_fixed=s.simplify(s.exp(c_nonzero))!=1,
                  meridian_eigenvalues_changed=expCZ[1, 1]==s.exp(-3*c) and expCZ[0, 0]==s.exp(c),
                  no_parent_relabel=Z.rows==4)
    return dict(checks=checks, sourced_projection=project(comm(X, Y)), meridian_multiplier=expCZ)


def serial(v):
    if isinstance(v, s.MatrixBase):
        return [[str(x) for x in row] for row in v.tolist()]
    if isinstance(v, s.Basic):
        return str(v)
    if isinstance(v, dict):
        return {k: serial(x) for k, x in v.items()}
    if isinstance(v, (tuple, list)):
        return [serial(x) for x in v]
    return v


def run():
    groups = {name: fn() for name, fn in (('metric', metric_controls), ('flat', flat_controls),
              ('reducing', reducing_controls), ('trace', trace_controls),
              ('domain', domain_controls), ('nonlinear', nonlinear_controls))}
    checks = {name+'/'+key: bool(value) for name, group in groups.items() for key, value in group['checks'].items()}
    return serial(dict(scope='Actual local operator and neutral linear domain, not a full physical end law or particle census',
                       checks=checks, all_checks_pass=all(checks.values()), groups=groups))


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
