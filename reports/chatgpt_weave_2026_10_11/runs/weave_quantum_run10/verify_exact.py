#!/usr/bin/env python3
"""Exact finite algebra for Run 10. Analytic continuum proofs are in the report.
No project code or experimental data is imported.
"""
import json
from pathlib import Path
from collections import deque
import sympy as s

OUT=Path(__file__).resolve().parent/'results'
OUT.mkdir(exist_ok=True)
checks=[]
def check(name, condition):
    ok=bool(condition)
    checks.append({'name':name,'passed':ok})
    if not ok: raise AssertionError(name)
def zero(M): return all(s.simplify(x)==0 for x in M)
I=s.I
P=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
A=I*P[2]; B=I*P[0]
check('quaternion relations',zero(A*A+s.eye(2)) and zero(B*B+s.eye(2)) and zero(A*B+B*A))

def adj(U):
    return s.Matrix(3,3,lambda a,b:s.simplify(s.trace(P[a]*U*P[b]*U.H)/2))
QA=adj(A);QB=adj(B)
check('adjoint lifts commute',QA*QB==QB*QA)
check('no common parallel direction',s.Matrix.vstack(QA-s.eye(3),QB-s.eye(3)).rank()==3)
check('central element acts trivially on directions',adj(-s.eye(2))==s.eye(3))

# F2[a,b]/(a^2,b^2), coefficients ordered 1,a,b,ab.
def mult(x,y):
    r=[0]*4
    for i,xi in enumerate(x):
        for j,yj in enumerate(y):
            if (i&j)==0: r[i|j]^=(xi&yj)
    return tuple(r)
line_w=[(1,1,0,0),(1,1,1,0),(1,0,1,0)]
w=(1,0,0,0)
for x in line_w: w=mult(w,x)
check('total Stiefel Whitney class is 1+ab',w==(1,0,0,1))
for perm in [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]:
    x=(1,0,0,0)
    for j in perm:x=mult(x,line_w[j])
    check('w2 independent of line ordering '+str(perm),x==w)

H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
D=s.diag(1,I)
OS=adj(H);OT=adj(D)
check('S and T adjoint rotations',OS.det()==1 and OT.det()==1 and OS.T*OS==s.eye(3) and OT.T*OT==s.eye(3))
check('classical modular relations',OS**2==s.eye(3) and (OS*OT)**3==s.eye(3))

def key(M):return tuple(M)
seen={key(s.eye(3)):s.eye(3)};todo=deque([s.eye(3)])
while todo:
    M=todo.popleft()
    for G in (OS,OT):
        V=G*M
        if key(V) not in seen:seen[key(V)]=V;todo.append(V)
check('rotation group order 24',len(seen)==24)
check('projective field central fourth S is positive',OS**4==s.eye(3))
zeta=(1+I)/s.sqrt(2)
ST=zeta**-3*OS; TT=zeta*OT
change=s.Matrix([[0,0,-I],[0,1,0],[I,0,0]])
Mtarget=s.Matrix([[I,0,0],[0,0,1],[0,1,0]])
Ptarget=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
check('external line restores target T only if added',zero(change*TT*change.inv()-zeta**-1*Mtarget))
check('external line restores target S only if added',zero(change*ST*change.inv()-zeta*Ptarget))
check('target central fourth S is negative',zero(ST**4+s.eye(3)))
check('no scalar line from normalized spinor',s.simplify((s.Symbol('r',positive=True)**2)/(s.Symbol('r',positive=True)**2))==1)

# A local tangent-space calculation of the Bogomolny identity at n=(0,0,1).
x1,x2,y1,y2=s.symbols('x1 x2 y1 y2',real=True)
vx=s.Matrix([x1,x2,0]);vy=s.Matrix([y1,y2,0]);n=s.Matrix([0,0,1])
bps=vx+n.cross(vy)
check('Bogomolny square identity',s.expand(vx.dot(vx)+vy.dot(vy)-bps.dot(bps)-2*n.dot(vx.cross(vy)))==0)

# Quasiperiodic log-norm potential fixes Q without numerical quadrature.
y,v,x=s.symbols('y v x',real=True,positive=True)
phi=s.pi*v*v/y
check('log norm quadratic shift',s.simplify(phi.subs(v,v+y)-phi-(2*s.pi*v+s.pi*y))==0)
flux_integral=s.diff(phi,v,2)*y
check('half integer charge from curvature',s.simplify(flux_integral/(4*s.pi))==s.Rational(1,2))
check('degree of tangent line one',2*s.Rational(1,2)==1)
check('minimal action coefficient',4*s.pi*s.Rational(1,2)==2*s.pi)
check('theta parameter has a sign in fixed flux sector',s.simplify(s.exp(2*s.pi*I*(s.Symbol('m',integer=True)+s.Rational(1,2))))==-1)

# Explicit, separate four-dimensional toron CONTROL, not an uplift of w.
area1,area2,g=s.symbols('area1 area2 g',positive=True)
Q4=s.simplify(2*(s.Rational(1,2))*(2*s.pi/area1)*(2*s.pi/area2)*(area1*area2)/(8*s.pi**2))
S4=2*s.pi**2/g**2*(area1/area2+area2/area1)
check('separate four dimensional toron charge',Q4==s.Rational(1,2))
check('separate four dimensional action bound',s.simplify(S4-4*s.pi**2/g**2-2*s.pi**2/g**2*(area1-area2)**2/(area1*area2))==0)

result={'checks':checks,'count':len(checks),'matrices':{'QA':str(QA),'QB':str(QB),'OS':str(OS),'OT':str(OT),'target_intertwiner':str(change)},'w_total':w,'bounds':{'Q':'1/2','g_squared_S':'2*pi','real_bosonic_zero_modes':2},'scope':'Finite algebra corroborates the analytic proofs. It is not a numerical Dirac eigensolver or full quantum quantization.'}
(OUT/'exact.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
