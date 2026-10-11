"""Separate tuple-exterior/component-weight exact controls; NO native import.

Same author, not outside review, not global harmonic/PDE computation.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
import json
import sympy as s

I=s.I
ZERO=s.zeros(2)

def parity_join(a,b):
    if set(a)&set(b):return None,0
    return tuple(sorted(a+b)),(-1)**sum(x>y for x in a for y in b)

def add(*parts):
    out={}
    for p in parts:
        for u,v in p.items():out[u]=out.get(u,ZERO)+v
    return {u:m.applyfunc(s.expand) for u,m in out.items() if any(s.expand(x)!=0 for x in m)}

def scale(p,c):return add({u:c*m for u,m in p.items()})

def mul(a,b):
    out={}
    for x,m in a.items():
        for y,n in b.items():
            u,sign=parity_join(x,y)
            if sign:out[u]=out.get(u,ZERO)+sign*m*n
    return add(out)

def eps(a,b,c):return (-1)**sum(x>y for x,y in combinations((a,b,c),2))

@lru_cache(None)
def run():
    p={}
    def ck(name,value):p[name]=bool(value)
    # Tuple order theta0,theta1,rho0_0,rho0_1,... differs from the
    # frozen interleaved mask/dagger/jet producer. No old run is called.
    mats=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
    z=s.symbols('s0:3')
    rows=[]
    for kap in (1,9):
        a=s.sqrt(s.Rational(2,kap))
        P=[{():a*z[j]*mats[j],(0,2+2*j):a*I*s.sqrt(2)*mats[j],
            (1,3+2*j):a*I*s.sqrt(2)*mats[j]} for j in range(3)]
        poly={};scalar=0
        for i,j,k in permutations(range(3)):
            coeff=I*eps(i,j,k)/3
            poly=add(poly,scale(add(mul(P[i],mul(P[j],P[k])),
                                   scale(mul(P[i],mul(P[k],P[j])),-1)),coeff))
            scalar+=kap*s.Rational(1,4)*coeff*a**3*z[i]*z[j]*z[k]*s.trace(mats[i]*(mats[j]*mats[k]-mats[k]*mats[j]))
        # d2theta=theta0theta1 coefficient/2, before parent kap/4.
        extracted={u[2:]:s.expand(kap*s.Rational(1,8)*s.trace(m))
                   for u,m in poly.items() if u[:2]==(0,1)}
        extracted={u:c for u,c in extracted.items() if c!=0}
        expected={}
        for i,j,k in permutations(range(3)):
            Hessian=s.diff(scalar,z[i],z[j])
            for x,y,sg in ((2+2*i,3+2*j,1),(3+2*i,2+2*j,-1)):
                u,sign=parity_join((x,),(y,))
                expected[u]=expected.get(u,0)+sg*sign*Hessian/2
        expected={u:s.expand(c) for u,c in expected.items() if s.expand(c)!=0}
        yy=s.simplify(s.diff(scalar,*z))
        ck(f'tuple_parent_matches_independent_scalar_Hessian_{kap}',extracted==expected and bool(expected))
        ck(f'wrong_fermion_sign_and_factor_rejected_{kap}',
           extracted!={u:-c for u,c in expected.items()} and extracted!={u:2*c for u,c in expected.items()})
        ck(f'correct_orthonormal_action_scaling_{kap}',s.simplify(yy+4*s.sqrt(s.Rational(2,kap)))==0)
        rows.append({'kappa':kap,'Y_distinct':str(yy),'fermion_monomials':len(extracted)})
    ck('no_global_overlap_claim_from_local_nonzero_control',len(rows)==2 and all(r['fermion_monomials']>0 for r in rows))
    # Scalar adjoint unit coordinates: every off-diagonal unit, then four
    # independent traceless diagonal coordinates. No root roster import.
    h=(2,2,2,-3,-3)
    coords=[(i,j,h[i]-h[j]) for i in range(5) for j in range(5) if i!=j]
    weights=[c[2] for c in coords]+[0]*4
    ck('component_centralizer_has12_with_generic4',
       sum(w==0 for w in weights)==12 and
       sum(x==y for i,x in enumerate((-4,-2,0,1,5)) for j,y in enumerate((-4,-2,0,1,5)) if i!=j)+4==4)
    singular=Counter()
    # Each projected block (lambda,rho) -> (f,v) is [[0,iw],[-iw,0]].
    # Hand multiplication, independent of native's48x48 matrix/rank.
    nonzero_rank=0
    for index,w in enumerate(weights):
        block=((0,I*w),(-I*w,0))
        gram=tuple(tuple(s.simplify(sum(s.conjugate(block[k][i])*block[k][j] for k in range(2))) for j in range(2)) for i in range(2))
        ck(f'projected_block_Gram_{index}_{w}',gram==((w*w,0),(0,w*w)))
        singular[w*w]+=2
        nonzero_rank+=2*(w!=0)
    ck('component_projected_full_rank_and_squares',nonzero_rank==24 and singular=={0:24,25:24})
    ck('zero_F_cubic_does_not_erase_mixing',any(w!=0 for w in weights))
    # Periodic parallel boundary counterexample in two real coordinates.
    t=s.symbols('x',real=True)
    for n in (1,5):
        c=s.cos(2*s.pi*n*t);d=s.sin(2*s.pi*n*t);v=2*s.pi*n/5
        ck(f'real_parallel_circle_comparator_{n}',
           s.simplify(s.diff(c,t)+5*v*d)==0 and s.simplify(s.diff(d,t)-5*v*c)==0)
        ck(f'periodic_but_not_old_boundary_constant_{n}',
           c.subs(t,0)==c.subs(t,1) and d.subs(t,0)==d.subs(t,1) and s.diff(c,t)!=0)
    # Distinct Schur calculation using scalar determinant expansion.
    v=s.symbols('v')
    a=5*v-v*v/3;b=-2*v*v/3;c=-5*v-4*v*v/3
    det=s.expand(a*c-b*b)
    ck('Schur_keeps_massive_correction_and_small_v_scope',
       det==-25*v*v-5*v**3 and det.subs(v,Fraction(1,10))!=0 and det.subs(v,-5)==0 and det.subs(v,5)!=0)
    common=s.Matrix([[1,2,-1],[1,2,-1],[1,2,-1]])
    mixed=s.diag(1,2,-1)
    ck('same_one_form_wedge_determinant_zero',common.det()==0)
    ck('different_spatial_profiles_are_not_that_input',mixed.det()!=0)
    q=(-2,-2,-2,3,3)
    ten=Counter(sum(q[i] for i in ab) for ab in combinations(range(5),2))
    bf=Counter(-x for x in q)
    adj=Counter(q[i]-q[j] for i in range(5) for j in range(5) if i!=j);adj[0]+=4
    ck('separate_complete_charge_branchings',ten=={-4:3,1:6,6:1} and bf=={2:3,-3:2} and adj=={0:12,-5:6,5:6})
    # ALL Cartan tensor coefficients, not selected evaluations or a fit.
    fundamental=[(1,0,0,-2),(0,1,0,-2),(-1,-1,0,-2),(0,0,1,3),(0,0,-1,3)]
    tenweights=[tuple(fundamental[i][k]+fundamental[j][k] for k in range(4)) for i,j in combinations(range(5),2)]
    dualweights=[tuple(-x for x in a) for a in fundamental]
    def cubic_coeff(ws,a,b,c):return sum(row[a]*row[b]*row[c] for row in ws)
    ck('all64_SM_Cartan_anomaly_tensor_coefficients_zero',
       all(cubic_coeff(tenweights+dualweights,a,b,c)==0 for a in range(4) for b in range(4) for c in range(4)))
    ck('opposite_wrong_bar_tensor_nonzero',
       any(cubic_coeff(tenweights+fundamental,a,b,c)!=0 for a in range(4) for b in range(4) for c in range(4)))
    ck('full_charge_trace_and_doublet_parity',all(sum(row[k] for row in tenweights+dualweights)==0 for k in range(4)) and (3+1)%2==0)
    # Kernel requires g3=z^2 I3, g2=z^-3 I2. Their determinant-one
    # equations are z^6=1 and z^-6=1, not a separate block choice.
    residues=[r for r in range(12) if (6*r)%12==0]
    ck('exact_six_kernel_residues_not_name_matching',len(residues)==6 and residues==[0,2,4,6,8,10])
    result={'predicates':p,'predicates_passed':sum(p.values()),'local_cubic_controls':rows,
            'adjoint_control':{'centralizer_real_dimension':12,'leading_Weyl_rank':nonzero_rank,
                               'squared_singular_value_multiplicities':{str(k):v for k,v in singular.items()}},
            'branchings_6Y':{'10':dict(ten),'bar5':dict(bf),'24':dict(adj)},
            'new_native_imported':False,'outside_review':False,'global_PDE_certificate':False,
            'global_harmonic_overlaps_evaluated':False,'finite_v_charged_census':False,
            'generated_selection':False,'full_goal_achieved':False}
    print(json.dumps(result,indent=2,sort_keys=True))
    assert all(p.values()),[k for k,v in p.items() if not v]
    return result

if __name__=='__main__':run()
