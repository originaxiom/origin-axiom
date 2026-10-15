"""Main's independent check of the SM seat's W90 (one Higgs defect A = |d_a| shared by the three sectors, B1657's laws at first
order, the matter's defect and every phase free), on HZ2021 at M_Z (B1637's received file). Own code: interval logic on a
log grid of A, ratios' bands by first-order error propagation, k-sigma boxes."""
import json, itertools, numpy as np
d = json.load(open("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"))["masses_GeV"]
v, s = d["value"], d["sigma"]
def ratio(a, b):
    r = v[a]/v[b]; return r, r*np.hypot(s[a]/v[a], s[b]/v[b])
SECT = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lep": ("e", "mu", "tau")}
A = np.logspace(-5, 0, 2_000_001)
def allowed(sec, vac, k):
    (x1, e1), (x2, e2) = ratio(SECT[sec][0], SECT[sec][2]), ratio(SECT[sec][1], SECT[sec][2])
    lo1, hi1, lo2, hi2 = max(x1-k*e1, 1e-12), x1+k*e1, max(x2-k*e2, 1e-12), x2+k*e2
    if vac == "conj":
        return ((A >= lo2) & (A <= hi2)) | ((A >= lo1) & (A <= hi1))
    # parallel: B = 4 x1/A for some x1 in [lo1, hi1]; need some x2 in [lo2, hi2] with |A - B| <= 4 x2 <= A + B
    Bmin, Bmax = 4*lo1/A, 4*hi1/A
    # min over B in [Bmin, Bmax] of |A - B| and max of A + B
    dmin = np.where((A >= Bmin) & (A <= Bmax), 0.0, np.minimum(abs(A-Bmin), abs(A-Bmax)))
    smax = A + Bmax
    return (dmin <= 4*hi2) & (smax >= 4*lo2)
for k in (2, 3):
    res = {}
    for asg in itertools.product(("par", "conj"), repeat=3):
        m = allowed("up", asg[0], k) & allowed("down", asg[1], k) & allowed("lep", asg[2], k)
        res[asg] = m.any()
    print(f"k={k}: three-sector assignments with a common A:", [a for a, ok in res.items() if ok] or "none")
    for p, q in (("up", "down"), ("down", "lep"), ("up", "lep")):
        ok = []
        for a, b in itertools.product(("par", "conj"), repeat=2):
            m = allowed(p, a, k) & allowed(q, b, k)
            if m.any(): ok.append((a, b, float(A[m].min()), float(A[m].max())))
        print(f"   {p}-{q}:", [(a, b, f"{x:.4g}-{y:.4g}") for a, b, x, y in ok])
