import numpy as np
rng=np.random.default_rng(2)
def stats(gen,n=100000):
    ws=0;fl=1;viol=0
    for _ in range(n):
        M=gen(); s=np.linalg.svd(M,compute_uv=False); d=abs(s[0]-s[1]-s[2])/s[0]; ws=max(ws,d); fl=min(fl,s[1]/s[0]); viol+= d>1e-9
    return ws,fl,viol
z=lambda: rng.normal(size=3)+1j*rng.normal(size=3)
def sym():
    a,b,c=z(); return np.array([[0,c,b],[c,0,a],[b,a,0]])
def asym():
    a,b,c=z(); return np.array([[0,c,b],[-c,0,a],[-b,-a,0]])
def gen_off():
    M=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); np.fill_diagonal(M,0); return M
def sym_plus_r_asym():
    S=sym(); A=asym(); r=rng.normal()+1j*rng.normal(); return S+r*A
def sym_plus_diag():
    S=sym(); S=S+np.diag(rng.normal(size=3)*0.3); return S
for nm,g in (("symmetric zero-diag (O+)",sym),("antisymmetric (O-)",asym),("general zero-diag (O+ + r O-)",sym_plus_r_asym),("general zero-diag random",gen_off),("symmetric with small diagonal",sym_plus_diag)):
    ws,fl,v=stats(g,50000); print(f"{nm:35s}: max|s1-s2-s3|/s1={ws:.2e}  min s2/s1={fl:.4f}  violations(>1e-9)={v}/50000")
