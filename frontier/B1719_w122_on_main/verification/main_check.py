"""B1719 (P-269): main's own check of W122's two claims (independent of the seat's script): the least certified Dehn fillings of
b+-LR (m003) and b++LR (m004) over primitive slopes |p|, q <= 7 are the Weeks manifold and the Meyerhoff manifold, by
isometry (not volume alone), and Weeks comes from -LR only."""
import math, snappy, json
WEEKS, MEYER = snappy.Manifold("m003(-3,1)"), snappy.Manifold("m004(5,1)")
out = {}
for name in ("b+-LR", "b++LR"):
    rows = []
    for q in range(0, 8):
        for p in range(-7, 8):
            if (q == 0 and p != 1) or math.gcd(p, q) != 1 or (q == 0 and p == 0): continue
            M = snappy.Manifold(name); M.dehn_fill((p, q))
            if M.solution_type() != "all tetrahedra positively oriented": continue
            v = float(M.volume()); rows.append((v, p, q))
    rows.sort()
    best = []
    for v, p, q in rows[:4]:
        M = snappy.Manifold(name); M.dehn_fill((p, q)); F = snappy.Manifold(M.filled_triangulation())
        iso = "Weeks" if abs(v - float(WEEKS.volume())) < 1e-9 and F.is_isometric_to(WEEKS) else ("Meyerhoff" if abs(v - float(MEYER.volume())) < 1e-9 and F.is_isometric_to(MEYER) else "")
        best.append({"vol": round(v, 10), "slope": [p, q], "is": iso})
    out[name] = {"certified": len(rows), "least_four": best}
import pathlib, sys
if "--check" not in sys.argv:
    json.dump(out, open(pathlib.Path(__file__).resolve().parent / "main_check.json", "w"), indent=1)
print(json.dumps(out, indent=1))
