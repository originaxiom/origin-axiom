"""B1645 -- the half bound.  Sealed instrument unchanged; the stored cells; the exact identities (post-seal); live: m for a
real direction from t^2 - (4 + u) t + 4 = 0 and m >= 1/2; m = 0 on an isotropic direction; the bite -- a complex
non-isotropic direction near R-bar has m > 0."""
import hashlib, json, math, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1645_the_half_bound"


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at e77f9b5b3")
    assert hashlib.sha256(open(A / "verification" / "half_bound.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(A / "verification" / "half_bound.json"))
    assert d["T1_max_rel"] < 1e-14 and d["T2_max_rel"] < 1e-14 and d["T4"]["m_min"] >= 0.5 - 1e-9
    assert all(abs(x - 0.5) < 1e-12 for x in d["T4"]["m_in_plane"]) and all(abs(x - 1) < 1e-12 for x in d["T4"]["m_normal"])
    assert d["T5"]["inf_m"] < 1e-12 and all(abs(s - 1) < 0.05 for s in d["T5"]["slopes"])
    assert all(json.load(open(A / "verification" / "post_seal_symbolic.json")).values())
    assert json.load(open(A / "verification" / "post_seal_cone.json"))["isotropic_m_max"] < 1e-12
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def _R(t, K=40):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    return np.array([-th2 ** 2, -th4 ** 2, 1j * th3 ** 2]) / (np.pi * th2 * th3 * th4)


def test_live_bound_cone_and_bite():
    Y = lambda a, R: np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)
    R = _R(complex(0.17, 1.23)); r = np.linalg.norm(R.real)
    rng = np.random.default_rng(7)
    for _ in range(50):
        a = rng.normal(size=3); s = np.linalg.svd(Y(a, R), compute_uv=False)
        u = abs(np.dot(a, R)) ** 2 / (r * r * np.dot(a, a))
        tp = ((4 + u) + math.sqrt((4 + u) ** 2 - 16)) / 2; tm = ((4 + u) - math.sqrt((4 + u) ** 2 - 16)) / 2
        assert abs(s[1] / s[0] - math.sqrt(tm / tp)) < 1e-12 and s[1] / s[0] >= 0.5 - 1e-12
    iso = np.array([1.0, 1j, 0.0]); s = np.linalg.svd(Y(iso, R), compute_uv=False)
    assert s[1] / s[0] < 1e-12                                                                 # isotropic: m = 0
    near = np.conj(R) / np.linalg.norm(R) + 0.05 * np.array([0.3, -0.1j, 0.2])
    s = np.linalg.svd(Y(near, R), compute_uv=False)
    assert s[1] / s[0] > 1e-3                                                                  # bite: off the cone, m > 0
