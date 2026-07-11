import numpy as np, random
def fp(sub,seed,level):
    w=seed
    for _ in range(level): w=''.join(sub[c] for c in w)
    return w
def U(word,coins):
    N=len(word); D=2*N; C=np.zeros((D,D),complex); S=np.zeros((D,D),complex)
    for x,c in enumerate(word): C[2*x:2*x+2,2*x:2*x+2]=coins[c]
    for x in range(N): S[2*((x-1)%N)+0,2*x+0]=1; S[2*((x+1)%N)+1,2*x+1]=1
    return S@C
def ph(M): return np.sort(np.angle(np.linalg.eigvals(M)))
def cost(a,b):
    d=np.abs(a[:,None]-b[None,:]); d=np.minimum(d,2*np.pi-d); return float(np.mean(d.min(1)**2))
Id=np.eye(2,dtype=complex)
def R(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]],complex)
Cga={'a':R(np.pi/5),'A':R(2*np.pi/5),'b':Id,'B':Id}
GOLD={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}
def gc(sub,lv):
    wlo,whi=fp(sub,'a',lv[0]),fp(sub,'a',lv[1]); return cost(ph(U(wlo,Cga)),ph(U(whi,Cga))),len(whi)
gcost,_=gc(GOLD,(3,4))
print(f"golden-angle coin, GOLDEN: {gcost:.2e}")
print("random controls (length-4 images, comparable N):")
worse=0
for seed in range(5,15):
    random.seed(seed)
    RAND={c:''.join(random.choice('abAB') for _ in range(4)) for c in 'abAB'}
    c,n=gc(RAND,(3,4))
    print(f"  seed {seed}: cost={c:.2e} (N->{n})  {'GOLDEN better' if gcost<c else 'control better'}")
    worse += (gcost<c)
print(f"\ngolden beats {worse}/10 random controls => golden-angle coin is {'ROBUSTLY golden-specific' if worse>=9 else 'NOT robustly special'}")
