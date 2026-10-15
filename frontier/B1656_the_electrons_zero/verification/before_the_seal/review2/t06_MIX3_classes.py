# Review 2, check 5: what do the MIX3 lines span?  exact classes of ubar, delta (mod the lattice, up to sign), the mirror relation (5/9,5/9) ~ (4/9,4/9), orbits of the 18 lines.
import numpy as np, math, sys
from fractions import Fraction as Fr
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("residues","sector_twists","line_w","OM","SECTORS","SIXY","UNITS","nR2","np"): globals()[k] = ns[k]
mod1 = lambda f: f - (f.numerator // f.denominator)
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
L18F = [(Fr(1, 9)*bb + Fr(i, 3), Fr(1, 9)*bb + Fr(j, 3)) for bb in (1, 2) for i in range(3) for j in range(3)]
MIX3i = [0, 4, 13]
print("MIX3 (ninths):", [(int(9*L18F[i][0]), int(9*L18F[i][1])) for i in MIX3i])
def cls(p, q, k):                      # k*w mod Lambda for w = p om - q, as (a,b) in [0,1)^2 meaning a om - b
    return (mod1(k*p), mod1(k*q))
def sgn_class(c):                      # up to sign (z -> -z)
    neg = (mod1(-c[0]), mod1(-c[1]))
    return min(c, neg)
pairs_ = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6), "fict(-3,5)": (-3, 5), "(-2,5)": (-2, 5)}
for name, (ql, qr) in pairs_.items():
    ub = [cls(*L18F[i], ql+qr) for i in MIX3i]; de = [cls(*L18F[i], ql-qr) for i in MIX3i]
    print("%-11s ubar classes (a,b in ninths of omega-1 coords): %s | up to sign: %d distinct | delta classes: %s | up to sign: %d distinct" % (
        name, [(str(a), str(b)) for a, b in ub], len({sgn_class(c) for c in ub}), [(str(a), str(b)) for a, b in de], len({sgn_class(c) for c in de})))
print("signed ubar distinct (up):", len({cls(*L18F[i], -3) for i in MIX3i}), " (down/lep):", len({cls(*L18F[i], 3) for i in MIX3i}))
# the classes of all 18 lines under the order-3 rotation and the mirror
rot = lambda p, q: (mod1(-p - q), mod1(p))
mir = lambda p, q: (mod1(-p), mod1(-q))
S18 = {(mod1(p), mod1(q)) for p, q in L18F}
seen = set(); classes = []
for pq in sorted(S18):
    if pq in seen: continue
    orb = set(); stack = [pq]
    while stack:
        a = stack.pop()
        if a in orb: continue
        orb.add(a); stack += [rot(*a), mir(*a)]
    seen |= orb; classes.append(sorted(orb))
print("classes of the 18 lines under <rotation, mirror>:", len(classes))
for c in classes: print("  size", len(c), [(int(9*a), int(9*b)) for a, b in c])
mixc = [next(i for i, c in enumerate(classes) if (mod1(L18F[j][0]), mod1(L18F[j][1])) in c) for j in MIX3i]
print("MIX3 lines belong to classes:", mixc, "-> distinct classes spanned:", len(set(mixc)), "of", len(classes))
# numeric: are R_s of (4/9,4/9) and (5/9,5/9) equal, per sector? (mirror image) -- R is not an E-cell output
for sec, (fl, fr) in SECTORS.items():
    Rs = []
    for (p1, p2) in [(4/9, 4/9), (5/9, 5/9)]:
        w = line_w(p1, p2, OM); x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); Rs.append(R)
    print(sec, "R(4/9,4/9) vs R(5/9,5/9):", {s: (np.round(Rs[0][s], 5), np.round(Rs[1][s], 5)) for s in UNITS})
