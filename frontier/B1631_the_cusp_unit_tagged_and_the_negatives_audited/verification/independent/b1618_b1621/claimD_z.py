import numpy as np
from setup import *
rng=np.random.default_rng(3)
def mean(D,g,kind):
    out=0
    for k in range(3):
        gk=np.linalg.matrix_power(g,k)
        out=out+(gk.conj().T if kind=='Dirac' else gk.T)@D@gk
    return out/3
for z in [1,-1,1j,-1j,np.exp(1j*np.pi/4)]:
    for kind in ['Dirac','TxT']:
        worst=0
        for S,sg,p,s in signed_perms_det1():
            if sg==1 and p!=(0,1,2):
                g=z*S.astype(complex)
                if abs(z**4-1)>1e-9: continue
                for _ in range(30):
                    D=np.diag(rng.normal(size=3)+1j*rng.normal(size=3))
                    sv=np.linalg.svd(mean(D,g,kind),compute_uv=False)
                    worst=max(worst,sv.max()-sv.min())
        print("tick = z*signed3cycle, z=%s, %s: max sv spread %.3g ; tick eigenvalues for z*P: %s"%(np.round(z,3),kind,worst,np.round(np.linalg.eigvals(z*P),3)))
