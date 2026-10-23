#!/usr/bin/env python3
"""POST HOC, labelled (committed before its run; prompted by the owner's request to verify the framing).  Not a test.
What main's coarse measure (a worst factor) hides: at TICK_LINE_HIGGS's best nine-row (tick_line_compare.json) and at
the post hoc tau* (tick_line_optimum.json), each of the nine model values against the measured one in units of the
measurement's own sigma (the pinned files' sigmas at 3412bf09d, propagated in quadrature on each ratio, no theory error),
and the chi-square with the record's 10% allowance per quantity (sigma_ln = 0.10, GAP5's allowance), as B1698 and B1720
scored theirs.
    python3 -B precision_check.py      # writes precision_check.json"""
import json, math, subprocess, hashlib, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
m = json.loads(bd)["masses_GeV"]; v, s = m["value"], m["sigma"]; ck = json.loads(bc)["ckm_abs"]
names = ["m_c/m_t", "m_u/m_t", "m_s/m_b", "m_d/m_b", "m_mu/m_tau", "m_e/m_tau", "|V_us|", "|V_cb|", "|V_ub|"]
pairs = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
rel = [math.hypot(s[a] / v[a], s[b] / v[b]) for a, b in pairs] + \
      [ck["sigma"][0][1] / ck["value"][0][1], ck["sigma"][1][2] / ck["value"][1][2], ck["sigma"][0][2] / ck["value"][0][2]]
rows = {"TICK_LINE_HIGGS best nine-row (F_22, 0.825 + 2.725i, (2/5, 1/5), L_max)":
            json.loads((HERE / "tick_line_compare.json").read_text())["menu, S, c = 3"]["nine: model over measured"],
        "post hoc tau* (F_22, 0.8174 + 2.6977i, (2/5, 1/5), L_max)":
            json.loads((HERE / "tick_line_optimum.json").read_text())["F_22 on (2/5, 1/5), L_max"]["model over measured at tau*"]}
OUT = {"relative sigma of each measured quantity": dict(zip(names, rel))}
for label, mm in rows.items():
    dev = {n: math.log(x) / r for n, x, r in zip(names, mm, rel)}
    chi2 = sum((math.log(x) / 0.10) ** 2 for x in mm)
    OUT[label] = {"model over measured": dict(zip(names, mm)), "deviation in measurement sigmas (ln ratio / relative sigma)": dev,
                  "chi-square at a 10% allowance (9 quantities)": chi2}
(HERE / "precision_check.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
