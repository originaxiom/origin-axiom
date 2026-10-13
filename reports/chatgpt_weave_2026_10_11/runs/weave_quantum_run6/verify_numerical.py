#!/usr/bin/env python3
"""Independent direct-series tests of Run 6 identities (not interval bounds)."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp

P=argparse.ArgumentParser();P.add_argument('--dps',type=int,default=60);args=P.parse_args()
if args.dps<30:raise SystemExit('Use at least 30 digits.')
mp.mp.dps=args.dps
HERE=Path(__file__).resolve().parent;OUT=HERE/'results';OUT.mkdir(exist_ok=True)
checks=[]
tol=mp.power(10,-args.dps+8)

def eta(tau):
 if mp.im(tau)<=0:raise ValueError('tau must be in H')
 N=int(mp.ceil((args.dps+25)*mp.log(10)/(2*mp.pi*mp.im(tau))))+8
 return mp.exp(mp.pi*1j*tau/12)*mp.fprod(1-mp.exp(2*mp.pi*1j*tau*n) for n in range(1,N+1))

def theta(a,b,tau,z=0):
 N=int(mp.ceil(mp.sqrt((args.dps+30)*mp.log(10)/(mp.pi*mp.im(tau)))))+8
 return mp.fsum(mp.exp(mp.pi*1j*tau*(n+a)**2+2*mp.pi*1j*(n+a)*(z+b)) for n in range(-N,N+1))

def th2(tau):return theta(mp.mpf('.5'),0,tau)
def th3(tau):return theta(0,0,tau)
def th4(tau):return theta(0,mp.mpf('.5'),tau)
def chars(tau):return mp.matrix([th3(2*tau)/eta(tau),th2(2*tau)/eta(tau)])
def phi(tau):return eta(tau)**21*mp.matrix([th2(tau)**2,th3(tau)**2,th4(tau)**2])

def norm(x):return mp.norm(x) if isinstance(x,mp.matrix) else abs(x)
def test(name,left,right,tolerance=None):
 r=norm(left-right)/max(mp.mpf(1),norm(right));limit=tol if tolerance is None else tolerance
 checks.append({'name':name,'normalized_residual':mp.nstr(r,16),'tolerance':mp.nstr(limit,10),'passed':bool(r<limit)})
 if not r<limit:raise AssertionError(name+' residual '+str(r))
 print('PASS',name,mp.nstr(r,7))

zeta=mp.exp(mp.pi*1j/4)
OL=mp.matrix([[1,0,0],[0,0,1],[0,-1,0]])
OR=mp.matrix([[0,-1,0],[1,0,0],[0,0,1]])
TL=zeta*OL;TR=(1/zeta)*OR;TS=TR*(TL**-1)*TR
D=mp.diag([-1j,1,1j])
H=mp.matrix([[1,1],[1,-1]])/mp.sqrt(2)
U=mp.diag([1,1j])
# Independent integer oscillator coefficients to 150, not loaded from exact script.
N=150;part=[0]*(N+1);part[0]=1
for m in range(1,N+1):
 for n in range(m,N+1):part[n]+=part[n-m]
p2=[sum(part[j]*part[n-j] for j in range(n+1)) for n in range(N+1)]
coef=[]
for n in range(N+1):
 k=int(n**.5);coef.append(sum(p2[n-r*r] for r in range(-k,k+1)))

def protected_series(tau):
 return mp.exp(-mp.pi*1j*tau/6)*mp.fsum(coef[n]*mp.exp(2*mp.pi*1j*tau*n) for n in range(N+1))

samples=[mp.mpc(0,1),mp.mpc('.17','1.3'),mp.mpc('-.29','.87'),mp.mpc('.31','1.1'),mp.mpc('.07','.62')]
for k,tau in enumerate(samples):
 test(f'eta3_T_{k}',eta(tau+1)**3,zeta*eta(tau)**3)
 test(f'eta3_S_with_weight_{k}',eta(-1/tau)**3,zeta**(-3)*tau**mp.mpf('1.5')*eta(tau)**3)
 test(f'cochain_target_T_{k}',phi(tau+1),D*TL*(D**-1)*phi(tau))
 test(f'cochain_target_S_with_weight_{k}',phi(-1/tau),tau**mp.mpf('11.5')*D*TS*(D**-1)*phi(tau))
 test(f'ordinary_su2_characters_T_{k}',chars(tau+1),mp.exp(-mp.pi*1j/12)*U*chars(tau))
 test(f'ordinary_su2_characters_S_{k}',chars(-1/tau),H*chars(tau))
 test(f'protected_character_vs_independent_oscillator_series_{k}',th3(2*tau)/eta(tau)**2,protected_series(tau))
 # The bare line character must NOT be confused with eta^3 as a weight-zero flat section.
 E2=1-24*mp.fsum(n*mp.exp(2*mp.pi*1j*tau*n)/(1-mp.exp(2*mp.pi*1j*tau*n)) for n in range(1,250))
 derivative=mp.diff(lambda z:eta(z)**3,tau)/(2*mp.pi*1j*eta(tau)**3)
 test(f'eta3_not_a_flat_constant_frame_{k}',derivative,E2/8)
 # Tensor-map equality for a generic neutral observable, separate from amplitude dynamics.
 X=mp.matrix([[1,2+1j,-3],[2-1j,4,mp.mpf('.7')],[-3,mp.mpf('.7'),-5]])
 for tag,T,O in [('L',TL,OL),('R',TR,OR)]:
  test(f'neutral_endomorphism_transport_{tag}_{k}',T*X*(T**-1),O*X*(O**-1))

# Direct nonzero-parameter checks of the protected charge classification, using
# the original four flavour charges, not pre-reduced A/B weights.
def weights(q,t):
 L1,L2,R1,R2=map(mp.mpf,q)
 aL=(L1-L2)/mp.sqrt(2);aR=(R1-R2)/mp.sqrt(2)
 bL=(L1+L2)/mp.sqrt(2);bR=(R1+R2)/mp.sqrt(2)
 c=mp.cosh(t);s=mp.sinh(t)
 return ((aL*aL+(c*bL+s*bR)**2)/2,(aR*aR+(s*bL+c*bR)**2)/2)
for n in [-3,-1,0,2,4]:
 for tt in ['-.61','.27','.83']:
  h,hb=weights((n,-n,0,0),mp.mpf(tt))
  test(f'protected_charge_h_n{n}_t{tt}',h,mp.mpf(n*n))
  test(f'protected_charge_hbar_n{n}_t{tt}',hb,mp.mpf(0))

report={'precision':args.dps,'count':len(checks),'max_normalized_residual':max([mp.mpf(c['normalized_residual']) for c in checks]),'all_passed':all(c['passed'] for c in checks),'checks':checks,'scope':'High precision corroborations with finite direct theta/product truncations; no certified interval tail bounds. No nonabelian defect connection calculated.'}
report['max_normalized_residual']=mp.nstr(report['max_normalized_residual'],18)
(OUT/f'numerical_{args.dps}.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('TOTAL',len(checks),'CHECKS; MAX',report['max_normalized_residual'])
