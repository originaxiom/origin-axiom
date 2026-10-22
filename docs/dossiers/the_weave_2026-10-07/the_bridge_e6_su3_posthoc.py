#!/usr/bin/env python3
"""W134, POST HOC (after the one run's read-out, which found E0 and E1 failed on two instrument checks). Nothing here
was in the rule.

  Q1  E0's A2: the roots in the span of e1 - e2 and e2 - e3 (x1 + x2 + x3 = 0, x4..x8 = 0), not every root on the
      first three coordinates (which adds the six +-(e_i + e_j)); then the other roots' A2 weights
  Q2  E1's identification: W46's T (the index's) against W123's rho up to a change of basis: the intertwiners X with
      X rho_W123(g) = rho_W46(g) X for g = S, T (the null space of the stacked linear system), and whether one is
      invertible; the traces of S, T and ST

    python3 -B the_bridge_e6_su3_posthoc.py      # writes the_bridge_e6_su3_posthoc.json beside itself
"""
import contextlib
import io
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_bridge_e6_su3 as W134  # noqa: E402

OUT = HERE / "the_bridge_e6_su3_posthoc.json"


def Q1():
    roots = W134.e8_roots()
    alpha, beta = (2, -2, 0, 0, 0, 0, 0, 0), (0, 2, -2, 0, 0, 0, 0, 0)
    lab = {r: (W134.ip(r, alpha), W134.ip(r, beta)) for r in roots}
    e6 = [r for r in roots if lab[r] == (0, 0)]
    a2 = [r for r in roots if all(r[k] == 0 for k in range(3, 8)) and r[0] + r[1] + r[2] == 0]
    rest = [r for r in roots if r not in set(e6) | set(a2)]
    ws = [(1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0)]
    counts = {str(w): sum(1 for r in rest if lab[r] == w) for w in ws}
    off = [r for r in roots if all(r[k] == 0 for k in range(3, 8)) and r[0] + r[1] + r[2] != 0]
    return {"A2's roots": len(a2), "the other roots": len(rest), "their weights": counts,
            "the run's extra six, +-(e_i + e_j), and their weights": sorted(str(lab[r]) for r in off),
            "holds": len(a2) == 6 and len(rest) == 162 and set(counts.values()) == {27}}


def Q2():
    R = W134.the_reps()
    rS, rT = W134.rho_exact()
    num = lambda M: np.array([[complex(x) for x in row] for row in M.evalf().tolist()])
    A = {"S": num(rS), "T": num(rT)}
    B = {"S": np.array(R["T"][0], dtype=complex), "T": np.array(R["T"][1], dtype=complex)}
    rows = []
    for g in ("S", "T"):                                   # X A - B X = 0, X row-major
        rows.append(np.kron(np.eye(3), A[g].T) - np.kron(B[g], np.eye(3)))
    M = np.vstack(rows)
    u, s, vh = np.linalg.svd(M)
    null = [vh[k].conj().reshape(3, 3) for k in range(len(s)) if s[k] < 1e-9] + [
        vh[k].conj().reshape(3, 3) for k in range(len(s), 9)]
    dets = [abs(np.linalg.det(X)) for X in null]
    tr = lambda X: [round(complex(np.trace(X)).real, 9), round(complex(np.trace(X)).imag, 9)]
    traces = {"W123": {g: tr(A[g]) for g in ("S", "T")} | {"ST": tr(A["S"] @ A["T"])},
              "W46": {g: tr(B[g]) for g in ("S", "T")} | {"ST": tr(B["S"] @ B["T"])}}
    return {"intertwiners (null dimension)": len(null), "the largest |det X|": float(max(dets)) if dets else 0.0,
            "traces": traces, "max |entry difference| (the run's equality check)": float(
                max(np.abs(A[g] - B[g]).max() for g in ("S", "T"))),
            "equivalent (an invertible intertwiner)": bool(dets and max(dets) > 1e-6)}


def main():
    out = {"arc": "W134", "status": "POST HOC, after the read-out", "Q1": Q1(), "Q2": Q2()}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
