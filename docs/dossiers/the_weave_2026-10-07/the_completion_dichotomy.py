"""W83: main's tribunal item "a gauge completion of the moves that keeps SU(2)_w and Y, or a proof that none exists in
the lane's E8 frame", answered by a dichotomy. This script was committed before its one run; predictions and priors here.

  M1  the commutant of colour (the lane's two colour roots) and SU(2)_w (the weak root) in e8: the roots orthogonal to all
      three number 30, and with the rank-5 Cartan they span an su(6) whose simple roots include the lane's A5 chain
      (`the_cusp_condensate_charge_map.CHAIN`); so every hypercharge (which commutes with colour and SU(2)_w) lies in that
      su(6)                                                                                              prior 95%
  M2  on the 6 = 3 (x) 2_q of that su(6) (the lane's weights in blocks (0, 1), (2, 3), (4, 5)), the trace-free Y commuting
      with the holonomy 1_3 (x) Q8 and with the moves' action on the family index 3:
        the moves act through O (signed permutations of the blocks)    dimension 0   (lemma A: no Y)       prior 99%
        through S3 only (unsigned permutations)                        dimension 1   (the democratic split) prior 99%
        trivially on the family index                                  dimension 2   (block-diagonal Y)     prior 99%
  So: every completion that keeps colour and SU(2)_w keeps a hypercharge only if the moves act on the lane's family index
  other than through O; and then that index is not the weave's M, on which the moves act through O (W49). Exact.

Run: python3 the_completion_dichotomy.py  ->  the_completion_dichotomy.json beside it.
"""
import itertools
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as sy

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_cusp_condensate_charge_map as CM  # noqa: E402

OUT = HERE / "the_completion_dichotomy.json"


def simple_roots(rs):
    """the simple roots of a root subsystem, by a generic linear functional"""
    f = [F(1, 2 ** k + 3) for k in range(8)]
    pos = [r for r in rs if CM.dot(r, f) > 0]
    simple = [r for r in pos if not any(CM.add(r, s, -1) in set(pos) for s in pos if s != r)]
    return simple


def commutant_dim(gens, n=6, traceless=True):
    xs = sy.symbols(f"x0:{n * n}")
    X = sy.Matrix(n, n, xs)
    eqs = []
    for g in gens:
        eqs += list(X * g - g * X)
    if traceless:
        eqs.append(X.trace())
    A = sy.Matrix([[sy.diff(e, x) for x in xs] for e in eqs])
    return n * n - A.rank()


def kron(a, b):
    return sy.Matrix(sy.kronecker_product(a, b))


def main_():
    out = {"status": "W83: the completion dichotomy in the lane's E8 frame (script committed before its one run)"}
    orth = [r for r in CM.RR if all(CM.dot(r, c) == 0 for c in CM.COLOUR) and CM.dot(r, CM.WEAK) == 0]
    simple = simple_roots(orth)
    cartan = sy.Matrix([[sy.Rational(CM.dot(a, b).numerator, CM.dot(a, b).denominator) for b in simple] for a in simple])
    chain_in = all(c in set(orth) for c in CM.CHAIN)
    # A5's Cartan matrix up to ordering: five simple roots, a path graph
    deg = sorted(sum(1 for j in range(len(simple)) if j != i and cartan[i, j] != 0) for i in range(len(simple)))
    a5 = len(simple) == 5 and deg == [1, 1, 2, 2, 2] and all(cartan[i, i] == 2 for i in range(5))
    out["M1"] = {"roots orthogonal to colour and SU(2)_w": len(orth), "simple roots": len(simple),
                 "degrees of the Dynkin graph": deg, "an A5": a5, "the lane's chain inside": chain_in,
                 "holds": len(orth) == 30 and a5 and chain_in}
    I2, I3 = sy.eye(2), sy.eye(3)
    qi = sy.Matrix([[sy.I, 0], [0, -sy.I]])
    qj = sy.Matrix([[0, 1], [-1, 0]])
    hol = [kron(I3, qi), kron(I3, qj)]

    def perm(p):
        M = sy.zeros(3, 3)
        for i, j in enumerate(p):
            M[j, i] = 1
        return M
    s3 = [kron(perm(p), I2) for p in ((1, 0, 2), (1, 2, 0))]
    v4 = [kron(sy.diag(1, -1, -1), I2), kron(sy.diag(-1, 1, -1), I2)]
    dims = {"through O": commutant_dim(hol + s3 + v4), "through S3 only": commutant_dim(hol + s3),
            "trivially": commutant_dim(hol)}
    out["M2"] = {"trace-free commutant dimensions": dims,
                 "holds": dims == {"through O": 0, "through S3 only": 1, "trivially": 2}}
    out["cells"] = {"M1": out["M1"]["holds"], "M2": out["M2"]["holds"]}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main_()
