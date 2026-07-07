import numpy as np, math, sys
sys.path.insert(0,'.')
from harness import *

print("== FLAG TEST 1: D0(V=2) at N~2500 for all m (estimator convergence) ==")
vals15, vals25 = [], []
for m in MS:
    w15=metallic_word(m,1500); w25=metallic_word(m,2500)
    d15=dq_spectrum(spectrum(w15,2.0),qs=(0,))[0]
    d25=dq_spectrum(spectrum(w25,2.0),qs=(0,))[0]
    vals15.append(d15); vals25.append(d25)
    print(f"  m={m}: D0(1500)={d15:.4f}  D0(2500)={d25:.4f}  shift={d25-d15:+.4f}", flush=True)
c15=classify(vals15); c25=classify(vals25)
print(f"  flag at N=1500: {c15['flag']} (e1/med={c15['e1_over_med']})   at N=2500: {c25['flag']} (e1/med={c25['e1_over_med']})")

print("== FLAG TEST 2: C_peak_T fit-form dependence ==")
Tgrid=np.logspace(-2,1,240)
peaks=[]
for m in MS:
    E=spectrum(metallic_word(m,1500),1.0)
    C=specific_heat(E,Tgrid)
    peaks.append(float(Tgrid[int(np.argmax(C))]))
x_forms={'log lam':[math.log(lam(m)) for m in MS],
         'theta':[theta(m) for m in MS],
         '1/lam':[1/lam(m) for m in MS]}
y=np.array(peaks)
for name,xs in x_forms.items():
    x=np.array(xs); errs=[]
    for i in range(6):
        sel=np.arange(6)!=i
        errs.append(abs(y[i]-np.polyval(np.polyfit(x[sel],y[sel],2),x[i])))
    print(f"  fit vs {name:8s}: e1={errs[0]:.4f}  med(others)={np.median(errs[1:]):.4f}  ratio={errs[0]/max(np.median(errs[1:]),1e-9):.1f}")

print("== FLAG TEST 3: gamma_on finite-size scaling (noise floor?) ==")
for m in (1,6):
    E=spectrum(metallic_word(m,1500),1.0)
    Eon=E[np.linspace(10,len(E)-10,12).astype(int)]
    for tgt in (1000,2500,5000,10000):
        w=metallic_word(m,tgt)
        g=lyapunov(w,1.0,Eon)
        print(f"  m={m} N={tgt}: gamma_on={g.mean():.5f}  (1/N={1/tgt:.5f})", flush=True)
