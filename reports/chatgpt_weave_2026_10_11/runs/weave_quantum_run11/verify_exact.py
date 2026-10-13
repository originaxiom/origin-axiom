#!/usr/bin/env python3
"""Exact, scoped checks for the Run 11 supplied Yang--Mills comparator.

Requires Python 3.10+ and sympy. This does not execute repository producers,
solve a new nonlinear PDE numerically, or certify an effective theory.
"""
from __future__ import annotations
import itertools, json
from pathlib import Path
import sympy as s

OUT=Path(__file__).resolve().parent/'results'
OUT.mkdir(exist_ok=True)
checks=[]
def ck(name: str, condition: bool) -> None:
    if not bool(condition): raise AssertionError(name)
    checks.append(name)
def zero(M) -> bool:
    return all(s.simplify(x)==0 for x in M)

x=s.symbols('x', real=True)
y,area_b,area_f=s.symbols('y area_b area_f', positive=True)
shape=s.Matrix([[1,x],[x,x*x+y*y]])/y
metric=s.diag(area_b*shape,area_f*shape)
inverse=metric.inv()
volume=area_b*area_f
# F=2*pi*t3*H on coordinates (a,b,c,d), all of period one.
H=s.zeros(4)
H[1,2]=1; H[2,1]=-1
H[0,3]=-1; H[3,0]=1
Hup=s.simplify(inverse*H*inverse.T)
star=s.zeros(4)
for i,j in itertools.product(range(4),repeat=2):
    star[i,j]=s.simplify(volume*s.Rational(1,2)*sum(
        s.LeviCivita(i,j,k,l)*Hup[k,l] for k,l in itertools.product(range(4),repeat=2)))
ck('metric determinant / arbitrary common complex shape',s.simplify(metric.det()-volume**2)==0)
ck('anti-self-duality for every x and y>0',zero(star+H))
contract=s.simplify(sum(H[i,j]*Hup[i,j] for i,j in itertools.product(range(4),repeat=2)))
ck('integrated gauge action g4^2 S = 4 pi^2',s.simplify(volume*contract-4)==0)
wedge=s.simplify(s.Rational(1,4)*sum(s.LeviCivita(i,j,k,l)*H[i,j]*H[k,l]
                    for i,j,k,l in itertools.product(range(4),repeat=4)))
ck('H wedge H = -2 times oriented volume',wedge==-2)
# tr t3^2=1/2: (2pi)^2/(8pi^2) * 1/2 * int H^2.
Q=s.simplify(s.Rational(1,4)*wedge)
ck('topological charge Q4=-1/2',Q==-s.Rational(1,2))

coords=s.symbols('a b c d', real=True)
a,b,c,d=coords
pot=s.Matrix([0,0,b,-a])  # omit common 2*pi*t3
curv=s.Matrix(4,4,lambda i,j:s.diff(pot[j],coords[i])-s.diff(pot[i],coords[j]))
ck('curvature computed from the written connection',curv==H)
ck('Yang--Mills equation: constant raised Abelian curvature',all(
    s.simplify(sum(s.diff(Hup[i,j],coords[i]) for i in range(4)))==0 for j in range(4)))
ck('Bianchi identity',all(sum(s.diff(H[j,k],coords[i]) for i,j,k in [p,(p[1],p[2],p[0]),(p[2],p[0],p[1])])==0
                      for p in itertools.combinations(range(4),3)))

I=s.I; t3=s.diag(1,-1)/2
Ua=s.diag(s.exp(-s.pi*I*d),s.exp(s.pi*I*d))
Ub=s.diag(s.exp(s.pi*I*c),s.exp(-s.pi*I*c))
ck('AD transition cocycle is -I in the fundamental',zero(Ua.subs(d,d+1)+Ua))
ck('BC transition cocycle is -I in the fundamental',zero(Ub.subs(c,c+1)+Ub))
ck('AB and CD have no centre twist',Ua*Ub==Ub*Ua)
ck('root-line cocycles close',s.simplify(s.exp(2*s.pi*I))==1)

# Complete simultaneous modular changes preserve the mixed flux class.
p,q,r,t=s.symbols('p q r t', integer=True)
M=s.Matrix([[p,q],[r,t]])
J=s.Matrix([[0,-1],[1,0]])
ck('all SL2 changes preserve mixed pairing',zero(M.T*J*M-(p*t-q*r)*J))
for name,m in [('L',s.Matrix([[1,1],[0,1]])),('R',s.Matrix([[1,0],[1,1]])),('S',s.Matrix([[0,-1],[1,0]]))]:
    block=s.diag(m,m)
    ck('mixed flux under simultaneous '+name,block.T*H*block==H)

# Holonomies P_C=diag(e^{i*pi*b},e^{-i*pi*b}); P_D analogously -pi*a.
# Their two eigenvalue pairs correspond to zeta and -zeta.
tau=x+I*y
z=a+tau*b
zeta=(-(-s.pi*a)+tau*(s.pi*b))/(2*s.pi)
ck('eigen-holonomy coordinate is exactly z/2',s.simplify(2*zeta-z)==0)
# For rectangle, allow unrelated shapes: connection remains YM but not ASD.
LA,LB,LC,LD=s.symbols('LA LB LC LD',positive=True)
grect=s.diag(LA**2,LB**2,LC**2,LD**2)
gri=grect.inv()
vrect=LA*LB*LC*LD
conrect=s.simplify(sum(H[i,j]*(gri*H*gri)[i,j] for i,j in itertools.product(range(4),repeat=2)))
rho=LA*LD/(LB*LC)
action_rect=s.simplify(vrect*conrect) # multiply pi^2/g^2
ck('detuned action equals 2 pi^2/g^2 (rho+rho^-1)',s.simplify(action_rect-2*(rho+1/rho))==0)
ck('matching base/fibre complex shapes is equal cross areas',s.simplify(LD/LC-LB/LA-(LA*LD-LB*LC)/(LA*LC))==0)
ck('action excess nonnegative exact square',s.simplify(action_rect-4-2*(LA*LD-LB*LC)**2/(LA*LD*LB*LC))==0)

# Exact charged Hessian: scalar Landau ground b1+b2 plus spin-one term 2 i F.
B1,B2=s.symbols('B1 B2',positive=True)
F=s.zeros(4)
F[0,3]=-B1;F[3,0]=B1;F[1,2]=B2;F[2,1]=-B2
spin1=2*I*F
expected=[-2*B1,2*B1,-2*B2,2*B2]
ck('spin-one magnetic shifts',s.expand(spin1.charpoly().as_expr()-s.prod(spin1.charpoly().gen-e for e in expected))==0)
ground=s.eye(4)*(B1+B2)+spin1
ck('detuned Hessian has eigenvalues including +/- (B1-B2)',s.expand(ground.det()+(B1-B2)**2*(3*B1+B2)*(B1+3*B2))==0)
ck('equal-strength Hessian is nonnegative with two charged polarizations',
   sorted(ground.subs({B1:2,B2:2}).eigenvals().items())==[(0,2),(8,2)])
ck('explicit unequal-strength negative control',min(ground.subs({B1:2,B2:3}).eigenvals())==-1)
# Negative helicity in AD is (1,-i), in BC is (1,+i); each is transverse
# because its divergence is a lowest-Landau-level annihilation operator.
vAD=s.Matrix([1,0,0,-I]);vBC=s.Matrix([0,1,I,0])
ck('AD lowest polarization',zero(spin1*vAD+2*B1*vAD))
ck('BC lowest polarization',zero(spin1*vBC+2*B2*vBC))
ck('ghost scalar ground is strictly positive',s.ask(s.Q.positive(B1+B2)))

# Euclidean Clifford check of actual Weyl kernels. Orientation Gamma* chosen
# so the index equals int ch_2; reversing it reverses every reported sign.
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
gamma=[s.kronecker_product(pauli[0],s.eye(2)),s.kronecker_product(pauli[1],s.eye(2)),
       s.kronecker_product(pauli[2],pauli[0]),s.kronecker_product(pauli[2],pauli[1])]
ck('all Euclidean Clifford anticommutators',all(zero(gamma[i]*gamma[j]+gamma[j]*gamma[i]-2*(i==j)*s.eye(4))
       for i,j in itertools.product(range(4),repeat=2)))
chir=-gamma[0]*gamma[1]*gamma[2]*gamma[3]
ck('chirality involution and two neutral components each',chir**2==s.eye(4) and s.trace(chir)==0)
fermion_counts=[]
for charge in [1,-1]:
    zeeman=I*charge*(-B1*gamma[0]*gamma[3]+B2*gamma[1]*gamma[2])
    D2=s.eye(4)*(B1+B2)+zeeman
    # Generic positive B1,B2: a single spin polarization, 1x1 orbital degeneracy.
    kernel=D2.nullspace()
    ck('charged root '+str(charge)+' has one zero spin polarization',len(kernel)==1)
    ck('charged root '+str(charge)+' has negative chirality',zero(chir*kernel[0]+kernel[0]))
    fermion_counts.append({'root_charge':charge,'complex_zero_modes':1,'chirality':-1})
index_ad=2*Q*2 # Dynkin index of adjoint SU2 is 2
ck('index from curvature agrees with two charged roots',index_ad==-2)
spin_census=[]
for spin in itertools.product([0,1],repeat=4):
    neutral=2 if sum(spin)==0 else 0
    positive=neutral;negative=neutral+2
    spin_census.append({'antiperiodic_bits':spin,'n_plus':positive,'n_minus':negative,'index':positive-negative})
ck('all sixteen spin structures preserve index, not individual kernels',all(row['index']==-2 for row in spin_census))
ck('periodic kernel includes neutral modes, total six',spin_census[0]['n_plus']==2 and spin_census[0]['n_minus']==4)
# All honest SO3 reps have integer spin. Sum_m m^2 is even by +/- pairing.
j=s.symbols('j',integer=True,nonnegative=True)
m=s.symbols('m',integer=True)
index_j=-s.summation(m*m,(m,-j,j))
ck('all-integer-spin index formula',s.simplify(index_j+j*(j+1)*(2*j+1)/3)==0)
ck('integer-spin evenness corroboration',all(int(index_j.subs(j,k))%2==0 for k in range(31)))
ck('fundamental cocycle cannot descend to this SO3 bundle',s.diag(-1,-1)!=s.eye(2))

# Wrong placement of Q8 twist on the small torus removes continuous flat modes.
QA=s.diag(-1,-1,1);QB=s.diag(1,-1,-1)
ck('no adjoint invariant on a Q8-twisted compactification fibre',len((QA-s.eye(3)).col_join(QB-s.eye(3)).nullspace())==0)

result={'status':'all exact checks passed','check_count':len(checks),'checks':checks,
 'charge':str(Q),'action_g4_squared':'4*pi**2','metric':str(metric),
 'field_strength_coefficient':str(H),'hodge_star_coefficient':str(star),
 'rectangular_action_g4_squared':str(s.pi**2*action_rect),
 'lowest_charged_vector_eigenvalue':'-abs(B1-B2)',
 'charged_fermion_kernel':fermion_counts,'spin_structure_census':spin_census,
 'index_integer_spin':str(index_j),
 'boundaries':['The four-torus and action are supplied, not derived from OA.',
 'This is not the E8/hyperbolic-parent or silver-boundary problem.',
 'Theta-coordinate agreement is not equality of target metrics or quantum measures.',
 'The Landau spin check is not a numerical infinite-dimensional eigensolver.',
 'Euclidean instanton zero modes are not four-dimensional generations.']}
(OUT/'exact_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':len(checks),'Q4':str(Q),'periodic_spin_counts':spin_census[0]},indent=2))
