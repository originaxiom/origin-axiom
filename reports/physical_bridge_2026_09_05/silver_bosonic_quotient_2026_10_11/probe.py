"""Exact compact-gauge algebra and boundary mechanisms, not a silver PDE."""
from functools import lru_cache
import json
import sympy as s
I=s.I;R=s.Rational;xx=s.symbols('x0:3',real=True);t=s.symbols('t',real=True)
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1);O=s.zeros(2)
def norm(a):return a.applyfunc(s.expand)
def eq(a,b):return norm(a-b)==s.zeros(*a.shape)
def comm(a,b):return a*b-b*a
def summ(a):return sum(a,O)
def herm(a):return norm((a+a.H)/2)
def imag(a):return norm((a-a.H)/(2*I))
def da(f,j,A):return norm(f.diff(xx[j])+I*comm(A[j],f))
def dm(f,j,A,B):return norm(da(f,j,A)-comm(B[j],f))
def dp(f,j,A,B):return norm(da(f,j,A)+comm(B[j],f))
def moment(A,B):return summ(da(B[j],j,A) for j in range(3))
def split(a,A,B):
    u=list(map(herm,a));v=list(map(imag,a))
    k=summ(da(u[j],j,A)+I*comm(B[j],v[j]) for j in range(3))
    m=summ(da(v[j],j,A)+I*comm(u[j],B[j]) for j in range(3))
    return norm(k),norm(m)
def P(f,A,B):return norm(-summ(dp(dm(f,j,A,B),j,A,B) for j in range(3)))
def curl(a,A,B):return [norm(dm(a[k],j,A,B)-dm(a[j],k,A,B)) for j in range(3) for k in range(j+1,3)]
def curv(A,B):
    phi=[A[j]+I*B[j] for j in range(3)]
    return [norm(phi[k].diff(xx[j])-phi[j].diff(xx[k])+I*comm(phi[j],phi[k])) for j in range(3) for k in range(j+1,3)]

@lru_cache(None)
def run():
    facts={}
    def ck(k,v):facts[k]=bool(v)
    x,y,z=xx
    A=[(1+x)*X+y*Y,(2+y*y)*Y+z*Z,(1+z)*Z+x*X]
    B=[(1+y)*Y+x*Z,(2+z)*Z+y*X,(1+x)*X+z*Y]
    u=[(1+x*x)*Z+y*X,(2+y)*X+z*Y,(1+z*z)*Y+x*Z]
    v=[(2+x)*Y+z*Z,(1+y*y)*Z+x*X,(3+z)*X+y*Y]
    a=[u[j]+I*v[j] for j in range(3)]
    lam=(1+x+y*z)*X+(2+x*x+z)*Y+y*Z
    kap,m=split(a,A,B);mu=moment(A,B)
    ck('actual_real_divergence_split',eq(summ(dp(a[j],j,A,B) for j in range(3)),kap+I*m))
    ck('kappa_and_moment_Hermitian',eq(kap,kap.H) and eq(m,m.H))
    gl=[dm(lam,j,A,B) for j in range(3)];gk,gm=split(gl,A,B)
    ck('generic_moment_Ward_with_full_jets',eq(gm,I*comm(mu,lam)))
    ck('generic_gauge_fixing_Ward',eq(gk,-P(lam,A,B)+comm(mu,lam)))
    expected=-summ(da(da(lam,j,A),j,A) for j in range(3))+comm(mu,lam)+summ(comm(B[j],comm(B[j],lam)) for j in range(3))
    ck('full_zero_form_cross_terms_cancel',eq(P(lam,A,B),expected))
    ck('curvature_Ward_all_pairs',all(eq(c,I*comm(h,lam)) for c,h in zip(curl(gl,A,B),curv(A,B))))
    ck('generic_residuals_not_assumed_zero',not eq(mu,O) and any(not eq(h,O) for h in curv(A,B)))
    ck('frozen_derivative_gauge_rejected',not eq(split([-comm(b,lam) for b in B],A,B)[1],gm))
    Af=[Z,2*Z,3*Z];Bf=[2*Z,3*Z,5*Z]
    gf=[dm(lam,j,Af,Bf) for j in range(3)];fk,fm=split(gf,Af,Bf);pl=P(lam,Af,Bf)
    ck('flat_harmonic_fixture_verified',eq(moment(Af,Bf),O) and all(eq(h,O) for h in curv(Af,Bf)))
    ck('compact_gauge_is_full_Hessian_null',eq(fm,O) and all(eq(c,O) for c in curl(gf,Af,Bf)))
    ck('flat_real_P_gauge_fixing',eq(fk,-pl) and eq(pl,pl.H))
    wrong=-summ(da(da(lam,j,Af),j,Af) for j in range(3))-summ(comm(b,comm(b,lam)) for b in Bf)
    ck('wrong_Higgs_potential_sign_rejected',not eq(pl,wrong))
    imk,imm=split([I*f for f in gf],Af,Bf)
    ck('complex_gauge_flat_but_not_moment_zero',all(eq(c,O) for c in curl([I*f for f in gf],Af,Bf)) and eq(imm,-pl) and not eq(imm,O))
    ck('imaginary_gauge_not_compact_slice',eq(imk,O) and s.trace(imm.subs({x:0,y:0,z:0})**2)>0)
    # Dirichlet compact-gauge test of the actual positive scalar form.
    lf=x*(1-x)*X+x*x*(1-x)*Y
    energy=s.trace(summ(da(lf,j,Af).H*da(lf,j,Af)+comm(Bf[j],lf).H*comm(Bf[j],lf) for j in range(3)))
    bulk=s.trace(lf*P(lf,Af,Bf))
    en=s.integrate(s.expand(energy),(x,0,1))
    ck('positive_real_form_with_nonunitary_B',en>0 and s.expand(s.integrate(bulk,(x,0,1))-en)==0)
    ck('nonzero_gauge_first_and_second_jets',not eq(lam.diff(x),O) and not eq(lam.diff(x,2),O))
    # Nonlocal zero-Fourier interval analogy: SAME boundary constant value.
    ut=1+t+t*t;vt=2+t*(1-t)
    mean=s.integrate(ut,(t,0,1));lt=s.integrate(-ut+mean,t);lt=lt-lt.subs(t,0)
    kap0=s.diff(ut,t);flux=ut.subs(t,1)-ut.subs(t,0);q=-flux
    ck('source_flux_Fredholm_compatibility',s.integrate(kap0,(t,0,1))+q==0)
    ck('wrong_flux_sign_rejected',s.integrate(kap0,(t,0,1))-q!=0)
    ck('real_inhomogeneous_boundary_solution',s.expand(-s.diff(lt,t,2)-kap0)==0 and lt.subs(t,1)==lt.subs(t,0) and s.diff(lt,t).subs(t,1)-s.diff(lt,t).subs(t,0)==q)
    ck('normal_gauge_jets_retained',s.diff(lt,t).subs(t,0)!=0 and s.diff(lt,t).subs(t,1)!=0)
    ck('slice_cancels_kappa_and_integrated_real_flux',s.diff(ut+s.diff(lt,t),t)==0 and (ut+s.diff(lt,t)).subs(t,1)==(ut+s.diff(lt,t)).subs(t,0))
    ck('imaginary_normal_primary_preserved',vt.subs(t,1)==vt.subs(t,0))
    ck('physical_harmonic_constant_not_removed',s.expand(ut+s.diff(lt,t)-mean)==0 and mean!=0)
    ck('frozen_normal_flux_cannot_solve_source',s.integrate(kap0,(t,0,1))!=0)
    ff=1+t**3-R(3,2)*t*t+t/2;gg=2+t*t*(1-t)**2
    green=s.integrate(s.expand(ff*(-s.diff(gg,t,2))+s.diff(ff,t,2)*gg),(t,0,1))
    badg=gg+t*(1-t)
    ck('integrated_mixed_Green_form_zero',green==0 and ff.subs(t,1)==ff.subs(t,0) and gg.subs(t,1)==gg.subs(t,0))
    ck('nonzero_projected_flux_Green_rejected',s.integrate(s.expand(ff*(-s.diff(badg,t,2))+s.diff(ff,t,2)*badg),(t,0,1))!=0)
    rr,amp=s.symbols('radius amplitude',positive=True)
    ck('all_nonzero_covector_Dirichlet_symbol',s.exp(-rr*t).subs(t,0)==1 and s.diff(amp*s.exp(-rr*t),t,2)==rr**2*amp*s.exp(-rr*t))
    # Exact finite complexes, NOT silver/E8 population data.
    toy=[]
    for r,h,k in [(1,0,1),(1,2,1),(2,1,2),(3,2,1)]:
        msize=2*r+h;d0=s.zeros(msize,r+k);d1=s.zeros(r,msize)
        for j in range(r):d0[2*j,j]=1;d0[2*j+1,j]=I;d1[j,2*j]=1;d1[j,2*j+1]=I
        re=d1.applyfunc(s.re);im=d1.applyfunc(s.im);ds=d0.H
        realclosed=re.row_join(-im).col_join(im.row_join(re))
        momentmat=ds.applyfunc(s.im).row_join(ds.applyfunc(s.re))
        physical=realclosed.col_join(momentmat)
        gaugemat=d0.applyfunc(s.re).col_join(d0.applyfunc(s.im))
        h1=msize-d0.rank()-d1.rank();quotient=2*msize-physical.rank()-gaugemat.rank()
        ck(f'toy_{r}_{h}_{k}_complex_and_real_quotient',d1*d0==s.zeros(r,r+k) and quotient==2*h1)
        ck(f'toy_{r}_{h}_{k}_endpoint_kernel_kept',len(d0.nullspace())==k)
        vec=d0*s.Matrix(list(range(1,r+1))+[0]*k)
        if h:
            vec[-1]+=2+3*I
        coeff=ds*vec
        lamfix=s.Matrix([-s.re(coeff[j])/2 for j in range(r)]+[0]*k)
        ah=vec+d0*lamfix
        ck(f'toy_{r}_{h}_{k}_faithful_harmonic_slice',d1*ah==s.zeros(r,1) and ds*ah==s.zeros(r+k,1) and (not h or ah[-1]==2+3*I))
        ck(f'toy_{r}_{h}_{k}_imaginary_gauge_rejected',any(v!=0 for v in (ds*(I*d0[:,0])).applyfunc(s.im)))
        toy.append({'gauge_rank':r,'harmonic_complex_dimension':h1,'real_physical_quotient':quotient,'endpoint_kernel':k})
    out={'facts':facts,'predicates_passed':sum(facts.values()),'finite_complex_controls':toy,
         'conditional_smooth_linear_quotient':all(facts.values()),'compact_real_gauge_only':True,
         'global_PDE_solved_numerically':False,'silver_census_recomputed':False,
         'nonlinear_moduli_integrated':False,'complete_Hamiltonian_proved':False,
         'nonauthor_review':False,'boundary_selected':False,'full_goal_achieved':False}
    print(json.dumps(out,indent=2,sort_keys=True));assert all(facts.values()),[k for k,v in facts.items() if not v]
    return out
if __name__=='__main__':run()
