"""B1642 -- the zero modes' residue at the puncture: computed, antisymmetric, not golden.  Sealed instrument unchanged; the
stored cells; live: Y_qp = -Y_pq from the quaternion units' anticommutation (exact, in the instrument's own 2x2 units), and
the bite -- a symmetric zero-diagonal matrix with the same moduli has three distinct singular values."""
import hashlib, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1642_the_golden_coupling_as_the_zero_modes_residue"


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 55bd29ab7")
    assert hashlib.sha256(open(A / "verification" / "residue_coupling.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(A / "verification" / "residue_coupling.json"))
    assert d["R1_max_abs"] == 0.0 and all(v["max_rel_spread"] < 1e-30 for v in d["R2"].values())
    assert all(v["max_rel_spread"] < 1e-30 for v in d["R3"].values())
    assert all(abs(a["sv"][2]) < 1e-12 and abs(a["sv"][1] - 1) < 1e-12 for a in d["R4"]["axis"])        # (1, 1, 0)
    assert all(m > 1e-3 for m in d["R6_misfit"].values())
    p = json.load(open(A / "verification" / "post_seal_residue.json"))
    assert all(x["antisym_rel"] < 1e-30 and x["Y_v_rel"] < 1e-30 for x in p)
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "NEGATIVE"


def test_antisymmetry_from_the_units_and_the_bite():
    qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]]); qk = qi @ qj
    eps = qj
    C = [qj, qi, qk]
    for a in range(3):
        for b in range(3):
            assert np.allclose(C[a].T @ eps @ C[b], -(C[b].T @ eps @ C[a]).T) or a == b
            assert np.allclose(C[a].T @ eps @ C[b] + C[b].T @ eps @ C[a], 0) or a == b      # Y_qp = -Y_pq entrywise
    x, y, z = 0.3, 0.97, 1.02
    sym = np.array([[0, z, y], [z, 0, x], [y, x, 0]]); s = np.linalg.svd(sym, compute_uv=False)
    assert s[2] > 1e-3 and abs(s[0] - s[1]) > 1e-3                                           # bite: symmetric is not (a, a, 0)
