"""(a) Independent read-out of B1825 run.json + per-observable decomposition at the least-chi2 address,
using main's own evaluator (B1821 cm_zero_line.rows_at) and main's target data files (B1741's sources) and sigma file.
Also dumps the full Yukawa matrices / 3x3 CKM at that point for (c)."""
import json, math, pathlib, sys, contextlib, io, time
from fractions import Fraction as Fr
import numpy as np

ROOT = pathlib.Path("/Users/dri/.gemini/antigravity/scratch/origin-axiom-independent-audit")
OUT = pathlib.Path(__file__).resolve().parent
run = json.loads((ROOT / "frontier/B1825_step_b_the_nine_from_one_address/verification/run.json").read_text())
print("run.json S:", json.dumps(run["S"], indent=0))
print("K:", {k: run["K"][k] for k in ("L_six", "C_six", "bits_CKM", "C_ten", "choice", "grade", "converged")})
print("CKM:", run["CKM"]); print("legs:", run["legs"]); print("reading:", run["reading"])
print("C_six+bits_CKM - C_ten =", run["K"]["C_six"] + run["K"]["bits_CKM"] - run["K"]["C_ten"])

# targets from the raw data files (same sha-pinned files B1741 compare.py reads)
DATA = ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"
CKMDATA = ROOT / "frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json"
v = json.loads(DATA.read_text())["masses_GeV"]["value"]; C = json.loads(CKMDATA.read_text())["ckm_abs"]["value"]
T = np.log(np.array([v["c"]/v["t"], v["u"]/v["t"], v["s"]/v["b"], v["d"]/v["b"], v["mu"]/v["tau"], v["e"]/v["tau"],
                     C[0][1], C[1][2], C[0][2], 3.12e-5]))
sig = np.array(json.loads((ROOT / "scripts/stepb/sigma/SIGMA_ONLY.json").read_text())["sigma_natural_log"])
shift = np.zeros(10); shift[4], shift[5] = math.log(3), -math.log(3)     # c = 3 (stepb_core.c_shift)
names = ["c/t", "u/t", "s/b", "d/b", "mu/tau", "e/tau", "|V_us|", "|V_cb|", "|V_ub|", "|J|"]

sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
t0 = time.time()
import cm_zero_line as Z
M = Z.mods(); print("mods() load s:", round(time.time() - t0, 1))
tau = complex(*run["S"]["address"]["tau"]); line = (Fr(3, 8), Fr(3, 8))
rows = Z.rows_at(tau, line)
row = [r for r in rows if r["direction"] == "DR" and r["radius"] == "L_2" and r["reading"] == "S~S~S"][0]
f = np.log(np.array([row["up"][1], row["up"][0], row["down"][1], row["down"][0], row["lepton"][1], row["lepton"][0], *row["V"], abs(row["J"])]))
z = (f + shift - T) / sig
res = {"tau": [tau.real, tau.imag], "chi2_ten_fresh": float(z @ z), "chi2_nine_fresh": float(z[:9] @ z[:9]),
       "per_obs": {n: {"model": float(math.exp(fi + si)), "target": float(math.exp(ti)), "z": float(zi), "z2": float(zi*zi)}
                   for n, fi, si, ti, zi in zip(names, f, shift, T, z)}}
print(json.dumps(res, indent=1))
# best over the 192 rows at this exact tau (node check)
best = []
for r in rows:
    if not r["V defined"]: continue
    ff = np.log(np.maximum(np.array([r["up"][1], r["up"][0], r["down"][1], r["down"][0], r["lepton"][1], r["lepton"][0], *r["V"], abs(r["J"])]), 1e-300))
    zz = (ff + shift - T) / sig; best.append((float(zz @ zz), r["direction"], r["radius"], r["reading"]))
best.sort(); res["best_rows_at_tau"] = best[:5]; print("best rows at this tau:", best[:5])

# full Yukawas & CKM at the address, rebuilt from B (b1656_funcs) primitives -- same recipe as rows_at
B = M["B"]; Lmax, L2 = Z.radii(tau); a = Z.direction("DR", tau)
ch = {}
for sn, ql, qr in Z.SECTORS:
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R); ch[sn] = (R, c)
Ys = {}
for (sn, ql, qr), rr in zip(Z.SECTORS, (1, 1, 0)):
    R, c = ch[sn]
    Sm = a[0]*B.QI + a[1]*B.QJ + a[2]*B.QK
    if rr: Sm = B.EPS @ Sm.conj() @ B.EPS.T
    u = {k: (math.sqrt(2*math.pi*L2 + c[k])*R[k] if c[k] is not None and 2*math.pi*L2 + c[k] > 0 else 0) for k in B.UNITS}
    Ys[sn] = (B.coupling(Sm, B.weighted_M(u)), Sm, u)
np.save(OUT / "a_point_yukawas.npy", {k: v[0] for k, v in Ys.items()}, allow_pickle=True)
json.dump({"tau": [tau.real, tau.imag], "dir": [complex(x).real for x in a] + [complex(x).imag for x in a],
           "u": {sn: {k: [complex(vv).real, complex(vv).imag] for k, vv in Ys[sn][2].items()} for sn in Ys},
           "c": {sn: {k: ch[sn][1][k] for k in ch[sn][1]} for sn in ch},
           "R": {sn: {k: [ch[sn][0][k].real, ch[sn][0][k].imag] for k in ch[sn][0]} for sn in ch}},
          open(OUT / "a_point_inputs.json", "w"), indent=1)
json.dump(res, open(OUT / "a_b1825_point.json", "w"), indent=1)
