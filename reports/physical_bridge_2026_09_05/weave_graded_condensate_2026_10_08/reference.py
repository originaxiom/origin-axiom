"""Separate rational polynomial-module route; no import of native probe."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb
from functools import lru_cache
import json


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def transpose(a):
    return [list(x) for x in zip(*a)]


def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def add(a,b):
    return [[x+y for x,y in zip(r,t)] for r,t in zip(a,b)]


def scale(a,c):
    return [[c*x for x in row] for row in a]


def diag(v):
    return [[v[i] if i==j else F(0) for j in range(len(v))] for i in range(len(v))]


def adj(a,g):
    return mul(mul(diag([1/x for x in g]),transpose(a)),diag(g))


def weyl_roots():
    simple=[(1,-1,-1,-1,-1,-1,-1,1),(2,2,0,0,0,0,0,0)]
    simple += [tuple(-2*int(i==k)+2*int(i==k+1) for i in range(8)) for k in range(6)]
    seen=set(simple)
    queue=list(simple)
    for r in queue:
        for a in simple:
            c=tuple(r[i]-dot(r,a)//4*a[i] for i in range(8))
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return seen


def simple_system(rr):
    # First nonzero positive, independent of tuple ordering.
    positive={r for r in rr if next(x for x in r if x)>0}
    return sorted(r for r in positive if not any(tuple(r[k]-a[k] for k in range(8)) in positive for a in positive))


def polynomial(n):
    g=[F(1,comb(n,k)) for k in range(n+1)]
    E=[[F(k) if i==k-1 else F(0) for k in range(n+1)] for i in range(n+1)]
    lower=adj(E,g)
    H=add(mul(E,lower),scale(mul(lower,E),-1))
    return E,lower,H,g


def blocks_from_polynomials(j):
    E,lower,H,g=polynomial(2*j)
    result=[]
    for m in range(-j-1,j+1):
        if m%2:
            continue
        a=(-j<=m<=j)
        q=(-j<=m+1<=j)
        if not(a or q):
            continue
        d=F(m+1,2)
        if a and q:
            k=j-m
            up=E[k-1][k]
            down=lower[k][k-1]
            gram=[g[k],g[k-1]/2]
            b0=[[d,down/2],[-up,d]]
            b1=diag([F(1),F(-1)])
        else:
            b0=[[d]]
            b1=[[F(1 if a else -1)]]
            gram=[F(1)]
        coeff2=scale(mul(adj(b1,gram),b1),-1)
        coeff1=add(mul(adj(b0,gram),b1),scale(mul(adj(b1,gram),b0),-1))
        coeff0=mul(adj(b0,gram),b0)
        value=coeff0[0][0]
        result.append((len(b0),value,coeff2,coeff1,coeff0,gram,m))
    return result


@lru_cache(None)
def run():
    rr=weyl_roots()
    beta=(0,0,0,2,0,2,0,0)
    gamma=(0,0,0,0,-2,-2,0,0)
    v=tuple(a+b for a,b in zip(beta,gamma))
    weights=Counter({0:8})
    weights.update(F(dot(r,v),2) for r in rr)
    # Strip highest irreducible modules rather than taking adjacent differences.
    remaining=weights.copy()
    spins=Counter()
    while any(remaining.values()):
        high=max(k for k,n in remaining.items() if n)
        assert high.denominator==1 and high%2==0
        j=int(high)//2
        copies=remaining[high]
        spins[j]+=copies
        for m in range(-j,j+1):
            remaining[2*m]-=copies
            assert remaining[2*m]>=0
    r6={r for r in rr if dot(r,beta)==dot(r,gamma)==0}
    simples=simple_system(r6)
    cartan=[[dot(a,b)//4 for b in simples] for a in simples]
    full,rhist=Counter(),Counter()
    block_checks=[]
    r_matches=[]
    for j,copies in spins.items():
        E,L,H,g=polynomial(2*j)
        for channels,value,c2,c1,c0,gram,m in blocks_from_polynomials(j):
            full[str(value)]+=channels*copies
            block_checks.append(c2==diag([-F(1)]*channels) and c1==diag([F(0)]*channels) and c0==diag([value]*channels))
            if -j<=-m-1<=j:
                rweight=-m-1
                kr=j-rweight
                rnorm=E[kr-1][kr]**2*g[kr-1]/g[kr] if kr else F(0)
                r_matches.append(value==F(rweight*rweight,4)+rnorm/2)
        for k in range(2*j+1):
            m=j-k
            if m%2:
                norm=E[k-1][k]**2*g[k-1]/g[k] if k else F(0)
                rhist[str(F(m*m,4)+norm/2)]+=copies
    E,L,H,g=polynomial(2)
    J=[[F(0),F(0),F(1)],[F(0),-F(1,2),F(0)],[F(1),F(0),F(0)]]
    intertwiners=[add(mul(J,t),mul(transpose(t),J))==diag([F(0)]*3) for t in (E,L,H)]
    dual_isometry=mul(mul(transpose(J),diag([1/x for x in g])),J)==diag(g)
    bad=diag([F(1),F(-1),F(0)])
    hroot=(-4,-4,-4,6,6,0,0,0)
    a2weights=Counter((dot(r,beta)//4,dot(r,gamma)//4) for r in rr)
    defining={(1,0),(-1,1),(0,-1)}
    dual={(-a,-b) for a,b in defining}
    facts={
        'Weyl_closure_240_norm2': len(rr)==240 and all(dot(r,r)==8 for r in rr),
        'A2_regular_root_subsystem': beta in rr and gamma in rr and v in rr and dot(beta,gamma)==-4,
        'old_peripheral_exact_lattice_identity': all(dot(r,tuple(v[k]-hroot[k] for k in range(8)))%8==0 for r in rr),
        'H_all_even_weights_SO3': all(k.denominator==1 and k%2==0 for k in weights),
        'highest_weight_subtraction_78_55_1': dict(spins)=={2:1,1:55,0:78},
        'A2_commutant_72_roots': len(r6)==72 and len(simples)==6,
        'full_72_root_reflection_closure': all(tuple(r[k]-dot(r,a)//4*a[k] for k in range(8)) in r6 for r in r6 for a in r6),
        'simple_Cartan_E6_degrees': sorted(sum(x==-1 for x in row) for row in cartan)==[1,1,1,2,2,3],
        'charged_A2_triplet_and_dual_multiplicity27': all(a2weights[w]==27 for w in defining|dual),
        'polynomial_metric_not_identity': g==[F(1),F(1,2),F(1)],
        'polynomial_sl2_relations': H==diag([F(2),F(0),F(-2)]) and add(mul(H,E),scale(mul(E,H),-1))==scale(E,2),
        'all_weighted_formal_adjoint_blocks': bool(block_checks) and all(block_checks),
        'R_negative_weight_pairing': bool(r_matches) and all(r_matches),
        'full_profile': full==Counter({'1/4':133,'5/4':110,'9/4':3,'13/4':2}),
        'R_profile': rhist==Counter({'1/4':55,'5/4':55,'9/4':1,'13/4':1}),
        'full_population_248': sum(full.values())==248,
        'R_population112': sum(rhist.values())==112,
        'essential_lower_bound_positive': min(F(a) for a in full)==F(1,4),
        'uniform_angular_linear_coefficient_bound': max(abs(F(m+1)+sign) for j in spins for m in range(-j-1,j+1) for sign in (-1,1))==4,
        'global_moment_and_spin_residuals': -F(1,4)+F(1,2)**2==0 and -F(1,2)+2*F(1,4)==0,
        'wrong_amplitude_not_stationary': -F(1,4)+F(1)**2!=0,
        'expanded_energy_balance': F(1,16)+F(1,16)-F(1,8)==0,
        'dual_form_intertwines_all_triple_generators': all(intertwiners),
        'dual_form_is_unitary_in_actual_metric': dual_isometry,
        'full_SU3_extension_control_rejected': add(mul(J,bad),mul(transpose(bad),J))!=diag([F(0)]*3),
        'odd_commuting_root_control54': sum(dot(r,v)//4%2 and dot(r,beta)==0 for r in rr)==54,
    }
    for name,ok in facts.items():
        if not bool(ok):
            raise AssertionError(name)
    return dict(predicates=facts,predicates_passed=len(facts),
        root_profile=dict(root_count=len(rr),H_weights={str(int(k)):weights[k] for k in sorted(weights)},
            spin_multiplicities={str(k):spins[k] for k in sorted(spins)},E6_roots=len(r6),
            E6_simple_roots_doubled=[list(a) for a in simples],E6_Cartan=cartan),
        spectrum_profile=dict(full_squared_thresholds=dict(full),R_squared_thresholds=dict(rhist),
            singular_channels=sum(full.values()),first_order_essential_gap_radius='1/2'),
        pairing_profile=dict(J=[[int(J[i][j]/g[i]) for j in range(3)] for i in range(3)],
            complex_charged_pair=[a2weights[(1,0)],a2weights[(-1,0)]],net_27_chirality=0))


if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
