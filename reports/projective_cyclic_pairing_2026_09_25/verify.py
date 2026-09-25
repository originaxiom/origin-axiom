"""F18 finite certificates for the authored all-degree cyclic-pairing proof."""
from functools import lru_cache
from itertools import product
from pathlib import Path
import importlib.util
import json
import sympy as s

path=Path(__file__).parent.parent/'projective_cover_characters_2026_09_25'/'verify.py'
spec=importlib.util.spec_from_file_location('f18_f17',path)
p=importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
v=p.v
BETA={'x':'y','y':'yXyy'}
BETA_INV={'x':'xxYx','y':'x'}
FIBER=('nM','mnMM')


def substitute(w,images):
    return p.reduce_word(''.join(images[c.lower()] if c.islower()
                                 else p.inverse(images[c.lower()]) for c in w))


@lru_cache(None)
def beta(w,power):
    images=BETA if power>=0 else BETA_INV
    for _ in range(abs(power)): w=substitute(w,images)
    return w


def fiber_exponents(w):
    return s.Matrix([w.count('x')-w.count('X'),w.count('y')-w.count('Y')])


B=s.Matrix.hstack(*(fiber_exponents(BETA[g]) for g in 'xy'))
A=B.T


def free_normal(w):
    """Exact free-fiber word followed by t^k; used only for bounded word controls."""
    letters={'m':('',1),'M':('',-1),'n':('x',1),'N':(beta('X',-1),-1)}
    u=''; k=0
    for g in w:
        vv,l=letters[g]
        u=p.reduce_word(u+beta(vv,k)); k+=l
    return u,k


@lru_cache(None)
def abelian_normal(w):
    """Independent integer semidirect multiplication, no free-word expansion."""
    letters={'m':(s.zeros(2,1),1),'M':(s.zeros(2,1),-1),
             'n':(s.Matrix([1,0]),1),'N':(-B.inv()*s.Matrix([1,0]),-1)}
    u=s.zeros(2,1); k=0
    for g in w:
        vv,l=letters[g]
        u=u+B**k*vv; k+=l
    return u,k


def fiber_action(name,j=0):
    rows=[]
    for w in FIBER:
        fw,k=free_normal('m'*j+p.subst(w,name)+'M'*j)
        if k: raise ValueError('not a fiber map')
        rows.append(list(fiber_exponents(fw)))
    return s.Matrix(rows)


C=fiber_action('theta')


def mod(a,m=4):
    return a.applyfunc(lambda x:int(x)%m)


def fiber_characters(degree,modulus=4):
    if degree<1: raise ValueError('degree must be positive')
    return tuple(a for a in product(range(modulus),repeat=2)
                 if mod((A**degree-s.eye(2))*s.Matrix(a),modulus)==s.zeros(2,1))


def witnesses(a,modulus=4,maxdeck=3):
    aa=s.Matrix(a); out=[]
    for name,sign in (('theta',1),('thetaT',-1)):
        for j in range(maxdeck):
            if mod((sign*C*A**j+s.eye(2))*aa,modulus)==s.zeros(2,1):
                out.append((name,j))
    return tuple(out)


def evaluate_character(degree,c,a,w,modulus=4):
    u,k=abelian_normal(w)
    if k%degree: raise ValueError('word outside the cover')
    if mod((A**degree-s.eye(2))*s.Matrix(a),modulus)!=s.zeros(2,1):
        raise ValueError('fiber assignment does not descend')
    return int((s.Matrix(a).T*u)[0]+c*(k//degree))%modulus


def cover_generators(degree):
    return FIBER+('m'*degree,)


def choose(degree,a):
    if degree%3:
        if tuple(a)!=(0,0): raise ValueError('nontrivial forbidden fiber character')
        return 'theta',0
    found=witnesses(a)
    if not found: raise ValueError('no listed witness')
    return found[0]


@lru_cache(None)
def actual_untwisted(middle,degree,name,j,embedding=1):
    k,q,rho,_=v.context(middle,embedding)
    jj=p.base_intertwiner(middle,name,embedding)[0]
    for _ in range(j): jj=jj*rho[0].inv()
    words=cover_generators(degree)
    images=tuple('m'*j+p.subst(w,name)+'M'*j for w in words)
    forward=tuple(p.word(w,rho) for w in words)
    target=tuple(g.inv().transpose() for g in forward)
    source=tuple(p.word(w,rho) for w in images)
    return jj,words,images,target,source


def actual_residuals(middle,degree,c,a,embedding=1):
    name,j=choose(degree,a)
    jj,words,images,target,source=actual_untwisted(middle,degree,name,j,embedding)
    k=jj.domain; out=[]
    for w,ww,t,b in zip(words,images,target,source):
        chi=evaluate_character(degree,c,a,w)
        image_chi=evaluate_character(degree,c,a,ww)
        out.append(t.scalarmul(k.from_sympy(s.I**(-chi)))*jj
                   -jj*b.scalarmul(k.from_sympy(s.I**image_chi)))
    return tuple(out)


def universal_unipotent_polynomial():
    d=s.symbols('d',nonzero=True); x=s.symbols('x')
    power=1+d*x+d*(d-1)*x*x/2+d*(d-1)*(d-2)*x**3/6
    z=power-1
    recovery=1+z/d+(1-d)*z*z/(2*d*d)+(1-d)*(1-2*d)*z**3/(6*d**3)
    residual=s.Poly(s.rem(s.expand(recovery-1-x),x**4,x),x,domain=s.QQ.frac_field(d))
    return d,x,power,recovery,residual


def report():
    d,x,power,recovery,res=universal_unipotent_polynomial()
    torsion=[]
    for a in product(range(4),repeat=2):
        torsion.append(dict(fiber_character=a,degree_three_marking=(0,a[0],a[1],(-a[0]+3*a[1])%4),
                            linear_inversion_witnesses=witnesses(a)))
    return dict(A=A.tolist(),B=B.tolist(),C=C.tolist(),thetaT=fiber_action('thetaT').tolist(),
                A3_mod4=mod(A**3).tolist(),sum_mod4=mod(s.eye(2)+A+A**2).tolist(),
                determinants=[int((A-s.eye(2)).det()),int((A**2-s.eye(2)).det())],
                degree_controls=[dict(degree=n,characters=4*len(fiber_characters(n))) for n in range(1,13)],
                torsion=torsion,unipotent_recovery=str(recovery),unipotent_residual=str(res.as_expr()),
                order19_control=dict(degree=9,character=(1,6),invariant=mod((A**9-s.eye(2))*s.Matrix([1,6]),19)==s.zeros(2,1),
                                     listed_inversion_witnesses=witnesses((1,6),19,9)),
                note='Finite certificates plus PROOF.md, not a finite-degree inference or an H1 census.')


if __name__=='__main__':
    print(json.dumps(report(),default=str,sort_keys=True),flush=True)
