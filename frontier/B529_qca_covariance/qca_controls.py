import numpy as np, random
def fp(sub,seed,level):
    w=seed
    for _ in range(level): w=''.join(sub[c] for c in w)
    return w
def U(word,coins):
    N=len(word); D=2*N; C=np.zeros((D,D),complex); S=np.zeros((D,D),complex)
    for x,c in enumerate(word): C[2*x:2*x+2,2*x:2*x+2]=coins[c]
    for x in range(N):                       # proper MOVING shift (non-degenerate)
        S[2*((x-1)%N)+0,2*x+0]=1; S[2*((x+1)%N)+1,2*x+1]=1
    return S@C
def ph(M): return np.sort(np.angle(np.linalg.eigvals(M)))
def cost(a,b):
    d=np.abs(a[:,None]-b[None,:]); d=np.minimum(d,2*np.pi-d); return float(np.mean(d.min(1)**2))
Id=np.eye(2,dtype=complex); isy=np.array([[0,-1],[1,0]],complex); H=np.array([[1,1],[1,-1]],complex)/2**.5
Cisy={'a':isy,'A':isy,'b':Id,'B':Id}; Cid={c:Id for c in 'abAB'}; CH={c:H for c in 'abAB'}
GOLD ={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}
TETRA={'a':'ab','b':'aA','A':'aB','B':'a'}          # tetranacci on {a,b,A,B}
random.seed(3)
RAND ={c:''.join(random.choice('abAB') for _ in range(4)) for c in 'abAB'}  # each image length 4

def show(sub,name,lv):
    wlo,whi=fp(sub,'a',lv[0]),fp(sub,'a',lv[1])
    row={n:cost(ph(U(wlo,cf)),ph(U(whi,cf))) for n,cf in [('id',Cid),('Had',CH),('isy',Cisy)]}
    print(f"  {name:11s} N {len(wlo):>4}->{len(whi):>4}:  id={row['id']:.2e}  Had={row['Had']:.2e}  isy={row['isy']:.2e}")
    return row,len(whi)

print("=== comparable sizes, proper moving shift ===")
g,_=show(GOLD,'GOLDEN',(3,4))
t,_=show(TETRA,'tetranacci',(4,5))     # tetranacci grows slower; use higher level for comparable N
r,_=show(RAND,'random',(3,4))
print()
print(f"isy nesting cost:  golden={g['isy']:.2e}   tetranacci={t['isy']:.2e}   random={r['isy']:.2e}")
print("DECISIVE: golden much smaller than controls => selection.  comparable => GENERIC (kill-rule fires).")
# is identity actually the WORST (handoff claim) or not?
print(f"\nhandoff claim 'identity WORST, isy best'. golden row: id={g['id']:.2e}  Had={g['Had']:.2e}  isy={g['isy']:.2e}")
print("worst coin (highest cost) for golden:", max(g,key=g.get), " | best:", min(g,key=g.get))
# degeneracy of isy spectrum on golden
w=fp(GOLD,'a',4); s=ph(U(w,Cisy))
print(f"\nisy golden spectrum: {len(np.unique(np.round(s,7)))} distinct of {len(s)} (high degeneracy => trivial nesting)")

print("\n=== the GOLDEN-ANGLE coin (embeds phi): is IT golden-specific or generic? ===")
def R(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]],complex)
Cga={'a':R(np.pi/5),'A':R(2*np.pi/5),'b':Id,'B':Id}
def ga_cost(sub,lv):
    wlo,whi=fp(sub,'a',lv[0]),fp(sub,'a',lv[1]); return cost(ph(U(wlo,Cga)),ph(U(whi,Cga)))
gg=ga_cost(GOLD,(3,4)); gt=ga_cost(TETRA,(4,5)); gr=ga_cost(RAND,(3,4))
print(f"  golden-angle coin: golden={gg:.2e}  tetranacci={gt:.2e}  random={gr:.2e}")
print("  golden much smaller => genuine golden selection; comparable => generic too")
