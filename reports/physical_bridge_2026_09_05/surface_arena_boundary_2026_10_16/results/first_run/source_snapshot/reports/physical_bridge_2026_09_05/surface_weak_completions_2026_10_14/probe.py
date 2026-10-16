"""Exact full-character census of all commuting corrections; no physical index."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent
def helper():
    p=HERE.parent/'surface_based_gauge_2026_10_14/probe.py'
    sp=importlib.util.spec_from_file_location('weak_class_based',p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m

@lru_cache(None)
def run():
    p=helper();checks={}
    def ck(n,v):checks[n]=bool(v)
    old=p.run();ck('prior complete based relation controls',old['all_passed'])
    a=s.diag(s.I,-s.I);A=s.diag(-a,a,-a)
    P=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
    L=s.kronecker_product(P,(s.eye(2)+a)/s.sqrt(2))
    x,y,z=s.symbols('x y z',nonzero=True)
    ck('commuting braid equations force equal factors',s.factor(x*x*y-y*y*x)==x*y*(x-y) and s.factor(y*y*z-z*z*y)==y*z*(y-z))
    labels=list(range(1,24,2));reps=sorted({min(m,24-m) for m in labels})
    ck('twelve angle solutions and six inverse classes',len(labels)==12 and len(reps)==6)
    ck('all centre conditions exact',all(p.clean(s.exp(-s.I*s.pi*m))==-1 for m in labels))
    ck('even label rejecting centre',p.clean(s.exp(-s.I*s.pi*2))!=-1)
    ck('central weak factor cannot repair',12*s.Rational(1,2)%1!=s.Rational(1,2))
    traces={}
    for j in (0,1):
        for k in range(12):
            g=A**j*L**k;t=p.clean(s.trace(g));t2=p.clean(s.trace(g*g));t3=p.clean(s.trace(g*g*g))
            traces[j,k]=(t,p.clean((t*t-t2)/2),p.clean((t**3-3*t*t2+2*t3)/6))
    rows=[]
    for m in reps:
        census=[]
        for odd,phases in [(False,[('+1',s.Integer(1)),('-1',s.Integer(-1))]),(True,[('+i',s.I),('-i',-s.I)])]:
            out=[]
            for name,av in phases:
                row=[]
                for r in range(12):
                    total=0
                    for (j,k),(t,w2,w3) in traces.items():
                        char=(w3+3*(t+s.conjugate(t)))*2*s.cos(s.pi*m*k/12) if odd else t*s.conjugate(t)+8+2*s.cos(s.pi*m*k/6)+3*(w2+s.conjugate(w2))
                        total+=char*av**(-j)*s.exp(-s.I*s.pi*r*k/6)
                    value=p.clean(total/24)
                    ck('integral phase '+str((m,odd,name,r)),value.is_Integer and value>=0)
                    row.append([r,int(value)])
                out.append([name,row])
            census.append(out)
        even,odd=census
        ck('all248 retained '+str(m),sum(n for out in census for _,row in out for _,n in row)==248 and sum(n for _,row in odd for _,n in row)==112)
        ck('weak roots noncentral '+str(m),p.clean(s.exp(-s.I*s.pi*m/6))!=1)
        ck('inverse class same characters '+str(m),all(p.clean(s.cos(s.pi*(24-m)*k/12)-s.cos(s.pi*m*k/12))==0 for k in range(12)))
        zeros=[row[0][1] for _,row in odd]
        rows.append({'m':m,'even':even,'odd':odd,'odd_zero_phase_ranks':zeros,
                     'full_parallel_gauge_dimension':old['records']['complete_based_gauge_invariant_dimension'],
                     'diagonal_Y_invariants':old['records']['diagonal_block_hypercharge_invariants']})
    xi,beta=s.symbols('xi beta',real=True)
    c1=s.I*s.Matrix([[0,1],[1,0]]);c2=s.I*s.Matrix([[0,-s.I],[s.I,0]])
    D=s.I*xi*c2+s.I*beta*c1
    ck('full zero-phase Fourier square',p.zero(D*D-(xi*xi+beta*beta)*s.eye(2)))
    for gamma in (-1,1):
        for N in range(-3,4):ck('integer beta control '+str((gamma,N)),abs(s.Rational(gamma,4)+s.Rational(3,4)-6*N)>=s.Rational(1,2))
    ck('noninteger unit comparator can erase projected mass',s.Rational(1,4)+s.Rational(3,4)-6*s.Rational(1,6)==0)
    return {'checks':checks,'records':{'angle_labels':labels,'inverse_representatives':reps,
        'classes':rows,'canonical_zero_phase_beta_squared_floor':'1/4',
        'canonical_even_tail_squared_floor':'3/16'},'all_passed':all(checks.values()),
        'scope':'complete stated commuting weak family and conditional projected spectral distinction, not physics admission'}
if __name__=='__main__':
    o=run();print(json.dumps(o,indent=2));raise SystemExit(0 if o['all_passed'] else 1)
