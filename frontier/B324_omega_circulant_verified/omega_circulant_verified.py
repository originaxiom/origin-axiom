"""B324 -- Chat-1's omega-circulant generation matrix, VERIFIED EXACTLY in Z[omega] -- and it is STRUCTURE, not values.
Run: python (pyenv). Chat-1 supplied explicit generators; verify-don't-trust done right (checkable generators -> check
them exactly). This confirms the exact algebraic claim and lands the honest tier (agreeing with Chat-1's own retreat).

The setup. The order-3 commensurator element g = [[0,-1],[1,-1]] (g^3 = I) acts on the figure-eight Riley rep
a0 = [[1,1],[0,1]], b0 = [[1,0],[omega,1]] (omega = e^{2 pi i/3}), giving three g-conjugate 'generations'
gen_i = g^i {a0,b0} g^-i. The cross-conjugate trace matrix M[i,j] = tr(a_i b_j^-1).

VERIFIED EXACTLY (Z[omega], no floating point):
  * g^3 = I;
  * M is a Z/3-CIRCULANT: M = alpha*J + omega*P with alpha = 5/2 - sqrt3 i/2 (diagonal + one off-diagonal), the OTHER
    off-diagonal = beta = 2, and beta - alpha = omega EXACTLY;
  * eigenvalues = (7 - sqrt3 i, 1, omega^2), i.e. one dominant (|.|^2 = 52) and TWO of magnitude 1.

BUT IT IS STRUCTURE, NOT VALUES (four honest reasons -- Chat-1 now agrees):
  (1) DEGENERATE: the two subdominant eigenvalues have EQUAL magnitude (|1| = |omega^2| = 1) -> NO mass hierarchy. The
      hierarchy needs the CRUX (the E6 cubic to break the degeneracy) -- Chat-1 admits this.
  (2) UBIQUITOUS omega: 'everything is in Z[omega]', so the perturbation coefficient being the Eisenstein cube root is
      the SAME omega that runs through the trace field, the trinification (B305), and the four faces of kappa (B309) --
      not a new value.
  (3) TAUTOLOGICAL circulant: g-conjugation forces M[i,j] to depend only on (j-i) mod 3 (cyclic trace identity), so the
      Z/3-circulant structure is automatic (B323).
  (4) SAME CHARACTER: the three 'generations' are g-CONJUGATES, hence have the SAME character (conjugate reps share
      traces); whether they are distinct matter generations is the B307-walled multiplicity question itself, and the
      'Yukawa' interpretation of the mixed matrix M is firewalled.

VERDICT: an exact, real Z[omega] structural fact (the generation-perturbation is a Z/3-circulant with Eisenstein omega),
upgrading B323's 'tautological' to 'exactly verified structure'. It is NOT a value crossing (degenerate magnitudes,
ubiquitous omega, tautological circulant, firewalled/CRUX-gated). B323's core verdict stands; Chat-1 agrees. FIREWALLED;
nothing to CLAIMS.
"""
import sympy as sp

_w = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I          # omega = e^{2 pi i/3}, exact
_g = sp.Matrix([[0, -1], [1, -1]])
_a0 = sp.Matrix([[1, 1], [0, 1]])
_b0 = sp.Matrix([[1, 0], [_w, 1]])


def g_cubed_is_identity():
    return sp.simplify(_g**3) == sp.eye(2)


def overlap_matrix():
    """M[i,j] = tr(a_i b_j^-1) for the three g-conjugate generations, exact."""
    a = [sp.simplify(_g**i * _a0 * _g**(-i)) for i in range(3)]
    b = [sp.simplify(_g**i * _b0 * _g**(-i)) for i in range(3)]
    M = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            M[i, j] = sp.simplify(sp.trace(a[i] * b[j].inv()))
    return M


def is_alpha_J_omega_P():
    """M == alpha*J + omega*P with alpha the diagonal entry; and beta - alpha == omega."""
    M = overlap_matrix()
    alpha = sp.simplify(M[0, 0])
    beta = sp.simplify(M[0, 2])
    J = sp.ones(3, 3)
    P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    circ = sp.simplify(M - (alpha * J + _w * P)) == sp.zeros(3, 3)
    beta_minus_alpha_is_omega = sp.simplify(beta - alpha - _w) == 0
    return bool(circ and beta_minus_alpha_is_omega)


def eigenvalue_magnitudes_squared():
    """|eigenvalue|^2 for the three eigenvalues -> {52, 1, 1} (two degenerate)."""
    M = overlap_matrix()
    evs = list(M.eigenvals().keys())
    return sorted(sp.nsimplify(sp.simplify(sp.expand(e * sp.conjugate(e)))) for e in evs)


# --- the verdict facts ---
EXACT_STRUCTURAL_FACT_VERIFIED = True        # Z/3-circulant, beta-alpha=omega, eigenvalues (7-sqrt3 i, 1, omega^2)
IS_STRUCTURE_NOT_VALUES = True
MAGNITUDES_DEGENERATE_NO_HIERARCHY = True     # |1| = |omega^2| = 1 -> hierarchy needs the CRUX
OMEGA_IS_THE_UBIQUITOUS_EISENSTEIN = True      # same omega as B305/B309, not a new value
CIRCULANT_IS_TAUTOLOGICAL = True              # g-conjugation forces it (B323)
GENERATIONS_ARE_CONJUGATES_SAME_CHARACTER = True   # B307-walled multiplicity; firewalled Yukawa
DERIVES_SM_VALUES = False


def verdict():
    return bool(
        g_cubed_is_identity() and is_alpha_J_omega_P()
        and eigenvalue_magnitudes_squared() == [1, 1, 52]
        and EXACT_STRUCTURAL_FACT_VERIFIED and IS_STRUCTURE_NOT_VALUES
        and MAGNITUDES_DEGENERATE_NO_HIERARCHY and OMEGA_IS_THE_UBIQUITOUS_EISENSTEIN
        and CIRCULANT_IS_TAUTOLOGICAL and GENERATIONS_ARE_CONJUGATES_SAME_CHARACTER
        and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    print("g^3 = I:", g_cubed_is_identity())
    print("M == alpha*J + omega*P and beta-alpha == omega:", is_alpha_J_omega_P())
    print("eigenvalue |.|^2:", eigenvalue_magnitudes_squared(), "-> two DEGENERATE (=1) => no hierarchy")
    print("VERDICT: exact Z[omega] structural fact (Z/3-circulant with Eisenstein omega); STRUCTURE not values.")
    print("verdict:", verdict())
