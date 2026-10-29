#!/usr/bin/env python3
"""W180 post hoc 1 (labelled; written after the output 7f05eb5a0 was read, committed before its run): why H0 failed.

H0 compared the frozen frame F(48, Y = 48) with W178's stored six at Im tau 48 and missed on all 98 pairs, by 4e-4 to
0.51 in ln, while H3 (the double ratio D at Im tau 64-128) matched the true frame to 1e-13.  The rule's split says the
two differ only by rho_s, of order e^{-2 pi Im tau}.  This reads, at Im tau 48 on four pairs (the worst, two of the
largest, the G2 line, and the best):
  per sector and channel  lambda, W177's exact c_series, c_inf + B_s y from the rule's split, and their difference
  per feature             W178's stored six, W178's own point function now, and the frozen frame F(48, 48)
Read-out only; no cell.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_integer_lambda_limits_posthoc.py
"""
import contextlib
import io
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_integer_lambda_limits as W180      # noqa: E402  (W180's frozen frame and split, unchanged)
W178, T8, W93, W177 = W180.W178, W180.T8, W180.W93, W180.W177
mp = W177.mp
OUT = HERE / "the_integer_lambda_limits_posthoc.json"
PAIRS = ((("0", "1/6"), 0.125), (("0", "1/2"), 0.125), (("1/2", "1/5"), 0.125), (("1/2", "1/10"), 0.375))
Y = 48.0


def main():
    t0 = time.time()
    W178._init(str(ROOT))
    lines = W178._G["lines"]
    w178 = json.loads((HERE / "the_six_at_the_cusp.json").read_text(encoding="utf-8"))
    out = {"arc": "W180 post hoc 1", "Im tau": Y, "per pair": []}
    for key, x in PAIRS:
        k = [i for i, l in enumerate(lines) if (str(l[0]), str(l[1])) == key][0]
        a, b = lines[k]
        row = {"line": list(key), "x": x, "channels": []}
        p1, _p2 = W178.precisions(Y)
        with mp.workdps(p1):
            t = mp.mpc(mp.mpf(x), mp.mpf(Y))
            for sec, _rd in W178.READ:
                qL, qR = T8.charges(W93, sec)
                ub = (qL + qR) * (mp.mpf(a.numerator) / a.denominator * t + mp.mpf(b.numerator) / b.denominator)
                for s in T8.UNITS:
                    th = W178.W89TH[s]
                    if W178.theta_zero(th, lines[k], qL + qR):
                        row["channels"].append([sec, s, "theta-zero"])
                        continue
                    lam, _w = W177.lam_w(th, ub, t)
                    exact = W177.c_series(th, ub, t)
                    cinf, B = W180.split(th, ub, t)
                    row["channels"].append([sec, s, mp.nstr(lam, 12), mp.nstr(exact, 15), mp.nstr(cinf + B * Y, 15),
                                            mp.nstr(exact - (cinf + B * Y), 5)])
        stored = w178["per line"][k]["per Re tau"][W178.XS.index(x)]["six per height"]["48.0"]
        now = W178.point((k, x, Y, False))
        frozen = W180.point((k, x, Y, "frozen", Y))
        row["six: stored W178"] = stored
        row["six: W178 point now"] = now.get("six")
        row["six: frozen F(48, 48)"] = frozen.get("six")
        row["status now, frozen"] = [now.get("status"), frozen.get("status")]
        out["per pair"].append(row)
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name, "in", out["seconds"], "s")


if __name__ == "__main__":
    main()
