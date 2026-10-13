"""B1640 -- the frame audit: on the ruled branch Tbar x T is non-degenerate at omega (B1635's own sealed read-outs); the
record's multiplier allows a symmetric weight-1 coupling and its conjugate does not; the TM1 residual pair needs two
different fixed-point types.  Stored results; GENESIS v1.42 reproduced by its amendment; live: the two read-outs that
carry the claims, from B1635's sealed JSON, and the eigenline bite (RL against an elliptic element of order 2)."""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1640_the_frame_audit"


def test_stored():
    d = json.load(open(A / "verification" / "frame_audit.json"))
    assert len(d["A"]["sealed_nondegenerate_at_omega"]) == 9 and all(k.startswith("TbT") for k in d["A"]["sealed_nondegenerate_at_omega"])
    assert d["A"]["min_gap_live"] > 1e-3
    rec, conj = d["B"]["record (rho = lift^-1; W = eta^18 Y)"], d["B"]["conjugate (rho-bar; W = eta^6 Y)"]
    assert rec["k=1"] == {"D": 0, "O+": 1, "O-": 0} and conj["k=1"] == {"D": 0, "O+": 0, "O-": 1}
    assert d["C"]["homomorphism_checks"] and d["C"]["RL"]["orders"] == [3] and d["C"]["RRL"]["orders"] == [2]
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def test_genesis_v142():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"])
    assert r.returncode == 0
    g = open(ROOT / "GENESIS.md", encoding="utf-8").read()
    assert "[v1.42] Audited (B1640" in g and "[v1.42] The hand (B1640)" in g


def test_live_from_the_sealed_readouts():
    s = json.load(open(ROOT / "frontier" / "B1635_couplings_on_the_ruled_branch" / "verification" / "couplings_on_the_ruled_branch.json"))
    m = s["K3_K5_masses"]
    r = m["TbT k=4 #0"]["omega"][0]
    assert r[0] - r[1] > 0.1 and r[1] - r[2] > 0.1                      # three distinct masses at omega under Tbar x T
    t = m["TT O+ k=1 #0"]["omega"][0]
    assert abs(t[1] - t[2]) < 1e-9                                     # the single symmetric piece is degenerate there (the bite)


def test_eigenline_bite():
    import numpy as np
    P13 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], complex); P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], complex)
    rS, rT = -1j * P13, np.diag([1j, 1, 1]) @ P23
    rR = rS @ np.linalg.inv(rT) @ np.linalg.inv(rS)                      # R = S T^-1 S^-1 in SL(2, Z)
    rRL = rR @ rT
    E3 = rS @ rT                                                         # ST, order 3 in PSL(2, Z)
    E2 = rS                                                              # S, order 2
    def shares(X, Y):
        _, V = np.linalg.eig(X)
        return all(np.linalg.norm(Y @ v - (v.conj() @ Y @ v) / (v.conj() @ v) * v) < 1e-9 for v in V.T)
    assert np.allclose(np.linalg.matrix_power(rRL, 3) / np.linalg.matrix_power(rRL, 3)[0, 0], np.eye(3))   # finite order 3 up to scalars
    assert not (shares(rRL, E2) and shares(E2, rRL))                     # never an order-2 stabiliser's lines
