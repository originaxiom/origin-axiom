import json, math, sys
import numpy as np
from scipy.stats import spearmanr, pearsonr
d=json.load(open('<repo>/relays/chat1_2026-10-14_step3/lift_cells.json'))
P=d['per thread']
cells=["C2/E4","C3/E4","C3/THETA2","C3/ORTH"]
words=list(P)
print("n words",len(words))
for n in cells:
    adm=[w for w in words if P[w][n].get('admitted')]
    na=[w for w in words if not P[w][n].get('admitted')]
    print("==",n,"admitted",len(adm))
    print(" non-admitted:",[(w,round(P[w]['y_max'],3),P[w][n].get('pd'),P[w][n].get('N256 vs N384')) for w in na])
    k=np.array([P[w][n]['kappa'] for w in adm]); f=np.array([P[w][n]['m1/m3'] for w in adm]); y=np.array([P[w]['y_max'] for w in adm])
    r=f/k
    print(" floor/kappa: min %.3g median %.3g max %.3g"%(r.min(),np.median(r),r.max()))
    print(" Spearman(kappa,floor) %.4f  Spearman(y,floor) %.4f Spearman(y,ln k) %.4f"%(spearmanr(k,f).correlation, spearmanr(y,f).correlation, spearmanr(y,np.log(k)).correlation))
    sl=np.polyfit(np.log(k),np.log(f),1); print(" loglog slope floor vs kappa %.3f"%sl[0])
    # partial: residual of log f after log k
    print(" kappa>1e3:",int(np.sum(k>1e3)), " max floor %.3g"%f.max(), "min floor %.3g"%f.min())
    print(" rank2 flag false admitted:",[ (w,P[w][n]['m1/m3'],P[w][n]['kappa'],P[w]['y_max']) for w in adm if not P[w][n]['rank 2']])
    eps7=1/(4*math.pi*1e7)
    print(" margin max %.3g"%max(P[w][n]['m1/m3']/(eps7*P[w][n]['kappa']) for w in adm))
