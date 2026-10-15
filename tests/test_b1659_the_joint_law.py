"""B1659 -- the joint law. The sealed instrument unchanged; the stored cells; live (numpy, independent of the
instrument): det Y = 4 det S det M tr(eps S M^T) and adj Y = det S A(M) + det M P A(S) at random complex S, M; the
symmetric form with N = M eps; geometric masses at N = S; the bite -- the constant 3 in place of 4, A in place of P A,
and N != S each fail."""
import hashlib, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1659_the_joint_law"
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ; BLOCKS = [QJ, QI, QK]
P = np.diag([1, -1, -1]); EI = np.linalg.inv(EPS)


def _Y(S, M):
    return np.array([[np.sum((Ca.T @ EPS @ S @ Cb)*M) for Cb in BLOCKS] for Ca in BLOCKS])


def _adj(Y):
    return np.array([[np.linalg.det(np.delete(np.delete(Y, j, 0), i, 1))*(-1)**(i+j) for j in range(3)] for i in range(3)])


def _A(M):
    m0, m1, m2, m3 = M.ravel(); I = 1j
    return np.array([[m0**2 + m1**2 + m2**2 + m3**2, 2*I*(m0*m2 + m1*m3), -I*(m0**2 + m1**2 - m2**2 - m3**2)],
                     [2*I*(m0*m1 + m2*m3), -4*m1*m2, 2*(m0*m1 - m2*m3)],
                     [-I*(m0**2 - m1**2 + m2**2 - m3**2), 2*(m0*m2 - m1*m3), -m0**2 + m1**2 + m2**2 - m3**2]])


def test_live_joint_law_and_bites():
    rng = np.random.default_rng(7)
    for _ in range(8):
        S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); M = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
        Y = _Y(S, M); n = np.linalg.norm(Y); l = np.trace(EPS @ S @ M.T)
        assert abs(np.linalg.det(Y) - 4*np.linalg.det(S)*np.linalg.det(M)*l)/n**3 < 1e-13
        assert abs(np.linalg.det(Y) - 3*np.linalg.det(S)*np.linalg.det(M)*l)/n**3 > 1e-4          # bite: the constant
        assert np.abs(_adj(Y) - np.linalg.det(S)*_A(M) - np.linalg.det(M)*P @ _A(S)).max()/n**2 < 1e-13
        assert np.abs(_adj(Y) - np.linalg.det(S)*_A(M) - np.linalg.det(M)*_A(S)).max()/n**2 > 1e-4  # bite: P is needed
        N = M @ EPS                                                                                  # the symmetric form
        assert np.abs(_Y(S, N @ EI) - _Y(N, S @ EI)).max()/n < 1e-13
        assert abs(l + (np.linalg.det(S + N) - np.linalg.det(S) - np.linalg.det(N)))/np.linalg.norm(S)/np.linalg.norm(N) < 1e-13
        sv = np.linalg.svd(_Y(S, S @ EI), compute_uv=False); assert abs(sv[0]*sv[2]/sv[1]**2 - 1) < 1e-10   # geometric at N = S
        sv = np.linalg.svd(_Y(S, N @ EI), compute_uv=False); assert abs(sv[0]*sv[2]/sv[1]**2 - 1) > 1e-3    # bite: N != S


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at f4b12d788")
    assert hashlib.sha256(open(A / "verification" / "the_joint_law.py", "rb").read()).hexdigest() == first.split()[4]
    assert hashlib.sha256(open(A / "PREREGISTRATION.md", "rb").read()).hexdigest().startswith("8123044b")
    d = json.load(open(A / "verification" / "the_joint_law.json"))
    for cell in ("J1", "J2", "J2b", "J2c", "J3", "J4", "J5"):
        assert d[cell]["holds"] is True, cell
    assert d["all_hold"] is True and d["J3"]["cases"] == 324 and d["J4"]["d_cases"] == 10
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"
