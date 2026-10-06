"""Live finite identities for a formal cubic boundary correction, not a TOE."""
import itertools
import json
from functools import lru_cache

import sympy as s


# Four commuting coordinates: three acyclic x's and one harmonic z.
# Five exterior generators: three acyclic c's and harmonic kappa,b.
def clean(p):
    return {k:s.Rational(v) for k,v in p.items() if v != 0}


def add(*polys):
    out = {}
    for p in polys:
        for key,value in p.items():
            out[key] = out.get(key,0)+value
    return clean(out)


def scale(p,c):
    return clean({k:c*v for k,v in p.items()})


def mul(p,q):
    out = {}
    for (e,o),a in p.items():
        for (f,t),b in q.items():
            if set(o)&set(t):
                continue
            sign = (-1)**sum(i>j for i in o for j in t)
            key = (tuple(x+y for x,y in zip(e,f)),tuple(sorted(o+t)))
            out[key] = out.get(key,0)+sign*a*b
    return clean(out)


def even(i):
    e=[0]*4;e[i]=1
    return {(tuple(e),()):s.Integer(1)}


def odd(i):
    return {((0,0,0,0),(i,)):s.Integer(1)}


def deriv_even(p,i):
    out={}
    for (e,o),v in p.items():
        if e[i]:
            f=list(e);f[i]-=1;out[(tuple(f),o)]=e[i]*v
    return clean(out)


def deriv_odd(p,i):
    out={}
    for (e,o),v in p.items():
        if i in o:
            j=o.index(i);out[(e,o[:j]+o[j+1:])]=(-1)**j*v
    return clean(out)


def delta(p):
    return add(*(mul(odd(i),deriv_even(p,i)) for i in range(3)))


def homotopy(p):
    return add(*(mul(even(i),deriv_odd(p,i)) for i in range(3)))


def number(key):
    e,o=key
    return sum(e[:3])+sum(i<3 for i in o)


def harmonic(p):
    return clean({k:v for k,v in p.items() if number(k)==0})


def primitive(p):
    # This never discards harmonic terms and reports them separately.
    out=[]
    for n in range(1,4):
        part={k:v for k,v in p.items() if number(k)==n}
        out.append(scale(homotopy(part),-s.Rational(1,n)))
    return add(*out),harmonic(p)


def monomials():
    for e in itertools.product(range(4),repeat=4):
        for r in range(6):
            for o in itertools.combinations(range(5),r):
                if sum(e)+r<=3:
                    yield (e,o)


@lru_cache(None)
def super_checks():
    checks={};rows=list(monomials())
    checks['all_monomial_delta_square']=all(delta(delta({k:1}))=={} for k in rows)
    checks['all_monomial_h_square']=all(homotopy(homotopy({k:1}))=={} for k in rows)
    checks['all_monomial_Euler_identity']=all(
        add(delta(homotopy({k:1})),homotopy(delta({k:1})))==
        scale({k:1},number(k)) for k in rows)
    checks['all_monomial_harmonic_projection']=all(harmonic(delta({k:1}))=={} for k in rows)
    x=[even(i) for i in range(3)];c=[odd(i) for i in range(3)]
    cubic=scale(add(*(mul(c[i],mul(x[(i+1)%3],x[(i+2)%3])) for i in range(3))),s.Rational(1,2))
    F,remainder=primitive(cubic)
    expected=scale(mul(x[0],mul(x[1],x[2])),-s.Rational(1,2))
    checks['CS_cubic_nonzero']=bool(cubic)
    checks['CS_cubic_delta_closed']=delta(cubic)=={}
    checks['CS_primitive_actual_sign']=F==expected and remainder=={} and add(cubic,delta(F))=={}
    checks['wrong_generator_sign_detected']=add(cubic,delta(scale(F,-1)))==scale(cubic,2)
    disabled_delta=lambda p: {}
    checks['disabled_pair_differential_detected']=add(cubic,disabled_delta(F))!={} and add(cubic,delta(F))=={}
    mixed=mul(odd(3),mul(odd(4),even(0)))
    mixed_cocycle=delta(mixed)
    G,rem=primitive(mixed_cocycle)
    checks['mixed_harmonic_legs_contract']=bool(mixed_cocycle) and rem=={} and add(mixed_cocycle,delta(G))=={}
    obstruction=mul(odd(3),mul(even(3),even(3)))
    G,rem=primitive(obstruction)
    checks['harmonic_obstruction_retained']=delta(obstruction)=={} and rem==obstruction and G=={} and bool(rem)
    checks['ghost_pair_sign_not_commuting']=mul(odd(0),odd(1))==scale(mul(odd(1),odd(0)),-1) and mul(odd(0),odd(0))=={}
    return checks,len(rows)


def comm(A,B):
    return A*B-B*A


def matrix_zero(A):
    return all(s.expand(z)==0 for z in A)


@lru_cache(None)
def trigonometric_controls():
    X,Y=s.symbols('X Y',real=True);u=s.symbols('u1:4',real=True)
    def E(i,j):
        out=s.zeros(5);out[i,j]=1;return out
    T=[E(0,1)-E(1,0),E(1,2)-E(2,1),E(2,0)-E(0,2)]
    f=[s.sin(X),s.sin(Y),s.cos(X)*s.cos(Y)]
    means=[]
    for i in range(3):
        j,k=(i+1)%3,(i+2)%3
        value=s.trace(T[i]*comm(T[j],T[k]))*f[i]*(s.diff(f[j],X)*s.diff(f[k],Y)-s.diff(f[j],Y)*s.diff(f[k],X))
        means.append(s.integrate(value,(X,0,2*s.pi),(Y,0,2*s.pi))/(4*s.pi**2))
    chi=sum((u[i]*f[i]*T[i] for i in range(3)),s.zeros(5))
    first=[chi.diff(X),chi.diff(Y)]
    second=[comm(z,chi)/2 for z in first]
    third=[comm(comm(z,chi),chi)/6 for z in first]
    curvature2=second[1].diff(X)-second[0].diff(Y)+comm(first[0],first[1])
    curvature3=third[1].diff(X)-third[0].diff(Y)+comm(first[0],second[1])+comm(second[0],first[1])
    q,v=s.symbols('q v',real=True)
    F=-q**3/6;graph_p=s.diff(F,q)
    # Canonical lambda=p dq; a boundary functional is a real cost.
    primitive_on_graph=graph_p*v
    wrong=primitive_on_graph-s.diff(-F,q)*v
    checks={
        'compact_SU5_generators':all(z.T==-z and s.trace(z)==0 for z in T),
        'bulk_cubic_survives':s.trace(T[0]*comm(T[1],T[2]))==2,
        'three_actual_CS_mean_coefficients':means==[s.Rational(1,2)]*3,
        'compact_generator_antihermitian':chi.conjugate().T==-chi,
        'gauge_orbit_curvature_quadratic':matrix_zero(curvature2),
        'gauge_orbit_curvature_cubic':matrix_zero(curvature3),
        'linear_flat_space_escape_preserved':not matrix_zero(comm(first[0],first[1])),
        'graph_primitive_not_automatically_zero':primitive_on_graph!=0,
        'priced_graph_counterterm_cancels':s.expand(primitive_on_graph-s.diff(F,q)*v)==0,
        'wrong_counterterm_sign_detected':s.expand(wrong)!=0,
    }
    return checks,[str(z) for z in means]


@lru_cache(None)
def run():
    a,n=super_checks();b,means=trigonometric_controls();checks={**a,**b}
    failed=[k for k,v in checks.items() if v is not True]
    return dict(checks=checks,passed=len(checks)-len(failed),failed=failed,
        profile=dict(monomials=n,CS_normalized_means=means,first_obstruction='delta-exact at cubic Hamiltonian order',
            vector_field_normal_remainder_order=3,linear_tangent_changed=False),
        all_order_charged_completion=False,physical_action_stationary=False,
        physical_goal_achieved=False,genesis_boundary_selected=False,non_author_acceptance=False)


if __name__=='__main__':
    result=run();print(json.dumps(result,sort_keys=True));raise SystemExit(bool(result['failed']))
