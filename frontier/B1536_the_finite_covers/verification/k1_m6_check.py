#!/usr/bin/env python3
"""B1536 control K1 on M6, its comparison read again from the recorded histograms (disclosed in PREREGISTRATION section 6).

control_k1.py reads route R at the one-class members only (its route R loop runs when a member has one class), but its flag
'route R = banked' compared route R's histogram with the whole banked one, which on M6 also holds the two-class members' classes
(int, gen). On M2 and M3 every member has one class, so the flag was right there; on M6 it is false by construction. Here the
recorded histograms of k1_m6.json are compared as they should be:
  - route N's histogram with the banked one, every class;
  - route R's histogram with the banked one restricted to the one-class members' class 'c1';
  - no failure recorded (every reading's identities, and route N = route R reading by reading at the one-class members).
Nothing is recomputed.

    python3 k1_m6_check.py [--record]   ->  k1_m6_check.json"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    k = json.loads((HERE / "k1_m6.json").read_text())
    rec = k["per level"]["6"]
    banked = rec["banked histogram"]
    c1 = {key: v for key, v in banked.items() if key.startswith("('c1'")}
    out = {
        "subgroup order cap": rec["subgroup order cap"],
        "subgroups": rec["subgroups"], "banked subgroups": rec["banked subgroups"],
        "members": rec["members"], "banked members": rec["banked members"],
        "route N = banked (every class)": rec["route N histogram"] == banked,
        "route R = banked at the one-class members ('c1')": rec["route R histogram"] == c1,
        "failures": rec["failures"],
        "readings": {"route N": sum(rec["route N histogram"].values()), "route R": sum(rec["route R histogram"].values()),
                     "banked": sum(banked.values()), "banked at 'c1'": sum(c1.values())},
        "the recorded flag 'route R = banked' (whole banked histogram)": rec["route R = banked"],
    }
    out["holds"] = (out["route N = banked (every class)"] and out["route R = banked at the one-class members ('c1')"] and
                    not out["failures"])
    print(json.dumps(out, indent=1))
    if "--record" in sys.argv:
        (HERE / "k1_m6_check.json").write_text(json.dumps(out, indent=1) + "\n")
    return out


if __name__ == "__main__":
    main()
