# Review 2, check 1b: E1's logic WITH the correction (the revised cA), on lines/taus other than the sealed ((1/9,1/9) at OM / GEN), all sectors.
# Also: the same without the correction (a0 zeroed) to show the correction is what makes it pass; and the ratio test for the O(eps^4) term.
import numpy as np, math, sys, time
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","a0_of","pairs"): globals()[k] = ns[k]
import types
def cA_nocorr(x, y, t, R, eps=1e-5, scale=1.0, nth=96, ns_=64):
    # copy of cA with the correction removed: run the real cA, then subtract the correction it added
    A0 = a0_of(x, y, t, R); c = cA(x, y, t, R, eps=eps, scale=scale, nth=nth, ns=ns_)
    return {s: (None if c[s] is None else c[s] - scale**2*np.pi*eps**2*abs(A0[s])**2) for s in UNITS}
T3 = 0.2 + 0.55j; T4 = -0.3 + 2.0j
cases = [((2/9, 5/9), OM, "OM"), ((4/9, 7/9), OM, "OM"), ((2/9, 5/9), GEN, "GEN"), ((0.137, 0.291), GEN, "GEN"), ((0.613, 0.287), -0.17+0.95j, "T2"),
         ((1/9, 2/9), OM, "OM"), ((5/9, 8/9), 0.31+0.7j, "T.31+.7i"), ((1/9, 4/9), 0.45+0.6j, "T.45+.6i"), ((7/9, 7/9), T3, "T3"), ((0.4, 0.15), T4, "T4"), ((1/9, 1/9), 0.31+0.7j, "T.31+.7i")]
t0 = time.time(); allsp = []; allct = []; allsp_nc = []; allct_nc = []
for (p1, p2), t, tn in cases:
    w = line_w(p1, p2, t); sp = []; ct = []; spn = []; ctn = []
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
        cs = [cA(x, y, t, R, eps=e) for e in (1e-3, 1e-4, 1e-5)]
        c2 = [cA(x, y, t, R, eps=e, scale=2.0) for e in (1e-3, 1e-4)]
        csn = [cA_nocorr(x, y, t, R, eps=e) for e in (1e-3, 1e-4, 1e-5)]
        c2n = [cA_nocorr(x, y, t, R, eps=e, scale=2.0) for e in (1e-3, 1e-4)]
        for s in UNITS:
            if cs[0][s] is None: continue
            sp.append(max(c[s] for c in cs) - min(c[s] for c in cs)); ct.append((c2[1][s] - c2[0][s])/(6*np.pi*math.log(10)) - 1)
            spn.append(max(c[s] for c in csn) - min(c[s] for c in csn)); ctn.append((c2n[1][s] - c2n[0][s])/(6*np.pi*math.log(10)) - 1)
    allsp += sp; allct += ct; allsp_nc += spn; allct_nc += ctn
    print((round(p1,3), round(p2,3)), tn, "spread max %.2e (thr 1e-9) | control max|v-1| %.2e (thr 1e-6) || NO correction: spread %.2e, control %.2e  [%.0fs]" % (max(sp), max(abs(v) for v in ct), max(spn), max(abs(v) for v in ctn), time.time()-t0), flush=True)
print("OVERALL with correction: spread max %.3e, control max|v-1| %.3e ; without: %.3e, %.3e" % (max(allsp), max(abs(v) for v in allct), max(allsp_nc), max(abs(v) for v in allct_nc)))
