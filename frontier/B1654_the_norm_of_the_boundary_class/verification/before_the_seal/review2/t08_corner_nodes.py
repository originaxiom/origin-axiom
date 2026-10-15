# Item 4: which grid nodes qualify as "within 0.1 of a corner" (geometry only), then D at exactly those nodes.
import math, time
import numpy as np, pre2
ns = pre2.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']; W=ns['W']; WP=ns['WP']
nodes=[]
for x in np.round(np.linspace(-0.5,0.5,21),4):
    for y in np.round(np.arange(0.86,2.0001,0.06),4):
        tau=complex(x,y)
        if abs(tau)<1-1e-9: continue
        nodes.append((float(x),float(y),float(min(abs(tau-W),abs(tau-WP)))))
print("grid nodes:",len(nodes))
near=[n for n in nodes if 0<n[2]<=0.1]
print("nodes with 0<dist<=0.1:", near)
close=[n for n in nodes if 0.1<n[2]<=0.2]
print("nodes with 0.1<dist<=0.2 (the 'far' nodes nearest the corner):", close)
print("y values:", np.round(np.arange(0.86,2.0001,0.06),4))
# compute D at exactly the near-corner nodes (allowed sub-check)
for (x,y,dist) in near:
    tau=complex(x,y); R=R_A(tau)
    out=[]
    for (nth,nss) in ((64,48),(96,64),(192,128)):
        c={r:cA(r,tau,1e-5,nth=nth,ns=nss) for r in (2,3,4)}
        out.append(abs(D_of(c,R))/nR2(R))
    print(f"node ({x},{y}) dist={dist:.5f}: |D|/|R|^2 = {out[0]:.8f} (64,48) / {out[1]:.8f} (96,64) / {out[2]:.8f} (192,128);  ratio |D|/(|R|^2 dist) = {out[0]/dist:.5f}  / {out[2]/dist:.5f}   [range 1.8,3.4]")
