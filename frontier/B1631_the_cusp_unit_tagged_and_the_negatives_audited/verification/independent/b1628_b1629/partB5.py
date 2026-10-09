import numpy as np
from fractions import Fraction

def stats(n, kmax=8):
    N=1<<n
    words=np.arange(N,dtype=np.int64)
    mask=N-1
    def rot(x,s): return ((x<<s)|(x>>(n-s)))&mask
    # primitive: not fixed by any rotation by proper divisor of n
    prim=np.ones(N,bool)
    for d in range(1,n):
        if n%d==0:
            prim &= (rot(words,d)!=words)
    both=(words!=0)&(words!=mask)
    ok=prim&both
    # bit matrix
    bits=((words[:,None]>>np.arange(n)[None,:])&1).astype(np.int8)    # N x n
    # cyclic run length containing each position: compute via boundaries
    # lengths: for each position, length of maximal cyclic run it belongs to
    runlen=np.zeros((N,n),dtype=np.int16)
    # for each word with both letters, find a start s where bits[s]!=bits[s-1]
    diff=(bits!=np.roll(bits,1,axis=1))        # True at run starts
    # forward run length from each position until next boundary (cyclic): compute using doubled array
    dd=np.concatenate([diff,diff,diff],axis=1)
    # distance to next start strictly after position i: scan from the right
    nxt=np.full((N,3*n),3*n,dtype=np.int16)
    cur=np.full(N,3*n,dtype=np.int16)
    for i in range(3*n-1,-1,-1):
        nxt[:,i]=cur            # next start index > i
        cur=np.where(dd[:,i],i,cur)
    # run containing position i: last start <= i, next start > i
    last=np.full((N,n),-1,dtype=np.int16)
    # last start <= i in cyclic sense: scan left to right on doubled array
    lastd=np.full((N,3*n),-1,dtype=np.int16); cl=np.full(N,-1,dtype=np.int16)
    for i in range(3*n):
        cl=np.where(dd[:,i],i,cl); lastd[:,i]=cl
    i0=np.arange(n,2*n)            # use second copy so that "last start" exists
    rl=nxt[:,i0]-lastd[:,i0]       # run length of run containing position i (for words with both letters)
    res={}
    for k in range(2,kmax+1):
        frac=(rl>=k).mean(axis=1)           # fraction of letters in runs >= k, per word
        res[k]=frac
    return ok, res, words, rot

def canonical_necklace_mask(ok, words, rot, n):
    # pick the minimal rotation representative: word equals min over rotations
    mn=words.copy()
    for s in range(1,n):
        mn=np.minimum(mn,rot(words,s))
    return ok&(mn==words)

for n in (16,18):
    ok,res,words,rot=stats(n)
    neck=canonical_necklace_mask(ok,words,rot,n)
    print(f"n={n}: primitive words with both letters = {ok.sum()}, necklaces = {neck.sum()} (ratio {ok.sum()/neck.sum():.4f})")
    print(" k  (k+1)/2^k   mean over necklaces   mean over primitive words   diff")
    for k in range(2,9):
        pred=(k+1)/2**k
        mn=res[k][neck].mean(); mw=res[k][ok].mean()
        print(f"{k:2d}  {pred:.6f}   {mn:.6f}             {mw:.6f}                {mn-pred:+.2e}")
# larger n via Monte Carlo on random primitive words
rng=np.random.default_rng(3)
def mc(n,samples,kmax=8):
    out={k:[] for k in range(2,kmax+1)}
    tot={k:0.0 for k in range(2,kmax+1)}; cnt=0
    for _ in range(samples):
        b=rng.integers(0,2,n)
        if b.min()==b.max(): continue
        # primitivity
        s=''.join(map(str,b)); 
        if any(n%d==0 and s==s[d:]+s[:d] for d in range(1,n)): continue
        diff=(b!=np.roll(b,1)); starts=np.flatnonzero(diff)
        lens=np.diff(np.concatenate([starts,[starts[0]+n]]))
        for k in tot: tot[k]+=lens[lens>=k].sum()/n
        cnt+=1
    return {k:tot[k]/cnt for k in tot}
r=mc(60,200000)
print("\nMonte Carlo n=60, 2e5 random words:")
for k,v in r.items(): print(f"  k={k}: {v:.5f} vs {(k+1)/2**k:.5f}")
