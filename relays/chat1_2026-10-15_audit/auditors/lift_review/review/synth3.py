import numpy as np, math
rng=np.random.default_rng(1)
for g in (0.5, 0.05, 5e-3, 5e-4, 8e-5):
  for cs in (2, 5, 10):
    worst=0; worst5=0
    for _ in range(200):
        Q1,_=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))); Q2,_=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
        M0=Q1@np.diag([0,g,1])@Q2.conj().T
        M1=cs*(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))/math.sqrt(2)
        U,s,Vh=np.linalg.svd(M0); o=np.argsort(s); u0,v0=U[:,o[0]],Vh[o[0],:].conj()
        k=abs(u0.conj()@M1@v0)/s[o[2]]
        for L,store in ((1000,0),(1e5,1)):
            e=1/(4*math.pi*L); sl=np.sort(np.linalg.svd(M0+e*M1,compute_uv=False))
            d=abs(sl[0]/sl[2]/e/k-1)
            if store==0: worst=max(worst,d)
            else: worst5=max(worst5,d)
    print(f'm2/m3={g:g} |M1|~{cs}: worst |4piL m1/m3/kappa - 1| over 200 draws: L=1000 {worst:.2e}; L=1e5 {worst5:.2e}')
