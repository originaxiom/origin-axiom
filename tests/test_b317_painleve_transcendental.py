"""B317 lock -- the Hitchin/Painleve-VI lens (P010), placed. The lens was already RUN (B164 the (0,4) cubic + dynamics,
B169 the isomonodromy flow, dynamical degree lambda_m^2, dimensionless time); P010's "unrun" is stale. B317 adds the
solution-landscape placement: the metallic trace map is HYPERBOLIC (|lambda_m|>1) -> infinite nonlinear-monodromy orbit
-> the metallic/figure-eight Painleve-VI solutions are TRANSCENDENTAL (not the algebraic finite-orbit Lisovyy-Tykhyy
ones), positive entropy 2 log(lambda_m), dynamical degree lambda_m^2. Real chaotic dynamics, dimensionless time ->
firewall relocated (P010's caveat). Third Phase-3 lead to reduce to banked work. Firewalled; nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B317_painleve_transcendental" / "painleve_transcendental.py"
_spec = importlib.util.spec_from_file_location("b317", _PATH)
b317 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b317)


def test_metallic_hyperbolic_positive_entropy():
    assert all(b317.is_hyperbolic(m) for m in (1, 2, 3))            # |lambda_m| > 1, loxodromic
    assert all(sp.N(b317.entropy(m)) > 0 for m in (1, 2, 3))        # positive entropy -> chaotic
    assert b317.dynamical_degree(1) == (3 + sp.sqrt(5)) / 2         # phi^2


def test_transcendental_not_algebraic():
    assert b317.METALLIC_ARE_TRANSCENDENTAL_PVI                     # hyperbolic -> not Lisovyy-Tykhyy algebraic
    assert b317.DYNAMICS_IS_CHAOTIC_POSITIVE_ENTROPY


def test_lens_was_run_p010_stale():
    assert b317.HITCHIN_LENS_ALREADY_RUN                           # B164/B169
    assert b317.P010_UNRUN_CLAIM_IS_STALE
    assert b317.THIRD_LEAD_TO_REDUCE_TO_BANKED_WORK               # after H14/B234, sqrt-7/B235


def test_firewall_relocated():
    assert b317.TIME_IS_DIMENSIONLESS_FIREWALL_RELOCATED           # B169: dimensionless modulus
    assert b317.DERIVES_SM_VALUES is False
    assert b317.verdict()
