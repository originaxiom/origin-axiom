"""B502 lock -- CL-3C / Gate C: the commensurator Z/3 vs its WRITTEN refutation condition.
Verdict: CLOSES.

Locks (i) the verbatim refutation condition against the live docs/OPEN_PROBLEMS.md; (ii) the
prereg CONTROLS (B302's location of the Z/3: object none / commensurator yes / index 12; B326's
H1(3-fold cover) = Z + (Z/4)^2 with irreducible Phi_3 deck action) -- fail => probe INVALID;
(iii) the exact identification torsion = Z[w]/4 with deck = mult-by-w, and the three-copies
refutation (Fix = 0, chain lattice, 16 not a cube, no Phi_3 root mod 2); (iv) the exact E6
omega-grading (0/6084 violations, 24+27+27, fixed = three orthogonal A2's) and the 27's 9+9+9
bifundamental trinification blocks in BOTH banked frames; (v) the (theta,phi) triality
3-cycling the blocks WITHIN the single 27 (B299 reproduced); (vi) the B329 branchings with the
2T order-3 eigen-multiplicities (9,9,9)/(15,6,6) within the one 27; (vii) the verdict CLOSES
with every realization on the CLOSES branch, and the FINDINGS integrity (verbatim condition +
firewall line). SnapPy behind importorskip in the two live-geometry locks, like the sibling
locks; everything else exact sympy/integer. Nothing to CLAIMS.md."""
import importlib.util
import pathlib

import pytest

sp = pytest.importorskip("sympy")

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_DIR = _ROOT / "frontier" / "B502_gateC_commensurator"

_spec = importlib.util.spec_from_file_location("b502_probe", _DIR / "probe.py")
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)                     # loads B302/B326/B329/B351/B299 via importlib


# ---------------- (i) the written condition is quoted verbatim ----------------
def test_refutation_condition_matches_open_problems_verbatim():
    doc = (_ROOT / "docs" / "OPEN_PROBLEMS.md").read_text()
    assert " ".join(P.REFUTATION_CONDITION.split()) in " ".join(doc.split())
    assert P.ENUM == ("OPENS", "CLOSES", "BLOCKED")


# ---------------- (ii) controls: fail => INVALID ----------------
def test_control_b302_banked_reproduction():
    c = P.control_b302(with_snappy=False)
    assert c["order3_matrix"] and c["eisenstein_unit_order3"]     # order-3 in PGL(2,O_-3)
    assert abs(c["cover_index"] - 12) < 0.5                       # Riley index 12 (Humbert)
    assert c["banked_verdict"]


def test_control_b302_object_has_no_order3_snappy():
    pytest.importorskip("snappy")
    c = P.control_b302(with_snappy=True)
    assert c["sym_order"] == 8 and c["sym_full"]                  # D4 = 2^3: no order-3


def test_control_b326_exact_alexander():
    c = P.control_b326(with_snappy=False)
    assert (c["disc"], c["torsion_order"]) == (5, 16)             # sqrt5 end; |torsion| = 16
    assert c["delta_mod4"] == [1, 1, 1]                           # Delta mod 4 = Phi_3
    assert c["snf"] == [[4, 0], [0, 4]]                           # (Z/4)^2
    assert c["deck_charpoly_mod4"] == [1, 1, 1] and c["deck_order3"]


def test_control_b326_cover_h1_snappy():
    pytest.importorskip("snappy")
    c = P.control_b326(with_snappy=True)
    assert c["n_cyclic_covers"] == 1                              # the unique 3-fold cyclic cover
    assert c["cover_h1"] == "Z/4 + Z/4 + Z"


# ---------------- (iii) the deck Z/3: one Eisenstein copy, not three ----------------
def test_torsion_is_the_rank_one_eisenstein_module():
    e = P.eisenstein_module_facts()
    assert e["phi3_minus_delta_is_4t"]                            # t^2+t+1 = 0 exactly on M
    assert e["delta_at_1"] == -1                                  # (t-1)-part vanishes
    assert e["delta_at_w_is_minus_4w"] and e["norm_delta_at_w"] == 16    # M = Z[w]/4
    assert e["snf_of_Zt_mod_delta_phi3"] == [[4, 0], [0, 4]]
    assert e["deck_satisfies_phi3_mod4"] and e["deck_order3_mod4"]       # deck = mult-by-w
    assert e["one_ramified_3"] and e["norm_1_minus_w"] == 3       # (1-w)^2 = -3w: the ONE 3


def test_deck_does_not_permute_three_copies():
    d = P.deck_three_copies_test()
    assert d["fixed_points"] == [(0, 0)]                          # permutation module needs
    assert not d["order_is_a_cube"]                               #   Fix = diagonal != 0,
    assert d["phi3_roots_mod2"] == []                             #   |A|^3, eigenvalue 1 mod 2
    assert d["invariant_subgroup_orders"] == [1, 4, 16]           # the full lattice, brute-forced
    assert d["lattice_is_chain"]                                  # 0 < 2M < M: no 3-splitting
    assert d["acts_irreducibly_within_one_module"] and not d["permutes_three_copies"]


# ---------------- (iv) the exact E6 grading and the trinification blocks ----------------
def test_omega_grading_is_an_exact_z3_automorphism():
    g = P.grading_is_z3_automorphism()
    assert g["violations"] == 0 and g["table_entries"] == 6084    # graded bracket, exact
    assert g["eigenspace_dims"] == (24, 27, 27)                   # su(3)^3 + 27 + 27bar
    assert g["deg1_deg2_are_conjugate"]                           # ONE 27 + conjugate, not copies


@pytest.mark.parametrize("frame", ["bourbaki_b351", "b299"])
def test_fixed_su3_cubed_and_27_blocks(frame):
    C = (P.b351.A if frame == "bourbaki_b351"
         else [[int(P.b299.E6_CARTAN[i, j]) for j in range(6)] for i in range(6)])
    f = P.fixed_subalgebra_is_a2_cubed(C)
    assert f["n_components"] == 3 and f["each_is_A2"] and f["mutually_orthogonal"]
    assert f["fixed_dim"] == 24
    b = P.blocks_are_trinification_factors(C)
    assert b["block_sizes"] == {0: 9, 1: 9, 2: 9}
    assert b["bifundamental_trinification_blocks"]                # trivial under exactly one A2


def test_helper_root_system_agrees_with_b351():
    assert set(P._positive_roots(P.b351.A)) == set(P.b351.POS)


# ---------------- (v) the triality acts WITHIN the single 27 ----------------
def test_theta_phi_3cycle_the_blocks_within_one_27():
    tr = P.triality_block_action()
    assert tr["b299_reproduced"]                                  # Z3xZ3, free, 9 orbits of 3
    assert tr["theta_phi_3cycle_the_blocks"]                      # 0 -> 1 -> 2 -> 0
    assert tr["within_elements_preserve_blocks"]                  # theta*phi^2, theta^2*phi
    assert tr["all_within_one_27"]                                # never a second 27


# ---------------- (vi) the B329 branching data: within one 27, both embeddings ----------------
def test_2T_order3_eigenmults_within_the_27():
    tt = P.order3_on_the_27_via_2T()
    assert tt["branch_principal"] == {"1": 3, "1'": 3, "1''": 3, "3": 6}
    assert tt["branch_trinification"] == {"1": 9, "1'": 3, "1''": 3, "2'": 3, "2''": 3}
    assert tt["n1_eq_n2_both"]                                    # B329: Level 4 both routes
    assert tt["eig_mults_principal"] == (9, 9, 9)
    assert tt["eig_mults_trinification"] == (15, 6, 6)


def test_no_three_27_substrate():
    s = P.no_three_27_substrate()
    assert s["three_27_dim"] == 81 and s["dim_e6"] == 78 and not s["fits_in_adjoint"]
    assert s["single_object_multiplicity"] == 1                   # B307/B321
    assert s["diagram_involution_order"] == 2                     # 27 <-> 27bar, not a Z/3


# ---------------- (vii) the verdict and the FINDINGS integrity ----------------
def test_verdict_closes_every_realization_unambiguously():
    deck = P.deck_three_copies_test()
    grad = P.grading_is_z3_automorphism()
    tri = P.triality_block_action()
    twoT = P.order3_on_the_27_via_2T()
    outcomes = P.refutation_condition_outcomes(deck, grad, tri, twoT)
    assert len(outcomes) == 4
    assert all(v.startswith("CLOSES") for v in outcomes.values())   # no AMBIGUOUS -> no BLOCKED
    assert P.VERDICT == "CLOSES" and P.VERDICT in P.ENUM
    assert P.OPENS_REACHED is False                                  # no owner escalation
    assert "sage/magma" in P.RESIDUAL_NOT_COMPUTED                   # the residual stays named


def test_findings_integrity():
    text = (_DIR / "FINDINGS.md").read_text()
    assert "CLOSES" in text
    # verbatim quote (whitespace-normalized; drop the markdown blockquote markers)
    norm = " ".join(w for w in text.split() if w != ">")
    assert " ".join(P.REFUTATION_CONDITION.split()) in norm
    assert "Nothing to `CLAIMS.md`; firewall untouched." in text
