"""B1976 (main, 2026-11-24; data-free): frame C, every sector reading S, at the points of order 30 on the act's line times
the order-6 points, with the controls of orders 6 and 5.  See CARD.md for the expectations.
    python3 -B level30.py > level30_run.txt"""
import sys, pathlib, json
from fractions import Fraction as Fr
from math import gcd, lcm
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
mp = DL.mp
SIXY = DL.B.SIXY; PAIRS = {s: (SIXY[DL.B.SECTORS[s][0]], SIXY[DL.B.SECTORS[s][1]]) for s in ("up", "down", "lep")}

def tied(N, p, q):
    units = [k for k in range(1, N) if gcd(k, N) == 1]
    for k in units:
        a = ((k * p[0]) % N, (k * p[1]) % N)
        if a == (q[0] % N, q[1] % N): return "k=%d" % k
        if a == (q[1] % N, q[0] % N): return "k=%d swapped" % k
    return None

print("E0: the unit test (sector pairs tied by a unit of Z/N, mod N):")
for N in (5, 6, 30):
    rel = {("%s~%s" % (s, t)): tied(N, PAIRS[s], PAIRS[t]) for s in PAIRS for t in PAIRS if s <= t}
    print("  N = %2d: %s" % (N, {k: v for k, v in rel.items() if v}))

def order(p): return lcm(p[0].denominator, p[1].denominator)
P6 = sorted({(Fr(i, 6), Fr(j, 6)) for i in range(6) for j in range(6) if order((Fr(i, 6), Fr(j, 6))) == 6})
P5 = [((k * Fr(1, 5)) % 1, (k * Fr(2, 5)) % 1) for k in range(1, 5)]
P30 = sorted({(((a5 + a6) % 1), ((b5 + b6) % 1)) for (a5, b5) in P5 for (a6, b6) in P6})
assert len(P6) == 24 and len(P30) == 96 and all(order(p) == 30 for p in P30)

def at(a, b, y=30.0):
    out = {}
    for s in ("up", "down", "lep"):
        RD, Mw, Ys, u, cs, ds = DL.parts("0.13", y, a, b, s)
        Y = Ys["S"]; sv = sorted(abs(x) for x in mp.svd_c(Y, compute_uv=False))
        mx = max([abs(v) for v in u.values() if v != 0] or [mp.mpf(1)])
        out[s] = dict(Y=Y, sv=sv, one=(abs(u["1"]) / mx if u["1"] != 0 else mp.mpf(0)))
    V = CM.U_of(out["up"]["Y"]).H * CM.U_of(out["down"]["Y"])
    out["diag"] = min(abs(V[k, k]) for k in range(3)); out["off"] = max(abs(V[i, j]) for i in range(3) for j in range(3) if i != j)
    d, l = out["down"]["sv"], out["lep"]["sv"]
    out["D"] = max(abs(mp.log((l[1] / l[2]) / (d[1] / d[2]))), abs(mp.log((l[0] / l[2]) / (d[0] / d[2]))))
    out["updown"] = mp.mnorm(out["up"]["Y"] - out["down"]["Y"], 1) / mp.mnorm(out["down"]["Y"], 1)
    return out

rows = {}
for name, pts in (("P6", P6), ("P5", P5), ("P30", P30)):
    rows[name] = []
    for (a, b) in pts:
        r = at(a, b)
        rows[name].append(dict(a=str(a), b=str(b), diag=float(r["diag"]), off=float(r["off"]), D=float(r["D"]), up_one=float(r["up"]["one"]), updown=float(r["updown"])))
        print("%-3s (%s, %s): least diag %.4f, largest off %.2e | lep-vs-down max|ln| %.3e | up '1' channel %.2e | |Y_up - Y_down|/|Y_down| %.2e" % (
            name, a, b, r["diag"], r["off"], r["D"], r["up"]["one"], r["updown"]), flush=True)
json.dump(rows, open(pathlib.Path(__file__).with_name("level30_run.json"), "w"), indent=1)
P5off = {(r["a"], r["b"]): r["off"] for r in rows["P5"]}
def five_part(a, b):
    a, b = Fr(a), Fr(b)
    for (a5, b5) in P5:
        if order(((a - a5) % 1, (b - b5) % 1)) == 6: return (str(a5), str(b5))
print("SUMMARY E1: P6 points with Y_up = Y_down (rel. diff < 1e-30): %d of %d; with the mixing the identity (diag > 1 - 1e-20): %d" % (
    sum(r["updown"] < 1e-30 for r in rows["P6"]), len(rows["P6"]), sum(r["diag"] > 1 - 1e-20 for r in rows["P6"])))
print("SUMMARY E2: P5 points with the up '1' channel zero: %d of 4; with lep = down (max|ln| < 1e-20): %d of 4" % (
    sum(r["up_one"] == 0 for r in rows["P5"]), sum(r["D"] < 1e-20 for r in rows["P5"])))
print("SUMMARY E3: P30 points with the leptons split from down (max|ln| > 0.1): %d of %d" % (sum(r["D"] > 0.1 for r in rows["P30"]), len(rows["P30"])))
print("SUMMARY E4: P30 points with the up '1' channel nonzero (> 1e-10): %d of %d" % (sum(r["up_one"] > 1e-10 for r in rows["P30"]), len(rows["P30"])))
print("SUMMARY E5: P30 points aligned (least diag >= 0.9): %d of %d" % (sum(r["diag"] >= 0.9 for r in rows["P30"]), len(rows["P30"])))
print("SUMMARY E6: P30 points whose largest off-diagonal exceeds that of their act's order-5 point: %d of %d" % (
    sum(r["off"] > P5off[five_part(r["a"], r["b"])] for r in rows["P30"]), len(rows["P30"])))
