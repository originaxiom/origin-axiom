import sys, math, time, numpy as np
sys.path.insert(0, '.')
import routeA as B
def ct(tau, eps=1e-5): return np.array([B.cA(r, tau, eps) - math.pi*math.log(tau.imag) for r in (2, 4, 3)])
S=np.array([[0,-1],[1,0]]); T=np.array([[1,1],[0,1]]); Ti=np.array([[1,-1],[0,1]])
G={'S':S,'TS':T@S,'ST':S@T,'TiS':Ti@S,'STi':S@Ti,'TST':T@S@T}
mob=lambda g,t:(g[0,0]*t+g[0,1])/(g[1,0]*t+g[1,1])
pts=[0.31+0.86j, -0.42+0.92j, 0.05+0.81j, 0.47+1.05j, -0.2+0.78j]
t0=time.time()
for t in pts:
    a=ct(t)
    for name,g in G.items():
        tg=mob(g,t)
        if tg.imag<0.75: continue
        b=ct(tg)
        print(f"{t} {name:4s} tg={tg:.3f}  sorted diff {np.max(np.abs(np.sort(a)-np.sort(b))):.2e}   c~(t)={np.round(a,4)}", flush=True)
print('time', time.time()-t0)
