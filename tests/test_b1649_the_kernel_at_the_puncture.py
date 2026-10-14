"""B1649 -- the kernel at the puncture.  Sealed instrument unchanged; the stored cells; live (closed form): R is a two-
sided null vector of s0 [R]x + a R^T + R a^T - (a.R) 1 for random s0 and a, and two sectors' left null vectors coincide;
the bite -- a non-isotropic R gives a massive first generation and a non-zero V_us."""
import hashlib, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1649_the_kernel_at_the_puncture"


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at a1bd642a6")
    assert hashlib.sha256(open(A / "verification" / "the_kernel_at_the_puncture.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(A / "verification" / "the_kernel_at_the_puncture.json"))
    assert d["K1"]["right_max_rel"] < 1e-20 and d["K1"]["left_max_rel"] < 1e-20
    for r in d["K2"]:
        assert abs(1 - r["V_ud"]) < 1e-10 and max(r["V_us"], r["V_ub"], r["V_cd"], r["V_td"]) < 1e-10
        assert max(r["m1_over_m3_u"], r["m1_over_m3_d"]) < 1e-10
    assert d["K3"]["rank"] == 3
    assert d["K4"]["m1_over_m3_u"] > 1e-3 and max(d["K4"]["V_us"], d["K4"]["V_ub"]) > 1e-3
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def _R(t, K=40):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    return np.array([-th2 ** 2, -th4 ** 2, 1j * th3 ** 2]) / (np.pi * th2 * th3 * th4)


def _Y(s, R):
    a = np.array(s[1:]); X = np.array([[0, -R[2], R[1]], [R[2], 0, -R[0]], [-R[1], R[0], 0]])
    return np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3) + s[0] * X


def _left_null(Y):
    W, s, _ = np.linalg.svd(Y); return W[:, 2], s


def test_live_kernel_alignment_and_bite():
    rng = np.random.default_rng(23); R = _R(complex(0.07, 1.31))
    rs = lambda: rng.normal(size=4) + 1j * rng.normal(size=4)
    for _ in range(10):
        Y = _Y(rs(), R)
        assert np.linalg.norm(Y @ R) < 1e-12 * np.linalg.norm(Y) * np.linalg.norm(R)
        assert np.linalg.norm(Y.T @ R) < 1e-12 * np.linalg.norm(Y) * np.linalg.norm(R)
    wu, _ = _left_null(_Y(rs(), R)); wd, _ = _left_null(_Y(rs(), R))
    assert abs(abs(np.vdot(wu, wd)) - 1) < 1e-12                                   # the massless states coincide
    Rb = R * np.array([1, 1, 1.1])                                                  # the bite: not isotropic
    Yu, Yd = _Y(rs(), Rb), _Y(rs(), Rb)
    (wu, su), (wd, sd) = _left_null(Yu), _left_null(Yd)
    assert su[2] / su[0] > 1e-3 and abs(abs(np.vdot(wu, wd)) - 1) > 1e-6
