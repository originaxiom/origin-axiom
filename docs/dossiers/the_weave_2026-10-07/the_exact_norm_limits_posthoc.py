#!/usr/bin/env python3
"""W181 post hoc 1 (labelled; written after the output e27737ca3 was read, committed before its run): are the cusp
limits trigonometric numbers of the line's order?

Reading W181's output showed limits that look like cosines at the line's denominator: on the 1/7 lines r = 2.8019,
1.4450 and 0.2470, near cos(2 pi/7)/cos(3 pi/7), cos(pi/7)/cos(2 pi/7) and cos(3 pi/7)/cos(pi/7); on the two G2 lines
D_inf = 6.313752, near cot(pi/20) = cos(pi/20)/cos(9 pi/20).  This tests one stated family on every accepted limit, from
the recorded numbers alone (no frame is computed):

  the family  |cos(j pi/M) / cos(k pi/M)|, M = 2 n with n the line's order lcm(den a, den b), 0 <= j, k <= M,
              cos(k pi/M) != 0, values in (0, 1e3)
  a match     relative deviation at most 1e-7 (the limits' own extrapolation spread is at most 3e-9 in ln)

and per value reports the best (j, k), its deviation, and the number of family members within 1e-7 (the family's size
is recorded per pair; with a few hundred members a chance match within 1e-7 is rare).  Read-outs also: the lines whose
D_inf differs between Re tau 1/8 and 3/8 by more than 1e-6.  No cell.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_exact_norm_limits_posthoc.py
"""
import json
import math
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_exact_norm_limits_posthoc.json"
REL = 1e-7


def family(M):
    out = []
    for j in range(M + 1):
        for k in range(M + 1):
            c = math.cos(k * math.pi / M)
            if abs(c) < 1e-12:
                continue
            v = abs(math.cos(j * math.pi / M) / c)
            if 0 < v < 1e3:
                out.append((v, j, k))
    return out


def best(value, fam):
    rel = [(abs(v - value) / value, j, k) for v, j, k in fam]
    rel.sort()
    hits = sum(1 for r, _j, _k in rel if r <= REL)
    r, j, k = rel[0]
    return {"value": value, "best (j, k)": [j, k], "relative deviation": r, "members within 1e-7": hits,
            "match": bool(r <= REL)}


def main():
    d = json.loads((HERE / "the_exact_norm_limits.json").read_text(encoding="utf-8"))
    rows, by_line = [], {}
    for r in d["per pair"]:
        if "D_inf" not in r:
            continue
        a, b = Fr(r["line"][0]), Fr(r["line"][1])
        n = math.lcm(a.denominator, b.denominator)
        M = 2 * n
        fam = family(M)
        r2, r1 = r["r2_inf, r1_inf (read-out)"]
        row = {"line": r["line"], "x": r["x"], "order n": n, "M": M, "family size": len(fam),
               "r2_inf": best(r2, fam), "r1_inf": best(r1, fam), "D_inf": best(r["D_inf"], fam)}
        rows.append(row)
        by_line.setdefault(tuple(r["line"]), {})[r["x"]] = r["D_inf"]
    out = {"arc": "W181 post hoc 1", "family": "|cos(j pi/M) / cos(k pi/M)|, M = 2 n", "relative tolerance": REL,
           "per pair": rows}
    for q in ("r2_inf", "r1_inf", "D_inf"):
        out[f"{q}: matched"] = sum(1 for w in rows if w[q]["match"])
        out[f"{q}: not matched (line, x, value)"] = [[w["line"], w["x"], w[q]["value"]] for w in rows
                                                      if not w[q]["match"]]
    out["pairs (of 62) with every one of r2, r1, D matched"] = sum(
        1 for w in rows if w["r2_inf"]["match"] and w["r1_inf"]["match"] and w["D_inf"]["match"])
    out["lines whose D_inf differs between the two Re tau (> 1e-6)"] = [
        [list(k), v] for k, v in by_line.items() if len(v) == 2 and abs(v[0.125] - v[0.375]) > 1e-6]
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
