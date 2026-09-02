"""B850 Cell 4's 'multiplicity maxima' (4/3/4/8/2) vs SnapPy's geometric multiplicities of complex-length classes
to Re(l) <= 4 -- recomputed here (fc R37 said 12/12/11/11/6). Multiplicity = number of geodesic classes sharing a
complex length (SnapPy's own 'multiplicity' column)."""
import snappy
from collections import Counter
out = {}
for name in ("m004", "m003", "m136", "m009", "m015"):
    M = snappy.Manifold(name)
    spec = M.length_spectrum(4.0, full_rigor=True)
    mults = [int(g.multiplicity) for g in spec]
    out[name] = (max(mults), round(sum(mults)/len(mults), 2), len(mults))
    print(f"{name}: max multiplicity {max(mults):2d}   mean {sum(mults)/len(mults):.2f}   classes {len(mults)}")
bank = {"m004": 4, "m003": 3, "m136": 4, "m009": 8, "m015": 2}
print("bank's maxima reproduced as geometric multiplicities:", all(out[k][0] == v for k, v in bank.items()))
print("B850's ordering claim (m009 double m004) survives geometrically:", out["m009"][0] == 2*out["m004"][0])
