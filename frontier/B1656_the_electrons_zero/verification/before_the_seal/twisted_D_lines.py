"""C2 exploration (main, unsealed): D_sector/|R|^2 on all 18 of W59's Higgs lines at omega, and the same lines' phases at
a generic tau (control: no order-3 symmetry there)."""
import numpy as np, twisted_D_explore as T
OM = T.OM; GEN = 0.13 + 1.07j
def Dsec(w, t):
    out = {}
    for sec, (fl, fr) in T.SECTORS.items():
        x = T.twist_of(T.SIXY[fl]*w, t); y = T.twist_of(T.SIXY[fr]*w, t)
        R = T.residues(x, y, t); n2 = sum(abs(R[s])**2 for s in R); c = T.cnorms(x, y, t, R)
        out[sec] = abs(sum(c[s]*R[s]**2 for s in T.UNITS if c[s] is not None))/n2
    return out
ninth, third = 1/9, 1/3
rows = []
for base in (ninth, 2*ninth):
    for i in range(3):
        for j in range(3):
            p1, p2 = base + i*third, base + j*third
            d = Dsec(T.line_w(p1, p2, OM), OM); rows.append((p1, p2, d))
            print(f"omega line ({p1:.3f},{p2:.3f}): up {d['up']:.4f} down {d['down']:.4f} lep {d['lep']:.2e}")
print("max lepton |D|/|R|^2 over the 18 lines at omega:", max(r[2]['lep'] for r in rows))
print("min quark |D|/|R|^2 over the 18 lines at omega:", min(min(r[2]['up'], r[2]['down']) for r in rows))
for p1, p2 in [(1/9, 1/9), (2/9, 5/9)]:
    d = Dsec(T.line_w(p1, p2, GEN), GEN)
    print(f"generic tau, phases ({p1:.3f},{p2:.3f}): up {d['up']:.4f} down {d['down']:.4f} lep {d['lep']:.4f}")
