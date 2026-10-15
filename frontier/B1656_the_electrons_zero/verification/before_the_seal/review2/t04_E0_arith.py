# Review 2, check 2: E0's exact arithmetic (Fractions) -- derived independently and cross-checked in complex floating arithmetic.
import numpy as np, math, sys, itertools, re, pathlib
from fractions import Fraction as Fr
SRC = pathlib.Path(__file__).resolve().parents[2].joinpath("the_electrons_zero.py").read_text()
# exec ONLY the arithmetic block of E0 (the lines from 'def isint' to the 'W59_set_invariant' assignment), verbatim
a = SRC.index("def isint(f)"); b = SRC.index('e0["void"]')
block = SRC[a:b]
# the block assigns into e0; give it one
ns2 = {"Fr": Fr, "e0": {}}
exec(block, ns2)
print({k: v for k, v in ns2["e0"].items()})
isint, lattice9, fixed3, L18F, NONFIX, mod1, S18, rot_minus, rot_plus = (ns2[k] for k in ("isint","lattice9","fixed3","L18F","NONFIX","mod1","S18","rot_minus","rot_plus"))
OM = complex(np.exp(2j*np.pi/3))
# (i) floating cross-check of lattice9 / fixed3 on 18 lines, the 3 NONFIX, and on a grid of ninths
def in_lat(z, tol=1e-9):
    n = z.imag/OM.imag; m = z.real - n*OM.real
    return abs(m - round(m)) < tol and abs(n - round(n)) < tol
bad = 0
for p9 in range(0, 18):
    for q9 in range(0, 18):
        p, q = Fr(p9, 9), Fr(q9, 9); w = float(p)*OM - float(q)
        l9 = in_lat(9*w); f3 = in_lat(OM*3*w - 3*w)
        if l9 != lattice9(p, q) or f3 != fixed3(p, q): bad += 1; print("MISMATCH", p, q, l9, lattice9(p, q), f3, fixed3(p, q))
print("grid of ninths (18x18): mismatches between exact and floating lattice9/fixed3:", bad)
# also thirds-of-ninths: 27ths grid, where fixed3 fails more often
bad = 0
for p27 in range(0, 27):
    for q27 in range(0, 27):
        p, q = Fr(p27, 27), Fr(q27, 27); w = float(p)*OM - float(q)
        l9 = in_lat(9*w); f3 = in_lat(OM*3*w - 3*w)
        if l9 != lattice9(p, q) or f3 != fixed3(p, q): bad += 1
print("grid of 27ths: mismatches:", bad)
# (ii) rotation formulas against complex arithmetic: omega*w = p' om - q' (minus) / p' om + q' (plus)
bad = 0
for p9 in range(-20, 21, 3):
    for q9 in range(-20, 21, 5):
        p, q = Fr(p9, 9), Fr(q9, 9)
        w = float(p)*OM - float(q); w2 = OM*w
        pm, qm = (-p - q), p                      # rot_minus image BEFORE mod
        if abs(w2 - (float(pm)*OM - float(qm))) > 1e-12: bad += 1
        wp = float(p)*OM + float(q); wp2 = OM*wp
        pp, qp = (q - p), -p
        if abs(wp2 - (float(pp)*OM + float(qp))) > 1e-12: bad += 1
print("rotation formulas vs complex arithmetic: mismatches", bad)
# (iii) mod1 on negative / integer Fractions
for f in [Fr(-1, 9), Fr(-10, 9), Fr(3), Fr(-3), Fr(0), Fr(17, 9), Fr(-9, 9), Fr(5, 3), Fr(-5, 3)]:
    m = mod1(f); assert 0 <= m < 1 and (f - m).denominator == 1, (f, m)
print("mod1 OK on negatives/integers")
# (iv) S18 content and the claims
print("|S18| =", len(S18), " rot_minus == S18:", rot_minus == S18, " rot_plus == S18:", rot_plus == S18, " |rot_plus & S18| =", len(rot_plus & S18))
# is the mod-1 reduction coherent: also check the rotation's cube = identity on S18 and bijectivity
def act_m(p, q): return (mod1(-p - q), mod1(p))
S = set(S18); S3 = {act_m(*act_m(*act_m(p, q))) for (p, q) in S}
print("rot_minus^3 = id on S18:", S3 == S)
# void condition used in code
print("NONFIX each 9w in lattice:", [lattice9(p,q) for p,q in NONFIX], " 3w fixed:", [fixed3(p,q) for p,q in NONFIX])
# all 18 'L18F' vs float LINES18
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
print("L18F matches LINES18:", all(abs(float(a)-c) < 1e-15 and abs(float(b_)-d) < 1e-15 for (a, b_), (c, d) in zip(L18F, LINES18)))
# are there OTHER lines (ninths grid) that are 'W59-like' but: 9w in lattice and 3w fixed?
fixed_ninths = [(p9, q9) for p9 in range(9) for q9 in range(9) if fixed3(Fr(p9, 9), Fr(q9, 9))]
print("ninth-grid points with 3w fixed:", len(fixed_ninths), "  (the 18 W59 lines are a subset?)", all((int(mod1(p)*9), int(mod1(q)*9)) in set(fixed_ninths) for p, q in S18))
print("fixed ninth-grid points NOT in W59 set:", [pq for pq in fixed_ninths if (Fr(pq[0],9), Fr(pq[1],9)) not in S18])
