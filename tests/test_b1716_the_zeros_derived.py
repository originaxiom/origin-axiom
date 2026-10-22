"""B1716 -- the frame's exact zeros, derived (P-262, P-268). Stored: the six checks. Live: the identities Z1 (the
determinant of the four-channel matter), Z3 (the quaternion form of the coupling) and Z4 (the signed cross product)
re-done on fresh random draws with B1656's functions."""
import itertools, json, pathlib, sys
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1716_the_zeros_derived" / "verification"


def test_stored():
    d = json.loads((A / "the_zeros_derived.json").read_text(encoding="utf-8"))
    assert d["Z1_max_rel"] < 1e-14 and d["Z2_max_rel_sum_R2"] < 1e-13 and d["Z3_max_rel"] < 1e-13
    assert d["Z4_signed_antisymmetry"] < 1e-13 and d["Z4_spectrum_defect"] < 1e-12
    assert d["Z5_tied_lines"] == 27 and d["Z5_max_rel_R_tied"] < 1e-12
    law = d["Z6_law_agree_disagree_undefined"]
    assert sum(v[1] for v in law.values()) == 0 and sum(v[2] for v in law.values()) == 0
    assert d["Z6_max_D_where_predicted"] < 1e-12 and d["Z6_min_D_where_not"] > 1e-6


def test_live_identities():
    sys.path.insert(0, str(A)); _argv = sys.argv; sys.argv = ["x"]
    import b1656_funcs as B
    sys.argv = _argv
    rng = np.random.default_rng(7)
    QU = {"1": np.eye(2, dtype=complex), "i": B.QI, "j": B.QJ, "k": B.QK}
    comp = lambda q: {s: np.trace(np.conj(U).T @ q) / 2 for s, U in QU.items()}
    for _ in range(20):
        u = {s: complex(*rng.normal(size=2)) for s in B.UNITS}
        assert abs(np.linalg.det(B.weighted_M(u)) - 0.25 * sum(v * v for v in u.values())) < 1e-12
        S = sum(complex(*rng.normal(size=2)) * U for U in QU.values())
        Y = B.coupling(S, B.weighted_M(u))
        Yq = np.array([[sum(u[s] * comp(np.linalg.inv(Ca) @ S @ Cb)[s] for s in B.UNITS) for Cb in B.BLOCKS] for Ca in B.BLOCKS])
        assert np.max(np.abs(Y - Yq)) < 1e-12 * np.max(np.abs(Y))
        for p, U in (("i", B.QI), ("j", B.QJ), ("k", B.QK)):
            m = dict(u); m[p] = 0
            Y = B.coupling(U, B.weighted_M(m))
            assert min(np.max(np.abs(np.diag(s) @ Y + (np.diag(s) @ Y).T)) for s in itertools.product((1, -1), repeat=3)) < 1e-12
            sv = np.linalg.svd(Y, compute_uv=False)
            assert abs(sv[1] / sv[0] - 1) < 1e-12 and sv[2] / sv[0] < 1e-12
