"""F11 exact cusp homotopy and coefficient cohomology; no global PDE solve."""
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import importlib.util
import sympy as s

path = Path(__file__).parent.parent/'projective_escape_2026_09_21'/'verify.py'
spec = importlib.util.spec_from_file_location('f11_f10', path)
f10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f10)
q,z,L,beta,k = f10.q,f10.z,f10.length,f10.beta,f10.kappa
xi,omega = s.symbols('xi omega', real=True)
RELATOR = 'mnMNmNMnmN'
PHASES = (s.Integer(1),s.Integer(-1),s.I,-s.I)


def clean(m):
    return m.applyfunc(lambda a: s.factor(s.cancel(a)))


def wedge(i):
    out=s.zeros(8)
    for mask in range(8):
        if not mask & (1<<i):
            sign=(-1)**sum(bool(mask & (1<<j)) for j in range(i))
            out[mask | (1<<i),mask]=sign
    return out


def form_metric():
    return s.diag(*(z**(2*mask.bit_count())/L**(2*bool(mask & 2))
                    for mask in range(8)))


def connection(dual=False):
    c=f10.local_connection()
    return tuple(-a.T for a in c) if dual else c


def inverse_longitude(dual=False):
    _,p,d,_=f10.cusp_generators()
    u=z*z/4-beta*beta/L**2
    sign=1 if dual else -1
    diagonal=s.I*omega*s.eye(4)+sign*k*d
    nilpotent=sign*beta*(p.T if dual else p)/u
    inv=diagonal.inv()
    return clean(inv-inv*nilpotent*inv)


def differential_parts(dual=False):
    c=connection(dual)
    radial=s.kronecker_product(wedge(2),s.eye(4))
    zero_order=sum((s.kronecker_product(wedge(i),c[i]+s.I*a*s.eye(4))
                    for i,a in enumerate((xi,omega,0))),s.zeros(32))
    return zero_order,radial


def homotopy(dual=False):
    return s.kronecker_product(wedge(1).T,inverse_longitude(dual))


def cartan_residual(dual=False):
    a,b=differential_parts(dual)
    h=homotopy(dual)
    return s.simplify(a*h+h*a+b*h.diff(z)-s.eye(32)), s.simplify(b*h+h*b)


def word(w,rho):
    dim=next(iter(rho.values())).rows
    inverse={g:a.inv() for g,a in rho.items()}
    out=s.eye(dim)
    for c in w:
        out=clean(out*(rho[c] if c.islower() else inverse[c.lower()]))
    return out


def fox(w,rho):
    dim=next(iter(rho.values())).rows
    prefix=s.eye(dim)
    out={g:s.zeros(dim) for g in rho}
    inverse={g:a.inv() for g,a in rho.items()}
    for c in w:
        g=c.lower()
        if c.islower():
            out[g]+=prefix
            prefix=clean(prefix*rho[g])
        else:
            prefix=clean(prefix*inverse[g])
            out[g]-=prefix
    return clean(s.Matrix.hstack(*(out[g] for g in rho)))


def affine_cocycle(w,rho):
    dim=next(iter(rho.values())).rows
    out=s.zeros(dim,dim*len(rho))
    for col in range(out.cols):
        lifts={}
        for index,(g,a) in enumerate(rho.items()):
            lifted=s.eye(dim+1)
            lifted[:dim,:dim]=a
            if index==col//dim:
                lifted[col%dim,dim]=1
            lifts[g]=lifted
        out[:,col]=word(w,lifts)[:dim,dim]
    return clean(out)


def representation(parameter=q,phase=s.Integer(1),dual=False):
    m,n=f10.generators(s.sympify(parameter))
    rho={'m':phase*m,'n':phase*n}
    return {g:clean(a.inv().T) for g,a in rho.items()} if dual else rho


@lru_cache(None)
def complex_matrices(parameter=q,phase=s.Integer(1),dual=False):
    rho=representation(parameter,phase,dual)
    b=s.Matrix.vstack(*(a-s.eye(4) for a in rho.values()))
    return clean(b),fox(RELATOR,rho)


def strip_zero_root(poly):
    p=s.Poly(poly,q,domain=s.QQ)
    while p.degree()>0 and p.eval(0)==0:
        p=p.exquo(s.Poly(q,q))
    return p.monic()


def maximal_minor_certificate(matrix):
    size=min(matrix.shape)
    gcd=s.Poly(0,q,domain=s.QQ)
    nminors=0
    denominators_only_q=True
    for rows in combinations(range(matrix.rows),size):
        for cols in combinations(range(matrix.cols),size):
            minor=s.factor(matrix.extract(rows,cols).det())
            num,den=s.fraction(s.cancel(minor))
            # All q>0 parameters are real; split exact Gaussian coefficients.
            real,imag=s.expand_complex(num).as_real_imag()
            for value in (real,imag):
                gcd=s.gcd(gcd,s.Poly(s.expand(value),q,domain=s.QQ))
            denpoly=s.Poly(den,q,extension=s.I)
            denominators_only_q &= len(denpoly.terms())==1
            nminors+=1
    if gcd.is_zero:
        return {'gcd':s.Integer(0),'positive_roots':None,
                'minors':nminors,'q_only_denominators':denominators_only_q}
    normalized=strip_zero_root(gcd.as_expr())
    return {'gcd':s.factor(normalized.as_expr()),
            'positive_roots':normalized.count_roots(0,s.oo),
            'minors':nminors,'q_only_denominators':denominators_only_q}


@lru_cache(None)
def certificates(phase=s.Integer(1)):
    b,j=complex_matrices(q,phase)
    return maximal_minor_certificate(b),maximal_minor_certificate(j)


def dimensions(parameter,phase=s.Integer(1),dual=False):
    b,j=complex_matrices(s.sympify(parameter),phase,dual)
    return 4-b.rank(),8-b.rank()-j.rank()


if __name__=='__main__':
    for phase in PHASES:
        cb,cj=certificates(phase)
        print('phase',phase,'B',cb,'J',cj,flush=True)
        print('ordinary H0,H1 at q=1:',dimensions(s.Integer(1),phase),flush=True)
