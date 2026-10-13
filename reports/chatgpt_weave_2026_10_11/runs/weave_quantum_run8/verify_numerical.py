#!/usr/bin/env python3
"""Independent oscillator, character-branching and modular checks for Run 8.
Uses direct analytic exponentials in tau, not principal roots of a nome.
Numerical residuals are not certified truncation/error bounds.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
from math import comb,ceil,pi
from collections import defaultdict
import mpmath as mp

ap=argparse.ArgumentParser();ap.add_argument('--dps',type=int,default=80)
args=ap.parse_args();mp.mp.dps=args.dps
if args.dps<30:raise ValueError('use at least 30 decimal digits')
HERE=Path(__file__).resolve().parent;OUT=HERE/'results';OUT.mkdir(exist_ok=True)
records=[]
def fstr(x):return mp.nstr(x,18)
def ck(name,a,b):
    if isinstance(a,mp.matrix):err=mp.norm(a-b)/max(mp.mpf(1),mp.norm(b))
    else:err=abs(a-b)/max(mp.mpf(1),abs(b))
    ok=err<mp.power(10,-args.dps+10)
    records.append({'name':name,'normalized_residual':fstr(err),'passed':bool(ok)})
    if not ok:raise AssertionError(f'{name}: {err}')
    print('PASS',name,fstr(err))
def ncut(tau):
    return max(40,int(ceil((args.dps+25)*mp.log(10)/(2*mp.pi*mp.im(tau))))+15)
def eta(tau):
    return mp.exp(mp.pi*1j*tau/12)*mp.fprod(1-mp.exp(2j*mp.pi*tau*n) for n in range(1,ncut(tau)+1))
def theta(p,tau):
    n=max(15,int(ceil(mp.sqrt((args.dps+25)*mp.log(10)/(mp.pi*mp.im(tau)))))+3)
    if p==2:return mp.fsum(mp.exp(mp.pi*1j*tau*(mp.mpf(k)+mp.mpf('0.5'))**2) for k in range(-n,n+1))
    return mp.fsum(((-1)**k if p==4 else 1)*mp.exp(mp.pi*1j*tau*k*k) for k in range(-n,n+1))
def chars(N,tau):
    pplus=pminus=mp.mpc(1);rp=mp.mpc(1)
    for n in range(1,ncut(tau)+1):
        z=mp.exp(2j*mp.pi*tau*(mp.mpf(n)-mp.mpf('0.5')))
        pplus*= (1+z)**N;pminus*=(1-z)**N
        rp*=(1+mp.exp(2j*mp.pi*tau*n))**N
    vacuum=mp.exp(-2j*mp.pi*tau*N/48)
    spinor=2**((N-1)//2)*mp.exp(2j*mp.pi*tau*N/24)*rp
    return mp.matrix([vacuum*(pplus+pminus)/2,vacuum*(pplus-pminus)/2,spinor])
# Integer Euler coefficients independently evaluated from a finite polynomial.
def euler_coeffs(power,M):
    a=[0]*(M+1);a[0]=1
    for n in range(1,M+1):
        b=[0]*(M+1)
        for k in range(M+1):
            if a[k]:
                for j in range(power+1):
                    if k+n*j<=M:b[k+n*j]+=a[k]*comb(power,j)*(-1)**j
        a=b
    return a
coef=euler_coeffs(5,180)
S=mp.matrix([[1,1,mp.sqrt(2)],[1,1,-mp.sqrt(2)],[mp.sqrt(2),-mp.sqrt(2),0]])/2
samples=[mp.mpc('0','1'),mp.mpc('.13','1.17'),mp.mpc('-.27','.91'),mp.mpc('.32','.77'),mp.mpc('1.13','1.08')]
for j,tau in enumerate(samples):
    O3,f3,s3=chars(3,tau);O5,f5,s5=chars(5,tau)
    e=eta(tau);t2,t3,t4=(theta(p,tau) for p in (2,3,4))
    O8=(t3**4+t4**4)/(2*e**4);V8=(t3**4-t4**4)/(2*e**4);S8=t2**4/(2*e**4)
    ck(f'{j}_vacuum_branch',O8,O3*O5+f3*f5)
    ck(f'{j}_vector_spinor_branch',V8,s3*s5)
    ck(f'{j}_even_ramond_branch',S8,f3*O5+O3*f5)
    ck(f'{j}_spin_triality_function_control',S8,V8)
    for N in (3,5):
        v=chars(N,tau)
        ck(f'{j}_SO{N}_S',chars(N,-1/tau),S*v)
        phases=[-mp.mpf(N)/48,mp.mpf('0.5')-mp.mpf(N)/48,mp.mpf(N)/24]
        T=mp.diag([mp.exp(2j*mp.pi*x) for x in phases])
        ck(f'{j}_SO{N}_T',chars(N,tau+1),T*v)
    B=e**5
    ck(f'{j}_quintic_inserted_trace_coefficients',mp.exp(2j*mp.pi*tau*5/24)*mp.fsum(mp.mpf(a)*mp.exp(2j*mp.pi*tau*n) for n,a in enumerate(coef)),B)
    ck(f'{j}_quintic_T',eta(tau+1)**5,mp.exp(5j*mp.pi/12)*B)
    ck(f'{j}_quintic_S',eta(-1/tau)**5,mp.exp(-5j*mp.pi/4)*mp.exp(mp.mpf('2.5')*mp.log(tau))*B)
    ck(f'{j}_relative_T_character',mp.exp(5j*mp.pi/12)/mp.exp(1j*mp.pi/4),mp.exp(1j*mp.pi/6))
    ck(f'{j}_relative_S_character',mp.exp(-5j*mp.pi/4)/mp.exp(-3j*mp.pi/4),-1j)
    # Independent oscillator determinant theta equality for five species.
    v=chars(5,tau)
    ck(f'{j}_NS_trace_square_theta', (v[0]+v[1])**2,(t3/e)**5)
    ck(f'{j}_graded_NS_trace_square_theta',(v[0]-v[1])**2,(t4/e)**5)
    ck(f'{j}_Ramond_trace_square_theta',v[2]**2,(t2/e)**5/2)
# Standard anyon data: exact rational twist exponents evaluated independently.
for nu in (3,5):
    dims=[mp.mpf(1),mp.mpf(1),mp.sqrt(2)]
    twists=[mp.mpf(1),-mp.mpf(1),mp.exp(1j*mp.pi*nu/8)]
    gauss=mp.fsum(d*d*t for d,t in zip(dims,twists))/2
    ck(f'gauss_milgram_nu_{nu}',gauss,mp.exp(2j*mp.pi*(mp.mpf(nu)/2)/8))
ck('dressed_spinor_twist',-mp.exp(-3j*mp.pi/8),mp.exp(5j*mp.pi/8))
# The relative eta2 phase is not shrinking with precision.
negative=abs(mp.exp(mp.pi*1j/6)-1)
ck('wrong_source_T_multiplier_negative_control',negative,2*mp.sin(mp.pi/12))
res={'dps':args.dps,'checks':records,'count':len(records),'maximum_normalized_residual':fstr(max(mp.mpf(r['normalized_residual']) for r in records)), 'wrong_source_T_residual':fstr(negative),'all_passed':all(r['passed'] for r in records),'limitations':'Finite direct-series/product cutoffs. No interval tail bounds. No full microscopic interface/RG or original puncture connection calculation.'}
(OUT/f'numerical_{args.dps}.json').write_text(json.dumps(res,indent=2))
print('TOTAL',res['count'],'MAX',res['maximum_normalized_residual'])
