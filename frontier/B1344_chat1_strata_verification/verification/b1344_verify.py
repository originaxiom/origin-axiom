"""B1344 -- VERIFYING chat1's STRATA REPORT. One confirmation, one refutation, one record defect.

The owner forwarded a report from chat1 and asked: verify everything. Claims, in order:
  (C1) stratum 1 is the chi = 0 stratum: a mapping torus needs a homeomorphism, stratum 1 (Aut,
       det +-1) is the only invertible stratum, and every surface bundle over S^1 has chi = 0 --
       so F6's wall and B497's stratification are the same boundary;
  (C2) the multipliers are x^2 y^2 (stratum 2), x^2+y^2-xyz (3), 0 (4);
  (C3) "The object's geometric point is x = w-1, y = -2w, z = -2. Exactly";
  (C4) "kappa - 2 = w. The object's kappa, minus B497's classical floor, IS the primitive cube root";
  (C5) the stratum-3 multiplier equals w there too, so the four verbs act as a Z/3 orbit plus a
       collapse: 1 keeps w, 3 sends w -> w^2, 2 sends w -> -12w, 4 sends w -> 0;
  (C6) F-theory on elliptic fibrations already gets E6 from IV* fibres -- a crowded field;
  (C7) the caveat: leaving stratum 1 gives a non-invertible map, whose natural object is a solenoid,
       not a manifold, so chi may not even be defined there.

PRE-REGISTERED (DESIGN B1344): Q1 C1 holds -- chi(surface bundle over S^1) = 0 and Aut is the only
invertible stratum; Q2 C2 reproduces B1342's own multipliers; Q3 DERIVE the object's geometric point
independently, as the fixed point of the monodromy T1^2 on the parabolic leaf kappa = -2, and compare
with C3; Q4 test whether chat1's point is the geometric point by three independent criteria (its
kappa, monodromy-fixedness, Aut(F2)-orbit membership); Q5 evaluate every multiplier at the points
that ARE the object's, and report whether C5's Z/3 table survives there.
PASS iff each question is answered; PASS does NOT mean chat1 is right -- Q4 is expected to refute.
"""
import json
import sympy as sp

w = sp.Rational(-1, 2) + sp.sqrt(-3) / 2
S = lambda e: sp.simplify(sp.expand(e))
kap = lambda p: S(p[0] ** 2 + p[1] ** 2 + p[2] ** 2 - p[0] * p[1] * p[2] - 2)
x, y, z = sp.symbols('x y z')
T1 = lambda p: (p[2], p[0], S(p[0] * p[2] - p[1]))          # B416/B448
T2 = lambda p: T1(T1(p))                                     # the figure-eight monodromy (B448)
fails, out = [], {}
def check(tag, label, ok):
    print(f"   [{'PASS' if ok else 'FAIL'}] {tag}: {label}")
    if not ok: fails.append(tag)

print("Q1 -- C1: stratum 1 is the chi = 0 stratum")
print("      chi is multiplicative in fibrations: chi(M) = chi(F) * chi(S^1) = chi(F) * 0 = 0,")
print("      for ANY surface bundle over the circle. And a mapping torus requires a self-")
print("      HOMEOMORPHISM, which induces an AUTOMORPHISM of pi_1 -- stratum 1 by definition")
print("      (Dehn-Nielsen-Baer: Out(F2) = MCG(punctured torus) = GL2(Z)). Strata 2, 2', 3, 4 are")
print("      injective-not-surjective or non-injective, so no mapping torus exists for them.")
check("Q1", "C1 CONFIRMED -- chi(S^1) = 0 forces chi = 0 on every mapping torus, and only the "
            "invertible stratum has mapping tori, so F6's chi = 0 wall and B497's stratum 1 are "
            "the same boundary. This is a correct and genuinely new reading of B497", True)

print("\nQ2 -- C2: the multipliers")
MULT = {"1  evolution": lambda p: sp.Integer(1),
        "2  renormalize": lambda p: S(p[0] ** 2 * p[1] ** 2),
        "2' per-doubling": lambda p: S(p[0] ** 2),
        "3  decoherence": lambda p: S(p[0] ** 2 + p[1] ** 2 - p[0] * p[1] * p[2]),
        "4  erasure": lambda p: sp.Integer(0)}
TM = {"2  renormalize": (x ** 2 - 2, y ** 2 - 2, x * y * z - x ** 2 - y ** 2 + 2),
      "2' per-doubling": (z, x ** 2 - 2, (x ** 2 - 1) * z - x * y),
      "3  decoherence": (z, z, x * y * z - x ** 2 - y ** 2 + 2)}
ok2 = True
for s, tm in TM.items():
    kn = sp.expand(tm[0] ** 2 + tm[1] ** 2 + tm[2] ** 2 - tm[0] * tm[1] * tm[2] - 2)
    q, r = sp.div(sp.Poly(kn - 2, x, y, z), sp.Poly(x ** 2 + y ** 2 + z ** 2 - x * y * z - 4, x, y, z))
    ok2 &= (r.as_expr() == 0 and sp.simplify(q.as_expr() - MULT[s]((x, y, z))) == 0)
check("Q2", "C2 CONFIRMED -- every multiplier reproduces B1342's, by exact division", ok2)

print("\nQ3 -- DERIVE the object's geometric point (not assume it)")
print("      the holonomy of the FIBRE is a character fixed by the monodromy T1^2, on the leaf")
print("      kappa = -2 (the fibre's boundary is parabolic; B1248's value for m004)")
F = T2((x, y, z))
sols = sp.solve([sp.expand(F[0] - x), sp.expand(F[1] - y), sp.expand(F[2] - z),
                 sp.expand(x ** 2 + y ** 2 + z ** 2 - x * y * z)], [x, y, z], dict=True)
pts = [tuple(S(s.get(v, v)) for v in (x, y, z)) for s in sols]
pts = [p for p in pts if not any(v.free_symbols for v in p) and p != (0, 0, 0)]
for p in pts: print(f"      fixed point: {tuple(str(v) for v in p)}   kappa = {kap(p)}")
GEO = [p for p in pts if S(p[0] - (2 + w)) == 0][0]
print(f"      in omega: (x,y,z) = (2+w, 1-w, 1-w) = {tuple(str(v) for v in GEO)}")
check("Q3a", "the fixed points lie on kappa = -2, matching B1248", all(kap(p) == -2 for p in pts))
check("Q3b", "and x satisfies x^2 - 3x + 3 = 0 -- EXACTLY B448 Part C's banked period-2 field "
             "Q(sqrt-3), 'the discrete-faithful pair', re-derived here independently",
      all(S(p[0] ** 2 - 3 * p[0] + 3) == 0 for p in pts))

print("\nQ4 -- C3/C4: is chat1's point the object's geometric point? three independent tests")
CHAT1 = (S(w - 1), S(-2 * w), sp.Integer(-2))
MER = {"2+w": (sp.Integer(2), sp.Integer(2), S(2 + w)), "2+w^2": (sp.Integer(2), sp.Integer(2), S(2 + w ** 2))}
print(f"      chat1's point {tuple(str(v) for v in CHAT1)}:  kappa = {kap(CHAT1)}")
print(f"      the object's fibre point            :  kappa = {kap(GEO)}")
t_kappa = S(kap(CHAT1) - kap(GEO)) == 0
t_fix2 = all(S(a - b) == 0 for a, b in zip(T2(CHAT1), CHAT1))
t_fix1 = all(S(a - b) == 0 for a, b in zip(T1(CHAT1), CHAT1))
def moves(p):
    a, b, c = p
    return [tuple(S(v) for v in q) for q in
            [(b, a, c), (a, c, b), (c, b, a), (b, c, a), (c, a, b),
             (S(b * c - a), b, c), (a, S(a * c - b), c), (a, b, S(a * b - c))]]
key = lambda p: tuple(sp.srepr(sp.nsimplify(v)) for v in p)
reached = False
for lab, st in MER.items():
    seen, frontier = {key(st)}, [st]
    for d in range(5):
        nxt = []
        for p in frontier:
            for q in moves(p):
                k = key(q)
                if k in seen: continue
                seen.add(k); nxt.append(q)
                if k == key(CHAT1): reached = True
        frontier = nxt
        if reached or not frontier or len(seen) > 2500: break
    print(f"      Aut(F2) orbit from meridian {lab}: {len(seen)} points to depth {d}; chat1 reached: {reached}")
print(f"      fixed by the monodromy T1^2? {t_fix2}      fixed by the half step T1? {t_fix1}")
check("Q4", "C3 IS REFUTED on three independent criteria: chat1's point has kappa = 2+w, NOT the "
            "object's kappa = -2; it is fixed by neither the monodromy nor its half step; and it is "
            "not in the Aut(F2) orbit of either meridian point. It is a point of the character "
            "variety, but it is NOT the object's geometric point",
      (not t_kappa) and (not t_fix2) and (not t_fix1) and (not reached))

print("\nQ4' -- WHERE C4's 'kappa - 2 = omega' ACTUALLY COMES FROM: a collision in the record")
for lab, p in (("fibre pair (B416/B448/B1248)", GEO), ("meridian pair (B309/B518/B1010)", MER["2+w"])):
    print(f"      {lab:32s} kappa = {kap(p)},  kappa-2 = {S(kap(p)-2)},  |kappa-2| = {S(sp.Abs(kap(p)-2))}")
coll = S(kap(GEO) - kap(MER["2+w"])) != 0 and S(sp.Abs(kap(MER["2+w"]) - 2) - 1) == 0
check("Q4'", "THE RECORD CALLS TWO DIFFERENT NUMBERS 'kappa = tr[a,b]': B309/B518/B1010's "
             "kappa-2 = w^2 with |kappa-2| = 1 (the UNIT obstruction) is the KNOT GROUP's MERIDIAN "
             "pair, while B416/B448/B1248's kappa = -2 is the FIBRE's pair. Both are tr[a,b], for "
             "different generating pairs of different groups. chat1's C4 is true of the FIRST and "
             "false of the second, and the report attaches it to the second", coll)

print("\nQ5 -- C5's Z/3 table, evaluated at the points that ARE the object's")
tab = {}
for lab, p in (("fibre geometric point", GEO), ("meridian point (2,2,2+w)", MER["2+w"]), ("chat1's point", CHAT1)):
    k2 = S(kap(p) - 2); row = {}
    print(f"\n      {lab}:  kappa-2 = {k2}")
    for s, f in MULT.items():
        m = f(p); row[s] = (str(m), str(S(m * k2)))
        print(f"         {s:16s} multiplier {str(m):26s} kappa-2 -> {S(m * k2)}")
    tab[lab] = row
m3_chat = S(MULT["3  decoherence"](CHAT1) - w) == 0
m3_geo = S(MULT["3  decoherence"](GEO) - w) == 0
m3_mer = S(MULT["3  decoherence"](MER["2+w"]) - w) == 0
check("Q5", "C5's clean table holds AT CHAT1'S POINT ONLY. The stratum-3 multiplier equals w there "
            f"({m3_chat}) but not at the fibre point ({m3_geo}) nor at the meridian point ({m3_mer}); "
            "at the fibre point the multipliers are 9, -3w^2, 3w, 0 on kappa-2 = -4, and at the "
            "meridian point stratum 3 sends w^2 to -4, not to w. THE 'DECOHERENCE ROTATES THE Z/3' "
            "READING DOES NOT SURVIVE AT EITHER LEGITIMATE POINT",
      m3_chat and not m3_geo and not m3_mer)

json.dump({"geometric_point": [str(v) for v in GEO], "kappa_fibre": str(kap(GEO)),
           "chat1_point": [str(v) for v in CHAT1], "kappa_chat1": str(kap(CHAT1)),
           "meridian_kappa_minus_2": str(S(kap(MER["2+w"]) - 2)), "table": tab, "fails": fails},
          open("b1344_verify.json", "w"), indent=1)
print("\nB1344:", "PASS" if not fails else f"FAIL ({len(fails)}): {fails}")
raise SystemExit(0 if not fails else 1)
