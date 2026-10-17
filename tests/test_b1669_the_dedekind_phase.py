"""B1669 -- the Dedekind phase. The sealed instrument unchanged; the stored cells; and three live mathematical facts:
the sum rule s1 = s2 + s3 for zero-diagonal complex symmetric 3x3 matrices (hence s2 >= s1/2), the golden spectrum of
the weight-1 form at tau = i and the (1, 1/2, 1/2) spectrum at omega, and the phase law 12 arg eta(x + iy) = pi x + O(|q|)."""
import hashlib, json, math, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1669_the_dedekind_phase"
INSTR = A / "verification" / "the_dedekind_phase.py"


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 20ed2c300")
    assert hashlib.sha256(open(INSTR, "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(A / "verification" / "the_dedekind_phase.json"))
    assert d["all_hold"] is True and d["B1635_reproduced"] is True
    assert d["table_TT"]["1"]["total"] == 1 and d["table_TbT"]["0"]["total"] == 1
    assert d["N8"]["sum_rule_symbolic"] == "0" and d["N8"]["grid_floor"]["value"] >= 0.5
    assert all(v["chi2_min"] > 500 for v in d["fits"].values())
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def _theta2(tau, N=14):
    q = np.exp(2j*np.pi*tau); n = np.arange(-N, N + 1)
    t3 = np.sum(q**(n**2/2.0)); t4 = np.sum((-1.0)**n*q**(n**2/2.0))
    t2 = 2*np.exp(1j*np.pi*tau/4)*np.sum(q**(np.arange(0, N)*(np.arange(0, N) + 1)/2.0))
    return t2**2, t3**2, t4**2


def test_sum_rule_and_floor_live():
    rng = np.random.default_rng(3)
    for _ in range(2000):
        a, b, c = rng.normal(size=3) + 1j*rng.normal(size=3)
        s = np.linalg.svd(np.array([[0, c, b], [c, 0, a], [b, a, 0]]), compute_uv=False)
        assert abs(s[0] - s[1] - s[2]) < 1e-12*s[0] and s[1] >= 0.5*s[0] - 1e-12
    phi = (1 + 5**0.5)/2
    for tau, want in ((1j, (1/phi, 1/phi**2)), (np.exp(2j*np.pi/3), (0.5, 0.5))):
        X, Y, Z = _theta2(tau); s = np.linalg.svd(np.array([[0, Z, Y], [Z, 0, X], [Y, X, 0]]), compute_uv=False)
        assert abs(s[1]/s[0] - want[0]) < 1e-9 and abs(s[2]/s[0] - want[1]) < 1e-9


def test_phase_law_live():
    k = np.arange(1, 80)
    for x in (-0.4, -0.1, 0.25, 0.5):
        tau = x + 3.0j; q = np.exp(2j*np.pi*tau); eta = np.exp(2j*np.pi*tau/24)*np.prod(1 - q**k)
        d = (12*np.angle(eta) - np.pi*x + np.pi) % (2*np.pi) - np.pi
        assert abs(d) < 1e-5
