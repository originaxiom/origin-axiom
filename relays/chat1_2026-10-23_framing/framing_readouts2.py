#!/usr/bin/env python3
"""POST HOC read-outs for the framing note, labelled (written after framing_readouts.json was read; committed before
their own run).  Not tests.
  G1  main's DR in its split reading (up S~, down and leptons S) with c = 3 on ZERO_FREE_HOLOMORPHIC's grid: the rows
      whose chi2_six is below PRECISION_BAR's 16.75 (location, model over measured, the three |V|, J), and the same
      rows read S~ in every sector and S in every sector (the stored fields);
  G2  at the best of them, main's frame recomputed: each sector's heaviest and lightest left singular vectors, as
      weights on the generations' blocks (QJ, QI, QK), for up read S~, up read S, down read S and down read S~.
    python3 -B framing_readouts2.py      # writes framing_readouts2.json"""
import contextlib, hashlib, importlib.util, io, json, math, subprocess, sys, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
ZF = HERE.parent / "chat1_2026-10-23_zero_free_frame"


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
m = json.loads(bd)["masses_GeV"]; v, s = m["value"], m["sigma"]; ck = json.loads(bc)["ckm_abs"]; C, CS = ck["value"], ck["sigma"]
PAIRS = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
T6 = np.log(np.array([v[a] / v[b] for a, b in PAIRS]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
REL = np.array([math.hypot(s[a] / v[a], s[b] / v[b]) for a, b in PAIRS] + [CS[0][1] / C[0][1], CS[1][2] / C[1][2], CS[0][2] / C[0][2]])
SIG = np.sqrt(REL ** 2 + 0.10 ** 2)
I = json.loads((ZF / "zero_free_holomorphic_index.json").read_text())
X = np.load(ZF / "zero_free_holomorphic.npz")["data"].astype(np.float64)
Y = X[:, I["dirs"].index("dR")]                                    # point, hor, field
OUT = {}


def nine_of(Yf, ru, rd):
    iu = {"S": 0, "St": 2}[ru]; idn = {"S": 4, "St": 6}[rd]; il = {"S": 8, "St": 10}[rd]
    k = {("S", "S"): 12, ("S", "St"): 16, ("St", "S"): 20, ("St", "St"): 24}[(ru, rd)]
    L = np.concatenate([Yf[..., iu:iu + 2], Yf[..., idn:idn + 2], Yf[..., il:il + 2]], axis=-1) * math.log(10)
    L[..., 4] += math.log(3); L[..., 5] -= math.log(3)
    return np.concatenate([L, np.log(np.maximum(Yf[..., k:k + 3], 1e-300))], axis=-1), Yf[..., k + 3]


L9, J = nine_of(Y, "St", "S")
chi6 = np.sum(((L9[..., :6] - T6) / SIG[:6]) ** 2, axis=-1)
hits = sorted(zip(*np.where(chi6 < 16.75)), key=lambda ph: chi6[ph])
G1 = []
for p, h in hits:
    k, re_t, im_t = I["tasks"][p]
    row = {"tau": [re_t, im_t], "line": I["lines"][k], "hor": I["hors"][h], "chi2_six": float(chi6[p, h]),
           "split: model over measured (six, then |V_us|, |V_cb|, |V_ub|)": np.exp(L9[p, h] - T9).round(3).tolist(),
           "split: |V|": np.exp(L9[p, h, 6:]).round(4).tolist(), "split: J": float(J[p, h])}
    for ru, rd, lab in (("St", "St", "S~ in every sector"), ("S", "S", "S in every sector")):
        L9b, Jb = nine_of(Y[p, h], ru, rd)
        row[f"{lab}: model over measured"] = np.exp(L9b - T9).round(3).tolist()
        row[f"{lab}: chi2_six"] = float(np.sum(((L9b[:6] - T6) / SIG[:6]) ** 2))
    G1.append(row)
OUT["G1 DR split, c = 3, rows below the six's bar (ZERO_FREE_HOLOMORPHIC's grid)"] = G1

# G2 the heaviest and lightest left vectors at the best G1 row, recomputed in main's frame
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py")
zfc = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(zfc)
rbs, B = zfc.rbs, zfc.B
best = G1[0]
k = I["lines"].index(best["line"]); a, b, lab = zfc.LINES[k]
assert lab == best["line"], (lab, best["line"])
re_t, im_t = best["tau"]
Mch = rbs.channels(re_t, im_t, a, b)
vd = zfc.direction("dR", re_t, im_t)
S = rbs.S_of(vd); St = rbs.St(S)
BL = ["QJ", "QI", "QK"]
G2 = {"point": best["tau"], "line": best["line"], "hor": best["hor"],
      "Higgs components (abs)": np.abs(vd).round(4).tolist(), "Higgs components (deg)": np.degrees(np.angle(vd)).round(1).tolist(),
      "|v.v| / |v|^2": float(abs(np.dot(vd, vd)) / np.linalg.norm(vd) ** 2)}
for sec in ("up", "down"):
    for rn, SS in (("S", S), ("S~", St)):
        Ym = B.coupling(SS, Mch[(sec, best["hor"])])
        U, sv, _ = np.linalg.svd(Ym)
        G2[f"{sec} read {rn}: m2/m3, m1/m3"] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
        G2[f"{sec} read {rn}: heaviest left vector on {BL}"] = (np.abs(U[:, 0]) ** 2).round(4).tolist()
        G2[f"{sec} read {rn}: middle left vector on {BL}"] = (np.abs(U[:, 1]) ** 2).round(4).tolist()
        G2[f"{sec} read {rn}: lightest left vector on {BL}"] = (np.abs(U[:, 2]) ** 2).round(4).tolist()
OUT["G2 the left vectors at the best G1 row"] = G2
(HERE / "framing_readouts2.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
