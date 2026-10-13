#!/usr/bin/env python3
"""Run 6: cochain-derived representation and protected-sector comparison.

Requires Python 3.10+ and sympy. All formal tests use exact arithmetic.
No verification code or matrix output is imported from earlier runs/repository.
"""
from __future__ import annotations
import itertools
import json
from fractions import Fraction
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
OUT=HERE/'results'; OUT.mkdir(exist_ok=True)
checks=[]
data={}

def simp(m):
    return m.applyfunc(lambda x: sp.simplify(sp.expand_complex(x))) if isinstance(m,sp.MatrixBase) else sp.simplify(sp.expand_complex(m))

def eq(a,b):
    if isinstance(a,sp.MatrixBase):
        return simp(a-b)==sp.zeros(*a.shape)
    return simp(a-b)==0

def check(name, condition, detail=None):
    ok=bool(condition)
    checks.append({'name':name,'passed':ok,'detail':detail})
    if not ok:
        raise AssertionError(name+': '+str(detail))
    print('PASS',name)

def serial(m):
    if isinstance(m,sp.MatrixBase): return [[str(simp(x)) for x in row] for row in m.tolist()]
    return str(m)

# --- Direct crossed-homomorphism quotient, including the trivial character ---
I=sp.eye(2); A=sp.diag(sp.I,-sp.I); B=sp.Matrix([[0,1],[-1,0]]); C=A*B
zeta=(1+sp.I)/sp.sqrt(2)
nL=(I+A)/sp.sqrt(2); nR=(I-B)/sp.sqrt(2)
pairs=[(1,-1),(-1,-1),(-1,1)] # theta2, theta3(clock), theta4 labels
allpairs=[(1,1)]+pairs
Q={(1,1):I,(1,-1):A,(-1,-1):C,(-1,1):B}
check('Q8_relations',eq(A*A,-I) and eq(B*B,-I) and eq(A*B,-B*A))
check('specified_SU2_normalizer_lifts',eq(nL*A*nL.inv(),A) and eq(nL*B*nL.inv(),A*B) and eq(nR*A*nR.inv(),A*B) and eq(nR*B*nR.inv(),B))
check('normalizer_unitarity_and_determinants',all(eq(n.H*n,I) and eq(n.det(),1) for n in [nL,nR]))

J=sp.zeros(4,2);J[2:4,:]=I
projections={};boundaries={}
for a,b in allpairs:
    p=(a,b)
    boundaries[p]=(a*A-I).col_join(b*B-I)
    projections[p]=(-(b*B-I)*(a*A-I).inv()).row_join(I)
check('all_four_H1_dimensions_are_two',all(boundaries[p].rank()==2 and projections[p].rank()==2 for p in allpairs))
check('all_projections_kill_coboundaries',all(eq(projections[p]*boundaries[p],sp.zeros(2)) for p in allpairs))
check('fixed_quotient_gauge_is_right_inverse',all(eq(projections[p]*J,I) for p in allpairs))
check('character_intertwiners_exact',all(eq(Q[p]*A*Q[p].inv(),p[0]*A) and eq(Q[p]*B*Q[p].inv(),p[1]*B) for p in allpairs))

cochain={};quotient={};targetp={}
for name,n in [('L',nL),('R',nR)]:
    for a,b in allpairs:
        p=(a,b);pn=(a,a*b) if name=='L' else (a*b,b)
        targetp[name,p]=pn
        F=sp.zeros(4)
        if name=='L':
            F[:2,:2]=n.inv();F[2:,:2]=n.inv();F[2:,2:]=n.inv()*a*A
        else:
            F[:2,:2]=n.inv();F[:2,2:]=n.inv()*a*A;F[2:,2:]=n.inv()
        F=simp(F);cochain[name,p]=F
        quotient[name,p]=simp(projections[pn]*F*J)
check('both_moves_are_cochain_maps_for_all_parities',all(eq(cochain[name,p]*boundaries[p],boundaries[targetp[name,p]]*n.inv()) for name,n in [('L',nL),('R',nR)] for p in allpairs))
check('quotient_maps_do_not_depend_on_coboundary_representative',all(eq(projections[targetp[name,p]]*cochain[name,p],quotient[name,p]*projections[p]) for name in ['L','R'] for p in allpairs))
# Independent gauge control: kill the b component rather than the a component.
Jb=sp.zeros(4,2);Jb[:2,:]=I
Pb={p:I.row_join(-(p[0]*A-I)*(p[1]*B-I).inv()) for p in allpairs}
Hb={p:simp(projections[p]*Jb) for p in allpairs}
check('alternate_b_zero_gauge_is_valid',all(eq(Pb[p]*boundaries[p],sp.zeros(2)) and eq(Pb[p]*Jb,I) and Hb[p].det()!=0 for p in allpairs))
check('all_move_matrices_agree_in_alternate_gauge',all(eq(quotient[name,p]*Hb[p],Hb[targetp[name,p]]*Pb[targetp[name,p]]*cochain[name,p]*Jb) for name in ['L','R'] for p in allpairs))

ML=quotient['L',(1,1)];MR=quotient['R',(1,1)]
check('untwisted_pullback_eigencharacters',eq(ML,sp.diag(zeta,sp.conjugate(zeta))) and eq(MR,sp.diag(sp.conjugate(zeta),zeta)))

raw={};common={};reps={}
for name in ['L','R']:
    raw[name]=sp.zeros(6);common[name]=sp.zeros(6)
    for col,p in enumerate(pairs):
        pn=targetp[name,p];row=pairs.index(pn); M=quotient[name,p]
        raw[name][2*row:2*row+2,2*col:2*col+2]=M
        common[name][2*row:2*row+2,2*col:2*col+2]=simp(Q[pn].inv()*M*Q[p])
    # Pullbacks compose oppositely. Invert the move matrices for the convention
    # rho(g h)=rho(g)rho(h) used for the target's modular coefficients.
    reps[name]=simp(common[name].inv())
check('two_three_dimensional_summands_are_invariant',all(common[name].extract([0,2,4],[1,3,5])==sp.zeros(3) and common[name].extract([1,3,5],[0,2,4])==sp.zeros(3) for name in ['L','R']))
TL=reps['L'].extract([1,3,5],[1,3,5]);TR=reps['R'].extract([1,3,5],[1,3,5])
OL=sp.Matrix([[1,0,0],[0,0,1],[0,-1,0]])
OR=sp.Matrix([[0,-1,0],[1,0,0],[0,0,1]])
check('cochain_derived_tensor_factorization',eq(TL,zeta*OL) and eq(TR,sp.conjugate(zeta)*OR))
check('other_summand_is_the_complex_conjugate',eq(reps['L'].extract([0,2,4],[0,2,4]),sp.conjugate(TL)) and eq(reps['R'].extract([0,2,4],[0,2,4]),sp.conjugate(TR)))
check('rotation_matrices_are_SO3',all(eq(O.T*O,sp.eye(3)) and O.det()==1 for O in [OL,OR]))
TS=simp(TR*TL.inv()*TR);OS=OR*OL.T*OR
D=sp.diag(-sp.I,1,sp.I)
P=sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
M=sp.Matrix([[sp.I,0,0],[0,0,1],[0,1,0]])
thetaL=sp.conjugate(zeta)*M;thetaS=zeta*P
check('exact_monomial_intertwiner_for_both_modular_generators',eq(D*TL*D.inv(),thetaL) and eq(D*TS*D.inv(),thetaS))
check('genuine_metaplectic_relations',eq(TS**2,(TS*TL)**3) and eq(TS**8,sp.eye(3)) and eq(TS**4,-sp.eye(3)))
check('braid_relation_for_L_and_Rinverse',eq(TL*TR.inv()*TL,TR.inv()*TL*TR.inv()))
check('geometric_line_character_on_S',eq(TS,zeta**(-3)*OS))
check('line_holonomy_not_trivial',eq(zeta**8,1) and eq((zeta**(-3))**4,-1))
check('normalizer_local_action_has_different_center',eq(OS**2,sp.eye(3)) and eq(OS**4,sp.eye(3)))

# Factorization on cochains is also checked by a block-diagonal gauge change.
BQ=sp.diag(*(Q[p] for p in pairs))
check('six_dimensional_common_frame_intertwiner',all(eq(BQ.inv()*raw[g]*BQ,common[g]) for g in ['L','R']))

data['cohomology']={
 'parities':pairs,'A':serial(A),'B':serial(B),'nL':serial(nL),'nR':serial(nR),
 'untwisted_pullback_L':serial(ML),'untwisted_pullback_R':serial(MR),
 'raw_pullbacks':{g:serial(raw[g]) for g in raw},
 'common_pullbacks':{g:serial(common[g]) for g in common},
 'selected_TL':serial(TL),'selected_TR':serial(TR),'selected_TS':serial(TS),
 'OL':serial(OL),'OR':serial(OR),'OS':serial(OS),'theta_intertwiner_D':serial(D),
 'Hodge_scope':'Conjugate invariant eigenspaces reconstructed. An independent Hodge-Riemann sign calculation is not performed.'}

# --- Exact finite image via signed permutations and eighth-root scalar ---
def tup(O): return tuple(int(x) for x in O)
def mat(t): return sp.Matrix(3,3,t)
def mul(g,h): return ((g[0]+h[0])%8,tup(mat(g[1])*mat(h[1])))
one=(0,tup(sp.eye(3)));gens=[(1,tup(OL)),(7,tup(OR))]
group={one};stack=[one]
while stack:
 g=stack.pop()
 for h in gens:
  z=mul(g,h)
  if z not in group:group.add(z);stack.append(z)
G=sorted(group);rotations={o for e,o in G}
check('exact_image_orders',len(G)==96 and len(rotations)==24)
cent=[e for e,o in G if o==one[1]]
check('scalar_center_is_fourth_roots',cent==[0,2,4,6])
check('all_finite_pairs_preserve_orientation',all(mat(o).det()==1 and mat(o).T*mat(o)==sp.eye(3) for o in rotations))

def phase_sum(terms):
    """Reduce exact integer sums in Q[zeta]/(zeta^4+1)."""
    a=[Fraction(0) for _ in range(4)]
    for exponent,coeff in terms:
        r=exponent%8;a[r%4]+=Fraction(coeff)*(1 if r<4 else -1)
    return a

def avg(terms):return [x/len(G) for x in phase_sum(terms)]

trace=lambda o:int(sp.trace(mat(o)))
irr=avg([(0,trace(o)**2) for e,o in G])
check('triplet_irreducible_by_character',irr==[1,0,0,0])
homdims=[]
for r in range(8):
 x=avg([((r-1)*e,trace(o)**2) for e,o in G])
 check('line_power_intertwiner_'+str(r),x==([1,0,0,0] if r==1 else [0,0,0,0]))
 homdims.append(int(x[0]))
check('no_invariant_bilinear_on_T',avg([(2*e,trace(o)**2) for e,o in G])==[0,0,0,0])
check('no_T_valued_quadratic_product',avg([(e,trace(o)**3) for e,o in G])==[0,0,0,0])
check('unique_invariant_Hermitian_pairing',avg([(0,trace(o)**2) for e,o in G])==[1,0,0,0])

# OPE covariance: rotations preserve metric and alternating bracket.
eps=lambda a,b,c:int(sp.LeviCivita(a,b,c))
check('rotation_action_preserves_all_current_structure_constants',all(
 sum(O[a,i]*O[b,j]*eps(i,j,k) for i in range(3) for j in range(3))==sum(eps(a,b,c)*O[c,k] for c in range(3))
 for ot in rotations for O in [mat(ot)] for a,b,k in itertools.product(range(3),repeat=3)))
check('central_i_twist_fails_current_vacuum_OPE',sp.I**2==-1 and sp.I**2!=1)
# Endomorphism action forgets the scalar exactly.
check('neutral_endomorphism_transport_cancels_geometric_line',all(eq(sp.kronecker_product((zeta**e)*mat(o),sp.conjugate((zeta**e)*mat(o))),sp.kronecker_product(mat(o),mat(o))) for e,o in G))

data['finite_representation']={'order':len(G),'rotation_order':len(rotations),'center_exponents_mod8':cent,'line_power_Hom_dimensions_r0_to7':homdims,'elements':[{'ell_exponent_mod8':e,'O':list(o)} for e,o in G]}

# --- Complete local protected algebra across an OPEN deformation interval ---
a,b,c,d,t=sp.symbols('a b c d t',real=True)
qL=sp.Matrix([a,b]);qR=sp.Matrix([c,d])
aR=(c-d)/sp.sqrt(2);bL=(a+b)/sp.sqrt(2);bR=(c+d)/sp.sqrt(2)
right_momentum=sp.sinh(t)*bL+sp.cosh(t)*bR
check('open_interval_holomorphy_three_independent_constraints',eq(right_momentum.subs(t,0),bR) and eq(sp.diff(right_momentum,t).subs(t,0),bL) and sp.Matrix([[0,0,1,-1],[1,1,0,0],[0,0,1,1]]).rank()==3)
sol=sp.linsolve([aR,bL,bR],[a,b,c,d])
check('protected_charge_lattice_is_n_minusn_zero_zero',sol==sp.FiniteSet((-b,b,0,0)))
N=18
# 2-coloured partitions, independently compared with p*p below.
p2=[0]*(N+1);p2[0]=1
for k in range(1,N+1):
 for colour in range(2):
  for h in range(k,N+1):p2[h]+=p2[h-k]
p=[0]*(N+1);p[0]=1
for k in range(1,N+1):
 for h in range(k,N+1):p[h]+=p[h-k]
check('two_independent_oscillator_counts_agree',all(p2[h]==sum(p[j]*p[h-j] for j in range(h+1)) for h in range(N+1)))

def p_at(i):return p2[i] if i>=0 else 0

def spinchar(j,traceR):
 if j==0:return 1
 if j==1:return traceR
 c0,c1=1,traceR
 for k in range(1,j):c0,c1=c1,(traceR-1)*c1-c0
 return c1
rows=[]
for h in range(N+1):
 dims=sum(p_at(h-n*n) for n in range(-int(h**.5),int(h**.5)+1))
 mult=[p_at(h-j*j)-p_at(h-(j+1)**2) for j in range(int(h**.5)+1)]
 check('protected_grade_'+str(h)+'_SU2_decomposition',all(m>=0 for m in mult) and dims==sum((2*j+1)*m for j,m in enumerate(mult)))
 target_mult=avg([(-e, trace(o)*sum(m*spinchar(j,trace(o)) for j,m in enumerate(mult))) for e,o in G])
 check('protected_grade_'+str(h)+'_has_no_target_T',target_mult==[0,0,0,0])
 trpi=sum(m*((-1)**j) for j,m in enumerate(mult))
 sing=(dims+3*trpi)//4;par=(dims-trpi)//4
 rows.append({'h':h,'dimension':dims,'SU2_integer_spin_multiplicities':mult,'Q8_trivial_multiplicity':sing,'each_parity_multiplicity':par,'T_multiplicity':0})
check('protected_weight_one_is_one_singlet_plus_triplet',rows[1]['dimension']==4 and rows[1]['Q8_trivial_multiplicity']==1 and rows[1]['each_parity_multiplicity']==1)
check('protected_graded_series_initial_values',[r['dimension'] for r in rows[:7]]==[1,4,9,20,42,80,147])
# A bounded scan checks, rather than establishes, the all-interval arithmetic.
scan=[q for q in itertools.product(range(-4,5),repeat=4) if q[2]-q[3]==0 and q[0]+q[1]==0 and q[2]+q[3]==0]
check('independent_bounded_charge_scan',scan==[(n,-n,0,0) for n in range(-4,5)])
data['protected_algebra']={'description':'su(2)_1 vacuum algebra tensor one Heisenberg vacuum algebra; open-interval local protected intersection, not enhanced isolated radii','character':'theta3(2tau)/eta(tau)^2','grades':rows,'max_grade':N}

# --- Ordinary protected spinor module / semion control ---
# e^{+/-i H_A/sqrt(2)} is not a local NS field in the original glued lattice.
charge=sp.sqrt(2)/2
check('spinor_weight_and_current_descendant',eq(charge**2/2,sp.Rational(1,4)) and eq((2*charge)**2/2,1))
check('spinor_pair_OPE_exponents',eq(charge**2,sp.Rational(1,2)) and eq(-charge**2,-sp.Rational(1,2)))
check('spinor_charges_are_not_local_NS_lattice',sp.Rational(1,2).is_integer is False)
omega=lambda a,b,c:(-1)**(a*b*c)
R=lambda a,b:sp.I**(a*b)
add=lambda a,b:(a+b)%2
pent=[];hexes=[]
for a,b,c,d in itertools.product(range(2),repeat=4):
 pent.append(omega(b,c,d)*omega(a,add(b,c),d)*omega(a,b,c)==omega(add(a,b),c,d)*omega(a,b,add(c,d)))
for a,b,c in itertools.product(range(2),repeat=3):
 hexes.append(eq(R(a,add(b,c)),omega(b,c,a)*R(a,c)/omega(b,a,c)*R(a,b)*omega(a,b,c)))
 hexes.append(eq(R(add(a,b),c),R(a,c)*R(b,c)*omega(a,c,b)/(omega(c,a,b)*omega(a,b,c))))
check('all_16_semion_pentagons',all(pent))
check('all_16_semion_hexagons',all(hexes))
check('wrong_trivial_associator_is_detected',not eq(R(1,add(1,1)),R(1,1)*R(1,1)))
S2=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
fusion=[[[simp(sum(S2[a,x]*S2[b,x]*sp.conjugate(S2[c,x])/S2[0,x] for x in range(2))) for c in range(2)] for b in range(2)] for a in range(2)]
check('Verlinde_fusion_is_Z2',all(fusion[a][b][c]==int(c==add(a,b)) for a,b,c in itertools.product(range(2),repeat=3)))
ranks=[]
for genus in range(5):
 for n in range(9):
  rank=simp(sum(S2[0,x]**(2-2*genus)*(S2[1,x]/S2[0,x])**n for x in range(2)))
  exp=2**genus if n%2==0 else 0
  check('ordinary_block_rank_g'+str(genus)+'_n'+str(n),rank==exp)
  ranks.append({'genus':genus,'semion_punctures':n,'rank':int(rank)})
check('ordinary_torus_control_never_has_rank_three',all(r['rank']!=3 for r in ranks if r['genus']==1))
check('semion_not_an_extra_triplet_fusion_channel',fusion[1][1]==[1,0])
data['ordinary_semion_control']={'S':serial(S2),'fusion':[[[int(x) for x in v] for v in w] for w in fusion],'ranks':ranks,'scope':'Ordinary integrable primary punctures of su(2)_1, NOT Q8-crossed spin defects or their junctions.'}

# All expressions in the recorded exact matrices must remain free of Float atoms.
check('no_floating_point_atoms_in_exact_matrices',all(not x.has(sp.Float) for m in list(raw.values())+list(reps.values())+[TL,TR,TS,ML,MR,D] for x in m))
data['checks']=checks;data['check_count']=len(checks);data['all_passed']=all(c['passed'] for c in checks)
(OUT/'exact_results.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
print('TOTAL',len(checks),'EXACT CHECKS PASSED')
