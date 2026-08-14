"""B899 (M8, FENCED -- geometry only): do the operational S3-breaking
magnitudes correlate with mu's root geometry?

Registered comparison (masterplan v2): the per-frame deviation magnitudes
(B890 vacua, B891 matter) and per-frame leakage scales (B889) against the
per-root spacing invariants of mu. THREE data points per test -- stated up
front: nothing here can be more than a registered orientation; no fitting,
one pre-declared comparison per pair (log-log), banked as geometry.
"""
import json, os, math
import mpmath as mp

mp.mp.dps = 35
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")

# mu's roots at 35 digits
coeffs = [500716339200, -2075673600, -4769856, 2197]
rts = sorted(float(r) for r in mp.polyroots(coeffs))
r1, r2, r3 = rts
print("roots:", rts)
# per-root invariants: distance to nearest other root; |mu'(r)| (normalized)
def dmu(x):
    return float(abs(3*coeffs[0]*x**2 + 2*coeffs[1]*x + coeffs[2]))
near = [min(abs(r - s) for s in rts if s != r) for r in rts]
mup = [dmu(r) for r in rts]
print("nearest-spacing per root:", near)
print("|mu'| per root:", mup)

B890 = json.load(open(os.path.join(ROOT, "B890_foreign_pair/results.json")))
B891 = json.load(open(os.path.join(ROOT, "B891_matter_extension/results.json")))
dev890 = [float(B890["frames"][str(i)]["max_dev"]) for i in (0, 1, 2)]
dev891 = [float(B891["frames"][str(i)]["max_dev"]) for i in (0, 1, 2)]

# the banked vacuum->frame bijection maps frame i to vacuum/root index
B889 = json.load(open(os.path.join(ROOT, "B889_canonical_dictionary/results.json")))
vmap = {int(k): v for k, v in B889["vacuum_frame_map"].items()}
print("frame->root map (banked):", vmap)

def spearman3(a, b):
    ra = sorted(range(3), key=lambda i: a[i])
    rb = sorted(range(3), key=lambda i: b[i])
    ia = {v: i for i, v in enumerate(ra)}; ib = {v: i for i, v in enumerate(rb)}
    d2 = sum((ia[i]-ib[i])**2 for i in range(3))
    return 1 - d2  # for n=3: 1 - 6*d2/(n(n^2-1)) = 1 - d2/4 -> report d2 raw

def loglog_slope(x, y):
    lx = [math.log(v) for v in x]; ly = [math.log(v) for v in y]
    mx = sum(lx)/3; my = sum(ly)/3
    num = sum((lx[i]-mx)*(ly[i]-my) for i in range(3))
    den = sum((lx[i]-mx)**2 for i in range(3))
    s = num/den
    resid = sum((ly[i]-my-s*(lx[i]-mx))**2 for i in range(3))
    return s, resid

res = {"roots": rts, "nearest_spacing": near, "mu_prime": mup,
       "frame_to_root": vmap, "tests": {}}
for name, dev in (("b890_vacua", dev890), ("b891_matter", dev891)):
    # frame i's deviation vs its OWN root's invariants (via the banked map)
    dv = [dev[i] for i in (0, 1, 2)]
    for inv_name, inv in (("nearest_spacing", near), ("mu_prime", mup)):
        x = [inv[vmap[i]] for i in (0, 1, 2)]
        s, resid = loglog_slope(x, dv)
        ordmatch = (sorted(range(3), key=lambda i: x[i])
                    == sorted(range(3), key=lambda i: dv[i]))
        res["tests"][f"{name}_vs_{inv_name}"] = {
            "x": x, "dev": dv, "loglog_slope": s, "resid": resid,
            "order_match": ordmatch}
        print(f"{name} vs {inv_name}: slope {s:.3f} resid {resid:.3f} "
              f"order-match {ordmatch}")
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1)
print("saved")
