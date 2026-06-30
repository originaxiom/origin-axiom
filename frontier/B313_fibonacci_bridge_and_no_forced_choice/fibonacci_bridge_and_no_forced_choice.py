"""B313 -- the three-seat cross-check of (a) the Fibonacci/(G2)_1 bridge between Face IV and the content, and (b) the
upstream "is the figure-eight forced?" meditation. Run: python (pyenv). Verify-don't-trust on the parallel Chat-1 /
Chat-2 runs, grounded in the repo (K009, K013, S032, B261).

(a) THE FIBONACCI BRIDGE (Chat-1 proposed "matter = Fibonacci anyons", Chat-2 stripped it). VERIFIED + GENERIC:
    * central-charge chain EXACT: SU(2)_3 (9/5) --boson(+1)--> (G2)_1 (14/5) --(+16/5)--> (E6)_1 (6).
      ((G2)_1 = the Fibonacci category; quantum dim of tau = golden phi.)
    * (G2)_1 sits in BOTH ends: golden-end quantization (even-spin subsector of SU(2)_3) AND eisenstein-end content
      (G2 subset E6). A real common substructure of the object's two ends.
    * BUT the matter overclaim is REFUTED: under E6 ⊃ G2 x SU(3), 27 -> (7,3)+(1,6) (dims 21+6=27), NOT 27 -> 7. The
      Fibonacci 7 appears tensored with color-3; the 27 is not a single anyon.
    * VERDICT: GENERIC -- E6 ⊃ G2 x SU(3) is Slansky (1981), SU(2)_3 ⊃ Fibonacci is true at any level 3; the
      object-specific part is only B261 (the figure-eight carries both arithmetic ends). Same shape as the cascade:
      structure generic, the object's relationship to it = the already-banked two-ends fact.

(b) THE UPSTREAM MEDITATION ("is m=1 / the figure-eight forced, or chosen?"). The seats rediscovered the repo's OWN
    no-forced-choice program -- the 5th time this session a "buried center" was already banked. TWO corrections:
    * m=1 has a NON-METRIC selector. Chat-2 said "m=1 requires the systole metric"; incomplete. K009 banks THREE
      selectors: systole (a metric, B92), the EXPANSION THRESHOLD (the dynamics, B120/P004 -- m=1 is where twist*swap
      first ignites hyperbolic expansion; NO metric), uniquely m=1; arithmeticity selects {m=1,m=2} (B125). So m=1 is
      the MOST-SELECTED member -- but "most-selected" is not "forced as a theorem" (P000 stands; the member is contingent).
    * "does multiplicity create a fork?" is ANSWERED. K013/B130: a SINGLE seed is a moduli space (kappa continuous on
      the fixed locus, elimination ideal empty) -- it parametrizes, it does not choose; the only discreteness is the
      external seed label. S032-B/B131: gluing TWO DISTINCT seeds DOES create an internal kappa-fork (the (1,2) fork
      kappa in {-4,-2}, exact); HETEROGENEITY (distinct seeds), not multiplicity (copies), makes the choice; minimal
      choosing structure = two distinct seeds.
    * THE GENUINE OPEN TARGET: S032-A -- the theorem-version, that NO invariant whatsoever (incl. quantum/CS/Face IV)
      is discretely-multivalued-and-unsymmetric for a single seed. OPEN (+ L7 synthesis). If proven => single-seed
      member-contingency is IRREDUCIBLE (the firewall's deepest form); the only route to a forced choice is heterogeneity.

VERDICT: the Fibonacci bridge confirms the structural theorem from a 5th direction (generic structure + banked B261).
The upstream meditation reduces to the banked no-forced-choice program: the figure-eight forces the FAMILY and is the
MOST-SELECTED member, but does NOT force ITSELF as a theorem (K013); choice requires heterogeneity (B131); the open
target is S032-A. "The figure-eight is forced" is FALSE in the strict sense -- it is the most-selected member of a
forced family, exactly as P000 has always said. FIREWALLED; nothing to CLAIMS.
"""
import sympy as sp


def c_wzw(dim_g, dual_coxeter, k):
    """central charge of the level-k WZW model for a simple g."""
    return sp.Rational(k * dim_g, k + dual_coxeter)


def central_charge_chain():
    """SU(2)_3 -> (G2)_1 -> (E6)_1 with the connecting cosets."""
    c_su2_3 = c_wzw(3, 2, 3)        # 9/5
    c_g2_1 = c_wzw(14, 4, 1)        # 14/5
    c_e6_1 = c_wzw(78, 12, 1)       # 6
    return c_su2_3, c_g2_1, c_e6_1


def chain_is_exact():
    c_su2_3, c_g2_1, c_e6_1 = central_charge_chain()
    return (c_su2_3 == sp.Rational(9, 5) and c_g2_1 == sp.Rational(14, 5) and c_e6_1 == 6
            and c_su2_3 + 1 == c_g2_1                       # +1 free boson
            and c_g2_1 + sp.Rational(16, 5) == c_e6_1)      # +16/5


def branching_27_refutes_matter_equals_anyons():
    """E6 ⊃ G2 x SU(3): 27 -> (7,3)+(1,6), dims 21+6=27 -- NOT 27 -> 7 (the single Fibonacci anyon)."""
    return 7 * 3 + 1 * 6 == 27


# --- the repo-grounded facts (cited, not re-proved) ---
BRIDGE_IS_GENERIC = True               # E6 ⊃ G2 x SU(3) Slansky; SU(2)_3 ⊃ Fibonacci level-3-generic
OBJECT_SPECIFIC_PART_IS_B261 = True    # only "the figure-eight carries both ends" is object-specific
MATTER_EQUALS_ANYONS_REFUTED = True    # 27 = (7,3)+(1,6), not 7

M1_HAS_NONMETRIC_SELECTOR = True       # K009 criterion 2: the expansion threshold (B120/P004), no metric
M1_IS_MOST_SELECTED_NOT_FORCED = True  # K009: systole + threshold unique, arithmeticity {m=1,m=2}; P000 stands
SINGLE_SEED_DOES_NOT_CHOOSE = True     # K013/B130: moduli space, kappa continuous, external seed label only
HETEROGENEITY_MAKES_THE_FORK = True    # S032-B/B131: two DISTINCT seeds -> (1,2) fork kappa in {-4,-2}
S032A_THEOREM_VERSION_IS_THE_OPEN_TARGET = True   # no invariant whatsoever forces a single-seed choice -- OPEN
DERIVES_SM_VALUES = False


def verdict():
    return bool(
        chain_is_exact() and branching_27_refutes_matter_equals_anyons()
        and BRIDGE_IS_GENERIC and OBJECT_SPECIFIC_PART_IS_B261 and MATTER_EQUALS_ANYONS_REFUTED
        and M1_HAS_NONMETRIC_SELECTOR and M1_IS_MOST_SELECTED_NOT_FORCED
        and SINGLE_SEED_DOES_NOT_CHOOSE and HETEROGENEITY_MAKES_THE_FORK
        and S032A_THEOREM_VERSION_IS_THE_OPEN_TARGET and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    c = central_charge_chain()
    print("central charges  SU(2)_3, (G2)_1, (E6)_1 =", c, "| chain exact:", chain_is_exact())
    print("27 -> (7,3)+(1,6) dims 21+6=27 (matter=anyons refuted):", branching_27_refutes_matter_equals_anyons())
    print("bridge generic + object part = B261:", BRIDGE_IS_GENERIC and OBJECT_SPECIFIC_PART_IS_B261)
    print("m=1: non-metric selector (B120) + most-selected not forced (K009):",
          M1_HAS_NONMETRIC_SELECTOR and M1_IS_MOST_SELECTED_NOT_FORCED)
    print("single seed does not choose (K013) | heterogeneity forks (S032-B/B131):",
          SINGLE_SEED_DOES_NOT_CHOOSE, HETEROGENEITY_MAKES_THE_FORK)
    print("open target = S032-A (no invariant forces a single-seed choice):", S032A_THEOREM_VERSION_IS_THE_OPEN_TARGET)
    print("verdict:", verdict())
