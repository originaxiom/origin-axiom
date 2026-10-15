# Review 2, check 4b: the lift law  L*s3/s1 (L=2560) == |D| |l_S(M_R)| / (8 pi s1^2 s2)  on lines/seeds other than the sealed (MIX3, seed 1655).
import numpy as np, math, sys, time, pathlib
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","coupling","weighted_M","cA","D_of"): globals()[k] = ns[k]
SRC = pathlib.Path(__file__).resolve().parents[2].joinpath("the_electrons_zero.py").read_text()
exec(SRC[SRC.index("def l_S(S, M):"): SRC.index("e6 = {")], globals())
def one(p1, p2, t, seed, nS=5, quad=(64, 48)):
    rng = np.random.default_rng(seed)
    SS = [rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)) for _ in range(nS)]
    w = line_w(p1, p2, t); out = {"lep_ratio": 0.0, "Lratio": [], "q40": [], "law": []}
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t); c = cA(x, y, t, R, nth=quad[0], ns=quad[1])
        for S in SS:
            vals = {}
            for L in (40.0, 640.0, 2560.0):
                u = {s: (math.sqrt(2*np.pi*L + c[s])*R[s] if c[s] is not None else 0j) for s in UNITS}
                sv = np.linalg.svd(coupling(S, weighted_M(u)), compute_uv=False); vals[L] = sv[2]/sv[0]
            if sec == "lep" and t == OM: out["lep_ratio"] = max(out["lep_ratio"], max(vals.values()))
            elif sec != "lep" or t != OM:
                out["Lratio"].append(abs(2560*vals[2560]/(640*vals[640]) - 1)); out["q40"].append(vals[40.0])
                MR = weighted_M(R); s0 = np.linalg.svd(coupling(S, MR), compute_uv=False)
                pred = abs(D_of(c, R))*abs(l_S(S, MR))/(8*np.pi*s0[0]**2*s0[1]); out["law"].append(abs(2560*vals[2560]/pred - 1))
    return out
t0 = time.time(); allr = {"lep_ratio": 0.0, "Lratio": [], "q40": [], "law": []}
cases = [((7/9, 7/9), OM, 2026), ((2/9, 5/9), OM, 31337), ((4/9, 7/9), OM, 424242), ((1/9, 4/9), OM, 99), ((5/9, 8/9), OM, 12345), ((8/9, 8/9), OM, 777), ((1/9, 7/9), OM, 4242),
         ((0.137, 0.291), GEN, 5), ((1/9, 1/9), GEN, 6)]
for (p1, p2), t, seed in cases:
    o = one(p1, p2, t, seed)
    print((round(9*p1, 2), round(9*p2, 2)), np.round(t, 3), "seed", seed, "| lep sigma3/sigma1 max %.1e | L-ratio err max %.2e | q40 min %.2e | lift-law err max %.2e [%.0fs]" % (o["lep_ratio"], max(o["Lratio"]), min(o["q40"]), max(o["law"]), time.time()-t0), flush=True)
    allr["lep_ratio"] = max(allr["lep_ratio"], o["lep_ratio"]); allr["Lratio"] += o["Lratio"]; allr["q40"] += o["q40"]; allr["law"] += o["law"]
print("OVERALL (", len(allr["law"]), "quark/generic-tau draws): lepton-at-omega ratio max %.1e ; L-ratio err max %.2e ; q40 min %.2e ; lift-law err max %.2e (thr 0.02)" % (allr["lep_ratio"], max(allr["Lratio"]), min(allr["q40"]), max(allr["law"])))
