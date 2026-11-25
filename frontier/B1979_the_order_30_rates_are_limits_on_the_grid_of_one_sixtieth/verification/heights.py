"""B1979 (main, 2026-11-24/25; data-free): B1977's 96 order-30 points, the rates of the masses and the mixing read on three
intervals of height (20-30, 30-40, 40-50) at B1977's column 0.13, and on 30-40 at a second column 0.31. Main's own run of
the web seat's CHK-1 (its R1 to R5), extended by one interval; then the rate classes recounted from the converged rates.
The points are read from B1977's committed json; the frame is B1945's determinant_law.parts, as in B1977.
    python3 -B heights.py > heights_run.txt"""
import sys, pathlib, json, time
from fractions import Fraction as Fr
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
mp = DL.mp
B1977 = json.loads((next((ROOT / "frontier").glob("B1977_*")) / "verification" / "rates30_run.json").read_text())
K = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")
def snap(x, a, b, y):
    o = {s: DL.parts(x, y, a, b, s)[2]["S"] for s in ("up", "down", "lep")}
    sv = {s: sorted(abs(v) for v in mp.svd_c(o[s], compute_uv=False)) for s in ("up", "down", "lep")}
    V = CM.U_of(o["up"]).H * CM.U_of(o["down"])
    q = {}
    for s in ("up", "down", "lep"):
        q[s + "_m2m3"] = sv[s][1] / sv[s][2]; q[s + "_m1m3"] = sv[s][0] / sv[s][2]
    for (i, j, n) in ((0, 1, "V12"), (1, 2, "V23"), (0, 2, "V13")): q[n] = abs(V[i, j])
    q["diag"] = min(abs(V[k, k]) for k in range(3)); return q
def rates(A, B, dy):
    return {k: (float(-(mp.log(B[k]) - mp.log(A[k])) / (mp.pi * dy)) if A[k] > 0 and B[k] > 0 else None) for k in K}
t0 = time.time(); rows = []
for r0 in B1977:
    a, b = Fr(r0["a"]), Fr(r0["b"])
    S = {y: snap("0.13", a, b, y) for y in (20.0, 30.0, 40.0, 50.0)}
    T = {y: snap("0.31", a, b, y) for y in (30.0, 40.0)}
    rows.append(dict(a=r0["a"], b=r0["b"], r2030=rates(S[20.0], S[30.0], 10), r3040=rates(S[30.0], S[40.0], 10), r4050=rates(S[40.0], S[50.0], 10),
                     r3040x=rates(T[30.0], T[40.0], 10), diag40=float(S[40.0]["diag"]), diag50=float(S[50.0]["diag"])))
print("computed %d points  [%.0f s]" % (len(rows), time.time() - t0))
json.dump(rows, open(pathlib.Path(__file__).with_name("heights_run.json"), "w"), indent=1)
def vals(key): return [(r, k, r[key][k]) for r in rows for k in K if r[key][k] is not None]
# R1: reproduction of B1977
by = {(r["a"], r["b"]): r for r in B1977}
d = max(abs(r["r2030"][k] - by[(r["a"], r["b"])][k]) for r in rows for k in K if r["r2030"][k] is not None)
print("R1 (20-30 at 0.13 reproduces B1977's json): largest difference %.1e over %d rates" % (d, len(vals("r2030"))))
def res(v): return abs(v * 60 - round(v * 60)) / 60
for key, name in (("r2030", "20-30 at 0.13"), ("r3040", "30-40 at 0.13"), ("r4050", "40-50 at 0.13"), ("r3040x", "30-40 at 0.31")):
    v = [x for (_, _, x) in vals(key)]; rs = sorted(res(x) for x in v)
    print("grid of 1/60, %s: %d rates; largest residual %.1e; median %.1e; within 3e-3: %d; within 1e-3: %d" % (name, len(v), rs[-1], rs[len(rs) // 2], sum(x <= 3e-3 for x in rs), sum(x <= 1e-3 for x in rs)))
def drift(k1, k2):
    return max(abs(r[k1][k] - r[k2][k]) for r in rows for k in K if r[k1][k] is not None and r[k2][k] is not None)
print("drift: 20-30 to 30-40 %.1e; 30-40 to 40-50 %.1e; column 0.13 to 0.31 on 30-40 %.1e" % (drift("r2030", "r3040"), drift("r3040", "r4050"), drift("r3040", "r3040x")))
slow = [r for r in rows if abs(r["r2030"]["V23"] - 1 / 30) < 3e-3]
print("slow points (V23 near 1/30 on 20-30): %d; V23 on 20-30, 30-40, 40-50: %s" % (len(slow), sorted({(round(r["r2030"]["V23"], 5), round(r["r3040"]["V23"], 5), round(r["r4050"]["V23"], 5)) for r in slow})))
print("aligned (least diagonal >= 0.9) at height 40: %d of 96; at 50: %d of 96" % (sum(r["diag40"] >= 0.9 for r in rows), sum(r["diag50"] >= 0.9 for r in rows)))
# classes: from B1977's 3-decimal key, a 2-decimal key, and the rates snapped to the grid of 1/60 (40-50)
def key3(r, f): return tuple(None if r[f][k] is None else round(r[f][k], 3) for k in K)
def key2(r, f): return tuple(None if r[f][k] is None else round(r[f][k], 2) for k in K)
def keyg(r, f): return tuple(None if r[f][k] is None else Fr(round(r[f][k] * 60), 60) for k in K)
offg = [(r["a"], r["b"], k, x) for (r, k, x) in vals("r4050") if res(x) > 1e-3]
print("rates on 40-50 farther than 1e-3 from the grid (snapping not used for them): %d %s" % (len(offg), offg[:6]))
print("classes: B1977's key (3 decimals) on 20-30: %d; on 30-40: %d; on 40-50: %d" % tuple(len({key3(r, f) for r in rows}) for f in ("r2030", "r3040", "r4050")))
print("classes: 2 decimals on 20-30: %d; on 40-50: %d" % tuple(len({key2(r, f) for r in rows}) for f in ("r2030", "r4050")))
G = {}
for r in rows: G.setdefault(keyg(r, "r4050"), []).append((r["a"], r["b"]))
print("CLASSES (rates snapped to the grid of 1/60, from 40-50): %d" % len(G))
for g, pts in sorted(G.items(), key=lambda t: -len(t[1])):
    print("  %2d points: %s" % (len(pts), " ".join("%s=%s" % (k, v) for k, v in zip(K, g))))
same = sum(keyg(r, "r3040") == keyg(r, "r4050") for r in rows)
print("SUMMARY: the grid class of a point is the same on 30-40 and 40-50 at %d of 96" % same)
