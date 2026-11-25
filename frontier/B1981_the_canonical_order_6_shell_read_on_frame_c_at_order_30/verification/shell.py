"""B1981 (main, 2026-11-25; data-free): frame C read over the canonical 24-point primitive order-6 shell at each order-5 point
of the act's line (and over all 96 points), in two declared readings (L, a weighted sum of Y; G, a weighted sum of Y Y^dagger),
under the uniform weight and three fixed alternatives. The card (CARD.md) fixes the expectations; hashes in
EXPECTATIONS_HASHED.md were fixed before the run.
    python3 -B shell.py > shell_run.txt"""
import sys, pathlib, json, time
from fractions import Fraction as Fr
from math import lcm
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
mp = DL.mp
SEC = ("up", "down", "lep")
K = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")
P96 = sorted((Fr(r["a"]), Fr(r["b"])) for r in json.loads((next((ROOT / "frontier").glob("B1977_*")) / "verification" / "rates30_run.json").read_text()))
def five(p): return ((6 * p[0]) % 1, (6 * p[1]) % 1)
def six_ok(p):
    q = ((25 * p[0]) % 1, (25 * p[1]) % 1)          # the 6-part (25 = 1 mod 6, 0 mod 5); exact order 6
    return lcm(q[0].denominator, q[1].denominator) == 6
assert len(P96) == 96 and all(six_ok(p) for p in P96)
BLOCKS = {}
for p in P96: BLOCKS.setdefault(five(p), []).append(p)
assert len(BLOCKS) == 4 and all(len(v) == 24 for v in BLOCKS.values())
BLOCKS = {"p5=(%s,%s)" % k: v for k, v in sorted(BLOCKS.items())}; BLOCKS["all 96"] = P96
H = (30.0, 40.0, 50.0)
t0 = time.time(); Y = {}
for p in P96:
    for y in H:
        for s in SEC: Y[(p, y, s)] = DL.parts("0.13", y, p[0], p[1], s)[2]["S"]
print("frame evaluated at %d points x %d heights x 3 sectors  [%.0f s]" % (len(P96), len(H), time.time() - t0), flush=True)
def weights(n, k):
    return [mp.mpf(1)] * n if k == 0 else [mp.mpf(1 + ((7 * i + 3 * k) % 11)) / 6 for i in range(n)]
def gram_U(Hm):
    E, Q = mp.eighe(Hm); order = sorted(range(3), key=lambda i: E[i])
    return [abs(E[i]) for i in order], mp.matrix([[Q[r, order[c]] for c in range(3)] for r in range(3)])
def read(pts, y, k, mode):
    mp.mp.dps = int(30 + 2 * y); w = weights(len(pts), k); out = {}; U = {}
    for s in SEC:
        if mode == "L":
            A = mp.matrix(3, 3)
            for wi, p in zip(w, pts): A += wi * Y[(p, y, s)]
            sv = sorted(abs(v) for v in mp.svd_c(A, compute_uv=False)); U[s] = CM.U_of(A)
        else:
            Hm = mp.matrix(3, 3)
            for wi, p in zip(w, pts): Hm += wi * Y[(p, y, s)] * Y[(p, y, s)].H
            ev, U[s] = gram_U(Hm); sv = [mp.sqrt(e) for e in ev]
        out[s + "_m2m3"] = sv[1] / sv[2]; out[s + "_m1m3"] = sv[0] / sv[2]
    V = U["up"].H * U["down"]
    for (i, j, n) in ((0, 1, "V12"), (1, 2, "V23"), (0, 2, "V13")): out[n] = abs(V[i, j])
    out["diag"] = min(abs(V[i, i]) for i in range(3)); return out
def rates(A, B):
    return {k: (float(-(mp.log(B[k]) - mp.log(A[k])) / (mp.pi * 10)) if A[k] > 0 and B[k] > 0 else None) for k in K}
R = {}
for mode in ("L", "G"):
    for bname, pts in BLOCKS.items():
        for k in range(4):
            S = {y: read(pts, y, k, mode) for y in H}
            R[(mode, bname, k)] = dict(r3040=rates(S[30.0], S[40.0]), r4050=rates(S[40.0], S[50.0]), diag50=float(S[50.0]["diag"]))
print("readings done  [%.0f s]" % (time.time() - t0))
json.dump({"%s|%s|%d" % key: v for key, v in R.items()}, open(pathlib.Path(__file__).with_name("shell_run.json"), "w"), indent=1)
def fmt(r): return " ".join("%s=%s" % (k, "-" if r[k] is None else "%.4f" % r[k]) for k in K)
for mode in ("L", "G"):
    for bname in BLOCKS:
        r = R[(mode, bname, 0)]
        print("%s %-16s 40-50: %s | diag50 %.4f" % (mode, bname, fmt(r["r4050"]), r["diag50"]))
        print("%s %-16s 30-40: %s" % (mode, bname, fmt(r["r3040"])))
def close(a, b, tol=1e-3): return all((a[k] is None and b[k] is None) or (a[k] is not None and b[k] is not None and abs(a[k] - b[k]) <= tol) for k in K)
B4 = [b for b in BLOCKS if b != "all 96"]
CL = []
for r in json.loads((next((ROOT / "frontier").glob("B1979_*")) / "verification" / "heights_run.json").read_text()):
    c = {k: float(Fr(round(r["r4050"][k] * 60), 60)) for k in K}
    if c not in CL: CL.append(c)
assert len(CL) == 12
def on_grid(v): return v is not None and abs(v * 60 - round(v * 60)) / 60 <= 1e-3
for mode in ("L", "G"):
    h1 = all(close(R[(mode, b, k)]["r4050"], R[(mode, b, 0)]["r4050"]) for b in BLOCKS for k in (1, 2, 3))
    worst = max(abs(R[(mode, b, k)]["r4050"][q] - R[(mode, b, 0)]["r4050"][q]) for b in BLOCKS for k in (1, 2, 3) for q in K
                if R[(mode, b, k)]["r4050"][q] is not None and R[(mode, b, 0)]["r4050"][q] is not None)
    print("SUMMARY H1 %s: rates independent of the weight within 1e-3: %s (largest difference %.1e)" % (mode, h1, worst))
for mode in ("L",):
    h2 = all(R[(mode, b, 0)]["r4050"][q] is not None and R[(mode, b, 0)]["r4050"][q] < 3 for b in BLOCKS for q in K if q.endswith(("m2m3", "m1m3")))
    print("SUMMARY H2 L: full rank (every mass rate finite and below 3) in every block: %s" % h2)
for mode in ("L", "G"):
    m = [next((i for i, c in enumerate(CL) if close(R[(mode, b, 0)]["r4050"], c)), None) for b in B4]
    print("SUMMARY H3 %s: each block's rates equal one of B1979's 12 classes: %s (class per block %s)" % (mode, all(x is not None for x in m), m))
    print("SUMMARY H4 %s: the 4 blocks give the same rates: %s" % (mode, all(close(R[(mode, b, 0)]["r4050"], R[(mode, B4[0], 0)]["r4050"]) for b in B4)))
def hier(r): return all(r[s + "_m2m3"] is not None and r[s + "_m2m3"] >= 0.1 and r[s + "_m1m3"] is not None and r[s + "_m1m3"] >= 0.2 for s in ("up", "down"))
print("SUMMARY H5 L: every block aligned at 50 and hierarchical in both quark sectors: %s (aligned %s; hierarchical %s)" % (
    all(R[("L", b, 0)]["diag50"] >= 0.9 and hier(R[("L", b, 0)]["r4050"]) for b in BLOCKS),
    [R[("L", b, 0)]["diag50"] >= 0.9 for b in BLOCKS], [hier(R[("L", b, 0)]["r4050"]) for b in BLOCKS]))
print("SUMMARY H6: the lepton m2/m3 rate is 2/5 in both readings in every block: %s" % all(
    R[(m, b, 0)]["r4050"]["lep_m2m3"] is not None and abs(R[(m, b, 0)]["r4050"]["lep_m2m3"] - 0.4) <= 1e-3 for m in ("L", "G") for b in BLOCKS))
print("SUMMARY H7: every rate of every reading and block within 1e-3 of the grid of 1/60: %s" % all(
    on_grid(R[(m, b, 0)]["r4050"][q]) for m in ("L", "G") for b in BLOCKS for q in K))
print("SUMMARY H8: readings L and G give the same rates in every block: %s" % all(close(R[("L", b, 0)]["r4050"], R[("G", b, 0)]["r4050"]) for b in BLOCKS))
