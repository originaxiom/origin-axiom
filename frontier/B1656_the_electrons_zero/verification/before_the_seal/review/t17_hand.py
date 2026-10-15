# the hand: w = psi1*tau - psi2 (B1653) versus w' = psi1*tau + psi2, for W59's 18 (psi1, psi2)
import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","residues","sector_twists","OM","SECTORS","SIXY","UNITS","nR2","D_of","np"): globals()[k] = ns[k]
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
def frac(x): return x - math.floor(x + 1e-9)
# (1) invariance of the 18-set under the order-3 action induced on (psi1, psi2) by w -> omega*w
def act_minus(p1, p2): return (-p1 - p2, p1)           # w = p1*om - p2 : om*w = -p1 - (p1+p2) om = p1' om - p2'  -> p1' = -(p1+p2), p2' = p1
def act_plus(p1, p2):  return (p2 - p1, -p1)            # w = p1*om + p2 : om*w = -p1 + (p2 - p1) om = p1' om + p2'  -> p1' = p2 - p1, p2' = -p1
S18 = {(round(frac(a)*9) % 9, round(frac(b)*9) % 9) for a, b in LINES18}
def inv(act):
    img = {(round(frac(act(a, b)[0])*9) % 9, round(frac(act(a, b)[1])*9) % 9) for a, b in LINES18}
    return img == S18
print("W59 set invariant under the induced order-3 action:  minus convention (B1653):", inv(act_minus), "  plus convention:", inv(act_plus))
# (2) D per sector in the opposite hand
def line_plus(p1, p2, t): return p1*t + p2
res = {"up": [], "down": [], "lep": []}
for (p1, p2) in LINES18[:9] + LINES18[9:12]:
    w = line_plus(p1, p2, OM)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
        res[sec].append(abs(D_of(c, R))/nR2(R))
print("opposite hand (w = psi1 tau + psi2), |D|/|R|^2 over 12 of the 18 pairs: ", {k: (round(min(v), 4), round(max(v), 4)) for k, v in res.items()})
