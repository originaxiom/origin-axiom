"""Exact full-root SM phase, coupled gap and parallel-pair ingredients."""
from collections import Counter
from functools import lru_cache
from itertools import combinations,product
import importlib.util
import json
from pathlib import Path
import sympy as s

def prior(name):
    path=Path(__file__).resolve().parent.parent/'weave_graded_condensate_2026_10_08'/(name+'.py')
    spec=importlib.util.spec_from_file_location('sm_parallel_prior_'+name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

old=prior('probe')
Q=s.Rational
W=(0,0,0,-1,1,-2,0,2)
V=(0,0,0,1,-1,0,0,0)
T=(5,5,5,-3,-3,-3,-3,-3)
C1=(1,-1,0,0,0,0,0,0)
C2=(0,1,-1,0,0,0,0,0)
WEAK=(Q(1,2),)*8

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(a,c): return tuple(c*x for x in a)
def neg(a): return scale(a,-1)
def roots(): return {tuple(Q(x,2) for x in a) for a in old.roots()}
def comm(a,b): return a*b-b*a
def zero(a): return all(s.simplify(x)==0 for x in a)
def basis(i): return tuple(int(k==i) for k in range(8))
def proj_b(a):
    mean=sum(a[3:])/5
    return (0,0,0)+tuple(x-mean for x in a[3:])
def proj_g(a): return add(a,neg(proj_b(a)))
def simple(rr):
    pos={r for r in rr if r>(0,)*8}
    return sorted(r for r in pos if not any(add(r,neg(a)) in pos for a in pos))

def frame():
    rr=roots();z=(0,)*8
    rb={r for r in rr if proj_g(r)==z};rg={r for r in rr if proj_b(r)==z}
    fb=[proj_b(tuple(s.Integer(v) for v in basis(i))) for i in range(3,8)]
    gb={proj_g(r) for r in rr if proj_b(r)==add(fb[0],fb[1])}
    fg=sorted(neg(r) for r in gb)
    return rr,rb,rg,fb,fg

def triple():
    h=s.diag(-4,-2,0,2,4);e=s.zeros(5)
    for i in range(4): e[i+1,i]=s.sqrt((i+1)*(4-i))
    return h,e,e.T

def wedge_lie(a):
    pairs=list(combinations(range(a.rows),2));out=s.zeros(len(pairs))
    for col,(i,j) in enumerate(pairs):
        for k in range(a.rows):
            if k!=j:
                row=pairs.index(tuple(sorted((k,j))))
                out[row,col]+=a[k,i]*(1 if k<j else -1)
            if k!=i:
                row=pairs.index(tuple(sorted((i,k))))
                out[row,col]+=a[k,j]*(1 if i<k else -1)
    return out

def wedge_group(a):
    pairs=list(combinations(range(a.rows),2))
    return s.Matrix([[a[i,k]*a[j,l]-a[i,l]*a[j,k] for k,l in pairs] for i,j in pairs])

def compositions(n):
    if n==0:
        return [()]
    return [(k,)+rest for k in range(1,n+1) for rest in compositions(n-k)]

def grade_table():
    out=[]
    for ns in compositions(5):
        mean=Q(sum(i*n for i,n in enumerate(ns)),5)
        integral=mean.q==1
        minus=sum(n for i,n in enumerate(ns) if integral and (i-mean)%2)
        out.append({'multiplicities':list(ns),'mean':str(mean),'integral':integral,'negative_eigenvalues':int(minus) if integral else None})
    return out

def middle_pair():
    e=s.zeros(5);g=s.zeros(5)
    e[1,0]=e[4,1]=g[2,0]=g[4,2]=1
    return s.diag(-2,0,0,0,2),e,g,s.diag(1,1,1,-4,1)

def actual_branch(rr,rb,rg,fb,fg):
    z=(0,)*8;actual=Counter(proj_g(r)+proj_b(r) for r in rr);actual[z+z]+=8
    tenb={add(a,b) for a,b in combinations(fb,2)}
    teng={add(a,b) for a,b in combinations(fg,2)}
    want=Counter({z+z:8})
    want.update(a+z for a in rg);want.update(z+b for b in rb)
    for left,right in ((teng,fb),({neg(x) for x in teng},{neg(x) for x in fb}),({neg(x) for x in fg},tenb),(fg,{neg(x) for x in tenb})):
        want.update(a+b for a,b in product(left,right))
    return actual,want,tenb,teng

@lru_cache(None)
def run():
    rr,rb,rg,fb,fg=frame();actual,want,tenb,teng=actual_branch(rr,rb,rg,fb,fg)
    h,e,f=triple();y=s.symbols('y',positive=True);a=-h/(4*y);q=e/(2*s.sqrt(y))
    hw=Counter({0:8});hw.update(int(2*dot(r,W)) for r in rr)
    spins={j:hw[2*j]-hw[2*j+2] for j in range(5)}
    full,rhist=old.spectrum(spins)
    c_b=neg(fb[0]);c_g=neg(fg[0])
    kernel=[(i,j) for i,j in product(range(5),repeat=2) if all((dot(r,add(scale(c_g,i),scale(c_b,j)))).q==1 for r in rr)]
    kept={r for r in rg if dot(r,T)%7==0}
    zeroT={r for r in rr if dot(r,T)==0}
    smcentral={r for r in rr if all(dot(r,c)==0 for c in (C1,C2,WEAK,T))}
    charges10=Counter(int(dot(r,T)/2) for r in teng)
    chargesbar5=Counter(int(-dot(r,T)/2) for r in fg)
    j=s.zeros(5)
    for i in range(5): j[i,4-i]=(-1)**i
    j10=wedge_group(j)
    z=s.symbols('z',nonzero=True);transition=s.diag(*[z**i for i in range(-2,3)])
    hm,em,gm,extra=middle_pair();null=s.Matrix([0,0,0,1,0])
    alpha=Q(3,5);beta=4*s.I/5
    rotate=s.Matrix([[s.conjugate(alpha),s.conjugate(beta)],[-beta,alpha]])
    er,gr=alpha*e,beta*e
    table=grade_table();allowed=[r['multiplicities'] for r in table if r['integral'] and r['negative_eigenvalues']==2]
    four=(0,0,0,-1,-1,0,1,1)
    fix2=8+sum(dot(r,V)%2==0 for r in rr);fix4=8+sum(dot(r,four)%2==0 for r in rr)
    x,t=s.symbols('x t',real=True);bump=s.Function('chi')(x,t)
    ax=1-s.diff(x*bump,x);ay=-s.diff(x*bump,t)
    norms=s.symbols('u:4')
    moment=s.Matrix([-norms[0],norms[0]-norms[1],norms[1]-norms[2],norms[2]-norms[3],norms[3]])
    solved=s.solve(list(moment-s.Matrix([-4,-2,0,2,4])),norms)
    aa=s.Matrix(s.symbols('a:3'));bb=s.Matrix(s.symbols('b:3'))
    cross=aa.cross(bb)
    ea=s.symbols('e:4');ga=s.symbols('g:4');ee=s.zeros(5);gg=s.zeros(5)
    for i in range(4): ee[i+1,i]=ea[i];gg[i+1,i]=ga[i]
    com=comm(ee,gg)
    bound=max(abs(m+1+sign) for jj in range(5) for m in range(-jj-1,jj+1) for sign in (-1,1))
    ssg=simple(rg);ssb=simple(rb)
    facts={
        'entire_root_system':len(rr)==240 and all(dot(r,r)==2 for r in rr),
        'two_actual_A4_systems':len(rg)==len(rb)==20 and all(len(ss)==4 and s.Matrix([[dot(a,b) for a in ss] for b in ss]).det()==5 for ss in (ssg,ssb)),
        'defining_weights_faithful':len(fg)==5 and {add(a,neg(b)) for a,b in product(fg,repeat=2) if a!=b}==rg and all(dot(a,b)==Q(4,5) if a==b else dot(a,b)==Q(-1,5) for a,b in product(fg,repeat=2)),
        'entire248_branching_including_bars':actual==want and sum(actual.values())==248,
        'correct_central_quotient':kernel==[(i,(-2*i)%5) for i in range(5)],
        'individual_gauge_SU5_faithful':all(any(dot(r,scale(c_g,i)).q!=1 for r in rr) for i in range(1,5)),
        'bundle_center_equals_gauge_Y':all(dot(r,add(c_b,scale(T,Q(-1,10)))).q==1 for r in rr),
        'full_SM_centralizer_roots':smcentral==rb,
        'torus_centralizer_has_no_mixed_roots':zeroT==rb|kept and len(zeroT)==28,
        'weak_color_Y_embedding':WEAK in rg and all(dot(WEAK,c)==0 for c in (C1,C2,T)) and dot(C1,C2)==-1,
        'gauge_five_Y_eigenblocks':Counter(dot(r,T) for r in fg)==Counter({-4:3,6:2}),
        'actual_SM_root_system':len(kept)==8 and sum(dot(r,r)==2 for r in kept)==8 and len({r for r in kept if dot(r,WEAK)!=0})==2,
        'central_holonomy_opposite_control':sum(dot(r,T)%5==0 for r in rg)+4==24,
        'SM_representation_labels_not_generations':charges10==Counter({-4:3,1:6,6:1}) and chargesbar5==Counter({2:3,-3:2}),
        'six_distinct_global_kernel_roots':s.degree(z**6-1,z)==6 and s.gcd(z**6-1,6*z**5)==1,
        'compact_principal_triple':comm(h,e)==2*e and comm(e,f)==h,
        'root_chain_matches_cartan':all(dot(add(basis(j),neg(basis(i))),W)==1 for i,j in zip((5,3,6,4),(3,6,4,7))),
        'integral_spin_induction_and_old_p':all(dot(r,W).q==1 and dot(r,add(W,neg(V)))%2==0 for r in rr),
        'all_vacuum_residuals_zero':zero(s.I*s.diff(q,y)-s.I*comm(a,q)) and zero(-y*y*s.diff(a,y)+comm(e/2,f/2)),
        'wrong_amplitude_fails':not zero(-y*y*s.diff(a,y)+comm(e,f)),
        'finite_positive_norm':s.trace(f*e)==20 and s.trace(h*h)==40,
        'entire_sl2_decomposition':spins=={0:24,1:11,2:21,3:11,4:1} and sum((2*j+1)*n for j,n in spins.items())==248,
        'SU5_saturates_compact_commutant':spins[0]==len(rg)+4,
        'all_j_through4_blocks_squared':all(zero(b['square']-(b['xi']**2+b['threshold'])*s.eye(b['channels'])) for jj in range(5) for b in old.radial_blocks(jj)),
        'full_threshold_histogram':full=={'1/4':35,'5/4':22,'9/4':74,'13/4':42,'21/4':44,'25/4':25,'37/4':4,'41/4':2},
        'full_and_R_populations_distinct':sum(full.values())==248 and sum(rhist.values())==112,
        'essential_gap_lower_edge':min(Q(k) for k in full)==Q(1,4),
        'correct_angular_bound_not_old4':bound==6 and s.expand(x*x-6*x-(x*x/2-18)-(x-6)**2/2)==0,
        'five_dual_form_unitary':j.T*j==s.eye(5) and all(j*v==-v.T*j for v in (h,e,f)),
        'exterior_dual_form_unitary':j10.T*j10==s.eye(10) and all(j10*wedge_lie(v)==-wedge_lie(v).T*j10 for v in (h,e,f)),
        'dual_descends_through_spin_line':zero(j*transition-transition.inv().T*j),
        'generic_Wilson_literal_J_control_fails':not zero(j*(h+s.eye(5))+(h.T+s.eye(5))*j),
        'compact_support_representative_closed':s.simplify(s.diff(ay,x)-s.diff(ax,t))==0,
        'cutoff_without_exact_correction_fails':s.diff(1-bump,t)!=0,
        'all16_grade_compositions':len(table)==16 and len({tuple(r['multiplicities']) for r in table})==16,
        'two_allowed_old_p_grade_patterns':allowed==[[1,1,1,1,1],[1,3,1]],
        'wrong_involution_class_distinguished':fix2==136 and fix4==120,
        'nonproportional_middle_stationary_control':comm(hm,em)==2*em and comm(hm,gm)==2*gm and comm(em,gm)==s.zeros(5) and comm(em,em.T)+comm(gm,gm.T)==hm and s.Matrix.hstack(em.reshape(25,1),gm.reshape(25,1)).rank()==2,
        'middle_trivial_summand_and_extra_U1':all(v*null==s.zeros(5,1) for v in (em,gm,em.T,gm.T)) and all(comm(extra,v)==s.zeros(5) for v in (em,gm,hm)) and s.trace(extra)==0,
        'arbitrary_middle_two_column_rank_bound':s.simplify((aa.T*cross)[0])==s.simplify((bb.T*cross)[0])==0 and cross!=s.zeros(3,1),
        'all_edge_commutators_are_adjacent_minors':all(com[i,jj]==(ea[jj+1]*ga[jj]-ga[jj+1]*ea[jj] if i==jj+2 else 0) for i,jj in product(range(5),repeat=2)),
        'single_isotypic_type_prime_dimension':[(d,m) for d,m in product(range(1,6),repeat=2) if d*m==5]==[(1,5),(5,1)],
        'principal_edge_norms_forced':[solved[v] for v in norms]==[4,6,6,4],
        'actual_SU2_flavor_symmetry':zero(rotate.conjugate().T*rotate-s.eye(2)) and rotate.det()==1 and zero(rotate[0,0]*er+rotate[0,1]*gr-e) and zero(rotate[1,0]*er+rotate[1,1]*gr),
        'zero_field_flat_end_control':sum(dot(r,V)%2!=0 for r in rr)==112,
    }
    return dict(facts={k:bool(v) for k,v in facts.items()},predicates_passed=sum(bool(v) for v in facts.values()),
        root_profile={'gauge_A4_roots':len(rg),'bundle_A4_roots':len(rb),'SM_roots':len(kept),'SM_dimension':len(kept)+4,'centralizer_SM_roots':len(smcentral),'center_kernel':[list(v) for v in kernel]},
        spectrum_profile={'spins':{str(j):n for j,n in spins.items()},'full':full,'R':rhist,'angular_bound':bound,'essential_square_edge':'1/4'},
        grade_profile={'compositions':table,'accepted':allowed,'old_involution_fixed_dimension':fix2,'four_minus_fixed_dimension':fix4,'principal_edge_norms':[int(solved[v]) for v in norms]},
        actual_zero_counts_computed=False,physical_chirality_achieved=False,genesis_selection_derived=False,all_parallel_frames_classified=False,physical_goal_achieved=False,nonauthor_acceptance=False)

if __name__=='__main__':
    data=run();print(json.dumps(data,indent=2,default=int))
    raise SystemExit(0 if all(data['facts'].values()) else 1)
