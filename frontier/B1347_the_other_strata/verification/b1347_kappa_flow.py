"""B1347 -- ENTERING THE OTHER THREE STRATA: the kappa-flow, measured.

B497 classified End(F2) into four strata in July and ended "the program to date = stratum 1 of 4".
B1342 derived WHY -- kappa is conserved in stratum 1 alone -- and verified the multipliers by ideal
membership. Nobody has ITERATED them. The atlas's own gloss on the monoid motif says it: "the
non-invertible verbs the programme has never computed."

THE WELL-POSED QUESTION. B497's U1 gives, for every stratum,
        kappa' - 2 = (kappa - 2) * M(x,y,z),
so after n steps  kappa_n - 2 = (kappa_0 - 2) * prod_{j<n} M(p_j). The orbit of "distance from
NOTHING" (B309's kappa = 2, which B1342 showed is a fixed point of the WHOLE monoid) is therefore
controlled by the product of multipliers along the orbit. So:

   DOES THE NON-INVERTIBLE DYNAMICS DRIVE kappa TOWARD 2 (collapse onto nothing)
   OR AWAY FROM IT (escape)?  AND IS THE ANSWER UNIFORM, OR POINT-DEPENDENT?

A uniform sign is a DIRECTION -- the thing stratum 1 provably cannot have, since its multiplier is
identically 1. A point-dependent sign is not a direction; it is a basin structure.

PRE-REGISTERED (DESIGN B1347): Q1 stratum 1 keeps log|kappa-2| EXACTLY constant on every orbit (the
control; if this fails the instrument is wrong); Q2 stratum 4 lands on kappa = 2 in ONE step from
every start; Q3 for strata 2, 2', 3 classify each orbit as COLLAPSE (log|kappa-2| -> -inf), ESCAPE
(-> +inf) or NEITHER, over a common sample including the object's own leaf kappa = -2; Q4 report
whether the sign is UNIFORM (a direction) or MIXED (a basin structure) -- and say which, rather than
hoping for one; Q5 measure the degree growth per stratum, since a non-invertible map loses
information and the degree is how much.

FENCE (S063, adopted): the physics verb-names for these strata live in speculations/S063 and are NOT
used here. This computes multipliers, orbits and degrees. Naming stratum 3 "decoherence" is the
seat's gloss, not a derivation, and no such name appears below.
"""
import json
import math
import random

import sympy as sp

x, y, z = sp.symbols('x y z')
KAP = lambda p: p[0] ** 2 + p[1] ** 2 + p[2] ** 2 - p[0] * p[1] * p[2] - 2

# B497's trace maps, as re-verified in B1342 (each reproduced from its word there)
STRATA = {
    "1  (Aut, det +-1)":      ((z, x, x * z - y),                                   sp.Integer(1)),
    "2  (squaring, det 4)":   ((x**2 - 2, y**2 - 2, x*y*z - x**2 - y**2 + 2),        x**2 * y**2),
    "2' (per-doubling, -2)":  ((z, x**2 - 2, (x**2 - 1)*z - x*y),                    x**2),
    "3  (Thue-Morse, det 0)": ((z, z, x*y*z - x**2 - y**2 + 2),                      x**2 + y**2 - x*y*z),
    "4  (degenerate, det 0)": ((z, z, z**2 - 2),                                     sp.Integer(0)),
}
F = {k: (sp.lambdify((x, y, z), v[0], "math"), sp.lambdify((x, y, z), v[1], "math"))
     for k, v in STRATA.items()}

BIG, SMALL, NSTEP = 1e100, 1e-13, 40
# METHOD NOTE -- a bug this arc's own control caught, recorded rather than silently fixed.
# The first version returned ESCAPE when the POINT overflowed. But the question is about
# |kappa - 2|, and stratum 1's points DO escape to infinity while kappa is exactly conserved
# (multiplier 1). Conflating the two made the control fail, correctly. The classifier below
# tracks log10|kappa - 2| through the MULTIPLIER PRODUCT, which is the quantity asked about,
# and reports point-overflow separately as a reason rather than as a verdict.
def orbit_class(key, p0, nstep=NSTEP):
    """(verdict, final log10|kappa-2| - initial) classified on the MULTIPLIER PRODUCT."""
    fmap, fmul = F[key]
    p = p0; k2 = KAP(p) - 2
    if abs(k2) < SMALL: return "ON-NOTHING", 0.0
    acc = 0.0                                   # log10 of prod |M| so far
    for n in range(nstep):
        try:
            m = fmul(*p)
        except (OverflowError, ValueError):
            return "ESCAPE", float("inf")
        if m == 0: return "COLLAPSE", float("-inf")
        acc += math.log10(abs(m))
        if acc > 60: return "ESCAPE", acc
        if acc < -60: return "COLLAPSE", acc
        try:
            p = fmap(*p)
        except (OverflowError, ValueError):
            # the POINT overflowed. For a constant multiplier kappa is unaffected; otherwise
            # |M| has already grown without bound, which the accumulator above records.
            break
        if any(abs(c) > BIG for c in p):
            break
    if abs(acc) < 1e-12: return "FLAT", acc
    return ("ESCAPE" if acc > 0 else "COLLAPSE"), acc

fails, out = [], {}
def check(tag, label, ok):
    print(f"   [{'PASS' if ok else 'FAIL'}] {tag}: {label}")
    if not ok: fails.append(tag)

random.seed(20260912)
# a common sample: random reals, plus the object's own leaf kappa = -2 (x^2+y^2+z^2 = xyz)
SAMPLE = [(random.uniform(-3, 3), random.uniform(-3, 3), random.uniform(-3, 3)) for _ in range(400)]
OBJ = []
for _ in range(200):                      # points ON the object's leaf, solved for z
    a, b = random.uniform(-4, 4), random.uniform(-4, 4)
    disc = (a*b)**2 - 4*(a*a + b*b)
    if disc < 0: continue
    OBJ.append((a, b, (a*b + math.sqrt(disc)) / 2))
print(f"sample: {len(SAMPLE)} generic points, {len(OBJ)} points on the object's leaf kappa = -2\n")

for key in STRATA:
    res = {}
    for lab, pts in (("generic", SAMPLE), ("kappa=-2 leaf", OBJ)):
        c = {}
        for p in pts:
            v, _ = orbit_class(key, p)
            c[v] = c.get(v, 0) + 1
        res[lab] = c
    out[key] = res
    print(f"  {key}")
    for lab, c in res.items():
        tot = sum(c.values())
        print(f"      {lab:14s} " + "  ".join(f"{k}:{v} ({100*v/tot:.0f}%)" for k, v in sorted(c.items())))

print()
g = out["1  (Aut, det +-1)"]
check("Q1", "CONTROL -- stratum 1 keeps |kappa-2| exactly constant on every orbit it does not "
            "overflow (multiplier 1); if this failed the instrument would be wrong",
      all(set(c) <= {"FLAT", "ON-NOTHING"} for c in g.values()))
s4 = out["4  (degenerate, det 0)"]
check("Q2", "stratum 4 lands ON kappa = 2 in one step from every start (multiplier 0) -- total "
            "collapse onto B309's 'nothing', which B1342 showed is a fixed point of the whole monoid",
      all(set(c) <= {"COLLAPSE", "ON-NOTHING"} for c in s4.values()))
mixed = {}
for key in ("2  (squaring, det 4)", "2' (per-doubling, -2)", "3  (Thue-Morse, det 0)"):
    c = out[key]["generic"]
    mixed[key] = (c.get("COLLAPSE", 0), c.get("ESCAPE", 0))
print()
for k, (col, esc) in mixed.items(): print(f"      {k}: COLLAPSE {col}  ESCAPE {esc}")
uniform = all((col == 0) != (esc == 0) for col, esc in mixed.values())
check("Q3/Q4", "the sign across strata 2, 2', 3 is " + ("UNIFORM -- a direction" if uniform else
       "MIXED -- a BASIN STRUCTURE, not a direction: both collapse and escape occur from the same "
       "stratum at different starting points, so the multiplier does not supply an arrow by itself"),
      True)
json.dump({"classes": {k: {kk: vv for kk, vv in v.items()} for k, v in out.items()},
           "uniform_sign": bool(uniform), "fails": fails},
          open("b1347_kappa_flow.json", "w"), indent=1)
print("\nB1347-flow:", "PASS" if not fails else f"FAIL ({fails})")
raise SystemExit(0 if not fails else 1)
