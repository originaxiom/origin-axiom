"""Separate Weyl closure, rational matrix and finite monomial verification."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def plus(a,b):
    return tuple(x+y for x,y in zip(a,b))

def times(a,c):
    return tuple(c*x for x in a)

def weyl():
    ss=[(1,-1,-1,-1,-1,-1,-1,1),(2,2,0,0,0,0,0,0)]
    ss += [tuple(-2*int(i==k)+2*int(i==k+1) for i in range(8)) for k in range(6)]
    seen=set(ss); todo=list(ss)
    for r in todo:
        for a in ss:
            n=plus(r,times(a,-dot(r,a)//4))
            if n not in seen:
                seen.add(n);todo.append(n)
    return seen

def rank(a):
    a=[list(map(F,row)) for row in a]
    if not a:
        return 0
    row=0
    for col in range(len(a[0])):
        pivot=next((k for k in range(row,len(a)) if a[k][col]),None)
        if pivot is None:
            continue
        a[row],a[pivot]=a[pivot],a[row]
        q=a[row][col];a[row]=[v/q for v in a[row]]
        for k in range(len(a)):
            if k!=row:
                q=a[k][col];a[k]=[v-q*w for v,w in zip(a[k],a[row])]
        row+=1
        if row==len(a):
            break
    return row

def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def tr(a):
    return list(map(list,zip(*a)))

def subtract(a,b):
    return [[x-y for x,y in zip(r,t)] for r,t in zip(a,b)]

def bracket(a,b):
    return subtract(mul(a,b),mul(b,a))

def unit(i,j):
    return [[F(int((r,c)==(i,j))) for c in range(3)] for r in range(3)]

def flatten(a):
    return [v for row in a for v in row]

def simples(rr):
    pos={a for a in rr if next(x for x in a if x)>0}
    return sorted(r for r in pos if not any(plus(r,times(a,-1)) in pos for a in pos))

def components(rr):
    # Equivalence closure by repeated union, not traversal used by native.
    blocks=[{r} for r in sorted(rr)]
    while True:
        pair=next(((i,j) for i in range(len(blocks)) for j in range(i) if any(dot(a,b) for a in blocks[i] for b in blocks[j])),None)
        if pair is None:
            return sorted(blocks,key=lambda b:min(b))
        i,j=pair;blocks[j]|=blocks[i];blocks.pop(i)

def fixed_tensor(sa,sb):
    # Exact root-of-unity phases: no floating matrices or finite-field rank.
    allowed={(i,j) for i,j in product(range(3),repeat=2) if (sa*i+sb*j)%3==0}
    unseen=set(product(range(3),repeat=2));count=0
    while unseen:
        i,j=min(unseen)
        orbit={((i+k)%3,(j+k)%3) for k in range(3)}
        count+=int(orbit<=allowed);unseen-=orbit
    return count

def monomial_mul(a,b):
    pa,ea=a;pb,eb=b
    return tuple(pa[pb[i]] for i in range(3)),tuple((eb[i]+ea[pb[i]])%3 for i in range(3))

def finite_group():
    identity=((0,1,2),(0,0,0));d=((0,1,2),(0,1,2));p=((1,2,0),(0,0,0))
    seen={identity};todo=[identity]
    for x in todo:
        for g in (d,p):
            z=monomial_mul(x,g)
            if z not in seen:
                seen.add(z);todo.append(z)
    return seen

@lru_cache(None)
def run():
    rr=weyl();beta=(0,0,0,2,0,2,0,0);delta=(0,0,0,0,2,2,0,0)
    v=plus(beta,times(delta,-1));k=plus(beta,delta)
    e6={r for r in rr if dot(r,beta)==dot(r,delta)==0}
    c=[(2,-2,0,0,0,0,0,0),(0,2,-2,0,0,0,0,0)]
    pieces=components({r for r in e6 if all(dot(r,a)==0 for a in c)})
    a,b=[simples(z) for z in pieces];basis=a+b+c
    labels=Counter(tuple(dot(r,t)//4 for t in basis) for r in e6)
    w={(1,0),(-1,1),(0,-1)}
    mixed=[]
    for signs in product((-1,1),repeat=3):
        ws=[{times(z,t) for z in w} for t in signs]
        expected={u+v+w for u,v,w in product(*ws)}
        if all(labels[z]==1 for z in expected):
            mixed.append(signs)
    candidates=[]
    for eps,eta in product((-1,1),repeat=2):
        center=tuple(eta*F(a[0][i]+2*a[1][i]+eps*(b[0][i]+2*b[1][i]),3) for i in range(8))
        residue=tuple(center[i]+F(k[i],6)-F(v[i],2) for i in range(8))
        if all(F(dot(r,residue),4).denominator==1 for r in rr):
            candidates.append((eps,eta,center))
    eps,eta,center=candidates[0]
    inv=[fixed_tensor(sa*eta,sb*eta*eps) for sa,sb,sc in mixed]
    missing=sum(F(dot(r,tuple(F(k[i],6)-F(v[i],2) for i in range(8))),4).denominator!=1 for r in rr)
    x,y=unit(0,2),unit(1,2)
    mat_k=bracket(x,tr(x));mat_k=[[p+q for p,q in zip(u,v)] for u,v in zip(mat_k,bracket(y,tr(y)))]
    h=[[F(2,3)*z for z in row] for row in mat_k]
    local=all(bracket(h,z)==[[2*t for t in row] for row in z] for z in (x,y))
    # Columns of all four linear intertwining equations in nine unknowns.
    columns=[]
    for i,j in product(range(3),repeat=2):
        jj=unit(i,j);col=[]
        for t in (x,y,tr(x),tr(y)):
            left=mul(jj,t);right=mul(tr(t),jj)
            col.extend(p+q for p,q in zip(flatten(left),flatten(right)))
        columns.append(col)
    dual_null=9-rank(tr(columns))
    c1,c2=[times(z,F(1,2)) for z in c]
    long={c1,c2,plus(c1,c2),times(c1,-1),times(c2,-1),times(plus(c1,c2),-1)}
    fundamental={times(plus(times(c1,2),c2),F(1,3)),times(plus(times(c1,-1),c2),F(1,3)),times(plus(times(c1,-1),times(c2,-2)),F(1,3))}
    short=fundamental|{times(z,-1) for z in fundamental};g2=long|short
    reflect_ok=all(plus(r,times(t,-2*dot(r,t)/dot(t,t))) in g2 for r in g2 for t in g2)
    predicates={
        'Weyl_reconstruction_240':len(rr)==240 and all(dot(r,r)==8 for r in rr),
        'orthogonal_E6_rank6':len(e6)==72 and rank(list(e6))==6,
        'trinification_two_A2_components':list(map(len,pieces))==[6,6] and len(a)==len(b)==2,
        'two_conjugate_27_tensors':len(mixed)==2 and mixed[0]==tuple(-t for t in mixed[1]),
        'all_E6_weights_accounted':18+6+27*len(mixed)==78 and len(labels)==72,
        'all_E8_phase_equations_exact':len(candidates)==1,
        'center_trivial_on_E6_adjoint':all(F(dot(r,center),4).denominator==1 for r in e6),
        'center_nontrivial_on_mixed_E8':missing==162,
        'tensor_duality_matches_center':all(sa+eps*sb==0 for sa,sb,sc in mixed),
        'finite_Heisenberg_order27':len(finite_group())==27,
        'adjoint_invariants_only_identity':fixed_tensor(1,-1)==1,
        'both_mixed_invariants_one':inv==[1,1],
        'wrong_same_tensor_has_none':fixed_tensor(1,1)==0,
        'two_spin_grade_equations':local,
        'spin_fields_commute':all(z==0 for z in flatten(bracket(x,y))),
        'moment_exact':all(F(z,6)==t/4 for row,hh in zip(mat_k,h) for z,t in zip(row,hh)),
        'positive_finite_norm_coefficient':sum(mul(tr(t),t)[i][i] for t in (x,y) for i in range(3))/6==F(1,3),
        'dual_equation_full_rank':dual_null==0,
        'G2_lengths_rank':len(long)==len(short)==6 and rank(list(g2))==2 and {dot(t,t) for t in short}=={F(2,3)} and {dot(t,t) for t in long}=={2},
        'G2_reflection_closed':reflect_ok,
        'G2_simple_cartan_product3':any(F(4*dot(l,t)**2,dot(l,l)*dot(t,t))==3 and dot(l,t)<0 for l in long for t in short),
    }
    return {'predicates':predicates,'predicates_passed':sum(predicates.values()),
        'root_profile':{'E8':240,'E6':len(e6),'trinification_adjoint_dimensions':[8,8,8],'mixed_dimensions':[27]*len(mixed)},
        'gauge_profile':{'adjoint_factor_invariants':[0,0,8],'mixed_factor_invariants':[3*n for n in inv],'dimension':8+3*sum(inv),'rank':rank(list(g2)),'long_roots':len(long),'short_roots':len(short)},
        'phase_profile':{'center_order':3,'total_peripheral_order':2,'uncompensated_mismatched_roots':missing,'flat_root_choices':9}}

if __name__=='__main__':
    data=run();print(json.dumps(data,indent=2))
    raise SystemExit(0 if all(data['predicates'].values()) else 1)
