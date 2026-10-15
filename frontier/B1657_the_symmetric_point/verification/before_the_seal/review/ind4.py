import numpy as np, math
exec(open('ind3.py').read().split("# the instrument's statistic")[0])
rng=np.random.default_rng(7)
# alpha with alpha.Rbar = 0 exactly (bilinear), beta random
for k,R in list(Rs.items())[:4]:
    out=[]
    for _ in range(2000):
        ea=10**rng.uniform(-6,-2); ev=10**rng.uniform(-6,-2)
        al=rng.normal(size=3)+1j*rng.normal(size=3)
        al=al-(al@R.conj())/(R@R.conj())*R   # remove component: al.Rbar -> al.Rbar - (al.Rbar)(R.Rbar)/(R.Rbar)=0
        be=rng.normal(size=3)+1j*rng.normal(size=3)
        al/=np.linalg.norm(al); be/=np.linalg.norm(be)
        a=2*(R.conj()+ea*al); v=3*(R+ev*be)
        s=sv(Y(a,v)); got=s[1:]/s[0]
        da=abs(a@a)/np.linalg.norm(a)**2; dv=abs(v@v)/np.linalg.norm(v)**2
        pred=np.sort([da,dv])[::-1]
        out.append(np.abs(got/pred-1).max()/max(ea,ev))
    print(k,"alpha.Rbar=0:",max(out), "  check", abs(al@R.conj()))
