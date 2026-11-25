#!/usr/bin/env python3
"""SM-C23: is frame C covariant under SL(2, Z) acting on the modulus and the point together?  (card
relays/cards/SM_C23_frame-cs-joint-covariance.md, pushed with this script before it is run.)  Data-free: only
ratios of singular values and moduli of the mixing are compared with themselves at the image; no measured number.
Main's frame is used unchanged (B1945's determinant_law.parts, B1945's cusp_mixing.U_of); only its canonical end is
supplied explicitly, as L(g tau) = L(tau) + log|c tau + d| (B1927), because B1927's table covers the fundamental
domain only.
    python3 -B run_c23.py MAIN_CHECKOUT > c23_run.txt"""
import json
import pathlib
import sys
from fractions import Fraction as Fr
from math import lcm

HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(next((MAIN / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL      # noqa: E402
import cusp_mixing as CM          # noqa: E402
mp = DL.mp
CR = DL.FM.CR
TABLE_CANON = CR.canon
SECS = ("up", "down", "lep")

# --- the group and the actions on the point (row convention; the point is (a, b), first coordinate times tau) ---
T = ((1, 1), (0, 1)); S = ((0, -1), (1, 0)); ACT = ((2, 1), (1, 1))
def inv(g): (a, b), (c, d) = g; return ((d, -b), (-c, a))
def tr(g): (a, b), (c, d) = g; return ((a, c), (b, d))
def rowmul(v, g): return ((v[0] * g[0][0] + v[1] * g[1][0]) % 1, (v[0] * g[0][1] + v[1] * g[1][1]) % 1)
def charlevel(v, g):                 # act on the characteristic (a, 2b), read back as (a, b)
    c = rowmul((v[0], 2 * v[1]), inv(g)); return (c[0], (c[1] / 2) % 1)
CANDIDATES = {
    "C1 (a,b) g^-1": lambda v, g: rowmul(v, inv(g)),
    "C2 (a,b) g": lambda v, g: rowmul(v, g),
    "C3 (a,b) g^T": lambda v, g: rowmul(v, tr(g)),
    "C4 (a,b) g^-T": lambda v, g: rowmul(v, tr(inv(g))),
    "C5 (a,2b) g^-1": charlevel,
}
def mob(g, t): (a, b), (c, d) = g; return (a * t + b) / (c * t + d), c * t + d

# --- the points: one orbit of the act at order 30 (it carries the slow 2-3 point), and controls of orders 5 and 6 ---
def order(p): return lcm(p[0].denominator, p[1].denominator)
P6 = sorted({(Fr(i, 6), Fr(j, 6)) for i in range(6) for j in range(6) if order((Fr(i, 6), Fr(j, 6))) == 6})
P5 = [((k * Fr(1, 5)) % 1, (k * Fr(2, 5)) % 1) for k in range(1, 5)]
P30 = sorted({((a5 + a6) % 1, (b5 + b6) % 1) for (a5, b5) in P5 for (a6, b6) in P6})
assert len(P30) == 96
orb = [(Fr(4, 15), Fr(1, 30))]
while True:
    n = rowmul(orb[-1], ACT)
    if n == orb[0]: break
    orb.append(n)
POINTS = orb + P5 + P6[:4]

def frame(t, v, L):
    """invariants of frame C at modulus t, point v, end L: per sector the sorted ratios s1/s3, s2/s3; |V| (ascending)"""
    CR.canon = lambda z: {"L_2": float(L), "L_max": float(L), "_extrapolated": False}
    try:
        Ys = {s: DL.parts(mp.re(t), mp.im(t), v[0], v[1], s)[2]["S"] for s in SECS}
    finally:
        CR.canon = TABLE_CANON
    out = {}
    for s in SECS:
        sv = sorted(abs(x) for x in mp.svd_c(Ys[s], compute_uv=False))
        out[s] = [sv[0] / sv[2], sv[1] / sv[2]] if sv[2] != 0 else None
    V = CM.U_of(Ys["up"]).H * CM.U_of(Ys["down"])
    out["V"] = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
    return out

def dist(A, B):
    d = 0
    for s in SECS:
        if A[s] is None or B[s] is None:
            d = max(d, 0 if A[s] is B[s] else mp.inf); continue
        d = max(d, *(abs(mp.log(x / y)) if x > 0 and y > 0 else abs(x - y) for x, y in zip(A[s], B[s])))
    vd = max(abs(A["V"][i][j] - B["V"][i][j]) for i in range(3) for j in range(3))
    return float(d), float(vd)

def main():
    mp.mp.dps = 50
    TAUS = [mp.mpc("0.13", "1.2"), mp.mpc("0.31", "1.5"), mp.mpc("-0.2", "2.0")]
    out = {"points": [[str(a), str(b)] for a, b in POINTS], "rows": []}
    for t0 in TAUS:
        L0 = mp.mpf(TABLE_CANON(complex(float(mp.re(t0)), float(mp.im(t0))))["L_2"])
        base = {}
        for v in POINTS:
            mp.mp.dps = 50
            base[v] = frame(t0, v, L0)
        for gname, g in (("T", T), ("S", S), ("ACT", ACT)):
            mp.mp.dps = 50
            t1, j = mob(g, t0); L1 = L0 + mp.log(abs(j))
            for cname, act in CANDIDATES.items():
                worst_m = worst_v = 0.0
                for v in POINTS:
                    mp.mp.dps = 50
                    dm, dv = dist(base[v], frame(t1, act(v, g), L1))
                    worst_m, worst_v = max(worst_m, dm), max(worst_v, dv)
                row = dict(tau=mp.nstr(t0, 6), g=gname, cand=cname, masses=worst_m, mixing=worst_v)
                out["rows"].append(row)
                print("tau %s  %-3s  %-15s  worst |ln ratio| %.2e   worst |dV| %.2e" % (row["tau"], gname, cname,
                      worst_m, worst_v), flush=True)
        # plants: S with the point unmoved; S with the end unshifted (best candidate's action)
        mp.mp.dps = 50
        t1, j = mob(S, t0)
        for pname, act, L1 in (("P1 S, point unmoved", lambda v, g: v, L0 + mp.log(abs(j))),
                               ("P2 S, end unshifted", CANDIDATES["C1 (a,b) g^-1"], L0)):
            wm = wv = 0.0
            for v in POINTS[:6]:
                mp.mp.dps = 50
                dm, dv = dist(base[v], frame(t1, act(v, S), L1)); wm, wv = max(wm, dm), max(wv, dv)
            out["rows"].append(dict(tau=mp.nstr(t0, 6), g="plant", cand=pname, masses=wm, mixing=wv))
            print("tau %s  plant %-22s worst |ln ratio| %.2e   worst |dV| %.2e" % (mp.nstr(t0, 6), pname, wm, wv),
                  flush=True)
    (HERE / "c23_results.json").write_text(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
