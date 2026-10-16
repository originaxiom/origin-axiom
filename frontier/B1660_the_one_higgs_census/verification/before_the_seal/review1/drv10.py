import os,sys,time,math,json
for k in ("OMP_NUM_THREADS","VECLIB_MAXIMUM_THREADS","OPENBLAS_NUM_THREADS"): os.environ[k]="1"
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import cc10 as cc
from multiprocessing import Pool
if __name__=="__main__":
    var=sys.argv[1]; li=int(sys.argv[2]); n=int(sys.argv[3])
    t0=time.time(); cc.build(); print("build",time.time()-t0, "CMIN", {i:round(v,2) for i,v in list(cc.CMIN.items())[:3]}, "min over lines", min(cc.CMIN.values()),flush=True)
    ln=cc.LINES18[li]
    with Pool(4,initializer=cc.init,initargs=(cc.PARTS,cc.CMIN)) as pool:
        t0=time.time()
        res=pool.map(cc.fit,[(var,li,cc.DMU,90000+k) for k in range(n)],chunksize=1); res.sort(key=lambda r:r[0])
        print("data",var,li,"time/fit(4w)",(time.time()-t0)/n*4,"best",res[0][0],"sorted",[round(r[0],1) for r in res[:12]],flush=True)
        S,L=cc.unpack(res[0][1]); q=cc.svs(var,S,ln,L); mus={(s,k):math.log(q[s][k]/q[s][0]) for s,k in cc.KEYS}
        print("best L",L,"2piL+cmin",2*np.pi*L+cc.CMIN[ln],flush=True)
        res2=pool.map(cc.fit,[(var,li,mus,91000+k) for k in range(n)],chunksize=1); b=sorted(r[0] for r in res2)
        print("plant",var,li,"sorted",[f"{x:.1e}" for x in b[:8]],"n<0.1:",sum(x<0.1 for x in b),"of",n,flush=True)
