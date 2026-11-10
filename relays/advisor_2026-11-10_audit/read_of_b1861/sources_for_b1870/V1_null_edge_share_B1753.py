# SOURCE FOR FINDING V1 OF THE ADVISOR SEAT'S AUDIT -- a reader's script, as that reader ran it on 2026-11-10.
# One line is changed: the repository root is computed here, where the reader had typed a local path.
# NOT RE-RUN by the advisor seat, and its output was not kept. Main holds (B1870) that this computation on the
# nulls belongs behind a sealed card; this file is the source main asked for, not a result.
# NULL-ONLY diagnostic on B1753's census (the apex band): where do random hierarchies find their chi2 minimum in Im tau?
# No measured number is compared; the banked observed minimum is read from the committed comparison.json only.
import sys, json, math, pathlib, collections
sys.dont_write_bytecode=True
ROOT=pathlib.Path(__file__).resolve().parents[4]
V=ROOT/"frontier/B1753_the_six_on_the_five_ality_lines/verification"
sys.path.insert(0,str(V))
import compare as M
C=M.C
import numpy as np
A=C.arrays()
comp=json.load(open(V/"comparison.json"))
print("banked keys",[k for k in comp.keys()][:12])
d6,d9=C.draws(1789); T=np.array(d6)
F=C.chi2_features("seat",False)
im=np.array([l[2] for l in A["lab"]])
best=np.full(len(T),np.inf); arg=np.zeros(len(T),int)
for X,f in F:
    x2=(X**2).sum(1)
    for s0 in range(0,len(T),400):
        t=f(T[s0:s0+400]); c=x2[:,None]-2*X@t.T+(t**2).sum(1)[None,:]
        m=c.min(0); a=c.argmin(0); upd=m<best[s0:s0+400]
        best[s0:s0+400]=np.where(upd,m,best[s0:s0+400]); arg[s0:s0+400]=np.where(upd,a,arg[s0:s0+400])
bim=im[arg]
edges=[2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6]
h,_=np.histogram(bim,edges); rows_h,_=np.histogram(im,edges)
print("apex Im range",im.min(),im.max())
for lo,hi,n,r in zip(edges[:-1],edges[1:],h,rows_h): print("  Im [%.1f,%.1f) null-best %5d (%.1f%%)   rows share %.1f%%"%(lo,hi,n,100*n/len(T),100*r/len(im)))
print("null chi2 min quantiles 0.1%,1%,10%,50%:",np.quantile(best,[0.001,0.01,0.1,0.5]))
print("null targets below 16.75:",int((best<16.75).sum()),"of",len(T))
top=np.sort(np.unique(im))[-10:]; print("share of null bests in the 10 highest apexes (of %d): %.3f"%(len(np.unique(im)),np.isin(bim,top).mean()))
