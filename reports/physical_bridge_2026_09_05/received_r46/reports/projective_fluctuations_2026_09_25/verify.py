"""F13 finite algebra controls; the analytic arguments have separate status."""
from functools import lru_cache
from pathlib import Path
import importlib.util
import sympy as s

ROOT=Path(__file__).parent.parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


f12=load('f13_f12',ROOT/'projective_global_metric_2026_09_21'/'verify.py')
f05=load('f13_f05',ROOT/'parent_twist_gap_2026_09_20'/'verify.py')
field=f12.f11
f11=field.v
f10=f12.f10
q,z,L,beta,k=f12.q,f12.z,f12.L,f12.beta,f12.k
omega=s.symbols('omega',real=True)
ACTUAL=((14,-1),(34,1))


def clean(a):
    return a.applyfunc(s.simplify)


def comm(a,b):
    return a*b-b*a


def frobenius2(a):
    return s.simplify(s.trace(a.H*a))


def six_representation(sign=1):
    return {g:sign*f05.exterior_group(a)
            for g,a in zip('mn',f10.generators())}


def field_affine(w,rho,p):
    """Compose homogeneous affine blocks, independently of prefix Fox sums."""
    dim=next(iter(rho.values())).rows
    total=dim*(1+len(rho))
    letters={}
    for j,(g,a) in enumerate(rho.items()):
        matrix=s.eye(total)
        matrix[:dim,:dim]=a
        matrix[:dim,dim*(j+1):dim*(j+2)]=s.eye(dim)
        inverse=s.eye(total)
        ai=field.reduce_matrix(a.inv(),p)
        inverse[:dim,:dim]=ai
        inverse[:dim,dim*(j+1):dim*(j+2)]=-ai
        letters[g]=matrix
        letters[g.upper()]=inverse
    out=s.eye(total)
    for letter in w:
        out=field.reduce_matrix(out*letters[letter],p)
    return out[:dim,:dim],out[:dim,dim:]


def rank_witness(a,p):
    _,cols=field.rref(a,p)
    _,rows=field.rref(a[:,list(cols)].T,p)
    sub=a.extract(rows,cols)
    det=f12.determinant_field(sub,p) if cols else s.Integer(1)
    return {'rank':len(cols),'rows':rows,'cols':cols,'minor':det}


@lru_cache(None)
def six_certificate(middle,sign):
    p=q*q-middle*q+1
    rho=six_representation(sign)
    b=field.reduce_matrix(s.Matrix.vstack(*(a-s.eye(6) for a in rho.values())),p)
    j=field.reduce_matrix(f11.fox(f11.RELATOR,rho),p)
    relation,affine=field_affine(f11.RELATOR,rho,p)
    wb,wj=rank_witness(b,p),rank_witness(j,p)
    result={'middle':middle,'six_character':sign,'B':wb,'J':wj,
            'H0':6-wb['rank'],'H1':12-wb['rank']-wj['rank'],
            'relation':relation==s.eye(6),'fox_equals_affine':j==affine,
            'J_B_zero':field.reduce_matrix(j*b,p)==s.zeros(6)}
    if result['H1']:
        null=field.kernel(j,p)
        for i in range(null.cols):
            if field.rank(b.row_join(null[:,i]),p)>wb['rank']:
                result['nonboundary_cocycle']=null[:,i]
                break
    return result


def six_cusp():
    return tuple(f05.exterior_lie(a) for a in f10.local_connection())


def six_longitude_inverse():
    _,p,d,_=f10.cusp_generators()
    d6,p6=f05.exterior_lie(d),f05.exterior_lie(p)
    u=z*z/4-beta*beta/L**2
    inv=(s.I*omega*s.eye(6)-k*d6).inv()
    return clean(inv+(beta/u)*inv*p6*inv)


def pauli_hermitian(prefix):
    a,b,c=s.symbols(prefix+'0:3',real=True)
    return s.Matrix([[a,b-s.I*c],[b+s.I*c,-a]])


def linearized_split():
    """Independent first jets at a normal orthonormal coordinate frame."""
    ps=tuple(pauli_hermitian('P'+str(i)+'_') for i in range(3))
    aa=tuple(s.I*pauli_hermitian('a'+str(i)+'_') for i in range(3))
    pp=tuple(pauli_hermitian('p'+str(i)+'_') for i in range(3))
    da=s.I*pauli_hermitian('diva_')
    dp=pauli_hermitian('divp_')
    # da,dp denote delta_A a,delta_A psi, not unsigned divergence.
    adj=da+dp+sum((comm(x,a+p) for x,a,p in zip(ps,aa,pp)),s.zeros(2))
    gauge=da+sum((comm(x,p) for x,p in zip(ps,pp)),s.zeros(2))
    moment=dp+sum((comm(x,a) for x,a in zip(ps,aa)),s.zeros(2))
    wrong_moment=dp-sum((comm(x,a) for x,a in zip(ps,aa)),s.zeros(2))
    return adj,gauge,moment,wrong_moment


def nonlinear_moment_coefficients():
    """Expand -sum_i (partial_i Psi_i + [A_i,Psi_i]) in a flat jet."""
    t=s.symbols('t',real=True)
    a0=tuple(s.I*pauli_hermitian('A'+str(i)+'_') for i in range(3))
    p0=tuple(pauli_hermitian('H'+str(i)+'_') for i in range(3))
    aa=tuple(s.I*pauli_hermitian('v'+str(i)+'_') for i in range(3))
    pp=tuple(pauli_hermitian('w'+str(i)+'_') for i in range(3))
    div=pauli_hermitian('dp_')
    diff=-t*div-sum((comm(a+t*x,p+t*y)-comm(a,p)
                                for a,p,x,y in zip(a0,p0,aa,pp)),s.zeros(2))
    first=-div-sum((comm(a,y) for a,y in zip(a0,pp)),s.zeros(2))
    first+=sum((comm(p,x) for p,x in zip(p0,aa)),s.zeros(2))
    second=-sum((comm(x,y) for x,y in zip(aa,pp)),s.zeros(2))
    return t,clean(diff),clean(first),clean(second)


if __name__=='__main__':
    for middle,sign in ACTUAL:
        print('ACTUAL',six_certificate(middle,sign),flush=True)
        print('OPPOSITE_CHARACTER_CONTROL',six_certificate(middle,-sign),flush=True)
