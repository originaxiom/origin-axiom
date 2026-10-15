# Review 2, check 5b: is (5/9,5/9) a pure duplicate of (4/9,4/9) for the coupling's singular values (same S)?  (S: seed 3, not 1655)
import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","coupling","weighted_M","cA","D_of"): globals()[k] = ns[k]
rng = np.random.default_rng(3); SS = [rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2)) for _ in range(3)]
for t, tn in [(OM, "omega"), (-0.17+0.95j, "generic -0.17+0.95i")]:
    for sec in ("up", "down", "lep"):
        fl, fr = SECTORS[sec]; out = []
        for (p1, p2) in [(4/9, 4/9), (5/9, 5/9)]:
            w = line_w(p1, p2, t); x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t); c = cA(x, y, t, R, nth=64, ns=48)
            L = 640.0; u = {s: (math.sqrt(2*np.pi*L + c[s])*R[s] if c[s] is not None else 0j) for s in UNITS}
            out.append(([np.linalg.svd(coupling(S, weighted_M(u)), compute_uv=False) for S in SS], abs(D_of(c, R))/nR2(R), c))
        d = max(np.max(np.abs(a - b)/a[0]) for a, b in zip(out[0][0], out[1][0]))
        print(tn, sec, "same-S singular values (4/9,4/9) vs (5/9,5/9): max rel diff %.2e ; |D|/|R|^2: %.6f vs %.6f ; c_s equal: %s" % (d, out[0][1], out[1][1], all((out[0][2][s] is None and out[1][2][s] is None) or abs(out[0][2][s]-out[1][2][s]) < 1e-9 for s in UNITS)))
