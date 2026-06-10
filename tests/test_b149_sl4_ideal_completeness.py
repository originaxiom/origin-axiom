"""B149 -- completeness of the SL(4) {1,1,w,w^2} defining ideal. Pure-sympy core + read-back of the committed
decomposition / irreducibility artifacts. (The Sage decomposition + F_p classification themselves are not re-run here.)"""
import json
import pathlib

from frontier.B149_sl4_ideal_completeness.probe import (
    b89_family_lies_in_variety,
    defining_ideal_generators,
    m4_equals_l_on_b89_family,
    q_zero_forces_reducible,
)

HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B149_sl4_ideal_completeness"


def test_consistency_gate_b89_family_in_variety():
    """The generic defining ideal is the same object B89 proved on: B89's posited family lies in V(I)."""
    assert b89_family_lies_in_variety() is True


def test_defining_ideal_has_ten_generators():
    gens, _ = defining_ideal_generators()
    assert len(gens) == 10


def test_m4_equals_l_identity_on_family():
    holds, _det = m4_equals_l_on_b89_family()
    assert holds is True


def test_q_zero_forces_reducible_exhibited():
    """EXHIBITED: on the Q=0 stratum, span(e2,e3) is invariant under A, t, and B -> reducible (MB7-filtered)."""
    assert q_zero_forces_reducible() is True


def test_decomposition_artifact_principal_stratum():
    """The committed symbolic decomposition: the Q-invertible (principal) stratum has exactly 2 components, both M^4=L,
    one genuine (det t != 0) = B89's family and one vacuous (det t = 0)."""
    d = json.loads((HERE / "decomposition.json").read_text())
    s = d["strata"]["rankQ2_Qinv"]
    assert s["n_components"] == 2
    assert all(c["m4_equals_l"] for c in s["components"])
    genuine = [c for c in s["components"] if not c["det_t_vanishes"]]
    vacuous = [c for c in s["components"] if c["det_t_vanishes"]]
    assert len(genuine) == 1 and len(vacuous) == 1            # B89's family + the vacuous branch
    assert d["verdict"]["all_strata_decomposed"] is True


def test_irreducibility_artifact_outcome_a():
    """The committed exact-over-F_p Burnside classification: the decisive cell (irreducible AND M^4=L fails) is EMPTY,
    and the ONLY stratum carrying irreducible reps is B89's rank-Q2 family -> M^4=L unconditional on the irreducible
    locus (OUTCOME a)."""
    a = json.loads((HERE / "irreducibility_fp.json").read_text())
    assert a["decisive_cell_irreducible_and_M4L_fails"] == 0
    assert a["verdict"] == "CLEAN"
    assert a["only_stratum_with_irreducible_reps"] == ["rankQ2 (Q=I2,B89)"]
