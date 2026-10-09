import itertools, math, sys
import numpy as np
from mpmath import mp, mpf, sqrt as msqrt
mp.dps = 40

# ---------- word utilities
def runs_cyclic(w):
    """cyclic run lengths of a cyclic binary word (string over L,R) with both letters;
    returned starting from the start of an R-run (so alternating R,L,R,L...)"""
    n=len(w)
    # rotate so that w[0] != w[-1]  (start of a run)
    for s in range(n):
        if w[s] != w[s-1]:
            break
    w2 = w[s:]+w[:s]
    out=[]; cur=1
    for i in range(1,n):
        if w2[i]==w2[i-1]: cur+=1
        else: out.append(cur); cur=1
    out.append(cur)
    return out

def cf_periodic(seq, start, depth=60):
    """value of the infinite periodic CF [a_start; a_{start+1}, ...] (cyclic seq), mp precision"""
    m=len(seq)
    # evaluate truncated at large depth (error ~ phi^-2*depth) -- ample at mp.dps=40 w/ depth 200
    D=max(depth,400)
    x=mpf(0)
    for t in range(D-1,0,-1):
        a=seq[(start+t)%m]
        x=1/(a+x)
    return seq[start%m]+x

def height_CF(w):
    """Method (a): half of max_i ([a_i;a_{i+1},...] + [0;a_{i-1},a_{i-2},...]) over a period of the run sequence."""
    a = runs_cyclic(w)
    m=len(a)
    best=mpf(0)
    for i in range(m):
        fwd = cf_periodic(a,i)
        # backward tail [0; a_{i-1}, a_{i-2}, ...]
        rev = a[::-1]           # rev[j] = a[m-1-j]
        j = (m-1-(i-1))%m       # index in rev of a_{i-1}
        # [0; rev[j], rev[j+1], ...] = 1/[rev[j]; rev[j+1],...]
        back = 1/cf_periodic(rev,j)
        v=(fwd+back)/2
        if v>best: best=v
    return best

# ---------- method (b): lattice minimum of the quadratic form (no rotation, no CF)
L = np.array([[1,0],[1,1]],dtype=object); R = np.array([[1,1],[0,1]],dtype=object)
def matrix(w):
    M=np.array([[1,0],[0,1]],dtype=object)
    for ch in w:
        M = M.dot(L if ch=='L' else R)
    return M
def height_lattice(w, Nmult=1.5):
    M=matrix(w); a,b,c,d=[int(x) for x in M.flatten()]
    assert a*d-b*c==1
    tr=a+d; D=tr*tr-4; assert D>0
    # form f(x,y)=det(v,Mv)= c x^2 + (d-a) x y - b y^2 ; M-invariant; disc = (d-a)^2+4bc = tr^2-4
    N=int(Nmult*max(abs(a),abs(b),abs(c),abs(d)))+5
    xs=np.arange(0,N+1,dtype=np.int64)[:,None]; ys=np.arange(-N,N+1,dtype=np.int64)[None,:]
    f=c*xs*xs+(d-a)*xs*ys-b*ys*ys
    f=np.abs(f); f[0,N]=10**18   # exclude zero vector
    f=np.where(f==0,10**18,f)    # irrational roots -> f never 0 for nonzero v; guard anyway
    mn=int(f.min())
    return mp.sqrt(D)/(2*mn), mn, D

# ---------- enumerate primitive necklaces
def necklaces(n):
    seen=set(); out=[]
    for bits in range(1,2**n-1):
        w=''.join('L' if (bits>>i)&1 else 'R' for i in range(n))
        if w in seen: continue
        rots={w[i:]+w[:i] for i in range(n)}
        seen|=rots
        if len(rots)==n:           # primitive
            out.append(min(rots))
    return out

if __name__=="__main__":
    print("LR :",height_CF("LR"), " sqrt5/2=",msqrt(5)/2)
    print("LLRR:",height_CF("LLRR"), " sqrt2=",msqrt(2))
    print("lattice LR:",height_lattice("LR")[0], "lattice LLRR:",height_lattice("LLRR")[0])
    allw=[]
    for n in range(2,15):
        ws=necklaces(n); allw+=ws
        print("n=",n,"primitive necklaces with both letters:",len(ws)); sys.stdout.flush()
    import pickle
    res=[(w,height_CF(w)) for w in allw]
    pickle.dump([(w,str(h)) for w,h in res],open('heights_CF.pkl','wb'))
    res.sort(key=lambda t:t[1])
    print("\nlowest 12 by CF method:")
    for w,h in res[:12]:
        print(f"  {w:16s} n={len(w):2d} runs={runs_cyclic(w)}  h={mp.nstr(h,15)}")
    # distinct values
    vals=[]
    for w,h in res:
        if not vals or abs(h-vals[-1][0])>mpf(10)**-25: vals.append((h,[w]))
        else: vals[-1][1].append(w)
    print("\ndistinct lowest values and the words attaining them:")
    for h,ws in vals[:6]:
        print("  ",mp.nstr(h,18), len(ws),"words (cyclic classes);", ws[:6])
    print("sqrt5/2=",mp.nstr(msqrt(5)/2,18)," sqrt2=",mp.nstr(msqrt(2),18))
