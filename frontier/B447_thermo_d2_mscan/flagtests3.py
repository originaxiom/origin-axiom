import numpy as np, math, sys
sys.path.insert(0,'.')
from harness import *
Tg=np.logspace(-2,1,2400)
def high_peak(E):
    C=specific_heat(E,Tg)
    best=None
    for i in range(1,len(Tg)-1):
        if C[i]>C[i-1] and C[i]>C[i+1]:
            lt=np.log(Tg[i-1:i+2]); a=np.polyfit(lt,C[i-1:i+2],2)
            t=float(np.exp(-a[1]/(2*a[0])))
            if best is None or t>best: best=t
    return best

print("== C_peak_T flag: N-stability (N~1500 vs N~3000) and V-scan ==")
for V in (0.5,1.0,2.0):
    for tgt in (1500,3000):
        vals=[high_peak(spectrum(metallic_word(m,tgt),V)) for m in MS]
        c=classify(vals)
        print(f"  V={V} N~{tgt}: peaks={[round(v,4) for v in vals]}  e1/med={c['e1_over_med']}  flag={c['flag']}", flush=True)
