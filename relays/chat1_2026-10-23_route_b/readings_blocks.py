#!/usr/bin/env python3
"""POST HOC, labelled (an exploration toward step 2, the reading question; written after route_b_referee_checks was
read; committed before its run): why a split reading gives a near-permutation CKM in main's frame.
For DR at the sealed census's best rows (the ten best six-rows with S~ for every sector and the by-hand Clebsch 3, and
the ten best six-rows with D within 3 sigma of P-094 in the split reading with the by-hand Clebsch 3):
  - for each sector and each reading (S: the Higgs's components h; S~: their conjugates), the weights |U|^2 of the
    heavy, middle and light left singular vectors on main's three generation blocks (BLOCKS = [Q_J, Q_I, Q_K]);
  - the up and down ratios m2/m3, m1/m3 in each reading, against the data;
  - |V| for the four (up, down) reading pairings, and its distance from the nearest permutation matrix.
    python3 -B readings_blocks.py      # writes readings_blocks.json and readings_blocks_run.txt"""
import contextlib, hashlib, importlib.util, io, itertools, json, math, subprocess, pathlib
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
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
v = json.loads(bd)["masses_GeV"]["value"]
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
P094, SIG = 10.58, 0.11
LINES = [(float(Fr(a)), float(Fr(b)), f"({a}, {b})") for (_t, a, b) in tic.LINES]
LOG, OUT = [], {"rows": []}


def say(s):
    LOG.append(s); print(s, flush=True)


rows = [json.loads(l) for l in (SEL / "two_ingredients_census.jsonl").read_text().splitlines() if l.strip()]
sel = {"St-all best six": [], "split D-matched best six": []}
for r in rows:
    for hor in ("L_max", "L_2"):
        for key, (ru, rd) in (("St-all best six", ("St", "St")), ("split D-matched best six", ("St", "S"))):
            x = np.log(np.maximum(np.array(r[f"up|{hor}|{ru}"] + r[f"down|{hor}|{rd}"] + r[f"lep|{hor}|{rd}"], dtype=float), 1e-300))
            x[4] += math.log(3); x[5] -= math.log(3)
            if key.startswith("split") and abs(math.exp((x[4] - x[2]) + (x[3] - x[5])) - P094) > 3 * SIG:
                continue
            sel[key].append((float(np.max(np.abs(x - T6))), r["line"], r["Re_tau"], r["Im_tau"], hor))
PERMS = [np.eye(3)[list(p)] for p in itertools.permutations(range(3))]


def left(Y):
    U, s, _ = np.linalg.svd(Y)
    return U, s


for key, lst in sel.items():
    lst.sort()
    for w, k, re_t, im_t, hor in lst[:10]:
        a, b, name = LINES[k]
        M = rbs.channels(re_t, im_t, a, b)
        h = rbs.at(rbs.H1, re_t, im_t)
        Sx = {"S": rbs.S_of(h), "St": rbs.St(rbs.S_of(h))}
        rec = {"set": key, "six (by hand)": math.exp(w), "tau": [re_t, im_t], "line": name, "hor": hor, "blocks": {}, "ratios": {}, "V": {}}
        U = {}
        for sec in ("up", "down", "lep"):
            for rd, SS in Sx.items():
                Uv, s = left(B.coupling(SS, M[(sec, hor)]))
                U[(sec, rd)] = Uv
                rec["blocks"][f"{sec} {rd}"] = (np.abs(Uv) ** 2).T.round(3).tolist()        # rows: heavy, middle, light
                rec["ratios"][f"{sec} {rd}"] = [float(s[1] / s[0]), float(s[2] / s[0])]
        for ru in ("S", "St"):
            for rd in ("S", "St"):
                V = np.conj(U[("up", ru)][:, ::-1].T) @ U[("down", rd)][:, ::-1]
                A = np.abs(V)
                dist = min(float(np.max(np.abs(A - P))) for P in PERMS)
                rec["V"][f"{ru}|{rd}"] = {"|V|": A.round(3).tolist(), "distance to the nearest permutation": dist,
                                          "nearest is the identity": bool(np.argmin([np.max(np.abs(A - P)) for P in PERMS]) == 0)}
        OUT["rows"].append(rec)
# summary: the heavy left vector's weight on the Q_I block (index 1), by reading
for key in sel:
    recs = [r for r in OUT["rows"] if r["set"] == key]
    for sec in ("up", "down", "lep"):
        for rd in ("S", "St"):
            wI = [r["blocks"][f"{sec} {rd}"][0][1] for r in recs]
            say(f"{key}: {sec} read {rd}: the heavy state's weight on the Q_I block {min(wI):.3f}-{max(wI):.3f}")
    for pair in ("St|St", "S|S", "St|S", "S|St"):
        d = [r["V"][pair]["distance to the nearest permutation"] for r in recs]
        ident = sum(r["V"][pair]["nearest is the identity"] for r in recs)
        say(f"{key}: V with (up, down) read {pair}: distance to the nearest permutation {min(d):.3f}-{max(d):.3f}; nearest is the identity at {ident} of {len(recs)} rows")
    for sec in ("up", "down"):
        for rd in ("S", "St"):
            rr = [r["ratios"][f"{sec} {rd}"] for r in recs]
            say(f"{key}: {sec} read {rd}: m2/m3 {min(x[0] for x in rr):.2e}-{max(x[0] for x in rr):.2e}, m1/m3 {min(x[1] for x in rr):.2e}-{max(x[1] for x in rr):.2e}")
say(f"data: m_c/m_t {math.exp(T6[0]):.2e}, m_u/m_t {math.exp(T6[1]):.2e}, m_s/m_b {math.exp(T6[2]):.2e}, m_d/m_b {math.exp(T6[3]):.2e}")
(HERE / "readings_blocks.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "readings_blocks_run.txt").write_text("\n".join(LOG) + "\n")
