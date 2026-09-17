import mpmath as mp, snappy, warnings; warnings.filterwarnings("ignore")
from snappy import Manifold
mp.mp.dps=60
print("="*70); print("Vol(m004) = 9 sqrt3 zeta_K(2)/pi^2, K=Q(sqrt-3)  [32-dp claim]"); print("="*70)
# L(2,chi_-3) = (1/9)[psi'(1/3) - psi'(2/3)]
L2=(mp.polygamma(1,mp.mpf(1)/3)-mp.polygamma(1,mp.mpf(2)/3))/9
zk2=mp.zeta(2)*L2
pred=9*mp.sqrt(3)*zk2/mp.pi**2
V=mp.mpf(str(Manifold('m004').high_precision().volume()))
print("  L(2,chi_-3) =",mp.nstr(L2,30))
print("  zeta_K(2)   =",mp.nstr(zk2,30))
print("  9*sqrt3*zeta_K(2)/pi^2 =",mp.nstr(pred,35))
print("  Vol(m004) (SnapPy hi-prec) =",mp.nstr(V,35))
print("  |difference| =",mp.nstr(abs(pred-V),5))
print("  agree to at least 32 significant digits:", abs(pred-V) < mp.mpf(10)**(-32)*abs(V))
cov=mp.mpf(3)**mp.mpf('1.5')*zk2/(4*mp.pi**2)
print("  covol PSL(2,O_-3) =",mp.nstr(cov,12)," (paper quotes 0.16916); Vol/covol =",mp.nstr(V/cov,20))

print(); print("="*70); print("KOIDE angle (Brannen parametrisation) vs 2/9"); print("="*70)
# sqrt(m_k) = sqrt(mu) (1 + sqrt2 cos(delta + 2 pi k/3))
def delta_from(me,mmu,mtau):
    v=[mp.sqrt(me),mp.sqrt(mmu),mp.sqrt(mtau)]
    s=sum(v)/3                      # = sqrt(mu)
    # components along cos(2pi k/3), sin(2pi k/3)
    import math
    ks=[0,1,2]
    C=sum(v[k]*mp.cos(2*mp.pi*k/3) for k in ks)
    S=sum(v[k]*mp.sin(2*mp.pi*k/3) for k in ks)
    # v_k = s(1 + sqrt2 cos(delta+2pi k/3)) -> C = s*sqrt2*(3/2)cos(delta), S = -s*sqrt2*(3/2) sin(delta)
    return mp.atan2(-S,C)
me,mmu,mtau=mp.mpf('0.51099895069'),mp.mpf('105.6583755'),mp.mpf('1776.86')
dme,dmmu,dmtau=mp.mpf('0.00000000016'),mp.mpf('0.0000023'),mp.mpf('0.12')
d0=delta_from(me,mmu,mtau)
print("  delta =",mp.nstr(d0,12),"   2/9 =",mp.nstr(mp.mpf(2)/9,12))
print("  delta - 2/9 =",mp.nstr(d0-mp.mpf(2)/9,5))
# propagate errors
import itertools
sig=mp.mpf(0)
for i,(m,dm) in enumerate([(me,dme),(mmu,dmmu),(mtau,dmtau)]):
    h=dm
    args=[me,mmu,mtau]; args2=list(args); args2[i]=args[i]+h
    dd=(delta_from(*args2)-d0)
    sig+=dd**2
sig=mp.sqrt(sig)
print("  sigma(delta) =",mp.nstr(sig,5))
print("  |delta-2/9|/sigma =",mp.nstr(abs(d0-mp.mpf(2)/9)/sig,5))
print("  paper: 0.89 sigma; difference 7.4e-6 against experimental 8.3e-6")
