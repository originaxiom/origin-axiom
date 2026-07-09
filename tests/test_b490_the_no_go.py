"""Locks for B490 (the no-go theorem T-NOGO-DGG).

Documentation-integrity lock, not a recompute: B490 is a FINDINGS-only meta node that
states the theorem organizing the twelve sourced kills (the per-kill computations are
locked at their own B-nodes). Asserts the load-bearing verdict lines: the three
independent reasons of T-NOGO-DGG, the kills it subsumes, the honest strength labels
(firewall = empirical law, NOT a proof), and the negative-result firewall (nothing to
CLAIMS.md). One exact arithmetic corollary IS recomputed: the K5 wrong-value kill
(no fifth root of unity in the cyclic group of 12th roots, since 5 does not divide 12).
"""
import math
import pathlib

_FIND = (pathlib.Path(__file__).resolve().parents[1]
         / "frontier" / "B490_the_no_go" / "FINDINGS.md").read_text(encoding="utf-8")


def test_theorem_named_and_registered():
    assert "T-NOGO-DGG" in _FIND
    assert "To register: T-NOGO-DGG in docs/THEOREM_REGISTRY.md" in _FIND


def test_three_reasons_of_the_theorem():
    assert "**Dimension (unassailable).**" in _FIND
    assert "T[M] is a 3-dimensional N=2 theory; the SM is a 4-dimensional chiral" in _FIND
    assert "**Flavor, not gauge (Gang–Yonekura, arXiv:1803.04009).**" in _FIND
    assert "**Abelian gauge (Dimofte–Gaiotto–Gukov 2011; verified B488).**" in _FIND
    assert "U(1)^{N−c}" in _FIND and "SU(3)×SU(2) is nonabelian" in _FIND


def test_theorem_subsumes_the_dgg_kills_and_closes_the_route():
    assert "This one theorem subsumes K9, K10, K11, K12" in _FIND
    assert 'the DGG route is closed, not "not yet found."' in _FIND


def test_kill_catalog_complete():
    for k in [f"| K{i} |" for i in range(1, 13)] + ["| K13* |", "| K14* |"]:
        assert k in _FIND, k


def test_honest_strength_labels():
    # the organizing firewall is explicitly NOT promoted to a theorem
    assert "an empirical law, 12/12 — NOT a proof" in _FIND
    assert "Three scoped obstructions (honest strength: not full theorems)" in _FIND
    assert "Does NOT (and cannot) prove" in _FIND


def test_negative_result_firewall():
    assert "nothing to CLAIMS.md" in _FIND


def test_k5_forbidden_zeta5_exact():
    # the K5 row's arithmetic, recomputed: det lands in <zeta_12>, and 5 does not divide 12,
    # so the cyclic group of 12th roots of unity has NO element of order 5 — zeta_5 FORBIDDEN
    assert "5∤12 ⇒ ζ₅ FORBIDDEN" in _FIND
    assert 12 % 5 != 0
    orders = {12 // math.gcd(k, 12) for k in range(12)}
    assert orders == {1, 2, 3, 4, 6, 12} and 5 not in orders
