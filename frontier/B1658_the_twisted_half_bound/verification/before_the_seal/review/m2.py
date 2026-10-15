import numpy as np
from scipy.optimize import minimize
exec(open('mine.py').read().split('mx=')[0])
def r(z,sgn):
    S=(z[:4]+1j*z[4:8]).reshape(2,2);p=z[8:10]+1j*z[10:12];q=z[12:14]+1j*z[14:16]
    return sgn*np.linalg.norm(Y(S,np.outer(p,q)))**2/(np.linalg.norm(S)**2*np.linalg.norm(p)**2*np.linalg.norm(q)**2)
for sg in (1,-1):
    b=min((minimize(r,rng.normal(size=16),args=(sg,),method='BFGS').fun for _ in range(40)))
    print(sg,b)
