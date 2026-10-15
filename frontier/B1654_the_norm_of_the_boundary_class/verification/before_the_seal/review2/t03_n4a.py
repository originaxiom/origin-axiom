# Item 1: N4(a) after the fix. Shift = -2 pi ln2 R_k^2 (channel 3 <-> R_k). Non-zero at the six named points? (R_A only, no c's)
import math
import numpy as np, pre2
ns = pre2.load(); R_A=ns['R_A']; nR2=ns['nR2']; TAUS=ns['TAUS']
print("named points: |shift|/|R|^2 for lam=(1,2,1)  [needs > 1e-3] ; and signed check against -2 pi ln2 R_k^2")
for name,tau in TAUS.items():
    R=R_A(tau)
    lam={2:1.0,3:2.0,4:1.0}
    # code path: sum((2pi(L-ln lam)+c) R^2) - sum((2pi L + c)R^2) = -2pi sum ln lam R^2 + 2 pi L*0 ; test with arbitrary c
    c={2:-2.2,3:-2.3,4:-2.4}
    L=5.0
    uu_c=sum((2*np.pi*(L-math.log(lam[r]))+c[r])*R[r]**2 for r in (2,3,4))
    D=sum(c[r]*R[r]**2 for r in (2,3,4))
    uu=sum((2*np.pi*L+c[r])*R[r]**2 for r in (2,3,4))
    shift=uu_c-uu
    pred=-2*np.pi*math.log(2)*R[3]**2
    print(f"{name:6s}  |shift|/|R|^2 = {abs(uu_c-D)/nR2(R):.4f}   signed: shift/pred - 1 = {abs(shift/pred-1):.1e}   |R_k|^2/|R|^2 = {abs(R[3])**2/nR2(R):.4f}")
# Minimal |R_k|^2/|R|^2 over the whole fundamental domain
mn=1e9
for x in np.linspace(-.5,.5,41):
    for y in np.arange(0.87,6.0,0.1):
        t=complex(x,y)
        if abs(t)<1: continue
        R=R_A(t); mn=min(mn,abs(R[3])**2/nR2(R))
print("min over fundamental domain of |R_k|^2/|R|^2:", mn, "-> shift floor 2pi ln2 * that =", 2*np.pi*math.log(2)*mn)
# Old lam=(1,2,4)
for name,tau in TAUS.items():
    R=R_A(tau); lam={2:1.0,3:2.0,4:4.0}
    print(name, "old lam: |shift|/|R|^2 =", abs(-2*np.pi*sum(math.log(lam[r])*R[r]**2 for r in (2,3,4)))/nR2(R))
