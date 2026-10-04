"""Every all-regular-tetrahedral census manifold: is CS (mod 1/2) exactly rational, denominator | 24?
Base rate included: non-arithmetic manifolds should give IRRATIONAL CS."""
import snappy
from fractions import Fraction as F
from collections import Counter
h=complex(0.5,0.8660254037844386)
reg=lambda M: all(min(abs(complex(z)-h),abs(complex(z)-h.conjugate()))<1e-9 for z in M.tetrahedra_shapes('rect'))
d=Counter(); n=0; bad=0
for k,M in enumerate(snappy.OrientableCuspedCensus):
    if k>=6000: break
    try:
        if not reg(M): continue
        n+=1; cs=float(M.chern_simons())%0.5; f=F(cs).limit_denominator(1000)
        if abs(float(f)-cs)>1e-9: bad+=1
        else: d[f.denominator]+=1
    except Exception: pass
print(f"regular-tetrahedral: {n}, non-rational CS: {bad}, denominators {dict(sorted(d.items()))}")
print("base rate (non-arithmetic):", [round(float(snappy.Manifold(m).chern_simons())%0.5,9) for m in ['m006','m011','m015']])
