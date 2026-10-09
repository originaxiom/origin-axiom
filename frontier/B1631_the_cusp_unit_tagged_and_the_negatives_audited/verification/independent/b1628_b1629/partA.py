import numpy as np
from math import sqrt
# --- Task 1: derive relations from explicit TM1 / TM2 matrices
rng = np.random.default_rng(1)
s6,s3,s2 = np.sqrt(6),np.sqrt(3),np.sqrt(2)
TBM = np.array([[ 2/s6, 1/s3, 0],
                [-1/s6, 1/s3, 1/s2],
                [ 1/s6,-1/s3, 1/s2]])
assert np.allclose(TBM@TBM.T, np.eye(3))
def extract(U):
    ue1,ue2,ue3 = abs(U[0,0])**2,abs(U[0,1])**2,abs(U[0,2])**2
    s13 = ue3
    s12 = ue2/(1-ue3)         # from |Ue2|^2 = s12^2 c13^2, |Ue1|^2 = c12^2 c13^2
    return s12,s13
def rot_cols(U, i, j, th, ph):
    # mix columns i,j by a rotation and a phase, preserving the third column
    V = U.astype(complex).copy()
    c,s = np.cos(th),np.sin(th)
    ci,cj = V[:,i].copy(),V[:,j].copy()
    V[:,i] =  c*ci + s*np.exp(1j*ph)*cj
    V[:,j] = -s*np.exp(-1j*ph)*ci + c*cj
    return V
maxerr1=maxerr2=0
for _ in range(2000):
    th,ph = rng.uniform(0,2*np.pi,2)
    U1 = rot_cols(TBM,1,2,th,ph)   # TM1: column 1 (index 0) = (sqrt(2/3),..) kept
    U2 = rot_cols(TBM,0,2,th,ph)   # TM2: column 2 (index 1) kept
    assert np.allclose(U1.conj().T@U1,np.eye(3)) and np.allclose(U2.conj().T@U2,np.eye(3))
    assert np.isclose(abs(U1[0,0])**2,2/3) and np.isclose(abs(U2[0,1])**2,1/3)
    s12,s13 = extract(U1); maxerr1=max(maxerr1,abs(s12-(1-2/(3*(1-s13)))))
    s12,s13 = extract(U2); maxerr2=max(maxerr2,abs(s12-1/(3*(1-s13))))
print("TM1 formula max err over 2000 random TM1 matrices:",maxerr1)
print("TM2 formula max err over 2000 random TM2 matrices:",maxerr2)
# analytic: |Ue1|^2 = c12^2 c13^2 = 2/3 -> s12^2 = 1-2/(3c13^2); |Ue2|^2 = s12^2 c13^2 = 1/3 -> s12^2 = 1/(3 c13^2)

# --- Task 2: pulls
def pred1(x): return 1-2/(3*(1-x))
def pred2(x): return 1/(3*(1-x))
def d1(x): return -2/(3*(1-x)**2)
def d2(x): return 1/(3*(1-x)**2)
b12, up12, dn12 = 0.308, 0.012, 0.011
b13, up13, dn13 = 0.02215, 0.00056, 0.00058
for name,pf,df in (("TM1",pred1,d1),("TM2",pred2,d2)):
    p = pf(b13); d = df(b13)
    print(f"\n{name}: prediction at best-fit s13^2 = {p:.5f}  (dpred/ds13^2 = {d:.4f})")
    # NuFIT pulls
    for label,best,sup,sdn in (("NuFIT6.0",b12,up12,dn12),("JUNO",0.3092,0.0087,0.0087)):
        s_theta12 = sup if p>best else sdn      # side of the prediction
        # theta13 spread propagated; side options
        for tag,s13sig in (("s13 upper",up13),("s13 lower",dn13),("s13 mean",(up13+dn13)/2)):
            s_pred = abs(d)*s13sig
            if label=="JUNO":
                tot = np.hypot(sup, s_pred)   # JUNO symmetric, +theta13 spread
            else:
                tot = np.hypot(s_theta12, s_pred)
            print(f"   {label:9s} [{tag}] sigma_tot={tot:.5f}  pull={(p-best)/tot:+.3f}   (no-theta13 pull {(p-best)/(s_theta12 if label!='JUNO' else sup):+.3f})")
    # sensitivity: what if we use symmetric 0.0115 for NuFIT?
    print("   NuFIT with symmetric sigma 0.0115:", (p-b12)/np.hypot(0.0115, abs(d)*0.00057))
    # variation of prediction across theta13 3-sigma range
    print("   prediction over s13^2 3sigma range 0.02030-0.02388:", pf(0.02030), pf(0.02388))
print("\nTM2 inside NuFIT 3sigma [0.275,0.345]? ", 0.275<=pred2(b13)<=0.345, pred2(b13))
print("TM1 inside 3sigma? ", 0.275<=pred1(b13)<=0.345)
# TM2 at upper s13^2 (larger), would it exceed 0.345?
print("TM2 at s13^2 +3sigma=0.02388:",pred2(0.02388), " TM2 at -3sigma 0.02030:",pred2(0.02030))
