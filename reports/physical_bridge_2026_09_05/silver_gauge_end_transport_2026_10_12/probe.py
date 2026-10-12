"""Exact actual-period and full normalized degree0–3 end controls.

No repository scientific producer imported. Conditional supplied end,
not a core PDE, physical particle census or generated vacuum selection.
"""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]

def mz(matrix):
    return all(s.simplify(v)==0 for v in matrix)

def exponent(word, generators):
    return [sum(1 if c==g else -1 if c==g.upper() else 0 for c in word)
            for g in generators]

def exterior(j):
    e=s.zeros(8)
    for mask in range(8):
        if not mask & (1<<j):
            e[mask|(1<<j),mask]=(-1)**((mask & ((1<<j)-1)).bit_count())
    return e

def compose(a,b,r):
    A,B=a; C,D=b
    return A*C,A*C.diff(r)+A*D+B*C,A*D.diff(r)+B*D

def full_operator(r,ell,mu,kx,ky,omit_weight=False):
    eps=[exterior(j) for j in range(3)]; ins=[x.T for x in eps]
    a=ell*s.exp(-r/ell);W=mu*s.exp(2*r/ell)
    g=s.diag(*[(1-(mask&6).bit_count())/ell for mask in range(8)])
    if omit_weight:g=s.zeros(8)
    d=(eps[0],eps[0]*(g+W*s.eye(8))+s.I*kx/a*eps[1]+s.I*ky/a*eps[2])
    adj=(-ins[0],(g+W*s.eye(8))*ins[0]-s.I*kx/a*ins[1]-s.I*ky/a*ins[2])
    q=(d[0]+adj[0],d[1]+adj[1])
    return d,adj,q,compose(q,q,r)

def run():
    facts={}
    def ck(name,value):
        facts[name]=bool(value)
        if not facts[name]:raise AssertionError(name)
    inputs=json.loads((HERE/'INPUTS.json').read_text())
    candidate=json.loads((REPO/inputs['candidate_path']).read_text())
    gen=candidate['generators']
    R=s.Matrix([exponent(w,gen) for w in candidate['relators']])
    P=s.Matrix([exponent(w,gen) for w in candidate['cusp_words']])
    ker=R.nullspace()
    ck('actual_real_period_kernel',len(ker)==1 and ker[0]==s.Matrix([0,0,1]))
    ck('actual_peripheral_period_map',P*ker[0]==s.Matrix([0,1]))
    ck('not_two_independently_chosen_periods',R.rank()==2 and P[:,0]!=s.zeros(2,1))
    h=inputs['gauge_H']; ten=[h[i]+h[j] for i,j in combinations(range(5),2)]
    adj=[h[i]-h[j] for i in range(5) for j in range(5) if i!=j]+[0]*4
    ck('actual_10_weights_not_fundamental',Counter(ten)=={4:3,-1:6,-6:1})
    ck('actual_adjoint_zero_weights_retained',Counter(adj)=={0:12,5:6,-5:6})
    z=s.symbols('z',nonzero=True)
    hol=s.diag(*(z**w for w in ten))
    ck('generic_10_has_no_D0_trivial_coefficient',(hol-s.eye(10)).rank()==10)
    ck('identity_10_control_retains_all',(hol-s.eye(10)).subs(z,1)==s.zeros(10))
    ck('minus_one_phase_keeps_actual_four',(hol-s.eye(10)).subs(z,-1).rank()==6)
    # z primitive fifth root: all fundamental phases equal; Lambda2 phase is not1.
    ck('central_5_phase_is_not_trivial_matter',all(w%5==4 for w in ten) and all(w%5==0 for w in adj))
    lattice=s.Matrix([[-s.Rational(6,5),-s.Rational(2,5)],[s.Rational(2,5),s.Rational(4,5)]])
    dual=lattice.T.inv()*s.Matrix([0,1])
    ck('actual_inverse_lattice_one_form',dual==s.Matrix([s.Rational(1,2),s.Rational(3,2)]))
    ck('actual_inverse_lattice_squared_norm',(dual.T*dual)[0]==s.Rational(5,2))
    ck('wrong_same_period_assignment_detected',lattice.T*dual!=s.Matrix([1,1]))

    r,ell,mu,kx,ky=s.symbols('r ell mu kx ky',real=True)
    b0,theta=s.symbols('b0 theta',real=True)
    end=json.loads((REPO/inputs['end_matrices_path']).read_text())
    Cs=[s.Matrix([[s.sympify(v,locals={'r':r,'ell':ell,'b0':b0}) for v in row] for row in M]) for M in end['five_connection']]
    gauge=s.kronecker_product(s.diag(*ten),s.eye(5))
    structure=[s.kronecker_product(s.eye(10),C) for C in Cs]
    additions=[s.zeros(50),s.I*theta*dual[0]*gauge,s.I*theta*dual[1]*gauge]
    ck('actual_commuting_gauge_addition_retains_curvature_brackets',
       all(mz((structure[i]+additions[i])*(structure[j]+additions[j])-(structure[j]+additions[j])*(structure[i]+additions[i])
              -(structure[i]*structure[j]-structure[j]*structure[i])) for i,j in combinations(range(3),2)))
    ck('gauge_addition_is_antihermitian',all(mz(A.H+A) for A in additions))
    ck('actual_moment_addition_commutes_with_full_structure_Psi',
       all(mz(A*(C+C.H)-(C+C.H)*A) for A in additions for C in structure))
    W=mu*s.exp(2*r/ell);a=ell*s.exp(-r/ell);L2=(kx*kx+ky*ky)/a**2
    d,adjop,q,square=full_operator(r,ell,mu,kx,ky)
    ck('full_degrees_1_3_3_1',Counter(mask.bit_count() for mask in range(8))=={0:1,1:3,2:3,3:1})
    ck('normalized_flat_d_squared_zero',all(mz(v) for v in compose(d,d,r)))
    ck('normalized_adjoint_squared_zero',all(mz(v) for v in compose(adjop,adjop,r)))
    ck('Q_formal_selfadjoint',mz(q[0].H+q[0]) and mz(q[1].H-q[1]))
    ck('Q_square_second_derivative_minus_identity',square[0]==-s.eye(8))
    ck('Q_square_first_derivative_zero',mz(square[1]))
    V=square[2].applyfunc(s.simplify)
    ck('Q_square_preserves_every_degree',all(V[i,j]==0 for i in range(8) for j in range(8) if i.bit_count()!=j.bit_count()))
    ck('scalar_and_top_potential',s.simplify(V[0,0]-(W*W+ell**-2+L2))==0 and s.simplify(V[7,7]-V[0,0])==0)
    expected=s.Matrix([[(W+1/ell)**2+s.diff(W,r)+L2,-2*s.I*kx/(ell*a),-2*s.I*ky/(ell*a)],
                       [2*s.I*kx/(ell*a),W*W-s.diff(W,r)+L2,0],
                       [2*s.I*ky/(ell*a),0,W*W-s.diff(W,r)+L2]])
    ck('complete_one_form_matrix',mz(V.extract([1,2,4],[1,2,4])-expected))
    transverse=s.Matrix([0,-ky,kx])
    ck('transverse_line_is_invariant_not_full_matrix',mz(expected*transverse-(W*W-s.diff(W,r)+L2)*transverse))
    ck('nonzero_longitudinal_normal_mixing',s.simplify(V[1,2])==-2*s.I*kx/(ell*a) and V[1,2]!=0)
    ck('all_three_dual_degree_diagonal_partners_retained',
       all(s.simplify(V[i,i]-V[j,j].subs(mu,-mu))==0 for i,j in ((3,4),(5,2),(6,1))))
    broken=full_operator(r,ell,mu,kx,ky,omit_weight=True)[3][2]
    ck('missing_form_weight_rejected',not mz(broken-V))
    f=s.Function('f')(r)
    A=lambda v:s.diff(v,r)+W*v
    Ad=lambda v:-s.diff(v,r)+W*v
    ck('bare_normal_flux_rejected',s.simplify(-A(f)+s.diff(f,r))==-W*f and -W*f!=0)
    hm=lambda v:Ad(A(v))+L2*v
    hp=lambda v:A(Ad(v))+L2*v
    ck('angular_scalar_intertwiner_defect_exact',s.simplify(A(hm(f))-hp(A(f))-2*L2/ell*f)==0)
    ck('zero_angular_intertwiner_recovers',s.simplify((A(hm(f))-hp(A(f))).subs({kx:0,ky:0}))==0)
    ck('cannot_drop_mixed_matrix_by_zero_mutation',not mz(expected-s.diag(*expected.diagonal())))

    x,nu,delta,sigma=s.symbols('x nu delta sigma',real=True)
    Y=s.Function('Y')(x);ff=Y/s.sqrt(x);kap=sigma/2-delta
    eq=-4*(x*x*s.diff(ff,x,2)+x*s.diff(ff,x))+(x*x+(-2*sigma+4*delta)*x+4*nu*nu)*ff
    wh=-4*x**s.Rational(3,2)*(s.diff(Y,x,2)+(-s.Rational(1,4)+kap/x+(s.Rational(1,4)-nu*nu)/x**2)*Y)
    ck('shifted_Whittaker_equation_exact',s.simplify(eq-wh)==0)
    ck('old_Whittaker_is_only_zero_angular_case',kap.subs(delta,0)==sigma/2 and kap!=sigma/2)
    return {'checks':facts,'passed':sum(facts.values()),'period_relation_matrix':R.tolist(),
            'peripheral_map':P.tolist(),'real_period_kernel':ker[0].tolist(),
            'inverse_lattice_form':[str(v) for v in dual],
            'gauge10_weights':dict(Counter(ten)),'adjoint_weights':dict(Counter(adj)),
            'one_form_potential':[[str(v) for v in row] for row in expected.tolist()],
            'full_potential_matrix':[[str(v) for v in row] for row in V.tolist()],
            'Whittaker_kappa':'sigma/2-|xi|^2/(4*abs(mu)*ell)',
            'global_core_match':False,'generated_SM_selection':False,
            'global_particles_or_family_count':False,'full_goal_achieved':False}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,default=str))
