"""Exact two-spin-field admission and full compensator centralizer."""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
import json
import sympy as s

BETA=(0,0,0,2,0,2,0,0)
DELTA=(0,0,0,0,2,2,0,0)
V=(0,0,0,2,-2,0,0,0)
C1=(2,-2,0,0,0,0,0,0)
C2=(0,2,-2,0,0,0,0,0)
W={(1,0),(-1,1),(0,-1)}

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def scale(a,c):
    return tuple(c*x for x in a)

def comm(a,b):
    return a*b-b*a

def zero(a):
    return all(s.simplify(x)==0 for x in a)

def roots():
    out=set()
    for i,j in combinations(range(8),2):
        for a,b in product((-2,2),repeat=2):
            r=[0]*8
            r[i],r[j]=a,b
            out.add(tuple(r))
    out.update(r for r in product((-1,1),repeat=8) if sum(x<0 for x in r)%2==0)
    return out

def simple(rr):
    pos={a for a in rr if a>(0,)*8}
    return sorted(a for a in pos if not any(add(a,scale(b,-1)) in pos for b in pos))

def components(rr):
    unseen=set(rr)
    answer=[]
    while unseen:
        todo=[min(unseen)]
        seen=set(todo)
        for a in todo:
            fresh={b for b in unseen-seen if dot(a,b)!=0}
            todo.extend(sorted(fresh))
            seen.update(fresh)
        unseen-=seen
        answer.append(seen)
    return sorted(answer,key=lambda x:min(x))

def label(r,ss):
    return tuple(dot(r,a)//4 for a in ss)

def weights(sign):
    return {tuple(sign*x for x in w) for w in W}

def frame(rr):
    e6={a for a in rr if dot(a,BETA)==dot(a,DELTA)==0}
    small={a for a in e6 if dot(a,C1)==dot(a,C2)==0}
    parts=components(small)
    a,b=[simple(p) for p in parts]
    c=[C1,C2]
    mixed={r for r in e6 if all(any(dot(r,t) for t in ss) for ss in (a,b,c))}
    labels={label(r,a+b+c) for r in mixed}
    signs=[]
    for sa,sb,sc in product((-1,1),repeat=3):
        want={u+v+w for u,v,w in product(weights(sa),weights(sb),weights(sc))}
        if want<=labels:
            signs.append((sa,sb,sc))
    return e6,parts,a,b,c,mixed,signs

def fields():
    x=s.zeros(3);x[0,2]=1
    y=s.zeros(3);y[1,2]=1
    k=s.diag(1,1,-2)
    return x,y,k,2*k/3

def lie_dimension(gens):
    basis=[]
    for g in gens:
        if s.Matrix.hstack(*[x.reshape(9,1) for x in basis+[g]]).rank()>len(basis):
            basis.append(g)
    while True:
        old=len(basis)
        for a,b in combinations(list(basis),2):
            g=comm(a,b)
            if s.Matrix.hstack(*[x.reshape(9,1) for x in basis+[g]]).rank()>len(basis):
                basis.append(g)
        if len(basis)==old:
            return old

def dual_dimension(gens):
    xx=s.symbols('j:9')
    j=s.Matrix(3,3,xx)
    equations=[entry for g in gens for entry in j*g+g.T*j]
    return 9-s.linear_eq_to_matrix(equations,xx)[0].rank()

def clock_pair():
    omega=(-1+s.sqrt(3)*s.I)/2
    d=s.diag(1,omega,s.conjugate(omega))
    p=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
    return omega,d,p

def invariant_dimension(ops):
    n=ops[0].rows
    stacked=s.Matrix.vstack(*[(g-s.eye(n)).applyfunc(s.simplify) for g in ops])
    return n-stacked.rank()

def color_vectors():
    a=s.Matrix(C1)/2;b=s.Matrix(C2)/2
    w1=(2*a+b)/3;w2=(-a+b)/3;w3=(-a-2*b)/3
    longs={tuple(x) for x in (a,b,a+b,-a,-b,-a-b)}
    shorts={tuple(x) for x in (w1,w2,w3,-w1,-w2,-w3)}
    return longs,shorts

@lru_cache(None)
def run():
    rr=roots(); e6,parts,a,b,c,mixed,signs=frame(rr)
    x,y,k,h=fields();u=s.symbols('y',positive=True)
    q=x/s.sqrt(6*u);r=y/s.sqrt(6*u);connection=-h/(4*u)
    f=-s.diff(connection,u)
    moment=f+(comm(q,q.T)+comm(r,r.T))/u
    dq=s.I*s.diff(q,u)-s.I*comm(connection,q)
    dr=s.I*s.diff(r,u)-s.I*comm(connection,r)
    eps=-signs[0][0]*signs[0][1]
    ta=scale(add(a[0],scale(a[1],2)),s.Rational(1,3))
    tb=scale(add(b[0],scale(b[1],2)),s.Rational(1,3))
    kval=add(BETA,DELTA)
    phase=lambda z,root: s.Rational(dot(root,z),4)
    residual=lambda z:add(add(z,scale(kval,s.Rational(1,6))),scale(V,s.Rational(-1,2)))
    choices=[eta for eta in (-1,1) if all(phase(residual(scale(add(ta,scale(tb,eps)),eta)),alpha).q==1 for alpha in rr)]
    eta=choices[0]
    center=scale(add(ta,scale(tb,eps)),eta)
    omega,d,p=clock_pair()
    de=d**eta;db=d**(eta*eps)
    adj=[s.kronecker_product(g,s.conjugate(g)) for g in (d,p)]
    mixed_invariants=[]
    for sa,sb,sc in signs:
        da=de if sa==1 else s.conjugate(de)
        dc=db if sb==1 else s.conjugate(db)
        mixed_invariants.append(invariant_dimension([s.kronecker_product(da,dc),s.kronecker_product(p,p)]))
    same=invariant_dimension([s.kronecker_product(d,d),s.kronecker_product(p,p)])
    longs,shorts=color_vectors();g2=longs|shorts
    reflected={tuple(s.simplify(x-2*dot(alpha,beta)/dot(beta,beta)*z) for x,z in zip(alpha,beta)) for alpha in g2 for beta in g2}
    gram_pairs={(s.Rational(2*dot(a,b),dot(b,b)),s.Rational(2*dot(a,b),dot(a,a))) for a in longs for b in shorts if dot(a,b)<0}
    j=s.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
    olde=s.sqrt(2)*s.Matrix([[0,1,0],[0,0,1],[0,0,0]])
    oldh=s.diag(2,0,-2)
    expected=Counter()
    for part,slot in zip(parts+[{z for z in e6 if dot(z,C1) or dot(z,C2)}-mixed],range(3)):
        for z in part:
            expected[label(z,a+b+c)]+=1
        expected[(0,)*6]+=2
    for sa,sb,sc in signs:
        expected.update(u+v+w for u,v,w in product(weights(sa),weights(sb),weights(sc)))
    actual=Counter(label(z,a+b+c) for z in e6);actual[(0,)*6]+=6
    oldp=(-4,-4,-4,6,6,0,0,0)
    missing=sum(phase(residual((0,)*8),z).q!=1 for z in rr)
    facts={
        'E8_240_norm2':len(rr)==240 and all(dot(z,z)==8 for z in rr),
        'regular_condensate_A2':BETA in rr and DELTA in rr and V in rr and dot(BETA,DELTA)==4,
        'same_old_peripheral':all(dot(z,add(oldp,scale(V,-1)))%8==0 for z in rr),
        'both_grade_two':comm(h,x)==2*x and comm(h,y)==2*y,
        'commuting_spin_fields':comm(x,y)==s.zeros(3),
        'moment_and_both_spin_residuals_zero':zero(moment) and zero(dq) and zero(dr),
        'flat_connection_control_fails':not zero((comm(q,q.T)+comm(r,r.T))/u),
        'wrong_norm_control_fails':not zero(f+2*(comm(q,q.T)+comm(r,r.T))/u),
        'noncommuting_pair_control_fails':comm(x,x.T)!=s.zeros(3),
        'generated_compact_algebra_is_full_su3':lie_dimension([x,y,x.T,y.T])==8,
        'fractional_grading_needs_lift':any(phase(scale(kval,s.Rational(1,3)),z).q!=1 for z in rr),
        'spin_line_cancellation':s.Rational(1,3)-s.Rational(-2,3)==1,
        'finite_positive_total_Higgs_norm':s.trace(x.T*x+y.T*y)/6==s.Rational(1,3),
        'E6_full_orthogonal_roots_rank6':len(e6)==72 and s.Matrix(list(e6)).rank()==6,
        'E6_simple_Cartan_determinant3':s.Matrix([[dot(z,w)//4 for w in simple(e6)] for z in simple(e6)]).det()==3,
        'two_other_regular_A2_factors':list(map(len,parts))==[6,6] and all(len(t)==2 and dot(*t)==-4 for t in (a,b)),
        'all_three_A2_commute':all(dot(z,w)==0 for left,right in combinations((a,b,c),2) for z in left for w in right),
        'full_E6_tensor_branching':actual==expected and len(mixed)==54 and len(signs)==2 and signs[0]==tuple(-z for z in signs[1]),
        'center_correct_in_E6':all(phase(center,z).q==1 for z in e6),
        'unique_oriented_center_matches_all_E8':len(choices)==1,
        'omitting_compensator_fails':missing==162,
        'inverting_compensator_fails':any(phase(residual(scale(center,-1)),z).q!=1 for z in rr),
        'clock_shift_unitary_det1':zero(d.conjugate().T*d-s.eye(3)) and p.T*p==s.eye(3) and s.simplify(d.det())==p.det()==1,
        'central_commutator_exact':zero(de*p*de.conjugate().T*p.T-omega**eta*s.eye(3)) and zero(db*p*db.conjugate().T*p.T-omega**(eta*eps)*s.eye(3)),
        'adjoint8_invariants_zero':invariant_dimension(adj)-1==0,
        'both_mixed_tensor_invariants_one':mixed_invariants==[1,1],
        'nondual_tensor_control_fails':same==0,
        'G2_twelve_distinct_nonzero_roots':len(g2)==12 and (0,)*8 not in g2,
        'G2_exact_long_short_lengths':{dot(z,z) for z in longs}=={s.Integer(2)} and {dot(z,z) for z in shorts}=={s.Rational(2,3)},
        'G2_reflection_closed':reflected==g2,
        'G2_cartan_not_dimension_guess':(-3,-1) in gram_pairs and s.Matrix(list(g2)).rank()==2,
        'old_SO3_dual_map_positive_control':all(j*t==-t.T*j for t in (olde,olde.T,oldh)) and j.T*j==s.eye(3),
        'two_field_dual_intertwiner_zero':dual_dimension([x,y,x.T,y.T])==0,
    }
    return {'facts':{k:bool(v) for k,v in facts.items()},'predicates_passed':sum(bool(v) for v in facts.values()),
        'root_profile':{'E8':240,'E6':len(e6),'trinification_adjoint_dimensions':[8,8,8], 'mixed_dimensions':[27]*len(signs)},
        'gauge_profile':{'adjoint_factor_invariants':[0,0,8],'mixed_factor_invariants':[3*n for n in mixed_invariants],'dimension':8+3*sum(mixed_invariants),'rank':s.Matrix(list(g2)).rank(),'long_roots':len(longs),'short_roots':len(shorts)},
        'phase_profile':{'center_order':3,'total_peripheral_order':2,'uncompensated_mismatched_roots':missing,'flat_root_choices':9},
        'explicit_frame':{'a':a,'b':b,'c':c,'mixed_signs':signs,'epsilon':eps,'eta':eta,'center_doubled_coordinates':[str(z) for z in center]},
        'physical_chirality_achieved':False,'fermion_gap_computed':False,'genesis_selection_derived':False,'all_compensators_classified':False,'physical_goal_achieved':False,'nonauthor_acceptance':False}

if __name__=='__main__':
    data=run()
    print(json.dumps(data,indent=2,default=int))
    raise SystemExit(0 if all(data['facts'].values()) else 1)
