# Review 2: the plus convention w' = psi1*tau + psi2 -- all 18 pairs non-fixed? leptons lifted?  (not a sealed cell)
import numpy as np, math, sys
from fractions import Fraction as Fr
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","residues","sector_twists","OM","SECTORS","SIXY","UNITS","nR2","D_of","np"): globals()[k] = ns[k]
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
L18F = [(Fr(1, 9)*bb + Fr(i, 3), Fr(1, 9)*bb + Fr(j, 3)) for bb in (1, 2) for i in range(3) for j in range(3)]
# plus convention: w' = p om + q ; (om-1)*3w' = 3[(p om + q)(om - 1)] = 3[p om^2 + q om - p om - q] = 3[(-p - q) + (q - 2p) om]
fixedplus = lambda p, q: (3*(p + q)).denominator == 1 and (3*(q - 2*p)).denominator == 1
print("plus convention: number of the 18 pairs with 3w' omega-fixed:", sum(fixedplus(p, q) for p, q in L18F))
res = []
for (p1, p2) in LINES18[:9:2] + LINES18[10::3]:
    w = p1*OM + p2
    out = {}
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
        out[sec] = (round(abs(D_of(c, R))/nR2(R), 4), abs(R["1"])/math.sqrt(nR2(R)))
    print((round(9*p1), round(9*p2)), "plus-hand |D|/|R|^2 up/down/lep:", out["up"][0], out["down"][0], out["lep"][0], " lep |R1|/|R| = %.1e" % out["lep"][1])
