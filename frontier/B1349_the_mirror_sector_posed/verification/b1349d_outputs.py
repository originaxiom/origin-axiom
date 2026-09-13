"""B1349 addendum 2 -- HOW MANY INDEPENDENT OUTPUTS DOES THE theta-EVEN MIRROR SET CARRY?

R11 needs outputs > 3 bits. The decisive sub-question is EAR-DEPENDENCE. B641/B856 established that
the ODD sector's five tones are EAR-INDEPENDENT -- identical for every admissible u -- which is
exactly why the bench repair DEMOTED AC4 as non-discriminating: a readout that does not vary with u
carries no information about u, so it is not an output at all.

So: compute h_m(v) = v* M_even(R^m L^m) v / (v* v) and ask whether it VARIES with v.
  EAR-INDEPENDENT  -> outputs = 0, R11 can NEVER close, the row is dead definitively.
  EAR-DEPENDENT    -> count the independent values.
"""
import numpy as np, itertools
from fractions import Fraction
np.set_printoptions(precision=10, suppress=True)

def su3(k=2):
    kap=k+3; W=[(a,b) for a in range(k+1) for b in range(k+1-a)]
    Lv=lambda w: np.array([w[0]+w[1]+2.,w[1]+1.,0.])
    ip=lambda u,v: float(np.dot(u,v)-u.sum()*v.sum()/3)
    P=list(itertools.permutations(range(3)))
    sg=lambda p:(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    S=np.zeros((6,6),dtype=complex)
    for i,wl in enumerate(W):
        for j,wm in enumerate(W):
            S[i,j]=sum(sg(p)*np.exp(-2j*np.pi*ip(Lv(wl)[list(p)],Lv(wm))/kap) for p in P)
    S*=-1j/(kap*np.sqrt(3.))
    C2=lambda w:(2/3)*(w[0]**2+w[0]*w[1]+w[1]**2)+2*(w[0]+w[1])
    T=np.diag([np.exp(2j*np.pi*(C2(w)/(2*kap)-(8*k/(k+3))/24)) for w in W])
    return W,S,T
W,S,T=su3(); R=T; L=np.linalg.inv(S)@np.linalg.inv(T)@S
ix={w:i for i,w in enumerate(W)}
Bev=np.zeros((6,4),dtype=complex)
Bev[ix[(0,0)],0]=1; Bev[ix[(1,1)],1]=1
Bev[ix[(0,1)],2]=Bev[ix[(1,0)],2]=1
Bev[ix[(0,2)],3]=Bev[ix[(2,0)],3]=1
Bod=np.zeros((6,2),dtype=complex)
Bod[ix[(0,1)],0]=1; Bod[ix[(1,0)],0]=-1
Bod[ix[(0,2)],1]=1; Bod[ix[(2,0)],1]=-1
def rest(M,B): return np.linalg.lstsq(B,M@B,rcond=None)[0]
def word(m):
    A=np.eye(6,dtype=complex)
    for _ in range(m): A=A@R
    for _ in range(m): A=A@L
    return A
def h(v,m,B):
    M=rest(word(m),B); v=v/np.linalg.norm(v)
    return np.vdot(v, M@v)

# the 8 rational maximal-stabiliser directions of the even sector (from b1349c)
RAT=[np.array(c,dtype=complex) for c in
     [(0,0,0,1),(1,0,0,0),(0,1,0,0),(0,0,1,0),
      (1,0,0,-0.5),(1,0,0,1),(0,1,1,0),(0,1,-0.5,0)]]
rng=np.random.default_rng(5)
GEN=[rng.normal(size=4)+1j*rng.normal(size=4) for _ in range(4)]

print("=== CONTROL: the ODD sector's tones must be EAR-INDEPENDENT (B641/B856) ===")
od=[np.array([1,0],dtype=complex), np.array([0,1],dtype=complex),
    np.array([1,1],dtype=complex), rng.normal(size=2)+1j*rng.normal(size=2)]
for m in range(1,6):
    vals=[h(v,m,Bod) for v in od]
    spread=max(abs(a-b) for a in vals for b in vals)
    print(f"   m={m}: h_odd = {np.round(vals[0],8)}   spread over 4 ears = {spread:.2e}")

print("\n=== THE QUESTION: is the theta-EVEN readout EAR-DEPENDENT? ===")
for m in range(1,8):
    vr=[h(v,m,Bev) for v in RAT]; vg=[h(v,m,Bev) for v in GEN]
    allv=vr+vg
    spread=max(abs(a-b) for a in allv for b in allv)
    print(f"   m={m}: spread over 12 ears = {spread:.3e}   "
          f"h at the 4 basis vectors = {np.round(vr[:4],6)}")

print("\n=== how many DISTINCT values, and is there a period in m? ===")
v0=RAT[1]                       # e(0,0), a canonical rational vertex direction
seq=[h(v0,m,Bev) for m in range(1,21)]
uniq=[]
for x in seq:
    if not any(abs(x-y)<1e-9 for y in uniq): uniq.append(x)
print(f"   at v = e(0,0): {len(uniq)} distinct values over m = 1..20")
print(f"   sequence (rounded): {np.round(seq[:10],6)}")
per=None
for p in range(1,11):
    if all(abs(seq[i]-seq[i+p])<1e-9 for i in range(len(seq)-p)): per=p; break
print(f"   period in m: {per}")
