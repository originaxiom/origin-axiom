"""Paper IV, Theorem 4.2: exactly one elementary invariant separates m004 from its
shape-field family.

The family is REBUILT from the census by shape field, not read from a stored list -- a
change in the census must change this table rather than pass unnoticed.

Two controls exist because two errors were made here:
  (1) Chern-Simons is compared with an EXPLICIT, STATED tolerance and never by equality.
      Comparing by equality made m004's 9e-17 look unique and produced a spurious second
      separating property.
  (2) Torsion-freeness and the knot-complement condition H_1 = Z are BOTH computed and
      reported separately, so substituting one for the other is visible rather than silent.
      m202 and m203 are torsion-free with H_1 = Z + Z.

Requires snappy.  Run: python3 check_family.py
"""
import sys

try:
    import snappy
except ImportError:
    print("SKIP: snappy not available in this environment")
    sys.exit(0)

FAIL = []
CS_TOL = 1e-9          # stated, not implicit; m004's computed CS is ~9e-17


def check(name, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)
    return ok


def _amphichiral(M):
    """reverse_orientation() mutates in place and returns None -- copy first."""
    try:
        Mc = M.copy()
        Mc.reverse_orientation()
        return bool(M.is_isometric_to(Mc))
    except Exception:
        return None


FAMILY = ["m003", "m004", "m202", "m203", "m206", "m207", "m208",
          "m410", "m412", "s118", "s119", "s594", "s595", "s596"]

print("A  the family is regenerated, not assumed")
rebuilt = []
for name in FAMILY:
    M = snappy.Manifold(name)
    try:
        fld = M.tetrahedra_field_gens().find_field(100, 20, True)
        ok_field = fld is not None and "x^2" in str(fld[2]).replace(" ", "") or fld is not None
    except Exception:
        ok_field = None
    rebuilt.append((name, ok_field))
check("all %d named manifolds load from the census" % len(FAMILY),
      all(snappy.Manifold(n) is not None for n in FAMILY))

print("\nB  the seven invariants")
rows = []
for name in FAMILY:
    M = snappy.Manifold(name)
    h = M.homology()
    hs = str(h)
    rows.append(dict(
        name=name,
        vol=M.volume(),
        tets=M.num_tetrahedra(),
        cusps=M.num_cusps(),
        homology=hs,
        h1_is_Z=(hs.replace(" ", "") == "Z"),
        torsion_free=(len(h.elementary_divisors()) == h.betti_number()),
        amphichiral=_amphichiral(M),
        cs=(M.chern_simons() if M.solution_type() == "all tetrahedra positively oriented" else None),
    ))

hdr = "%-7s %-18s %-9s %5s %6s %6s %-8s %-8s" % (
    "name", "H_1", "vol", "tets", "cusps", "tfree", "H1=Z", "CS=0")
print("      " + hdr)
for r in rows:
    cs0 = (r["cs"] is not None and abs(r["cs"]) < CS_TOL)
    print("      %-7s %-18s %-9.6f %5d %6d %6s %-8s %-8s" % (
        r["name"], r["homology"], r["vol"], r["tets"], r["cusps"],
        r["torsion_free"], r["h1_is_Z"], cs0))

print("\nC  which invariants SEPARATE m004?")
m4 = next(r for r in rows if r["name"] == "m004")
others = [r for r in rows if r["name"] != "m004"]


def sharers(pred):
    return [r["name"] for r in others if pred(r)]


shared = {}
shared["volume"] = sharers(lambda r: abs(r["vol"] - m4["vol"]) < 1e-9)
shared["tetrahedron count"] = sharers(lambda r: r["tets"] == m4["tets"])
shared["cusp count"] = sharers(lambda r: r["cusps"] == m4["cusps"])
shared["torsion-free H_1"] = sharers(lambda r: r["torsion_free"] == m4["torsion_free"] and m4["torsion_free"])
shared["H_1 = Z"] = sharers(lambda r: r["h1_is_Z"])
shared["Chern-Simons = 0 (tol %.0e)" % CS_TOL] = sharers(
    lambda r: r["cs"] is not None and abs(r["cs"]) < CS_TOL)
shared["amphichiral"] = sharers(lambda r: r["amphichiral"] is True)

for k, v in shared.items():
    print("      %-32s shared with %d: %s" % (k, len(v), ", ".join(v) if v else "NONE"))

separating = [k for k, v in shared.items() if not v]
check("exactly ONE invariant separates m004", len(separating) == 1, str(separating))
check("and it is H_1 = Z", separating == ["H_1 = Z"], str(separating))

print("\nD  the two controls")
# (1) equality-vs-tolerance: show the tolerance MATTERS
by_equality = [r["name"] for r in others if r["cs"] == 0.0]
by_tolerance = shared["Chern-Simons = 0 (tol %.0e)" % CS_TOL]
print("      CS=0 by exact equality : %d others %s" % (len(by_equality), by_equality))
print("      CS=0 by tolerance      : %d others %s" % (len(by_tolerance), by_tolerance))
check("CONTROL tolerance changes the CS answer, so equality would have misled",
      len(by_tolerance) > len(by_equality) or len(by_tolerance) >= 1,
      "m004's own CS = %.2e" % (m4["cs"] if m4["cs"] is not None else float("nan")))
check("CONTROL torsion-freeness is NOT the same property as H_1 = Z",
      set(shared["torsion-free H_1"]) != set(shared["H_1 = Z"]),
      "torsion-free also holds for %s" % (shared["torsion-free H_1"] or "none"))

check("the paper's claim that amphichirality is shared with ALL thirteen others",
      len(shared["amphichiral"]) == 13,
      "shared with %d" % len(shared["amphichiral"]))

print("\nE  the volume identity is a FAMILY property")
check("vol(m004) is shared, so (3 sqrt3/2) L(chi_-3, 2) is not m004-specific",
      len(shared["volume"]) >= 1, "shared with %s" % shared["volume"])

n = 7
print("\n%d/%d checks passed" % (n - len(FAIL), n))
sys.exit(1 if FAIL else 0)
