"""The big run's values, assembled before any data is read (main, 2026-11-14 night). Frame C as defined, with the exact
channel weight (Theorem 90's leading form, checked against the exact horoball norm to about 1e-5), the canonical end
(the horocycle of length 2), the read-out on the whole (B1928), in four declared options: the Higgs world W- (up S~,
down S, leptons S; the record's practice) or W+ (up S, down S~, leptons S~), and the measure (a) move count or (b) area.
Seven outputs per option, named by position: up m2/m3, up m1/m3, down m2/m3, down m1/m3, |V12|, |V23|, |V13|.
Errors: (a) the jackknife sampling error over 3000 words (the grid's interpolation, B1928's P1, is listed beside it);
(b) the spread between the end's two brackets above Im tau = 6. Writes BIG_RUN_VALUES.json and prints only its sha256."""
import json, hashlib, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
POS = ["up m2/m3", "up m1/m3", "down m2/m3", "down m1/m3", "|V12|", "|V23|", "|V13|"]
e = json.loads((HERE / "ergodic_both_worlds.json").read_text())
R, se = np.array(e["R_exact_weight"]), np.array(e["se_truncated"])          # se: the paired run's jackknife on the same words
a = json.loads((HERE / "area_measure.json").read_text())
sl = {"up|L_2|St": (0, 2), "up|L_2|S": (2, 4), "down|L_2|S": (4, 6), "down|L_2|St": (6, 8), "ckm|L_2|St|S": (8, 11), "ckm|L_2|S|St": (11, 14)}
W = {"W-": ("up|L_2|St", "down|L_2|S", "ckm|L_2|St|S"), "W+": ("up|L_2|S", "down|L_2|St", "ckm|L_2|S|St")}
pick = lambda v, ks: np.concatenate([np.array(v)[slice(*sl[k])] for k in ks])
opts = {}
for i, w in enumerate(("W-", "W+")):
    opts["%s|a (move count)" % w] = {"values": R[7 * i:7 * i + 7].tolist(), "error": se[7 * i:7 * i + 7].tolist(),
                                     "error_kind": "jackknife sampling, 3000 words of 40 letters"}
    bh, bt = pick(a["exact|held"], W[w]), pick(a["exact|trend"], W[w])
    opts["%s|b (area)" % w] = {"values": bh.tolist(), "error": np.abs(bt - bh).tolist(),
                               "error_kind": "the end above Im tau = 6, held against trended"}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
out = {"positions": POS, "options": opts,
       "frame": "frame C (docs/total_inputs_scoreboard.json) with the exact channel weight N = 2 pi L_2 + c_s - pi |a0|^2 e^{-2 L_2}",
       "inputs_from": {"fiber_grid_t90.json": sha(HERE / "fiber_grid_t90.json"), "ergodic_both_worlds.json": sha(HERE / "ergodic_both_worlds.json"),
                       "area_measure.json": sha(HERE / "area_measure.json")},
       "computed": "once, by main; second computations owed (agy-002, agy-exp)"}
p = HERE / "BIG_RUN_VALUES.json"; p.write_text(json.dumps(out, indent=1))
print("BIG_RUN_VALUES.json sha256", sha(p))
