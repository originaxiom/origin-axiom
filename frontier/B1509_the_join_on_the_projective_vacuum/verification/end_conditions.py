"""B1509, post-run (computed after extension_index_run.txt, from its data): the 10'-count of W1 under every end condition.

For a flat V on a 3-manifold with torus boundary, an end condition is a subspace W of H^1(T; V), with its annihilator W^perp in
H^1(T; V*).  The count N_W(V) = dim{x in H^1(M;V): x|T in W} - dim{y in H^1(M;V*): y|T in W^perp} equals
    N_W = dim W - h0(T; V) + h0(M; V) - h0(M; V*)                      (FINDINGS section 2, proof there)
so it depends on dim W only.  Main's interior index is the case dim W = r1(V*).  The extreme choices need no pairing:
    W = 0    : N = (a1 - r1) - b1          W = all : N = a1 - (b1 - q1)
This script reads the run's (a0, a1, t0, r1) and (b0, b1, s0, q1) for W1 at all six points and checks the three values against the
formula."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    run = json.loads((HERE / "extension_index_run.txt").read_text(encoding="utf-8"))
    rows = []
    for r in run["exact"]:
        a0, a1, t0, r1 = r["W1 data (a0,a1,t0,r1)"]
        b0, b1, s0, q1 = r["W1* data"]
        t1 = r1 + q1
        formula = {d: d - t0 + a0 - b0 for d in range(t1 + 1)}
        lower = (a1 - r1) - b1
        interior = (a1 - r1) - (b1 - q1)
        upper = a1 - (b1 - q1)
        rows.append({"q": r["q"], "mu": r["mu"], "dim H^1(T;W1)": t1, "N_W by dim W": formula,
                     "lower (W=0)": lower, "interior (dim W = q1 = %d)" % q1: interior, "upper (W=all)": upper,
                     "formula_matches": lower == formula[0] and upper == formula[t1] and interior == formula[q1],
                     "10' count = -N_W, over all end conditions": sorted({-v for v in formula.values()})})
    return rows


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True)
    print(txt)
    if "--record" in sys.argv:
        (HERE / "end_conditions_run.txt").write_text(txt + "\n", encoding="utf-8")
