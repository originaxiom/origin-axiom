import numpy as np, math
exec(open('ind3.py').read().split("# the instrument's statistic")[0])
rng=np.random.default_rng(7)
R=Rs["i"]
for ea,ev in ((1e-3,1e-3),(1e-3,1e-5),(1e-5,1e-3),(1e-4,1e-4)):
    al=rng.normal(size=3)+1j*rng.normal(size=3); al=al-(al@R.conj())/(R@R.conj())*R
    be=rng.normal(size=3)+1j*rng.normal(size=3)
    al/=np.linalg.norm(al); be/=np.linalg.norm(be)
    a=2*(R.conj()+ea*al); v=3*(R+ev*be)
    s=sv(Y(a,v)); got=s[1:]/s[0]
    da=abs(a@a)/np.linalg.norm(a)**2; dv=abs(v@v)/np.linalg.norm(v)**2
    print(ea,ev,"got",got,"def sorted",np.sort([da,dv])[::-1],"da,dv",da,dv, "ratios", got/np.sort([da,dv])[::-1])
    # exact det check
    print("   s1 s2 s3 / (|a.v||a.a||v.v|):", s[0]*s[1]*s[2]/(abs(a@v)*abs(a@a)*abs(v@v)), " s1/(|a||v|)", s[0]/(np.linalg.norm(a)*np.linalg.norm(v)))
