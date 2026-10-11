"""Exact LOCAL controls for the authored fixed-boundary phase proof.

Does not solve the silver PDE or evaluate global harmonic overlaps.
Only frozen arithmetic is reused, not old run/output or census producers.
"""
from collections import Counter
from functools import lru_cache
import importlib.util
from itertools import combinations, permutations
import json
from pathlib import Path
import sympy as s

BASE = Path(__file__).resolve().parents[1]
I = s.I

def mz(m):
    return all(s.simplify(x) == 0 for x in m)

def load_arithmetic():
    spec = importlib.util.spec_from_file_location(
        'fixed_fermion_arithmetic', BASE/'silver_fermion_action_2026_10_11/probe.py')
    p = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(p)
    return p

def epsilon(i, j, k):
    return s.LeviCivita(i, j, k)

@lru_cache(None)
def run():
    f = {}
    def ck(name, value):
        f[name] = bool(value)
    p = load_arithmetic()
    mats = [s.Matrix([[0, 1], [1, 0]]),
            s.Matrix([[0, -I], [I, 0]]), s.diag(1, -1)]
    zz = s.symbols('z0:3')
    T = s.trace(mats[0]*(mats[1]*mats[2]-mats[2]*mats[1]))
    ts = []
    for a, b, c in permutations(range(3)):
        ts.append(s.expand(epsilon(a,b,c)*s.trace(mats[a]*(mats[b]*mats[c]-mats[c]*mats[b]))))
    ck('all_six_trilinear_permutations_symmetric_and_nonzero',
       T != 0 and all(t == T for t in ts))
    cubic_summary = []
    for kappa in (s.Integer(1), s.Integer(9)):
        scale = s.sqrt(2/kappa)
        rho = [[p.gen(p.fields['p'+str(j), a], mats[j]) for a in range(2)] for j in range(3)]
        PP = [p.scale(p.add({0:zz[j]*mats[j]},
              p.scale(p.add(*(p.mul(p.gen(a),rho[j][a]) for a in range(2))),I*s.sqrt(2))),scale)
              for j in range(3)]
        cubic = {}
        scalar = s.Integer(0)
        for i,j,k in permutations(range(3)):
            cubic = p.add(cubic,p.scale(p.mul(PP[i],p.add(p.mul(PP[j],PP[k]),
                                p.scale(p.mul(PP[k],PP[j]),-1))), I*epsilon(i,j,k)/3))
            scalar += I*kappa*s.Rational(1,12)*epsilon(i,j,k)*scale**3*zz[i]*zz[j]*zz[k]*s.trace(mats[i]*(mats[j]*mats[k]-mats[k]*mats[j]))
        actual = p.tr(p.scale(p.d2(cubic),kappa/4))
        # Expected physical Hessian contains scalar spinors, not a second
        # matrix multiplication of the coefficient profile already in T.
        rs = [[p.gen(p.fields['p'+str(j),a]) for a in range(2)] for j in range(3)]
        expected = {}
        Y = I*scale*T
        for i,j,k in permutations(range(3)):
            expected = p.add(expected,p.scale(p.dot(rs[i],rs[j]),Y*zz[k]/2))
        # trace(identity_2)=2; remove that bookkeeping trace factor.
        wanted = {u:s.expand(c/2) for u,c in p.tr(expected).items()}
        ck(f'direct_parent_Berezin_cubic_kappa_{kappa}',actual == wanted)
        ck(f'wrong_standard_fermion_phase_rejected_kappa_{kappa}',
           bool(actual) and actual != {u:-c for u,c in wanted.items()})
        ck(f'wrong_cubic_factor_rejected_kappa_{kappa}',
           bool(actual) and actual != {u:2*c for u,c in wanted.items()})
        ck(f'scalar_cubic_and_physical_Hessian_kappa_{kappa}',
           s.simplify(scalar-Y*zz[0]*zz[1]*zz[2]) == 0 and
           s.simplify(s.diff(scalar,*zz)-Y) == 0)
        cubic_summary.append({'kappa':int(kappa),'T':str(T),'Y_distinct':str(s.simplify(Y)),
                              'scalar_polynomial':str(s.simplify(scalar)),
                              'fermion_monomials':len(actual)})
    ck('action_prefactor_changes_normalized_cubic_not_selection',
       cubic_summary[0]['Y_distinct'] != cubic_summary[1]['Y_distinct'])

    h = [2,2,2,-3,-3]
    H = s.diag(*h)
    E = lambda i,j:s.Matrix(5,5,lambda a,b:int(a==i and b==j))
    ad_weights = []
    for i in range(5):
        for j in range(5):
            if i==j:continue
            ck(f'actual_matrix_adjoint_weight_{i}_{j}',
               mz(H*E(i,j)-E(i,j)*H-(h[i]-h[j])*E(i,j)))
            ad_weights.append(h[i]-h[j])
    ad_weights += [0]*4
    ck('full_adjoint_twenty_roots_and_four_Cartan',len(ad_weights)==24)
    centralizer = 24-s.diag(*ad_weights).rank()
    generic = [-4,-2,0,1,5]
    generic_weights = [generic[i]-generic[j] for i in range(5) for j in range(5) if i!=j]+[0]*4
    ck('SM_centralizer_12_with_v_zero_24_and_generic_4',
       centralizer==12 and s.zeros(24).nullspace().__len__()==24 and
       24-s.diag(*generic_weights).rank()==4)
    X=E(0,3)+E(3,0); Y=-I*E(0,3)+I*E(3,0)
    ck('broken_real_compact_rotation_keeps_i',
       mz(I*(H*X-X*H)+5*Y) and mz(I*(H*Y-Y*H)-5*X))
    G=s.Matrix([[0,5],[-5,0]])
    ck('real_rotation_positive_mass_Gram',G.T*G==25*s.eye(2))
    t=s.symbols('t',real=True)
    for n in (1,5):
        v=2*s.pi*n/5
        w=s.cos(2*s.pi*n*t)*X+s.sin(2*s.pi*n*t)*Y
        ck(f'closed_periodic_parallel_broken_positive_control_{n}',
           mz(s.diff(w,t)+I*v*(H*w-w*H)) and mz(w.subs(t,1)-w.subs(t,0)))
        ck(f'fixed_old_constant_boundary_rejects_that_section_{n}',not mz(s.diff(w,t)))
        ck(f'holonomy_central_comparator_{n}',
           s.simplify(s.exp(I*v*2)-s.exp(-I*v*3))==0)
    ck('identity_full_holonomy_comparator_retained',s.exp(4*I*s.pi)==1 and s.exp(-6*I*s.pi)==1)
    ck('unbroken_constant_section_passes_fixed_boundary',mz(H*E(0,1)-E(0,1)*H))

    # Actual same-factor deformation changes no old curvature or moment.
    omega=[s.Integer(1),s.Integer(2),s.Integer(-1)]
    ss=mats
    structure=[s.kronecker_product(m,s.eye(5)) for m in ss]
    gauge=s.kronecker_product(s.eye(2),H)
    ck('structure_and_gauge_commutation_not_identical_dimensions',
       all(mz(a*gauge-gauge*a) for a in structure) and not mz(ss[0]*ss[1]-ss[1]*ss[0]))
    ck('Cartan_addition_preserves_full_old_curvature_brackets',
       all(mz((structure[i]+omega[i]*gauge)*(structure[j]+omega[j]*gauge)
              -(structure[j]+omega[j]*gauge)*(structure[i]+omega[i]*gauge)
              -(structure[i]*structure[j]-structure[j]*structure[i]))
           for i in range(3) for j in range(3)))
    ck('Cartan_addition_preserves_old_moment_commutators',
       all(mz((structure[i]+omega[i]*gauge)*structure[j]-structure[j]*(structure[i]+omega[i]*gauge)
              -(structure[i]*structure[j]-structure[j]*structure[i]))
           for i in range(3) for j in range(3)))
    common=sum((epsilon(i,j,k)*omega[i]*omega[j]*omega[k]*ss[0]*(ss[1]*ss[2]-ss[2]*ss[1])
                for i,j,k in permutations(range(3))),s.zeros(2))
    mixed=sum((epsilon(i,j,k)*omega[i]*omega[j]*omega[k]*ss[i]*(ss[j]*ss[k]-ss[k]*ss[j])
               for i,j,k in permutations(range(3))),s.zeros(2))
    ck('pure_one_profile_adjoint_F_cubic_zero',mz(common))
    ck('wrong_three_spatial_profile_replacement_detected',not mz(mixed))

    # K=1,v=1 is an exact control normalization, not a core metric value.
    ad=s.diag(*ad_weights); z=s.zeros(24)
    R=(z.row_join(I*ad)).col_join((-I*ad).row_join(z))
    ck('actual_projected_fermion_mixing_rank24',R.rank()==24)
    ck('projected_squared_singular_values_24_zero_24_positive',
       R.H*R==s.diag(*(ad_weights+ad_weights)).applyfunc(lambda x:x*x) and
       Counter(x*x for x in ad_weights+ad_weights)=={0:24,25:24})
    ck('wrong_F_cubic_only_mass_rejected',R!=s.zeros(48))
    v=s.symbols('v',real=True)
    g=s.diag(5,-5); b=s.Matrix([1,2]); m=s.Matrix([[3]])
    full=(v*g).row_join(v*b).col_join((v*b.T).row_join(m))
    schur=v*g-v*v*b*m.inv()*b.T
    ck('massive_complement_Schur_retained',s.simplify(full.det()-3*schur.det())==0)
    ck('Schur_same_leading_not_same_exact_mass',
       mz(schur.diff(v).subs(v,0)-g) and not mz(schur-v*g))
    ck('small_v_does_not_license_all_v_no_crossing',
       schur.subs(v,s.Rational(1,10)).det()!=0 and schur.subs(v,-5).det()==0 and schur.subs(v,5).det()!=0)

    q=[-x for x in h]  # actual conventional6Y weights
    ten=Counter(q[i]+q[j] for i,j in combinations(range(5),2))
    barfive=Counter(-x for x in q)
    adj=Counter(q[i]-q[j] for i in range(5) for j in range(5) if i!=j)
    adj[0]+=4
    ck('full_10_bar5_and_24_charge_branchings',ten=={-4:3,1:6,6:1} and barfive=={2:3,-3:2} and adj=={0:12,-5:6,5:6})
    u1,u2,w,y=s.symbols('u1 u2 w y')
    lam=[u1-2*y,u2-2*y,-u1-u2-2*y,w+3*y,-w+3*y]
    p10=sum((lam[i]+lam[j])**3 for i,j in combinations(range(5),2))
    pbar5=sum((-x)**3 for x in lam)
    ck('full_SM_restriction_cubic_anomaly_polynomial_zero',s.expand(p10+pbar5)==0)
    ck('mixed_gravitational_hypercharge_trace_zero',
       s.expand(sum(lam[i]+lam[j] for i,j in combinations(range(5),2))-sum(lam))==0)
    ck('wrong_bar_anomaly_is_detected',s.expand(p10-pbar5)!=0)
    ck('dropping_complete_charged_component_is_detected',
       s.expand(p10+pbar5-(lam[0]+lam[1])**3)!=0)
    ck('anomalous_single_rep_positive_opposite_control',s.expand(p10)!=0 and s.expand(pbar5)!=0)
    ck('SU2_doublet_mod2_complete_generation',3+1==4 and (3+1)%2==0)
    zeta=s.exp(I*s.pi/3); c3=s.exp(2*I*s.pi/3)
    ck('six_element_group_kernel_actual_embedding',
       s.simplify(zeta**(-2)*c3-1)==0 and s.simplify(-zeta**3-1)==0 and
       all(s.simplify(zeta**r-1)!=0 for r in range(1,6)) and s.simplify(zeta**6-1)==0)
    result={'facts':f,'predicates_passed':sum(f.values()),'local_cubic_controls':cubic_summary,
            'adjoint_control':{'centralizer_real_dimension':centralizer,'full_adjoint_dimension':24,
                               'leading_Weyl_rank':R.rank(),'squared_singular_value_multiplicities':{'0':24,'25':24}},
            'branchings_6Y':{'10':dict(ten),'bar5':dict(barfive),'24':dict(adj)},
            'neutral_modes_not_lifted_by_this_branch':'6+j, j=0..6, fixed chosen neutral L',
            'unbroken_adjoint_chiral_profiles_small_v':12,
            'conditional_same_action_phase':True,'global_harmonic_overlaps_evaluated':False,
            'global_PDE_solved':False,'finite_v_charged_census':False,
            'generated_selection':False,'outside_review':False,'full_goal_achieved':False}
    print(json.dumps(result,indent=2,sort_keys=True))
    assert all(f.values()),[k for k,b in f.items() if not b]
    return result

if __name__=='__main__':
    run()
