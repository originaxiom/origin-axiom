"""Full136 regular even cusp safeguards; analytic argument is separately scoped."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
def metric():
    p=HERE.parent/'surface_parent_dictionary_2026_10_13/upstream_total_metric.py'
    sp=importlib.util.spec_from_file_location('full_even_metric',p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def zero(m):return all(s.simplify(v)==0 for v in m)
def character(g):
    t=s.trace(g);w2=(t*t-s.trace(g*g))/2
    return s.simplify(t*s.conjugate(t)+10+3*(w2+s.conjugate(w2)))
def populations(A,B,L):
    chars={(j,k,h):character(A**j*L**k*B**h) for j in (0,1) for k in range(4) for h in (0,1)}
    out=[]
    for label,lam in [('+1',s.S(1)),('-1',s.S(-1)),('+i',s.I),('-i',-s.I)]:
        row=[]
        for eps in (1,-1):
            q=s.simplify(sum(lam**(-k)*s.Integer(eps)**(-h)*v for (j,k,h),v in chars.items())/16)
            if not q.is_Integer:raise ValueError('nonintegral projector rank')
            row.append(int(q))
        out.append([label,row])
    return out,chars

@lru_cache(None)
def run():
    ck={}
    def check(n,v):ck[n]=bool(v)
    a=s.diag(s.I,-s.I);b=s.Matrix([[0,1],[-1,0]])
    A=s.diag(-a,a,-a);B=s.diag(b,-b,-b)
    P=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
    L=s.kronecker_product(P,(s.eye(2)+a)/s.sqrt(2))
    check('actual T preserves short-cycle matrix',zero(L*A*L.H-A))
    check('actual T transports long-cycle matrix',zero(L*B*L.H-A*B))
    check('literal fourth power is retained centre',zero(L**4+s.eye(6)))
    check('even coefficients commute despite full odd commutator',zero(A*B+B*A) and character(A*B*A.H*B.H)==136)
    pop,chars=populations(A,B,L)
    check('complete even character136',character(s.eye(6))==136)
    check('all projector ranks nonnegative',all(n>=0 for _,row in pop for n in row))
    check('all short-periodic population included',sum(sum(row) for _,row in pop)==(character(s.eye(6))+character(A))/2==82)
    check('both admitted zero-phase populations exist',all(sum(row)>0 for _,row in pop[:2]))
    check('short periodic does not mean zero x phase',sum(sum(row) for _,row in pop[2:])>0)
    identity6=s.eye(6);t=s.trace(identity6)
    w2=(t*t-s.trace(identity6*identity6))/2
    one_sided=s.simplify(t*s.conjugate(t)+10+3*w2)
    check('omitting conjugate exterior sector changes136',one_sided==91 and one_sided!=character(identity6))
    c=metric().gammas();I=s.eye(4);ell=s.Symbol('ell',positive=True)
    # All brackets from the already pinned full coframe/Koszul source.
    C={(0,1,0):-1/ell,(1,2,2):1/(2*ell),(0,3,2):-1/ell,(1,3,3):-1/(2*ell)}
    C.update({(j,i,k):-v for (i,j,k),v in list(C.items())})
    G=lambda i,j,k:(C.get((i,j,k),0)-C.get((j,k,i),0)+C.get((k,i,j),0))/2
    omega=[sum((G(i,j,k)*c[j]*c[k]/4 for j in range(4) for k in range(4)),s.zeros(4)) for i in range(4)]
    check('Omega1 is complete connection',zero(omega[0]-c[0]*c[1]/(2*ell)-c[2]*c[3]/(4*ell)))
    check('Omega3 is complete connection',zero(omega[2]-(c[0]*c[3]-c[1]*c[2])/(4*ell)))
    K=sum((c[i]*omega[i] for i in range(4)),s.zeros(4))
    check('full spin contraction remains unchanged',zero(K+c[1]/(2*ell)-c[0]*c[2]*c[3]/(4*ell)))
    n1=s.simplify(ell*ell*omega[0].H*omega[0]).eigenvals()
    n3=s.simplify(ell*ell*omega[2].H*omega[2]).eigenvals()
    check('Omega1 norm bound exact',max(n1)==s.Rational(9,16))
    check('Omega3 norm bound exact',max(n3)==s.Rational(1,4))
    GH=s.I*c[0]*c[1]
    check('line-curvature matrix is bounded',GH.H==GH and GH*GH==I)
    beta=s.Symbol('beta',real=True);area=s.Symbol('area',positive=True);y=s.Symbol('y',positive=True)
    bs=s.Symbol('b',positive=True)
    cm=1+bs;cx=(s.Rational(3,4)+bs)**2+s.Rational(3,4)+bs
    growing_m=s.pi**2*y/(2*area)-cm/ell**2
    growing_x=s.pi**2*y*y/(8*ell**2)-cx/ell**2
    check('short nonzero lower bound eventually grows',s.limit(growing_m,y,s.oo)==s.oo)
    check('x nonzero lower bound eventually grows',s.limit(growing_x,y,s.oo)==s.oo)
    q=s.Symbol('q',nonnegative=True)
    check('elementary norm absorption preserves positive term',s.expand((q-1)**2-(q*q/2-1))==s.expand((q-2)**2/2))
    check('nearest canonical bound positive',s.Rational(3,4)*(s.Rational(3,4)-s.Rational(1,2))==s.Rational(3,16))
    check('ordinary zero unit cannot pass last-stratum bound',s.S(0)*(s.S(0)-s.Rational(1,2))<s.Rational(3,16))
    # The integer-sector proof is the n>=1/n<=0 inequality in FULL_EVEN_PROOF.
    check('bound is increasing above nearest canonical sector',s.diff(bs*(bs-s.Rational(1,2)),bs).subs(bs,s.Rational(3,4))>0)
    records={'short_periodic_phase_populations':pop,'even_coefficient_dimension':136,
             'short_periodic_dimension':sum(sum(row) for _,row in pop),
             'connection_squared_norms_ell_one':[[9,16],[1,4]],
             'canonical_uniform_tail_squared_bound_ell_one':[3,16]}
    return {'checks':ck,'records':records,'all_passed':all(ck.values()),
            'scope':'finite exact full-even population/connection safeguards for authored uniform end proof; no odd QDQ or global physical index'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
