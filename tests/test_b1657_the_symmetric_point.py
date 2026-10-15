"""B1657 -- the symmetric point. The sealed instrument unchanged; the stored cells; live (numpy, independent of the
instrument): P's eigenlines at omega; the conjugate law and the parallel law at one perturbation each; the bite -- each
law fails in the other's vacuum."""
import hashlib, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1657_the_symmetric_point"


def _R(tau, K=30):
    q = np.exp(1j*np.pi*tau); n = np.arange(K); m = np.arange(1, K)
    t2 = 2*np.sum(q**((n+.5)**2)); t3 = 1 + 2*np.sum(q**(m**2)); t4 = 1 + 2*np.sum((-1)**m*q**(m**2))
    tp = 2*np.pi*np.sum((-1)**n*(2*n+1)*q**((n+.5)**2))
    return np.array([-t2**2, 1j*t3**2, -t4**2])/tp


def _Y(a, v):
    return np.outer(a, v) + np.outer(v, a) - (a @ v)*np.eye(3)


def _light(a, v):
    s = np.linalg.svd(_Y(a, v), compute_uv=False); return s[1]/s[0], s[2]/s[0]


def test_live_the_move_and_the_two_laws():
    P = np.array([[0, 1, 0], [0, 0, -1], [1, 0, 0]], dtype=float)
    R = _R(np.exp(2j*np.pi/3)); R = R/np.linalg.norm(R)
    assert np.abs(P @ R - np.exp(-1j*np.pi/3)*R).max() < 1e-12 and abs(R @ R) < 1e-13
    rng = np.random.default_rng(0); al = rng.normal(size=3) + 1j*rng.normal(size=3); be = rng.normal(size=3) + 1j*rng.normal(size=3)
    al, be = al/np.linalg.norm(al), be/np.linalg.norm(be); e = 1e-3
    d = lambda x: (x @ x)/np.linalg.norm(x)**2
    a, v = R.conj() + e*al, R + e*be                                     # the conjugate vacuum
    got = np.array(_light(a, v)); law = np.sort([abs(d(a)), abs(d(v))])[::-1]
    assert np.abs(got/law - 1).max() < 0.05
    a, v = R + e*al, R + e*be                                            # the parallel vacuum
    m2, m1 = _light(a, v)
    assert abs(m2/(abs(d(a) + d(v))/4) - 1) < 0.1 and abs(m1/(abs(d(a)*d(v))/4) - 1) < 0.1
    assert np.abs(np.array([m2, m1])/np.sort([abs(d(a)), abs(d(v))])[::-1] - 1).max() > 0.5   # the bite: the other law fails


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at d4dcd0d50")
    assert hashlib.sha256(open(A / "verification" / "the_symmetric_point.py", "rb").read()).hexdigest() == first.split()[4]
    assert hashlib.sha256(open(A / "PREREGISTRATION.md", "rb").read()).hexdigest().startswith("1e0a4bc9")
    d = json.load(open(A / "verification" / "the_symmetric_point.json"))
    assert d["S0"]["void"] is False
    for cell in ("S1", "S2", "S3", "S4", "S5"):
        assert d[cell]["holds"] is True, cell
    assert d["S3"]["conjugate_vacuum"]["conj_law"] < 0.05 and d["S3"]["parallel_vacuum"]["conj_law"] > 100
    assert d["S5"]["kappa_abs_mean_vs_w87_rel"] < 1e-5 and abs(d["S5"]["w87_slope"] - 2.9491719847) < 1e-8
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"
