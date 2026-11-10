# SOURCE FOR FINDING V1 OF THE ADVISOR SEAT'S AUDIT -- a reader's script, as that reader ran it on 2026-11-10.
# One line is changed: the repository root is computed here, where the reader had typed a local path.
# NOT RE-RUN by the advisor seat, and its output was not kept. Main holds (B1870) that this computation on the
# nulls belongs behind a sealed card; this file is the source main asked for, not a result.
# NULL-ONLY diagnostic: where do B1726's random targets find their best rows in Im tau? No measured value is compared here;
# the only data-derived number used is the banked observed statistic read from the committed comparison.json.
import sys, json, math, pathlib, collections
sys.dont_write_bytecode=True
ROOT=pathlib.Path(__file__).resolve().parents[4]
V=ROOT/"frontier/B1726_the_two_ingredients_replicated/verification"
sys.path.insert(0,str(V))
import compare as C
import numpy as np
A=C.arrays()
comp=json.load(open(V/"comparison.json"))
obs=math.log(comp["best_six"]["seat"]["best_factor"])
print("banked obs best factor",comp["best_six"]["seat"]["best_factor"],"banked mean fraction",comp["fraction_as_good_mean"]["six|seat"])
d6,d9=C.draws(1726)
im=np.array([l[2] for l in A["lab"]]); 
cnt=collections.Counter(); hits=0; hit_im=collections.Counter(); bestvals=[]
for t in d6[:4000]:
    w,i,cfg=C.best_over(t,"seat")
    cnt[round(float(im[i]),2)]+=1; bestvals.append(w)
    if w<=obs+1e-12: hits+=1; hit_im[round(float(im[i]),2)]+=1
print("null targets:",len(d6),"hits",hits,"fraction",hits/len(d6),"(banked per-seed 1726:",comp["fraction_as_good_per_seed"]["1726"]["six|seat"],")")
print("argmin Im tau histogram over null targets:")
for k in sorted(cnt): print("  %.2f %5d %s"%(k,cnt[k],"#"*(cnt[k]//20)))
print("hits by Im tau",dict(hit_im))
bv=np.exp(np.array(bestvals)); print("null best-factor quantiles 1%,5%,50%:",np.quantile(bv,[0.01,0.05,0.5]))
# how the box maps: edge share
e=cnt[2.05]+cnt[3.45]; print("share of null targets whose best row is on the window's edge (2.05 or 3.45): %.3f"%(e/len(d6)), " (uniform would be %.3f)"%(2/15))
