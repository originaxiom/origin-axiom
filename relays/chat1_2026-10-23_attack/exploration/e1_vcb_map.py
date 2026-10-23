"""POST HOC exploration, labelled (reads the committed zero-free census; compares with data).
E1 V_cb's Higgs-independence across the census under aligned (null-led) readings; E2 where V_cb is near the data;
E3 the six for aligned two-Higgs pairs at those points (stored per-sector ratios); E4 summary."""
import json, math, subprocess, hashlib, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
ZF = ROOT / "relays/chat1_2026-10-23_zero_free_frame"
def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout
bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
m = json.loads(bd)["masses_GeV"]; v, s = m["value"], m["sigma"]; ck = json.loads(bc)["ckm_abs"]; C, CS = ck["value"], ck["sigma"]
PAIRS = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
T6 = np.log(np.array([v[a] / v[b] for a, b in PAIRS]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
REL = np.array([math.hypot(s[a] / v[a], s[b] / v[b]) for a, b in PAIRS] + [CS[0][1] / C[0][1], CS[1][2] / C[1][2], CS[0][2] / C[0][2]])
SIG = np.sqrt(REL ** 2 + 0.10 ** 2)
I = json.loads((ZF / "zero_free_census_index.json").read_text())
X = np.load(ZF / "zero_free_census.npz")["data"].astype(np.float64)       # point, dir, hor, field
DIRS = I["dirs"]; F = I["fields"]; fi = {f: i for i, f in enumerate(F)}
LEAD = {"dR": "St", "F_2": "St", "F_10": "St", "F_18": "St", "F_26": "St", "F_6": "S", "F_14": "S", "F_22": "S"}   # reading that makes it h0-led
NULLED = list(LEAD)
out = {}
# E1: V_cb across null-led directions in their aligned reading
vcb = np.stack([X[:, DIRS.index(d), :, fi[f"Vcb {LEAD[d]}|{LEAD[d]}"]] for d in NULLED], axis=-1)    # point, hor, dir
lv = np.log(vcb)
spread = lv.max(axis=-1) - lv.min(axis=-1)
for lo, hi in ((1.0, 2.0), (2.0, 2.5), (2.5, 3.0), (3.0, 3.5), (3.5, 4.01)):
    msk = np.array([lo <= t[2] < hi for t in I["tasks"]])
    out[f"E1 V_cb spread (max/min over the 8 null-led directions), Im tau {lo}-{hi}: median, 90th pct"] = [float(np.exp(np.median(spread[msk]))), float(np.exp(np.quantile(spread[msk], 0.9)))]
# the channel V_cb: median over the null-led directions
vch = np.exp(np.median(lv, axis=-1))                                     # point, hor
near = np.abs(np.log(vch / C[1][2])) < math.log(1.25)
out["E2 points x hors with channel V_cb within 25% of the data"] = int(near.sum())
out["E2 of"] = int(near.size)
# by line order and Im tau
tasks = I["tasks"]; lines = I["lines"]
ords = {}
for p in range(len(tasks)):
    for h in range(2):
        if near[p, h]:
            k = lines[tasks[p][0]]
            ords.setdefault(k[2] if isinstance(k, list) else str(k), 0)
print("line label example", lines[0])
# E3 the six for aligned pairs (up from du, down+lep from dd), c = 3
def sec(d, sec_, rd):
    return X[:, DIRS.index(d), :, fi[f"log10 {sec_} m2/m3 {rd}"]], X[:, DIRS.index(d), :, fi[f"log10 {sec_} m1/m3 {rd}"]]
best = []
for du in NULLED:
    u2, u1 = sec(du, "up", LEAD[du])
    for dd in NULLED:
        d2, d1 = sec(dd, "down", LEAD[dd]); l2, l1 = sec(dd, "lep", LEAD[dd])
        L6 = np.stack([u2, u1, d2, d1, l2 + math.log10(3), l1 - math.log10(3)], axis=-1) * math.log(10)
        chi6 = np.sum(((L6 - T6) / SIG[:6]) ** 2, axis=-1)
        # add V_cb channel term
        chiq = chi6 + ((np.log(vch) - T9[7]) / SIG[7]) ** 2
        for lab, arr in (("chi2_six", chi6), ("chi2_six + Vcb", chiq)):
            p, h = np.unravel_index(int(np.argmin(arr)), arr.shape)
            best.append((lab, du, dd, float(arr[p, h]), tasks[p], I["hors"][h], float(vch[p, h]), float(chi6[p, h])))
for lab in ("chi2_six", "chi2_six + Vcb"):
    rows = sorted([b for b in best if b[0] == lab], key=lambda b: b[3])[:8]
    out[f"E3 best aligned pairs by {lab}"] = [{"up": b[1], "down": b[2], "value": round(b[3], 2), "point": b[4], "line": lines[b[4][0]], "hor": b[5], "Vcb channel": round(b[6], 4), "chi2_six there": round(b[7], 2)} for b in rows]
print(json.dumps(out, indent=1, default=str))
