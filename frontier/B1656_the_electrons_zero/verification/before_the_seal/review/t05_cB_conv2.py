import numpy as np, math, sys, time, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, ".")
from load_inst import load
from cbfast import cB_np
ns = load()
for k in ("cA","pairs","rmax_np","vangles","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np"): globals()[k] = ns[k]
def case(p1, p2, t, sec, n_list=(16, 24, 32), eps=1e-5, ql=None, qr=None):
    w = line_w(p1, p2, t); fl, fr = SECTORS[sec]
    ql = SIXY[fl] if ql is None else ql; qr = SIXY[fr] if qr is None else qr
    x, y = sector_twists(w, t, ql, qr); R = residues(x, y, t)
    ca = cA(x, y, t, R, eps=eps)
    ca6 = cA(x, y, t, R, eps=1e-7)
    for s in UNITS:
        if ca[s] is None: continue
        row = []
        for n in n_list:
            v, (a0, a1) = cB_np(pairs, rmax_np, vangles, x, y, t, s, R[s], n=n)
            row.append("n=%d |A5-B|=%.2e |A7-B|=%.2e" % (n, abs(v - ca[s]), abs(v - ca6[s])))
        print((round(p1, 3), round(p2, 3)), "tau=%s" % np.round(t, 3), sec, s, "|a0|=%.3f" % abs(a0), " | ".join(row))
# another generic tau, other line, all sectors
T2 = -0.17 + 0.95j
for sec in ("up", "down", "lep"):
    case(2/9, 5/9, T2, sec)
# leptons on non-fixed lines at omega
case(2/9, 0.0, OM, "lep"); case(4/9, 1/9, OM, "lep")
# at the sealed generic tau but a different line
case(4/9, 7/9, GEN, "down")
