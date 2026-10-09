import pickle, time
from mpmath import mp, mpf
from partB import *
mp.dps=40
data=[(w,mpf(h)) for w,h in pickle.load(open('heights_CF.pkl','rb'))]
t=time.time(); maxdiff=mpf(0); worst=None; bad=0
for w,h in data:
    hl,mn,D=height_lattice(w)
    diff=abs(hl-h)
    if diff>maxdiff: maxdiff=diff; worst=w
    if diff>mpf(10)**-20: bad+=1
print("words checked:",len(data)," lattice-vs-CF mismatches (>1e-20):",bad," max |diff|:",mp.nstr(maxdiff,5),"at",worst, f"({time.time()-t:.0f}s)")
# lattice lowest values independent of CF
lat=sorted(((height_lattice(w)[0],w) for w,_ in data),key=lambda t:t[0])
print("lowest 4 by lattice-minimum method:",[(mp.nstr(h,12),w) for h,w in lat[:4]])
