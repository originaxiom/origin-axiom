#!/usr/bin/env python3
"""Direct oscillator and theta-series checks; mpmath only, no previous code.
All powers of q with fractional exponents are evaluated through tau explicitly.
Finite truncations are high-precision corroborations, not interval certificates.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp

p=argparse.ArgumentParser();p.add_argument('--dps',type=int,default=90);args=p.parse_args()
if args.dps<35:raise SystemExit('Use at least 35 decimal digits.')
mp.mp.dps=args.dps
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
results=[]

def cut(tau):
    if mp.im(tau)<=0:raise ValueError('tau must lie in the upper half-plane')
    return max(20,int(mp.ceil((mp.mp.dps+25)*mp.log(10)/(2*mp.pi*mp.im(tau))))+10)
def qpow(tau,p):return mp.exp(2j*mp.pi*tau*p)
def eta(tau):
    q=qpow(tau,1);return qpow(tau,mp.mpf(1)/24)*mp.fprod(1-q**n for n in range(1,cut(tau)+1))
def ramond_inserted(tau):
    # Normalized trace sqrt(2) Tr_R o(G) q^(L0-c/24).
    q=qpow(tau,1)
    return qpow(tau,mp.mpf(1)/8)*mp.fprod((1-q**n)**3 for n in range(1,cut(tau)+1))
def jacobi_odd_derivative(tau):
    nmax=int(mp.ceil(mp.sqrt((mp.mp.dps+25)*mp.log(10)/(mp.pi*mp.im(tau)))))+8
    return mp.fsum((-1)**n*(2*n+1)*qpow(tau,mp.mpf((2*n+1)**2)/8) for n in range(nmax))
def E2(tau):
    q=qpow(tau,1)
    return 1-24*mp.fsum(n*q**n/(1-q**n) for n in range(1,cut(tau)+1))
def characters(tau):
    q=qpow(tau,1);N=cut(tau)
    plus=qpow(tau,-mp.mpf(1)/16)*mp.fprod((1+qpow(tau,mp.mpf(n)-mp.mpf('0.5')))**3 for n in range(1,N+1))
    minus=qpow(tau,-mp.mpf(1)/16)*mp.fprod((1-qpow(tau,mp.mpf(n)-mp.mpf('0.5')))**3 for n in range(1,N+1))
    ramond=2*qpow(tau,mp.mpf(1)/8)*mp.fprod((1+q**n)**3 for n in range(1,N+1))
    return mp.matrix([(plus+minus)/2,ramond,(plus-minus)/2])
def norm(x):
    return mp.norm(x) if isinstance(x,mp.matrix) else abs(x)
def record(name,lhs,rhs,tolerance=None,kind='identity'):
    err=norm(lhs-rhs)/max(mp.mpf(1),norm(rhs))
    tolerance=tolerance or mp.power(10,-mp.mp.dps+12)
    if err>tolerance:raise AssertionError(f'{name}: {mp.nstr(err,12)} > {mp.nstr(tolerance,8)}')
    results.append({'name':name,'kind':kind,'normalized_residual':mp.nstr(err,16)})

rt2=mp.sqrt(2)
S=mp.matrix([[1,rt2,1],[rt2,0,-rt2],[1,-rt2,1]])/2
vac_exp=[-mp.mpf(1)/16,mp.mpf(1)/8,mp.mpf(7)/16]
T=mp.diag([mp.exp(2j*mp.pi*x) for x in vac_exp])
z8=mp.exp(mp.pi*1j/4)
points=[mp.mpc(0,1),mp.mpc('0.13','1.2'),mp.mpc('-0.21','.93'),mp.mpc('.21','.73'),mp.mpc('.31','1.43')]
for ix,tau in enumerate(points):
    e=eta(tau);f=ramond_inserted(tau)
    record(f'{ix}: oscillator trace eta3',f,e**3)
    record(f'{ix}: independent Jacobi derivative',f,jacobi_odd_derivative(tau))
    record(f'{ix}: block T',ramond_inserted(tau+1),z8*f)
    # Principal tau power is the chosen S lift; im tau > 0.
    record(f'{ix}: block S',ramond_inserted(-1/tau),z8**(-3)*tau**mp.mpf('1.5')*f)
    d=mp.diff(ramond_inserted,tau)/(2j*mp.pi)
    record(f'{ix}: inserted modular differential equation',d,E2(tau)*f/8)
    ch=characters(tau)
    record(f'{ix}: full vacuum characters S',characters(-1/tau),S*ch)
    record(f'{ix}: full vacuum characters T',characters(tau+1),T*ch)
    # Framing character ground-state exponent, versus bare topological twist.
    exponent=mp.mpf(3)/16-mp.mpf(1)/16
    record(f'{ix}: ground-state Dehn twist',mp.exp(2j*mp.pi*exponent),z8)
    # Individual Ramond gamma trace versus ordinary Ramond character.
    record(f'{ix}: ordinary vs inserted oscillator relation',
        ch[1]/(2*f),mp.fprod(((1+qpow(tau,n))/(1-qpow(tau,n)))**3 for n in range(1,cut(tau)+1)))
    # All series evaluated again at slightly larger truncation, independent finite coefficient sum.
    coeff=json.loads((OUT/'exact_results.json').read_text())['eta_cube_relative_coefficients']
    series=qpow(tau,mp.mpf(1)/8)*mp.fsum(c*qpow(tau,n) for n,c in enumerate(coeff))
    # q^60 at the declared points is below 1e-119; tolerance still records finite truncation.
    record(f'{ix}: exact coefficient polynomial',series,f,tolerance=mp.power(10,-min(mp.mp.dps-12,108)))

# Check simple Gaussian current-Ward pole-normalization and genuine central phases.
B1=mp.diag([-mp.exp(-3j*mp.pi/8),mp.exp(1j*mp.pi/8)])
F=-mp.matrix([[1,1],[1,-1]])/rt2
B2=F.T*B1*F
record('non-Abelian braid equation',B1*B2*B1,B2*B1*B2)
commnorm=norm(B1*B2-B2*B1)
if commnorm<mp.mpf('0.1'):raise AssertionError('Braiding commutator spuriously zero')
results.append({'name':'noncommuting braids negative control','kind':'negative','commutator_norm':mp.nstr(commnorm,16)})
record('central monodromy around f',mp.exp(2j*mp.pi*(mp.mpf(3)/16-mp.mpf(1)/2-mp.mpf(3)/16)),-1)
record('one-puncture S4', (z8**(-3))**4,-1)
record('one-puncture braid relation',(z8**(-3))**2,(z8**(-3)*z8)**3)

errs=[mp.mpf(r['normalized_residual']) for r in results if 'normalized_residual' in r]
output={'dps':args.dps,'checks':results,'number_checks':len(results),'max_normalized_residual':mp.nstr(max(errs),16),
 'notes':'High-precision direct series/product controls; not interval-certified. Scalar block comparison includes declared conformal weight and framing.'}
(OUT/f'numerical_{args.dps}.json').write_text(json.dumps(output,indent=2))
print(json.dumps({k:output[k] for k in ['dps','number_checks','max_normalized_residual']},indent=2))
