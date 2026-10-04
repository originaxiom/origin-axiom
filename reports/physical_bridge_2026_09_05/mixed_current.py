"""R91 exact existing E8 mixed current; no physical identification or PDE solver."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
import json
import sympy as s


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def neg(a):
    return tuple(-x for x in a)


def roots():
    rr=set()
    for i,j in combinations(range(8),2):
        for a,b in product((-2,2),repeat=2):
            v=[0]*8; v[i]=a; v[j]=b; rr.add(tuple(v))
    rr.update(v for v in product((-1,1),repeat=8) if v.count(-1)%2==0)
    return rr


def vector(i,j,sign=-1):
    return tuple(2*(int(k==i)+sign*int(k==j)) for k in range(8))


def bases():
    return ([vector(i,i+1) for i in range(4)],
            [vector(6,7),vector(5,6),vector(6,7,1),(-1,)*8])


def labels(r,basis):
    values=[dot(r,b) for b in basis]
    assert all(v%4==0 for v in values)
    return tuple(v//4 for v in values)


def weight(indices,n):
    c=Counter(indices)
    return tuple(c[i]-c[i+1] for i in range(n-1))


def exterior(n,k):
    return Counter(weight(i,n) for i in combinations(range(n),k))


def adjoint(n):
    out=Counter({(0,)*(n-1):n-1})
    for i,j in product(range(n),repeat=2):
        if i!=j:
            out[tuple(int(i==k)-int(j==k)-int(i==k+1)+int(j==k+1) for k in range(n-1))]+=1
    return out


def dual(c):
    return Counter({neg(w):m for w,m in c.items()})


def tensor3(a,b,c):
    return Counter({x+y+z:i*j*k for x,i in a.items() for y,j in b.items() for z,k in c.items()})


def geometry():
    rr=roots(); g,st=bases(); gw=weight((3,4),5)
    lookup={(labels(r,g),labels(r,st)):r for r in rr}
    r=[lookup[gw,weight((i,),5)] for i in range(5)]
    a5=st+[r[4]]; a2=g[:2]; a1=[g[3]]
    cartan=lambda basis:[[dot(x,y)//4 for y in basis] for x in basis]
    chain=lambda n:[[2*int(i==j)-int(abs(i-j)==1) for j in range(n)] for i in range(n)]
    center={v for v in rr if all(dot(v,b)==0 for b in a2+a1)}
    mr={(i,5):r[i] for i in range(5)}
    mr.update({(5,i):neg(r[i]) for i in range(5)})
    mr.update({(i,j):add(r[i],neg(r[j])) for i,j in product(range(5),repeat=2) if i!=j})
    y=(-2,-2,-2,3,3,0,0,0)
    t=tuple(sum(Q(j+1,2)*st[j][k] for j in range(4)) for k in range(8))
    u=tuple(sum(Q((3,2,1,0)[j],2)*st[j][k] for j in range(4)) for k in range(8))
    reflection=lambda v:tuple(v[k]-Q(dot(v,r[4]),4)*r[4][k] for k in range(8))
    yp=reflection(y); charge=lambda v,h:Q(dot(v,h),2)
    cy={v for v in center if charge(v,y)==0}; cp={v for v in center if charge(v,yp)==0}
    actual=Counter(labels(v,a5+a2+a1) for v in rr); actual[(0,)*8]+=8
    z6,z3,z2=Counter({(0,)*5:1}),Counter({(0,)*2:1}),Counter({(0,):1})
    f6,f3,f2=exterior(6,1),exterior(3,1),exterior(2,1)
    a15,a20=exterior(6,2),exterior(6,3)
    roster=(tensor3(adjoint(6),z3,z2)+tensor3(z6,adjoint(3),z2)+tensor3(z6,z3,adjoint(2))
            +tensor3(a20,z3,f2)+tensor3(a15,dual(f3),z2)+tensor3(dual(a15),f3,z2)
            +tensor3(f6,f3,f2)+tensor3(dual(f6),dual(f3),f2))
    original_fundamentals=roster-tensor3(f6,f3,f2)-tensor3(dual(f6),dual(f3),f2)
    original_fundamentals+=tensor3(dual(f6),f3,f2)+tensor3(f6,dual(f3),f2)
    wrong=roster-tensor3(a15,dual(f3),z2)-tensor3(dual(a15),f3,z2)
    wrong+=tensor3(a15,f3,z2)+tensor3(dual(a15),dual(f3),z2)
    swap=lambda i:5 if i==4 else 4 if i==5 else i
    active=[mr[i,j] for i,j in ((0,1),(1,2),(2,3),(3,5))]
    residual={v for v in rr if all(dot(v,b)==0 for b in active)}
    checks={
        'complete_E8_roots':len(rr)==240 and all(dot(v,v)==8 for v in rr),
        'A5_A2_A1_Cartans':cartan(a5)==chain(5) and cartan(a2)==chain(2) and cartan(a1)==chain(1),
        'factors_orthogonal':all(dot(a,b)==0 for left,right in ((a5,a2),(a5,a1),(a2,a1)) for a in left for b in right),
        'color_weak_commutant_A5':len(center)==30 and center==set(mr.values()),
        'matrix_root_bijection':len(mr)==len(set(mr.values()))==30 and set(mr.values())<=rr,
        'whole_248_branching':actual==roster and sum(actual.values())==248,
        'original_fundamental_orientation_rejected':sum(original_fundamentals.values())==248 and original_fundamentals!=actual,
        'wrong_bars_rejected_at_equal_dimension':sum(wrong.values())==248 and wrong!=actual,
        'omitted_Cartans_rejected':Counter(labels(v,a5+a2+a1) for v in rr)!=roster,
        'both_Y_commutants':len(cy)==len(cp)==20 and {reflection(v) for v in cy}==cp,
        'reflection_bijects_E8':{reflection(v) for v in rr}==rr and all(reflection(reflection(v))==v for v in rr),
        'reflection_fixes_color_weak':all(reflection(b)==b for b in a2+a1),
        'actual_Y_transport':yp==tuple(-(y[k]-6*t[k])/5 for k in range(8)),
        'matrix_root_transport':all(reflection(v)==mr[swap(i),swap(j)] for (i,j),v in mr.items()),
        'every_root_charge_transports':all(charge(reflection(v),yp)==charge(v,y) for v in rr),
        'charge_histogram_transports':Counter(charge(v,y) for v in rr)==Counter(charge(v,yp) for v in rr),
        'partial_relabel_rejected':charge(r[0],y)==6 and charge(r[0],yp)==0,
        'wrong_Y_mixing_rejected':charge(r[0],tuple(y[k]-5*t[k] for k in range(8)))!=0,
        'actual_mixed_T_charges':tuple(charge(v,t) for v in r)==(1,1,1,1,-4),
        'adjoint_trace_Y':sum(charge(v,y)**2 for v in rr)==60*30,
        'adjoint_trace_U':sum(charge(v,u)**2 for v in rr)==60*12,
        'full_fixture_commutant':len(residual)==20,
        'full_A5_removes_Y':len({v for v in rr if all(dot(v,b)==0 for b in a5)})==8,
    }
    return dict(checks=checks,roots=240,color_weak_commutant_dimension=35,
                ordinary_SM_commutant_dimension=25,fixture_unbroken_algebra_dimension=24,
                full_A5_unbroken_dimension=11,Y_transported=list(map(str,yp)))


def unit(i,j):
    m=s.zeros(6); m[i,j]=1; return m


def bracket(a,b):
    return (a*b-b*a).applyfunc(s.expand)


def norm(a):
    return s.trace(a*a.conjugate().T).expand()


def fixture():
    return [unit(0,5)+unit(5,i+1) for i in range(3)]


def lie_closure(seed):
    echelon={}; mats=[]
    def insert(m):
        v=[Q(str(x)) for x in list(m)]
        for p,b in sorted(echelon.items()):
            if v[p]:
                t=v[p]; v=[a-t*c for a,c in zip(v,b)]
        p=next((i for i,a in enumerate(v) if a),None)
        if p is None:
            return
        t=v[p]; v=[a/t for a in v]; echelon[p]=v; mats.append(s.Matrix(6,6,v))
    for m in seed:
        insert(m)
    cursor=0
    while cursor<len(mats):
        for m in mats[:cursor]:
            insert(bracket(mats[cursor],m))
        cursor+=1
    return mats


def block_current(c):
    b=c[:5,:5]; p=c[:5,5:]; q=c[5:,:5]; z=c[5,5]; adj=lambda m:m.conjugate().T
    top=bracket(b,adj(b))+p*adj(p)-adj(q)*q
    off=b*adj(q)+p*s.conjugate(z)-adj(b)*p-adj(q)*z
    return top.row_join(off).col_join(adj(off).row_join(q*adj(q)-adj(p)*p)).applyfunc(s.expand)


def current():
    cs=fixture(); j=sum((bracket(c,c.T) for c in cs),s.zeros(6))
    curv=[bracket(cs[i],cs[k]) for i,k in combinations(range(3),2)]
    target=s.diag(3,-1,-1,-1,0,0); y=s.diag(1,1,1,1,1,-5); t=s.diag(1,1,1,1,-4,0)
    yp=s.diag(1,1,1,1,-5,1); mats=lie_closure(cs+[c.T for c in cs]); projections=[]
    for k in range(1,4):
        xi=s.diag(*([4-k]*k+[-k]*(4-k)+[0,0])); projections.append(s.trace(xi*j))
    cx=s.Matrix(6,6,lambda i,k:((i+2*k)%5-2)+s.I*((2*i+k)%3-1)); cx[5,5]=-s.trace(cx[:5,:5])
    checks={
        'entire_mixed_current':j==target,
        'all_three_flag_projections':projections==[12,8,4],
        'gauge_moment_cancels':s.trace(y*j)==s.trace(t*j)==0,
        'ordinary_Y_still_broken':sum(norm(bracket(y,c)) for c in cs)==216,
        'transported_Y_preserved':all(bracket(yp,c)==s.zeros(6) for c in cs),
        'all_curvatures_retained':all(f!=s.zeros(6) for f in curv) and sum(norm(f) for f in curv)==6,
        'real_residual_retained':norm(j)==12 and norm(-j/2)==3,
        'full_star_Lie_closure':len(mats)==24 and all(s.trace(m)==0 and m[:,4]==s.zeros(6,1) and m[4,:]==s.zeros(1,6) for m in mats),
        'full_complex_block_identity':block_current(cx)==bracket(cx,cx.conjugate().T),
        'off_diagonal_not_free_to_drop':block_current(cx)[:5,5:]!=s.zeros(5,1),
        'same_action_potential':2*(sum(norm(f) for f in curv)+norm(-j/2))==18,
        'shifted_source_is_not_bare_zero':j!=s.zeros(6),
        'normal_commuting_opposite_control':all(bracket(a,b)==s.zeros(6) for a,b in product((y,t,yp),repeat=2)),
    }
    for a in (Q(1,2),Q(1),Q(2),Q(-1)):
        cc=[s.Rational(a.numerator,a.denominator)*c for c in cs]
        jj=sum((bracket(c,c.T) for c in cc),s.zeros(6))
        ff=[bracket(cc[i],cc[k]) for i,k in combinations(range(3),2)]
        v=2*(sum(norm(f) for f in ff)+norm(jj/2))
        checks['scaling_'+str(a)]=v==18*a**4 and 4*v/a!=0
    return dict(checks=checks,current_diagonal=list(map(str,j.diagonal())),
                flag_projections=list(map(str,projections)),curvature_norm='6',moment_norm='12',
                ordinary_Y_breaking_norm='216',homogeneous_potential_coefficient='18')


def run():
    rows=[geometry(),current()]
    for group,row in zip(('embedding_transport','mixed_current_action'),rows):
        for name,ok in row['checks'].items():
            print(json.dumps(dict(group=group,name=name,passed=bool(ok))),flush=True)
    failed=[name for row in rows for name,ok in row['checks'].items() if not ok]
    out=dict(total=sum(len(r['checks']) for r in rows),failed=failed,
             results=[{k:v for k,v in r.items() if k!='checks'} for r in rows],
             stationary_mixed_background_constructed=False,physical_chirality_derived=False,
             source_law_selected=False,full_goal_achieved=False)
    print(json.dumps(out,sort_keys=True),flush=True)
    assert not failed,failed
    return out


if __name__=='__main__':
    run()
