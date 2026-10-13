#!/usr/bin/env python3
"""Direct-series and independently factored oscillator checks for Run 3.

Uses decimal-string inputs, direct tau series (no fractional-nome branches),
explicit charge traces and prime forms. These are numerical corroborations,
not interval bounds. All-domain results are proved in TECHNICAL_REPORT.md.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from functools import lru_cache
from pathlib import Path
import mpmath as mp

p=argparse.ArgumentParser();p.add_argument('--dps',type=int,default=80);args=p.parse_args()
if args.dps<40:raise ValueError('Use at least 40 decimal digits.')
mp.mp.dps=args.dps
OUT=Path(__file__).resolve().parent
J=mp.j;pi=mp.pi
R=lambda a,b=1:mp.mpf(a)/b
TOL=mp.power(10,-args.dps+16)
rows=[];groups={};negative=[]

def c(x,y):return mp.mpc(mp.mpf(x),mp.mpf(y))
def norm(x):
 if isinstance(x,(list,tuple)):return mp.sqrt(sum(abs(t)**2 for t in x))
 if isinstance(x,mp.matrix):return mp.sqrt(sum(abs(t)**2 for t in x))
 return abs(x)
def record(group,left,right,tolerance=None,tag=''):
 e=norm(left-right)/max(mp.mpf(1),norm(right)) if not isinstance(left,(list,tuple)) else norm([x-y for x,y in zip(left,right)])/max(mp.mpf(1),norm(right))
 if e>(TOL if tolerance is None else tolerance):
  raise AssertionError(f'{group}: residual {mp.nstr(e,10)} > tolerance, {tag}')
 rows.append({'group':group,'tag':tag,'relative_residual':mp.nstr(e,args.dps)})
 groups[group]=max(groups.get(group,mp.mpf(0)),e)

def ntheta(z,t):
 return int(mp.ceil(mp.sqrt((args.dps+25)*mp.log(10)/(pi*mp.im(t)))+abs(mp.im(z))/mp.im(t)+7))
@lru_cache(maxsize=4096)
def th(k,z,t,d=0):
 z,t=mp.mpc(z),mp.mpc(t)
 N=ntheta(z,t)
 if k==1:
  ans=mp.mpc(0)
  for n in range(N+1):
   a=R(2*n+1,2);v=2*pi*a
   r=d%4
   trig=[mp.sin,mp.cos,lambda x:-mp.sin(x),lambda x:-mp.cos(x)][r](v*z)
   ans+=2*((-1)**n)*mp.exp(pi*J*t*a*a)*v**d*trig
  return ans
 ans=mp.mpc(0)
 for n in range(-N,N+1):
  a=mp.mpf(n)+(R(1,2) if k==2 else 0)
  sg=(-1)**n if k==4 else 1
  ans+=sg*mp.exp(pi*J*t*a*a+2*pi*J*a*z)*(2*pi*J*a)**d
 return ans
@lru_cache(maxsize=256)
def et(t):
 t=mp.mpc(t);q=mp.exp(2*pi*J*t)
 N=int(mp.ceil((args.dps+25)*mp.log(10)/(2*pi*mp.im(t))))+8
 prod=mp.mpc(1);qn=q
 for n in range(1,N+1):prod*=1-qn;qn*=q
 return mp.exp(pi*J*t/12)*prod

def characteristic(a,b,z,t):
 return sum(mp.exp(pi*J*t*(n+a)**2+2*pi*J*(n+a)*(z+b)) for n in range(-ntheta(z,t),ntheta(z,t)+1))
def prime(z,t):return th(1,z,t)/(2*pi*et(t)**3)
# Independent oscillator products: no theta/eta calls.
def char_over_eta_product(a,z,t):
 Q=mp.exp(2*pi*J*t);ez=mp.exp(2*pi*J*z)
 N=int(mp.ceil((args.dps+25)*mp.log(10)/(2*pi*mp.im(t))))+12
 out=mp.exp(pi*J*t*(a*a-R(1,12))+2*pi*J*a*z)
 qplus=mp.exp(2*pi*J*t*(R(1,2)+a));qminus=mp.exp(2*pi*J*t*(R(1,2)-a))
 for n in range(N):out*=(1+ez*qplus)*(1+qminus/ez);qplus*=Q;qminus*=Q
 return out
def prime_product(z,t):
 Q=mp.exp(2*pi*J*t);ez=mp.exp(2*pi*J*z)
 N=int(mp.ceil(((args.dps+25)*mp.log(10)+2*pi*abs(mp.im(z)))/(2*pi*mp.im(t))))+8
 ans=mp.sin(pi*z)/pi;qn=Q
 for n in range(1,N+1):ans*=(1-ez*qn)*(1-qn/ez)/(1-qn)**2;qn*=Q
 return ans

def svec(z,t,der=0):
 P=th(1,z,t);r=mp.sqrt(P);ell=th(1,z,t,1)/P
 ans=[]
 for k in [3,2]:
  w=th(k,z,2*t)
  if der==0:a=w/r
  elif der==1:a=(th(k,z,2*t,1)-ell*w/2)/r
  elif der==2:a=(th(k,z,2*t,2)-ell*th(k,z,2*t,1)+(R(3,4)*ell**2-th(1,z,t,2)/(2*P))*w)/r
  else:raise ValueError('derivative order must be 0,1,2')
  ans.append(a)
 return mp.matrix(ans)
def amp(z,t):return et(t)*svec(z,t)
def W(a,b):return a[0]*b[1]-a[1]*b[0]
def wp_lattice(z,t):
 # Period-1 partial fraction sum, exponentially convergent along tau.
 ans=pi*pi/(mp.sin(pi*z)**2)-pi*pi/3
 N=int(mp.ceil((args.dps+20)*mp.log(10)/(2*pi*mp.im(t))))+8
 for n in range(1,N+1):
  for sg in [1,-1]:ans+=pi*pi/(mp.sin(pi*(z+sg*n*t))**2)-pi*pi/(mp.sin(pi*sg*n*t)**2)
 return ans

def cover_corr(z,t,product=False):
 T=2*t;a=R(1,4)
 f=prime_product if product else prime
 base=char_over_eta_product(a,z-t/2,T) if product else characteristic(a,0,z-t/2,T)/et(T)
 return base*f(z,T)**(-R(1,2))*f(z-t,T)**(-R(1,2))*f(-t,T)**R(1,4)
CONST=(2*pi)**R(3,4)*mp.exp(pi*J/8)
H=mp.matrix([[1,1],[1,-1]])/mp.sqrt(2);Dt=mp.matrix([[1,0],[0,J]])
P=mp.matrix([[0,0,1],[0,1,0],[1,0,0]])
M=mp.matrix([[J,0,0],[0,0,1],[0,1,0]])
moduli=[c('0','1'),c('0.13','1.2'),c('-0.21','0.93'),c('0.21','0.73'),c('0.31','1.43')]
points=[c('0.20','0.08'),c('0.29','0.13')]
for it,t in enumerate(moduli):
 for iz,z in enumerate(points):
  tag=f'tau[{it}],z[{iz}]'
  # Two independent definitions of the oscillator-normalized block.
  C=cover_corr(z,t);F=amp(z,t)
  record('bosonized cover formula equals faithful quantum amplitude',C,CONST*F[0],tag=tag)
  record('independent fermion and prime oscillator products',cover_corr(z,t,True),C,tag=tag)
  record('geometric Wronskian eta cubed',W(svec(z,t),svec(z,t,1)),-pi*et(t)**3,tag=tag)
  record('quantum Wronskian eta fifth',W(F,et(t)*svec(z,t,1)),-pi*et(t)**5,tag=tag)
  record('Lame equation with independently summed wp',svec(z,t,2),R(3,4)*wp_lattice(z,t)*svec(z,t),tag=tag)
  # The square-root branches are fixed by continuation from tau=i,0<z<1.
  # For these chosen simply-connected patches the principal roots agree.
  record('full amplitude modular T',amp(z,t+1),mp.exp(-pi*J/24)*Dt*F,tag=tag)
  record('full amplitude modular S',amp(z/t,-1/t),mp.exp(-pi*J/8)*mp.power(t,R(3,4))*H*F,tag=tag)
  record('cover prime product identity',th(1,z,2*t)*th(1,z-t,2*t),-J*mp.exp(-pi*J*t/2+pi*J*z)*et(2*t)**2/et(t)*th(1,z,t),tag=tag)
  record('shifted characteristic identity',characteristic(R(1,4),0,z-t/2,2*t),mp.exp(pi*J*z/2-pi*J*t/8)*th(3,z,2*t),tag=tag)
 # Puncture residue is a matrix element, not a state-counting character.
 U=mp.matrix([th(3,0,2*t),th(2,0,2*t)])/mp.sqrt(et(t))
 tiny=mp.power(10,-R(args.dps+8,2))
 record('puncture residue limit',mp.sqrt(2*pi*tiny)*amp(tiny,t),U,tag=f'tau[{it}]')
 K=mp.matrix([2*U[0]*U[1],U[0]**2+U[1]**2,U[0]**2-U[1]**2])
 direct=mp.matrix([th(k,0,t)**2/et(t) for k in [2,3,4]])
 record('quadratic residue reconstruction',K,direct,tag=f'tau[{it}]')
 KT=mp.matrix([th(k,0,t+1)**2/et(t+1) for k in [2,3,4]])
 KS=mp.matrix([th(k,0,-1/t)**2/et(-1/t) for k in [2,3,4]])
 record('Gaussian quadratic T multiplier',KT,mp.exp(-pi*J/12)*M*K,tag=f'tau[{it}]')
 record('Gaussian quadratic S multiplier',KS,mp.exp(-pi*J/4)*mp.sqrt(t)*P*K,tag=f'tau[{it}]')
 # Deliberately wrong target multiplier must fail.
 bad=norm(KT-mp.exp(7*pi*J/4)*M*K)/norm(K)
 assert bad>R(1,2)
 negative.append({'test':'target T multiplier is not the Gaussian multiplier','tau_index':it,'relative_error':mp.nstr(bad,args.dps)})
 record('analytic mismatch magnitude',bad,2*mp.sin(pi/12),tag=f'tau[{it}]')
 record('relative geometric versus quantum residue factor',direct,et(t)**2*mp.matrix([th(k,0,t)**2/et(t)**3 for k in [2,3,4]]),tag=f'tau[{it}]')

# Local OPE control with two distinct punctures, not a purported all-genus test.
t=c('0.17','1.03');T=2*t;pos=c('0.25','0.31');a=R(1,4)
eps=mp.power(10,-R(args.dps,2))*(1+J/5)
def general_corr(charges,positions):
 arg=sum(q*z for q,z in zip(charges,positions));out=characteristic(a,0,arg,T)/et(T)
 for i in range(len(charges)):
  for j in range(i+1,len(charges)):out*=prime(positions[i]-positions[j],T)**(charges[i]*charges[j])
 return out
# Two -1/2 punctures coalesce, becoming a -1 insertion.
C3=general_corr([1,-R(1,2),-R(1,2)],[pos,0,eps])
C2=general_corr([1,-1],[pos,0])
record('twist fusion OPE degeneration',C3/(-eps)**R(1,4),C2,tolerance=mp.power(10,-R(args.dps,2)+8))

# Explicit analytic continuation of the square root along based loops.
# Discretization determines an INTEGER branch winding, not a continuous
# determinant phase approximation. N and 2N must agree.
def branch_winding(vertices,N):
 start=vertices[0];prev=mp.arg(th(1,start,t));delta=mp.mpf(0);maxstep=0
 for a0,b0 in zip(vertices[:-1],vertices[1:]):
  for n in range(1,N+1):
   z=a0+(b0-a0)*R(n,N);arg=mp.arg(th(1,z,t));d=arg-prev
   while d>pi:d-=2*pi
   while d<=-pi:d+=2*pi
   delta+=d;maxstep=max(maxstep,abs(d));prev=arg
 integer=int(mp.nint((delta-(mp.arg(th(1,vertices[-1],t))-mp.arg(th(1,start,t))))/(2*pi)))
 assert maxstep<pi/2
 return integer
z0=c('0.17','0.11')
def Y(z):return mp.matrix([[svec(z,t)[0],svec(z,t,1)[0]],[svec(z,t)[1],svec(z,t,1)[1]]])
Z=mp.matrix([[1,0],[0,-1]]);X=mp.matrix([[0,1],[1,0]])
monodromy=[]
for label,path,expected in [
 ('A',[z0,z0+1],J*Z),
 ('B',[z0,z0+t],-J*X),
 ('commutator',[z0,z0+1,z0+1+t,z0+t,z0],-mp.eye(2))]:
 k=branch_winding(path,32);k2=branch_winding(path,64);assert k==k2
 actual=((-1)**k)*Y(path[-1])*Y(z0)**-1
 record('continued faithful quaternion monodromy',actual,expected,tag=label)
 monodromy.append({'loop':label,'root_branch_integer':k,'resolution_agrees':True})

result={'precision_decimal_digits':args.dps,'named_groups':len(groups),'individual_comparisons':len(rows),
 'largest_relative_residual':mp.nstr(max(groups.values()),args.dps),
 'strict_comparison_largest_residual':mp.nstr(max(mp.mpf(r['relative_residual']) for r in rows if r['group']!='twist fusion OPE degeneration'),args.dps),
 'groups':{k:mp.nstr(v,args.dps) for k,v in groups.items()},'comparisons':rows,
 'negative_controls':negative,'monodromy':monodromy,'field_normalization_constant':'(2*pi)^(3/4)*exp(i*pi/8)',
 'source_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'warning':'High precision comparisons, not rigorous truncation/roundoff bounds. OPE limit has an explicitly weaker finite-distance tolerance.'}
(OUT/f'amplitude_results_{args.dps}dps.json').write_text(json.dumps(result,indent=2)+'\n')
for group,err in groups.items():print('PASS',group,mp.nstr(err,8))
print('Negative target-multiplier control:',mp.nstr(bad,18))
print('COMPLETE',len(groups),'groups;',len(rows),'comparisons at',args.dps,'digits')
