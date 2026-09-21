"""F11 post-failure exact quadratic-field checks; original producer unchanged."""
from pathlib import Path
import importlib.util
from functools import lru_cache
from itertools import combinations
import sympy as s

spec=importlib.util.spec_from_file_location('f11_exception_original',Path(__file__).with_name('verify.py'))
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
q=v.q


def modulus(phase):
    if phase==-1:
        return q*q-34*q+1
    if phase in (s.I,-s.I):
        return q*q-14*q+1
    raise ValueError('Only nontrivial central characters have these loci')


def reduce_scalar(a,p):
    num,den=s.fraction(s.cancel(a))
    inv=s.invert(den,p,q,extension=s.I)
    return s.rem(s.expand(num*inv),p,q,extension=s.I)


def reduce_matrix(a,p):
    return a.applyfunc(lambda x: reduce_scalar(x,p))


def rref(a,p):
    a=reduce_matrix(a,p)
    row=0
    pivots=[]
    for col in range(a.cols):
        pivot=next((i for i in range(row,a.rows) if a[i,col]!=0),None)
        if pivot is None:
            continue
        a.row_swap(row,pivot)
        inv=reduce_scalar(1/a[row,col],p)
        a[row,:]=reduce_matrix(inv*a[row,:],p)
        for i in range(a.rows):
            if i!=row and a[i,col]!=0:
                a[i,:]=reduce_matrix(a[i,:]-a[i,col]*a[row,:],p)
        pivots.append(col)
        row+=1
        if row==a.rows:
            break
    return a,tuple(pivots)


def rank(a,p):
    return len(rref(a,p)[1])


def kernel(a,p):
    rr,pivots=rref(a,p)
    free=[i for i in range(a.cols) if i not in pivots]
    out=s.zeros(a.cols,len(free))
    for j,col in enumerate(free):
        out[col,j]=1
        for row,pivot in enumerate(pivots):
            out[pivot,j]=-rr[row,col]
    return out


def minor_rank_three_witness(a,p):
    for rows in combinations(range(a.rows),3):
        for cols in combinations(range(a.cols),3):
            det=s.cancel(a.extract(rows,cols).det())
            num,_=s.fraction(det)
            real,imag=s.expand_complex(num).as_real_imag()
            g=s.gcd(s.Poly(p,q),s.Poly(s.expand(real),q))
            g=s.gcd(g,s.Poly(s.expand(imag),q))
            if g.degree()==0:
                return rows,cols,s.factor(det)
    raise ArithmeticError('No uniform rank-three witness found')


@lru_cache(None)
def certificate(phase,dual=False):
    p=modulus(phase)
    b,j=v.complex_matrices(q,phase,dual)
    rb,rj=rank(b,p),rank(j,p)
    null=kernel(j,p)
    witness=None
    for i in range(null.cols):
        if rank(b.row_join(null[:,i]),p)>rb:
            witness=null[:,i]
            break
    if witness is None:
        raise ArithmeticError('No nontrivial H1 witness')
    rows,cols,det=minor_rank_three_witness(j,p)
    return {'B_rank':rb,'J_rank':rj,'H1':8-rb-rj,'cocycle':witness,
            'minor_rows':rows,'minor_cols':cols,'minor':det,
            'cocycle_closed':reduce_matrix(j*witness,p)==s.zeros(4,1),
            'not_boundary':rank(b.row_join(witness),p)==rb+1}


if __name__=='__main__':
    for phase in (-s.Integer(1),s.I,-s.I):
        for dual in (False,True):
            print('phase',phase,'dual',dual,certificate(phase,dual),flush=True)
