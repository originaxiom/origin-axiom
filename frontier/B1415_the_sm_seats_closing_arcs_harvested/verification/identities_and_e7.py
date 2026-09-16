#!/usr/bin/env python3
"""Own checks for sm:B1361 (the only U(1)^2-neutral E6 cubic; sigma_1 = sigma_2 + sigma_3 on hollow complex symmetric 3x3),
sm:B1362 (the deck-symmetric circulant has a degenerate pair) and sm:B1360 (E7's roots orthogonal to a minuscule coweight are E6's 72)."""
import numpy as np, itertools, sympy as sp
rng=np.random.default_rng(1); worst=0
for _ in range(2000):
    a,b,c=rng.normal(size=3)+1j*rng.normal(size=3)
    s=np.linalg.svd(np.array([[0,a,b],[a,0,c],[b,c,0]]),compute_uv=False); worst=max(worst,abs(s[0]-s[1]-s[2]))
print('hollow complex symmetric 3x3: max |s1-s2-s3| over 2000 random =', worst); assert worst<1e-12
x,y=sp.symbols('x y'); print('circulant circ(x,y,y) eigenvalues:', sp.Matrix([[x,y,y],[y,x,y],[y,y,x]]).eigenvals())
ch={1:(1,-2),2:(1,1),3:(-2,1)}
inv=[m for m in itertools.combinations_with_replacement((1,2,3),3) if sum(ch[i][0] for i in m)==0 and sum(ch[i][1] for i in m)==0]
print('U(1)^2-neutral cubic monomials in 27_1,27_2,27_3:', inv); assert inv==[(1,2,3)]
R=[]
for i,j in itertools.combinations(range(8),2):
    for a in (1,-1):
        for b in (1,-1):
            v=np.zeros(8); v[i]=a; v[j]=b; R.append(v)
for s in itertools.product((1,-1),repeat=8):
    if sum(1 for t in s if t<0)%2==0: R.append(np.array(s)/2)
R=np.array(R); r0=R[0]; E7=np.array([r for r in R if abs(r@r0)<1e-9]); print('E7 roots', len(E7))
w=[r-(r@r0)/2*r0 for r in R if abs(r@r0-1)<1e-9][0]   # a weight of the 56
zeros=sum(1 for r in E7 if abs(r@w)<1e-9); vals=sorted({round(float(r@w),6) for r in E7})
print('E7 roots orthogonal to a 56 weight:', zeros, 'inner products', vals, '|w|^2 =', round(float(w@w),4)); assert zeros==72 and vals==[-1.0,0.0,1.0]
print('ALL PASS')
