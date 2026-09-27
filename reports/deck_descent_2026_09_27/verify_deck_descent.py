"""Exact finite controls; no repository science imports or file output."""
import json
import sympy as sp


def companion(c):
    m = sp.Matrix([[1, c], [0, 1]])
    t = sp.zeros(6)
    t[2:4, 0:2] = sp.eye(2)
    t[4:6, 2:4] = sp.eye(2)
    t[0:2, 4:6] = m
    return m, t


def three_fibres(t, include_seam=True):
    n = t.rows
    d = sp.zeros(3 * n)
    d[n:2*n, 0:n] = t
    d[2*n:3*n, n:2*n] = t
    d[0:n, 2*n:3*n] = t**-2 if include_seam else t
    return d


def data(c):
    m, t = companion(c)
    t3 = t**3
    d = three_fibres(t)
    wrong = three_fibres(t, include_seam=False)
    p = (sp.eye(18) + d + d**2) / 3
    naive = (sp.eye(6) + t + t**2) / 3
    cover_basis = sp.Matrix.hstack(*(t3-sp.eye(6)).nullspace())
    invariant_equations = (t-sp.eye(6)) * cover_basis
    return {
        "c": c,
        "det_T": int(t.det()),
        "cube_is_monodromy": t3 == sp.diag(m, m, m),
        "monodromy_retained": t3 != sp.eye(6),
        "square_zero_remainder": (t3-sp.eye(6))**2 == sp.zeros(6),
        "deck_cube_identity": d**3 == sp.eye(18),
        "seam_omitted_cube_identity": wrong**3 == sp.eye(18),
        "projector_idempotent": p**2 == p,
        "projector_rank": int(p.rank()),
        "naive_fibre_average_idempotent": naive**2 == naive,
        "downstairs_H0": 6-int((t-sp.eye(6)).rank()),
        "cover_H0": 6-int((t3-sp.eye(6)).rank()),
        "cover_invariant_H0": cover_basis.cols-int(invariant_equations.rank()),
        "cube_on_cover_H0": (t3-sp.eye(6))*cover_basis == sp.zeros(6, cover_basis.cols),
        "coefficient_domain": "exact rationals",
    }


def validate(result):
    nonzero = result["c"] != 0
    assert result["det_T"] == 1
    assert result["cube_is_monodromy"]
    assert result["monodromy_retained"] == nonzero
    assert result["square_zero_remainder"]
    assert result["deck_cube_identity"]
    assert result["seam_omitted_cube_identity"] == (not nonzero)
    assert result["projector_idempotent"] and result["projector_rank"] == 6
    assert result["naive_fibre_average_idempotent"] == (not nonzero)
    assert result["downstairs_H0"] == (1 if nonzero else 2)
    assert result["cover_H0"] == (3 if nonzero else 6)
    assert result["cover_invariant_H0"] == result["downstairs_H0"]
    assert result["cube_on_cover_H0"]


if __name__ == "__main__":
    results = [data(c) for c in (1, -2, 0)]
    for result in results:
        validate(result)
    print(json.dumps({"scope": "circle comparator, not M6 or physical generations",
                      "sympy_version": sp.__version__, "results": results}, indent=2))
