#!/usr/bin/env python3
"""EXPLORATORY read-out, labelled (committed before bl_line_scan.jsonl was read): what the B - L line does in main's
frame, at each of the three points, with no by-hand Clebsch.
  1. the first-order check at the tick's exact d = e line: the slopes of the leptons' and the down quarks' log m2/m3
     and log m1/m3 in a' and b' at w' = 0 (central differences +-0.02), and their ratios;
  2. for the model S~ in every sector (the sealed reading) and for main's readings (up S~, down and leptons S): the
     six-ratio and nine-target worst factors over the w' grid, the best w' and the double ratio D there;
  3. the w' where D is within 3 sigma of P-094 (10.58 +- 0.11, Antusch, Hinze and Saad), and the best six among them.
Targets: Huang-Zhou 2021 at M_Z and PDG 2025's three moduli, from the record's pinned files at main's 3412bf09d.
    python3 -B bl_line_readout.py      # writes bl_line_readout.json and bl_line_readout_run.txt"""
import hashlib, json, math, subprocess, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())


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
rows = [json.loads(l) for l in (HERE / "bl_line_scan.jsonl").read_text().splitlines() if l.strip()]
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


def vec(r, hor, cu, cd, cl):
    vals = r[f"up|{hor}|{cu}"] + r[f"down|{hor}|{cd}"] + r[f"lep|{hor}|{cl}"] + r[f"ckm|{hor}|{cu}|{cd}"][:3]
    return np.log(np.maximum(np.array(vals, dtype=float), 1e-300))


def dratio(x):
    return math.exp((x[4] - x[2]) + (x[3] - x[5]))


for point in ("six_best", "nine_best", "tick_d_eq_e"):
    R = {(r["a2"], r["b2"]): r for r in rows if r["point"] == point}
    say(f"== {point}: {len(R)} grid points")
    OUT[point] = {}
    hor0 = "L_2" if point != "tick_d_eq_e" else "L_max"
    # 1. first-order slopes at w' = 0
    sl = {}
    for sec in ("down", "lep"):
        for rd in ("S", "St"):
            for idx, nm in ((0, "m2/m3"), (1, "m1/m3")):
                for ax, (p, m) in (("a'", ((0.02, 0.0), (-0.02, 0.0))), ("b'", ((0.0, 0.02), (0.0, -0.02)))):
                    if p in R and m in R:
                        d = (math.log(max(R[p][f"{sec}|{hor0}|{rd}"][idx], 1e-300)) - math.log(max(R[m][f"{sec}|{hor0}|{rd}"][idx], 1e-300))) / 0.04
                        sl[(sec, rd, nm, ax)] = d
    for rd in ("S", "St"):
        for nm in ("m2/m3", "m1/m3"):
            for ax in ("a'", "b'"):
                dd, dl = sl.get(("down", rd, nm, ax)), sl.get(("lep", rd, nm, ax))
                if dd is not None and dl is not None:
                    say(f"  slope of log {nm} in {ax} ({rd}, {hor0}): down {dd:+.4f}, leptons {dl:+.4f}, ratio {dl / dd if abs(dd) > 1e-12 else float('nan'):+.3f}")
    OUT[point]["slopes"] = {"|".join(k): val for k, val in sl.items()}
    # 2. and 3.
    for label, (cu, cd, cl) in (("S~ for every sector", ("St", "St", "St")), ("main's readings", ("St", "S", "S"))):
        recs = []
        for (a2, b2), r in R.items():
            for hor in ("L_max", "L_2"):
                x = vec(r, hor, cu, cd, cl)
                recs.append({"a2": a2, "b2": b2, "hor": hor, "six": float(np.exp(np.max(np.abs(x[:6] - T6)))),
                             "nine": float(np.exp(np.max(np.abs(x - T9)))), "D": dratio(x), "R2": math.exp(x[4] - x[2]), "R1": math.exp(x[3] - x[5]),
                             "mm": np.exp(x - T9).tolist(), "J": r[f"ckm|{hor}|{cu}|{cd}"][3]})
        base = [q for q in recs if q["a2"] == 0.0 and q["b2"] == 0.0]
        b6 = min(recs, key=lambda q: q["six"]); b9 = min(recs, key=lambda q: q["nine"])
        near = [q for q in recs if abs(q["D"] - P094) <= 3 * SIG]
        b6n = min(near, key=lambda q: q["six"]) if near else None
        OUT[point][label] = {"baseline": base, "best_six": b6, "best_nine": b9, "n_D_within_3sigma": len(near), "best_six_with_D_within_3sigma": b6n}
        say(f"  [{label}] baseline w'=0: " + "; ".join(f"{q['hor']} six {q['six']:.2f} nine {q['nine']:.2f} D {q['D']:.2f}" for q in base))
        say(f"  [{label}] best six {b6['six']:.3f} at w' = ({b6['a2']}, {b6['b2']}) {b6['hor']}, D {b6['D']:.2f}; model/measured {[round(z, 2) for z in b6['mm'][:6]]}")
        say(f"  [{label}] best nine {b9['nine']:.3f} at w' = ({b9['a2']}, {b9['b2']}) {b9['hor']}, D {b9['D']:.2f}, J {b9['J']:.1e}; model/measured {[round(z, 2) for z in b9['mm']]}")
        if b6n:
            say(f"  [{label}] {len(near)} rows with D within 3 sigma of P-094; best six among them {b6n['six']:.3f} at w' = ({b6n['a2']}, {b6n['b2']}) {b6n['hor']} (D {b6n['D']:.2f}); nine there {b6n['nine']:.2f}")
        else:
            say(f"  [{label}] no row with D within 3 sigma of P-094")
(HERE / "bl_line_readout.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "bl_line_readout_run.txt").write_text("\n".join(LOG) + "\n")
