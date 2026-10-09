import numpy as np, random, pickle
from mpmath import mp, mpf
from partB import matrix, height_CF, runs_cyclic
mp.dps=40

def reduce_F(z, iters=200):
    z=z.copy()
    for _ in range(iters):
        z = z - np.round(z.real)
        m = np.abs(z)<1-1e-15
        if not m.any(): break
        z[m] = -1/z[m]
    return z

def height_trace(w, dt=2e-5):
    M=[int(x) for x in matrix(w).flatten()]; a,b,c,d=M
    tr=a+d; D=tr*tr-4; sq=np.sqrt(D)
    # fixed points: c z^2 + (d-a) z - b = 0
    al=((a-d)+sq)/(2*c); be=((a-d)-sq)/(2*c)
    mid=(al+be)/2; r=abs(al-be)/2
    lam=(tr+sq)/2
    T=2*np.log(lam)               # translation length of M along its axis
    t=np.arange(0,T,dt)
    # arclength-parametrised axis: z = mid + r(tanh t + i sech t) (orientation irrelevant)
    z = mid + r*(np.tanh(t) + 1j/np.cosh(t))
    # one period of the axis, centred around the apex, so shift t window to include apex of this lift too
    t2=np.arange(-T/2,T/2,dt)
    z2 = mid + r*(np.tanh(t2) + 1j/np.cosh(t2))
    zr=reduce_F(z2)
    return zr.imag.max(), np.abs(zr.real).max(), (zr.imag.min())

if __name__=="__main__":
    for w in ["LR","LLRR","LLRLRR","LLLR","LLLLLLLLLLLLR"]:
        ht,_,_=height_trace(w)
        print(f"{w:16s} trace-max-Im = {ht:.6f}   CF = {mp.nstr(height_CF(w),10)}")
    data=[(w,mpf(h)) for w,h in pickle.load(open('heights_CF.pkl','rb'))]
    random.seed(7)
    samp=random.sample(data,60)
    worst=0
    for w,h in samp:
        ht,_,_=height_trace(w)
        worst=max(worst,abs(ht-float(h)))
    print("random 60 words (n<=14): max |trace - CF| =",worst)
