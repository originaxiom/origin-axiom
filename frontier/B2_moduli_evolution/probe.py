"""
Frontier probe B2 — the monodromy action on the figure-eight moduli space.

  SPECULATIVE FRONTIER WORK.  Outputs are *logged observations*, not claims.
  See ../../GOVERNANCE.md sec. 5 and ./README.md.

Question (ROADMAP.md, probe B2; handoff "Step 4B"):
  How does the monodromy A act on the moduli space of the figure-eight knot
  complement, and what is the continuum limit of that discrete evolution?

Two computations:
  [1] The action on the logarithmic boundary coordinates (log M, log L) is, by
      construction, the linear map A itself -- so the moduli dynamics are the
      hyperbolic dynamics with multipliers phi^2, phi^-2. Exact.
  [2] The handoff document claims A acts on the A-polynomial curve as
      (M, L) -> (M^2 L, M L). This probe TESTS that claim directly: does that
      substitution leave the figure-eight A-polynomial curve invariant?

Run:  python frontier/B2_moduli_evolution/probe.py
"""

import sympy as sp

M, L, t = sp.symbols("M L t")

# Geometric component of the figure-eight (4_1) A-polynomial.
#   A_poly(M, L) = M^4 L^2 - (M^8 - M^6 - 2 M^4 - M^2 + 1) L + M^4
A_POLY = M**4 * L**2 - (M**8 - M**6 - 2 * M**4 - M**2 + 1) * L + M**4

# Monodromy as a linear map on (log M, log L).
A_MON = sp.Matrix([[2, 1], [1, 1]])


def computation_1_log_coordinate_action():
    """A acts linearly on (log M, log L); report its fixed point and multipliers."""
    eig = A_MON.eigenvals()
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    multipliers = {sp.simplify(k): v for k, v in eig.items()}
    # the only fixed point of a hyperbolic linear map is the origin
    fixed_point = sp.linsolve(((A_MON - sp.eye(2)), sp.zeros(2, 1)))
    return {
        "map": A_MON,
        "multipliers": multipliers,
        "expanding_is_phi_squared": sp.simplify(max(eig, key=lambda e: abs(e)) - phi**2) == 0,
        "fixed_point": fixed_point,
    }


def computation_2_test_curve_invariance():
    """Test the handoff claim: is A_POLY(M,L)=0 invariant under (M,L)->(M^2 L, M L)?"""
    mapped = sp.expand(A_POLY.subs({M: M**2 * L, L: M * L}, simultaneous=True))
    p = sp.Poly(A_POLY, L)
    q = sp.Poly(mapped, L)
    # curve invariant  <=>  p divides q  (p is the irreducible geometric component)
    quotient, remainder = sp.div(q, p)
    return {
        "mapped_degree_in_L": q.degree(),
        "remainder_is_zero": remainder.is_zero,
        "remainder": sp.expand(remainder.as_expr()),
    }


def computation_3_continuum_limit():
    """The continuum limit of iterating A is the flow exp(t * log A)."""
    # log A from probe B1 (exact), in the sl(2) basis.
    log_phi2 = sp.log(sp.Rational(3, 2) + sp.sqrt(5) / 2)
    logA = (log_phi2 / sp.sqrt(5)) * sp.Matrix([[1, 2], [2, -1]])
    flow = sp.simplify((t * logA).exp())
    # at t = 1 the flow must return A
    returns_A = sp.simplify(flow.subs(t, 1) - A_MON) == sp.zeros(2, 2)
    return {"generator_logA": logA, "flow_at_t1_equals_A": returns_A}


def main():
    print("=" * 72)
    print("Frontier probe B2 — monodromy action on the moduli space")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md sec. 5)")
    print("=" * 72)

    c1 = computation_1_log_coordinate_action()
    print("\n[1] Action on (log M, log L)")
    print(f"    map                 = {c1['map'].tolist()}  (= the monodromy A)")
    print(f"    multipliers          = {c1['multipliers']}")
    print(f"    expanding = phi^2    : {c1['expanding_is_phi_squared']}")
    print(f"    fixed point          = {c1['fixed_point']}  (origin = complete structure)")

    c2 = computation_2_test_curve_invariance()
    print("\n[2] Handoff claim test: is the A-polynomial curve invariant under")
    print("    (M, L) -> (M^2 L, M L) ?")
    print(f"    mapped poly degree in L : {c2['mapped_degree_in_L']}")
    print(f"    A_POLY divides mapped   : {c2['remainder_is_zero']}")
    if not c2["remainder_is_zero"]:
        print(f"    -> NOT invariant. Nonzero remainder; the handoff framing of the")
        print(f"       (M,L) action does not preserve the knot A-polynomial curve.")

    c3 = computation_3_continuum_limit()
    print("\n[3] Continuum limit of the discrete evolution")
    print(f"    generator log(A)     = {c3['generator_logA'].tolist()}")
    print(f"    exp(1 * log A) == A  : {c3['flow_at_t1_equals_A']}")

    print("\n[verdict]  See README.md.")


if __name__ == "__main__":
    main()
