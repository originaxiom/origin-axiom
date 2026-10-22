#!/usr/bin/env python3
"""POST HOC, labelled (at the referee's prompt, after every output above was read; committed before its run): the
checks behind the referee's corrections to ROUTE_B_EXPLORATION.md.
  1. The sealed census in the split reading (up S~; down and leptons S), with the by-hand Clebsch 3 and without: the
     best six among rows with D within 3 sigma of P-094, with R2, R1, D, the nine and model over measured there.
  2. The directions as scanned: |u2 . u3| (u = unit h2, h3), the lengths of the four combinations, and the overlap of
     c0 with the conjugate of h1, at the fourteen base points.
  3. R2, R1 at the best D-matched S~ row (Clebsch -3) and at the control's best six-row; and the count of rows with D in
     band and both ratios in [2, 4.5].
  4. The control's best row with c0 replaced by its projection on conj(h1): the coupling is then DR read as S~ plus a
     small multiple of DR read as S (a blend of main's two readings).
    python3 -B route_b_referee_checks.py      # writes route_b_referee_checks.json and _run.txt"""
import contextlib, hashlib, importlib.util, io, json, math, subprocess, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
SEL = HERE.parent / "chat1_2026-10-22_selection_map"
_spec = importlib.util.spec_from_file_location("rbs", HERE / "route_b_scan.py")
rbs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rbs)
B, tic = rbs.B, rbs.tic


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
v = json.loads(bd)["masses_GeV"]["value"]; C = json.loads(bc)["ckm_abs"]["value"]
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
P094, SIG = 10.58, 0.11
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


# 1. the census, split reading
LINES = [f"({a}, {b})" for (_t, a, b) in tic.LINES]
rows = [json.loads(l) for l in (SEL / "two_ingredients_census.jsonl").read_text().splitlines() if l.strip()]
for c in (3, 1):
    best = None; n = 0
    for r in rows:
        for hor in ("L_max", "L_2"):
            x = np.log(np.maximum(np.array(r[f"up|{hor}|St"] + r[f"down|{hor}|S"] + r[f"lep|{hor}|S"] + r[f"ckm|{hor}|St|S"][:3], dtype=float), 1e-300))
            x[4] += math.log(c); x[5] -= math.log(c)
            R2, R1 = math.exp(x[4] - x[2]), math.exp(x[3] - x[5])
            if abs(R2 * R1 - P094) <= 3 * SIG:
                n += 1
                s6 = math.exp(np.max(np.abs(x[:6] - T6)))
                if best is None or s6 < best[0]:
                    best = (s6, r["Re_tau"], r["Im_tau"], LINES[r["line"]], hor, R2, R1, R2 * R1, math.exp(np.max(np.abs(x - T9))), np.exp(x - T9).round(3).tolist())
    OUT[f"census split c={c}"] = {"n_D_matched": n, "best": best}
    say(f"1. census, split reading, Clebsch {c}: {n} rows with D within 3 sigma; best six {best[0]:.3f} at {best[1]} + {best[2]}i on {best[3]}, "
        f"{best[4]}; R2 {best[5]:.2f}, R1 {best[6]:.2f}, D {best[7]:.2f}; nine {best[8]:.2f}; model/measured {best[9]}")

# 2. the directions as scanned
OUT["directions"] = []
for (re_t, im_t, a, b) in rbs.BASE:
    v1, v2, v3 = rbs.at(rbs.H1, re_t, im_t), rbs.at(rbs.H2, re_t, im_t), rbs.at(rbs.H3, re_t, im_t)
    u2, u3 = v2 / np.linalg.norm(v2), v3 / np.linalg.norm(v3)
    lens = {f"c{ang}": float(np.linalg.norm((u2 + np.exp(1j * math.radians(ang)) * u3) / math.sqrt(2))) for ang in (0, 90, 180, 270)}
    c0 = (u2 + u3) / math.sqrt(2)
    ov = float(abs(np.vdot(np.conj(v1) / np.linalg.norm(v1), c0 / np.linalg.norm(c0))))
    OUT["directions"].append({"base": [re_t, im_t, a, b], "u2.u3 (complex)": str(np.round(np.vdot(u2, u3), 4)), "lengths": lens,
                              "|<conj h1, c0>| (unit)": ov})
say("2. directions: " + "; ".join(f"{d['base']}: u2.u3 {d['u2.u3 (complex)']}, |c0| {d['lengths']['c0']:.3f}, |c180| {d['lengths']['c180']:.3f}, "
                                   f"overlap(c0, conj h1) {d['|<conj h1, c0>| (unit)']:.4f}" for d in OUT["directions"]))

# 3. R2, R1 at the best D-matched S~ row and at the control's best six-row
X = np.load(HERE / "route_b_scan.npz")["data"][..., 0, :]
XC = np.load(HERE / "route_b_clebsch1_control.npz")["data"]
for label, A in (("Clebsch -3, S~", X), ("control, S~", XC)):
    L = np.log(np.maximum(A[..., :9], 1e-300))
    six = np.max(np.abs(L[..., :6] - T6), axis=-1)
    R2 = np.exp(L[..., 4] - L[..., 2]); R1 = np.exp(L[..., 3] - L[..., 5]); D = R2 * R1
    dm = np.abs(D - P094) <= 3 * SIG
    i = np.unravel_index(np.argmin(np.where(dm, six, np.inf)), six.shape)
    j = np.unravel_index(np.argmin(six), six.shape)
    both = dm & (R2 >= 2) & (R2 <= 4.5) & (R1 >= 2) & (R1 <= 4.5)
    k = np.unravel_index(np.argmin(np.where(both, six, np.inf)), six.shape) if both.any() else None
    OUT[f"R at rows, {label}"] = {"best D-matched": [float(np.exp(six[i])), float(R2[i]), float(R1[i])], "best six": [float(np.exp(six[j])), float(R2[j]), float(R1[j])],
                                  "D in band and both ratios in [2, 4.5]": [int(both.sum()), float(np.exp(six[k])) if k is not None else None]}
    say(f"3. {label}: best D-matched six {np.exp(six[i]):.3f} with R2 {R2[i]:.2f}, R1 {R1[i]:.2f}; best six {np.exp(six[j]):.3f} with R2 {R2[j]:.2f}, "
        f"R1 {R1[j]:.2f}; rows with D in band and both ratios in [2, 4.5]: {int(both.sum())}" + (f", best six {np.exp(six[k]):.3f}" if k is not None else ""))

# 4. the control's best row as a blend of main's two readings of DR
L = np.log(np.maximum(XC[..., :9], 1e-300)); nine = np.max(np.abs(L - T9), axis=-1)
i = np.unravel_index(np.argmin(nine), nine.shape)
b, c, r, p, h = i
re_t, im_t, a_, b_ = rbs.BASE[b]; cand = rbs.CANDS[c]; hor = rbs.HORS[h]
M = rbs.channels(re_t, im_t, a_, b_)
v1, v2, v3 = rbs.at(rbs.H1, re_t, im_t), rbs.at(rbs.H2, re_t, im_t), rbs.at(rbs.H3, re_t, im_t)
u2, u3 = v2 / np.linalg.norm(v2), v3 / np.linalg.norm(v3)
dirs = {"h2": u2, "h3": u3, **{f"c{ang}": (u2 + np.exp(1j * math.radians(ang)) * u3) / math.sqrt(2) for ang in (0, 90, 180, 270)}}
s = dirs[cand]; n1 = np.linalg.norm(v1); kap = rbs.RHO[r] * np.exp(1j * math.radians(15 * p)) * n1
e = np.conj(v1) / n1; proj = np.vdot(e, s) * e                       # s's component along conj(h1)
o_full = rbs.outputs(M, hor, rbs.S_of(v1) + kap * rbs.S_of(s), rbs.S_of(v1) + kap * rbs.S_of(s), "St_all")
o_proj = rbs.outputs(M, hor, rbs.S_of(v1) + kap * rbs.S_of(proj), rbs.S_of(v1) + kap * rbs.S_of(proj), "St_all")
f = lambda o: (math.exp(np.max(np.abs(np.log(np.array(o[:6])) - T6))), math.exp(np.max(np.abs(np.log(np.array(o[:9])) - T9))))
lam = kap * np.vdot(e, s) * n1 / n1                                  # S~(h1 + kap proj) = S(conj h1) + conj(lam) S(h1)
OUT["blend"] = {"row": {"base": rbs.BASE[b], "cand": cand, "rho": rbs.RHO[r], "phi_deg": 15 * int(p), "hor": hor},
                "full (six, nine)": f(o_full), "projected on conj(h1) (six, nine)": f(o_proj),
                "|blend coefficient| = |kappa <conj h1, s>| / |h1|": float(abs(kap * np.vdot(e, s)) / n1)}
say(f"4. the control's best nine-row {OUT['blend']['row']}: six, nine {f(o_full)[0]:.3f}, {f(o_full)[1]:.3f}; with s projected on conj(h1): "
    f"{f(o_proj)[0]:.3f}, {f(o_proj)[1]:.3f}; so the coupling is DR read as S~ plus {OUT['blend']['|blend coefficient| = |kappa <conj h1, s>| / |h1|']:.4f} "
    f"times DR read as S")
(HERE / "route_b_referee_checks.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "route_b_referee_checks_run.txt").write_text("\n".join(LOG) + "\n")
