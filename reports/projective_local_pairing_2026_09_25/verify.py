"""F16 exact hypotheses for the authored convergent local-pairing proof."""
from pathlib import Path
from functools import lru_cache
import importlib.util
import json
import sympy as s

path=Path(__file__).parent.parent/'projective_deformation_tangent_2026_09_25'/'verify_v2.py'
spec=importlib.util.spec_from_file_location('f16_corrected_f15',path)
adapter=importlib.util.module_from_spec(spec); spec.loader.exec_module(adapter)
v=adapter.v


def inverse_word(w):
    return w.swapcase()[::-1]


def reduce_word(w):
    out=[]
    for c in w:
        if out and out[-1]==c.swapcase(): out.pop()
        else: out.append(c)
    return ''.join(out)


@lru_cache(None)
def slice_certificate(middle,embedding):
    a=v.actual(middle,embedding); k=a['K']; t=a['T']; b=a['B']; r=a['R']
    if b.rank()!=15: raise ValueError('gauge derivative must be injective')
    ambient={sign:v.kernel(t-v.eye(30,k).scalarmul(k(sign))) for sign in (1,-1)}
    w={sign:v.quotient(a['Bs'][sign],ambient[sign]) for sign in (1,-1)}
    total=v.cat(b,w[1],w[-1]); odd=r*w[-1]
    if total.shape!=(30,30) or total.rank()!=30:
        raise ArithmeticError('no ambient gauge coordinate chart')
    rows=odd.transpose().rref()[1]
    if len(rows)!=w[-1].shape[1]:
        raise ArithmeticError('odd relator derivative not injective')
    minor=odd.extract(rows,range(odd.shape[1]))
    return dict(a=a,ambient=ambient,W=w,total=total,odd=odd,
                rows=rows,minor=minor,total_det=total.det(),minor_det=minor.det())


def exp_jet(x,degree=4):
    k=x.domain; out=[v.eye(x.shape[0],k)]; power=out[0]
    for n in range(1,degree+1):
        power=power*x
        out.append(power.scalarmul(k.from_sympy(s.Rational(1,s.factorial(n)))))
    return tuple(out)


def chart_jet_residuals(a,u,degree=4):
    """F(exp(tu)rho0)=exp(tTu)rho0, checked coefficientwise."""
    k=a['K']; j=a['J']; ji=j.inv()
    tu=a['T']*u; out=[]
    for g,rho in enumerate(a['rho']):
        x=v.uncoords(u.extract(range(15*g,15*g+15),[0]))
        tx=v.uncoords(tu.extract(range(15*g,15*g+15),[0]))
        for ex,et in zip(exp_jet(x,degree),exp_jet(tx,degree)):
            out.append(ji*(ex*rho).transpose()*j-et*rho)
    return tuple(out)


@lru_cache(None)
def conjugated_family():
    """Exact rational-function control, NOT a new off-q physical family."""
    q=v.f10.q; t=s.Symbol('t'); k=s.QQ.frac_field(q,t)
    rho=tuple(v.dm(x,k) for x in v.f10.generators(q+t))
    j=v.dm(v.intertwiner(q+t),k)
    units=[]
    for i,l,power in ((0,1,1),(2,3,2),(1,2,1)):
        x=s.eye(4); x[i,l]=t**power; units.append(v.dm(x,k))
    g=units[0]*units[1]*units[2]; gi=g.inv()
    moved=tuple(gi*x*g for x in rho); ja=g.transpose()*j*g
    return dict(k=k,q=q,t=t,rho=moved,original=rho,J=j,Ja=ja,g=g,
                fixed_J=v.dm(v.intertwiner(q),k))


def word(w,rho):
    k=rho[0].domain
    out=v.eye(4,k); letters={g:a for g,a in zip('mn',rho)}
    letters.update({g:a.inv() for g,a in zip('MN',rho)})
    for c in w: out=out*letters[c]
    return out


def report(middle,embedding):
    c=slice_certificate(middle,embedding); a=c['a']; k=a['K']
    w=v.cat(c['W'][1],c['W'][-1]); r=a['R']
    return dict(middle=middle,embedding=embedding,q=str(a['q']),
        ambient_plus=c['ambient'][1].shape[1],ambient_minus=c['ambient'][-1].shape[1],
        slice_plus=c['W'][1].shape[1],slice_minus=c['W'][-1].shape[1],
        gauge_coordinate_rank=c['total'].rank(),
        gauge_coordinate_determinant=str(k.to_sympy(c['total_det'])),
        odd_residual_rank=c['odd'].rank(),odd_minor_rows=list(c['rows']),
        odd_minor_determinant=str(k.to_sympy(c['minor_det'])),
        slice_tangent_dim=15-(r*w).rank(),
        W_plus=v.display(c['W'][1]),W_minus=v.display(c['W'][-1]),
        odd_minor=v.display(c['minor']))


if __name__=='__main__':
    for middle in (14,34):
        for embedding in (1,-1):
            print(json.dumps(report(middle,embedding),sort_keys=True),flush=True)
