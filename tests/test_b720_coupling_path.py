"""B720 — the three NO-MATCH discriminating facts, COMPUTED (B830).

Replaces a label-lock. The original test asserted that three hardcoded strings were distinct --
it verified that three different strings had been typed, and could only fail if someone edited
the dict to repeat one (B828). These locks run the computations instead.
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b830", ROOT / "frontier" / "B830_b720_recompute" / "cells.py")
c = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c)


def test_nomatch_1_the_cyclotomic_branches_are_disjoint():
    """Eisenstein Q(zeta_3) vs Gaussian Q(i): they meet only in Q."""
    r = c.a1_branch_mismatch()
    assert r["same_field"] is False
    assert r["compositum_degree"] == 4          # so neither contains the other
    assert r["intersection_is_Q"] is True
    assert r["REFUTED"] is False


def test_nomatch_3_markov_is_finite_mutation_but_NOT_finite_type():
    """ABHY positive geometry needs finite TYPE; the object's quiver is finite MUTATION only."""
    r = c.a2_markov_finite_mutation_not_finite_type()
    assert r["mutation_finite"] is True
    assert r["mutation_class_size"] == 1        # self-mutating up to iso
    assert r["finite_type"] is False
    assert r["REFUTED"] is False


def test_the_finite_type_detector_actually_works():
    """Positive control: without it, finite_type=False could just mean the detector is broken."""
    r = c.a2_markov_finite_mutation_not_finite_type()
    assert r["control_A3_finite_type"] is True, "an A3 Dynkin quiver MUST register as finite type"
    assert r["control_A3_class_size"] == 4


def test_nomatch_2_flat_connection_moduli_is_finite_dimensional():
    """A local field theory has a function's worth of DOF per point; this is finite."""
    r = c.a3_no_local_dof()
    assert r["finite_dimensional"] is True
    assert r["dim_H1_E6"] == 6 and r["dim_H1_SL2_geometric"] == 1
    assert r["REFUTED"] is False


def test_the_cited_residue_is_still_labelled_as_cited():
    """A1 computes the OBJECT's side only. That Connes-Marcolli's cosmic Galois is mixed-Tate
    over Z[i] is a fact about ANOTHER construction and is not computable here -- calling the
    composite claim 'computed' would be the necessary-vs-sufficient error B525 exists to catch."""
    f = " ".join((ROOT / "frontier" / "B830_b720_recompute" / "FINDINGS.md").read_text(
        encoding="utf-8").split())
    assert "PART-COMPUTED, PART-CITED" in f or "part-computed, part-cited" in f
