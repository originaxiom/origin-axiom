"""Separate Weyl, Fraction and polynomial module route; no native import."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations,product
import importlib.util
import json
from pathlib import Path

path=Path(__file__).resolve().parent.parent/'weave_graded_condensate_2026_10_08/reference.py'
spec=importlib.util.spec_from_file_location('sm_parallel_rational_prior',path)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def times(a,c): return tuple(c*x for x in a)
def pb(r):
    mean=sum(r[3:])/5
    return (F(0),)*3+tuple(x-mean for x in r[3:])
def pg(r): return plus(r,times(pb(r),-1))

def grade_table():
    rows=[]
    for cut in product((False,True),repeat=4):
        ns=[1]
        for take in cut:
            if take: ns.append(1)
            else: ns[-1]+=1
        mean=F(sum(i*n for i,n in enumerate(ns)),5)
        ok=mean.denominator==1
        rows.append({'multiplicities':ns,'mean':str(mean),'integral':ok,
                     'negative_eigenvalues':sum(n for i,n in enumerate(ns) if (i-mean)%2) if ok else None})
    return sorted(rows,key=lambda row:row['multiplicities'])

def rank(a):
    a=[list(map(F,row)) for row in a];n=0
    for j in range(len(a[0])):
        k=next((k for k in range(n,len(a)) if a[k][j]),None)
        if k is None:continue
        a[n],a[k]=a[k],a[n];q=a[n][j];a[n]=[x/q for x in a[n]]
        for k in range(len(a)):
            if k!=n:
                q=a[k][j];a[k]=[x-q*y for x,y in zip(a[k],a[n])]
        n+=1
        if n==len(a):break
    return n

@lru_cache(None)
def run():
    rr={tuple(F(x,2) for x in r) for r in old.weyl_roots()};zero=(F(0),)*8
    w=(0,0,0,-1,1,-2,0,2);v=(0,0,0,1,-1,0,0,0);t=(5,5,5,-3,-3,-3,-3,-3)
    rb={r for r in rr if pg(r)==zero};rg={r for r in rr if pb(r)==zero}
    fb=[pb(tuple(F(i==j) for i in range(8))) for j in range(3,8)]
    fg=sorted({times(pg(r),-1) for r in rr if pb(r)==plus(fb[0],fb[1])})
    cb=times(fb[0],-1);cg=times(fg[0],-1)
    kernel=[(i,j) for i,j in product(range(5),repeat=2) if all(dot(r,plus(times(cg,i),times(cb,j))).denominator==1 for r in rr)]
    c1=(1,-1,0,0,0,0,0,0);c2=(0,1,-1,0,0,0,0,0);weak=(F(1,2),)*8
    sm={r for r in rg if dot(r,t)%7==0}
    central={r for r in rr if all(dot(r,a)==0 for a in (c1,c2,weak,t))}
    # Strip highest weights, independent of adjacent-difference native.
    hw=Counter({0:8});hw.update(2*dot(r,w) for r in rr);left=hw.copy();spins=Counter()
    while any(left.values()):
        highest=max(k for k,n in left.items() if n)
        assert highest.denominator==1 and highest%2==0
        j=int(highest)//2;n=left[highest];spins[j]+=n
        for m in range(-j,j+1):
            left[2*m]-=n;assert left[2*m]>=0
    full=Counter();rhist=Counter();matrix_checks=[]
    for j,copies in spins.items():
        e,l,h,g=old.polynomial(2*j)
        for channels,threshold,c2m,c1m,c0,gram,m in old.blocks_from_polynomials(j):
            full[str(threshold)]+=channels*copies
            matrix_checks.append(c2m==old.diag([-F(1)]*channels) and c1m==old.diag([F(0)]*channels) and c0==old.diag([threshold]*channels))
        for k in range(2*j+1):
            m=j-k
            if m%2:
                norm=e[k-1][k]**2*g[k-1]/g[k] if k else F(0)
                rhist[str(F(m*m,4)+norm/2)]+=copies
    e,l,h,g=old.polynomial(4)
    # Bilinear invariant form in non-orthonormal monomial basis.
    jform=[[(-1)**i*g[i] if k==4-i else F(0) for k in range(5)] for i in range(5)]
    dual=[old.add(old.mul(jform,a),old.mul(old.transpose(a),jform))==old.diag([F(0)]*5) for a in (e,l,h)]
    isometry=old.mul(old.mul(old.transpose(jform),old.diag([1/x for x in g])),jform)==old.diag(g)
    table=grade_table();accepted=[a['multiplicities'] for a in table if a['integral'] and a['negative_eigenvalues']==2]
    wrong=(0,0,0,-1,-1,0,1,1)
    fix2=8+sum(dot(r,v)%2==0 for r in rr);fix4=8+sum(dot(r,wrong)%2==0 for r in rr)
    edge_norms=[-sum(range(-4,-4+2*(i+1),2)) for i in range(4)]
    teng={plus(a,b) for a,b in combinations(fg,2)}
    tenb={plus(a,b) for a,b in combinations(fb,2)}
    counted=Counter((pg(r),pb(r)) for r in rr);counted[(zero,zero)]+=8
    expected=Counter({(zero,zero):8});expected.update((a,zero) for a in rg);expected.update((zero,b) for b in rb)
    for ga,ba in ((teng,fb),([times(x,-1) for x in teng],[times(x,-1) for x in fb]),([times(x,-1) for x in fg],tenb),(fg,[times(x,-1) for x in tenb])):
        expected.update(product(ga,ba))
    facts={
        'Weyl_population_and_full_branching':len(rr)==240 and counted==expected,
        'two_A4_rank4_and_twenty_roots':len(rb)==len(rg)==20 and rank(list(rb))==rank(list(rg))==4,
        'defining_gauge_weight_differences':len(fg)==5 and {plus(a,times(b,-1)) for a,b in product(fg,repeat=2) if a!=b}==rg,
        'actual_joint_centre_kernel':kernel==[(i,(-2*i)%5) for i in range(5)],
        'bundle_centre_trade_to_Y':all(dot(r,plus(cb,times(t,F(-1,10)))).denominator==1 for r in rr),
        'SM_gauge_roots_and_full_centralizer':len(sm)==8 and central==rb,
        'central_Y_opposite_control':sum(dot(r,t)%5==0 for r in rg)==20,
        'actual_gauge_five_blocks':Counter(dot(a,t) for a in fg)==Counter({-4:3,6:2}),
        'principal_H_even_and_correct_periphery':all(dot(r,w).denominator==1 and dot(r,plus(w,times(v,-1)))%2==0 for r in rr),
        'all248_highest_weight_subtraction':dict(spins)=={4:1,3:11,2:21,1:11,0:24},
        'polynomial_spin2_triple':h==old.diag([F(4),F(2),F(0),F(-2),F(-4)]) and old.add(old.mul(e,l),old.scale(old.mul(l,e),-1))==h,
        'positive_spin2_norm20':sum(old.mul(l,e)[i][i] for i in range(5))==20,
        'every_weighted_adjoint_block':bool(matrix_checks) and all(matrix_checks),
        'exact_full_threshold_histogram':full==Counter({'1/4':35,'5/4':22,'9/4':74,'13/4':42,'21/4':44,'25/4':25,'37/4':4,'41/4':2}),
        'full248_R112_not_particles':sum(full.values())==248 and sum(rhist.values())==112,
        'smallest_threshold_positive':min(F(x) for x in full)==F(1,4),
        'polynomial_metric_dual_form':all(dual) and isometry and g==[F(1),F(1,4),F(1,6),F(1,4),F(1)],
        'six_is_angular_bound':max(abs(m+1+sigma) for j in spins for m in range(-j-1,j+1) for sigma in (-1,1))==6,
        'sixteen_cut_compositions_complete':len(table)==16 and len({tuple(x['multiplicities']) for x in table})==16,
        'old_p_selects_two_grade_patterns':accepted==[[1,1,1,1,1],[1,3,1]],
        'wrong_p_class_has_different_fixed_dimension':fix2==136 and fix4==120,
        'moment_forces_edge_norms':edge_norms==[4,6,6,4],
        'single_type_factorizations_of5':[(a,b) for a,b in product(range(1,6),repeat=2) if a*b==5]==[(1,5),(5,1)],
        'flat_spin_odd_control112':sum(dot(r,v)%2!=0 for r in rr)==112,
    }
    return dict(predicates=facts,predicates_passed=sum(facts.values()),
        root_profile={'gauge_A4_roots':len(rg),'bundle_A4_roots':len(rb),'SM_roots':len(sm),'SM_dimension':len(sm)+4,'centralizer_SM_roots':len(central),'center_kernel':[list(x) for x in kernel]},
        spectrum_profile={'spins':{str(j):n for j,n in spins.items()},'full':dict(full),'R':dict(rhist),'angular_bound':6,'essential_square_edge':'1/4'},
        grade_profile={'compositions':table,'accepted':accepted,'old_involution_fixed_dimension':fix2,'four_minus_fixed_dimension':fix4,'principal_edge_norms':edge_norms})

if __name__=='__main__':
    data=run();print(json.dumps(data,indent=2))
    raise SystemExit(0 if all(data['predicates'].values()) else 1)
