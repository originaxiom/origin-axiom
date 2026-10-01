"""R70 necessary neutral multiplet admission; not a full physical end law."""
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


old = local('r70_fermion', 'cone_fermion.py')
field = old.old
N, P, Z, H = old.N, old.P, old.Z, old.H
clean, zero, comm = old.clean, old.zero, old.comm
alpha = old.alpha
Hlink = s.diag(alpha, 1/alpha)
Omega = s.Matrix([[0, 1], [-1, 0]])
S = -Omega*Hlink
Green = s.BlockMatrix([[s.zeros(2), Hlink], [-Hlink, s.zeros(2)]]).as_explicit()
Reality = s.BlockMatrix([[s.zeros(2), S], [-S, s.zeros(2)]]).as_explicit()


@lru_cache(None)
def period_controls():
    t, beta = s.symbols('t beta', real=True)
    q = s.Symbol('q', positive=True)
    x = s.Symbol('x', real=True)
    M = s.eye(4)+t*N+t*t*P/2
    L = s.diag(q, q**-3, q, q)*(s.eye(4)+beta*t*t*P)
    X = s.Matrix(4, 4, s.symbols('x0:16', complex=True))
    U = s.eye(4)+x*t*N+x*x*t*t*P/2
    integral = (U.inv()*X*U).applyfunc(lambda a: s.integrate(s.expand(a), (x, 0, 1)))
    weighted = s.trace(Z*integral)
    transverse = 1-s.cos(2*s.pi*x)
    orbit_M, orbit_L = comm(X, M), comm(X, L)
    projected = old.project(X)
    checks = dict(
        actual_meridian_Z=zero(comm(Z, M)),
        actual_longitude_Z=zero(comm(Z, L)),
        radial_Z=zero(comm(Z, H)),
        full_Duhamel_projection=zero(weighted-s.trace(Z*X)),
        complementary_projection_zero=zero(s.trace(Z*(X-projected))),
        similarity_meridian_annihilator=zero(s.trace(Z*M.inv()*orbit_M)),
        similarity_longitude_annihilator=zero(s.trace(Z*L.inv()*orbit_L)),
        meridian_neutral_period=s.trace(Z*M.inv()*(M*Z))==12,
        longitude_neutral_period=s.trace(Z*L.inv()*(L*Z))==12,
        periodic_gauge_period=zero(s.integrate(s.diff(s.sin(2*s.pi*x), x), (x, 0, 1))),
        gauge_commutator_projection=zero(s.trace(Z*comm(t*N, X))) and
                                      zero(s.trace(Z*comm(s.log(q)*Z+beta*P, X))),
        ordinary_trace_is_insufficient=s.trace(M*Z)==0 and s.trace(Z*M.inv()*(M*Z))!=0,
        moving_Z_must_be_transported=not zero(comm(X, Z)),
        two_based_loops_not_average=transverse.subs(x,0)==0 and
                                   s.integrate(transverse,(x,0,1))==1,
        based_loop_control_is_not_flat=not zero(s.diff(transverse,x)),
    )
    return dict(checks=checks, period_norm=12, matrix_dimension=4,
                weighted_Duhamel=clean(weighted))


@lru_cache(None)
def profile_controls():
    pa = s.eye(4)[:2, :]
    pb = S.inv()*s.eye(4)[2:, :]
    both = pa.col_join(pb)
    relative = s.eye(4)[:, 2:]
    gamma = s.BlockMatrix([[s.zeros(2), -s.eye(2)], [s.eye(2), s.zeros(2)]]).as_explicit()
    plus = s.Matrix([1, -s.I*alpha])
    minus = plus.conjugate()
    same = old.domain_source.same
    domains = [old.domain_source.domain(w, Hlink) for w in (plus, minus, s.Matrix([0, 1]))]
    checks = dict(
        banked_Green=zero(Green-old.trace_controls()['Green']),
        banked_reality=zero(Reality*Reality.conjugate()-s.eye(4)),
        exact_neutral_Q=zero(Reality*gamma-gamma*Reality),
        both_profile_constraints_full_rank=both.rank()==4 and not both.nullspace(),
        one_profile_plus_reality_full_rank=pa.col_join(pa*Reality).rank()==4,
        Green_nonzero_rank=Green.rank()==4,
        zero_trace_not_maximal=0<Green.rows//2,
        relative_maximal_current=relative.rank()==2 and zero(relative.H*Green*relative),
        relative_fails_reality=not same(relative, Reality*relative.conjugate()),
        relative_passes_one_profile=zero(pa*relative),
        relative_fails_other_profile=not zero(pb*relative),
        all_line_profiles=all(same(pa*d, w) and same(pb*d, w.conjugate()) for d, w in zip(domains, (plus, minus, s.Matrix([0, 1])))),
        all_line_current=all(zero(d.H*Green*d) for d in domains),
        all_line_reality=all(same(d, Reality*d.conjugate()) for d in domains),
        both_helicities_survive=not same(domains[0], domains[1]),
    )
    return dict(checks=checks, constraints=both, trace_dimension=4,
                required_maximal_dimension=2, tested_domains=3)


@lru_cache(None)
def boson_controls():
    r = field.r
    vx, vy = s.Function('vx')(r), s.Function('vy')(r)
    C = field.fields()
    changed = [C[0], C[1]+vx*Z, C[2]+vy*Z]
    oldF, oldI = field.residuals(C, field.metric())
    newF, newI = field.residuals(changed, field.metric())
    dF = {ij: clean(newF[ij]-oldF[ij]) for ij in oldF}
    tangent = [s.zeros(4), vx*Z, vy*Z]
    kinetic = clean(r*r*field.one_norm(tangent, field.metric()))
    residual_density = clean(r*r*field.two_norm(dF, field.metric()))
    target = 12*(field.alpha*s.conjugate(vx)*vx+s.conjugate(vy)*vy/field.alpha)
    dtarget = 12*(field.alpha*s.conjugate(s.diff(vx,r))*s.diff(vx,r)+
                  s.conjugate(s.diff(vy,r))*s.diff(vy,r)/field.alpha)
    R, eps = s.symbols('R epsilon', positive=True)
    # Nonzero apex, outer value zero. H1 is sufficient; no endpoint smoothing is needed.
    explicit_density = 12*field.alpha*(1-r/R)**2
    explicit_action = 24*field.alpha/R**2
    quartic = explicit_density**2/r**2
    bad = s.diff(s.sqrt(r),r)**2
    X, Y = s.zeros(4), s.zeros(4)
    X[0, 1], Y[1, 0] = 1, 1
    checks = dict(
        full_radial_x=zero(dF[0,1]-s.diff(vx,r)*Z),
        full_radial_y=zero(dF[0,2]-s.diff(vy,r)*Z),
        full_tangential_zero=zero(dF[1,2]),
        full_moment_unchanged=zero(newI-oldI),
        actual_kinetic_density=zero(kinetic-target),
        actual_residual_density=zero(residual_density-dtarget),
        self_brackets_zero=zero(comm(vx*Z, vy*Z)) and zero(comm(vx*Z,s.conjugate(vx)*Z)),
        positive_H1_kinetic=zero(s.integrate(explicit_density,(r,0,R))-4*field.alpha*R),
        positive_H1_action=zero(s.integrate(explicit_action,(r,0,R))-24*field.alpha/R),
        positive_H1_apex=(1-r/R).subs(r,0)==1 and (1-r/R).subs(r,R)==0,
        positive_outside_L4=s.limit(s.integrate(quartic,(r,eps,R)),eps,0,dir='+')==s.oo,
        bad_derivative_diverges=s.limit(s.integrate(bad,(r,eps,R)),eps,0,dir='+')==s.oo,
        products_not_automatically_zero=not zero(comm(Z,X)),
        complementary_source_retained=zero(old.project(comm(X,Y))-Z/3),
        weighted_cross_scaling=zero(comm(Z/r,X)-(comm(Z,X)/r)),
    )
    return dict(checks=checks, kinetic_density=kinetic, residual_density=residual_density,
                explicit_kinetic=4*field.alpha*R, explicit_potential_times_g7_squared=24*field.alpha/R)


@lru_cache(None)
def boundary_controls():
    t, beta, k = s.symbols('t beta k', real=True)
    x, y, dx, dy, z, dz, wx, wy = s.symbols('x y dx dy z dz wx wy', complex=True)
    Cx, Cy = t*N+x*Z, k*Z+beta*t*t*P+y*Z
    theta = clean(s.trace(Cy*dx*Z-Cx*dy*Z))
    line = clean(theta.subs({x:z*wx,y:z*wy,dx:dz*wx,dy:dz*wy}, simultaneous=True))
    helicity = line.subs({wx:1,wy:-s.I*alpha})
    longitude = line.subs({wx:0,wy:1})
    added = -12*k*dx
    checks = dict(
        full_affine_boundary=zero(theta-12*((k+y)*dx-x*dy)),
        line_quadratic_cancels=zero(line-12*k*wx*dz),
        longitude_line_passes=zero(longitude),
        helicity_background_term_survives=zero(helicity-12*k*dz) and not zero(helicity),
        both_helicities_same_affine_term=zero(line.subs({wx:1,wy:s.I*alpha})-helicity),
        specified_counterterm_cancels=zero((theta+added).subs({x:z*wx,y:z*wy,dx:dz*wx,dy:dz*wy},simultaneous=True)),
        wrong_counterterm_sign_fails=not zero((theta-added).subs({x:z,y:-s.I*alpha*z,dx:dz,dy:-s.I*alpha*dz},simultaneous=True)),
        boundary_two_form_unchanged=zero(s.diff(theta+added,dy).diff(x)-s.diff(theta+added,dx).diff(y)+24),
        fixed_x_variation_control=zero(theta.subs({x:0,dx:0})),
        background_k_not_removed=not zero(line.subs({wx:1,wy:0})),
    )
    return dict(checks=checks, affine_one_form=theta, line_one_form=line,
                specified_linear_variation=added)


def serial(value):
    return old.serial(value)


def run():
    groups = {name:fn() for name,fn in (('period',period_controls),('profile',profile_controls),
              ('boson',boson_controls),('boundary',boundary_controls))}
    checks = {name+'/'+key: bool(value) for name,group in groups.items() for key,value in group['checks'].items()}
    return serial(dict(scope='Necessary same-action local multiplet test and finite-action alternatives, not a selected physical end law',
                       groups=groups,checks=checks,all_checks_pass=all(checks.values())))


if __name__ == '__main__':
    result=run()
    print(json.dumps(result,sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
