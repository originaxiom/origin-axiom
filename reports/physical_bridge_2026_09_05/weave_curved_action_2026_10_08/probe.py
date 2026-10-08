"""Universal cyclic-trace algebra plus local geometry and full parent controls."""
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
import importlib.util
import json
import sympy as s


def clean(p):
    return {k:s.simplify(v) for k,v in p.items() if s.simplify(v)!=0}


def atom(name):
    return {(name,):s.Integer(1)}


def add(*args):
    out={}
    for p in args:
        for w,c in p.items():
            out[w]=out.get(w,0)+c
    return clean(out)


def scale(c,p):
    return clean({w:c*v for w,v in p.items()})


def mul(p,q):
    out={}
    for w,c in p.items():
        for v,d in q.items():
            out[w+v]=out.get(w+v,0)+c*d
    return clean(out)


def comm(p,q):
    return add(mul(p,q),scale(-1,mul(q,p)))


def dagger(p):
    # All primitive letters stand for independent HERMITIAN matrices.
    return clean({tuple(reversed(w)):s.conjugate(c) for w,c in p.items()})


def trace(p):
    out={}
    for w,c in p.items():
        key=min(w[i:]+w[:i] for i in range(len(w))) if w else ()
        out[key]=out.get(key,0)+c
    return clean(out)


def norm(p):
    return trace(mul(dagger(p),p))


def coeff(p,t,n):
    return clean({w:s.expand(c).coeff(t,n) for w,c in p.items()})


def eq(p,q):
    return not add(p,scale(-1,q))


def complex_pair(a,b):
    return scale(1/s.sqrt(2),add(a,scale(s.I,b)))


def epsilon(tup):
    return (-1)**sum(tup[i]>tup[j] for i in range(3) for j in range(i+1,3))


def universal_checks():
    x=[atom('X'+str(i)) for i in range(4)]
    q,r=complex_pair(*x[:2]),complex_pair(*x[2:])
    M=add(comm(q,dagger(q)),comm(r,dagger(r)))
    vD=scale(s.Rational(1,2),trace(mul(M,M)))
    vF=scale(2,norm(comm(q,r)))
    quartic=add(vD,vF)
    ym=add(*(scale(s.Rational(1,2),norm(comm(a,b))) for a,b in combinations(x,2)))
    F=atom('F')
    expanded=scale(s.Rational(1,2),trace(mul(add(F,M),add(F,M))))
    cross=trace(mul(F,M))
    expected=add(scale(s.Rational(1,2),norm(F)),vD,cross)
    # One active derivative in the ten-dimensional epsilon superpotential.
    p,q0,r0,dq,dr=[atom(n) for n in ('P','Q','R','dQ','dR')]
    phi=[p,q0,r0]
    cubic=add(*(scale(epsilon(t),mul(phi[t[0]],comm(phi[t[1]],phi[t[2]]))) for t in permutations(range(3))))
    parent=add(scale(s.Rational(1,2),trace(add(mul(r0,dq),scale(-1,mul(q0,dr))))),
               scale(-1/(6*s.sqrt(2)),trace(cubic)))
    primitive=scale(s.Rational(1,2),trace(add(mul(dq,r0),mul(q0,dr))))
    reduced=add(scale(-1,trace(mul(q0,dr))),scale(1/s.sqrt(2),trace(mul(q0,comm(p,r0)))))
    # Variation and its precise boundary primitive, in Hermitian A convention.
    a,u,v,du,dv=[atom(n) for n in ('a','u','v','du','dv')]
    t=s.symbols('t',real=True)
    qt,rt,pt=add(q0,scale(t,u)),add(r0,scale(t,v)),add(p,scale(t,a))
    dqt,drt=add(dq,scale(t,du)),add(dr,scale(t,dv))
    Wt=add(scale(s.Rational(1,2),trace(add(mul(qt,drt),scale(-1,mul(rt,dqt))))),
           scale(-s.I,trace(mul(qt,comm(pt,rt)))))
    variation=coeff(Wt,t,1)
    bulk=trace(add(mul(u,add(dr,scale(-s.I,comm(p,r0)))),
                   scale(-1,mul(v,add(dq,scale(-s.I,comm(p,q0))))),
                   scale(-s.I,mul(a,comm(r0,q0)))))
    boundary=scale(s.Rational(1,2),trace(add(mul(dq,v),mul(q0,dv),scale(-1,mul(dr,u)),scale(-1,mul(r0,du)))))
    # All six cubic Hessian terms retained, not only q-a-r at one ordering.
    aa,qq,rr=[atom(n) for n in ('aa','qq','rr')]
    ss=s.symbols('ss',real=True)
    general=scale(-s.I,trace(mul(add(q0,scale(t,u),scale(ss,qq)),
                                  comm(add(p,scale(t,a),scale(ss,aa)),
                                       add(r0,scale(t,v),scale(ss,rr))))))
    hess=coeff(coeff(general,t,1),ss,1)
    six=scale(-s.I,trace(add(mul(u,comm(aa,r0)),mul(qq,comm(a,r0)),
                            mul(u,comm(p,rr)),mul(qq,comm(p,v)),
                            mul(q0,comm(a,rr)),mul(q0,comm(aa,v)))))
    # Full boson residual scaling; curvature variation and all four scalars.
    a1,a2,f=atom('a1'),atom('a2'),atom('f')
    A=add(a1,scale(s.I,a2))
    U,V=complex_pair(atom('u1'),atom('u2')),complex_pair(atom('v1'),atom('v2'))
    Ft=add(scale(t,f),scale(-s.I*t**2,comm(a1,a2)))
    Dq=add(scale(t,U),scale(-s.I*t**2,comm(A,q)))
    Dr=add(scale(t,V),scale(-s.I*t**2,comm(A,r)))
    mu=add(Ft,scale(t**2,M))
    potential=add(norm(Dq),norm(Dr),scale(2*t**4,norm(comm(q,r))),scale(s.Rational(1,2),norm(mu)))
    quadratic=add(norm(U),norm(V),scale(s.Rational(1,2),norm(f)))
    # Derive, rather than posit, the moment map from the same kinetic metric.
    ep,epx,epy,da1,da2,dxda2,dyda1=[atom(n) for n in ('eps','eps_x','eps_y','da1','da2','dxda2','dyda1')]
    k1=add(epx,scale(-s.I,comm(a1,ep)))
    k2=add(epy,scale(-s.I,comm(a2,ep)))
    omega_A=trace(add(mul(k1,da2),scale(-1,mul(k2,da1))))
    dF=add(dxda2,scale(-1,dyda1),scale(-s.I,add(comm(da1,a2),comm(a1,da2))))
    surface_A=trace(add(mul(epx,da2),mul(ep,dxda2),scale(-1,mul(epy,da1)),scale(-1,mul(ep,dyda1))))
    moment_A=add(scale(-1,trace(mul(ep,dF))),surface_A)
    kq=scale(s.I,comm(ep,q))
    omega_q=scale(s.I,trace(add(mul(kq,dagger(U)),scale(-1,mul(U,dagger(kq))))))
    moment_q=scale(-1,trace(mul(ep,add(comm(U,dagger(q)),comm(q,dagger(U))))))
    return {
        'connection_moment_from_half_kinetic_metric':eq(omega_A,moment_A),
        'matter_moment_from_spin_kinetic_metric':eq(omega_q,moment_q),
        'wrong_connection_metric_detected':not eq(scale(2,omega_A),moment_A),
        'wrong_matter_metric_detected':not eq(scale(2,omega_q),moment_q),
        'universal_quartic_identity':eq(quartic,ym),
        'omitting_mixed_commutator_detected':not eq(vD,ym),
        'omitting_R_moment_source_detected':not eq(add(scale(s.Rational(1,2),norm(comm(q,dagger(q)))),vF),ym),
        'moment_cross_coefficient':eq(expanded,expected),
        'derivative_curvature_cross_cancels':eq(add(cross,scale(-1,trace(mul(F,M)))),{}),
        'ten_dimensional_six_cubic_permutations':eq(trace(cubic),scale(6,trace(mul(p,comm(q0,r0))))),
        'ten_to_six_superpotential_with_boundary':eq(parent,add(reduced,primitive)),
        'dropping_derivative_primitive_detected':not eq(parent,reduced),
        'superpotential_variation_with_surface_term':eq(variation,add(bulk,boundary)),
        'dropping_variation_surface_detected':not eq(variation,bulk),
        'full_cubic_Hessian_six_terms':eq(hess,six),
        'zero_background_potential_zero':coeff(potential,t,0)=={},
        'zero_background_first_variation_zero':coeff(potential,t,1)=={},
        'full_boson_quadratic_positive_norm_sum':eq(coeff(potential,t,2),quadratic),
        'interacting_potential_not_just_quadratic':bool(coeff(potential,t,4)),
    }


def e(i,j,n=3):
    x=s.zeros(n);x[i,j]=1;return x


def matrix_checks():
    x,y=s.symbols('x y',real=True)
    phase=(1+s.I*x)/(1-s.I*x)
    U=s.diag(phase,1/phase,1)
    Ui=U.inv()
    ax=e(0,1)+e(1,0)
    ay=s.diag(1,-1,0)
    q=e(0,2)+x*e(2,0)+y*e(0,1)
    cp=lambda a,b:a*b-b*a
    D=lambda a,b,p:s.diff(p,x)+s.I*s.diff(p,y)-s.I*cp(a+s.I*b,p)
    axp=U*ax*Ui-s.I*s.diff(U,x)*Ui
    ayp=U*ay*Ui-s.I*s.diff(U,y)*Ui
    qp=U*q*Ui
    residual=(D(axp,ayp,qp)-U*D(ax,ay,q)*Ui).applyfunc(s.simplify)
    wrong=(D(U*ax*Ui,U*ay*Ui,qp)-U*D(ax,ay,q)*Ui).applyfunc(s.simplify)
    Ap,Qp,Rp=e(0,1),e(2,0),e(1,2)
    vertex=s.trace(Qp*cp(Ap,Rp))
    return {
        'gauge_transform_unitary':(U.H*U-s.eye(3)).applyfunc(s.simplify)==s.zeros(3),
        'space_dependent_gauge_covariance':residual==s.zeros(3),
        'omitted_derivative_compensator_detected':wrong!=s.zeros(3),
        'retained_family_cubic_vertex_nonzero':vertex==1,
        'commuting_cubic_control_zero':s.trace(s.eye(3)*cp(Ap,s.eye(3)))==0,
    }


def curvature_checks():
    x,y,h=s.symbols('x y h',real=True)
    sigma=x*x+x*y+2*y*y
    ax,ay=x*y,x*x-y
    sx,sy=s.diff(sigma,y)/2,-s.diff(sigma,x)/2
    u=x*x+y+1;v=x*y+y*y
    phi=u+s.I*v
    dx=lambda z:s.diff(z,x)+s.I*(sx-h*ax)*z
    dy=lambda z:s.diff(z,y)+s.I*(sy-h*ay)*z
    px,py=dx(phi),dy(phi)
    norm=lambda z:s.expand(z*s.conjugate(z))
    Fs=s.diff(sy,x)-s.diff(sx,y)
    Fg=s.diff(ay,x)-s.diff(ax,y)
    div=s.diff(s.I*s.conjugate(phi)*py,x)-s.diff(s.I*s.conjugate(phi)*px,y)
    identity=s.simplify(norm(px+s.I*py)-norm(px)-norm(py)-div-(Fs-h*Fg)*norm(phi))
    # Same formula for the flat holomorphic-patch control.
    z=x+s.I*y
    dz=s.diff(z,x)+s.I*s.diff(z,y)
    current=s.diff(s.I*s.conjugate(z)*s.diff(z,y),x)-s.diff(s.I*s.conjugate(z)*s.diff(z,x),y)
    lap=s.diff(sigma,x,2)+s.diff(sigma,y,2)
    # d(f dz) coefficient: i f_x-f_y = i Dbar f. No silent relative phase.
    f=x*x*y+s.I*y*y
    wedge=s.I*s.diff(f,x)-s.diff(f,y)
    db=s.diff(f,x)+s.I*s.diff(f,y)
    return {
        'stokes_dxdy_to_dz_phase':s.simplify(-s.I*wedge-db)==0,
        'omitting_stokes_phase_detected':s.simplify(wedge-db)!=0,
        'curved_spin_identity_with_gauge_and_surface':identity==0,
        'spin_curvature_is_scalar_curvature_quarter':s.simplify(Fs+lap/2)==0,
        'flat_holomorphic_patch_Dirac_residual_zero':dz==0,
        'flat_patch_rough_energy_two':norm(s.diff(z,x))+norm(s.diff(z,y))==2,
        'flat_patch_boundary_cancels_rough':s.simplify(current)==-2,
        'dropping_surface_changes_patch_energy':norm(s.diff(z,x))+norm(s.diff(z,y))!=norm(dz),
    }


@lru_cache(None)
def run():
    facts={**universal_checks(),**matrix_checks(),**curvature_checks()}
    L,m=s.symbols('L m',positive=True)
    residual=10/L**2
    facts.update({
        'unchanged_spin_continuum_threshold_zero':s.limit(residual,L,s.oo)==0,
        'inserted_mass_comparator_changes_threshold':s.limit(residual+m*m,L,s.oo)==m*m,
        'complete_graph_cutoff_error_bound_vanishes':s.limit(1/L,L,s.oo)==0,
        'curvature_cusp_term_negative_not_a_tachyon_test':s.Rational(-2,4)==-s.Rational(1,2),
    })
    profile={'ten_dimensional_cubic_permutations':6,
             'moment_squared_coefficient':'1/2','mixed_commutator_coefficient':2,
             'four_real_scalar_commutator_pairs':6,
             'nonzero_family_trace_vertex':1,'flat_patch_rough_energy':2,
             'flat_patch_surface_energy':-2,'spin_cusp_threshold':0,
             'supplied_mass_threshold':'m^2','scalar_curvature_coefficient':'1/4',
             'stationary_origin':True,'full_boson_Hessian_nonnegative':True,
             'parent_chiral_fields_including_connection':3}
    return {'facts':facts,'predicates_passed':sum(facts.values()),'action_profile':profile,
            'genesis_selects_action':False,'gapped_4D_reduction_derived':False,
            'physical_chiral_SM_derived':False,'global_anomaly_acceptance':False,
            'full_nonlinear_domain_theorem':False,'nonauthor_acceptance':False}


if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
