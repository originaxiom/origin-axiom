#!/usr/bin/env python3
"""READING TEST READ-OUTS (labelled; written after the cells were read, from committed outputs only; committed before
its run).  The read-outs READING_TEST_RESULT.md quotes that reading_test_cells.json does not hold:
  - the failure branches at the optima; the CKM's share of chi2 (min, median); minima by order, Im tau, Re tau,
    horocycle and alpha;
  - every S4 row and every S5 row with its line, tau, horocycle, chi2_nine, chi2_six, |h.h|, |V_ud|, |V_cb|,
    alpha_u3 - alpha_d3 and the chi2 terms above 21.67, and a classification of the S5 rows;
  - the post hoc denser search's changes by direction; C2 against the bar.
    python3 -B reading_test_readouts.py      # writes reading_test_readouts.json"""
import importlib.util, json, math, pathlib, sys
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
d = json.loads((HERE / "reading_test_rows.json").read_text()); tasks, rows = d["tasks"], d["rows"]
lines = json.loads((HERE / "reading_test_store_index.json").read_text())["lines"]
c2 = json.loads((HERE / "reading_test_c2.json").read_text()); ph = json.loads((HERE / "reading_test_posthoc.json").read_text())
NAMES = ["m_c/m_t", "m_u/m_t", "m_s/m_b", "m_d/m_b", "m_mu/m_tau", "m_e/m_tau", "|V_us|", "|V_cb|", "|V_ub|"]
main = [r for r in rows if tasks[r["p"]][1] != 0.8854]
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("ih", HERE / "inverse_higgs.py"); ih = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(ih)
sys.argv = _argv
SIGLN = ih.SIG


def lab(r):
    k = tasks[r["p"]][0]
    return {"line": f"({lines[k][1]}, {lines[k][2]})", "order": lines[k][0], "tau": tasks[r["p"]][1:], "hor": r["hor"]}


def terms(r):
    t = (np.log(np.array(r["model/data"])) / SIGLN) ** 2
    return {NAMES[i]: round(float(t[i]), 1) for i in range(9) if t[i] > 21.67}


def desc(r):
    V = r["|V|"]; au, ad = r["alpha_u3, alpha_d3"]
    return {**lab(r), "chi2_nine": round(r["chi2_nine"], 1), "chi2_six": round(r["chi2_six there"], 1), "|h.h|": round(r["|h.h|"], 4),
            "|V_ud|": V[0][0], "|V_cb|": V[1][2], "alpha_u3 - alpha_d3": round(au - ad, 4), "terms above 21.67": terms(r)}


out = {}
b1 = [r["|V|"][0][0] < 0.5 for r in main]; b2 = [r["|V|"][1][2] > 0.5 for r in main]
out["branches: |V_ud| < 0.5, |V_cb| > 0.5, both, neither"] = [sum(b1), sum(b2), sum(a and b for a, b in zip(b1, b2)), sum((not a) and (not b) for a, b in zip(b1, b2))]
ck = np.array([r["chi2 CKM share there"] for r in main])
out["CKM share at the optima: min, median"] = [float(ck.min()), float(np.median(ck))]
for key, f in (("order", lambda r: lab(r)["order"]), ("Im tau", lambda r: tasks[r["p"]][2]), ("Re tau", lambda r: tasks[r["p"]][1]),
               ("horocycle", lambda r: r["hor"]), ("alpha", lambda r: lines[tasks[r["p"]][0]][1])):
    g = {}
    for r in main:
        g.setdefault(str(f(r)), []).append(r["chi2_nine"])
    out[f"lowest chi2_nine by {key}"] = dict(sorted(((k, round(min(v), 1)) for k, v in g.items()), key=lambda kv: kv[1]))
s4 = [r for r in main if not (r["|V|"][0][0] < 0.5 or r["|V|"][1][2] > 0.5)]
s5 = [r for r in main if not (r["Lemma A |V_ud| bound"] < 0.933519 or r["Lemma B |V_tb| bound"] < 0.997723)]
out["S4 rows"] = [desc(r) for r in sorted(s4, key=lambda r: r["chi2_nine"])]
s4ids = {(r["p"], r["hor"]) for r in s4}
cls = {"also S4": 0, "order 12 far from null (|h.h| > 0.5), not S4": 0, "2-3 exchanged (|V_cb| > 0.85)": 0, "other": 0}
s5d = []
for r in sorted(s5, key=lambda r: r["chi2_nine"]):
    if (r["p"], r["hor"]) in s4ids:
        c = "also S4"
    elif r["|V|"][1][2] > 0.85:
        c = "2-3 exchanged (|V_cb| > 0.85)"
    elif r["|h.h|"] > 0.5 and lab(r)["order"] == "N=12":
        c = "order 12 far from null (|h.h| > 0.5), not S4"
    else:
        c = "other"
    cls[c] += 1; s5d.append({**desc(r), "class": c})
out["S5 classes"] = cls
out["S5 rows"] = s5d
P = ph["P2 rows"]
ch = [(q["dense min"] - q["scan min"]) / q["scan min"] for q in P]
within = [c for c in ch if abs(c) <= 1e-3]
out["post hoc P2: rows within 0.1%, of them lower / higher, largest |change| among them"] = [len(within), sum(c < -1e-12 for c in within), sum(c > 1e-12 for c in within),
                                                                                              float(max(abs(c) for c in within))]
low = [c for q, c in zip(P, ch) if q["in the 40 lowest"]]
out["post hoc P2: largest |change| on the 40 lowest rows"] = float(max(abs(c) for c in low))
out["C2 against the bar: noisy and noiseless searches ending below 21.67"] = [sum(o["found (noisy)"] < 21.67 for o in c2["C2 rows"]),
                                                                              sum(o["found (noiseless)"] < 21.67 for o in c2["C2 rows"])]
(HERE / "reading_test_readouts.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
print("written")
