"""B1399 design time: pin the census. For B1186's 99 arithmetic members and their connected covers of degree 2 and 3 (SnapPy's
covers()), keep those with cuspidal dimension b1 - #cusps >= 2; record each one's isometry signature (canonical) and parentage;
remove isometric duplicates. Homology and canonical triangulations only: no harmonic form, no count."""
import json, sys, time, warnings
from pathlib import Path
warnings.filterwarnings("ignore")
import snappy
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1394_the_regular_three" / "verification"))
OUT = sys.argv[1] if len(sys.argv) > 1 else str(HERE / "census_list.json")
import regular_three as R3
t0 = time.time()
rows = []
for n in R3.census_members():
    M = snappy.Manifold(n)
    for deg in (2, 3):
        for i, C in enumerate(M.covers(deg)):
            H = C.homology()
            b1 = sum(1 for e in H.elementary_divisors() if e == 0)
            d = b1 - C.num_cusps()
            if d < 2:
                continue
            try:
                sig = C.isometry_signature()
            except Exception as e:
                sig = None
            rows.append(dict(parent=n, degree=deg, index=i, cuspidal_dim=d, b1=b1, cusps=C.num_cusps(),
                             tets=C.num_tetrahedra(), homology=str(H), isometry_signature=sig,
                             triangulation_isosig=C.triangulation_isosig()))
seen, census = {}, []
for r in rows:
    key = r["isometry_signature"] or ("tri:" + r["triangulation_isosig"])
    if key in seen:
        seen[key]["also_from"].append((r["parent"], r["degree"], r["index"]))
        continue
    r["also_from"] = []
    seen[key] = r
    census.append(r)
from collections import Counter
print("eligible covers:", len(rows), "; distinct up to isometry:", len(census), "; without an isometry signature:",
      sum(1 for r in census if r["isometry_signature"] is None), "; seconds", round(time.time() - t0))
print("distinct by (degree, cuspidal dim):", sorted(Counter((r["degree"], r["cuspidal_dim"]) for r in census).items()))
print("tetrahedra:", min(r["tets"] for r in census), "-", max(r["tets"] for r in census), "; cusps:", sorted(Counter(r["cusps"] for r in census).items()))
json.dump(dict(note="B1399 design-time census: homology and isometry signatures only", census=census),
          open(OUT, "w"), indent=1)
