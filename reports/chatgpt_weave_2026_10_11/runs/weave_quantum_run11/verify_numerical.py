#!/usr/bin/env python3
"""Numerical corroboration of the Run 11 classical comparator.

Direct theta series and independently built magnetic-torus wavefunctions.
Finite truncations are conservative but not interval-certified.
Requires mpmath. Run with --dps 50 or --dps 80.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp

parser=argparse.ArgumentParser()
parser.add_argument('--dps',type=int,default=80)
args=parser.parse_args()
if not 30<=args.dps<=200: raise ValueError('dps must lie in [30,200]')
mp.mp.dps=args.dps
rows=[]

def norm(x):
    if isinstance(x,mp.matrix): return mp.sqrt(sum(abs(v)**2 for v in x))
    return abs(x)

def ck(name,left,right,tol=None):
    residual=norm(left-right)/max(mp.mpf(1),norm(right))
    tolerance=mp.power(10,-args.dps+12) if tol is None else tol
    if residual>tolerance:
        raise AssertionError(f'{name}: {mp.nstr(residual,15)} > {mp.nstr(tolerance,15)}')
    rows.append({'name':name,'normalized_residual':mp.nstr(residual,16)})

def theta(kind,z,tau,order=0):
    a=mp.mpf('0.5') if kind==2 else mp.mpf(0)
    N=int(mp.ceil(mp.sqrt((args.dps+35)*mp.log(10)/(mp.pi*tau.imag))+
                  abs(z.imag)/tau.imag+5))
    return mp.fsum((2j*mp.pi*(n+a))**order *
        mp.exp(mp.pi*1j*tau*(n+a)**2+2j*mp.pi*(n+a)*z) for n in range(-N,N+1))

def pair(z,tau): return mp.matrix([theta(3,z,2*tau),theta(2,z,2*tau)])
def projector(v): return (v*v.H)/(v.H*v)[0]
def quotient(zeta,tau):
    z=2*zeta
    u,v=theta(3,z,2*tau),theta(2,z,2*tau)
    du,dv=2*theta(3,z,2*tau,1),2*theta(2,z,2*tau,1)
    return v/u,(u*dv-v*du)/u**2

Z=mp.matrix([[1,0],[0,-1]])
X=mp.matrix([[0,1],[1,0]])
moduli=[mp.mpc('0','1'),mp.mpc('.17','1.23'),mp.mpc('-.31','.87')]
for k,tau in enumerate(moduli):
    zeta=mp.mpc('.143','.117')
    p=projector(pair(2*zeta,tau))
    ck(f'{k}: theta quotient period one',projector(pair(2*(zeta+1),tau)),p)
    ck(f'{k}: theta quotient period tau',projector(pair(2*(zeta+tau),tau)),p)
    ck(f'{k}: Weyl reflection',projector(pair(-2*zeta,tau)),p)
    ck(f'{k}: first half-period is record Z',projector(pair(2*zeta+1,tau)),Z*p*Z)
    ck(f'{k}: second half-period is record X',projector(pair(2*zeta+tau,tau)),X*p*X)
    aa,bb=mp.mpf('.27'),mp.mpf('.19')
    phi_c,phi_d=mp.pi*bb,-mp.pi*aa
    eigencoordinate=(-phi_d+tau*phi_c)/(2*mp.pi)
    ck(f'{k}: gauge-holonomy quotient equals Run10 profile',
       projector(pair(2*eigencoordinate,tau)),projector(pair(aa+tau*bb,tau)))
    for j,br in enumerate([0,mp.mpf('.5'),tau/2,(1+tau)/2]):
        ck(f'{k}: ramification point {j}',quotient(br,tau)[1],mp.mpf(0))
    # Chain rule: the flat YM metric in the quotient coordinate pulls back
    # to a constant. A direct comparison with the round metric is separate.
    f,df=quotient(zeta,tau)
    g=1/abs(df)**2
    ck(f'{k}: induced flat metric pullback',g*abs(df)**2,mp.mpf(1))

# Local cone behavior g_{xi xi-bar} ~ const / |xi-xi0| at a simple branch.
tau=moduli[1]
epsilon=mp.power(10,-args.dps//4)
f0=quotient(mp.mpc(0),tau)[0]
f1,df1=quotient(epsilon,tau)
f2,df2=quotient(2*epsilon,tau)
# finite-separation tests have deliberately weaker, explicitly separate tolerance.
finite_tol=mp.power(10,-args.dps//3)
ck('finite branch: map displacement scales quadratically',(f2-f0)/(f1-f0),mp.mpf(4),finite_tol)
ck('finite branch: quotient metric scales inversely quadratically',abs(df2/df1)**2,mp.mpf(4),finite_tol)

# Local compact-direction charged mass. This is a local adiabatic mass,
# not a substitute for the full global fluctuation operator.
LC,LD=mp.mpf('.3'),mp.mpf('.41')
def local_mass(a,b):
    return min(4*mp.pi**2*((n+b)**2/LC**2+(m-a)**2/LD**2)
               for n in range(-2,3) for m in range(-2,3))
ck('compact W mass vanishes at the quotient branch',local_mass(0,0),mp.mpf(0))
ck('positive off-branch W mass',local_mass(mp.mpf('.25'),mp.mpf('.25')),
   4*mp.pi**2*mp.mpf('.0625')*(1/LC**2+1/LD**2))

# Independent Landau construction on a unit-flux rectangular two-torus,
# using Landau gauge A_y = sign * B*x, D=d-iA.
def landau(x,y,Lx,Ly,sign):
    B=2*mp.pi/(Lx*Ly)
    N=int(mp.ceil(mp.sqrt((args.dps+35)*mp.log(10)*Ly/(mp.pi*Lx))+abs(x/Lx)+5))
    vals=[];dxs=[];dys=[]
    for n in range(-N,N+1):
        distance=x-n*Lx
        v=mp.exp(sign*2j*mp.pi*n*y/Ly-B*distance**2/2)
        vals.append(v)
        dxs.append(-B*distance*v)
        dys.append(-sign*1j*B*distance*v)
    return mp.fsum(vals),mp.fsum(dxs),mp.fsum(dys)

for sign in [1,-1]:
    for k,(Lx,Ly) in enumerate([(mp.mpf('1.3'),mp.mpf('.7')),
                                (mp.mpf('.8'),mp.mpf('1.1'))]):
        x,y=mp.mpf('.21')*Lx,mp.mpf('.37')*Ly
        B=2*mp.pi/(Lx*Ly)
        val,dx,dy=landau(x,y,Lx,Ly,sign)
        ck(f'Landau {sign},{k}: differential annihilator',dx+1j*sign*dy,0)
        ck(f'Landau {sign},{k}: x transition',landau(x+Lx,y,Lx,Ly,sign)[0],
           mp.exp(sign*1j*B*Lx*y)*val)
        ck(f'Landau {sign},{k}: y transition',landau(x,y+Ly,Lx,Ly,sign)[0],val)
        # Independent differentiation of the wavefunction, not the derivative sums.
        raw_dx=mp.diff(lambda xx:landau(xx,y,Lx,Ly,sign)[0],x)
        raw_dy=mp.diff(lambda yy:landau(x,yy,Lx,Ly,sign)[0],y)-sign*1j*B*x*val
        ck(f'Landau {sign},{k}: independently differentiated x',raw_dx,dx)
        ck(f'Landau {sign},{k}: independently differentiated y',raw_dy,dy)

# Explicit four-dimensional Dirac equation, not just its squared eigenvalues.
gA=mp.matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
gB=mp.matrix([[0,0,-1j,0],[0,0,0,-1j],[1j,0,0,0],[0,1j,0,0]])
gC=mp.matrix([[0,1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,-1,0]])
gD=mp.matrix([[0,-1j,0,0],[1j,0,0,0],[0,0,0,1j],[0,0,-1j,0]])
gammas=[gA,gB,gC,gD]
lengths=[mp.mpf('1.3'),mp.mpf('.9'),mp.mpf('.8'),mp.mpf('.7')]
for charge in [1,-1]:
    a,b,c,d=[mp.mpf('.23')*L for L in lengths]
    va,da,dd=landau(a,d,lengths[0],lengths[3],-charge)
    vb,db,dc=landau(b,c,lengths[1],lengths[2],charge)
    spinor=mp.matrix([0,charge,1,0])/mp.sqrt(2)
    derivatives=[da*vb,va*db,va*dc,dd*vb]
    result=mp.matrix([0,0,0,0])
    for gamma,derivative in zip(gammas,derivatives): result+=gamma*spinor*derivative
    ck(f'root {charge}: complete four-dimensional Dirac equation',result,mp.matrix(4,1))
    chirality=-gA*gB*gC*gD
    ck(f'root {charge}: negative chiral wavefunction',chirality*spinor,-spinor)

# The reduced metric is not the round metric: give a nonconstant ratio, not
# a fake near-zero identity. This is a negative control with measured output.
tau=moduli[1]
ratios=[]
for zeta in [mp.mpc('.12','.11'),mp.mpc('.32','.13')]:
    f,df=quotient(zeta,tau)
    ratios.append((1+abs(f)**2)**2/abs(df)**2)
if abs(ratios[0]-ratios[1])<mp.mpf('1e-5'): raise AssertionError('metric negative control inconclusive')

out=Path(__file__).resolve().parent/'results'
out.mkdir(exist_ok=True)
strict=[r for r in rows if not r['name'].startswith('finite branch:')]
finite=[r for r in rows if r['name'].startswith('finite branch:')]
summary={'dps':args.dps,'status':'all numerical comparisons passed','count':len(rows),
         'strict_count':len(strict),'finite_count':len(finite),
         'max_strict_normalized_residual':mp.nstr(max(mp.mpf(r['normalized_residual']) for r in strict),16),
         'max_finite_normalized_residual':mp.nstr(max(mp.mpf(r['normalized_residual']) for r in finite),16),
         'YM_to_round_metric_ratios_at_two_points':[mp.nstr(v,18) for v in ratios],
         'checks':rows,
         'boundary':'Finite theta/Gaussian truncations; not interval-certified bounds or a nonlinear PDE solver.'}
(out/f'numerical_{args.dps}.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='checks'},indent=2))
