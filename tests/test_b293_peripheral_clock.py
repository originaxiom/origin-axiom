"""B293 lock -- the EMERGENT CLOCK from the peripheral symplectic structure. The Goldman bracket on the figure-eight
character variety is {x,y}=2z-xy (cyclic) with the boundary trace kappa the Casimir (-> the cusp data is central, the
leaves {kappa=const} carry the (mu,lambda) conjugate pair); the NZ frame (B263) gives the same symplectic structure
(A B^T symmetric, BF coupling k_um=-1). A filling = a Lagrangian/time choice. The Lambda<->CS-time match is a [HOOK];
the k(t) trajectory is a STOP-GATE. FIREWALLED; nothing to CLAIMS.md.
(Reproducer: python frontier/B293_peripheral_clock/peripheral_clock.py.)"""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B293_peripheral_clock" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b293", _PATH)
b293 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b293)


def test_goldman_bracket_and_casimir():
    x, y, z = sp.symbols('x y z')
    assert sp.expand(b293.clock.goldman_bracket(x, y) - (2*z - x*y)) == 0      # the character-variety symplectic form
    assert b293.clock.kappa_is_casimir()                                       # boundary trace Poisson-central


def test_nz_frame_same_structure():
    assert b293.NZ_SYMPLECTIC_OK                                              # B263: A B^T symmetric (valid Lagrangian)
    assert b293.BF_COUPLING_k_um == -1                                        # unit mu<->lambda pairing


def test_clock_is_peripheral_and_filling_is_polarization():
    assert b293.CLOCK_IS_PERIPHERAL_SYMPLECTIC
    assert b293.FILLING_IS_A_POLARIZATION


def test_trajectory_stop_gate_firewall():
    assert b293.K_OF_T_TRAJECTORY_IS_STOP_GATE                                # conjugacy yes, trajectory no (S044)
    assert b293.DYNAMICAL_GAUGE_FIXING_SHARED_B295                            # shared frontier with B295
    assert b293.DERIVES_SM_VALUES is False
    assert b293.verdict()
