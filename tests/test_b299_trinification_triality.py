"""B299 lock -- the (theta,phi) Z3xZ3 is the E6 trinification triality (free 9x3 on the 27), verified self-contained;
the "H-label = phi-eigenvalue on the 27" derivation FAILS (free action -> split is external); the heterotic E6 is
generic (confirms B282). From a cross-chat handoff carrying external-heterotic material, assessed here. FIREWALLED;
nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B299_trinification_triality" / "trinification_triality.py"
_spec = importlib.util.spec_from_file_location("b299", _PATH)
b299 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b299)


def test_genuine_z3xz3_of_e6():
    assert b299.is_z3xz3()
    assert b299.fixed_dims() == (2, 2, 0)
    assert b299.preserves_E6()                          # genuine E6 lattice autos (det-3 Cartan)


def test_27_is_free_9x3_trinification_triality():
    for M in (b299.THETA, b299.PHI):
        n, fixed, sizes = b299.orbit_structure_on_27(M)
        assert n == 27 and fixed == 0 and sizes == {3: 9}
    assert b299.IS_TRINIFICATION_TRIALITY


def test_h_label_from_phi_fails():
    assert b299.H_LABEL_FROM_PHI_DERIVED is False        # free action -> no per-weight eigenvalue; split external


def test_heterotic_e6_generic_confirms_b282_firewall():
    assert b299.HETEROTIC_E6_IS_GENERIC
    assert b299.RIGOR_NEEDS_CLASS_S_E6                   # the (mu,lambda)<->(theta,phi) bridge = the CRUX gate
    assert b299.DERIVES_SM_VALUES is False
    assert b299.verdict()
