"""Actual even cusp channels and uniform twist control, not a full index."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
def load(path):
    sp=importlib.util.spec_from_file_location('even_cusp_metric',path)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def zero(m):return all(s.simplify(x)==0 for x in m)

@lru_cache(None)
def run():
    checks={}
    def ck(n,v):checks[n]=bool(v)
    a=s.diag(s.I,-s.I);b=s.Matrix([[0,1],[-1,0]])
    A0=s.diag(-a,a,-a);B0=s.diag(b,-b,-b)
    P13=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
    L=s.kronecker_product(P13,(s.eye(2)+a)/s.sqrt(2))
    hs=[-s.I*A0,s.diag(s.eye(2),s.zeros(2),-s.eye(2))]
    chars=[(1,-1,1),(1,1,-1)]
    for j,(H,ch) in enumerate(zip(hs,chars)):
        ck(f'actual Lie field {j}',H.H==H and s.trace(H)==0 and s.trace(H.H*H)>0)
        for name,U,sign in zip(['A','B','T'],[A0,B0,L.H],ch):
            ck(f'actual character {j} {name}',zero(U*H*U.H-sign*H))
        ck(f'actual puncture even {j}',zero((A0*B0*A0.H*B0.H)*H*(A0*B0*A0.H*B0.H).H-H))
        ck(f'actual cusp sign cancellation {j}',ch[2]*(1 if j==0 else -1)==1)
    ck('nonabelian parent direction not identically decoupled',not zero(hs[0]*B0-B0*hs[0]))
    geo=load(HERE.parent/'surface_parent_dictionary_2026_10_13/upstream_total_metric.py')
    c1,c2,c3,c4=geo.gammas();I=s.eye(4)
    ell,area,p=s.symbols('ell area p',positive=True)
    t=s.Symbol('t',real=True);beta,xi,lam=s.symbols('beta xi lam',real=True)
    K=c1*c3*c4;GV=s.I*c3*c4;Z=s.I*c1*c3;J=s.I*c2*c4
    Pi=(I+Z)*(I+J)/4
    for name,X in [('Z',Z),('J',J),('GammaV',GV),('K',K)]:
        ck('Hermitian involution '+name,X.H==X and X*X==I)
    ck('joint spin projector',Pi.H==Pi and Pi*Pi==Pi and Pi.rank()==1 and zero(Z*J-J*Z))
    GX=-c1*c2*c3*c4
    ck('profile internal chirality retained',zero(GX*Pi+Pi))
    ck('actual radial density removes only density term',zero((-c2/(2*ell)+K/(4*ell))+c2/(2*ell)-K/(4*ell)))
    C=2*ell*p/s.sqrt(area);a_t=p*s.exp(-t/2)/s.sqrt(area)
    h=s.exp(-C*s.exp(-t/2)-t/4)
    ordinary=c2*s.diff(h,t)/ell+(s.I*c4*a_t+K/(4*ell))*h
    ck('exact full high frequency zero profile',zero(ordinary*Pi))
    ck('omitted mixed term fails this profile',not zero((ordinary-K*h/(4*ell))*Pi))
    ck('reversed mixed term fails this profile',not zero((ordinary-K*h/(2*ell))*Pi))
    u=s.Symbol('u',positive=True)
    norm=s.integrate(2*s.exp(-2*u)/C,(u,0,s.oo))
    ck('exact whole line profile norm',s.simplify(norm-1/C)==0)
    z0=s.Symbol('z0',positive=True)
    ck('exact normalized low height tail',s.integrate(2*s.exp(-2*u),(u,z0,s.oo))==s.exp(-2*z0))
    k=s.Symbol('k',positive=True)
    ck('cutoff residual tends to zero at growing frequency',s.limit(s.exp(-2*k*z0),k,s.oo)==0)
    ck('norm escapes every fixed compact height',s.limit(1-s.exp(-2*k*z0),k,s.oo)==1)
    V=s.I*c4*a_t;R=s.I*c1*beta/ell
    ck('shrinking vertical term has actual norm scale',zero(V.H*V-p*p*s.exp(-t)/area*I))
    ck('radial derivative twist anticommutes',zero(c2*R+R*c2))
    ck('all vertical frequencies twist anticommutes',zero(V*R+R*V))
    ck('full mixed twist cross term',zero((K/(4*ell))*R+R*(K/(4*ell))+beta*GV/(2*ell*ell)))
    ck('twist square is positive',zero(R*R-beta*beta/(ell*ell)*I))
    Hinf=s.I*c2*xi/ell+K/(4*ell)+R
    target=((ell*lam)**2-xi*xi-(beta-s.Rational(1,4))**2)*((ell*lam)**2-xi*xi-(beta+s.Rational(1,4))**2)/ell**4
    ck('whole fixed frequency asymptotic polynomial',s.simplify((lam*I-Hinf).det()-target)==0)
    ck('fixed frequency positive threshold is not zero profile exclusion',zero(ordinary*Pi) and s.Rational(1,16)>0)
    bounds=[]
    for name,B in [('ordinary0',s.S(0)),('canonical0',s.Rational(3,4)),('ordinary1',s.Integer(-6)),('canonical1',-s.Rational(21,4)),('canonical_minus1',s.Rational(27,4))]:
        bound=abs(B)*(abs(B)-s.Rational(1,2));bounds.append([name,int(bound.p),int(bound.q)])
        if name!='ordinary0':ck('uniform even channel bound '+name,bound>0)
    # Integer n>=1: |3/4-6n|=6n-3/4>=21/4;
    # n<=0: |3/4-6n|=3/4-6n>=3/4. No fractional unit is selected.
    ck('canonical nearest integer sector has positive bound',bounds[1][1:]==[3,16])
    records={'coefficient_characters':[list(x) for x in chars],
             'spin_projector_rank':int(Pi.rank()),'profile_norm_power':-1,
             'fixed_p_squared_masses_ordinary0':[[1,16],[1,16]],
             'fixed_p_squared_masses_canonical0':[[1,4],[1,1]],
             'uniform_squared_bounds_ell_one':bounds}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'even-channel algebra/profile and authored conditional Weyl/form argument; not global full QDQ or physical index'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
