#!/usr/bin/env python3
"""POST HOC, labelled (committed before its run; the referee of ZERO_FREE_FRAME_EXPLORATION.md reported it from a scratch
check and asked for a committed script before it is cited).  Reads no target.
The question: at the census's best six-rows the down quarks and the leptons coincide (D = c^2) although most of those
rows lie on order-10 lines (2/5, 1/10), (2/5, 3/10), where main's coincidence law (B1698, B1703) does not force d = e.
The referee's observation: with the Higgs's i-component set to zero, d = e holds exactly there.  This script computes,
in main's frame (through the zero-free census's code), D_frame - 1 = (R2 * R1 at c = 1) - 1 for
  (a) the best six-row of each fitting combination of the census read-out (F_6, F_14, F_22 with S; F_10, F_18, F_26 and
      DR with S~), at its tau, line and horocycle: the direction as it is, with v_i set to zero, and with v_i scaled by
      lambda in {0.01, 0.1, 10, 100} (renormalised; ratios do not see the norm); and |v_i| of the unit direction;
  (b) along the lines (2/5, 1/10), (2/5, 3/10), (2/5, 7/10) and (2/5, 4/5), at Re tau in {0.1, 0.4} and Im tau in
      {1.5, 2.0, 2.5, 3.0, 3.5}, both horocycles, for F_6, F_14, F_10 and DR: the largest |D_frame - 1| with v as it
      is and with v_i = 0.
    python3 -B zero_free_de_mechanism.py      # writes zero_free_de_mechanism.json"""
import contextlib, importlib.util, io, json, math, sys, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zfc", HERE / "zero_free_census.py")
zfc = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(zfc)
rbs = zfc.rbs
RO = json.loads((HERE / "zero_free_readout.json").read_text())["by direction"]
IDX = {"S": (4, 8), "St": (6, 10)}                       # (down m2/m3, lep m2/m3) field indices; m1/m3 follow


def d_minus_1(x, rd, ih):
    i_dn, i_lp = IDX[rd]
    lnR2 = (x[ih, i_lp] - x[ih, i_dn]) * math.log(10)
    lnR1 = (x[ih, i_dn + 1] - x[ih, i_lp + 1]) * math.log(10)
    return math.expm1(lnR2 + lnR1)


def variant(v, lam):
    w = np.array(v, dtype=complex); w[0] *= lam
    n = np.linalg.norm(w)
    return w / n


OUT = {"(a) best six-rows": {}, "(b) along the lines": {}}
for d, rd in (("F_6", "S"), ("F_14", "S"), ("F_22", "S"), ("F_10", "St"), ("F_18", "St"), ("F_26", "St"), ("dR", "St")):
    wh = RO[d][f"{'S-all' if rd == 'S' else 'St-all'} c=3"]["six"]["where"]
    re_t, im_t = wh["tau"]; name = wh["line"]; ih = rbs.HORS.index(wh["hor"])
    a, b = (float(Fr(s.strip())) for s in name.strip("()").split(","))
    M = rbs.channels(re_t, im_t, a, b)
    v = zfc.direction(d, re_t, im_t)
    rec = {"tau": [re_t, im_t], "line": name, "hor": wh["hor"], "|v_i| of the unit direction": float(abs(v[0]))}
    for lam in (1.0, 0.0, 0.01, 0.1, 10.0, 100.0):
        rec[f"D_frame - 1, v_i x {lam:g}"] = d_minus_1(zfc.rows_at(M, variant(v, lam)), rd, ih)
    OUT["(a) best six-rows"][f"{d} {rd}"] = rec
    print(d, rd, name, rec["|v_i| of the unit direction"], rec["D_frame - 1, v_i x 1"], rec["D_frame - 1, v_i x 0"], flush=True)
for name in ("(2/5, 1/10)", "(2/5, 3/10)", "(2/5, 7/10)", "(2/5, 4/5)"):
    a, b = (float(Fr(s.strip())) for s in name.strip("()").split(","))
    worst = {}
    for re_t in (0.1, 0.4):
        for im_t in (1.5, 2.0, 2.5, 3.0, 3.5):
            M = rbs.channels(re_t, im_t, a, b)
            for d in ("F_6", "F_14", "F_10", "dR"):
                v = zfc.direction(d, re_t, im_t)
                for lam in (1.0, 0.0):
                    x = zfc.rows_at(M, variant(v, lam))
                    for rd in ("S", "St"):
                        for ih in range(2):
                            key = f"{d} {rd}, v_i x {lam:g}"
                            worst[key] = max(worst.get(key, 0.0), abs(d_minus_1(x, rd, ih)))
    OUT["(b) along the lines"][name] = worst
    print(name, {k: f"{v:.1e}" for k, v in worst.items()}, flush=True)
(HERE / "zero_free_de_mechanism.json").write_text(json.dumps(OUT, indent=1) + "\n")
