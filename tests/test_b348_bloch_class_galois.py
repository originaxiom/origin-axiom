"""B348 lock -- gate A extension: the Bloch/scissors class is a self-symmetrized Galois orbit.

The class beta = 2[e^{i pi/3}] over the Eisenstein end: the Galois action swaps the P12
Eisenstein roots; the seam identity 1 - z0 = conj(z0) makes the generic Bloch duality
involution and the arithmetic conjugation the SAME map at the object's shape; the orbit is
{+Vol, -Vol} with sum 0; and the residual sign (= orientation) is killed by the object's own
amphichirality (P9/B318). No forced choice in this class. CONDITIONAL per the C-guardrail;
extended-Bloch/K3 torsion stays untested; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = (pathlib.Path(__file__).resolve().parents[1] / "frontier"
         / "B348_bloch_class_galois" / "bloch_class_galois.py")
_spec = importlib.util.spec_from_file_location("b348", _PATH)
b348 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b348)


def test_galois_swaps_the_P12_eisenstein_roots():
    both_roots, distinct = b348.galois_swaps_the_eisenstein_roots()
    assert both_roots and distinct


def test_the_seam_identity_is_exact():
    exact, forced = b348.seam_identity()
    assert exact      # 1 - z0 == conj(z0), exactly
    assert forced     # z(1-z) = 1  <=>  z^2 - z + 1 = 0 (the locus is exactly the Eisenstein quadratic)


def test_orbit_is_symmetrizable_with_volume_magnitude():
    orbit, sum_zero, vol_match = b348.orbit_is_symmetrizable()
    assert sum_zero                                # sum of the orbit = 0 (canonical)
    assert vol_match                               # |member| = Vol(4_1), recomputed independently
    assert orbit[0] > 0 > orbit[1]                 # a genuine +- pair, not a degenerate orbit


def test_sign_is_orientation_and_amphichirality_kills_it():
    cs_zero, d_vanishes_on_fixed_field = b348.sign_is_the_orientation_and_the_object_kills_it()
    assert cs_zero
    assert d_vanishes_on_fixed_field


def test_consistency_with_the_proven_core_constants():
    # the probe's volume equals the P9 anchor without importing it from the probe
    from origin_axiom.constants import VOL_FIG8
    orbit, _, _ = b348.orbit_is_symmetrizable()
    assert abs(float(orbit[0]) - VOL_FIG8) < 1e-12
