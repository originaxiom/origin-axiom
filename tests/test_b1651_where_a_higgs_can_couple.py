"""B1651 -- where a Higgs can couple the zero modes.  Sealed instrument unchanged; the stored cells; live (closed form,
numpy theta series): the pairing triplet v(z) = c_r th_r(0) th_r(z)/th_1(z) is isotropic at a generic z (the identity);
the half-period triplets are the fixed lines (0, -1, i), (i, 0, 1), (i, -1, 0) at two tau; under L (tau -> tau + 1) the
triplet at any z moves by Ad(g_L)^-1 exactly; the V4-twisted moves share exactly the four body diagonals; the bite --
a generic point's triplet is not tau-independent, and L's law fails with R's matrix."""
import hashlib, itertools, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1651_where_a_higgs_can_couple"
C = np.array([-1, -1, 1j])


def _th(n, z, t, K=40):
    k = np.arange(-K, K + 1)
    if n == 3:
        return np.sum(np.exp(1j * np.pi * t * k * k + 2j * k * z))
    if n == 4:
        return np.sum((-1.0) ** k * np.exp(1j * np.pi * t * k * k + 2j * k * z))
    h = k + 0.5; e = np.exp(1j * np.pi * t * h * h + 1j * (2 * k + 1) * z)
    return np.sum(e) if n == 2 else -1j * np.sum((-1.0) ** k * e)


def _v(z, t):
    return np.array([C[r] * _th(n, 0, t) * _th(n, z, t) / _th(1, z, t) for r, n in enumerate((2, 4, 3))])


def _ov(u, w):
    return abs(np.vdot(u, w)) / (np.linalg.norm(u) * np.linalg.norm(w))


def _ad(w, x, y, z):
    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


S2 = 1 / np.sqrt(2)
AL, AR = _ad(S2, S2, 0, 0), _ad(S2, 0, -S2, 0)
V4 = [np.diag(d).astype(complex) for d in ([1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1])]


def test_live_isotropy_half_periods_and_L_law():
    t1, t2 = complex(0.13, 1.21), complex(-0.31, 0.97)
    z = np.pi * (0.37 + 0.23 * t1)
    v = _v(z, t1)
    assert abs(np.dot(v, v)) < 1e-12 * np.vdot(v, v).real                       # isotropic at a generic point
    for (m, n), line in {(0.5, 0): (0, -1, 1j), (0, 0.5): (1j, 0, 1), (0.5, 0.5): (1j, -1, 0)}.items():
        for t in (t1, t2):
            w = _v(np.pi * (m + n * t), t)
            assert max(_ov(np.array(line), D @ w) for D in V4) > 1 - 1e-12        # the fixed lines, up to V4
    for zz in (z, np.pi * (0.11 + 0.71 * t1)):                                    # L: tau -> tau + 1, z fixed
        assert _ov(_v(zz, t1 + 1), AL.T @ _v(zz, t1)) > 1 - 1e-12
    # the bite: a generic point's triplet moves with tau; L's law fails with R's matrix
    g1, g2 = _v(np.pi * (0.37 + 0.23 * t1), t1), _v(np.pi * (0.37 + 0.23 * t2), t2)
    assert max(_ov(g1, D @ g2) for D in V4) < 1 - 1e-6
    assert max(_ov(_v(z, t1 + 1), D @ M @ _v(z, t1)) for D in V4 for M in (AR, AR.T)) < 1 - 1e-6


def test_live_twisted_moves_share_the_body_diagonals():
    lines = []
    for D1, D2 in itertools.product(V4, repeat=2):
        A1, B1 = D1 @ AL, D2 @ AR
        for lam in (1, -1, 1j, -1j):
            for mu in (1, -1, 1j, -1j):
                _, s, Vh = np.linalg.svd(np.vstack([A1 - lam * np.eye(3), B1 - mu * np.eye(3)]))
                if s[-1] < 1e-10:
                    u = Vh[-1].conj(); lines.append(u / u[np.argmax(abs(u))])
    assert len(lines) == 4
    assert all(np.allclose(abs(u), 1, rtol=0, atol=1e-12) and abs(u.imag).max() < 1e-12 for u in lines)
    assert len({tuple(np.round(u.real, 9)) for u in lines}) == 4


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 6d6f7f660")
    assert hashlib.sha256(open(A / "verification" / "where_a_higgs_couples.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(A / "verification" / "where_a_higgs_couples.json"))
    assert d["U1"]["one_form_max_rel"] < 1e-15 and d["U1"]["quad_ratio_minus_lam_max"] < 1e-15
    assert d["U1"]["min_abs_lam_over_mu_over_rad"] > 5
    assert d["U2_max_dev_from_sign"] < 1e-15 and d["U2_all_nontrivial"]
    u3 = d["U3"]
    assert u3["a_isotropy_max_fixed_points"] < 1e-25 and u3["a_isotropy_max_generic_points"] < 1e-25
    assert u3["b_half_period_tau_independence_min_overlap"] > 1 - 1e-12
    assert len(u3["c_control_max_overlap"]) == 4 and max(u3["c_control_max_overlap"].values()) < 1 - 1e-6
    assert d["U4_exact_law_D1"]["L"] > 1 - 1e-12 and d["U4_exact_law_D1"]["R"] > 1 - 1e-12
    assert d["U4_images_as_predicted"] and d["U4_max_half_lattice_dist"] < 1e-12
    assert max(d["U4_control_swapped_matrix_puncture_max"].values()) < 1 - 1e-6
    u5 = d["U5"]
    assert (u5["group_order"], u5["commutant_dim"], u5["untwisted_common_lines"]) == (24, 1, 0)
    assert u5["untwisted_min_sigma"] > 1e-6 and abs(u5["untwisted_max_overlap"] - 0.5) < 1e-12
    assert (u5["n_twisted_common_lines"], u5["max_joint_dim"], u5["distinct_twisted_lines"]) == (4, 1, 4)
    assert u5["all_twisted_lines_body_diagonals_real"] and u5["kernel_is_V4"] and u5["n_permutations"] == 6
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"
