import numpy as np
np.random.seed(1)

F  = np.array([[1,1],[1,0]], float)     # evolution (det -1)
D  = np.array([[2,0],[0,2]], float)     # decimation (det 4)
D2 = np.array([[1,2],[1,0]], float)     # decimation pd (det -2)
T  = np.array([[1,1],[1,1]], float)     # TM/erasure (det 0)

def boot(v):
    return np.block([[v, v],[v@v, v]])

def lyap(M):
    """timelike = EXPANDING (Perron) direction: sign -1 if |eig|>1, +1 if <1."""
    w, V = np.linalg.eig(M)
    P = np.zeros((4,4)); s=[]; used=np.zeros(4,bool); col=0
    sgn = lambda wi: -1.0 if abs(wi) > 1+1e-9 else (1.0 if abs(wi) < 1-1e-9 else 0.0)
    for i in range(4):
        if used[i]: continue
        if abs(w[i].imag) < 1e-9:
            P[:,col]=V[:,i].real; s.append(sgn(w[i])); used[i]=True; col+=1
        else:
            for j in range(i+1,4):
                if not used[j] and abs(w[j]-np.conj(w[i]))<1e-7:
                    P[:,col]=V[:,i].real; P[:,col+1]=V[:,i].imag
                    s += [sgn(w[i])]*2; used[i]=used[j]=True; col+=2; break
    Pi=np.linalg.inv(P); G=Pi.T@np.diag(s)@Pi
    n_time=sum(1 for x in s if x<0); n_space=sum(1 for x in s if x>0); n_null=sum(1 for x in s if x==0)
    return G, (n_time,n_space,n_null), np.abs(w)

def preserves(Mmap, G, n=6000):
    X=np.random.randn(n,4)
    q=np.einsum('ni,ij,nj->n',X,G,X)
    tl=X[q<0]
    if len(tl)==0: return None
    Y=tl@Mmap.T; qY=np.einsum('ni,ij,nj->n',Y,G,Y)
    return float(np.mean(qY<0))

Mstar=boot(F); G,sig,aw=lyap(Mstar)
print(f"M* cone: (timelike,spacelike,null)={sig}  |eig|={np.round(aw,3)}")
print(f"self-preservation of M* on its OWN timelike (expanding) cone: {preserves(Mstar,G):.3f}  (expect ~1.0)\n")

print("=== C3: does each verb's bootstrap preserve M*'s single timelike cone? ===")
for name,v in [("evolution",F),("decimation-2I",D),("decimation-pd",D2),("TM/erasure",T)]:
    Mv=boot(v); _,sv,awv=lyap(Mv); fr=preserves(Mv,G)
    proper = "(3,1) proper" if sv==(1,3,0) else ("DEGENERATE(null)" if sv[2]>0 else f"NON-(3,1) {sv[:2]}")
    print(f"  {name:15s} det={np.linalg.det(Mv):+6.2f}  own causal type={proper:20s}  preserves M* cone: {fr:.3f}")

print("\n=== foreign controls (evolution-type bootstraps of non-golden quartic Pisot) ===")
# tetranacci companion (det can be +-1); child x^4-x-1
tetr=np.array([[1,1,1,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]],float)
_,st,at=lyap(tetr); print(f"  tetranacci companion: causal type {st}, |eig|={np.round(at,3)} -> (3,1) generic to evolution-type")
