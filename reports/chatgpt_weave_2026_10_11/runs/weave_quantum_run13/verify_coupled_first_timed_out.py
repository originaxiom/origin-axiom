#!/usr/bin/env python3
"""Exact controls for Run 13. Finite models are not the silver PDE or spectrum."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s

OUT = Path(__file__).resolve().parent
facts: dict[str, bool] = {}

def zero(x) -> bool:
    if isinstance(x, s.MatrixBase):
        return all(s.simplify(v) == 0 for v in x)
    return s.simplify(x) == 0

def check(name: str, cond: bool) -> None:
    facts[name] = bool(cond)
    if not facts[name]:
        raise AssertionError(name)

def R(M: s.Matrix) -> s.Matrix:
    """Realification: complex x+iy -> [x,y]."""
    A, B = M.applyfunc(s.re), M.applyfunc(s.im)
    return A.row_join(-B).col_join(B.row_join(A))

def rv(v: s.Matrix) -> s.Matrix:
    return v.applyfunc(s.re).col_join(v.applyfunc(s.im))

# 1. Mixed kinetic term, gauge mode, gauge fixing: all real Euclidean p and m>0.
p = s.Matrix(s.symbols('p0:4', real=True))
m = s.symbols('m', positive=True)
p2 = (p.T*p)[0]
H = ((p2+m*m)*s.eye(4)-p*p.T).row_join(-s.I*m*p)
H = H.col_join((s.I*m*p.T).row_join(s.Matrix([[p2]])))
g = (s.I*p).col_join(s.Matrix([m]))
F = (s.I*p.T).row_join(s.Matrix([[-m]]))
check('mixed_hessian_Hermitian', zero(H-H.H))
check('original_gauge_direction_is_null', zero(H*g))
check('invariant_derivative_annihilates_gauge_direction',
      zero((-m*s.eye(4)).row_join(s.I*p)*g))
check('Faddeev_Popov_is_minus_p2_plus_m2', zero((F*g)[0]+p2+m*m))
K = s.simplify(H+F.H*F)
check('Feynman_gauge_cancels_every_mixing_entry', zero(K-(p2+m*m)*s.eye(5)))
check('opposite_gauge_fixing_sign_fails',
      not zero(H+(s.I*p.T).row_join(s.Matrix([[m]])).H*
               (s.I*p.T).row_join(s.Matrix([[m]]))-(p2+m*m)*s.eye(5)))
# Proca inversion is a separate invariant-variable control.
P = (p2+m*m)*s.eye(4)-p*p.T
Pinv = (s.eye(4)+p*p.T/(m*m))/(p2+m*m)
check('Proca_inverse_retains_longitudinal_constraint', zero(P*Pinv-s.eye(4)))
# Gauge invariant B=A-ds/m; E=ds-mA=-mB. This uses no division by a zero mass.
A = s.Matrix(s.symbols('a0:4'))
sigma = s.symbols('sigma')
B = A-s.I*p*sigma/m
check('unitary_gauge_variable_identity', zero(s.I*p*sigma-m*A+m*B))

# 2. Construct a nonreal, self-dual finite Hilbert complex.
# Numerical-looking masses below are exact arbitrary control data, NOT predictions.
n0, n1 = 3, 6
D0b=s.zeros(n1,n0); D0b[0,0]=2; D0b[1,1]=4
Cb=s.diag(0,0,3,3,5,0)
U=s.eye(n1)
for i,j in [(0,2),(1,3),(2,4),(3,5),(0,5)]:
    T=s.eye(n1); T[i,i]=T[j,j]=s.Rational(3,5)
    T[i,j]=-s.Rational(4,5); T[j,i]=s.Rational(4,5)
    U=U*T
U=U*s.diag(1,s.I,(3+4*s.I)/5,-s.I,(4-3*s.I)/5,-1)
# left phases mix compact-real and imaginary scalar directions nontrivially.
U=s.diag(s.I,1,(3-4*s.I)/5,1,s.I,1)*U
check('complex_basis_unitary', zero(U.H*U-s.eye(n1)))
check('complex_basis_genuinely_nonreal', not zero(U-U.conjugate()))
d0=U*D0b
d1=U.conjugate()*Cb*U.H
d2=-d0.T
check('flat_complex_d1_d0', zero(d1*d0))
check('flat_complex_d2_d1', zero(d2*d1))
check('curl_bilinear_is_symmetric_not_Hermitian', zero(d1-d1.T) and not zero(d1-d1.H))
L0=d0.H*d0
L1=d0*d0.H+d1.H*d1
L2=d1*d1.H+d2.H*d2
L3=d2*d2.H
check('zero_form_laplacian_preserves_compact_reality', zero(L0-L0.conjugate()))
check('Hodge_dual_degree_zero_three', zero(L3-L0.conjugate()))
check('Hodge_dual_degree_one_two', zero(L2-L1.conjugate()))
check('complex_intertwining_degree_zero_one', zero(L1*d0-d0*L0))
check('complex_intertwining_degree_one_two', zero(L2*d1-d1*L1))
check('one_form_spectrum_in_explicit_basis', zero(U.H*L1*U-s.diag(4,16,9,9,25,0)))

# Canonical four-Weyl internal operator and its mass square.
RF=s.zeros(n0).row_join(-d0.H)
RF=RF.col_join((-d0.conjugate()).row_join(d1))
check('Weyl_mass_bilinear_complex_symmetric', zero(RF-RF.T))
LF=s.diag(L0,L1)
check('Weyl_mass_square_equals_all_odd_Hodge_degrees', zero(RF.H*RF-LF))
V=s.diag(s.eye(n0),U)
canonical=s.zeros(n0).row_join(-D0b.T)
canonical=canonical.col_join((-D0b).row_join(Cb))
check('unitary_congruence_not_similarity_gives_mass_blocks', zero(V.T*RF*V-canonical))
check('wrong_Hermitian_bilinear_substitution_fails', not zero(RF-RF.H))
for j, mass in [(0,2),(1,4)]:
    f=s.eye(n0)[:,j]; e=d0*f/mass
    zlambda=f.col_join(s.zeros(n1,1))
    zrho=s.zeros(n0,1).col_join(e)
    check(f'vector_Weyl_pair_m{mass}_first',zero(RF*zlambda+mass*zrho.conjugate()))
    check(f'vector_Weyl_pair_m{mass}_second',zero(RF*zrho+mass*zlambda.conjugate()))
for j,mass in [(2,3),(3,3),(4,5)]:
    z=s.zeros(n0,1).col_join(U[:,j])
    check(f'chiral_Takagi_mode_{j}',zero(RF*z-mass*z.conjugate()))

# The anti-linear mass conjugation K(v)=conjugate(d1 v), K^2=d1^dagger d1.
check('antilinear_curl_square',zero(d1.conjugate()*d1-d1.H*d1))
Cproj=U*s.diag(0,0,1,1,1,1)*U.H
check('co_closed_subspace_projector',zero(Cproj*Cproj-Cproj) and zero(d0.H*Cproj))
check('antilinear_curl_preserves_co_closed',zero(d0.H*d1.conjugate()))
# Wrong deletion of conjugation changes square and gives wrong masses.
check('linear_curl_square_is_not_mass_square',not zero(d1*d1-d1.H*d1))

# Scalar Hessian as a real quadratic form. G=-Re d0^dagger u, M=-Im d0^dagger u.
Adj=d0.H; Ar=Adj.applyfunc(s.re); Ai=Adj.applyfunc(s.im)
G=-(Ar.row_join(-Ai)); M=-(Ai.row_join(Ar))
Rd1=R(d1)
Hs=s.simplify(Rd1.T*Rd1+M.T*M)
Hgf=s.simplify(Hs+G.T*G)
check('real_scalar_plus_gauge_fixing_equals_Hodge',zero(Hgf-R(L1)))
Tg=d0.applyfunc(s.re).col_join(d0.applyfunc(s.im))
Ti=rv(s.I*d0)
check('compact_gauge_is_scalar_null',zero(Hs*Tg))
check('imaginary_complex_gauge_is_not_null',not zero(Hs*Ti))
check('compact_and_imaginary_exact_are_orthogonal',zero(Tg.T*Ti))
check('gauge_inverse_Gram',zero(Tg.T*Tg-s.diag(4,16,0)))
Pg=Tg*s.diag(s.Rational(1,4),s.Rational(1,16),0)*Tg.T
check('compact_gauge_projector',zero(Pg*Pg-Pg) and zero(Pg-Pg.T))
check('gauge_subspace_reduces_Hodge',zero(Pg*Hgf-Hgf*Pg))
phys_cols=[rv(s.I*U[:,0]),rv(s.I*U[:,1])]
for j in [2,3,4,5]: phys_cols.extend([rv(U[:,j]),rv(s.I*U[:,j])])
W=s.Matrix.hstack(*phys_cols)
check('physical_scalar_basis_is_orthonormal_and_gauge_orthogonal',
      zero(W.T*W-s.eye(10)) and zero(Tg.T*W))
check('physical_scalar_masses_include_uneaten_exact_partners',
      zero(W.T*Hs*W-s.diag(4,16,9,9,9,9,25,25,0,0)))
check('harmonic_scalar_real_dimension_two',Hs.nullspace().__len__()-Tg.rank()==2)
check('unbroken_zero_form_gauge_mode_retained', L0.nullspace().__len__()==1)
check('harmonic_Weyl_gauge_plus_matter_retained',RF.nullspace().__len__()==2)

# All-degree Hodge multiplicities and physical boson/fermion counts.
spectra={0:[4,16,0],1:[4,16,9,9,25,0],2:[4,16,9,9,25,0],3:[4,16,0]}
census={}
for lam in [4,9,16,25]:
    r0=spectra[0].count(lam)
    n1lam=spectra[1].count(lam)
    r1=n1lam-r0
    nF=n1lam+spectra[3].count(lam)
    nBphys=3*r0+(2*n1lam-r0)
    check(f'physical_degrees_balance_lambda_{lam}', nBphys==2*nF==4*r0+2*r1)
    census[str(lam)]={'massive_vector_multiplets':r0,'massive_chiral_multiplets':r1,
                     'real_bosonic_on_shell':nBphys,'fermionic_on_shell':2*nF}
check('complex_gauge_deletion_would_break_count',
      (3*2+2*(n1-1)-2*2) != (4*2+2*3))
# Deliberately break flatness: neither complex nor fermion/Hodge block diagonal survives.
bad=Cb.copy(); bad[0,0]=1
bad1=U.conjugate()*bad*U.H
badR=s.zeros(n0).row_join(-d0.H).col_join((-d0.conjugate()).row_join(bad1))
check('nonflat_control_rejected',not zero(bad1*d0) and not zero((badR.H*badR)[:n0,n0:]))

# 3. Standard rest-frame N=1 Clifford algebra: normalization/control only.
def annihilator(mode: int) -> s.Matrix:
    X=s.zeros(4)
    for n in range(4):
        if (n>>mode)&1:
            target=n^(1<<mode)
            sign=(-1)**((n & ((1<<mode)-1)).bit_count())
            X[target,n]=sign
    return X
b=[annihilator(0),annihilator(1)]
for i in range(2):
    for j in range(2):
        check(f'rest_supercharge_anticommutator_{i}{j}',
              zero(2*m*(b[i]*b[j].H+b[j].H*b[i])-2*m*(i==j)*s.eye(4)))
check('rest_supercharge_nilpotence',all(zero(x*x) for x in b) and zero(b[0]*b[1]+b[1]*b[0]))
parity=s.diag(1,-1,-1,1)
check('rest_supercharges_exchange_statistics',all(zero(parity*x+x*parity) for x in b))
check('standard_chiral_and_vector_state_counts',
      sum(1 for i in range(4) if parity[i,i]==1)==2 and s.kronecker_product(s.eye(2),parity).trace()==0)

result={'status':'exact finite controls, not a global PDE or actual silver mass calculation',
        'facts':facts,'passed':sum(facts.values()),'total':len(facts),
        'artificial_control_spectrum':census,
        'physical_boundary_supplied':True,'actual_silver_census_recomputed':False,
        'independent_author_review':False,'full_nonlinear_Hamiltonian_proved':False}
(OUT/'COUPLED_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
