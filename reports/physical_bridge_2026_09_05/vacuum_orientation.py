"""A post-R4, pre-sealed competing-vacuum control for the same potential."""
import argparse
import json
from pathlib import Path

import numpy as np
import sympy as sp

from . import vacuum as v


def cartan_stabilizer(h):
    h = sp.Matrix(h)
    if h.shape != (6, 1):
        raise ValueError("six Cartan coefficients required")
    weights, _, _, positive, generators = v.representation()
    s, n = v.embedding()[:2]
    charges = [(h.T*w)[0] for w in weights]
    a = sp.diag(*charges)
    columns = []
    for t in generators:
        # Independent direct full-matrix action, not the earlier coordinate map.
        da = sp.I*v.comm(t, a)
        col = v.real_column(sp.I*t*s).col_join(v.real_column(sp.I*t*n))
        col = col.col_join(v.real_column(sp.Matrix(729, 1, list(da))))
        columns.append(col)
    action = sp.Matrix.hstack(*columns)
    # Delete zero rows only: they impose no equation. No rank tolerance is used.
    active = [i for i in range(action.rows) if any(action.row(i))]
    rank = action[active, :].rank()
    su5_roots = []
    for coeff, label, _ in positive:
        if coeff[0] == coeff[1] == 0:
            su5_roots.append((h.T*sp.Matrix(label))[0])
    assert len(su5_roots) == 10
    return a, 78-rank, su5_roots


def analyze():
    s, n, y, yh, _, _ = v.embedding()
    a, dim, positive_charges = cartan_stabilizer([0, 0, 1, 4, 16, 64])
    _, reference_dim, _ = cartan_stabilizer(yh)
    scale_squared = sp.trace(y*y)/sp.trace(a*a)
    assert scale_squared > 0
    assert a*s == a*n == sp.zeros(27, 1)
    assert scale_squared*sp.trace(a*a) == sp.trace(y*y)
    normalized = np.array(a, complex)*float(sp.sqrt(scale_squared))
    c = v.constraints(np.array(s, complex), np.array(n, complex), normalized)
    value = float(c@c)
    z = v.constraints(np.array(s, complex), np.array(n, complex), np.zeros((27, 27)))
    return {
        "scope": "same R4 potential and scalar norms; explicit alternative orientation",
        "cartan_coefficients_before_norm": [0, 0, 1, 4, 16, 64],
        "scale_squared": str(scale_squared),
        "positive_su5_root_charges": [str(x) for x in positive_charges],
        "su5_roots_with_zero_charge": 2*sum(x == 0 for x in positive_charges),
        "compact_unbroken_dimension": dim,
        "reference_Y_unbroken_dimension": reference_dim,
        "potential_numerical": value,
        "zero_adjoint_potential_control": float(z@z),
        "not_gauge_equivalent_to_Y": bool(dim != reference_dim),
        "global_minimum_proof": "same scalar constraints as R4; A*S=A*N=0 and exact norm equality",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = json.dumps(analyze(), indent=2, allow_nan=False)+"\n"
    with args.output.open("x", encoding="utf-8") as handle:
        handle.write(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
