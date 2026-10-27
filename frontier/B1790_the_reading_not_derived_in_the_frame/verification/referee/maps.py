"""Attacks 3-4: the mirror and other candidate maps, per sector and per ratio, own driver.
For each map g: pres = max_sec d(spec_rd(p), spec_rd(gp)); flip = d(spec_rd(p), spec_other(gp)) per sector;
point = d(spec_S(p), spec_St(p)) (same point, no map)."""
import sys; sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import common as C, numpy as np, json
from fractions import Fraction as Fr
def fm(x): return float(x)
P = [(complex(0.35, 2.9), Fr(2, 5), Fr(3, 10)), (complex(0.12, 3.2), Fr(1, 10), Fr(7, 10)), (complex(0.71, 2.6), Fr(2, 7), Fr(1, 7))]
def maps(t, a, b):
    tb = t.conjugate()
    return {
        "mirror (1-conj tau, a, -a-b)": (1 - tb, a, -a - b),
        "pure conj (-conj tau, a, -b)": (-tb, a, -b),
        "charge conj w->-w (tau, -a, -b)": (t, -a, -b),
        "mirror o C: w-> conj w (1-conj tau, -a, a+b)": (1 - tb, -a, a + b),
        "T (tau+1, a, b-a)": (t + 1, a, b - a),
        "w->w+1 (tau, a, b+1)": (t, a, b + 1),
        "w->w+tau (tau, a+1, b)": (t, a + 1, b),
        "w->w+1/2": (t, a, b + Fr(1, 2)),
        "w->w+tau/2": (t, a + Fr(1, 2), b),
        "w->w+(1+tau)/2": (t, a + Fr(1, 2), b + Fr(1, 2)),
    }
out = []
for which in ("L_max", "L_2"):
    for t, a, b in P:
        sp = C.spectra(t, a, b, which)
        row = {"p": [t.real, t.imag, str(a), str(b), which]}
        row["same point S vs St, per sector, per ratio (m2/m3, m1/m3)"] = {s: np.abs(np.log(sp[(s, "S")] / sp[(s, "St")])).round(4).tolist() for s in C.SECT}
        for nm, (t2, a2, b2) in maps(t, a, b).items():
            sq = C.spectra(t2, a2, b2, which)
            pres = max(C.dln(sp[(s, rd)], sq[(s, rd)]) for s in C.SECT for rd in ("S", "St"))
            flip = {s: round(min(C.dln(sp[(s, "S")], sq[(s, "St")]), C.dln(sp[(s, "St")], sq[(s, "S")])), 4) for s in C.SECT}
            row[nm] = {"preserve_worst": pres, "flip_per_sector(min over direction)": flip}
        out.append(row)
        print(json.dumps(row, default=fm))
json.dump(out, open(__import__("pathlib").Path(__file__).resolve().parent / "maps.json", "w"), indent=1, default=fm)
