import numpy as np, math
def dot(X,Y): return np.sum(X*Y,axis=1)
def Gp(X,Y,v): return dot(v,Y)[:,None]*X + dot(v,X)[:,None]*Y - dot(X,Y)[:,None]*v
def inv_sqrt(K):
    e,U=np.linalg.eigh(K); return U@np.diag(e**-0.5)@U.conj().T
def crand(rng,*s): return rng.normal(size=s)+1j*rng.normal(size=s)
def run(seed, gap, cscale, zero='row', N=200):
    rng=np.random.default_rng(seed)
    a=crand(rng,N); th=rng.normal(size=N)+0.3j*rng.normal(size=N)
    R=a[:,None]*np.stack([np.ones(N),1j*np.cos(th),1j*np.sin(th)],1)
    h=crand(rng,N,3); c=rng.normal(size=(N,3))*cscale
    X=[crand(rng,N,3) for _ in range(3)]; Y=[crand(rng,N,3) for _ in range(3)]
    if zero=='row': X[0]=R
    else: Y[0]=R*(1+0.1*rng.normal(size=N))[:,None]   # E4*R analogue: scalar times R
    # make the light pair small: Y[2] ~ Y[1] + gap*noise
    X[2]=X[1]+gap*crand(rng,N,3)
    KL=np.array([[np.sum(dot(X[i],np.conj(X[j]))) for j in range(3)] for i in range(3)])
    KR=np.array([[np.sum(dot(Y[i],np.conj(Y[j]))) for j in range(3)] for i in range(3)])
    A,B=inv_sqrt(KL),inv_sqrt(KR)
    Ym=lambda v: np.array([[np.sum(dot(Gp(X[p],Y[q],v),np.conj(h))) for q in range(3)] for p in range(3)])
    MR=A@Ym(R)@B.T; U,s,Vh=np.linalg.svd(MR); o=np.argsort(s); s3=s[o[2]]
    u0,v0=U[:,o[0]],Vh[o[0],:].conj()
    k=abs(u0.conj()@(A@Ym(c*R)@B.T)@v0)/s3
    out=[]
    for Lv in (1000,1e5):
        sl=np.sort(np.linalg.svd(A@Ym(np.sqrt(1+c/(2*math.pi*Lv))*R)@B.T,compute_uv=False))
        out.append(4*math.pi*Lv*sl[0]/sl[2]/k-1)
    return s[o[1]]/s3, s[o[0]]/s3, k, out
for zero in ('row','col'):
  for gap in (1, 1e-1, 1e-2, 3e-3):
    for cs in (3, 10):
        r=[run(sd,gap,cs,zero) for sd in range(6)]
        print(zero, f'gap {gap:g} c~scale {cs}: m2/m3 {min(x[0] for x in r):.1e}..{max(x[0] for x in r):.1e}  kappa {min(x[2] for x in r):.2g}..{max(x[2] for x in r):.2g}  worst L3 dev @1000 {max(abs(x[3][0]) for x in r):.2e}  @1e5 {max(abs(x[3][1]) for x in r):.2e}')
