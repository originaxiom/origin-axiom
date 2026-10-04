"""TIER 1. The frame-bundle scale-free ratio is an L-value of Q(sqrt-3).  Requires snappy, mpmath.
NOTE: use the EXACT Hurwitz form. mpmath nsum on a periodic character mis-extrapolates (0.7725, wrong)."""
import mpmath as mp, snappy
mp.mp.dps=30
L2=(mp.zeta(2,mp.mpf(1)/3)-mp.zeta(2,mp.mpf(2)/3))/9
cov=mp.sqrt(3)*L2/8
v=float(snappy.Manifold('m004').volume())
print(f"L(2,chi_-3)={mp.nstr(L2,16)}  covolume={mp.nstr(cov,13)}  12*cov={mp.nstr(12*cov,13)}  vol(m004)={v:.13f}")
assert abs(float(12*cov)-v)<1e-9
r=cov/(16*mp.pi**2)
for nm,i in [("m004",12),("m003",12),("m202",24),("s959",36)]:
    print(f"  {nm}: ratio = {i} x {mp.nstr(r,12)} = {mp.nstr(i*r,12)}")
print("GENERIC: m003 == m004 (twins). It carries the field + index, not the object.")
