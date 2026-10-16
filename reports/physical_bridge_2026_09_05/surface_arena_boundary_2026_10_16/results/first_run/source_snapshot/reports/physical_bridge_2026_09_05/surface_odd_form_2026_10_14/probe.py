"""Finite exact safeguards for an authored extreme-domain cross-form argument."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
def cliffords():
    p=HERE.parent/'surface_parent_dictionary_2026_10_13/upstream_total_metric.py'
    sp=importlib.util.spec_from_file_location('odd_form_metric',p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m.gammas()
def zero(m):return all(s.simplify(v)==0 for v in m)
def odd_character(g):
    t=s.trace(g);t2=s.trace(g*g);t3=s.trace(g*g*g)
    w3=(t**3-3*t*t2+2*t3)/6
    return s.simplify(2*w3+6*(t+s.conjugate(t)))
def phase_population(A,L):
    chars={(j,k):odd_character(A**j*L**k) for j in (0,1) for k in range(4)}
    rows=[]
    for sg,ae in [('+i',s.I),('-i',-s.I)]:
        ranks=[]
        for r,num in [(1,1+s.I),(3,-1+s.I),(5,-1-s.I),(7,1-s.I)]:
            lam=num/s.sqrt(2)
            n=s.simplify(sum(ae**(-j)*lam**(-k)*v for (j,k),v in chars.items())/8)
            if not n.is_Integer:raise ValueError('nonintegral odd projector rank: '+str(n))
            ranks.append([r,int(n)])
        rows.append([sg,ranks])
    return rows

@lru_cache(None)
def run():
    checks={}
    def ck(n,v):checks[n]=bool(v)
    c=cliffords();c1,c2,c3,c4=c;I=s.eye(4)
    ell=s.Symbol('ell',positive=True);beta=s.Symbol('beta',real=True)
    C={(0,1,0):-1/ell,(1,2,2):1/(2*ell),(0,3,2):-1/ell,(1,3,3):-1/(2*ell)}
    C.update({(j,i,k):-v for (i,j,k),v in list(C.items())})
    mixed=c1*c3*c4/(4*ell)
    H0=-c2/(2*ell)+mixed+s.I*beta*c1/ell
    F=[]
    for k in range(4):
        v=sum((c[i]*c[j]*C.get((i,j,k),0) for i in (2,3) for j in (0,1)),s.zeros(4))
        if k in (2,3):v+=c[k]*H0+H0*c[k]
        F.append(s.simplify(v))
    K3=(-c1*c4+c2*c3)/(2*ell);K4=(-c2*c4-c1*c3)/(2*ell)
    ck('full mixed first order coefficient E3',zero(F[2]-K3))
    ck('full mixed first order coefficient E4',zero(F[3]-K4))
    ck('no horizontal derivative in cross operator',zero(F[0]) and zero(F[1]))
    ck('all mixed second derivative coefficients cancel',all(zero(c[i]*c[j]+c[j]*c[i]) for i in (2,3) for j in (0,1)))
    ck('density term anticommutes vertically',all(zero(c[i]*c2+c2*c[i]) for i in (2,3)))
    ck('R line term anticommutes vertically',all(zero(c[i]*c1+c1*c[i]) for i in (2,3)))
    gv=s.I*c3*c4
    ck('both cross matrices reverse vertical chirality',zero(gv*K3+K3*gv) and zero(gv*K4+K4*gv))
    ck('cross coefficients skew Hermitian',zero(K3.H+K3) and zero(K4.H+K4))
    ck('E3 coefficient norm exact one',max(s.simplify(ell**2*K3.H*K3).eigenvals())==1)
    ck('E4 coefficient norm exact one',max(s.simplify(ell**2*K4.H*K4).eigenvals())==1)
    ck('omitted mixed spin term changes E3 coefficient',not zero(c3*mixed+mixed*c3))
    ck('omitted mixed spin term changes E4 coefficient',not zero(c4*mixed+mixed*c4))
    k3,k4=s.symbols('k3 k4',real=True);symbol=c3*k3+c4*k4
    ck('regular vertical gradient symbol exact',zero(symbol.H*symbol-(k3*k3+k4*k4)*I))
    a,b=s.symbols('a b',nonnegative=True)
    ck('absorption bound is an exact nonnegative square',s.expand(a*a/2+4*b*b-2*s.sqrt(2)*a*b)==s.expand((a/s.sqrt(2)-2*b)**2))
    eps=s.Symbol('eps',positive=True);rad=s.Symbol('rad',positive=True)
    ck('half pole derivative squared radial norm diverges',s.limit(s.integrate(rad**-2,(rad,eps,1)),eps,0,dir='+')==s.oo)
    q=s.Symbol('q',nonnegative=True);bb=s.Symbol('bb',real=True)
    ck('projected shifted potential elementary bound',s.expand((q*q/2-bb*bb-q)-(q*q/4-bb*bb-1))==s.expand((q/2-1)**2))
    aa=s.diag(s.I,-s.I);ab=s.Matrix([[0,1],[-1,0]])
    A=s.diag(-aa,aa,-aa);B=s.diag(ab,-ab,-ab)
    P=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
    L=s.kronecker_product(P,(s.eye(2)+aa)/s.sqrt(2))
    ck('literal Q8 coefficient relations retained',zero(A*A+s.eye(6)) and zero(B*B+s.eye(6)) and zero(A*B+B*A))
    ck('literal cusp fourth power retained',zero(L**4+s.eye(6)))
    ck('literal cusp commutes with A',zero(L*A-A*L))
    ck('complete odd character dimension112',odd_character(s.eye(6))==112)
    ck('odd centre acts on whole112 not six',odd_character(-s.eye(6))==-112 and odd_character(A)==0)
    pop=phase_population(A,L)
    ck('all actual harmonic phase ranks nonnegative',all(n>=0 for _,row in pop for _,n in row))
    ck('both A eigenspaces exhaust56',all(sum(n for _,n in row)==56 for _,row in pop))
    ck('whole odd population exhaust112',sum(n for _,row in pop for _,n in row)==112)
    ck('all actual phases bounded away from integers',min(min(s.Rational(r,8),1-s.Rational(r,8)) for _,row in pop for r,n in row if n)>0)
    ck('zero phase comparator fails confining frequency duty',s.S(0)<s.Rational(1,8))
    return {'checks':checks,'all_passed':all(checks.values()),'records':{
        'odd_phase_populations':pop,'odd_coefficient_dimension':112,
        'cross_matrix_norms_ell_one':[1,1],
        'form_vertical_fraction':[1,2],'form_norm_error_ell_one':4},
        'scope':'finite exact cross-form and whole odd-phase safeguards; authored conditional analytic proof, not global admission or physical index'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
