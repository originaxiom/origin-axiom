#!/usr/bin/env python3
"""INDEPENDENT verification of cc3's B8128 (genericity control): of 7 elementary properties,
exactly one separates m004 from its shape-field family (Q(sqrt-3)) -- H_1 = Z. Own scan, own
property table, own SnapPy calls (not cc3's wins.py). Gate 5 untouched (pure topology)."""
import snappy
from fractions import Fraction

EXPECTED = {"m003","m004","m202","m203","m206","m207","m208","m410","m412","s118","s119","s594","s595","s596"}


def quad_disc(z, maxden=64, tol=1e-9):
    b = Fraction(-2 * z.real).limit_denominator(maxden)
    c = Fraction(abs(z) ** 2).limit_denominator(maxden)
    if abs(float(b) + 2 * z.real) > tol or abs(float(c) - abs(z) ** 2) > tol:
        return None
    d = b * b - 4 * c
    if d >= 0:
        return None
    n = d.numerator * d.denominator
    for s in range(2, 60):
        while n % (s * s) == 0:
            n //= s * s
    return n


# --- SECTION 1: independent family rebuild (shape field = Q(sqrt-3)) ---
fam = []
for i, N in enumerate(snappy.OrientableCuspedCensus()):
    if i > 1200:
        break
    try:
        sh = [complex(z) for z in N.tetrahedra_shapes("rect")]
    except Exception:
        continue
    if {quad_disc(z) for z in sh} == {-3}:
        fam.append(N.name())
print("family size:", len(fam))
print("family:", sorted(fam))
print("matches cc3's stated 14:", set(fam) == EXPECTED)


def amphichiral(M):
    Mr = M.copy()
    Mr.reverse_orientation()
    try:
        r = M.is_isometric_to(Mr)
        return bool(r)
    except Exception:
        try:
            return M.isometry_signature() == Mr.isometry_signature()
        except Exception:
            return None


# --- SECTION 2: independent property table over cc3's stated family ---
rows = {}
for nm in sorted(EXPECTED):
    M = snappy.Manifold(nm)
    h = str(M.homology())
    try:
        cs = float(M.chern_simons())
    except Exception:
        cs = None
    rows[nm] = {
        "homology": h,
        "h1_is_Z": (h == "Z"),
        "vol": float(M.volume()),
        "tets": M.num_tetrahedra(),
        "cusps": M.num_cusps(),
        "cs": cs,
        "cs_is_zero": (cs is not None and abs(cs) < 1e-9),
        "torsion_free": ("/" not in h),
        "amphichiral": amphichiral(M),
    }

# --- SECTION 3: the separator analysis (which of 7 props is m004's value unique on?) ---
props = ["h1_is_Z", "vol", "tets", "cusps", "torsion_free", "amphichiral", "cs_is_zero"]
separators = []
for p in props:
    m004v = rows["m004"][p]
    others = [rows[nm][p] for nm in rows if nm != "m004"]
    if p == "vol":
        unique = all(abs(m004v - o) > 1e-9 for o in others)
    else:
        unique = all(m004v != o for o in others)
    if unique:
        separators.append(p)

print()
print("H1=Z members (expect [m004] only):", sorted(nm for nm, r in rows.items() if r["h1_is_Z"]))
print("m004 vol == m003 vol:", abs(rows["m004"]["vol"] - rows["m003"]["vol"]) < 1e-9,
      f"({rows['m004']['vol']:.15f})")
print("all 14 amphichiral:", all(r["amphichiral"] is True for r in rows.values()))
print("CS=0 members (shared subset):", sorted(nm for nm, r in rows.items() if r["cs_is_zero"]))
print("torsion-free members (shared):", sorted(nm for nm, r in rows.items() if r["torsion_free"]))
print()
print(">>> SEPARATORS (m004 unique across the family):", separators)
print(">>> VERDICT:", "CONFIRMED -- exactly one separator, H_1=Z" if separators == ["h1_is_Z"]
      else f"MISMATCH -- got {separators}")

# --- SECTION 4: the two bugs cc3 caught, independently reproduced ---
print()
print("BUG 1 (CS float-equality): m004 CS =", rows["m004"]["cs"], "vs m203 CS =", rows["m203"]["cs"])
print("  -> raw float-equality would wrongly separate m004; under tol both are 0 (shared):",
      rows["m004"]["cs_is_zero"] and rows["m203"]["cs_is_zero"])
print("BUG 2 (torsion-free != H1=Z): m202 torsion-free?", rows["m202"]["torsion_free"],
      "but H1=Z?", rows["m202"]["h1_is_Z"], f"(homology {rows['m202']['homology']})")
print("  -> torsion-freeness does NOT separate m004 (m202/m203 also torsion-free); only H1=Z does.")


# --- results dump (banking-seat lock input, B1136) ---
import json as _json, os as _os
_out = {
    "family": sorted(fam),
    "family_size": len(fam),
    "matches_cc3_14": set(fam) == EXPECTED,
    "separators": separators,
    "unique_separator_is_h1_Z": (separators == ["h1_is_Z"]),
    "h1_Z_members": sorted(nm for nm, r in rows.items() if r["h1_is_Z"]),
    "vol_m004_eq_m003": abs(rows["m004"]["vol"] - rows["m003"]["vol"]) < 1e-9,
    "vol_shared": rows["m004"]["vol"],
    "all_amphichiral": all(r["amphichiral"] is True for r in rows.values()),
    "cs_zero_members": sorted(nm for nm, r in rows.items() if r["cs_is_zero"]),
    "torsion_free_members": sorted(nm for nm, r in rows.items() if r["torsion_free"]),
}
with open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "b1136_results.json"), "w") as _f:
    _json.dump(_out, _f, indent=2)
print("results dumped to b1136_results.json")
