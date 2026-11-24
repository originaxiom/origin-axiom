"""B1977 (main, 2026-11-24; data-free): rates of the masses and the mixing at B1976's 96 order-30 points, heights 20 and 30.
    python3 -B rates30.py > rates30_run.txt"""
import sys, pathlib, json
from fractions import Fraction as Fr
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1976_*")) / "verification"))
import level30 as L
mp = L.mp
def snap(a, b, y):
    o = {}
    for s in ("up", "down", "lep"):
        Y = L.DL.parts("0.13", y, a, b, s)[2]["S"]; o[s] = Y
    o["sv"] = {s: sorted(abs(x) for x in mp.svd_c(o[s], compute_uv=False)) for s in ("up", "down", "lep")}
    o["V"] = L.CM.U_of(o["up"]).H * L.CM.U_of(o["down"]); return o
def rate(x1, x2): return float(-(mp.log(abs(x2)) - mp.log(abs(x1))) / (mp.pi * 10))
SLOW = {("4/15", "1/30"), ("4/15", "11/30"), ("4/15", "7/10"), ("11/15", "3/10"), ("11/15", "19/30")}
rows = []
for (a, b) in L.P30:
    A, B = snap(a, b, 20.0), snap(a, b, 30.0)
    r = dict(a=str(a), b=str(b))
    for s in ("up", "down", "lep"):
        r[s + "_m2m3"] = rate(A["sv"][s][1] / A["sv"][s][2], B["sv"][s][1] / B["sv"][s][2])
        r[s + "_m1m3"] = rate(A["sv"][s][0] / A["sv"][s][2], B["sv"][s][0] / B["sv"][s][2])
    for (i, j, n) in ((0, 1, "V12"), (1, 2, "V23"), (0, 2, "V13")):
        r[n] = rate(A["V"][i, j], B["V"][i, j]) if abs(B["V"][i, j]) > 0 and abs(A["V"][i, j]) > 0 else None
    r["diag"] = float(min(abs(B["V"][k, k]) for k in range(3))); r["off"] = float(max(abs(B["V"][i, j]) for i in range(3) for j in range(3) if i != j))
    rows.append(r)
    print("(%s, %s)%s up %.3f %.3f | down %.3f %.3f | lep %.3f %.3f | V12 %s V23 %s V13 %s | diag %.4f off %.1e" % (
        a, b, " *" if (str(a), str(b)) in SLOW else "", r["up_m2m3"], r["up_m1m3"], r["down_m2m3"], r["down_m1m3"], r["lep_m2m3"], r["lep_m1m3"],
        *("%.3f" % r[n] if r[n] is not None else "-" for n in ("V12", "V23", "V13")), r["diag"], r["off"]), flush=True)
json.dump(rows, open(pathlib.Path(__file__).with_name("rates30_run.json"), "w"), indent=1)
slow = [r for r in rows if (r["a"], r["b"]) in SLOW]
hier = lambda r: r["up_m2m3"] >= 0.1 and r["up_m1m3"] >= 0.2 and r["down_m2m3"] >= 0.1 and r["down_m1m3"] >= 0.2
print("SUMMARY G1: slow points with a hierarchy in both quark sectors: %d of %d" % (sum(hier(r) for r in slow), len(slow)))
print("SUMMARY G2: slow points with V23's rate within 2e-3 of 1/30: %d of %d (rates %s)" % (sum(r["V23"] is not None and abs(r["V23"] - 1 / 30) < 2e-3 for r in slow), len(slow), [round(r["V23"], 4) for r in slow if r["V23"] is not None]))
allr = [v for r in rows for k, v in r.items() if k not in ("a", "b", "diag", "off") and v is not None]
off = [v for v in allr if abs(v * 60 - round(v * 60)) / 60 > 3e-3]
print("SUMMARY G3: rates within 3e-3 of a multiple of 1/60: %d of %d (worst offenders %s)" % (len(allr) - len(off), len(allr), sorted(off, key=lambda v: -abs(v * 60 - round(v * 60)))[:6]))
print("SUMMARY G4: slow points with lepton m2/m3 rate differing from down's by more than 1e-2: %d of %d" % (sum(abs(r["lep_m2m3"] - r["down_m2m3"]) > 1e-2 for r in slow), len(slow)))
g5 = [r for r in rows if r["diag"] >= 0.9 and hier(r) and min(v for v in (r["V12"], r["V23"], r["V13"]) if v is not None) < 0.1]
print("SUMMARY G5: points aligned, hierarchical in both quark sectors, and with a mixing rate below 1/10: %d (%s)" % (len(g5), [(r["a"], r["b"]) for r in g5][:8]))
