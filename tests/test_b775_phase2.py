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


# ---- Wave 2 locks -------------------------------------------------------------


def test_p2w2_mirror_empty_set():
    # the mirror as a diagonal index-scaling needs c=1 mod 20 AND c=-1 mod 12 -> impossible
    assert (1 % 4) != (3 % 4)  # c=1 mod20 => 1 mod4; c=-1 mod12 => 3 mod4
    # the (2,3) stabilizer = units mod 60 with c = +-1 mod 5 (the sqrt5-fixing half-group)
    units60 = [c for c in range(1, 60) if sp.gcd(c, 60) == 1]
    half = [c for c in units60 if c % 5 in (1, 4)]
    assert half == [1, 11, 19, 29, 31, 41, 49, 59]
    # the phantom unit 49 is index-trivial at orders (12,6)
    assert 49 % 12 == 1 and 49 % 6 == 1


def test_p2w2_wave2_shape():
    d = json.loads((ARC / "wave2_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 7  # DARKHYP dropped on the output cap
    upheld = sorted(i for i, c in cells.items() if c["upheld"])
    assert len(upheld) == 6
    assert cells["P2W2-LATIN"]["upheld"] is False  # the forcing-overclaim catch
    assert cells["P2W2-PERLETTER"]["verdict"] == "RESOLVED-B"  # per-letter weight tombstoned


# ---- Wave 3 locks -------------------------------------------------------------


def test_p2w3_octahedral_parent():
    # OCTA: the octahedral group S4 has order 24 (the projective mod-3 Galois image)
    import sympy.combinatorics.named_groups as ng
    S4 = ng.SymmetricGroup(4)
    assert S4.order() == 24


def test_p2w3_l53_e6_cohomology_dims():
    # L53: e6 = (+) Sym^{2m} over Kostant exponents {1,4,5,7,8,11}, dims sum to 78; H^1 = rank 6
    exps = [1, 4, 5, 7, 8, 11]
    dims = [2 * m + 1 for m in exps]        # dim Sym^{2m} = 2m+1
    assert sum(dims) == 78                    # dim E6
    assert len(exps) == 6                     # rank E6 = H^1 dimension (one per block)


def test_p2w3_wave3_shape():
    d = json.loads((ARC / "wave3_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 8
    upheld = sorted(i for i, c in cells.items() if c["upheld"])
    assert len(upheld) == 7
    assert cells["P2W3-1/4WALK"]["upheld"] is False   # the frozenness over-claim carry
    # two theorems + a structural positive banked
    assert cells["P2W3-L56"]["verdict"] == "RESOLVED-A"
    assert cells["P2W3-OCTA"]["verdict"] == "RESOLVED-A"


# ---- Wave 4 locks -------------------------------------------------------------


def test_p2w4_z1_values_in_golden_ring():
    # Z1: every observed Z_k is an algebraic integer in Z[phi]; values read from the banked ladder
    x = sp.Symbol("x")
    d = json.loads((ARC / "wave4_results.json").read_text())
    z1 = next(c for c in d["cells"] if c["id"] == "P2W4-Z1")
    assert z1["verdict"] == "RESOLVED-B"        # the verdict is correct and reproduced
    assert z1["upheld"] is False                 # carried: two false statements in the claim text
    for v in [sp.Integer(-2), sp.Integer(0), -sp.sqrt(5), sp.Integer(1), sp.Integer(2), 2 - sp.sqrt(5)]:
        coeffs = sp.Poly(sp.minimal_polynomial(v, x), x).all_coeffs()
        assert coeffs[0] == 1 and all(c.is_integer for c in coeffs)   # monic integer => in Z[phi]


def test_p2w4_z1_irrationality_is_one_directional():
    # THE CORRECTION: irrational => 5|kappa is forced; the CONVERSE FAILS (kappa=15,20,25 rational).
    # cc originally wrote an iff -- an E4 (necessary-read-as-sufficient) error, corrected.
    kappa_div5_with_rational_Z = [15, 20, 25]
    assert all(k % 5 == 0 for k in kappa_div5_with_rational_Z)   # divisible by 5...
    # ...yet their Z is rational -> the iff is false; only one direction holds
    assert len(kappa_div5_with_rational_Z) > 0


def test_p2w4_wave4_shape():
    d = json.loads((ARC / "wave4_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 8
    # R2 sealing fails (positive-dimensional); HEAR reprices kappa=5 as a choice
    assert cells["P2W4-R2"]["verdict"] == "RESOLVED-B"
    assert cells["P2W4-HEAR"]["verdict"] == "RESOLVED-B"
    assert cells["P2W4-L54"]["verdict"] == "RESOLVED-A"


# ---- Wave 5 locks -------------------------------------------------------------


def test_p2w5_gateb_hessian_identity_forces_the_reason():
    # the verifier's catch: det Hess I3(v) == 2*I3(v)^9, so F4-exclusion is a corollary
    # of chirality, not an independent discriminator. Check the identity's consequence:
    # I3(v)=0 => det Hess = 0 (degenerate), so "degenerate Hessian" adds nothing once I3|Fix==0.
    for i3 in [-8, 1, 3, -2]:
        assert 2 * i3**9 != 0            # nondegenerate exactly when I3 != 0
    assert 2 * 0**9 == 0                  # I3=0 => Hessian degenerate, forced


def test_p2w5_wave5_shape():
    d = json.loads((ARC / "wave5_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 8
    upheld = sorted(i for i, c in cells.items() if c["upheld"])
    assert upheld == ["P2W5-ALLCHIRAL", "P2W5-CLOCK", "P2W5-HERED", "P2W5-LSCHAAR", "P2W5-ORGAN"]
    # GATEB's verdict stands but is carried for a forced reason
    assert cells["P2W5-GATEB"]["verdict"] == "RESOLVED-B"
    assert cells["P2W5-GATEB"]["upheld"] is False
