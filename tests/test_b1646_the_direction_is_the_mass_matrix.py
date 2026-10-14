"""B1646 -- the direction is the mass matrix.  Sealed instrument unchanged; the stored cells; live: the block form and the
bijection at one tau; the bite -- a target outside the symmetric matrices is not reached (the antisymmetric part of
U^dag Y U's 2-3 block is zero for every a), and a random non-isotropic R (the control) breaks the null vector."""
import hashlib, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1646_the_direction_is_the_mass_matrix"


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 0bbbb6cab")
    assert hashlib.sha256(open(A / "verification" / "direction_mass_matrix.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(A / "verification" / "direction_mass_matrix.json"))
    assert d["D1"]["unitarity_max"] < 1e-12 and d["D1"]["block_max_rel"] < 1e-12
    assert d["D2"]["min_sv_ratio_of_L"] > 1e-3 and d["D2"]["masses_max_rel"] < 1e-12
    assert d["D3"]["prod_max_rel"] < 1e-12 and d["D3"]["sumsq_max_rel"] < 1e-12
    for l2, row in d["D4"]["by_l2"].items():
        assert row["in_between"] == 0
        if float(l2) > 0: assert row["defect_range"][1] < 1e-4 and max(row["m_range_tau_i"][1], row["m_range_tau_0"][1]) < 1e-3
        else: assert row["defect_range"][0] > 1 - 1e-6 and min(row["m_range_tau_i"][0], row["m_range_tau_0"][0]) >= 0.5 - 1e-6
    assert d["D5"]["max_relerr"] < 1e-2
    assert all(abs(r[3] - 0.5) < 1e-12 for r in d["D6"]["iy"]) and abs(d["D6"]["tau_i"][0] - 0.6096) < 1e-4
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def _R(t, K=40):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    return np.array([-th2 ** 2, -th4 ** 2, 1j * th3 ** 2]) / (np.pi * th2 * th3 * th4)


def _frame(R):
    n = np.cross(R.real, R.imag); n = n / np.linalg.norm(n); nR = np.linalg.norm(R)
    return np.column_stack([R / nR, np.conj(R) / nR, n]), n, nR


def test_live_block_bijection_and_bite():
    Y = lambda a, R: np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)
    R = _R(complex(-0.21, 1.37)); U, n, nR = _frame(R)
    rng = np.random.default_rng(11)
    for _ in range(20):
        a = rng.normal(size=3) + 1j * rng.normal(size=3)
        B = U.conj().T @ Y(a, R) @ U
        assert np.abs(B[:, 0]).max() < 1e-12 and np.abs(B[1, :]).max() < 1e-12              # kills R; misses conj(R)
        M2 = B[np.ix_([0, 2], [1, 2])]
        assert abs(M2[0, 1] - M2[1, 0]) < 1e-12                                             # the 2-3 block is symmetric
        assert abs(np.linalg.det(M2) + nR ** 2 * np.dot(a, a)) < 1e-12 * np.abs(M2).max() ** 2
    L = np.column_stack([[2 * np.dot(e, np.conj(R)), nR * np.dot(e, n), -np.dot(e, R)] for e in np.eye(3)])
    k = np.array([0.3 + 0.1j, -0.7j, 1.1]); a = np.linalg.solve(L, k)
    s = np.linalg.svd(Y(a, R), compute_uv=False); sK = np.linalg.svd(np.array([[k[0], k[1]], [k[1], k[2]]]), compute_uv=False)
    assert np.allclose(s[:2], sK, atol=1e-12) and s[2] < 1e-12                              # any symmetric block is reached
    Rr = rng.normal(size=3) + 1j * rng.normal(size=3)                                        # control: not isotropic
    s = np.linalg.svd(Y(rng.normal(size=3) + 1j * rng.normal(size=3), Rr), compute_uv=False)
    assert s[2] / s[0] > 1e-3                                                                # the bite: no massless state
