#!/usr/bin/env python3
"""MEMO-55 CELL: THE SUPERPOSITION SPEAKS (C4b) — the positive half of B1151's
honest negative: the merged zeta_K spacings, which reject single-GUE at
p ~ 1e-85, are FIT by the 2-fold GUE superposition surmise at the same level
as each factor fits single-GUE — the product structure of zeta_K = zeta *
L(chi_-3) is visible in, and sufficient for, its spacing statistics.

B1151 (cc bench) located the C4 gate failure in the MERGE: per-factor
D ~ 0.040/0.049 vs merged D = 0.13365.  The named follow-up: test the merged
spacings POSITIVELY against the superposition of two independent GUE spectra.
Data: the committed raw zeros of B1151 (main @ 522c7caa), 2468 zeta + 2991
L(chi_-3) zeros to T=3000.  Same unfolding conventions as the banked cert.

THE MODEL (closed form; Wigner-surmise renewal, the same approximation family
as the single-GUE test it replaces):
  unit-density GUE gap function   E_W(s) = exp(-4s^2/pi) - s*erfc(2s/sqrt(pi))
  superposition of two independent factors with density fractions f1+f2=1:
     E(s)   = E_W(f1 s) * E_W(f2 s)
     CDF(s) = 1 + E'(s),  E'(s) = f1 E_W'(f1 s)E_W(f2 s) + f2 E_W(f1 s)E_W'(f2 s)
     E_W'(s) = -erfc(2s/sqrt(pi)) - (4s/pi) exp(-4s^2/pi)
  f_i = per-factor share of the merged count (global; drift fenced below).

PREREGISTERED (two-outcome; gates as asserts):
  A1 (anchor): reproduce B1151's per-factor numbers with its own unfolding:
     D_zeta = 0.0401, D_L = 0.0487 (to 1e-3).
  A2 (anchor): reproduce the merged single-GUE D = 0.13365 (to 1e-3) with the
     cert's merged unfolding rho_K = (1/2pi)[log(t/2pi) + log(3t/2pi)].
  S1 (the claim): D_superposition < 0.06 AND D_superposition < D_single/2 —
     the superposition surmise absorbs the merge deviation down to the
     per-factor (surmise-error) level.  Otherwise bank that negative.
  C1 (control, the discriminating direction): each SINGLE factor fits the
     superposition CDF WORSE than it fits single-GUE (the superposition is
     not a universally better fitter — it fits the merge specifically).
  Report p-values throughout; at n ~ 5459 even a correct surmise is expected
  to fail strict p > 0.01 (the surmise is an approximation detectable at
  ~2500 samples, B1151's own fence) — the preregistered claim is the D gate.
"""
import os
from math import log, pi, sqrt, erfc, exp
import numpy as np
from scipy.stats import kstest

HERE=os.path.dirname(os.path.abspath(__file__))
DATA=os.path.join(HERE,'c4data')

def read_zeros(fn): return sorted(float(x) for x in open(os.path.join(DATA,fn)) if x.strip())
zz=read_zeros('c4_zeros_zeta.txt'); zl=read_zeros('c4_zeros_L.txt')
print(f"data: {len(zz)} zeta zeros (to {zz[-1]:.2f}), {len(zl)} L(chi_-3) zeros (to {zl[-1]:.2f})")

# --- B1151's per-factor unfolding (its gue_analysis.py, verbatim logic)
def unfold_factor(ts, cond):
    us=[]
    for a,b in zip(ts,ts[1:]):
        tm=0.5*(a+b); rho=(1/(2*pi))*log(cond*tm/(2*pi))
        if rho>0: us.append((b-a)*rho)
    return np.array(us)
def gue_cdf(s):
    from scipy.special import erf as verf
    s=np.asarray(s,dtype=float)
    return verf(2*s/np.sqrt(pi))-(4*s/pi)*np.exp(-4*s*s/pi)

uz=unfold_factor(zz,1); ul=unfold_factor(zl,3)
Dz,pz=kstest(uz,gue_cdf); Dl,pl=kstest(ul,gue_cdf)
print(f"A1: zeta alone  D={Dz:.4f} (B1151: 0.0401)  p={pz:.3g}")
print(f"A1: L alone     D={Dl:.4f} (B1151: 0.0487)  p={pl:.3g}")
assert abs(Dz-0.0401)<1e-3 and abs(Dl-0.0487)<1e-3

# --- merged unfolding (the banked cert's zeta_K density)
merged=sorted(zz+zl)
def rhoK(t): return (1/(2*pi))*(log(t/(2*pi))+log(3*t/(2*pi)))
um=[]
for a,b in zip(merged,merged[1:]):
    tm=0.5*(a+b); r=rhoK(tm)
    if r>0: um.append((b-a)*r)
um=np.array(um)
Dm,pm=kstest(um,gue_cdf)
print(f"A2: merged vs single-GUE  D={Dm:.5f} (B1151: 0.13365)  p={pm:.3g}  mean={um.mean():.6f}")
assert abs(Dm-0.13365)<1e-3

# --- the superposition surmise, closed form
f1=len(zz)/(len(zz)+len(zl)); f2=1-f1
print(f"density fractions (global counts): f_zeta={f1:.4f}, f_L={f2:.4f}")
def E_W(s): return exp(-4*s*s/pi)-s*erfc(2*s/sqrt(pi))
def E_Wp(s): return -erfc(2*s/sqrt(pi))-(4*s/pi)*exp(-4*s*s/pi)
def sup_cdf_scalar(s):
    if s<=0: return 0.0
    return 1.0 + f1*E_Wp(f1*s)*E_W(f2*s) + f2*E_W(f1*s)*E_Wp(f2*s)
def sup_cdf(s):
    s=np.asarray(s,dtype=float)
    return np.array([sup_cdf_scalar(v) for v in np.atleast_1d(s)])
# model sanity: CDF(0)=0, CDF(inf)=1, unit mean (numeric)
grid=np.linspace(0,12,24001)
cdfg=sup_cdf(grid)
mean_model=np.trapezoid(1-cdfg,grid)
print(f"model sanity: CDF(0)={sup_cdf_scalar(0):.1e}, CDF(12)={sup_cdf_scalar(12):.10f}, mean={mean_model:.6f}")
assert abs(sup_cdf_scalar(12)-1)<1e-9 and abs(mean_model-1)<0.02

# --- S1: the positive test
Ds,ps=kstest(um,sup_cdf)
print(f"S1: merged vs 2-fold GUE SUPERPOSITION  D={Ds:.5f}  p={ps:.3g}")
print(f"    (single-GUE D was {Dm:.5f}; factors' own D: {Dz:.4f}/{Dl:.4f})")
assert Ds<0.06 and Ds<Dm/2

# --- C1: control — the factors themselves should NOT prefer the superposition
Dzs,_=kstest(uz,sup_cdf); Dls,_=kstest(ul,sup_cdf)
print(f"C1: zeta alone vs superposition D={Dzs:.4f} (vs GUE {Dz:.4f}); L alone D={Dls:.4f} (vs GUE {Dl:.4f})")
assert Dzs>Dz and Dls>Dl

print(f"""
THE SUPERPOSITION SPEAKS: the merged zeta_K spacings that reject single-GUE
(D={Dm:.3f}, p~1e-85) are fit by the 2-fold GUE superposition surmise at
D={Ds:.3f} — the per-factor surmise-error level — while each factor alone
prefers single-GUE over the superposition (control).  B1151's negative and
this positive are two halves of one statement: zeta_K's spacing statistics
see exactly its product structure zeta * L(chi_-3), no more and no less.
Generic (universality-class) throughout — no object-specificity claimed, no
firewall crossing; Gate 5 untouched.""")
