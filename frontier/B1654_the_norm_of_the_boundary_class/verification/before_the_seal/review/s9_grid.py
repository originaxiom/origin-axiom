import sys, time; sys.path.insert(0,'.')
import numpy as np, math, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']; W=ns['W']; WP=ns['WP']
t0=time.time()
res=[]
xs = np.linspace(-0.5,0.5,41)+0.0123      # offset from the sealed grid
ys = np.arange(0.87,2.31,0.037)
for x in xs:
    if abs(x)>0.5: continue
    for y in ys:
        tau=complex(x,y)
        if abs(tau)<1-1e-9: continue
        R=R_A(tau); c={r: cA(r,tau,1e-5,nth=48,ns=32) for r in (2,3,4)}
        res.append((abs(D_of(c,R))/nR2(R), x, y, min(abs(tau-W),abs(tau-WP))))
res.sort()
print("points:",len(res),"time",time.time()-t0)
print("smallest 12:")
for r in res[:12]: print("   |D|/|R|^2=%.4f at tau=%.3f+%.3fi  dist to nearest corner=%.3f"%r)
far=[r for r in res if r[3]>0.1]
print("smallest far (>0.1 from both corners):", far[0])
# ratio |D|/(|tau-omega|) near corners
near=[r for r in res if r[3]<0.2 ]
print("near-corner slopes |D|/|R|^2/dist:", sorted(round(r[0]/r[3],3) for r in near)[:6], sorted(round(r[0]/r[3],3) for r in near)[-4:])
