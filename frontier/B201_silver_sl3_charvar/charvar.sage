# B201 (Part 1): metallic SL(3) character variety via the trace-map fixed locus (parallels B71).
from sage.all import PolynomialRing, QQ
# Bundle monodromy = T_m^2 (T_m = B48 metallic SL(3) trace map for phi_m: a->a^m b, b->a).
# m=1 must reproduce B71 (3 components: V0 geometric + W1/W2 Dehn-filling). m=2 = silver (NEW).
import time
R = PolynomialRing(QQ, ['x%d'%i for i in range(1,9)]); x = R.gens()
def Tm(coords, m):
    x1,x2,x3,x4,x5,x6,x7,x8 = coords
    tau = {-1:x6, 0:x2, 1:x3}; sig = {-1:x7, 0:x5, 1:x8}
    for k in range(2, m+2):
        tau[k] = x1*tau[k-1] - x4*tau[k-2] + tau[k-3]
        sig[k] = x4*sig[k-1] - x1*sig[k-2] + sig[k-3]
    return (tau[m], x1, tau[m+1], sig[m], x4, sig[m-1], tau[m-1], sig[m+1])
def Tm_sq(coords, m):
    return Tm(Tm(coords, m), m)
for m in (1, 2):
    t0=time.time()
    img = Tm_sq(x, m)
    eqs = [R(img[i]-x[i]) for i in range(8)]
    I = R.ideal(eqs)
    print("="*64); print("m=%d  (bundle monodromy T_%d^2)"%(m,m), flush=True)
    try:
        d = I.dimension()
    except Exception as e:
        print("  dimension failed:", e); continue
    print("  Fix(T_%d^2) ideal dimension = %d  (t=%.1fs)"%(m,d,time.time()-t0), flush=True)
    try:
        comps = I.minimal_associated_primes()
    except Exception as e:
        print("  decomposition failed/stalled:", e); continue
    print("  # components = %d  (t=%.1fs)"%(len(comps), time.time()-t0), flush=True)
    for k,P in enumerate(comps):
        g = [str(gg) for gg in P.gens()]
        # short signature: linear gens (the component-defining identifications)
        lin = [s for s in g if P.gen(g.index(s)).degree()<=1]
        print("    comp[%d] dim=%d  #gens=%d  linear: %s"%(k, P.dimension(), len(g), lin[:6]), flush=True)
print("DONE")
