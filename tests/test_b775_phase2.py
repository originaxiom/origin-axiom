"""B775 Phase 2 Wave 1 -- locks on the structural results."""
import json
import pathlib

import sympy as sp

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B775_phase2_wave1"


def test_p2aabb_gamma5_derives_from_sigma():
    # the incidence matrix of sigma:a->ab has discriminant EXACTLY 5 -> Gal(Q(sqrt5)) = gamma5
    lam = sp.symbols("lambda")
    M = sp.Matrix([[1, 1], [1, 0]])
    cp = M.charpoly(lam).as_expr()
    assert cp == lam**2 - lam - 1
    assert sp.discriminant(cp, lam) == 5
    assert M.det() == -1  # phi*(1-phi)


def test_p2aabb_c_does_not_derive():
    # a<->b swap is NOT a sigma-automorphism: sigma(a)=ab, and swap-conjugation gives a->ba != ab
    sigma = {"a": "ab", "b": "a"}
    swap = {"a": "b", "b": "a"}
    # s . sigma . s applied to 'a': swap(sigma(swap('a'))) = swap(sigma('b')) = swap('a') = 'b'... image word
    conj = "".join(swap[ch] for ch in sigma[swap["a"]])  # swap(sigma(b)) = swap('a')='b'
    assert conj != sigma["a"]  # 'b' != 'ab' -> not an automorphism, c does not derive


def test_p2weld_minus_inv_phi_is_conjugate():
    # -1/phi = 1 - phi, the ubiquitous Galois conjugate (base-rate, dismissed)
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(-1 / phi - (1 - phi)) == 0


def test_p2_wave1_all_upheld():
    d = json.loads((ARC / "wave1_results.json").read_text())
    cells = d["cells"]
    assert len(cells) == 7
    assert all(c["upheld"] for c in cells)
    verds = {c["id"]: c["verdict"] for c in cells}
    assert verds["P2-T1MOVER"] == "RESOLVED-B"      # WALLED
    assert verds["P2-SELRULE"] == "RESOLVED-A" if "P2-SELRULE" in verds else True
    # the three tombstones
    tomb = [c for c in cells if c.get("terminal_state", "").startswith("DISMISSED")]
    assert len(tomb) == 3
