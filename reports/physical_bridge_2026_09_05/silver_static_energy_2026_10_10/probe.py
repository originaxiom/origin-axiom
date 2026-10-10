"""Canonical static superspace expansion; not a particle-spectrum computation."""
from functools import lru_cache
import json
import sympy as s

I=s.I
N=3
ONE=s.eye(N)
ZERO=s.zeros(N)
Q=s.Rational

def mz(a):return all(s.expand(x)==0 for x in a)
def tidy(a):return {u:v.applyfunc(s.expand) for u,v in a.items() if not mz(v)}
def add(*args):
    out={}
    for a in args:
        for u,c in a.items():out[u]=out.get(u,ZERO)+c
    return tidy(out)
def scale(a,c):return tidy({u:c*v for u,v in a.items()})
def mul(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():
            if u&v:continue
            swaps=sum((v&((1<<j)-1)).bit_count() for j in range(4) if u&(1<<j))
            out[u|v]=out.get(u|v,ZERO)+(-1)**swaps*c*d
    return tidy(out)
def left(a,j):
    return tidy({u^(1<<j):(-1)**((u&((1<<j)-1)).bit_count())*c
                 for u,c in a.items() if u&(1<<j)})
def dag(a):
    out={}
    for u,c in a.items():
        term={0:c.H}
        for j in reversed(range(4)):
            if u&(1<<j):term=mul(term,{1<<(j^2):ONE})
        out=add(out,term)
    return out
def coeff(a,mask):return a.get(mask,ZERO)
def d4(a):return -s.trace(coeff(a,15))/4
def d2(a):return s.trace(coeff(a,3))/2
def comm(a,b):return a*b-b*a
def norm(a):return s.expand(s.trace(a*a.H))
def chiral(p,f):return {0:p,3:2*f}

@lru_cache(None)
def run():
    facts={}
    def ck(k,v):facts[k]=bool(v)
    X=s.diag(1,-1,0)
    Y=s.Matrix([[0,1,I],[1,0,2],[-I,2,0]])
    T=s.Matrix([[0,I,1],[-I,1,0],[1,0,-1]])
    A=X;B=Y;D=X+Y;dD=2*T-X;F=X+2*Y+I*(T-Y)
    p=A+I*B
    theta2={3:2*ONE};bar2={12:-2*ONE};u=mul(theta2,bar2)
    ck('canonical_adjoints',dag(theta2)==bar2 and dag(u)==u)
    ck('measure_normalization',d2(theta2)==3 and d4(u)==3)
    ck('left_derivative_anticommutation',mz(coeff(add(left(left(u,0),1),left(left(u,1),0)),12)))
    ck('noncommuting_fixture',not mz(comm(A,B)) and not mz(comm(B,D)))
    ck('actual_F_complex',not mz(F-F.H))
    V=scale(mul(u,{0:D}),Q(1,2))
    G=add({0:ONE},scale(V,2));Gi=add({0:ONE},scale(V,-2))
    ck('exponential_inverse_exact',mul(G,Gi)=={0:ONE} and mul(V,V)=={})
    Phi=chiral(p,F);barPhi=dag(Phi)
    dG=mul(u,{0:dD})
    Z=add(mul(Gi,dG),scale(mul(mul(Gi,barPhi),G),I),scale(Phi,-I))
    expected={0:2*B,3:-2*I*F,12:-2*I*F.H,
              15:-4*(dD+I*comm(p.H,D))}
    ck('full_static_Z_expansion',Z==tidy(expected))
    ck('twisted_Z_reality',dag(Z)==mul(mul(G,Z),Gi))
    directK=s.expand(d4(mul(Z,Z))/4)
    K=s.expand(s.trace(B*(dD+I*comm(A,D)))+norm(F)/2)
    ck('direct_kinetic_coefficient_half',s.expand(directK-K)==0)
    ck('wrong_F_coefficient_two_rejected',s.expand(directK-K-3*norm(F)/2)!=0)
    ck('B_commutator_trace_cancels',s.trace(B*comm(B,D))==0)
    ck('wrong_top_measure_sign_rejected',s.expand(-directK-K)!=0)
    # barD_j=-left_bj; barD2=-2*barD1*barD2, right operator first.
    def bd(a,j):return scale(left(a,j+2),-1)
    def bd2(a):return scale(bd(bd(a,1),0),-2)
    W=[scale(bd2(mul(Gi,left(G,j))),Q(-1,4)) for j in range(2)]
    ck('W_direct_left_derivative',[W[0],W[1]]==[{2:2*D},{1:-2*D}])
    WW=add(scale(mul(W[1],W[0]),-1),mul(W[0],W[1]))
    ck('spinor_raising_convention',WW=={3:8*D*D})
    gauge=s.expand((d2(WW)+s.conjugate(d2(WW)))/16)
    ck('gauge_D_coefficient_half',s.expand(gauge-s.trace(D*D)/2)==0)
    ck('wrong_bartheta_sign_rejected',dag(theta2)!=scale(bar2,-1))

    # All six epsilon terms, with independent derivatives, no integration
    # by parts hidden inside the expansion. Matrix multiplication is ordered.
    ps=[X+I*Y,T+2*I*X,Y+I*T]
    fs=[F,T+I*X,Y-2*I*T]
    dp=[[ (j+1)*X+(k+1)*Y+I*(j-k+1)*T for k in range(3)] for j in range(3)]
    df=[[ (k+2)*T+I*(j+1)*Y for k in range(3)] for j in range(3)]
    eps=lambda i,j,k:s.LeviCivita(i,j,k)
    PP=[chiral(ps[i],fs[i]) for i in range(3)]
    raw={}
    cc=[ZERO.copy() for _ in range(3)]
    divergence=0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                e=eps(i,j,k)
                if not e:continue
                raw=add(raw,scale(mul(PP[i],chiral(dp[j][k],df[j][k])),e),
                        scale(mul(PP[i],add(mul(PP[j],PP[k]),scale(mul(PP[k],PP[j]),-1))),I*e/3))
                cc[i]+=e*(dp[j][k]-dp[k][j]+I*comm(ps[j],ps[k]))
                divergence+=e*s.trace(dp[j][i]*fs[k]+ps[i]*df[j][k])
    source=sum(s.trace(fs[i]*cc[i]) for i in range(3))
    cs=s.expand(d2(raw))
    ck('CS_direct_source_and_divergence',s.expand(cs-source-divergence)==0)
    ck('CS_surface_omission_detected',s.expand(divergence)!=0 and s.expand(cs-source)!=0)
    cubic=sum(I*eps(i,j,k)*s.trace(fs[i]*comm(ps[j],ps[k]))
              for i in range(3) for j in range(3) for k in range(3))
    ck('nonzero_holomorphic_cubic_retained',s.expand(cubic)!=0)

    # Direct covariant integration by parts on an interval, a local control
    # for the volume-form/divergence theorem on the actual compact core.
    x=s.symbols('x',real=True)
    bx=(1+x)*Y;dx=(x*x+x)*Y+T
    leftval=s.trace(bx*(s.diff(dx,x)+I*comm(X,dx)))
    mu=s.diff(bx,x)+I*comm(X,bx)
    bulk=-s.trace(dx*mu);surface=s.trace(bx*dx).subs(x,1)-s.trace(bx*dx).subs(x,0)
    ck('covariant_IBP_keeps_surface',s.integrate(s.expand(leftval-bulk),(x,0,1))==surface)
    ck('dropping_real_surface_detected',surface!=0 and s.integrate(s.expand(leftval-bulk),(x,0,1))!=0)
    ck('parallel_D_zero_mean_flux_cancels',s.integrate(s.cos(x),(x,0,2*s.pi))==0)
    ck('not_pointwise_flux_zero',s.cos(x).subs(x,0)==1)
    ck('nonparallel_D_breaks_cancellation',s.integrate(s.cos(x)**2,(x,0,2*s.pi))==s.pi)
    ck('constant_gauge_flux_rejected',s.trace(X*X)>0)
    structure=s.kronecker_product(X,s.eye(3));gaugeD=s.kronecker_product(s.eye(3),Y)
    ck('structure_flux_nonzero_but_orthogonal',norm(structure)>0 and s.trace(structure*gaugeD)==0)
    y=s.symbols('y',real=True)
    wedge=s.cos(x)*s.cos(y)*s.trace(Y*Y)
    ck('A1_pairing_integrated_not_pointwise',s.integrate(wedge,(x,0,2*s.pi),(y,0,2*s.pi))==0 and wedge.subs({x:0,y:0})!=0)

    # Differentiate real/imaginary coordinates, not a holomorphic label.
    d,m,fr,fi,cr,ci=s.symbols('d m fr fi cr ci',real=True)
    f=fr+I*fi;c=cr+I*ci
    ell=d*d/2-d*m+(fr*fr+fi*fi)/2+(f*c+s.conjugate(f*c))/4
    sol={d:m,fr:-cr/2,fi:ci/2}
    ck('real_auxiliary_variation',all(s.expand(s.diff(ell,v).subs(sol))==0 for v in (d,fr,fi)))
    ck('F_conjugate_solution',s.expand(f.subs(sol)+s.conjugate(c)/2)==0)
    ck('wrong_F_no_dagger_rejected',s.expand(s.diff(ell,fi).subs({fr:-cr/2,fi:-ci/2}))==-ci)
    potential=m*m/2+(cr*cr+ci*ci)/8
    ck('completed_real_squares',s.expand(ell-((d-m)**2/2+((fr+cr/2)**2+(fi-ci/2)**2)/2-potential))==0)
    ck('onshell_exact_positive_potential',s.expand(ell.subs(sol)+potential)==0)
    ck('auxiliary_real_hessian_positive',s.hessian(ell,(d,fr,fi))==s.eye(3))

    # Compact-gauge Ward identity including nonzero derivative jets.
    aa=[X,Y,T];bb=[Y,T,X];db=[2*T,X,3*Y]
    lam=X+T;dl=[T,X,Y+T]
    moment=sum((db[j]+I*comm(aa[j],bb[j]) for j in range(3)),ZERO)
    da=[dl[j]+I*comm(aa[j],lam) for j in range(3)]
    deltaB=[I*comm(bb[j],lam) for j in range(3)]
    dm=sum((I*comm(db[j],lam)+I*comm(bb[j],dl[j])+I*comm(da[j],bb[j])+I*comm(aa[j],deltaB[j]) for j in range(3)),ZERO)
    ck('moment_gauge_Ward_with_jets',mz(dm-I*comm(moment,lam)))
    bad=dm-sum((I*comm(bb[j],dl[j]) for j in range(3)),ZERO)
    ck('omitting_derivative_jets_rejected',not mz(bad-I*comm(moment,lam)))
    ph=[aa[j]+I*bb[j] for j in range(3)]
    deltaP=[dl[j]+I*comm(ph[j],lam) for j in range(3)]
    dh=I*comm(dp[0][1]-dp[1][0],lam)+I*comm(ph[1],dl[0])-I*comm(ph[0],dl[1])+I*comm(deltaP[0],ph[1])+I*comm(ph[0],deltaP[1])
    hh=dp[0][1]-dp[1][0]+I*comm(ph[0],ph[1])
    ck('curvature_gauge_Ward_with_jets',mz(dh-I*comm(hh,lam)))
    t=s.symbols('t',real=True);Kmat=I*comm(X,Y)
    interacting=norm(t*(1+t)*Kmat)/2
    ck('nonzero_cubic_static_term',s.expand(interacting).coeff(t,3)>0)
    ck('nonzero_quartic_static_term',s.expand(interacting).coeff(t,4)>0)
    ck('nonlinear_moment_not_dropped',norm(I*comm(X,Y))>0)
    # All-direction theorem is in PROOF, these are discriminating controls.
    hess=s.hessian((m*m)/2+(cr*cr+ci*ci)/8,(m,cr,ci))
    ck('residual_hessian_positive',hess==s.diag(1,Q(1,4),Q(1,4)))
    bump=x**3*(1-x)**3
    positive=s.integrate(norm(s.diff(bump,x)*X),(x,0,1))
    ck('positive_non_gauge_direction',positive>0 and all(s.diff(bump,x,j).subs(x,e)==0 for j in range(3) for e in (0,1)))
    af=[X,ZERO,ZERO];bf=[2*X,ZERO,ZERO]
    pf=[af[j]+I*bf[j] for j in range(3)]
    daf=[dl[j]+I*comm(af[j],lam) for j in range(3)]
    dbf=[I*comm(bf[j],lam) for j in range(3)]
    dpf=[dl[j]+I*comm(pf[j],lam) for j in range(3)]
    mf=sum((I*comm(bf[j],dl[j])+I*comm(daf[j],bf[j])+I*comm(af[j],dbf[j]) for j in range(3)),ZERO)
    hf=I*comm(pf[1],dl[0])-I*comm(pf[0],dl[1])+I*comm(dpf[0],pf[1])+I*comm(pf[0],dpf[1])
    ck('nonzero_gauge_tangent_null_at_flat_background',mz(mf) and mz(hf) and any(not mz(v) for v in dpf))
    ck('zero_residual_has_no_mass_gap_certificate',potential.subs({m:0,cr:0,ci:0})==0)
    result={'facts':facts,'predicates_passed':sum(facts.values()),
            'normalizations':{'F_kinetic':'1/2','D_kinetic':'1/2','Fc_source':'1/4','F_solution':'-c_dagger/2','V':'norm(mu)^2/2+norm(c)^2/8'},
            'matrix_controls_are_not_silver_PDE':True,
            'coefficient_recomputed':False,'full_E8_structure_constants_recomputed':False,
            'static_energy_derived':True,'full_dynamical_stability_proved':False,
            'physical_kernel_computed':False,'boundary_selected':False,
            'nonauthor_analytic_review':False,'physical_goal_achieved':False}
    assert all(facts.values()),[k for k,v in facts.items() if not v]
    return result

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
