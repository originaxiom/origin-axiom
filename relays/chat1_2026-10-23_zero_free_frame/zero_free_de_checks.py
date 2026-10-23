#!/usr/bin/env python3
"""POST HOC, labelled (committed before its run; the exploration note's referee, second pass, reported these from
scratch runs and asked for a committed check before they are cited).  Reads no target.
  (a) The five cases where zero_free_de_lines found an order-4-or-5 line not exact: every failing row (|ln R2| or
      |ln R1| >= 1e-6), with both sectors' m1/m3 and |ln R1|, |ln R2| there (from the committed census npz).
  (b) Near the fits: the largest |D_frame - 1| (c = 1) over Re tau in {0.1, 0.4}, Im tau in {2.3, ..., 2.7}, both
      horocycles, on the five alpha = 2/5 order-10 lines, for each direction in its better reading (F_6, F_14, F_22
      with S; F_10, F_18, F_26 and DR with S~), from the census npz.
  (c) Every order-10 line of the census at 0.4 + 2.5i, for F_14 and DR, both readings and horocycles, recomputed in
      main's frame: |D_frame - 1| with the Higgs as it is and with v_i = 0; whether 5w is the half period (1/2 mod 1)
      for the lines where v_i = 0 restores d = e.
  (d) By hand, checked numerically with mpmath: |theta3^a - theta4^a - 4a e^{i pi tau}| / |4a e^{i pi tau}| at
      0.4 + 2.5i and 0.1 + 1.3i for the ten a; and |v_i| / max(|v_+|, |v_-|) of the unit direction at the best six-row
      of each a < 0 line and at 0.4 + 2.5i.
    python3 -B zero_free_de_checks.py      # writes zero_free_de_checks.json"""
import contextlib, importlib.util, io, json, math, sys, pathlib
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zfc", HERE / "zero_free_census.py")
zfc = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(zfc)
rbs = zfc.rbs
IDX = json.loads((HERE / "zero_free_census_index.json").read_text())
X = np.load(HERE / "zero_free_census.npz")["data"]
LINES, TASKS, DIRS = IDX["lines"], IDX["tasks"], IDX["dirs"]
line_of = np.array([t[0] for t in TASKS]); re_of = np.array([t[1] for t in TASKS]); im_of = np.array([t[2] for t in TASKS])
RO = json.loads((HERE / "zero_free_readout.json").read_text())["by direction"]
FI = {"S": (4, 8), "St": (6, 10)}
L10 = math.log(10)


def ab(name):
    return tuple(Fr(s.strip()) for s in name.strip("()").split(","))


def order(name):
    a, b = ab(name)
    return math.lcm(a.denominator, b.denominator)


def lnR(x, rd):
    """x: (..., 28) log10 fields -> ln R2, ln R1"""
    i_dn, i_lp = FI[rd]
    return (x[..., i_lp] - x[..., i_dn]) * L10, (x[..., i_dn + 1] - x[..., i_lp + 1]) * L10


OUT = {}
# (a)
cases = [("F_-10", "S", "(0, 1/2)"), ("F_-10", "St", "(0, 1/2)"), ("F_-6", "S", "(0, 1/2)"), ("F_-2", "St", "(0, 1/2)"),
         ("F_6", "St", "(0, 1/5)")]
OUT["(a) the five exceptions"] = {}
for d, rd, name in cases:
    di, k = DIRS.index(d), LINES.index(name)
    m = np.where(line_of == k)[0]
    x = X[m, di].astype(np.float64)                                  # point, hor, field
    r2, r1 = lnR(x, rd)
    i_dn, i_lp = FI[rd]
    bad = np.argwhere((np.abs(r2) >= 1e-6) | (np.abs(r1) >= 1e-6))
    rows = [{"tau": [float(re_of[m[p]]), float(im_of[m[p]])], "hor": rbs.HORS[h], "|ln R2|": float(abs(r2[p, h])),
             "|ln R1|": float(abs(r1[p, h])), "log10 m1/m3 (down, lepton)": [float(x[p, h, i_dn + 1]), float(x[p, h, i_lp + 1])]}
            for p, h in bad]
    OUT["(a) the five exceptions"][f"{d} {rd} on {name}"] = {
        "failing rows": len(rows), "largest |ln R2| there": max((r["|ln R2|"] for r in rows), default=None),
        "range of |ln R1| there": [min((r["|ln R1|"] for r in rows), default=None), max((r["|ln R1|"] for r in rows), default=None)],
        "largest log10 m1/m3 there (either sector)": max((max(r["log10 m1/m3 (down, lepton)"]) for r in rows), default=None),
        "rows": rows}
# (b)
OUT["(b) near the fits, alpha = 2/5 order-10 lines"] = {}
o10 = [k for k, n in enumerate(LINES) if order(n) == 10 and ab(n)[0] == Fr(2, 5)]
sel = np.isin(line_of, o10) & np.isin(np.round(im_of, 2), [2.3, 2.4, 2.5, 2.6, 2.7])
for d, rd in (("F_6", "S"), ("F_14", "S"), ("F_22", "S"), ("F_10", "St"), ("F_18", "St"), ("F_26", "St"), ("dR", "St")):
    x = X[sel, DIRS.index(d)].astype(np.float64)
    r2, r1 = lnR(x, rd)
    OUT["(b) near the fits, alpha = 2/5 order-10 lines"][f"{d} {rd}"] = {
        "lines": [LINES[k] for k in o10], "rows": int(r2.size), "max |D_frame - 1|": float(np.max(np.abs(np.expm1(r2 + r1))))}
# (c)
OUT["(c) every order-10 line at 0.4 + 2.5i"] = {}
for k, name in enumerate(LINES):
    if order(name) != 10:
        continue
    a, b = ab(name)
    M = rbs.channels(0.4, 2.5, float(a), float(b))
    half = ((5 * a) % 1 == 0) and ((5 * b) % 1 == Fr(1, 2))
    rec = {"5*alpha integer and 5*beta = 1/2 mod 1": bool(half)}
    for d in ("F_14", "dR"):
        v = zfc.direction(d, 0.4, 2.5)
        for lam in (1.0, 0.0):
            w = np.array(v, dtype=complex); w[0] *= lam; w = w / np.linalg.norm(w)
            x = zfc.rows_at(M, w)
            worst = 0.0
            for rd in ("S", "St"):
                r2, r1 = lnR(x, rd)
                worst = max(worst, float(np.max(np.abs(np.expm1(r2 + r1)))))
            rec[f"{d}, v_i x {lam:g}: max |D_frame - 1|"] = worst
    OUT["(c) every order-10 line at 0.4 + 2.5i"][name] = rec
    print(name, rec, flush=True)
# (d)
mp.mp.dps = 30
OUT["(d) by hand"] = {"theta3^a - theta4^a against 4a e^{i pi tau} (relative error)": {}, "|v_i| / max(|v+|, |v-|)": {}}
for re_t, im_t in ((0.4, 2.5), (0.1, 1.3)):
    t2, t3, t4 = zfc.th(complex(re_t, im_t))
    q2 = mp.exp(1j * mp.pi * mp.mpc(re_t, im_t))
    for a in zfc.AS:
        approx = 4 * a * q2
        OUT["(d) by hand"]["theta3^a - theta4^a against 4a e^{i pi tau} (relative error)"][f"a = {a} at {re_t} + {im_t}i"] = \
            float(abs((t3 ** a - t4 ** a - approx) / approx))
pts = {f"F_{a}": RO[f"F_{a}"]["S-all c=3"]["six"]["where"]["tau"] for a in (-10, -6, -2)}
for d, (re_t, im_t) in list(pts.items()) + [(f"F_{a}", (0.4, 2.5)) for a in (-10, -6, -2)]:
    v = zfc.direction(d, re_t, im_t)
    vp, vm = v[1] + 1j * v[2], v[1] - 1j * v[2]
    OUT["(d) by hand"]["|v_i| / max(|v+|, |v-|)"][f"{d} at {re_t} + {im_t}i"] = float(abs(v[0]) / max(abs(vp), abs(vm)))
(HERE / "zero_free_de_checks.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
