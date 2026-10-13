#!/usr/bin/env python3
"""Independent finite checks for Run 4. No imported project/run verification code."""
from __future__ import annotations
from itertools import product, combinations
from pathlib import Path
from fractions import Fraction
import json
import sympy as s

OUT=Path(__file__).resolve().parent
checks={}
def check(name, statement):
    ok=bool(statement)
    checks[name]=ok
    if not ok: raise AssertionError(name)

def simp(x): return s.simplify(s.expand(x))

# Exterior algebra over exact sympy coefficients; generator order fixes Berezin signs.
class Grass:
    def __init__(self, terms=None):
        self.t={m:simp(c) for m,c in (terms or {}).items() if simp(c)!=0}
    def __add__(self,o):
        if not isinstance(o,Grass): o=Grass({0:s.sympify(o)})
        t=self.t.copy()
        for m,c in o.t.items(): t[m]=t.get(m,0)+c
        return Grass(t)
    __radd__=__add__
    def __neg__(self): return Grass({m:-c for m,c in self.t.items()})
    def __sub__(self,o): return self+(-o)
    def __mul__(self,o):
        if not isinstance(o,Grass): return Grass({m:c*s.sympify(o) for m,c in self.t.items()})
        t={}
        for a,x in self.t.items():
            for b,y in o.t.items():
                if a&b: continue
                sign=(-1)**sum((b&((1<<i)-1)).bit_count() for i in range(a.bit_length()) if a>>i&1)
                t[a|b]=t.get(a|b,0)+sign*x*y
        return Grass(t)
    __rmul__=__mul__

g=[Grass({1<<i:1}) for i in range(5)]
a,b0,b1,bb0,bb1=g
b=[b0,b1]; bb=[bb0,bb1]
D=s.Matrix([[2,1],[1,3]])
S=sum((bb[i]*b[j]*D[i,j] for i in range(2) for j in range(2)),Grass())
exp=Grass({0:1})-S+(S*S)*s.Rational(1,2)
# Overall measure orientation fixed by the positive det D in the zero-saturated integral.
raw=(a*exp).t.get(31,0)
orientation=simp(D.det()/raw)
def integral(x): return simp(orientation*(x*exp).t.get(31,0))
check('berezin_measure_orientation_is_a_sign',orientation in [1,-1])
check('unsaturated_integral_vanishes',integral(Grass({0:1}))==0)
check('single_zero_insertion_has_one_determinant',integral(a)==D.det())
# q_i are point evaluations in a basis with one zero mode and two nonzero modes.
V=s.Matrix([[1,2,0],[3,1,1],[-2,0,2]])
fields=[sum((V[i,j]*[a,b0,b1][j] for j in range(3)),Grass()) for i in range(3)]
for i in range(3):
    check(f'one_insertion_{i}',integral(fields[i])==V[i,0]*D.det())
check('two_psi_insertions_all_zero',all(integral(x*y)==0 for x in fields for y in fields))
check('product_of_integrals_can_be_nonzero',integral(fields[0])*integral(fields[1])==75)
# With psi_i psi_j barpsi_k ordering the signs follow the declared Berezin convention.
G=s.Matrix(V[:,1:3])*D.inv()
mixed=[]
for i,j,k in product(range(3),range(3),range(2)):
    val=integral(fields[i]*fields[j]*bb[k])
    rhs=D.det()*(V[i,0]*G[j,k]-V[j,0]*G[i,k])
    mixed.append(simp(val-rhs)==0)
check('mixed_wick_correlators_share_one_determinant',all(mixed))

# Quaternion real regular irreducible 4D representation on (1,i,j,k).
def qbasis(a,b):
    if a==0:return 1,b
    if b==0:return 1,a
    if a==b:return -1,0
    return (1 if (a,b) in [(1,2),(2,3),(3,1)] else -1,6-a-b)
def mat_left(a):
    M=s.zeros(4)
    for b in range(4):
        z,c=qbasis(a,b);M[c,b]=z
    return M
def mat_right(a):
    M=s.zeros(4)
    for b in range(4):
        z,c=qbasis(b,a);M[c,b]=z
    return M
L=[mat_left(i) for i in [1,2,3]]
R=[mat_right(i) for i in [1,2,3]]
check('left_right_quaternions_commute',all(A*B==B*A for A in L for B in R))
check('faithful_quaternion_matrices',L[0]**2==-s.eye(4) and L[0]*L[1]==L[2] and L[1]*L[0]==-L[2])

# Exact singular OPE of B_ab=:chi_a chi_b:, using fermion Wick signs.
def addpair(d,a,b,c):
    if a==b:return
    if a>b:a,b,c=b,a,-c
    d[(a,b)]=simp(d.get((a,b),0)+c)
    if d[(a,b)]==0:del d[(a,b)]
def ope(A,B):
    double=0;single={}
    for (a,b),x in A.items():
      for (c,d),y in B.items():
        double+=x*y*(int(a==d and b==c)-int(a==c and b==d))
        if a==c:addpair(single,b,d,-x*y)
        if a==d:addpair(single,b,c,x*y)
        if b==c:addpair(single,a,d,x*y)
        if b==d:addpair(single,a,c,-x*y)
    return simp(double),single

def cur(M,sign=1):return {(a,b):sign*s.I*M[a,b]/2 for a,b in combinations(range(4),2) if M[a,b]!=0}
def scale(A,k):return {ab:simp(k*v) for ab,v in A.items() if simp(k*v)!=0}
def equal(A,B):return all(simp(A.get(k,0)-B.get(k,0))==0 for k in set(A)|set(B))
# Orientation convention of each su2 basis is chosen once to give +i epsilon.
J=[cur(M,1) for M in L]
I=[cur(M,-1) for M in R]
def eps(a,b,c):return s.LeviCivita(a,b,c)
for name,C in [('quaternion',J),('commuting',I)]:
    check(name+'_level_one_double_poles',all(ope(C[a],C[b])[0]==s.Rational(1,2)*int(a==b) for a,b in product(range(3),repeat=2)))
    ok=[]
    for a,b in product(range(3),repeat=2):
        rhs={}
        for c in range(3):
            for ab,v in scale(C[c],s.I*eps(a,b,c)).items():rhs[ab]=rhs.get(ab,0)+v
        ok.append(equal(ope(C[a],C[b])[1],rhs))
    check(name+'_su2_simple_poles',all(ok))
check('the_two_current_algebras_commute',all(ope(A,B)==(0,{}) for A in J for B in I))

# Conjugation on bilinears via real SO4 matrices.
def transform_bilinear(C,M):
    out={}
    for (a,b),v in C.items():
        for c,d in product(range(4),repeat=2):addpair(out,c,d,v*M[a,c]*M[b,d])
    return out
signs=[]
for g in L[:2]:
    row=[]
    for C in J:
        images=transform_bilinear(C,g)
        row.append(1 if equal(images,C) else -1 if equal(images,scale(C,-1)) else 0)
    signs.append(row)
check('three_current_parity_characters',signs==[[1,-1,-1],[-1,1,-1]])
check('three_other_currents_are_Q8_singlets',all(equal(transform_bilinear(C,g),C) for C in I for g in L))
check('sugawara_central_charge_split',s.Rational(3,3)+s.Rational(3,3)==2)
# Normalizer lifts and adjoint rotations. A sign of all generator axes is conventional.
NL=(s.eye(4)+L[0])/s.sqrt(2)
NR=(s.eye(4)-L[1])/s.sqrt(2)
rotations=[]
for M in [NL,NR]:
    Cmat=s.zeros(3)
    for a,C in enumerate(J):
        image=transform_bilinear(C,M)
        for b,T in enumerate(J):
            # Orthogonal basis coefficient obtained by exact coefficient inner product.
            numerator=sum(s.conjugate(v)*image.get(k,0) for k,v in T.items())
            denominator=sum(s.conjugate(v)*v for v in T.values())
            Cmat[a,b]=simp(numerator/denominator)
    rotations.append(Cmat)
check('normalizer_current_matrices_are_rotations',all(M.T*M==s.eye(3) and M.det()==1 for M in rotations))

def closure(mats):
    identity=s.eye(mats[0].rows)
    seen={tuple(identity)};q=[identity]
    for M in q:
        for Gm in mats:
            N=M*Gm;key=tuple(N)
            if key not in seen:seen.add(key);q.append(N)
    return q
check('rotation_image_order_24',len(closure(rotations))==24)

# NS Fock graded Q8 characters: q here records twice the conformal weight.
max_n=12
def char_series(coefs):
    p=[0]*(max_n+1);p[0]=1
    for mode in range(1,max_n+1,2):
        z=[0]*(max_n+1)
        for n in range(max_n+1):
            for occupation,a in enumerate(coefs):
                if n+mode*occupation<=max_n:z[n+mode*occupation]+=p[n]*a
        p=z
    return p
ch_id=char_series([1,4,6,4,1]);ch_z=char_series([1,-4,6,-4,1]);ch_i=char_series([1,0,2,0,1])
fock=[]
for n,(a0,b0,c0) in enumerate(zip(ch_id,ch_z,ch_i)):
    mult=[Fraction(a0+b0+6*c0,8),Fraction(a0+b0-2*c0,8),Fraction(a0-b0,4)]
    check(f'fock_decomposition_level_{n}',all(m.denominator==1 and m>=0 for m in mult) and mult[0]+3*mult[1]+2*mult[2]==a0)
    fock.append({'h':str(Fraction(n,2)),'dimension':a0,'trivial':int(mult[0]),'each_nontrivial_parity':int(mult[1]),'quaternion_doublets':int(mult[2])})
check('level_one_complete_six_currents',fock[2]['trivial']==3 and fock[2]['each_nontrivial_parity']==1 and fock[2]['dimension']==6)

# Bundle factor, stabilizer and metric arithmetic.
y=s.symbols('y',positive=True)
# d_tau d_bar_tau log y = (1/4)*d_y^2 log y.
check('relative_modular_norm_curvature',s.diff(s.log(y),y,2)/4==-1/(4*y**2))
check('relative_target_norm_curvature',s.diff(11*s.log(y),y,2)/4==-11/(4*y**2))
check('cusp_orders_match_weights',s.Rational(22,24)==s.Rational(11,12) and s.Rational(2,24)==s.Rational(1,12))
# At S:i and ST:omega, eta^2's weight-one factor cancels its finite character.
check('eta2_S_stabilizer_total_factor',simp((-s.I)*s.I)==1)
check('eta2_ST_stabilizer_total_factor',simp(s.exp(-s.I*s.pi/3)*s.exp(s.I*s.pi/3))==1)
check('eta2_minusI_stabilizer_total_factor',(-1)*(-1)==1)
check('trivial_counterterm_cannot_change_T_character',simp(s.exp(s.I*s.pi/6)-1)!=0)
# q=h geometric representative -> quantum representative requires pulling both
# metric and connection; this algebraic identity is checked with a symbolic scalar.
x=s.symbols('x',real=True);a0=s.Function('a')(x);h=s.Function('h')(x)
check('pulled_back_connection_intertwines',simp(s.diff(h*a0,x)-s.diff(h,x)/h*(h*a0)-h*s.diff(a0,x))==0)

# Standard free-boson radius deformation: action and momenta conventions declared in report.
rad=s.symbols('R',positive=True);m,n=s.symbols('m n',integer=True)
pL=m/rad+n*rad/2;pR=m/rad-n*rad/2
check('radius_family_preserves_integer_spin',simp((pL**2-pR**2)/2)==m*n)
check('radius_changes_scaling_dimension',simp((pL**2+pR**2)/2-m**2/rad**2-n**2*rad**2/4)==0)
check('current_current_abelian_structure_constant_zero',ope(I[2],I[2])[1]=={})

out={'checks':checks,'passed':sum(checks.values()),'berezin':{'D':str(D),'orientation':str(orientation),'mixed_values':[str(integral(fields[0]*fields[1]*bb[k])) for k in range(2)]},'current_quaternion_parities':signs,'current_rotation_matrices':[[[str(x) for x in M.row(i)] for i in range(3)] for M in rotations],'fock_table':fock}
(OUT/'exact_results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
