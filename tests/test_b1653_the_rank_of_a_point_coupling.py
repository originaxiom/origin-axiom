"""B1653 -- the rank of a point coupling.  Sealed instrument unchanged; the stored cells; live (numpy theta series,
double precision, independent of the sealed mpmath instrument): with a flat line, the zero modes' value bilinear at a
regular point is rank one, B1644's coupling built from it has rank 2 for a random Higgs S, and up (Q, u^c) and down
(Q, d^c) share the left null vector; the bite -- a coupling at two points, and a tilted profile, have rank 3, while a
radially symmetric profile about a regular point acts as the point (the mean-value property)."""
import hashlib, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1653_the_rank_of_a_point_coupling"
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ
BLOCKS = [QJ, QI, QK]
SIXY = {"Q": 1, "u": -4, "d": 2}


def _thc(a, b, u, T, K=40):
    n = np.arange(-K, K + 1) + a
    return np.sum(np.exp(1j * np.pi * T * n * n + 2j * np.pi * n * (u + b)))


def _th1(u, t, K=40):
    k = np.arange(-K, K + 1); h = k + 0.5
    return -1j * np.sum((-1.0) ** k * np.exp(1j * np.pi * t * h * h + 1j * np.pi * (2 * k + 1) * u))


def _bil(x, y, u, t):
    (ax, bx), (ay, by) = x, y; T = 2 * t; t1 = _th1(u, t)
    den = 1j * np.exp(-1j * np.pi * t / 2) * np.exp(-1j * np.pi * u) * t1
    X0, X1, Y0, Y1 = _thc(ax, bx, u, T), _thc(ax, bx, u + t, T), _thc(ay, by, u, T), _thc(ay, by, u + t, T)
    return np.array([[X0 * Y0 / t1, np.exp(1j * np.pi * by) * X0 * Y1 / den],
                     [np.exp(1j * np.pi * bx) * X1 * Y0 / den, np.exp(1j * np.pi * (bx + by)) * X1 * Y1 / _th1(u + t, t)]])


def _coupling(S, M):
    return np.array([[np.sum((Ca.T @ EPS @ S @ Cb) * M) for Cb in BLOCKS] for Ca in BLOCKS])


def _ratio(Y):
    s = np.linalg.svd(Y, compute_uv=False); return s[-1] / s[0]


def _twist(w, t):
    a = w.imag / t.imag; return (a, 2 * (w.real - a * t.real))


def _left_null(Y):
    U, s, Vh = np.linalg.svd(Y); return U[:, -1]


RNG = np.random.default_rng(1653)
T0 = complex(0.13, 1.07)
U0 = complex(0.3, 0.2)


def _S():
    return RNG.normal(size=(2, 2)) + 1j * RNG.normal(size=(2, 2))


def test_live_rank_one_rank_two_and_the_shared_null_state():
    for _ in range(3):
        x = (RNG.uniform(-0.5, 0.5), RNG.uniform(-1, 1)); y = (RNG.uniform(-0.5, 0.5), RNG.uniform(-1, 1))
        M = _bil(x, y, U0, T0)
        assert abs(np.linalg.det(M)) < 1e-12 * np.abs(M).max() ** 2                 # a point's bilinear is rank one
        assert _ratio(_coupling(_S(), M)) < 1e-12                                     # so the coupling has rank 2
    w = complex(0.17, 0.11) + 0.29 * T0                                               # a generic hypercharge line
    Yu = _coupling(_S(), _bil(_twist(SIXY["Q"] * w, T0), _twist(SIXY["u"] * w, T0), U0, T0))
    Yd = _coupling(_S(), _bil(_twist(SIXY["Q"] * w, T0), _twist(SIXY["d"] * w, T0), U0, T0))
    assert abs(np.vdot(_left_null(Yu), _left_null(Yd))) > 1 - 1e-10                    # up and down share it


def test_the_bite_two_points_and_profiles():
    x, y = (0.21, 0.37), (-0.13, -0.58)
    Rb = _bil(x, y, U0, T0); Vb = _bil(x, y, complex(-0.25, 0.31), T0); Vb *= np.abs(Rb).max() / np.abs(Vb).max()
    assert _ratio(_coupling(_S(), Rb) + _coupling(_S(), Vb)) > 1e-6                   # two points: rank 3
    radii = [0.02, 0.04, 0.06, 0.08, 0.1]; NT = 64
    g = lambda r: np.exp(-r * r / 0.0025)
    def M(wfun):
        out = np.zeros((2, 2), dtype=complex)
        for r in radii:
            for k in range(NT):
                z = U0 + r * np.exp(2j * np.pi * k / NT); out += wfun(z, r) * r * _bil(x, y, z, T0)
        return out
    Mr = M(lambda z, r: g(r)); Mt = M(lambda z, r: g(r) * (1 + (z - U0).real / 0.05))
    assert abs(np.linalg.det(Mr)) < 1e-11 * np.abs(Mr).max() ** 2                      # radial: acts as the point
    assert abs(np.linalg.det(Mt)) > 1e-6 * np.abs(Mt).max() ** 2                       # tilted: lifts


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 4e3981e24")
    assert hashlib.sha256(open(A / "verification" / "the_rank_of_a_point_coupling.py", "rb").read()).hexdigest() == first.split()[4]
    assert hashlib.sha256(open(A / "PREREGISTRATION.md", "rb").read()).hexdigest().startswith("70ecef80")
    d = json.load(open(A / "verification" / "the_rank_of_a_point_coupling.json"))
    assert d["plumbing"]["all_below_1e-30"]
    for cell in ("U0", "U1", "U2", "U3", "U4", "U5", "U6"):
        assert d[cell]["holds"] is True, cell
    assert d["U2"]["b_null_quaternion_max"] < 1e-30 and d["U2"]["d_triplet_isotropy_min"] > 1e-3
    assert d["U3"]["b_lines_max"] < 1e-30 and d["U3"]["c_two_point_min"] > 1e-6
    assert d["U6"]["a_radial_regular"]["det_max"] < 1e-30 and d["U6"]["d_radial_puncture"]["det_min"] > 1e-2
    assert all(c.endswith("- 1.0j)") for c in d["U7_read_out"]["c1_at_each_case"])     # c1 = -i at every case
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"
