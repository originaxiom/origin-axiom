import numpy as np, math
exec(open('ind3.py').read().split("# the instrument's statistic")[0])
rng=np.random.default_rng(3)
for k,R in Rs.items():
    out=[]
    for _ in range(300):
        ea,ev=10**rng.uniform(-5,-2),10**rng.uniform(-5,-2)
        al=rng.normal(size=3)+1j*rng.normal(size=3); be=rng.normal(size=3)+1j*rng.normal(size=3)
        a=2*(R+ea*al/np.linalg.norm(al)); v=3*(R+ev*be/np.linalg.norm(be))   # a near R, v near R
        s=sv(Y(a,v)); got=s[1:]/s[0]
        da=abs(a@a)/np.linalg.norm(a)**2; dv=abs(v@v)/np.linalg.norm(v)**2
        out.append(np.abs(got/np.sort([da,dv])[::-1]-1).max()/max(ea,ev))
    print(k,"a near R (not Rbar), v near R: worst |light/defect-1|/eps =",max(out), "median",np.median(out))
    out=[]
    for _ in range(300):
        ea,ev=10**rng.uniform(-5,-2),10**rng.uniform(-5,-2)
        al=rng.normal(size=3)+1j*rng.normal(size=3); be=rng.normal(size=3)+1j*rng.normal(size=3)
        a=2*(R.conj()+ea*al/np.linalg.norm(al)); v=3*(R.conj()+ev*be/np.linalg.norm(be))   # both near Rbar
        s=sv(Y(a,v)); got=s[1:]/s[0]
        da=abs(a@a)/np.linalg.norm(a)**2; dv=abs(v@v)/np.linalg.norm(v)**2
        out.append(np.abs(got/np.sort([da,dv])[::-1]-1).max()/max(ea,ev))
    print(k,"a near Rbar, v near Rbar: worst",max(out),"median",np.median(out))
