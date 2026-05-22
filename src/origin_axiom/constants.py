"""
Verified constants for the Origin Axiom proven core.

Exact (symbolic) where possible; floating-point values are literature / SnapPy
results carried as test anchors. See ``CLAIMS.md``.
"""

import sympy as sp

# --- Golden ratio (exact) --------------------------------------------------
PHI = sp.Rational(1, 2) + sp.sqrt(5) / 2          # (1 + sqrt 5) / 2
PHI_SQ = sp.expand(PHI**2)                        # = PHI + 1 = (3 + sqrt 5) / 2

# --- Numerical anchors -----------------------------------------------------
PHI_FLOAT = float(PHI)                            # 1.6180339887498949
LOG_PHI_SQ = float(sp.log(PHI_SQ))                # 0.9624236501192069

# --- Figure-eight knot complement (4_1) — SnapPy / literature values -------
# Used by claim P9. Hard-coded so the algebra/statistics tests need no SnapPy.
VOL_FIG8 = 2.0298832128193072                     # hyperbolic volume (minimal)
CS_FIG8 = 0.0                                     # Chern-Simons invariant
CS_SISTER = 0.25                                  # Chern-Simons invariant of sister m003
