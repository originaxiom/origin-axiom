"""Separate real-block kernels and polynomial boundary linsolve controls."""
from functools import lru_cache
import json
import sympy as s
I=s.I;t=s.symbols('t',real=True)
def zero(a):return a.applyfunc(s.expand)==s.zeros(*a.shape)
def rb(a):return a.applyfunc(s.re).row_join(-a.applyfunc(s.im)).col_join(a.applyfunc(s.im).row_join(a.applyfunc(s.re)))
@lru_cache(None)
def run():
    checks={}
    def ck(k,v):checks[k]=bool(v)
    # Formal composition: ad(B) is Hermitian, D_A is skew; no native matrix jets.
    L=s.Matrix([[0,-1,2],[1,0,-3],[-2,3,0]])
    T=s.Matrix([[2,1,0],[1,-1,2],[0,2,3]])
    ck('real_skew_connection_Hermitian_Higgs',L.T==-L and T.T==T and L*T!=T*L)
    d=L-T;dp=L+T;P=d.H*d
    ck('formal_actual_adjoint',d.H==-dp)
    ck('formal_cross_term_is_moment',zero(P-(-L*L+T*T+(L*T-T*L))))
    # Flat harmonic constant commuting connection makes the moment term zero.
    Af=s.Matrix([[0,-2,0],[2,0,0],[0,0,0]])
    Bf=s.diag(3,3,4);Df=Af-Bf;Pf=Df.T*Df
    ck('harmonic_real_positive_P',Af*Bf==Bf*Af and Pf.T==Pf and all(v>0 for v in Pf.eigenvals()))
    ck('formal_wrong_Higgs_sign_rejected',not zero(Pf-(-Af*Af-Bf*Bf)))
    u=s.Matrix([1,2,3]);v=s.Matrix([2,3,5])
    # Real coordinate block of D_A plus complex Higgs uses i Bf as odd-real map.
    C=Af;J=Bf
    D0=C+I*J;P0=D0.H*D0
    # This finite control is required to have real Gram; use disjoint paired rows below.
    ck('cross_term_not_silently_dropped',not zero(P0-(C.T*C+J.T*J)))
    # Solve the actual nonlocal boundary problem; no explicit native integration formula.
    ut=3-2*t+5*t**3;source=s.diff(ut,t);q=-(ut.subs(t,1)-ut.subs(t,0))
    c=s.symbols('c0:5',real=True);f=sum(c[j]*t**j for j in range(5))
    equations=list(s.Poly(s.expand(-s.diff(f,t,2)-source),t).all_coeffs())
    boundary=[f.subs(t,1)-f.subs(t,0),s.diff(f,t).subs(t,1)-s.diff(f,t).subs(t,0)-q]
    sols=s.linsolve(equations+boundary,c)
    ck('boundary_linsolve_exists_with_kernel',sols!=s.EmptySet and any(q.free_symbols for q in next(iter(sols))))
    unique=s.linsolve(equations+boundary+[s.integrate(f,(t,0,1))],c)
    sf=s.expand(f.subs(dict(zip(c,next(iter(unique))))))
    ck('boundary_mean_fixed_unique_solution',not sf.free_symbols-{t} and s.integrate(sf,(t,0,1))==0)
    ck('boundary_source_and_flux_exact',s.expand(-s.diff(sf,t,2)-source)==0 and sf.subs(t,0)==sf.subs(t,1) and s.diff(sf,t).subs(t,1)-s.diff(sf,t).subs(t,0)==q)
    ck('boundary_inconsistent_flux_rejected',s.linsolve(equations+[boundary[0],boundary[1]-1],c)==s.EmptySet)
    ck('boundary_wrong_flux_sign_rejected',s.linsolve(equations+[boundary[0],boundary[1]+2*q],c)==s.EmptySet)
    ck('boundary_real_slice_preserves_harmonic_mean',s.diff(ut+s.diff(sf,t),t)==0 and s.expand(ut+s.diff(sf,t)-s.integrate(ut,(t,0,1)))==0)
    ck('boundary_normal_derivatives_not_frozen',s.diff(sf,t).subs(t,0)!=0 and s.diff(sf,t).subs(t,1)!=0)
    # Full real-block kernel, followed by an orthogonal compact-gauge projector.
    cases=[]
    for rank,h,ends in [(1,1,2),(2,0,1),(2,3,2),(3,1,1)]:
        m=2*rank+h;d0=s.zeros(m,rank+ends);d1=s.zeros(rank,m)
        for j in range(rank):d0[2*j,j]=2;d0[2*j+1,j]=I;d1[j,2*j]=I;d1[j,2*j+1]=-2
        U=s.eye(rank)
        for j in range(rank-1):U[j,j+1]=1
        active=d0[:,:rank]*U
        d0=active.row_join(s.zeros(m,ends));ds=d0.H
        M=rb(d1).col_join(ds.applyfunc(s.im).row_join(ds.applyfunc(s.re)))
        kernels=M.nullspace();K=s.Matrix.hstack(*kernels) if kernels else s.zeros(2*m,0)
        G=active.applyfunc(s.re).col_join(active.applyfunc(s.im))
        gram=G.T*G;Pr=s.eye(2*m)-G*gram.inv()*G.T
        harmonic=Pr*K
        H1=m-d0.rank()-d1.rank()
        key=f'block_{rank}_{h}_{ends}_'
        ck(key+'chain_and_positive_gauge_Gram',zero(d1*d0) and all(gram[:j,:j].det()>0 for j in range(1,rank+1)))
        ck(key+'real_quotient_matches_complex_H1',harmonic.rank()==2*H1 and K.cols-G.rank()==2*H1)
        ck(key+'slice_is_orthogonal_not_deleting_harmonics',zero(G.T*harmonic) and zero(M*harmonic) and zero(Pr*Pr-Pr) and zero(Pr.T-Pr))
        ck(key+'zero_form_kernel_kept',len(d0.nullspace())==ends)
        imaginary=(I*active[:,0]);iv=imaginary.applyfunc(s.re).col_join(imaginary.applyfunc(s.im))
        ck(key+'complex_gauge_not_moment_null',not zero(M*iv))
        cproj=rb(ds)*harmonic
        ck(key+'whole_complex_adjoint_harmonic',zero(cproj))
        cases.append({'complex_H1':H1,'real_kernel_before_gauge':K.cols,'real_gauge_rank':G.rank(),'real_quotient_rank':harmonic.rank(),'endpoint_kernel':ends})
    out={'predicates':checks,'predicates_passed':sum(checks.values()),'different_finite_controls':cases,
         'native_imported':False,'same_author':True,'conditional_linear_quotient':all(checks.values()),
         'global_silver_PDE_recomputed':False,'physical_population_recomputed':False,
         'full_multiplet_or_Hamiltonian':False,'nonlinear_moduli':False,'outside_review':False,
         'generated_selection':False,'full_goal_achieved':False}
    print(json.dumps(out,indent=2,sort_keys=True));assert all(checks.values()),[k for k,v in checks.items() if not v]
    return out
if __name__=='__main__':run()
