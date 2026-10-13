"""B1644 -- a Higgs in the multiplicity space.  The sealed instrument unchanged and the run's copy differing by one cast;
the stored cells; live: det Y(a) = (R.R)(a.a)(R.a) symbolically, and Jacobi's identity making the theta triplet
isotropic (so det = 0); the bite -- a non-isotropic R gives a non-zero determinant."""
import hashlib, json, pathlib, difflib
import numpy as np
import sympy as sp
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1644_a_higgs_in_the_multiplicity_space"


def test_sealed_fixed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 8fa3d82ba")
    assert hashlib.sha256(open(A / "verification" / "adjoint_higgs.py", "rb").read()).hexdigest() == first.split()[4]
    a = open(A / "verification" / "adjoint_higgs.py").read().splitlines()
    b = open(A / "verification" / "adjoint_higgs_fixed.py").read().splitlines()
    changed = [l for l in difflib.unified_diff(a, b, lineterm="", n=0) if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    assert len(changed) == 4 and any("float(a[0])" in l for l in changed)                  # one cast and one comment
    d = json.load(open(A / "verification" / "adjoint_higgs.json"))
    assert d["S1"]["max_rel_vs_table"] < 1e-25 and d["S1"]["max_asym_rel"] < 1e-25 and d["S1"]["min_abs_diag_rel"] > 0.1
    assert all(abs(v["min_dist_to_golden"] - 0.381966) < 1e-5 for k, v in d["S3a"].items() if k != "overall_min_dist_to_golden")
    assert d["S3c"]["rank_of_spectrum_map"] == 1
    r = json.load(open(A / "verification" / "post_seal_ratio.json"))
    assert all(abs(v["real"]["m_min"] - 0.5) < 1e-6 and v["complex"]["m_min"] < 0.01 for v in r.values())
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "NEGATIVE"


def test_the_determinant_and_jacobi_and_the_bite():
    ai, aj, ak, Ri, Rj, Rk = sp.symbols("a_i a_j a_k R_i R_j R_k")
    Y = (ai * sp.Matrix([[-Ri, Rj, 0], [Rj, Ri, Rk], [0, Rk, -Ri]]) + aj * sp.Matrix([[Rj, Ri, Rk], [Ri, -Rj, 0], [Rk, 0, -Rj]])
         + ak * sp.Matrix([[-Rk, 0, Rj], [0, -Rk, Ri], [Rj, Ri, Rk]]))
    assert sp.expand(Y.det() - (Ri**2 + Rj**2 + Rk**2) * (ai**2 + aj**2 + ak**2) * (Ri * ai + Rj * aj + Rk * ak)) == 0
    t = complex(0.13, 1.21); n = np.arange(-40, 41); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    R = np.array([-th2 ** 2, -th4 ** 2, 1j * th3 ** 2])
    assert abs(np.sum(R * R)) / np.sum(np.abs(R) ** 2) < 1e-12                                # isotropic (Jacobi)
    Rn = np.array([1.0, 0.7 + 0.2j, -0.3j])
    assert abs(np.sum(Rn * Rn)) > 0.1                                                         # bite: a generic R is not
