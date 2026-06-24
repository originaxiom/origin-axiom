"""'U sure?' check: is the SL5 o5 'clean exponent = ~1% sublocus' GENUINE or a numerical artifact?
For loxodromic (order(mu)=inf) irreducible reps ON the variety (tiny relresid), is the best-k
exponent error O(1) [genuine: they satisfy NO integer exponent -> sublocus real] or ~relresid*cond
[numerical -> the correction would be wrong]?"""
import sys, numpy as np
sys.path.insert(0,'frontier/B199_metallic_exponent_law')
from geom_grid import make_A, newton_t, irred, mu_order
n,o,exps=5,5,[0,1,2,3,4]
A,Ai,Ai2=make_A(o,exps); gfix=list(range(n-1))
def bestk(B,t):
    comm=A@B@Ai@np.linalg.inv(B); mu=Ai@t
    errs=[min(np.max(np.abs(comm-np.linalg.matrix_power(mu,k))),
              np.max(np.abs(comm+np.linalg.matrix_power(mu,k)))) for k in range(1,9)]
    return min(range(1,9),key=lambda k:errs[k-1]), min(errs)
clean=[]; notclean=[]
rng=np.random.default_rng(0); found=0
for s in range(6000):
    t,r=newton_t(A,Ai,Ai2,n,gfix,rng)
    if t is None or r>1e-11 or abs(np.linalg.det(t))<1e-3 or np.linalg.cond(t)>1e6: continue
    B=Ai2@t@A@np.linalg.inv(t)
    mu=Ai@t
    if np.max(np.abs(mu-t))<1e-6 or irred(A,B,n)!=n*n: continue
    order,off=mu_order(mu)
    if order is not None: continue   # keep only loxodromic/infinite-order
    k,e=bestk(B,t); found+=1
    rec=(e, r, np.linalg.cond(t), k)
    (clean if e<1e-6 else notclean).append(rec)
    if found>=60: break
print("loxodromic irreducible reps:",found)
print("  CLEAN (best-k err<1e-6):",len(clean))
print("  NOT-CLEAN:",len(notclean))
if notclean:
    es=np.array([x[0] for x in notclean]); rs=np.array([x[1] for x in notclean]); cs=np.array([x[2] for x in notclean])
    print("  not-clean best-k err: min=%.2e median=%.2e max=%.2e"%(es.min(),np.median(es),es.max()))
    print("  not-clean relresid:   median=%.2e   cond(t): median=%.1f"%(np.median(rs),np.median(cs)))
    print("  ratio err/(relresid*cond) median=%.2e  (>>1 => GENUINE no-exponent; ~1 => numerical)"%np.median(es/(rs*cs)))
if clean:
    print("  clean best-k values:", sorted(set(x[3] for x in clean)))
