import numpy as np, math, sys, warnings
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","a0_of","residues","sector_twists","line_w","OM","UNITS","nR2","D_of","np"): globals()[k] = ns[k]
warnings.simplefilter("error")        # any numpy RuntimeWarning (division by zero etc.) becomes an exception
w = line_w(2/9, 5/9, OM); x, y = sector_twists(w, OM, -3, 6); R = residues(x, y, OM)
for val in (0j, 1e-13, R["1"]):
    R2 = dict(R); R2["1"] = val
    a = a0_of(x, y, OM, R2); c = cA(x, y, OM, R2, nth=32, ns=24)
    print("R1 =", val, "-> a0['1'] =", a["1"], " c['1'] =", c["1"], " c['i'] =", None if c["i"] is None else round(c["i"], 6))
# all four channels None (degenerate): D_of / max of empty must not be reached in the cells; check helpers
R0 = {s: 0j for s in UNITS}
print("all-zero R:", a0_of(x, y, OM, R0), cA(x, y, OM, R0, nth=32, ns=24))
