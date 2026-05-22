"""
Frontier probe B1 — the gluing identity vs. discrete Chern-Simons flatness.

  SPECULATIVE FRONTIER WORK.  Outputs here are *logged observations*, not claims.
  See ../../GOVERNANCE.md sec. 5 and ./README.md.

Question (ROADMAP.md, probe B1):
  Does the boundary-to-bulk gluing identity
        W(q, m, s, Q) = S_L(m, Q) - F_R(q, s) + m*s
  map onto a discrete Chern-Simons flatness condition F = 0?

In Witten's 2+1 gravity the gauge connection splits as  A_conn = omega + e
(omega = spin connection, e = dreibein/frame field); the equation of motion is
flatness  F(A_conn) = 0.  This probe runs the two computations that can be done
*exactly*, then states honestly how far they get and where they stop.

Run:  python frontier/B1_gluing_chern_simons/probe.py
"""

import numpy as np
import sympy as sp

from origin_axiom.gluing import on_shell_gluing, S_A

PHI = (1 + 5 ** 0.5) / 2
LOG_PHI2 = np.log(PHI ** 2)

# --- sl(2,R) basis ---------------------------------------------------------
H = np.array([[1.0, 0.0], [0.0, -1.0]])      # boost generator  -> spin connection
E = np.array([[0.0, 1.0], [0.0, 0.0]])
F = np.array([[0.0, 0.0], [1.0, 0.0]])
FRAME = E + F                                # symmetric frame generator
TORSION = E - F                              # antisymmetric part


def computation_1_frame_spin_decomposition():
    """Decompose log(A) into spin-connection (H) and frame (E+F) parts."""
    from scipy.linalg import logm

    A = np.array([[2.0, 1.0], [1.0, 1.0]])
    log_A = logm(A).real

    # Closed-form claim:  log A = (log phi^2 / sqrt 5) * (H + 2*(E+F))
    a = LOG_PHI2 / np.sqrt(5)                 # spin-connection coefficient
    d = 2 * LOG_PHI2 / np.sqrt(5)             # frame coefficient
    claim = a * H + d * FRAME
    max_err = np.max(np.abs(claim - log_A))

    # Torsion component = coefficient of the antisymmetric generator E - F.
    # log A is symmetric => zero torsion component.
    torsion_coeff = np.sum(log_A * TORSION) / np.sum(TORSION * TORSION)

    return {
        "log_A": log_A,
        "spin_coeff_a": a,
        "frame_coeff_d": d,
        "frame_to_spin_ratio": d / a,
        "reconstruction_error": max_err,
        "torsion_coeff": torsion_coeff,
    }


def computation_2_gluing_is_composition():
    """The gluing identity, re-read as a holonomy composition law."""
    q, Q = sp.symbols("q Q", real=True)
    on_shell = sp.expand(on_shell_gluing(q, Q))
    target = sp.expand(S_A(q, Q))
    identity_holds = sp.expand(on_shell - target) == 0

    # The extremised intermediate data (m, s) is the *shared edge* between the
    # two half-moves: m = q, s = Q - q  (from dW/dm = dW/ds = 0).
    m, s = sp.symbols("m_int s_int", real=True)
    from origin_axiom.gluing import gluing_functional

    W = gluing_functional(q, m, s, Q)
    sol = sp.solve([sp.diff(W, m), sp.diff(W, s)], [m, s], dict=True)[0]
    return {"identity_holds": identity_holds, "shared_edge": sol}


def main():
    print("=" * 72)
    print("Frontier probe B1 — gluing identity vs. discrete CS flatness")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md sec. 5)")
    print("=" * 72)

    c1 = computation_1_frame_spin_decomposition()
    print("\n[1] Frame / spin-connection decomposition of log(A)")
    print(f"    log A      = (log phi^2 / sqrt5) * (H + 2*(E+F))")
    print(f"    spin coeff a               = {c1['spin_coeff_a']:.10f}")
    print(f"    frame coeff d              = {c1['frame_coeff_d']:.10f}")
    print(f"    frame-to-spin ratio d/a    = {c1['frame_to_spin_ratio']:.10f}")
    print(f"    reconstruction error       = {c1['reconstruction_error']:.2e}  (vs scipy logm)")
    print(f"    torsion coeff (E-F part)   = {c1['torsion_coeff']:.2e}  -> torsion-free")

    c2 = computation_2_gluing_is_composition()
    print("\n[2] Gluing identity as a holonomy composition law")
    print(f"    S_A = ext[S_L - F_R + m*s] holds : {c2['identity_holds']}")
    print(f"    extremised shared edge (m,s)     : {c2['shared_edge']}")

    print("\n[verdict]  See README.md. In brief: the gluing reproduces the")
    print("holonomy-composition structure that discrete flatness encodes, and")
    print("log(A) splits cleanly into a torsion-free frame + spin connection.")
    print("It does NOT produce the Chern-Simons action or its level k. B1 is")
    print("a qualified-yes at the holonomy level; the CS-action map stays open.")


if __name__ == "__main__":
    main()
