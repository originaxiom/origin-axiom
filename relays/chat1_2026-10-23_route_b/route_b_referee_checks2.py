#!/usr/bin/env python3
"""POST HOC, labelled (at the referee's second pass; committed before its run): two checks behind the second round of
corrections to ROUTE_B_EXPLORATION.md.
  1. The frame's own R2 and R1 at kappa -> 0 (the sealed census's rows, no Clebsch), at the base points where route (b)'s
     best rows sit: in the reading S for every sector at route_b_sall's three order-9 points, and in the split reading
     at route (b)'s best split six-row's point (0.4 + 2.8i on (2/5, 1/10)); both horocycles.
  2. Covariance of a blend of main's two readings of DR at the Clebsch-1 control's best row (0.4 + 2.8i on (2/5, 1/2),
     L_max, reading S~): S_eff = S~(DR) + lam S(DR) with lam the blend coefficient there, compared at tau and at
     tau + 1 (b -> b - a) with lam fixed, with lam times -i and with lam times i; and the c0 model itself
     (S~(DR + kappa S(c0)), c0 recomputed at tau + 1) under the same move.
    python3 -B route_b_referee_checks2.py      # writes route_b_referee_checks2.json and _run.txt"""
import contextlib, importlib.util, io, json, math, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SEL = HERE.parent / "chat1_2026-10-22_selection_map"
_spec = importlib.util.spec_from_file_location("rbs", HERE / "route_b_scan.py")
rbs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rbs)
B, tic = rbs.B, rbs.tic
LINES = [(float(Fr(a)), float(Fr(b))) for (_t, a, b) in tic.LINES]
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


# 1. kappa -> 0 from the census
want = {"S for every sector": [((0.1, 3.5), (2 / 9, 5 / 9)), ((0.4, 3.5), (2 / 9, 5 / 9)), ((0.1, 3.5), (2 / 9, 4 / 9))],
        "split": [((0.4, 2.8), (0.4, 0.1))]}
read = {"S for every sector": ("S", "S", "S"), "split": ("St", "S", "S")}
rows = [json.loads(l) for l in (SEL / "two_ingredients_census.jsonl").read_text().splitlines() if l.strip()]
OUT["kappa -> 0"] = {}
for key, pts in want.items():
    ru, rd, rl = read[key]
    for (re_t, im_t), (a, b) in pts:
        r = next(r for r in rows if r["Re_tau"] == re_t and r["Im_tau"] == im_t and abs(LINES[r["line"]][0] - a) < 1e-9 and abs(LINES[r["line"]][1] - b) < 1e-9)
        for hor in ("L_max", "L_2"):
            d, l = r[f"down|{hor}|{rd}"], r[f"lep|{hor}|{rl}"]
            R2, R1 = l[0] / d[0], d[1] / l[1]
            OUT["kappa -> 0"][f"{key} {re_t}+{im_t}i ({a:.4f}, {b:.4f}) {hor}"] = [R2, R1]
            say(f"1. {key}, {re_t} + {im_t}i on ({a:.4f}, {b:.4f}), {hor}: R2 {R2:.2f}, R1 {R1:.2f} (no Clebsch, kappa -> 0)")

# 2. the blend's covariance at the control's best row
re_t, im_t, a, b = 0.4, 2.8, 0.4, 0.5
hor = "L_max"
M0 = rbs.channels(re_t, im_t, a, b); M1 = rbs.channels(re_t + 1, im_t, a, b - a)


def higgs(t_re):
    v1, v2, v3 = rbs.at(rbs.H1, t_re, im_t), rbs.at(rbs.H2, t_re, im_t), rbs.at(rbs.H3, t_re, im_t)
    u2, u3 = v2 / np.linalg.norm(v2), v3 / np.linalg.norm(v3)
    return v1, (u2 + u3) / math.sqrt(2)


v1, c0 = higgs(re_t); w1, d0 = higgs(re_t + 1)
ir = int(np.argmin(np.abs(np.array(rbs.RHO) - 0.06309573444801936)))   # the control's best nine-row: rho 10^-1.2, phi 75
rho, phi = rbs.RHO[ir], math.radians(75)
assert abs(rho - 0.06309573444801936) < 1e-15
kap = rho * np.exp(1j * phi) * np.linalg.norm(v1)
e = np.conj(v1) / np.linalg.norm(v1)
lam = np.conj(kap * np.vdot(e, c0)) / np.linalg.norm(v1)     # S~(h1 + kap c0) ~ S(conj h1) + lam S(h1)


def outs(M, Seff):
    Y = {sec: B.coupling(Seff, M[(sec, hor)]) for sec in ("up", "down", "lep")}
    o = []
    for sec in ("up", "down", "lep"):
        s = np.linalg.svd(Y[sec], compute_uv=False); o += [s[1] / s[0], s[2] / s[0]]
    return np.array(o + tic.ckm_left(Y["up"], Y["down"])[:3])


base = outs(M0, rbs.St(rbs.S_of(v1)) + lam * rbs.S_of(v1))
res = {}
for label, f in (("lam fixed", 1), ("lam times -i", -1j), ("lam times i", 1j)):
    moved = outs(M1, rbs.St(rbs.S_of(w1)) + lam * f * rbs.S_of(w1))
    res[label] = float(np.max(np.abs(np.log(moved / base))))
c0_0 = outs(M0, rbs.St(rbs.S_of(v1) + kap * rbs.S_of(c0)))
c0_1 = outs(M1, rbs.St(rbs.S_of(w1) + kap * rbs.S_of(d0)))
res["the c0 model (c0 recomputed at tau + 1)"] = float(np.max(np.abs(np.log(c0_1 / c0_0))))
res["|lam|"] = float(abs(lam))
OUT["blend covariance, max |delta ln| over the six ratios and three |V|"] = res
say(f"2. blend S~(DR) + lam S(DR) at 0.4 + 2.8i on (2/5, 1/2), L_max, |lam| {abs(lam):.4f}: under tau -> tau + 1, max |delta ln| "
    + "; ".join(f"{k} {v:.2e}" for k, v in res.items() if k != "|lam|"))
(HERE / "route_b_referee_checks2.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "route_b_referee_checks2_run.txt").write_text("\n".join(LOG) + "\n")
