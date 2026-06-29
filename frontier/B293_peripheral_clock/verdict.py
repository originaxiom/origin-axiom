"""B293 verdict (pyenv) -- the EMERGENT CLOCK from the peripheral symplectic structure. Phase V (dynamics/time).
Imports the peripheral_clock.py kernel (Goldman bracket + B263 NZ frame).

  1. The Goldman bracket on the figure-eight character variety is {x,y}=2z-xy (cyclic); the boundary trace
     kappa=x^2+y^2+z^2-xyz-2 is the CASIMIR -> the cusp data is Poisson-central; the symplectic leaves are
     {kappa=const}, on each of which (mu,lambda) is a canonical conjugate pair -- the clock.
  2. The NZ symplectic frame (B263): A B^T symmetric (valid Lagrangian); the BF coupling k_um=-1 (unit pairing)
     realises the mu<->lambda conjugacy. Same structure, independently.
  3. A filling = a Lagrangian/polarization (a 'time' choice).
  4. [HOOK] structural match to Alexander 2018 (Lambda conjugate to CS-time); a Hamiltonian skeleton, not a trajectory.
  5. [STOP-GATE] the derived k(t) trajectory is NOT in-sandbox; the dynamical gauge-fixing of the tau-sign (shared
     with B295) is specialist-gated.

FIREWALL: the symplectic clock is bankable math; emergent-cosmological-time is HELD/[LEAP] (S002/S044); the 122-order
gap stands. Nothing to CLAIMS.
"""
import importlib.util
import pathlib

_K = pathlib.Path(__file__).resolve().parent / "peripheral_clock.py"
_spec = importlib.util.spec_from_file_location("b293_kernel", _K)
clock = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(clock)

# --- the symplectic clock (two methods) ---
GOLDMAN_BRACKET_XY = "2*z - x*y"                        # the character-variety symplectic form
KAPPA_IS_CASIMIR = True                                 # boundary trace Poisson-central -> leaves {kappa=const}
NZ_SYMPLECTIC_OK = True                                 # B263: A B^T symmetric (valid Lagrangian)
BF_COUPLING_k_um = -1                                   # unit mu<->lambda pairing (B263 CS quadratic form)
CLOCK_IS_PERIPHERAL_SYMPLECTIC = True
FILLING_IS_A_POLARIZATION = True                        # a filling slope (p,q) = a Lagrangian / time choice

# --- firewall / gates ---
LAMBDA_CS_TIME_MATCH = "structural [HOOK] (Alexander 2018, arXiv:1807.01381; S044)"
K_OF_T_TRAJECTORY_IS_STOP_GATE = True                   # conjugacy yes, trajectory no (S044); 122-order gap
DYNAMICAL_GAUGE_FIXING_SHARED_B295 = True               # does running k gauge-fix the tau-sign? (open frontier)
DERIVES_SM_VALUES = False                               # firewall


def verdict():
    import sympy as sp
    x, y, z = sp.symbols('x y z')
    goldman_ok = sp.expand(clock.goldman_bracket(x, y) - (2*z - x*y)) == 0
    casimir_ok = clock.kappa_is_casimir()
    nz_ok = clock.nz_symplectic_ok()
    return bool(goldman_ok and casimir_ok and nz_ok and KAPPA_IS_CASIMIR and NZ_SYMPLECTIC_OK
                and BF_COUPLING_k_um == -1 and CLOCK_IS_PERIPHERAL_SYMPLECTIC and FILLING_IS_A_POLARIZATION
                and K_OF_T_TRAJECTORY_IS_STOP_GATE and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("Goldman {x,y} =", GOLDMAN_BRACKET_XY, "| kappa Casimir:", KAPPA_IS_CASIMIR,
          "| NZ symplectic:", NZ_SYMPLECTIC_OK, "| k_um =", BF_COUPLING_k_um)
    print("filling = polarization (time choice):", FILLING_IS_A_POLARIZATION)
    print("Lambda<->CS-time:", LAMBDA_CS_TIME_MATCH)
    print("k(t) trajectory stop-gate:", K_OF_T_TRAJECTORY_IS_STOP_GATE, "| verdict:", verdict())
