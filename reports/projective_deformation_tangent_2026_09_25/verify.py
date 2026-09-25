"""F15 exact full adjoint tangent and first-order matter continuation only."""
from functools import lru_cache
from pathlib import Path
import importlib.util
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix as DM

path=Path(__file__).parent.parent/'projective_escape_2026_09_21'/'verify.py'
spec=importlib.util.spec_from_file_location('f15_f10',path)
f10=importlib.util.module_from_spec(spec)
spec.loader.exec_module(f10)
REL='mnMNmNMnmN'
POSITIONS=tuple((i,j) for i in range(4) for j in range(4) if i!=j)


def dm(a,k):
    return DM.from_Matrix(s.Matrix(a)).convert_to(k).to_dense()


def zero(n,m,k):
    return DM.zeros((n,m),k,fmt='dense')


def eye(n,k):
    return DM.eye(n,k).to_dense()


def col(a,i):
    return a.extract(range(a.shape[0]),[i])


def cat(*a):
    return a[0].hstack(*a[1:])


def stack(*a):
    return a[0].vstack(*a[1:])


def kernel(a):
    return a.nullspace(divide_last=True).transpose().to_dense()


def span(a):
    return a.extract(range(a.shape[0]),a.rref()[1])


def quotient(b,z):
    joined=cat(b,z)
    pivots=joined.rref()[1]
    return joined.extract(range(joined.shape[0]),[i for i in pivots if i>=b.shape[1]])


def basis(k):
    out=[]
    for i,j in POSITIONS:
        a=s.zeros(4); a[i,j]=1; out.append(dm(a,k))
    for i in range(3):
        a=s.zeros(4); a[i,i]=1; a[3,3]=-1; out.append(dm(a,k))
    return tuple(out)


def coords(a):
    rows=a.to_list(); k=a.domain
    if sum((rows[i][i] for i in range(4)),k.zero)!=0:
        raise ValueError('matrix is not tracefree')
    values=[rows[i][j] for i,j in POSITIONS]+[rows[i][i] for i in range(3)]
    return DM([[v] for v in values],(15,1),k)


def uncoords(v):
    k=v.domain
    return sum((a.scalarmul(v.to_list()[i][0]) for i,a in enumerate(basis(k))),zero(4,4,k))


def linear_map(action,k):
    return cat(*(coords(action(a)) for a in basis(k)))


def fox_jet(rho,drho=None):
    """Value and exact first derivative of the coefficient Fox matrix."""
    k=rho[0].domain; n=rho[0].shape[0]
    if drho is None: drho=(zero(n,n,k),zero(n,n,k))
    inv=tuple(a.inv() for a in rho)
    dinv=tuple(-b*d*b for b,d in zip(inv,drho))
    prefix,dp=eye(n,k),zero(n,n,k)
    out=[zero(n,n,k),zero(n,n,k)]; dout=[zero(n,n,k),zero(n,n,k)]
    for c in REL:
        i='mn'.index(c.lower())
        if c.islower():
            out[i]=out[i]+prefix; dout[i]=dout[i]+dp
            dp,prefix=dp*rho[i]+prefix*drho[i],prefix*rho[i]
        else:
            dp,prefix=dp*inv[i]+prefix*dinv[i],prefix*inv[i]
            out[i]=out[i]-prefix; dout[i]=dout[i]-dp
    return cat(*out),cat(*dout)


def word_jet(rho,drho,word=REL):
    """Independent product in matrices over K[epsilon]/epsilon^2."""
    k=rho[0].domain; n=rho[0].shape[0]
    jets={g:(a,d) for g,a,d in zip('mn',rho,drho)}
    for g,a,d in zip('MN',rho,drho):
        ai=a.inv(); jets[g]=(ai,-ai*d*ai)
    out,der=eye(n,k),zero(n,n,k)
    for c in word:
        a,d=jets[c]
        out,der=out*a,der*a+out*d
    return out,der


def intertwiner(q):
    a=q/4; b=q/(2*(q+1)); c=(q*q+1)/(2*(q+1))
    return s.Matrix([[a,-a,b,c],[-a,a,-b,b],[b,-b,1,-1],[c,b,-1,1]])


@lru_cache(None)
def context(middle,embedding=1):
    if middle not in (14,34) or embedding not in (-1,1): raise ValueError('unsupported point')
    d,c=(3,4) if middle==14 else (2,12)
    k=s.QQ.algebraic_field(s.sqrt(d),s.I)
    q=s.Rational(middle,2)+embedding*c*s.sqrt(d)
    rho=tuple(dm(a,k) for a in f10.generators(q))
    j=dm(intertwiner(q),k)
    return k,q,rho,j


def tangent_data(rho,j):
    k=j.domain; ji=j.inv(); n=15
    c=linear_map(lambda x:ji*x.transpose()*j,k)
    ad=tuple(linear_map(lambda x,a=a:a*x*a.inv(),k) for a in rho)
    b=stack(*(a-eye(n,k) for a in ad))
    rel,_=fox_jet(ad)
    t=stack(cat(ad[0]*c,zero(n,n,k)),cat(zero(n,n,k),ad[1]*c))
    zs={}; bs={}; hs={}
    for sign in (1,-1):
        zs[sign]=kernel(stack(rel,t-eye(30,k).scalarmul(k(sign))))
        bs[sign]=span(b*(eye(n,k)-c.scalarmul(k(sign))))
        hs[sign]=quotient(bs[sign],zs[sign])
    h=cat(hs[1],hs[-1])
    return dict(B=b,R=rel,T=t,C=c,Z=zs,Bs=bs,Hs=hs,H=h)


@lru_cache(None)
def actual(middle,embedding=1):
    k,q,rho,j=context(middle,embedding)
    a=tangent_data(rho,j)
    qsym=f10.q
    raw=f10.generators()
    derivatives=tuple(dm(g.diff(qsym).subs(qsym,q),k) for g in raw)
    qt=stack(*(coords(d*r.inv()) for d,r in zip(derivatives,rho)))
    a.update(K=k,q=q,rho=rho,J=j,qt=qt)
    return a


def direct_differential(rho):
    k=rho[0].domain; bs=basis(k); cols=[]
    for g in range(2):
        for x in bs:
            dr=[zero(4,4,k),zero(4,4,k)]; dr[g]=x*rho[g]
            _,d=word_jet(rho,dr)
            cols.append(coords(d))
    return cat(*cols)


def matter_complex(rho,phase,dual=False):
    k=rho[0].domain; phase=k.from_sympy(phase)
    twisted=tuple(a.scalarmul(phase) for a in rho)
    if dual: twisted=tuple(a.inv().transpose() for a in twisted)
    b=stack(*(a-eye(4,k) for a in twisted))
    r,_=fox_jet(twisted)
    h=quotient(b,kernel(r))
    left=kernel(r.transpose()).transpose()
    return dict(rho=twisted,B=b,R=r,H=h,left=left)


def matter_derivative(rho,phase,dual,tangent):
    k=rho[0].domain; ph=k.from_sympy(phase)
    u=[uncoords(tangent.extract(range(15*g,15*g+15),[0])) for g in range(2)]
    raw=tuple(a.scalarmul(ph) for a in rho)
    dr=tuple(x*a for x,a in zip(u,raw))
    if dual:
        inverses=tuple(a.inv().transpose() for a in raw)
        dr=tuple(-ai*d.transpose()*ai for ai,d in zip(inverses,dr))
        raw=inverses
    return fox_jet(raw,dr)[1]


def obstruction_row(rho,phase,dual,directions):
    k=rho[0].domain; m=matter_complex(rho,phase,dual)
    if m['H'].shape!=(8,1) or m['left'].shape!=(1,4):
        raise ArithmeticError('expected a single exceptional H1 and H2 class')
    pieces=[m['left']*matter_derivative(rho,phase,dual,col(directions,i))*m['H']
            for i in range(directions.shape[1])]
    return cat(*pieces) if pieces else zero(1,0,k)


@lru_cache(None)
def matter_data(middle,embedding=1):
    a=actual(middle,embedding); phase=s.I if middle==14 else -s.Integer(1)
    rows=tuple(obstruction_row(a['rho'],phase,d,a['H']) for d in (False,True))
    joint=stack(*rows); start=a['Hs'][1].shape[1]
    odd=joint.extract(range(2),range(start,joint.shape[1]))
    return dict(rows=rows,joint=joint,odd=odd,
                qrows=tuple(obstruction_row(a['rho'],phase,d,a['qt']) for d in (False,True)))


def display(a):
    return [[str(x) for x in row] for row in a.to_Matrix().tolist()]


def report(middle,embedding):
    a=actual(middle,embedding); m=matter_data(middle,embedding)
    b,r,h=a['B'],a['R'],a['H']; k=a['K']
    return dict(middle=middle,embedding=embedding,q=str(a['q']),
        B_rank=b.rank(),relator_rank=r.rank(),H1=h.shape[1],
        plus=a['Hs'][1].shape[1],minus=a['Hs'][-1].shape[1],
        Z_plus=a['Z'][1].shape[1],Z_minus=a['Z'][-1].shape[1],
        B_plus=a['Bs'][1].shape[1],B_minus=a['Bs'][-1].shape[1],
        q_nonboundary=cat(b,a['qt']).rank()>b.rank(),
        q_even_mod_boundary=cat(b,(a['T']-eye(30,k))*a['qt']).rank()==b.rank(),
        matter_rows=[display(x) for x in m['rows']],
        matter_joint_rank=m['joint'].rank(),odd_matter_joint_rank=m['odd'].rank(),
        odd_first_order_survivors=a['Hs'][-1].shape[1]-m['odd'].rank(),
        q_matter_obstructions=[display(x) for x in m['qrows']],
        quotient_basis=display(h))


if __name__=='__main__':
    for middle in (14,34):
        for embedding in (1,-1):
            print(json.dumps(report(middle,embedding),sort_keys=True),flush=True)
