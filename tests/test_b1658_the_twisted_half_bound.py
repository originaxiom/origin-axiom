"""B1658 -- the twisted half bound. The sealed instrument unchanged; the stored cells; live (numpy, independent of the
instrument): adj Y(S, pq^T) = det S * A with ||A|| = 2||M||^2 for random S; the Gram spectrum {1, 2, 2, 4} for null M; the
bite -- a non-null M leaves the spectrum, and a synthetic world scaled x6 lies outside the factor-4 bound."""
import hashlib, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1658_the_twisted_half_bound"
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ; BLOCKS = [QJ, QI, QK]


def _Y(S, M):
    return np.array([[np.sum((Ca.T @ EPS @ S @ Cb)*M) for Cb in BLOCKS] for Ca in BLOCKS])


def _adj(Y):
    return np.array([[np.linalg.det(np.delete(np.delete(Y, j, 0), i, 1))*(-1)**(i+j) for j in range(3)] for i in range(3)])


def _gram(M):
    basis = [np.array(b, dtype=complex).reshape(2, 2) for b in np.eye(4)]
    L = np.array([_Y(B, M).ravel() for B in basis]).T
    return np.linalg.eigvalsh(L.conj().T @ L)


def test_live_factorisation_and_spectrum():
    rng = np.random.default_rng(0)
    for _ in range(5):
        p, q = rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2)
        M = np.outer(p, q); S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
        assert abs(np.linalg.norm(_adj(_Y(S, M)))/(abs(np.linalg.det(S))*np.linalg.norm(M)**2) - 2) < 1e-10
        assert np.abs(_gram(M/np.linalg.norm(M)) - np.array([1, 2, 2, 4])).max() < 1e-10
    Mg = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))                       # the bite: a non-null M departs
    assert np.abs(_gram(Mg/np.linalg.norm(Mg)) - np.array([1, 2, 2, 4])).max() > 1e-3


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at b6542d300")
    assert hashlib.sha256(open(A / "verification" / "the_twisted_half_bound.py", "rb").read()).hexdigest() == first.split()[4]
    assert hashlib.sha256(open(A / "PREREGISTRATION.md", "rb").read()).hexdigest().startswith("3fd8de72")
    d = json.load(open(A / "verification" / "the_twisted_half_bound.json"))
    assert d["T0"]["void"] is False
    for cell in ("T1", "T2", "T2b", "T3", "T5"):
        assert d[cell]["holds"] is True, cell
    assert d["T4"]["refuted_at_3sigma"] is True and d["T4"]["pairs_t_plus_1_over_t"]["up/lep"]["z_above_4"] > 20
    assert d["T5"]["control_outside_bound_x6_refuted"] is True and d["T5"]["control_inside_bound_3_9_refuted"] is False
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"
