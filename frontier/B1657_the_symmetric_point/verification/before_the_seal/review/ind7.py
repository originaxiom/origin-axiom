import numpy as np, math
exec(open('ind3.py').read().split("# the instrument's statistic")[0])
rng=np.random.default_rng(3)
R=Rs["i"]
for eps in (1e-2,1e-3,1e-4):
    al=rng.normal(size=3)+1j*rng.normal(size=3); be=rng.normal(size=3)+1j*rng.normal(size=3)
    al/=np.linalg.norm(al); be/=np.linalg.norm(be)
    a=R+eps*al; v=R+eps*be
    s=sv(Y(a,v)); print(eps, s/s[0], " defects", abs(a@a)/np.linalg.norm(a)**2, abs(v@v)/np.linalg.norm(v)**2, " |a.v|",abs(a@v))
