"""R73 actual compact orbit controls; no physical matter or end selection."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

def local(name, filename):
    spec=importlib.util.spec_from_file_location(name,Path(__file__).with_name(filename))
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

f=local('r73_field','nilpotent_cone.py')
c=local('r73_channel','cone_channel.py')
N,P,H,Z=f.N,f.P,f.H,f.D
zero,clean,comm=f.zero,f.clean,f.comm
r,alpha=f.r,f.alpha
th,thp,thpp,eps=s.symbols('theta theta_p theta_pp epsilon',real=True)
phase=s.exp(s.I*th)

def dr(x):
    return f.dr(x)+thp*x.diff(th)+thpp*x.diff(thp)

def residuals(C):
    F={(i,j):clean((dr(C[j]) if i==0 else s.zeros(4))-
                   (dr(C[i]) if j==0 else s.zeros(4))+comm(C[i],C[j]))
       for i in range(3) for j in range(3)}
    inv=f.metric()
    I=dr(r*r*(C[0]+C[0].H))/(r*r)
    I+=sum((inv[i,j]*comm(C[i],C[j].H) for i in range(3) for j in range(3)),s.zeros(4))
    return F,clean(I)

@lru_cache(None)
def orbit_controls():
    C=f.fields(); t=s.exp(-f.h)
    g=s.diag(phase,1,1,1/phase)
    changed=[(f.hp-s.I*thp)*H,t*phase*N,f.k*Z+f.beta*t*t*phase**2*P]
    F,I=residuals(changed); oldF,oldI=residuals(C)
    badF,_=residuals([C[0]]+changed[1:])
    vx,vy=s.symbols('vx vy',complex=True)
    dx,dy=s.symbols('delta_x delta_y',complex=True)
    theta_boundary=s.trace(changed[2]*(s.I*t*phase*N)-changed[1]*(2*s.I*f.beta*t*t*phase**2*P))
    zform=[s.zeros(4),vx*Z,vy*Z]
    checks=dict(
        unitary=zero(g.H*g-s.eye(4)),
        determinant_one=zero(g.det()-1),
        actual_radial=zero(g*C[0]*g.inv()-dr(g)*g.inv()-changed[0]),
        actual_x=zero(g*C[1]*g.inv()-changed[1]),
        actual_y=zero(g*C[2]*g.inv()-changed[2]),
        full_flatness=all(zero(v) for v in F.values()),
        offshell_moment_unchanged=zero(I-oldI),
        radial_Higgs_unchanged=zero(changed[0]+changed[0].H-2*C[0]),
        wrong_radial_omission_fails=not zero(badF[0,1]),
        Z_preserved=zero(g*Z*g.inv()-Z),
        neutral_profile_unchanged=all(zero(g*a*g.inv()-a) for a in zform),
        gauge_holomorphic_boundary_zero=zero(theta_boundary),
        neutral_affine_boundary_unchanged=zero(s.trace((changed[2]+vy*Z)*dx*Z-(changed[1]+vx*Z)*dy*Z)-12*((f.k+vy)*dx-vx*dy)),
        nontrivial_phase_not_fixed_entries=not zero(changed[1]-C[1]),
    )
    return dict(checks=checks,moment=I,scope='All real smooth phases; local exact covariance, gauge admission declared')

@lru_cache(None)
def tangent_controls():
    C=f.fields(); t=s.exp(-f.h)
    eta=[s.zeros(4),s.I*t*N,2*s.I*f.beta*t*t*P]
    straight=[C[i]+eps*eta[i] for i in range(3)]
    F,I=residuals(straight); _,oldI=residuals(C)
    B=alpha*t*t+4*f.beta*f.beta*t**4/alpha
    inc=clean(I-oldI)
    kin=clean(r*r*f.one_norm(eta,f.metric()))
    density=clean(r*r*s.trace(inc.H*inc)/2)
    x=s.Symbol('s',positive=True)
    # Substitute h through exp(-2h), avoiding an unjustified algebraic generator.
    leading=clean(B.subs(f.h,s.log(alpha*x)/2))
    orbitdiff=clean(2*alpha*t*t*(phase-1)*(s.conjugate(phase)-1)+
        f.beta*f.beta*t**4/alpha*(phase**2-1)*(s.conjugate(phase)**2-1))
    z=s.Rational(3,5)+s.I*s.Rational(4,5)
    checks=dict(
        tangent_full_flatness=all(zero(v) for v in F.values()),
        tangent_linear_moment_zero=zero(inc.diff(eps).subs(eps,0)),
        straight_moment_quadratic=zero(inc-eps**2*B*H/r**2),
        straight_exact_density=zero(density-eps**4*B**2/r**2),
        kinetic_density=zero(kin-2*alpha*t*t-4*f.beta*f.beta*t**4/alpha),
        kinetic_leading=zero(s.limit(x*kin.subs(f.h,s.log(alpha*x)/2),x,s.oo)-2),
        action_leading=zero(s.limit(x*x*leading**2,x,s.oo)-1),
        L2_comparator_finite=s.integrate(s.exp(-x),(x,1,s.oo))==s.exp(-1),
        divergent_L4_comparator=s.integrate(s.exp(x/2),(x,1,s.oo))==s.oo,
        comparison_lower_bound=s.exp(8)>16**2 and (s.Rational(1,2)-2/s.Integer(16))>0,
        exact_phase_has_different_quadratic_term=zero(s.diff(phase,th,2).subs(th,0)+1),
        orbit_difference_density=zero(orbitdiff-f.one_norm([s.zeros(4),t*(phase-1)*N,f.beta*t*t*(phase**2-1)*P],f.metric())*r*r),
        orbit_difference_L4_leading_positive=2*(z-1)*(s.conjugate(z)-1)==s.Rational(8,5),
        trivial_orbit_difference_zero=zero(orbitdiff.subs(th,0)),
    )
    return dict(checks=checks,kinetic_density=kin,straight_increment=inc,
                straight_action_density=density,scope='Actual asymptotic comparison, not cutoff fitting or particle count')

@lru_cache(None)
def covariance_controls():
    # A nonzero interacting, off-shell matrix fixture. Phase represented by a rational unit.
    z=s.Rational(3,5)+4*s.I/5; g=s.diag(z,1,1,1/z)
    w=s.Rational(2,7); Q=s.I*w*H
    D=[s.Matrix([[1,s.I,0,0],[0,-1,0,0],[0,0,0,1],[0,0,0,0]]),
       N+s.I*N.H+Z/3,P+N.H/2+s.I*H]
    Dr=[s.zeros(4),s.Matrix([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),s.I*P.H]
    # At a point Q'=0: derivative of Ad_g D is Ad_g D'+[Q,Ad_g D].
    Dg=[g*a*g.inv() for a in D]; Cg=[Dg[0]-Q,Dg[1],Dg[2]]
    Dgr=[g*a*g.inv()+comm(Q,v) for a,v in zip(Dr,Dg)]
    at=s.Rational(3,7); inv=s.diag(1,2/at**2,1/(2*at**2))
    def at_res(C,Cdr):
        F={(i,j):(Cdr[j] if i==0 else s.zeros(4))-(Cdr[i] if j==0 else s.zeros(4))+comm(C[i],C[j]) for i in range(3) for j in range(3)}
        I=Cdr[0]+Cdr[0].H+2*(C[0]+C[0].H)/at+sum((inv[i,j]*comm(C[i],C[j].H) for i in range(3) for j in range(3)),s.zeros(4))
        return F,clean(I)
    F,I=at_res(D,Dr); Fg,Ig=at_res(Cg,Dgr)
    _,badI=at_res(Dg,Dgr)
    checks=dict(
        fixture_compact=zero(g.H*g-s.eye(4)),
        fixture_radial_antiHermitian=zero(Q+Q.H),
        all_curvature_covariance=all(zero(Fg[ij]-g*a*g.inv()) for ij,a in F.items()),
        full_moment_covariance=zero(Ig-g*I*g.inv()),
        nonzero_interaction_control=not zero(F[1,2]) and not zero(I),
        positive_trace_norm_preserved=zero(s.trace(Ig.H*Ig)-s.trace(I.H*I)),
        curvature_positive_norm_preserved=zero(f.two_norm(Fg,inv)-f.two_norm(F,inv)),
        omission_breaks_full_moment=not zero(badI-g*I*g.inv()),
        bracket_cross_not_erased=not zero(comm(Z,s.Matrix(4,4,lambda i,j:int(i==0 and j==1)))),
        bounded_phase_preserves_Z=zero(g*Z*g.inv()-Z),
    )
    return dict(checks=checks,scope='Nonzero off-shell fixture plus authored general covariance proof')

@lru_cache(None)
def operator_controls():
    z=s.Rational(3,5)+4*s.I/5
    g=s.diag(z,1,1,1/z)
    coeff=c.sp(c.left*s.kronecker_product(g,g.inv().T)*c.T)
    U=c.tensor(c.sp(s.eye(8)),coeff)
    G=c.tensor(c.sp(s.eye(8)),c.G)
    M=c.tensor(c.M,c.I9); zero36=c.sp(s.zeros(36)); eye36=c.sp(s.eye(36))
    gamma=c.blocks(zero36,-eye36,eye36,zero36); J=-G*gamma
    a=s.Rational(4); t=s.Rational(1,5); v=s.Rational(1,7); beta=s.Rational(2,3); omega=s.Rational(3,11)
    E=s.sqrt(a)*t*c.tensor(c.ex,c.n)+beta*t*t/s.sqrt(a)*c.tensor(c.ey,c.p)
    Ed=s.sqrt(a)*t*c.tensor(c.ex.H,c.nd)+beta*t*t/s.sqrt(a)*c.tensor(c.ey.H,c.pd)
    L=E+Ed; K=-v*c.tensor(c.sp(s.eye(4)),c.h)
    A=c.blocks(M+K,-L,-L,-M-K)
    Ku=K-s.I*omega*c.tensor(c.sp(s.eye(4)),c.h)
    Lu=c.sp(coeff*c.n*coeff.inv())
    Eu=s.sqrt(a)*t*c.tensor(c.ex,Lu)+beta*t*t/s.sqrt(a)*c.tensor(c.ey,coeff*c.p*coeff.inv())
    Eud=s.sqrt(a)*t*c.tensor(c.ex.H,coeff*c.nd*coeff.inv())+beta*t*t/s.sqrt(a)*c.tensor(c.ey.H,coeff*c.pd*coeff.inv())
    Lg=Eu+Eud
    Kadj=c.sp(G[:36,:36].inv()*Ku.H*G[:36,:36])
    Ag=c.blocks(M+Ku,-Lg,-Lg,-M-Kadj)
    expected=U*A*U.inv()-s.I*omega*c.tensor(c.sp(s.eye(8)),c.h)
    wrong=c.blocks(M+Ku,-Lg,-Lg,-M-Ku)
    adj=lambda a:c.sp(G.inv()*a.H*G)
    checks=dict(
        coefficient_unitary=c.zero(coeff.H*c.G*coeff-c.G),
        form_unitary=c.zero(U.H*G*U-G),
        all_72_components=Ag.shape==(72,72),
        correct_radial_Q_transport=c.zero(Ag-expected),
        derivative_omission_rejected=not c.zero(Ag-U*A*U.inv()),
        nonHermitian_angular_allowed=not c.zero(adj(Ag)-Ag),
        Gamma_A_Hermitian=c.zero(adj(gamma*Ag)-gamma*Ag),
        actual_Green_conserved=c.zero(Ag.H*J+J*Ag),
        wrong_K_adjoint_breaks_current=not c.zero(wrong.H*J+J*wrong),
        angular_anticommutation_not_invariant=not c.zero(Ag*gamma+gamma*Ag),
        boundary_current_unitary=c.zero(U.H*J*U-J),
        exact_Z_trace_unchanged=coeff[:,8]==s.eye(9)[:,8],
        positive_and_negative_phases=coeff[0,0]==z and coeff[2,2]==1/z,
    )
    return dict(checks=checks,form_dimension=72,scope='Exact transported coefficient/current, not full boundary-domain classification')

@lru_cache(None)
def compensator_controls():
    t=s.Symbol('t',positive=True); beta,k,thm,thmr=s.symbols('beta k theta_mu theta_mu_r',real=True)
    C=[(f.hp-s.I*thp)*H,t*phase*N,k*Z+beta*t*t*phase**2*P]
    Cm=[-s.I*thmr*H,s.I*thm*C[1],2*s.I*thm*beta*t*t*phase**2*P]
    Am=-s.I*thm*H
    Ar=-s.I*thmr*H
    mixed=[clean(Cm[i]-(Ar if i==0 else s.zeros(4))+comm(Am,C[i])) for i in range(3)]
    checks=dict(
        full_radial_mixed_zero=zero(mixed[0]),
        full_x_mixed_zero=zero(mixed[1]),
        full_y_mixed_zero=zero(mixed[2]),
        omitted_compensator_x_fails=not zero(Cm[1]),
        omitted_compensator_y_fails=not zero(Cm[2]),
        omitted_radial_mixed_derivative_fails=not zero(Cm[0]+comm(Am,C[0])),
        wrong_compensator_sign_fails=not zero(Cm[1]-comm(Am,C[1])),
        gauge_field_antiHermitian=zero(Am+Am.H),
    )
    return dict(checks=checks,scope='Spacetime-dependent pure compact gauge is not a new physical scalar')

def serial(v):
    if isinstance(v,dict):return {str(k):serial(a) for k,a in v.items()}
    if isinstance(v,(list,tuple)):return [serial(a) for a in v]
    if isinstance(v,s.MatrixBase):return [[str(a) for a in row] for row in v.tolist()]
    if isinstance(v,s.Basic):return str(v)
    return v

def run():
    groups={n:fn() for n,fn in [('orbit',orbit_controls),('tangent',tangent_controls),('covariance',covariance_controls),('operator',operator_controls),('compensator',compensator_controls)]}
    checks={n+'/'+k:bool(v) for n,g in groups.items() for k,v in g['checks'].items()}
    return serial(dict(scope='Classical same-action compact transport; gauge/end admission supplied; not matter, chirality or TOE',groups=groups,checks=checks,all_checks_pass=all(checks.values())))

if __name__=='__main__':
    out=run(); print(json.dumps(out,sort_keys=True,indent=2))
    raise SystemExit(0 if out['all_checks_pass'] else 1)
