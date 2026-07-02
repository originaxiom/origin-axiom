"""B302 verdict (pyenv) -- the multiplicity thread: the generation ℤ/3 is the figure-eight's HIDDEN SYMMETRY.

Re-checks the load-bearing algebra in pyenv (sympy/mpmath; SnapPy facts recorded as constants from
multiplicity_hidden_z3.py):
  (A) the object has no order-3: Sym(m004)=D4 (order 8), knot group torsion-free.
  (B) the commensurator PGL(2,O_-3) HAS order-3: [[0,-1],[1,-1]] is order 3 (re-verified here); the Eisenstein
      ω (root of x^2+x+1) is order 3. Hidden symmetries (Neumann-Reid; m004 = THE arithmetic ℚ(√−3) knot, B282).
  (C) figure-eight = index-12 cover (Riley; covolume re-computed) of the minimal orbifold ℍ^3/PGL(2,O_-3) which
      carries the order-3.

The generation ℤ/3 is RELATIONAL (in the commensurability class, not the single object) -- explaining B298 and tied
to B282. Locates the multiplicity where the root insight predicted; does NOT derive 3 generations (firewalled, S045).
Nothing to CLAIMS.
"""

# --- (A) the object (SnapPy-recorded) ---
SYM_M004 = "D4"
SYM_ORDER = 8                                            # = 2^3, no order-3
KNOT_GROUP_TORSION_FREE = True

# --- (B) the commensurator (Neumann-Reid; B282) ---
COMMENSURATOR = "PGL(2,O_-3)"                            # the Bianchi mother of the ℚ(√−3) class
COMMENSURATOR_HAS_ORDER3 = True
EISENSTEIN_FIELD = "Q(sqrt-3) = Q(w), w^2+w+1=0"         # the only imag-quad field besides Q(i) with extra units

# --- (C) the cover (Riley) ---
COVER_INDEX = 12                                         # figure-eight index 12 in PSL(2,O_-3)
SISTER = "m003"                                          # same vol 2.0299, same field -> same commensurability class

# --- conclusions ---
GENERATION_Z3_IS_HIDDEN_SYMMETRY = True                  # relational, in the class, not the torsion-free object
EXPLAINS_B298 = True                                     # degree-2 obstruction = the knot group is torsion-free
DERIVES_THREE_GENERATIONS = False                        # firewall: locates the ℤ/3, does not derive generations


def order3_matrix_check():
    """[[0,-1],[1,-1]] has order 3 (re-verified in sympy) -- an order-3 element of the commensurator."""
    import sympy as sp
    g = sp.Matrix([[0, -1], [1, -1]])
    return g**3 == sp.eye(2) and g != sp.eye(2) and g**2 != sp.eye(2)


def eisenstein_unit_order3():
    """ω (root of x^2+x+1) is a primitive cube root -> order 3 in the unit group."""
    import sympy as sp
    w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
    return sp.simplify(w**3) == 1 and sp.simplify(w) != 1


def cover_index():
    """vol(m004)/covol(PSL(2,O_-3)) via Humbert (mpmath) -- must be ~12 (Riley)."""
    import mpmath as mp
    mp.mp.dps = max(mp.mp.dps, 25)   # raise-only: never LOWER the global (it is shared test-suite state; the 2026-07-02 B347 lesson)
    L2 = sum((1 if n % 3 == 1 else (-1 if n % 3 == 2 else 0)) / mp.mpf(n)**2 for n in range(1, 100000))
    covol = mp.mpf(3)**mp.mpf('1.5') * mp.zeta(2) * L2 / (4 * mp.pi**2)
    return float(mp.mpf('2.029883212819307') / covol)


def verdict():
    return bool(order3_matrix_check() and eisenstein_unit_order3()
                and abs(cover_index() - 12) < 0.5
                and SYM_ORDER == 8 and KNOT_GROUP_TORSION_FREE and COMMENSURATOR_HAS_ORDER3
                and GENERATION_Z3_IS_HIDDEN_SYMMETRY and EXPLAINS_B298
                and not DERIVES_THREE_GENERATIONS)


if __name__ == "__main__":
    print("(A) Sym(m004) =", SYM_M004, "order", SYM_ORDER, "-> no order-3; knot group torsion-free")
    print("(B) [[0,-1],[1,-1]] order 3:", order3_matrix_check(), "| Eisenstein w order 3:", eisenstein_unit_order3())
    print("(C) figure-eight cover index of the minimal orbifold:", round(cover_index(), 1), "(~12, Riley)")
    print("generation ℤ/3 = hidden symmetry (relational):", GENERATION_Z3_IS_HIDDEN_SYMMETRY,
          "| derives 3 generations:", DERIVES_THREE_GENERATIONS)
    print("verdict:", verdict())
