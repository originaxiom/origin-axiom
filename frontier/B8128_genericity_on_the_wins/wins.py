#!/usr/bin/env python3
"""B8128 -- THE GENERICITY CONTROL, TURNED ON THE OBJECT'S OWN SUCCESSES.

Owner-elected. Every closure of the last two days came from one instrument: vary the thing that
should not matter and see whether the result survives.  B8111 varied the group, B8117 the
substrate, B8118 the manifold, B8125 compactness.  IT HAS NEVER BEEN AIMED AT THE WINS.

B8118 found, while checking something else, that 14 census manifolds share m004's shape field --
so the E6 that arrives arithmetically through that field is the CLASS's, not m004's.  This asks
the same question of every property the corpus treats as the object's own.

THE TEST: for each banked property, does it hold for the other members of the shape-field family?
A property shared by all of them is a property of the FAMILY.  Only the properties that SEPARATE
m004 are the object's.

QUANTIFIER: the orientable cusped census manifolds whose tetrahedron shape field is Q(sqrt-3),
and elementary invariants of each.  Gate 5 untouched; no measured value.
"""
import json, math, os
from fractions import Fraction
import snappy

HERE = os.path.dirname(os.path.abspath(__file__))
FAILED = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAILED.append(l)

def rat(x, maxden=64, tol=1e-9):
    f = Fraction(x).limit_denominator(maxden)
    return f if abs(float(f) - x) < tol else None

def quad_disc(z):
    b, c = rat(-2 * z.real), rat(abs(z) ** 2)
    if b is None or c is None: return None
    d = b * b - 4 * c
    if d >= 0: return None
    n = d.numerator * d.denominator
    for s in range(2, 60):
        while n % (s * s) == 0: n //= s * s
    return n

print("=" * 78); print("SECTION 1 -- THE SHAPE-FIELD FAMILY (B8118's 14, rebuilt)"); print("=" * 78)
fam = []
for i, N in enumerate(snappy.OrientableCuspedCensus()):
    if i > 1200: break
    try: sh = [complex(z) for z in N.tetrahedra_shapes("rect")]
    except Exception: continue
    if {quad_disc(z) for z in sh} == {-3}: fam.append(N.name())
print(f"  family size: {len(fam)}")
print(f"  members: {fam}")
gate("m004 is in the family", "m004" in fam)
gate("the family is B8118's 14", len(fam) == 14, str(len(fam)))

print(); print("=" * 78); print("SECTION 2 -- THE PROPERTY TABLE"); print("=" * 78)
rows = []
for nm in fam:
    N = snappy.Manifold(nm)
    h = N.homology()
    hs = str(h)
    torsion_free = ("/" not in hs)          # Z^k with no Z/n summands
    try: cs = float(N.chern_simons())
    except Exception: cs = None
    # amphichiral: isometric to its own mirror image
    try:
        M2 = snappy.Manifold(nm); M2.reverse_orientation()
        amph = bool(N.is_isometric_to(M2))
    except Exception:
        amph = None
    rows.append(dict(name=nm, vol=float(N.volume()), tets=N.num_tetrahedra(),
                     cusps=N.num_cusps(), homology=hs, torsion_free=torsion_free,
                     h1_is_Z=(hs.replace(" ", "") == "Z"),
                     cs=cs, cs_is_zero=(cs is not None and abs(cs) < 1e-9),
                     amphichiral=amph))
print(f"  {'name':>7} {'vol':>12} {'tet':>4} {'cusp':>5}  {'H_1':<18} {'tor-free':>9} {'CS':>10} {'amph':>6}")
for r in rows:
    print(f"  {r['name']:>7} {r['vol']:12.9f} {r['tets']:4d} {r['cusps']:5d}  {r['homology']:<18} "
          f"{str(r['torsion_free']):>9} {('%.6f'%r['cs']) if r['cs'] is not None else 'n/a':>10} {str(r['amphichiral']):>6}")

print(); print("=" * 78); print("SECTION 3 -- WHICH PROPERTIES SEPARATE m004?"); print("=" * 78)
me = next(r for r in rows if r["name"] == "m004")
sep, shared = [], []
# NOTE, and both of these were caught by re-reading the first run's own table:
#  (1) comparing cs by float EQUALITY made m004's 9e-17 differ from other members' 0.0, so the
#      one property that "separated" did so only through floating point. Compare cs_is_zero.
#  (2) torsion-freeness is not the knot-complement condition; H_1 = Z EXACTLY is. m202/m203 are
#      torsion-free with H_1 = Z+Z. Test the full homology.
for key, label in (("vol","volume"), ("tets","tetrahedron count"), ("cusps","cusp count"),
                   ("torsion_free","torsion-free H_1"), ("h1_is_Z","H_1 = Z exactly"),
                   ("amphichiral","amphichirality"), ("cs_is_zero","Chern-Simons = 0")):
    same = [r["name"] for r in rows if r["name"] != "m004" and r[key] == me[key]]
    (shared if same else sep).append((label, me[key], same))
    verdict = "SEPARATES" if not same else f"shared with {len(same)}: {same[:5]}{'...' if len(same)>5 else ''}"
    print(f"  {label:<20} m004 = {str(me[key]):<22} {verdict}")

print()
gate("at least one property SEPARATES m004 from the family", len(sep) > 0,
     f"{len(sep)} separating, {len(shared)} shared")
gate("the shape field itself does NOT separate (it defines the family)", True)

print(); print("=" * 78); print("THE READING"); print("=" * 78)
print(f"""
  SHARED with other members -> a property of the FAMILY, not of m004:
    {[s[0] for s in shared]}
  SEPARATES m004 -> genuinely the object's:
    {[s[0] for s in sep]}

  Anything the corpus derives from a SHARED property is a statement about the
  shape-field family. Anything it derives from a SEPARATING property is about m004.
""")

RES = {"family": fam, "family_size": len(fam), "rows": rows,
       "separating": [{"property": a, "m004": str(b)} for a, b, _ in sep],
       "shared": [{"property": a, "m004": str(b), "shared_with": c} for a, b, c in shared],
       "method": "vary the manifold within the shape field; a property shared by other members is the family's",
       "scope": ("Elementary invariants of the 14 orientable cusped census manifolds whose "
                 "tetrahedron shape field is Q(sqrt-3). Tests which properties SEPARATE m004. Does "
                 "NOT test every banked result -- it tests the invariants those results rest on. "
                 "Gate 5 untouched.")}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True, default=str)
print("  results.json written")
if FAILED: raise SystemExit(f"\nCONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
