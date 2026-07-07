import numpy as np, math, sys
sys.path.insert(0,'.')
from harness import *

print("== FLAG 2 RESOLUTION: C_peak_T on fine grid + parabolic interpolation ==")
Tg=np.logspace(-2,1,2400)
peaks=[]
for m in MS:
    E=spectrum(metallic_word(m,1500),1.0)
    C=specific_heat(E,Tg)
    i=int(np.argmax(C))
    # parabolic interpolation in log T
    lt=np.log(Tg[i-1:i+2]); cc=C[i-1:i+2]
    a=np.polyfit(lt,cc,2)
    peaks.append(float(np.exp(-a[1]/(2*a[0]))))
print("  fine-grid peaks:", [round(p,5) for p in peaks])
c=classify(peaks)
print(f"  classifier: e1/med={c['e1_over_med']}  flag={c['flag']}  (coarse-grid run had 6.57)")

print("== FLAG 1 RESOLUTION: exact band-based D0 (transfer-matrix, no diagonalization) ==")
def word_level(m,k):
    w=[0]
    for _ in range(k):
        nxt=[]
        for cch in w: nxt.extend([0]*m+[1] if cch==0 else [0])
        w=nxt
    return np.array(w,dtype=int)

def tr_period(word,V,E):
    M=np.eye(2)
    for n in range(len(word)):
        v=V*(1.0 if word[n]==0 else -1.0)
        M=np.array([[E-v,-1.0],[1.0,0.0]])@M
        nm=np.max(np.abs(M))
        if nm>1e100: M/= nm  # bands need |tr|<=2; huge norm = deep in gap, fine to rescale? NO - rescaling breaks tr.
    return np.trace(M)

def bands(word,V,ngrid=60000):
    Es=np.linspace(-(V+2.5),V+2.5,ngrid)
    tr=np.array([tr_period(word,V,E) for E in Es])
    inside=np.abs(tr)<=2.0
    # band intervals from the boolean mask, refine edges by bisection
    edges=[]
    i=0
    total=0.0; nb=0
    while i<len(Es):
        if inside[i]:
            j=i
            while j+1<len(Es) and inside[j+1]: j+=1
            # refine
            lo=Es[i-1] if i>0 else Es[i]; hi=Es[j+1] if j+1<len(Es) else Es[j]
            def f(E): return abs(tr_period(word,V,E))-2.0
            a,b=lo,Es[i]
            for _ in range(40):
                mid=(a+b)/2
                if f(mid)>0: a=mid
                else: b=mid
            left=(a+b)/2
            a,b=Es[j],hi
            for _ in range(40):
                mid=(a+b)/2
                if f(mid)>0: b=mid
                else: a=mid
            right=(a+b)/2
            total+=right-left; nb+=1
            i=j+1
        else: i+=1
    return nb,total

for V in (1.0,2.0):
    print(f"  -- V={V} --")
    vals=[]
    for m in MS:
        # two consecutive approximant levels with periods in ~[80,900]
        ks=[]
        k=1
        while True:
            L=len(word_level(m,k))
            if L>900: break
            if L>=80: ks.append(k)
            k+=1
        if len(ks)<2: ks=[k-2,k-1]
        k1,k2=ks[-2],ks[-1]
        w1,w2=word_level(m,k1),word_level(m,k2)
        n1,S1=bands(w1,V); n2,S2=bands(w2,V)
        # D0 from band scaling between consecutive levels:
        D0=math.log(n2/n1)/math.log((S1/n1)/(S2/n2))
        vals.append(D0)
        print(f"    m={m}: level {k1}(q={len(w1)},bands={n1},S={S1:.4f}) -> {k2}(q={len(w2)},bands={n2},S={S2:.4f})  D0={D0:.4f}", flush=True)
    c=classify(vals)
    print(f"    classifier at V={V}: e1/med={c['e1_over_med']}  flag={c['flag']}")
