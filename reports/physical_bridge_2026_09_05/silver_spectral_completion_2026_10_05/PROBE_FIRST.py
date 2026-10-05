"""Exact spectral-completion certificates; no nonlinear physical model claimed."""
import importlib.util
import json
from functools import lru_cache
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE=Path(__file__).resolve().parent
FIELD=s.QQ.algebraic_field(s.sqrt(2))
GEN='abt'


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod


def red(a):return a.applyfunc(s.expand)
def mul(a,b):return red(a*b)
def dm(a):return DomainMatrix.from_Matrix(a).convert_to(FIELD)
def rank(a):return 0 if not a.rows or not a.cols else dm(a).rank()
def inv(a):return dm(a).inv().to_Matrix()
def zero(a):return red(a)==s.zeros(a.rows,a.cols)


def kernel(a):
    if a.rows==0:return s.eye(a.cols)
    if a.cols==0:return s.zeros(0,0)
    r,piv=dm(a).rref();r=r.to_Matrix()
    free=[j for j in range(a.cols) if j not in piv]
    out=s.zeros(a.cols,len(free))
    for k,j in enumerate(free):
        out[j,k]=1
        for i,p in enumerate(piv):out[p,k]=-r[i,j]
    return red(out)


def columns(a):
    if not a.cols:return a
    piv=dm(a).rref()[1]
    return a[:,list(piv)]


class Complex:
    def __init__(self,rep,data):
        self.rep=rep;self.n=n=rep['a'].rows
        self.letters=dict(rep)
        self.letters.update({g.upper():inv(m) for g,m in rep.items()})
        for w in data['relators']:assert self.word(w)==s.eye(n),w
        self.P,self.Q=[self.word(w) for w in data['cusp_words']]
        assert zero(mul(self.P,self.Q)-mul(self.Q,self.P))
        self.B=s.Matrix.vstack(*(rep[g]-s.eye(n) for g in GEN))
        self.F=s.Matrix.vstack(*(self.fox(w) for w in data['relators']))
        self.R=s.Matrix.vstack(*(self.fox(w) for w in data['cusp_words']))
        self.D=s.Matrix.vstack(self.P-s.eye(n),self.Q-s.eye(n))
        self.G=(s.eye(n)-self.Q).row_join(self.P-s.eye(n))
        assert data['cusp_words']==['abAB','abt']
        self.R2=-mul(mul(self.Q,self.fox('abAB')[:,:2*n]),s.diag(inv(rep['t']),inv(rep['t'])))
        assert zero(mul(self.F,self.B)) and zero(mul(self.G,self.D))
        assert zero(mul(self.R,self.B)-self.D)
        assert zero(mul(self.R2,self.F)-mul(self.G,self.R))
        self.H=kernel(self.G.col_join(self.D.T))
        proj=mul(mul(self.H,inv(mul(self.H.T,self.H))),self.H.T)
        self.res=columns(mul(mul(proj,self.R),kernel(self.F)))
        self.L=kernel(self.G.col_join(self.D.T).col_join(self.res.T))
        self.flag=columns(self.L.row_join(self.res))
        assert self.flag.cols==self.H.cols
        self.H2=kernel(self.G.T)

    def word(self,w):
        a=s.eye(self.n)
        for c in w:a=mul(a,self.letters[c])
        return a

    def fox(self,w):
        a=s.eye(self.n);blocks=[s.zeros(self.n) for _ in GEN]
        for c in w:
            j=GEN.index(c.lower())
            if c.islower():blocks[j]=red(blocks[j]+a);a=mul(a,self.letters[c])
            else:a=mul(a,self.letters[c]);blocks[j]=red(blocks[j]-a)
        return s.Matrix.hstack(*blocks)


def cone(E,L,A0=None,A2=None):
    n=E.n
    A0=s.zeros(n,0) if A0 is None else A0
    A2=E.H2 if A2 is None else A2
    a0,a1,a2=A0.cols,L.cols,A2.cols
    dims=[n+a0,4*n+a1,4*n+a2,n]
    d0=s.zeros(dims[1],dims[0]);d1=s.zeros(dims[2],dims[1]);d2=s.zeros(n,dims[2])
    d0[:3*n,:n]=E.B;d0[3*n+a1:,:n]=s.eye(n);d0[3*n+a1:,n:]=-A0
    d1[:2*n,:3*n]=E.F;d1[2*n+a2:,:3*n]=E.R
    d1[2*n+a2:,3*n:3*n+a1]=-L;d1[2*n+a2:,3*n+a1:]=-E.D
    d2[:,:2*n]=E.R2;d2[:,2*n:2*n+a2]=-A2;d2[:,2*n+a2:]=-E.G
    assert zero(mul(E.D,A0)) and zero(mul(E.G,L))
    assert zero(mul(d1,d0)) and zero(mul(d2,d1))
    ranks=list(map(rank,(d0,d1,d2)))
    h=[dims[j]-([0]+ranks)[j]-(ranks+[0])[j] for j in range(4)]
    assert min(h)>=0
    return dict(H=h,J=h[1]+h[3]-h[0]-h[2],dimensions=dims,ranks=ranks)


def cup(E):
    n=E.n
    return s.zeros(n).row_join(inv(E.P).T).col_join((-inv(E.Q).T).row_join(s.zeros(n)))


def paired(E,D,L):
    J=cup(E)
    LD=mul(D.H,kernel(mul(mul(L.T,J),D.H)))
    a,b=cone(E,L),cone(D,LD)
    assert a['H']==b['H'][::-1]
    assert a['H'][0]==a['H'][3]==0
    assert a['J']==L.cols-(E.n-rank(E.D))==-b['J']
    return dict(E=a,dual=b,polarization=[L.cols,LD.cols])


def adjoint0(rep):
    basis=[];off=[(i,j) for i in range(5) for j in range(5) if i!=j]
    for i,j in off:
        z=s.zeros(5);z[i,j]=1;basis.append(z)
    for i in range(4):
        z=s.zeros(5);z[i,i]=1;z[4,4]=-1;basis.append(z)
    out={}
    for g,a in rep.items():
        ai=inv(a);cols=[]
        for z in basis:
            v=mul(mul(a,z),ai)
            assert s.trace(v)==0
            cols.append(s.Matrix([v[i,j] for i,j in off]+[v[i,i] for i in range(4)]))
        out[g]=s.Matrix.hstack(*cols)
    return out


@lru_cache(None)
def charged():
    old=load('spectral_old_native',HERE.parent/'silver_operator_gate_2026_10_05/probe.py')
    data=json.loads((HERE.parent/'silver_operator_gate_2026_10_05/candidate.json').read_text())
    assert data['relators']==old.marked_relators()
    v=old.four(data)
    c=s.Matrix([s.Rational(a)+s.sqrt(2)*s.Rational(b) for a,b in data['cocycle_Qsqrt2_pairs']])
    checks={};rows={};neutral={}
    def ck(k,x):checks[k]=bool(x);assert checks[k],k
    for amp in (0,1):
        w=old.extension(v,amp*c)
        reps={'W':w,'F':{g:old.wedge(a) for g,a in w.items()}}
        sect={}
        for label,rep in reps.items():
            E,D=[Complex(r,data) for r in (rep,{g:inv(a).T for g,a in rep.items()})]
            key=str(amp)+label;J=cup(E)
            ck(key+'_cup_descent',zero(mul(mul(E.D.T,J),D.H)) and zero(mul(mul(E.H.T,J),D.D)))
            ck(key+'_perfect_cup',rank(mul(mul(E.H.T,J),D.H))==E.H.cols==D.H.cols)
            ck(key+'_restriction_isotropic',zero(mul(mul(E.res.T,J),D.res)))
            ck(key+'_determinant_one',all(s.simplify(a.det())==1 for a in rep.values()))
            spectra=[paired(E,D,E.flag[:,:ell]) for ell in range(E.H.cols+1)]
            natural=paired(E,D,E.L)
            ck(key+'_received_complement_recovered',spectra[E.L.cols]==natural)
            ck(key+'_wrong_R2_sign_detected',not zero(mul(-E.R2,E.F)-mul(E.G,E.R)))
            ck(key+'_all_indices_and_endpoints',all(r['E']['J']==ell-E.H2.cols and r['E']['H'][0]==r['E']['H'][3]==0 for ell,r in enumerate(spectra)))
            sect[label]=dict(boundary_H0=E.n-rank(E.D),boundary_H1=E.H.cols,
                complement=E.L.cols,restriction=E.res.cols,natural=natural,spectra=spectra)
        N=Complex(adjoint0(w),data)
        nk=cone(N,N.res)
        ck(str(amp)+'_neutral_selfdual_pairing',nk['H']==nk['H'][::-1] and nk['J']==0)
        neutral[str(amp)]=nk
        rows[str(amp)]=sect
    census=[]
    for ellw in range(5):
        for ellf in range(7):
            jw,jf=rows['1']['W']['spectra'][ellw]['E']['J'],rows['1']['F']['spectra'][ellf]['E']['J']
            census.append(dict(ellW=ellw,ellF=ellf,JW=jw,JF=jf,conditional_SU5_cubic=jw-jf))
    ck('all35_integer_dimensions',len(census)==35)
    ck('five_anomaly_free_pairs',[(r['ellW'],r['ellF']) for r in census if not r['conditional_SU5_cubic']]==[(i,i+1) for i in range(5)])
    ck('same_dimensions_split_index_control',all(rows['0'][k]['spectra'][ell]['E']['J']==rows['1'][k]['spectra'][ell]['E']['J'] for k in ('W','F') for ell in range(len(rows['1'][k]['spectra']))))
    ck('natural_nonsplit_preserved',rows['1']['W']['natural']['E']['H']==[0,2,2,0] and rows['1']['F']['natural']['E']['H']==[0,3,4,0])
    ck('natural_split_paired',all(rows['0'][k]['natural']['E']['J']==0 for k in ('W','F')))
    ck('three_not_in_this_anomaly_free_dimension_menu',all(abs(r['JW'])<3 for r in census if not r['conditional_SU5_cubic']))
    return dict(checks=checks,charged=rows,neutral_native_only=neutral,census=census)


def analytic_controls():
    smooth=load('spectral_old_smooth',HERE.parent/'silver_smooth_boundary_gate_2026_10_05/probe.py')
    qx,qy,gamma,j,parity=smooth.matrices();x,y=s.symbols('x y',real=True)
    e=s.eye(4);xi=s.Matrix([0,x,y,0]);xp=s.Matrix([0,-y,x,0])
    a=e[:,0].row_join(xi);b=xp.row_join(e[:,3]);z=s.zeros(4,2)
    full=a.row_join(z).col_join(z.row_join(b));q=x*qx+y*qy
    projector=s.Matrix([[x*x,x*y],[x*y,y*y]])/(x*x+y*y)
    tangent=s.Matrix([x,y]);checks={}
    checks['high_symbol_universal']=s.factor((a.H*q*a).det())==-(x*x+y*y)**2
    checks['high_maximal_green']=zero(full.H*gamma*full) and full.rank()==4
    checks['high_reality']=full.row_join(j*full.conjugate()).rank()==4
    checks['high_parity']=full.row_join(parity*full).rank()==4
    checks['exact_auxiliary_derivative_admitted']=s.simplify((s.eye(2)-projector)*tangent)==s.zeros(2,1)
    # Naive preimage retains closed1 and2 but omits scalar primitives.
    bad=xi.row_join(e[:,3])
    checks['primitive_omission_nonelliptic']=zero(bad.H*q*bad)
    qt=s.diag(q,-q);qn=s.I*gamma
    checks['untwisted_hodge_preserves_zero_equations']=zero(j*qt.conjugate()+qt*j) and zero(j*qn.conjugate()+qn*j)
    checks['hodge_exchanges_parity']=zero(j*parity+parity*j)
    # Nonlinear gauge sector: f dg is not closed although dg is exact.
    f,g=s.sin(x),s.sin(y)
    obstruction=s.diff(f,x)*s.diff(g,y)
    checks['nonlinear_gauge_control_detected']=obstruction==s.cos(x)*s.cos(y) and obstruction.subs({x:0,y:0})==1
    h=s.symbols('h0:4');weights=list(h)+[-sum(h)]
    tr5=sum(a**3 for a in weights)
    tr10=sum((weights[i]+weights[k])**3 for i in range(5) for k in range(i+1,5))
    checks['SU5_cubic_full_roster']=s.expand(tr10-tr5)==0 and s.expand(tr5)!=0
    checks['SU5_adjoint_real_anomaly_zero']=s.expand(sum((a-b)**3 for a in weights for b in weights))==0
    checks['bulk_interaction_not_deleted']=smooth.bulk_cubic()==1
    return dict(checks=checks,principal_determinant=str(s.factor((a.H*q*a).det())),
                nonlinear_obstruction=str(obstruction),gauge_endpoint_H_per_coefficient=[1,0,0,1])


@lru_cache(None)
def run():
    a,b=charged(),analytic_controls();checks=dict(a.pop('checks'));checks.update(b.pop('checks'))
    failed=[k for k,v in checks.items() if not v]
    return dict(checks=checks,passed=len(checks)-len(failed),failed=failed,**a,analytic=b,
        nonlinear_physical_domain_closed=False,genesis_polarization_selected=False,
        numerical_PDE_kernel_solved=False,physical_goal_achieved=False,non_author_acceptance=False)


if __name__=='__main__':
    data=run();print(json.dumps(data,sort_keys=True));raise SystemExit(bool(data['failed']))
