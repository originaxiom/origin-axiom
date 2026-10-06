"""Separate exact Fraction/bit-mask/Fourier reference; no native imports."""
import itertools
import json
from fractions import Fraction as Q
from functools import lru_cache


def sum_poly(*terms):
    out={}
    for term in terms:
        for key,value in term.items():
            out[key]=out.get(key,Q(0))+value
    return {k:v for k,v in out.items() if v}


def scaled(p,c):
    return {k:v*c for k,v in p.items() if v*c}


def product(p,q):
    out={}
    for (e,mask),a in p.items():
        for (f,other),b in q.items():
            if mask&other:continue
            crossings=sum((other&((1<<i)-1)).bit_count() for i in range(5) if mask&(1<<i))
            key=(tuple(e[i]+f[i] for i in range(4)),mask|other)
            out[key]=out.get(key,Q(0))+(-1)**crossings*a*b
    return {k:v for k,v in out.items() if v}


def variable(i,exterior=False):
    e=[0]*4
    if not exterior:e[i]=1
    return {(tuple(e),(1<<i) if exterior else 0):Q(1)}


def apply(p,reverse=False,enabled=True):
    if not enabled:return {}
    out={}
    for (e,mask),value in p.items():
        for i in range(3):
            powers=list(e);bit=1<<i
            if reverse:
                if not mask&bit:continue
                sign=(-1)**(mask&(bit-1)).bit_count();powers[i]+=1
                key=(tuple(powers),mask^bit);coefficient=sign*value
            else:
                if not e[i] or mask&bit:continue
                sign=(-1)**(mask&(bit-1)).bit_count();powers[i]-=1
                key=(tuple(powers),mask|bit);coefficient=sign*e[i]*value
            out[key]=out.get(key,Q(0))+coefficient
    return {k:v for k,v in out.items() if v}


def count(key):
    e,mask=key
    return sum(e[:3])+(mask&7).bit_count()


def split_primitive(p):
    parts={};harm={}
    for key,value in p.items():
        n=count(key)
        if not n:harm[key]=value
        else:parts.setdefault(n,{})[key]=value
    return sum_poly(*(scaled(apply(part,True),-Q(1,n)) for n,part in parts.items())),harm


@lru_cache(None)
def polynomial_controls():
    # Independent population construction: stars-and-bars + exterior masks.
    rows=set()
    for total in range(4):
        for mask in range(32):
            n=total-mask.bit_count()
            if n<0:continue
            for slots in itertools.combinations_with_replacement(range(4),n):
                e=tuple(slots.count(i) for i in range(4));rows.add((e,mask))
    checks={
        'all_delta_square':all(apply(apply({k:Q(1)}))=={} for k in rows),
        'all_h_square':all(apply(apply({k:Q(1)},True),True)=={} for k in rows),
        'all_Euler_identity':all(sum_poly(apply(apply({k:Q(1)},True)),apply(apply({k:Q(1)}),True))==scaled({k:Q(1)},count(k)) for k in rows),
        'all_delta_harmonic_projection_zero':all(not any(count(t)==0 for t in apply({k:Q(1)})) for k in rows),
    }
    x=[variable(i) for i in range(3)];c=[variable(i,True) for i in range(3)]
    F=scaled(product(x[0],product(x[1],x[2])),-Q(1,2))
    cubic=scaled(apply(F),-1)
    derived,harm=split_primitive(cubic)
    checks.update(cubic_nonzero=bool(cubic),cubic_closed=apply(cubic)=={},
        cubic_primitive_sign=derived==F and harm=={} and sum_poly(cubic,apply(derived))=={},
        wrong_sign_detected=sum_poly(cubic,apply(scaled(derived,-1)))==scaled(cubic,2),
        disabled_differential_detected=sum_poly(cubic,apply(derived,enabled=False))!={} and sum_poly(cubic,apply(derived))=={})
    mixed=product(variable(3,True),product(variable(4,True),x[0]))
    sf=apply(mixed);sol,hm=split_primitive(sf)
    checks['mixed_harmonic_contracts']=bool(sf) and hm=={} and sum_poly(sf,apply(sol))=={}
    obs=product(variable(3,True),product(variable(3),variable(3)))
    sol,hm=split_primitive(obs)
    checks['harmonic_obstruction_preserved']=bool(obs) and apply(obs)=={} and sol=={} and hm==obs
    checks['odd_sign_and_square']=product(c[0],c[1])==scaled(product(c[1],c[0]),-1) and product(c[0],c[0])=={}
    return checks,len(rows)


# Gaussian rationals, not float/complex arithmetic. Fourier-polynomial
# keys are (u1 power,u2 power,u3 power,X frequency,Y frequency).
ZERO=(Q(0),Q(0));ONE=(Q(1),Q(0));I=(Q(0),Q(1))


def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def times(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def fp_add(*terms):
    out={}
    for p in terms:
        for k,v in p.items():out[k]=plus(out.get(k,ZERO),v)
    return {k:v for k,v in out.items() if v!=ZERO}


def fp_scale(p,n):
    return {k:(n*v[0],n*v[1]) for k,v in p.items() if n and v!=ZERO}


def fp_mul(p,q):
    out={}
    for k,v in p.items():
        for t,w in q.items():
            key=tuple(k[i]+t[i] for i in range(5))
            out[key]=plus(out.get(key,ZERO),times(v,w))
    return {k:v for k,v in out.items() if v!=ZERO}


def diff(p,direction):
    return {k:times(v,(Q(0),Q(k[3+direction]))) for k,v in p.items() if k[3+direction]}


def blank():return [[{} for j in range(5)] for i in range(5)]
def madd(*mat):return [[fp_add(*(M[i][j] for M in mat)) for j in range(5)] for i in range(5)]
def mscale(M,n):return [[fp_scale(p,n) for p in row] for row in M]
def mmul(A,B):return [[fp_add(*(fp_mul(A[i][k],B[k][j]) for k in range(5))) for j in range(5)] for i in range(5)]
def bracket(A,B):return madd(mmul(A,B),mscale(mmul(B,A),-1))
def mdiff(A,d):return [[diff(p,d) for p in row] for row in A]
def empty(A):return all(not p for row in A for p in row)


@lru_cache(None)
def fourier_controls():
    sinx={(0,0,0,1,0):(Q(0),-Q(1,2)),(0,0,0,-1,0):(Q(0),Q(1,2))}
    siny={(0,0,0,0,1):(Q(0),-Q(1,2)),(0,0,0,0,-1):(Q(0),Q(1,2))}
    coscos={(0,0,0,m,n):(Q(1,4),Q(0)) for m in (-1,1) for n in (-1,1)}
    f=[sinx,siny,coscos]
    T=[]
    for i,j in ((0,1),(1,2),(2,0)):
        M=[[0]*5 for _ in range(5)];M[i][j]=1;M[j][i]=-1;T.append(M)
    def int_mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
    def tr_bracket(A,B,C):
        BC=int_mul(B,C);CB=int_mul(C,B)
        D=[[BC[i][j]-CB[i][j] for j in range(5)] for i in range(5)]
        return sum(int_mul(A,D)[i][i] for i in range(5))
    means=[]
    for i in range(3):
        j,k=(i+1)%3,(i+2)%3
        wedge=fp_add(fp_mul(diff(f[j],0),diff(f[k],1)),fp_scale(fp_mul(diff(f[j],1),diff(f[k],0)),-1))
        integrand=fp_scale(fp_mul(f[i],wedge),tr_bracket(T[i],T[j],T[k]))
        means.append(integrand.get((0,0,0,0,0),ZERO))
    chi=blank()
    for r in range(3):
        pol={tuple(k[i]+(1 if i==r else 0) for i in range(5)):v for k,v in f[r].items()}
        for i in range(5):
            for j in range(5):chi[i][j]=fp_add(chi[i][j],fp_scale(pol,T[r][i][j]))
    first=[mdiff(chi,k) for k in range(2)]
    second=[mscale(bracket(a,chi),Q(1,2)) for a in first]
    third=[mscale(bracket(bracket(a,chi),chi),Q(1,6)) for a in first]
    F2=madd(mdiff(second[1],0),mscale(mdiff(second[0],1),-1),bracket(first[0],first[1]))
    F3=madd(mdiff(third[1],0),mscale(mdiff(third[0],1),-1),bracket(first[0],second[1]),bracket(second[0],first[1]))
    # Conjugate frequency and transpose: actual Fourier anti-Hermiticity.
    adj=[[{k[:3]+(-k[3],-k[4]):(v[0],-v[1]) for k,v in chi[j][i].items()} for j in range(5)] for i in range(5)]
    # Canonical primitive polynomial evaluated via exact polynomial data.
    potential={(3,0): -Q(1,6)}
    derivative={(a-1,b):a*v for (a,b),v in potential.items() if a}
    graph={(2,0):-Q(1,2)}
    corrected=sum_poly(graph,scaled(derivative,-1))
    opposite=sum_poly(graph,derivative)
    checks={
        'SU5_compact_matrices':all(all(M[i][j]==-M[j][i] for i in range(5) for j in range(5)) and sum(M[i][i] for i in range(5))==0 for M in T),
        'nonzero_bulk_trace':tr_bracket(*T)==2,
        'actual_CS_Fourier_means':means==[(Q(1,2),Q(0))]*3,
        'actual_compact_Fourier_generator':empty(madd(adj,chi)),
        'quadratic_curvature_cancels':empty(F2),
        'cubic_curvature_cancels':empty(F3),
        'old_linear_escape_not_deleted':not empty(bracket(first[0],first[1])),
        'graph_primitive_nonzero':bool(graph),
        'counterterm_cancels':corrected=={} and bool(graph),
        'opposite_counterterm_fails':bool(opposite),
    }
    return checks,[str(z[0]) for z in means]


@lru_cache(None)
def run():
    a,n=polynomial_controls();b,means=fourier_controls();checks={**a,**b}
    failed=[k for k,v in checks.items() if v is not True]
    return dict(checks=checks,passed=len(checks)-len(failed),failed=failed,
        profile=dict(monomials=n,CS_normalized_means=means,first_obstruction='delta-exact at cubic Hamiltonian order',
            vector_field_normal_remainder_order=3,linear_tangent_changed=False),
        all_order_charged_completion=False,physical_action_stationary=False,
        physical_goal_achieved=False,genesis_boundary_selected=False,non_author_acceptance=False)


if __name__=='__main__':
    result=run();print(json.dumps(result,sort_keys=True));raise SystemExit(bool(result['failed']))
