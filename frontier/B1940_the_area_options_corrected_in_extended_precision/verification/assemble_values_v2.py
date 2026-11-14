"""The big run's values, corrected (P-853; main, 2026-11-14, before the look). B1932's move-count options are carried
unchanged (their read-out grid stops at height 6, where the double-precision frame is sound; agy-exp's X-EXACT-W agrees
with them). The area options are recomputed: B1932's construction (below height 6 its grid and quadrature; above it the
x-average over five columns, the trapezoid in height, the end in two brackets, the tail beyond 45 held), with F-bar above
height 6 from the extended-precision frame (frame_mp.py) on a refined set of heights.
Values: the held bracket on the refined heights. Error: the end's two brackets and the change from B1932's heights to the
refined ones, in quadrature. Writes BIG_RUN_VALUES_v2.json beside B1932's file, which stays in the record; prints only
its sha256."""
import json, hashlib, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
OLD = next((ROOT / "frontier").glob("B1932_*")) / "verification" / "BIG_RUN_VALUES.json"
OLD_SHA = "df1c9bee002ecf5eeb7f1f360e497a5c091bf092cdbaa499352ea3201d02b536"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(OLD) == OLD_SHA
V = json.loads(OLD.read_text()); a = json.loads((HERE / "area_measure_mp.json").read_text())
sl = {"up|L_2|St": (0, 2), "up|L_2|S": (2, 4), "down|L_2|S": (4, 6), "down|L_2|St": (6, 8), "ckm|L_2|St|S": (8, 11), "ckm|L_2|S|St": (11, 14)}
W = {"W-": ("up|L_2|St", "down|L_2|S", "ckm|L_2|St|S"), "W+": ("up|L_2|S", "down|L_2|St", "ckm|L_2|S|St")}
pick = lambda v, ks: np.concatenate([np.array(v)[slice(*sl[k])] for k in ks])
opts = {}
for w in ("W-", "W+"):
    opts["%s|a (move count)" % w] = V["options"]["%s|a (move count)" % w]
    held, trend, held1 = pick(a["exact|held|H2"], W[w]), pick(a["exact|trend|H2"], W[w]), pick(a["exact|held|H1"], W[w])
    opts["%s|b (area)" % w] = {"values": held.tolist(), "error": np.sqrt((trend - held) ** 2 + (held1 - held) ** 2).tolist(),
                               "error_kind": "the end above Im tau = 6 (held against trended) and the height quadrature (B1932's heights against the refined ones), in quadrature; F-bar above height 6 in extended precision"}
out = {"positions": V["positions"], "options": opts, "frame": V["frame"],
       "corrects": {"file": "B1932's BIG_RUN_VALUES.json", "sha256": OLD_SHA, "what": "the area options (P-853): the double-precision frame lost the first generation and the mixing above Im tau about 11"},
       "inputs_from": {"B1932 move-count options": OLD_SHA, "area_measure_mp.json": sha(HERE / "area_measure_mp.json")},
       "computed": "the move-count options once by main and recomputed independently by agy-exp (X-EXACT-W); the area options once by main in extended precision, their second computation owed (agy-002's A2-CANON-T90 or agy-exp's X-MEASURE)"}
p = HERE / "BIG_RUN_VALUES_v2.json"; p.write_text(json.dumps(out, indent=1))
print("BIG_RUN_VALUES_v2.json sha256", sha(p))
