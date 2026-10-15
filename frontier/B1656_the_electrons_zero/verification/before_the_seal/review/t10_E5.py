import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","D_of","np","twist_of"): globals()[k] = ns[k]
def lepD(w, t, ql=SIXY["L"], qr=SIXY["e"]):
    x, y = sector_twists(w, t, ql, qr); R = residues(x, y, t); c = cA(x, y, t, R, nth=64, ns=48)
    return abs(D_of(c, R))/nR2(R), abs(R["1"])/math.sqrt(nR2(R)), {s: (None if c[s] is None else round(c[s], 4)) for s in UNITS}
def fixed3w(p1, p2, t=OM):
    w3 = 3*line_w(p1, p2, t); d = t*w3 - w3; n = d.imag/t.imag; m = d.real - n*t.real
    return abs(m - round(m)) < 1e-9 and abs(n - round(n)) < 1e-9
def in_lattice(z, t=OM):
    n = z.imag/t.imag; m = z.real - n*t.real
    return abs(m - round(m)) < 1e-9 and abs(n - round(n)) < 1e-9
print("--- E5(b) lines: is 3w omega-fixed? is 9w in the lattice?")
for (p1, p2) in [(1/9, 2/9), (1/9, 0.0), (2/9, 1/9), (4/9, 1/9)]:
    w = line_w(p1, p2, OM); D, r1, c = lepD(w, OM)
    print((round(p1,3), round(p2,3)), "3w fixed:", fixed3w(p1, p2), " 9w in Lambda:", in_lattice(9*w), " lep |D|/|R|^2 = %.4f |R1|/|R| = %.1e" % (D, r1), c)
print("--- all 18 W59 lines: 3w fixed / 9w in lattice")
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
print(all(fixed3w(*l) for l in LINES18), all(in_lattice(9*line_w(*l, OM)) for l in LINES18))
print("--- E5(c): fictitious (-3,5) on W59 lines; sum is 2, so 'ubar' = 2w:")
for (p1, p2) in LINES18[:3]:
    w = line_w(p1, p2, OM); D, r1, c = lepD(w, OM, -3, 5)
    print((round(p1,3), round(p2,3)), "|D|/|R|^2 = %.4f |R1|/|R| = %.3f" % (D, r1), c, " 2w fixed?", in_lattice(OM*2*w - 2*w))
print("--- alternative isolating control: sum-preserving fictitious pair (-2,5): ubar = 3w (omega-fixed), delta = -7w (not in lattice)")
for (p1, p2) in LINES18[:3]:
    w = line_w(p1, p2, OM); D, r1, c = lepD(w, OM, -2, 5)
    print((round(p1,3), round(p2,3)), "|D|/|R|^2 = %.4f |R1|/|R| = %.3f" % (D, r1), c)
print("--- another isolating control: sum-NOT-preserving but difference in 9Z: (q_L,q_R) = (-6,3): ubar=-3w ; (q_L,q_R)=(0,9)? ubar=9w in lattice (degenerate)")
for (p1, p2) in LINES18[:3]:
    w = line_w(p1, p2, OM); D, r1, c = lepD(w, OM, -3, 6)
