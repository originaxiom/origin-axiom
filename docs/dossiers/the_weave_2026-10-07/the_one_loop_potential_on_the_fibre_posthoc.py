"""W59, POST HOC (written after W59's one run and its read-out; labelled; W59's JSON is unchanged). K4 failed as worded:
at omega the three nonzero 2-torsion points came out as shallow local minima, not saddles, with six saddles between
them; at tau1 two extra saddles sit next to (1/2, 0). The global minima and maxima were as predicted. A read-out also
had a bug: its Higgs lines were computed for every local minimum, and are right only for the two 3-torsion ones.

  PH1  the truncation: the Hessian's eigenvalues at the four 2-torsion points and the 3-torsion points, at omega and at
       tau1, for N = 48, 96, 160 and 240; and the stationary points again at N = 96 (a 36 x 36 grid of starts)
  PH2  the Higgs alone at omega, corrected: the lines w with 3w at the two global minima only, and the twists each
       Standard Model field sees there

Run: python3 the_one_loop_potential_on_the_fibre_posthoc.py  ->  the_one_loop_potential_on_the_fibre_posthoc.json.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_one_loop_potential_on_the_fibre as OP  # noqa: E402  (W59: the joint potential, the search, the charges)

OUT = HERE / "the_one_loop_potential_on_the_fibre_posthoc.json"
POINTS = {"0": (0.0, 0.0), "(1/2, 0)": (0.5, 0.0), "(0, 1/2)": (0.0, 0.5), "(1/2, 1/2)": (0.5, 0.5),
          "(1/3, 1/3)": (1 / 3, 1 / 3), "(2/3, 2/3)": (2 / 3, 2 / 3)}


def ph1():
    out = {}
    for name, t in (("omega", OP.OMEGA), ("tau1", OP.TAU1)):
        rows = {}
        for N in (48, 96, 160, 240):
            V = OP.Joint(t, 1, N)
            rows[str(N)] = {k: {"value": V.value(p), "Hessian eigenvalues": np.linalg.eigvalsh(V.hess(p)).tolist()}
                            for k, p in POINTS.items()}
        pts = OP.stationary(OP.Joint(t, 1, 96), grid=36)
        out[name] = {"at the symmetric points, by truncation N": rows,
                     "the stationary points at N = 96 (36 x 36 starts)": pts}
    return out


def ph2():
    lines = []
    for num in (1, 2):
        for i in range(3):
            for j in range(3):
                w = ((Fraction(num, 9) + Fraction(i, 3)) % 1, (Fraction(num, 9) + Fraction(j, 3)) % 1)
                seen = {f: [str((q * c) % 1) for c in w] for f, q in OP.CHARGES.items()}
                lines.append({"w": [str(c) for c in w], "the twist each field sees (q w mod 1)": seen,
                              "d^c and e^c see different twists": seen["d^c"] != seen["e^c"]})
    return {"3w at the global minima (1/3, 1/3) and (2/3, 2/3): the 18 lines w": lines,
            "d^c and e^c differ on every line": all(x["d^c and e^c see different twists"] for x in lines)}


def main():
    out = {"status": "W59 post hoc: K4's fine structure against the truncation; the Higgs read-out corrected "
                     "(labelled; W59's JSON unchanged)",
           "PH1": ph1(), "PH2": ph2()}
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: "..." for k in out}, indent=1))


if __name__ == "__main__":
    main()
