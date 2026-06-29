"""B290 verdict (pyenv; SnapPy-derived constants from core_scale_ladder.py) -- the core-geodesic SCALE LADDER and
the n-vs-k question. Phase III (wall #5, scale).

  1. POSITIVE (math): the complex core length of the (1,n) filling is ell_C(1,n) = 2*pi*i/n + (pi/sqrt(3))/n^2 + ...,
     so |ell_C| ~ 2*pi/n (confirming B286). The 1/n^2 coefficient pi/sqrt(3) = 2*pi/|tau_cusp| (tau_cusp = 2*sqrt(3)*i)
     -- the Neumann-Zagier core-geodesic ladder, cusp-shape-controlled. Two methods: SnapPy core_length + the
     coefficient PREDICTED from the cusp shape.
  2. NEGATIVE: filling n (topological surgery integer) =/= WRT level k (quantum root-of-unity q=e^{2pi i/(k+2)}, B204).
     Independent axes; 'n = k' is a formal substitution, not an identity.
  3. HELD (firewalled): under k=n, G*Lambda = 6*pi/k (S043) gives core = 2*pi/n = (G*Lambda)/3 -- a coincidence with
     the 122-order gap, NOT banked.

This module re-derives the correction coefficient (pi/sqrt(3) = 2*pi/|tau|) in pyenv sympy (gives the lock teeth).
FIREWALL: the ladder is bankable math; the n=k identity is a NEGATIVE; the G*Lambda link is HELD. Nothing to CLAIMS.
"""

# --- the ladder (SnapPy; core_scale_ladder.py) ---
CUSP_SHAPE = "2*sqrt(3)*i"                              # m004 cusp modulus
LADDER = "ell_C(1,n) = 2*pi*i/n + (pi/sqrt(3))/n^2 + O(1/n^3)"
LEADING_IS_2pi_over_n = True                            # |ell_C| ~ 2*pi/n (confirms B286)
CORRECTION_COEFF_MEASURED = 1.813786                   # Re(ell)*n^2 at n=400 (-> pi/sqrt(3))
NZ_CUSP_SHAPE_CONTROLLED = True                         # coeff = 2*pi/|tau_cusp|

# --- the n-vs-k question ---
FILLING_N_IS_TOPOLOGICAL = True                        # (1,n) Dehn surgery coefficient
WRT_LEVEL_K_IS_QUANTUM = True                          # q = e^{2*pi*i/(k+2)} root of unity (B204)
N_EQUALS_K = False                                     # independent axes; formal substitution only

# --- firewall ---
CORE_EQUALS_GLAMBDA_OVER_3_UNDER_kn = "HELD (122-order gap; S043/B259)"
DERIVES_SM_VALUES = False


def correction_coeff_from_cusp_shape():
    """pi/sqrt(3) = 2*pi/|tau_cusp| with tau_cusp = 2*sqrt(3)*i -- recomputed in sympy."""
    import sympy as sp
    tau = 2 * sp.sqrt(3) * sp.I
    return sp.simplify(2 * sp.pi / sp.Abs(tau))         # = pi/sqrt(3)


def verdict():
    import sympy as sp
    coeff = correction_coeff_from_cusp_shape()
    coeff_ok = sp.simplify(coeff - sp.pi / sp.sqrt(3)) == 0
    measured_ok = abs(float(coeff) - CORRECTION_COEFF_MEASURED) < 2e-3   # cusp-shape prediction vs SnapPy measurement
    return bool(coeff_ok and measured_ok and LEADING_IS_2pi_over_n and NZ_CUSP_SHAPE_CONTROLLED
                and FILLING_N_IS_TOPOLOGICAL and WRT_LEVEL_K_IS_QUANTUM and not N_EQUALS_K
                and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("ladder:", LADDER)
    print("correction coeff from cusp shape (sympy):", correction_coeff_from_cusp_shape(),
          " vs measured", CORRECTION_COEFF_MEASURED)
    print("filling n == WRT level k:", N_EQUALS_K, "(independent axes: topological surgery vs quantum root of unity)")
    print("core = (G*Lambda)/3 under k=n:", CORE_EQUALS_GLAMBDA_OVER_3_UNDER_kn)
    print("verdict:", verdict())
