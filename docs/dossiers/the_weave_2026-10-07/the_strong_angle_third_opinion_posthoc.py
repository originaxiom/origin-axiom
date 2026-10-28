#!/usr/bin/env python3
"""W168, POST HOC (labelled; written after W168's output was read, committed before its one run): theta_Y, theta_H,
theta_M and J at the four rows of chat1's read-out table, on this seat's instrument.  W168's own R used B1749's best
row (0.666666667 + 3.0550505i); chat1's table uses B1749's (2/5, 1/2) at 0.605263158 + 3.0258581i.  Nothing is graded.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_strong_angle_third_opinion_posthoc.py
"""
import contextlib
import io
import json
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_strong_angle_third_opinion as W68   # noqa: E402  (W168's instrument, unchanged)
T8 = W68.T8
OUT = HERE / "the_strong_angle_third_opinion_posthoc.json"


def main():
    root = T8.repo_root()
    col = T8.L_column({T8.COLUMN: T8.git_bytes(root, W68.REV, T8.COLUMN)})
    W93, W89 = T8.own_modules(root)
    rows = [("B1726's (2/5, 1/2)", (Fr(2, 5), Fr(1, 2)), complex(0.55, 3.05)),
            ("B1749's (2/5, 1/2), chat1's row", (Fr(2, 5), Fr(1, 2)), complex(0.605263158, 3.0258580889584423)),
            ("B1786's (2/5, 23/30)", (Fr(2, 5), Fr(23, 30)), complex(0.269230769, 3.037487672558812)),
            ("its mirror (2/5, 5/6)", (Fr(2, 5), Fr(5, 6)), complex(0.730769231, 3.037487672558812))]
    out = {"arc": "W168", "status": "POST HOC (labelled), one run", "rows": []}
    for name, ln, tau in rows:
        p = W68.theta_Y_at(W93, W89, ln, tau, "dR", "L_max", col)
        out["rows"].append({"row": name, "tau": [tau.real, tau.imag],
                            "theta_Y / pi": W68.wrap(p["Y"]) / math.pi, "theta_H / pi": W68.wrap(p["H"]) / math.pi,
                            "theta_M / pi": W68.wrap(p["M"]) / math.pi, "J": p["J"]})
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print("done", len(out["rows"]))


if __name__ == "__main__":
    main()
