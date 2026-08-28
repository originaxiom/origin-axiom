#!/usr/bin/env python3
"""MEMO-105 CELL (MENU-1, TIER 1): THE MENU'S WIDTH — the owner signed
the instrument with the location line ("maps composed of banked
objects only, degrees confined to the degree ledger's rank-1 lattice
{-2,0,1,3}, composition depth <= the weld book's price scale"); this
cell FREEZES the tier-1 instantiation of that line and RUNS the
enumeration.  Everything below this docstring's PROTOCOL block was
written before any enumeration ran; the numbers bank whatever they
are.

PROTOCOL (FROZEN BEFORE THE RUN):
  Atoms (17; every one a banked exact dimensionless quantity, degree 0
  in memo 96's ledger, so the lattice constraint is satisfied
  identically at tier 1; grammar constants 1, 2, 3 declared):
    1, 2, 3 (grammar constants); 11 (the sum rule, B928);
    12 (Vol = 12 Vol_orb, B1188; the Coxeter number); 27, 64, 72, 78
    (the stack's dims: the 27, the glued 64, the roots, dim e6);
    112 (the discrete ladder's integer count, B1188); 953, 2304 (the
    value arc's twist pair, B931/B910-928); 151/64, 553/64 (the banked
    sum-rule pair, 151/64 + 553/64 = 11); 3/8 (the reproduced
    sin^2 theta_W row); phi = (1+sqrt5)/2 (memo 49/90); 2+sqrt3
    (memo 99's fundamental unit).  Complex atoms (omega, 2-omega)
    excluded: the tier-1 menu is real.  Transcendental atoms (Vol,
    pi^2/6, 2 log phi) excluded from tier 1 (declared tier 2).
  Grammar: binary ops {+, -, *, /} on ORDERED operands; expression
  size <= 3 atom-occurrences (the price-scale instantiation of
  "composition depth"); optionally ONE sqrt at the root.  Nothing
  else: no other unary ops, no sqrt inside, no powers beyond what
  the ops compose.
  Dedup: values identified by 40 significant digits at 60-dps
  arithmetic (collision risk negligible at these heights; every
  banked value keeps one witness recipe, so any suspected collision
  is re-checkable exactly).  Division guarded at |denominator| >
  1e-30.  No magnitude pruning (the atom scale caps intermediates
  at ~2304^2, far inside range).
  THE MENU: M1 = every distinct value in the OPEN interval (0,1)
  reachable by the grammar.  (0,1)-membership is the ONLY filter —
  no shape or ordering filter, so nothing measured-informed enters
  (Gate 5: this cell never touches a measured value).
  BANKED QUANTITIES (preregistered): W1 = |M1| (the width); the
  decile histogram; D = the median nearest-neighbor gap and the
  minimum gap (the menu's RESOLUTION).  Guaranteed nonempty (3/8 is
  an atom), so the two-outcome fork is not empty/nonempty but the
  STANDING RULE the width buys:
  THE DENOMINATOR RULE (the instrument's point): any future MENU-2
  sealed comparison inherits W1 as its family-wise denominator, and
  a claimed hit at precision coarser than the local menu spacing
  (scale D) carries NO evidential weight at this bound — the exact
  discipline of memo 95's 324-pair scan and B1126, now fixed BEFORE
  any data contact instead of after.
Gate 5 untouched (no measured value appears anywhere in this cell).
"""
from mpmath import mp, mpf, sqrt as msqrt

mp.dps = 60
ATOMS = [
    ("1", mpf(1)), ("2", mpf(2)), ("3", mpf(3)), ("11", mpf(11)),
    ("12", mpf(12)), ("27", mpf(27)), ("64", mpf(64)), ("72", mpf(72)),
    ("78", mpf(78)), ("112", mpf(112)), ("953", mpf(953)), ("2304", mpf(2304)),
    ("151/64", mpf(151)/64), ("553/64", mpf(553)/64), ("3/8", mpf(3)/8),
    ("phi", (1 + msqrt(5))/2), ("2+sqrt3", 2 + msqrt(3)),
]
OPS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if abs(b) > mpf("1e-30") else None,
}

def key(v):
    return mp.nstr(v, 40, strip_zeros=False)

# level 1: atoms
V1 = {}
for name, v in ATOMS:
    V1.setdefault(key(v), (v, name))
# level 2: op(atom, atom), ordered
V2 = {}
for o, f in OPS.items():
    for n1, a in ATOMS:
        for n2, b in ATOMS:
            r = f(a, b)
            if r is not None:
                k = key(r)
                if k not in V1 and k not in V2:
                    V2[k] = (r, f"({n1} {o} {n2})")
# level 3: op(V2, atom) and op(atom, V2), ordered
V3 = {}
for o, f in OPS.items():
    for k2, (v2, r2) in V2.items():
        for n1, a in ATOMS:
            for x, y, rec in ((v2, a, f"({r2} {o} {n1})"), (a, v2, f"({n1} {o} {r2})")):
                r = f(x, y)
                if r is not None:
                    k = key(r)
                    if k not in V1 and k not in V2 and k not in V3:
                        V3[k] = (r, rec)
ALL = {}
for D_ in (V1, V2, V3):
    for k, (v, rec) in D_.items():
        ALL.setdefault(k, (v, rec))
print(f"value pool: {len(V1)} atoms, {len(V2)} at size 2, {len(V3)} at size 3 "
      f"(distinct values, ordered-operand grammar)")

# the menu: (0,1) values, plus one optional root-sqrt (sqrt maps (0,1)->(0,1))
MENU = {}
for k, (v, rec) in ALL.items():
    if 0 < v < 1:
        MENU.setdefault(k, (v, rec))
for k, (v, rec) in list(MENU.items()):
    s = msqrt(v)
    ks = key(s)
    if ks not in MENU:
        MENU[ks] = (s, f"sqrt({rec})")
W1 = len(MENU)
vals = sorted(v for v, _ in MENU.values())
print(f"\nW1 (THE TIER-1 MENU WIDTH) = {W1}")

# decile histogram
hist = [0]*10
for v in vals:
    hist[min(9, int(v*10))] += 1
print("decile histogram (0.0-0.1 ... 0.9-1.0):")
print("   " + "  ".join(f"{h}" for h in hist))

# resolution: nearest-neighbor gaps
gaps = sorted(vals[i+1] - vals[i] for i in range(len(vals)-1))
med = gaps[len(gaps)//2]
print(f"menu resolution: median nearest-neighbor gap D = {mp.nstr(med, 6)}, "
      f"minimum gap = {mp.nstr(gaps[0], 6)}")
smallest = vals[0]
largest = vals[-1]
print(f"extremes: smallest menu value {mp.nstr(smallest, 10)}, largest {mp.nstr(largest, 10)}")
# a few witness recipes near the middle, for the record's legibility
mid = [(v, rec) for v, rec in sorted(MENU.values())][W1//2 : W1//2 + 3]
for v, rec in mid:
    print(f"   witness: {mp.nstr(v, 12)} = {rec}")

print(f"""
THE DENOMINATOR RULE, NOW QUANTITATIVE (banked before any data
contact): the tier-1 menu holds W1 = {W1} values in (0,1) with median
spacing ~{mp.nstr(med, 3)}.  Any future MENU-2 sealed comparison at this
complexity bound inherits W1 as its family-wise denominator, and a
hit resolved no finer than the local spacing is chance, not evidence
— the memo-95/B1126 discipline, fixed in advance.  READING (typed,
interpretive sentence labeled): a menu this shape means the
"prediction" arm cannot be won at tier 1 by VALUE ALONE — it needs a
forcing theorem that selects one map before looking (exactly the
pincer's surviving slot); absent that, the values-as-menu arm stands
as the default.  Tier 2 (transcendental atoms Vol, pi^2/6, 2 log phi)
and any bound change are NEW preregistrations, not amendments.
Gate 5 untouched.""")
