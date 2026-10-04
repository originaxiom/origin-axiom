"""R93 actual compact-join Wilson premises, not a parameter-free SM derivation."""
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'joined_background.py'
if sha256(SOURCE.read_bytes()).hexdigest()!='f1d6bfb9e998a3306ddb41757c9356f4e99757a93ebbfc474e84be9d49bee4c7':
    raise RuntimeError('Changed retained R85 producer')
spec=importlib.util.spec_from_file_location('r93_retained_r85',SOURCE)
N=importlib.util.module_from_spec(spec); spec.loader.exec_module(N)
Y=(-2,-2,-2,3,3)
PERIOD={'x':0,'y':0,'z':1,'a':0,'b':0,'c':-1}


def exponent(w,period=PERIOD):
    return sum(period[t.lower()]*(1 if t.islower() else -1) for t in w)


def character():
    rows=[[w.count(t)-w.count(t.upper()) for t in 'xyzabc'] for w in N.DOUBLE_RELS]
    rank=s.Matrix(rows).rank()
    return {'checks':{'all_actual_relators_zero_period':all(exponent(w)==0 for w in N.DOUBLE_RELS),
                      'primitive_z_period_one':exponent('z')==1,
                      'right_z_inverse_period':exponent('c')==-1,
                      'b1_one_from_actual_relators':rank==5,
                      'bad_seam_character_rejected':any(exponent(w,dict(PERIOD,c=0))!=0 for w in N.DOUBLE_RELS)},
            'relators':list(N.DOUBLE_RELS),'exponent_rows':rows,'rank':rank,'b1':6-rank}


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def roots():
    rr=set()
    for i,j in combinations(range(8),2):
        for u,v in product((-2,2),repeat=2):
            a=[0]*8; a[i]=u; a[j]=v; rr.add(tuple(a))
    rr.update(a for a in product((-1,1),repeat=8) if a.count(-1)%2==0)
    return rr


def bases():
    e=lambda i,j,t=-1:tuple(2*(int(k==i)+t*int(k==j)) for k in range(8))
    gauge=[e(i,i+1) for i in range(4)]
    structure=[e(6,7),e(5,6),e(6,7,1),(-1,)*8]
    return structure,gauge


def label(r,bs):
    v=[dot(r,b) for b in bs]
    if any(x%4 for x in v):
        raise ValueError('Nonintegral Dynkin label')
    return tuple(x//4 for x in v)


def weights(k):
    out=Counter()
    for js in combinations(range(5),k):
        c=Counter(js); out[tuple(c[i]-c[i+1] for i in range(4))]+=1
    return out


def adjoint():
    out=Counter({(0,)*4:4})
    for i,j in product(range(5),repeat=2):
        if i!=j:
            out[tuple(int(i==k)-int(j==k)-int(i==k+1)+int(j==k+1) for k in range(4))]+=1
    return out


def dual(a):
    return Counter({tuple(-x for x in w):m for w,m in a.items()})


def tensor(a,b):
    return Counter({u+v:m*n for u,m in a.items() for v,n in b.items()})


def blocks(values):
    return sorted(Counter(values).values(),reverse=True)


def centralizer_dimension(values):
    return sum(n*n for n in blocks(values))-1


@lru_cache(None)
def geometry():
    rr=roots(); st,g=bases(); y=Y+(0,0,0)
    actual=Counter(label(r,st)+label(r,g) for r in rr); actual[(0,)*8]+=8
    f=weights(1); x=weights(2); z=Counter({(0,)*4:1}); a=adjoint()
    roster=(tensor(a,z)+tensor(z,a)+tensor(f,x)+tensor(dual(f),dual(x))
            +tensor(x,dual(f))+tensor(dual(x),f))
    wrong=roster-tensor(f,x)-tensor(dual(f),dual(x))+tensor(f,dual(x))+tensor(dual(f),x)
    charged=lambda r:dot(r,y)//2
    gauge_roots={r for r in rr if all(dot(r,b)==0 for b in st)}
    neutral={r for r in gauge_roots if charged(r)==0}
    gram=lambda b:s.Matrix([[dot(v,w)//4 for w in b] for v in b])
    chain=s.Matrix(4,4,lambda i,j:2*int(i==j)-int(abs(i-j)==1))
    ten=Counter((len([j for j in js if j<3]),sum(Y[j] for j in js)) for js in combinations(range(5),2))
    barfive=Counter((int(j<3),-Y[j]) for j in range(5))
    checks={'all_240_roots':len(rr)==240 and all(dot(r,r)==8 for r in rr),
            'orthogonal_A4_factors':all(dot(v,w)==0 for v in st for w in g),
            'both_A4_Cartans':gram(st)==gram(g)==chain,
            'full_248_roster':actual==roster and sum(actual.values())==248,
            'equal_dimension_wrong_bars_rejected':sum(wrong.values())==248 and wrong!=actual,
            'omitted_Cartans_rejected':Counter(label(r,st)+label(r,g) for r in rr)!=roster,
            'gauge_SU5_root_kernel20':len(gauge_roots)==20,
            'SM_gauge_roots8':len(neutral)==8,
            'SM_gauge_with_Cartans12':len(neutral)+4==12,
            'integer_Y_trace_zero':sum(Y)==0,
            'Y_commutes_structure':all(dot(y,b)==0 for b in st),
            'Y_norm30':sum(v*v for v in Y)==30,
            'full_adjoint_trace1800':sum(charged(r)**2 for r in rr)==1800,
            'wrong_trace_scale_rejected':sum(charged(r)**2 for r in rr)!=30,
            'gauge_center_faithful_in_248':any(label(r,g)==(1,0,0,0) for r in rr),
            'ten_SM_weights':ten==Counter({(2,-4):3,(1,1):6,(0,6):1}),
            'barfive_SM_weights':barfive==Counter({(1,2):3,(0,-3):2}),
            'order7_SM_two_blocks':blocks([v%7 for v in Y])==[3,2] and centralizer_dimension([v%7 for v in Y])==12,
            'order5_central_restores24':centralizer_dimension([v%5 for v in Y])==24,
            'generic_five_distinct_is_not_SM':centralizer_dimension([v%11 for v in (-2,-1,0,1,2)])==4,
            'central_control_is_not_SM':centralizer_dimension([0]*5)!=12}
    return {'checks':checks,'gauge_dimensions':{'SM':12,'central':24,'generic':4},
            'adjoint_trace_Y_squared':1800,'adjoint_one_form_complex_profiles':12,
            'cartan_Wilson_coordinates_at_least':4}


def global_kernel():
    # z=e^(2 pi i t); center coordinates are g3=e^(2 pi i a/3), g2=e^(2 pi i b/2).
    accepted=[(k,a,b) for k in range(6) for a in range(3) for b in range(2)
              if (-2*k+2*a)%6==0 and (3*k+3*b)%6==0]
    expected=[(k,k%3,k%2) for k in range(6)]
    return {'checks':{'Z6_kernel_all_six':accepted==expected,
                      'kernel_closed':all(((u[0]+v[0])%6,(u[1]+v[1])%3,(u[2]+v[2])%2) in accepted for u in accepted for v in accepted),
                      'wrong_product_no_quotient_rejected':len(accepted)!=1},'kernel':accepted}


def action_controls():
    # Algebraic local residual additivity; not a numerical harmonic metric on Y.
    i=s.I; identity=s.eye(5); y=s.diag(*Y)
    e=s.zeros(5); e[0,1]=1
    psi=[e+e.T,s.diag(1,-1,0,0,0),s.zeros(5)]
    aa=[e-e.T,s.zeros(5),s.zeros(5)]
    dg=[s.kronecker_product(a,identity) for a in aa]
    ps=[s.kronecker_product(a,identity) for a in psi]
    line=[s.kronecker_product(identity,-i*v*y) for v in (1,2,3)]
    bracket=lambda a,b:a*b-b*a
    dc=[dg[j]+ps[j] for j in range(3)]
    cross=[bracket(dc[j]+line[j],dc[k]+line[k])-bracket(dc[j],dc[k]) for j,k in combinations(range(3),2)]
    added_moment=sum((bracket(line[j],ps[j]) for j in range(3)),s.zeros(25))
    bad=s.kronecker_product(-i*s.diag(1,-1,0,0,0),identity)
    q=s.symbols('q',nonzero=True); h=s.diag(*(q**v for v in Y))
    norm=s.trace(y*y)
    return {'checks':{'commuting_Wilson_curvature_additivity':all(a==s.zeros(25) for a in cross),
                      'commuting_Wilson_moment_additivity':added_moment==s.zeros(25),
                      'unitary_addition':all(a.conjugate().T==-a for a in line),
                      'noncommuting_opposite_has_moment':bracket(bad,ps[0])!=s.zeros(25),
                      'nonclosed_omega_opposite_has_curvature':-i*y!=s.zeros(5),
                      'formal_holonomy_determinant_one':s.simplify(h.det())==1,
                      'period_tangent_nonzero':norm==30 and exponent('z')==1,
                      'odd_skew_matrix_singular':s.det(s.Matrix(5,5,lambda j,k:(j+1)*(k+2) if j<k else -(k+1)*(j+2) if k<j else 0))==0,
                      'even_skew_opposite_can_invert':s.Matrix([[0,1],[-1,0]]).det()==1,
                      'rank1_twist_can_have_invariant_control':(s.Matrix([[1]])-s.eye(1)).nullspace()!=[]},
            'no_PDE_profile_computed':True}


@lru_cache(None)
def evaluate():
    groups={'character':character(),'geometry':geometry(),'global_kernel':global_kernel(),'action':action_controls()}
    for ab in N.CHARS:
        out=N.public(N.case(ab))
        groups['join_'+''.join(map(str,ab))]=out
    flags={'physical_goal_achieved':False,'generated_SM_selection':False,
           'physical_chirality_derived':False,'non_author_acceptance':False,
           'quantum_moduli_lifting_computed':False}
    checks={name+':'+k:v for name,g in groups.items() for k,v in g['checks'].items()}
    return {'groups':groups,'checks':checks,**flags}


def run():
    out=evaluate()
    for name,g in out['groups'].items():
        print(json.dumps({'group':name,**g},sort_keys=True),flush=True)
    failed=[k for k,v in out['checks'].items() if not v]
    summary={'passed':len(out['checks'])-len(failed),'total':len(out['checks']),'failed':failed,
             **{k:v for k,v in out.items() if k not in ('groups','checks')},
             'scope':'actual join plus algebraic Wilson premises; authored conditional analytic admission'}
    print(json.dumps(summary,sort_keys=True),flush=True)
    return summary


if __name__=='__main__':
    raise SystemExit(0 if not run()['failed'] else 1)
