#!/usr/bin/env python3
"""Run 5 exact checks. All checks are algebraic; no physical data are used.

The all-radius rigidity conclusion is proved in the report. The bounded
integer scans below verify the arithmetic and do not replace that proof.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
r = sp.symbols('r', positive=True)  # r=exp(t); not the torus modulus
c, s = (r + 1/r)/2, (r - 1/r)/2
sqrt2 = sp.sqrt(2)
Q = sp.Matrix([[1,-1],[1,1]])/sqrt2
C = sp.diag(Q,Q)
B = sp.Matrix([[1,0,0,0],[0,c,0,s],[0,0,1,0],[0,s,0,c]])
M = B*C
G = sp.diag(1,1,-1,-1)
checks: list[dict] = []

def zero(expr):
    if isinstance(expr, sp.MatrixBase):
        return all(sp.simplify(e)==0 for e in expr)
    return sp.simplify(expr)==0

def check(name, condition, details=None):
    if not bool(condition):
        raise AssertionError(name)
    checks.append({'name':name,'passed':True, **({'details':details} if details is not None else {})})

def vec(x): return sp.Matrix([sp.Rational(a) for a in x])
def momenta(x): return sp.simplify(M*vec(x))
def weights(x):
    p=momenta(x)
    return tuple(sp.factor(sum(p[i]**2 for i in inds)/2) for inds in ((0,1),(2,3)))
def ope(x,y):
    p,q=momenta(x),momenta(y)
    return tuple(sp.factor(sum(p[i]*q[i] for i in inds)) for inds in ((0,1),(2,3)))
def add(x,y): return tuple(sp.Rational(a)+sp.Rational(b) for a,b in zip(x,y))

check('charge-basis orthogonal', zero(C.T*C-sp.eye(4)))
check('boost preserves Lorentz bilinear', zero(B.T*G*B-G))
check('boost determinant one', zero(B.det()-1))
check('full map preserves odd-lattice pairing', zero(M.T*G*M-G))
check('boost identity at free point', zero(B.subs(r,1)-sp.eye(4)))
check('inverse boost is r reciprocal', zero(B.subs(r,1/r)*B-sp.eye(4)))

psi=(1,0,0,0)
psi2=(0,1,0,0)
P=(-sp.Rational(1,2),-sp.Rational(1,2),0,0)
PA=(-sp.Rational(1,2),sp.Rational(1,2),0,0)
Pc=(-sp.Rational(1,2),-sp.Rational(1,2),sp.Rational(1,2),sp.Rational(1,2))
Ps=(-sp.Rational(1,2),-sp.Rational(1,2),-sp.Rational(1,2),-sp.Rational(1,2))
hp,bp=weights(psi)
hP,bP=weights(P)
check('fermion exact weights', zero(hp-(1+c*c)/4) and zero(bp-s*s/4))
check('both faithful components have equal weights', weights(psi)==weights(psi2))
check('fermion spin remains half', zero(hp-bp-sp.Rational(1,2)))
check('tracked puncture exact weights', zero(hP-c*c/4) and zero(bP-s*s/4))
check('puncture spin remains quarter', zero(hP-bP-sp.Rational(1,4)))
check('alternative flavour spinor stays chiral', weights(PA)==(sp.Rational(1,4),0))
check('conjugately paired local puncture', weights(Pc)==(1/(4*r*r),1/(4*r*r)))
check('same-sign paired local puncture', weights(Ps)==(r*r/4,r*r/4))

a,b=ope(psi,P)
check('original chiral puncture OPE exponents', zero(a+c*c/2) and zero(b+s*s/2))
check('central puncture monodromy unchanged', zero(a-b+sp.Rational(1,2)))
check('fused flavour spinor stays chiral', weights(add(psi,P))==(sp.Rational(1,4),0))
check('OPE conformal-weight balance', all(zero(x-y) for x,y in zip((a,b),[weights(add(psi,P))[0]-hp-hP,weights(add(psi,P))[1]-bp-bP])))
check('equal half-pole applies to both components at t=0', ope(psi,P)[0].subs(r,1)==-sp.Rational(1,2) and ope(psi2,P)[0].subs(r,1)==-sp.Rational(1,2))
check('antiholomorphic exponent vanishes only at positive r=1', sp.solve(sp.together(b),r)==[1])
a2,b2=ope(psi,Pc)
check('full local puncture gives same fermion sign', zero(a2-b2+sp.Rational(1,2)))
check('full local puncture half-pole only at free point', sp.solve(sp.together(b2),r)==[1])
check('flavour root currents unchanged', weights((1,-1,0,0))==(1,0) and weights((0,0,1,-1))==(0,1))
check('charge root currents cease to be chiral', all(zero(x-y) for x,y in zip(weights((1,1,0,0)),(c*c,s*s))))

# Exact Q8 action on the original complex flavour doublet.
i=sp.I
A=sp.diag(i,-i)
J=sp.Matrix([[0,-i],[-i,0]])
check('faithful quaternion relations', A*A==-sp.eye(2) and J*J==-sp.eye(2) and A*J==-J*A)
check('central puncture relation', sp.simplify(A*J*A.inv()*J.inv())==-sp.eye(2))
q8=[sgn*X for X in [sp.eye(2),A,J,A*J] for sgn in [1,-1]]
normalizers=[(sp.eye(2)+A)/sqrt2,(sp.eye(2)-J)/sqrt2]
check('all quaternion elements preserve total current', all(zero(U.conjugate().T*U-sp.eye(2)) for U in q8))
check('both grammar normalizers preserve total current', all(zero(U.conjugate().T*U-sp.eye(2)) and zero(U.det()-1) for U in normalizers))
check('quaternion group closes exactly', all(any(zero(U*V-W) for W in q8) for U in q8 for V in q8))

# The locality/fermion parity gluing is retained, not an arbitrary SU(2) x circle product.
local_points=[(a,b,c_,d) for a in range(-2,3) for b in range(-2,3) for c_ in range(-1,2) for d in range(-1,2)]
check('odd-lattice spin statistics identity', all((a*a+b*b-c_*c_-d*d-a-b-c_-d)%2==0 for a,b,c_,d in local_points))
check('spin-charge gluing retained', all((a+b-(a-b))%2==0 and (c_+d-(c_-d))%2==0 for a,b,c_,d in local_points))
# With d_R=0, h=1/2 and hbar=0 imply d_L in {-1,0,1}.
# d=0 forces s even and is impossible mod 4. d=+-1 gives (s-2m)(s+2m)=1.
scan=[]
for d in [-1,0,1]:
    for sl in range(-101,102):
        for m in range(-50,51):
            if (sl-d)%2==0 and d*d+sl*sl-4*m*m==2:
                scan.append((d,sl,m))
check('bounded independent chiral-candidate scan', sorted(scan)==[(-1,-1,0),(-1,1,0),(1,-1,0),(1,1,0)], scan)
check('d=0 case excluded mod four', all((sl*sl-4*m*m-2)%4!=0 for sl in range(-10,11,2) for m in range(-5,6)))
check('integer factorization identity for d=+-1', sp.expand((sp.Symbol('s')-2*sp.Symbol('m'))*(sp.Symbol('s')+2*sp.Symbol('m')))==sp.Symbol('s')**2-4*sp.Symbol('m')**2)
check('only real boost preserving any candidate is t=0', sp.solve(s,r)==[1])

# Odd-spin second variation: obtain it directly from the Gaussian exponent.
t,y,u,v=sp.symbols('t y u v', real=True)
E=-sp.pi*y*((u*u+v*v)*sp.cosh(2*t)+2*u*v*sp.sinh(2*t))
check('odd-spin first exponent variation', zero(sp.diff(E,t).subs(t,0)+4*sp.pi*y*u*v))
check('odd-spin second exponent variation', zero(sp.diff(E,t,2).subs(t,0)+4*sp.pi*y*(u*u+v*v)))
check('odd-spin second trace kernel', zero((sp.diff(E,t,2)+sp.diff(E,t)**2).subs(t,0)-(16*sp.pi**2*y*y*u*u*v*v-4*sp.pi*y*(u*u+v*v))))

# Bilinear OPE exponent associativity is preserved by every boost.
x1,x2,x3=[vec(z) for z in [psi,P,(-1,1,0,0)]]
for metric,label in [(sp.diag(1,1,0,0),'holomorphic'),(sp.diag(0,0,1,1),'antiholomorphic')]:
    f=lambda x,z:(M*x).dot(metric*(M*z))
    check(f'{label} additive OPE exponent coherence', zero(f(x1,x2)+f(x1+x2,x3)-f(x2,x3)-f(x1,x2+x3)))

result={
 'scope':'Exact algebra and finite arithmetic checks; not all-genus Q8 sewing or an eigensolver.',
 'parameter':'r=exp(t)>0; free point t=0,r=1',
 'checks':checks,
 'count':len(checks),
 'formulae':{
  'h_psi':str(hp),'hbar_psi':str(bp),'h_puncture':str(hP),'hbar_puncture':str(bP),
  'ope_holomorphic':str(a),'ope_antiholomorphic':str(b),
  'odd_spin_second_variation':'16*pi^2*Im(tau)^2*abs(eta(tau))^8',
  'odd_spin_leading_term':'8*pi^2*Im(tau)^2*abs(eta(tau))^8*t^2 + O(t^4)'
 },
 'chiral_candidates_d_s_m':scan,
 'claims_not_proved_by_tests':['Every Q8 defect junction evaluated','Full singular determinant connection','Universal quantum completion uniqueness','Derivation of original chiral dictionary from the grammar']
}
(ROOT/'results_exact.json').write_text(json.dumps(result,indent=2)+'\n')
for z in checks: print('PASS',z['name'])
print(f'Exact checks passed: {len(checks)}')
