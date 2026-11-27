#!/usr/bin/env python3
"""SM-C24's failing control (fam1-v1-unset-04): the card's check, "every pair whose a has a 5-part is aligned and
hierarchical, in the act's line's classes", applied to an input made wrong on purpose: the 48 pairs WITHOUT a 5-part,
read from the sealed rows. The check must reject them.
    python3 relays/claims/sm_refile/c24_control.py
Exit 1 with a last line "CONTROL FAILS:" when the check rejects the wrong input; 0 when it does not; 3 if invalid."""
import json, pathlib, sys
from collections import Counter
from fractions import Fraction as Fr
try:
    HERE = pathlib.Path(__file__).resolve().parent
    ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
    d = json.loads((ROOT / "relays" / "sm_c24" / "c24_results.json").read_text())["rows"]
    K = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")
    key = lambda x: tuple(None if x[k] is None else round(x[k] * 60) for k in K)
    hier = lambda x: x["up_m2m3"] >= 0.1 and x["down_m2m3"] >= 0.1 and x["up_m1m3"] >= 0.2 and x["down_m1m3"] >= 0.2
    wrong = [x for x in d if Fr(x["a"]).denominator % 5 != 0]
    line = set(key(x["r4050"]) for x in d if x["on_line"])
    passes = all(x["r4050"]["diag"] >= 0.9 and hier(x["r4050"]) for x in wrong) and set(key(x["r4050"]) for x in wrong) <= line
except Exception as e:
    print("CONTROL INVALID: %s" % type(e).__name__); sys.exit(3)
print("the 48 pairs without a 5-part pass the check: %s" % passes)
if not passes:
    print("CONTROL FAILS: as it must, the check rejects the pairs whose a has no 5-part"); sys.exit(1)
print("CONTROL DID NOT FAIL: the check accepted the wrong input"); sys.exit(0)
