#!/usr/bin/env python3
# B674 ramanujan_trifocal - VX (run 2, corrected): exact sympy cross-checks of
# the PSLQ identifications found by trifocal_values.py.
# CONVENTION NOTE: trifocal_values.py prints PSLQ coefficient lists ASCENDING
# (c0 + c1 x + ... + cd x^d).  Run 1 of this script transcribed the R_s^5
# octic as if descending (preserved in vx_run1_superseded.txt); this run uses
# the correct order throughout.  Appends to values_output.txt.
import os
import sympy as sp
from mpmath import mp, mpf, exp, pi, sqrt, log, fabs, nstr

mp.dps = 220
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
def emit(s=""):
    print(s, flush=True)
    OUT.append(str(s))

x, y, t = sp.symbols('x y t')
emit("")
emit("## VX. EXACT CROSS-CHECKS (sympy, exact arithmetic; run 2 - corrected")
emit("##     coefficient-order convention; run 1 preserved in vx_run1_superseded.txt)")

# VX1: silver octic closed form.  Claim: U_s^2 = sqrt(k16) = (2^(1/4)-1)/(2^(1/4)+1)
a = sp.Rational(2)**sp.Rational(1, 4)
cand = (a - 1) / (a + 1)
mp1 = sp.minimal_polynomial(cand, x)
emit(f"VX1 minpoly((2^(1/4)-1)/(2^(1/4)+1)) = {sp.expand(mp1)}")
emit(f"    PSLQ minpoly of U_s^2:            x**4 - 12*x**3 + 6*x**2 - 12*x + 1")
emit(f"    match: {sp.expand(mp1) == sp.expand(x**4 - 12*x**3 + 6*x**2 - 12*x + 1)}")
q_s = exp(-4 * pi)
def poch_pm(q, r, m, sign):
    p = mpf(1); e = r
    E = int((mp.dps + 40) * mp.log(10) / (-log(q))) + 12
    while e <= E:
        p *= (1 + sign * q**e); e += m
    return p
U_s = sqrt(mpf(2)) * exp(log(q_s) / 8) * poch_pm(q_s, 2, 2, 1) / poch_pm(q_s, 1, 2, 1)
d = fabs(U_s**2 - mpf(sp.N(cand, 230).__str__()))
emit(f"    |U_s^2 - (2^(1/4)-1)/(2^(1/4)+1)| = {nstr(d, 3)} (dps 220)"
     f" -> {'PASS' if d < mpf(10)**-200 else 'FAIL'}")
emit(f"    => U_s = sqrt((2^(1/4)-1)/(2^(1/4)+1)) = k16^(1/4) exactly")

# VX2: k16 = U_s^4 closed form = ((2^(1/4)-1)/(2^(1/4)+1))^2
mp2 = sp.minimal_polynomial(cand**2, x)
emit(f"VX2 minpoly(((2^(1/4)-1)/(2^(1/4)+1))^2) = {sp.expand(mp2)}")
emit(f"    PSLQ minpoly of U_s^4 = k16:       x**4 - 132*x**3 - 250*x**2 - 132*x + 1")
emit(f"    match: {sp.expand(mp2) == sp.expand(x**4 - 132*x**3 - 250*x**2 - 132*x + 1)}")

# VX3: tie the two independent silver-RR identifications together EXACTLY.
#   t = 1/y - 11 - y  (the classical RR eta identity variable, control C6),
#   so y = R_s^5 satisfies the degree-8 lift y^4 * quart(1/y - 11 - y).
quart = t**4 - 286750*t**3 + 1343750*t**2 + 50781250*t + 244140625
octic_asc = [1, -286794, 10807222, -82016442, 208205070,
             82016442, 10807222, 286794, 1]          # as printed (ASCENDING)
octic = sum(c * y**k for k, c in enumerate(octic_asc))
L = sp.expand(y**4 * quart.subs(t, 1/y - 11 - y))
emit(f"VX3 y^4*quart(1/y-11-y) - minpoly(R_s^5) = {sp.expand(L - octic)}")
emit(f"    -> the tR_s quartic and the R_s^5 octic (two INDEPENDENT PSLQ")
emit(f"       results) are EXACTLY linked by the classical identity; equality"
     f" holds, not just divisibility.")

# VX4: structural symmetries of the found polynomials.
P48 = (x**8 - 13320*x**7 + 92188*x**6 + 275400*x**5 + 340038*x**4
       + 275400*x**3 + 92188*x**2 - 13320*x + 1)     # palindromic: asc = desc
pal = sp.expand(x**8 * P48.subs(x, 1/x) - P48) == 0
emit(f"VX4 k48 octic palindromic (k48 and 1/k48 are conjugates): {pal}")
sgn = sp.expand(x**8 * octic.subs(y, -sp.Rational(1)/x) - octic.subs(y, x)) == 0
emit(f"    minpoly(R_s^5) satisfies P(x) = x^8 P(-1/x)  (y and -1/y conjugate:"
     f" the RR unit structure): {sgn}")
emit(f"    tR_s quartic constant term = 244140625 = 5^12: {244140625 == 5**12}"
     f"  (the level-5 eta variable carries a pure 5-power norm: the 5-vein shape)")
emit(f"    V_s^3 octic: leading coeff 2097152 = 2^21: {2097152 == 2**21}; "
     f"constant -1; |c1_desc| = 134217728 = 2^27: {134217728 == 2**27} "
     f"(denominator a pure 2-power: the octic/2-adic side pressing on the cubic leg)")

# VX5: H_-48 exact root vs an independent dps-320 j recomputation
mp.dps = 320
q_g = exp(-4 * pi * sqrt(mpf(3)))
E4 = mpf(1); E6 = mpf(1)
for n in range(1, 80):
    tt = q_g**n / (1 - q_g**n)
    E4 += 240 * n**3 * tt
    E6 -= 504 * n**5 * tt
jg = 1728 * E4**3 / (E4**3 - E6**2)
jex = mpf(1417905000) + mpf(818626500) * sqrt(mpf(3))
d = fabs(jg - jex)
emit(f"VX5 |j(2*sqrt3*i) - (1417905000 + 818626500*sqrt3)| = {nstr(d, 3)} "
     f"(dps 320) -> {'PASS' if d < mpf(10)**-290 else 'FAIL'}")
emit(f"    H_-48 coefficient factorizations: 2835810000 = "
     f"{dict(sp.factorint(2835810000))}; 6549518250000 = "
     f"{dict(sp.factorint(6549518250000))}")

# VX6: caution note quantified - the handoff-literal octic vs the modular one
mp.dps = 220
Uh_s = sqrt(mpf(2)) * exp(log(q_s) / 8) * poch_pm(q_s, 1, 2, -1) / poch_pm(q_s, 2, 2, 1)
emit(f"VX6 |U_s - Uh_s| = {nstr(fabs(U_s - Uh_s), 3)}  (the literal product sits"
     f" ~1e-11 from the modular value at silver; PSLQ non-identification of Uh"
     f" is therefore consistent-with, not proof-of, transcendence - the"
     f" discriminating fact is the exact identity Uh = sqrt2 q^(1/4)"
     f" eta(tau)/eta(4tau), control C5)")

with open(os.path.join(HERE, "values_output.txt"), "a") as f:
    f.write("\n".join(OUT) + "\n")
print("VX DONE")
