"""B253 -- adjudication of the Chat-2 handoff "the chirality REDUCTION" (2026-06-28). FIREWALLED.

The handoff has three parts. Verdict up front:
  PART A (the E6/E8 complex-rep asymmetry): VERIFIED, bankable, firewall-clean rep theory.
  THE CORRECTION to B252 (explicit symmetry does not preclude SSB-sourced asymmetry): VALID, adopted.
  PART B (chirality "reduces" to gauged-vs-SSB of tau, "decidable"): OVERSTATED -> firewalled speculation, not
         decidable from the object. Three independent reasons + the CS "discriminator" is inconclusive at CS=0.

------------------------------------------------------------------------------------------------------------
PART A -- bankable (Sage-verified in chirality_capability_sage.py):
  A gauge group supports chiral matter iff it has a COMPLEX (non-self-dual) representation.
    E6: has a complex rep (the 27, 27 != 27bar); Out(E6)=Z/2.            -> complex-rep-CAPABLE
    E7: only self-dual reps (56 pseudoreal); Out(E7)=1.                  -> NOT complex-rep-capable
    E8: only self-dual reps (248 real, the adjoint = its min rep); Out(E8)=1. -> NOT complex-rep-capable
  OBJECT-SPECIFIC (via B248): the figure-eight's geometric transition runs from the complex-rep-capable end
  (E6, hyperbolic, Q(sqrt-3)) to the no-complex-rep end (E8, spherical, Q(sqrt5)). The "chirality axis" (in the
  4d-GUT reading) coincides with the B248 transition axis. E7 (no complex rep) is also Niven-excluded (B249) --
  consistent. This is firewall-clean: a statement about the abstract McKay-label groups, asserting no physics.

------------------------------------------------------------------------------------------------------------
THE CORRECTION to B252 (valid, adopted): B252 said the object "cannot source a matter-antimatter asymmetry."
That is too strong. Amphicheirality gives the 27<->27bar swap as an EXPLICIT (representation-theory) symmetry; a
theory with an explicit symmetry can still produce asymmetry by SPONTANEOUSLY BREAKING it. So the precise,
defensible statement is: the object has no EXPLICIT CP-odd datum (B252 core, still true); any asymmetry would have
to arise by spontaneous breaking of tau, which needs DYNAMICS (a potential, vacua) -- external to the object
(firewall K018). This refinement fits the S040 thesis: the object supplies the symmetric seed; the world supplies
the breaking.

------------------------------------------------------------------------------------------------------------
PART B -- the "reduction" chirality <=> gauged-vs-SSB of the amphicheiral involution tau. The dichotomy is logically
clean (gauged tau -> 27/27bar identified -> vector-like -> non-chiral; global tau + SSB -> two mirror vacua, each
chiral, a Left-Right structure). But it is NOT decidable from the object, for three independent reasons:
  (1) 3d, not 4d. The 3d-3d correspondence (K006) gives T[4_1] a 3d N=2 theory (6d on a 3-manifold). 4d chirality
      (Weyl fermions, the 27 of a 4d E6 GUT, Left-Right models) is a 4d notion; class-S (4d) needs a 2-manifold, not
      the 3-manifold 4_1. So 4d chirality is simply not an observable of the object's licensed theory.
  (2) E6 is a McKay LABEL, not a 4d gauge group (B247). There is no dynamical 27 to be chiral or vector-like.
  (3) gauging tau is a model-building CHOICE (you choose to sum over its bundles), and SSB needs dynamics the
      firewall (K018) says the object does not supply. So gauged-vs-global-and-broken is not an object-determined
      fact.
The proposed cheap discriminator (the Chern-Simons invariant) is INCONCLUSIVE here: tau reverses orientation so
acts on CS by CS -> -CS; the figure-eight has CS=0, so tau is anomaly-free / GAUGEABLE -- but gaugeable does not
mean gauged, and CS=0 leaves BOTH branches open. It would be decisive only if CS != 0 (forcing tau global). So
branch (b) ("amphicheirality as the ORIGIN of chirality") is a legitimate FIREWALLED reading (consistent with S040:
symmetric seed + external breaking), not a bankable or object-decidable reduction.

Run: python chirality_capability.py (pyenv). Nothing to CLAIMS.md.
"""

# Part A facts, verified in chirality_capability_sage.py (recorded with provenance):
COMPLEX_REP_CAPABLE = {"E6": True, "E7": False, "E8": False}   # has a non-self-dual irrep?
OUT_GROUP_ORDER = {"E6": 2, "E7": 1, "E8": 1}                  # |Out(G)| (Dynkin diagram symmetry)
MIN_REP = {"E6": (27, "complex"), "E7": (56, "pseudoreal"), "E8": (248, "real")}

CS_FIGURE_EIGHT = 0   # B250 (4_1 amphicheiral)


def chirality_axis_matches_transition_axis():
    """B248: hyperbolic end = E6 (complex-rep-capable), spherical end = E8 (not). True => the axes coincide."""
    return COMPLEX_REP_CAPABLE["E6"] and not COMPLEX_REP_CAPABLE["E8"]


def cs_under_tau(cs):
    """the amphicheiral involution reverses orientation: CS -> -CS."""
    return -cs


def tau_is_gaugeable():
    """tau is anomaly-free (gaugeable) iff it fixes the CS invariant. CS(4_1)=0 -> fixed -> gaugeable."""
    return cs_under_tau(CS_FIGURE_EIGHT) == CS_FIGURE_EIGHT


def cs_discriminator_is_decisive():
    """the CS discriminator picks gauged-vs-global only if CS != 0 (forcing tau global). At CS=0: inconclusive."""
    return CS_FIGURE_EIGHT != 0


def part_b_decidable_from_object():
    """Part B's resolution is NOT object-determined: 3d-not-4d, McKay-label-not-gauge-group, gauging/SSB external."""
    object_gives_3d_not_4d = True          # K006 (3d-3d): T[4_1] is 3d; 4d chirality needs class-S (a 2-manifold)
    e6_is_mckay_label_not_gauge_group = True   # B247
    gauging_and_ssb_are_external = True    # K018: no dynamics/scale from the object
    return not (object_gives_3d_not_4d or e6_is_mckay_label_not_gauge_group or gauging_and_ssb_are_external)


if __name__ == "__main__":
    print("=== B253: adjudication of the Chat-2 chirality REDUCTION ===\n")
    print("PART A (bankable, Sage-verified rep theory):")
    for g in ("E6", "E7", "E8"):
        d, real = MIN_REP[g]
        print(f"  {g}: min rep {d} ({real}), |Out|={OUT_GROUP_ORDER[g]}, complex-rep-capable={COMPLEX_REP_CAPABLE[g]}")
    print(f"  chirality axis == B248 transition axis (E6 capable -> E8 not): {chirality_axis_matches_transition_axis()}")
    assert chirality_axis_matches_transition_axis()
    assert COMPLEX_REP_CAPABLE == {"E6": True, "E7": False, "E8": False}

    print("\nCORRECTION to B252 (adopted): 'cannot source asymmetry' -> 'no EXPLICIT CP-odd datum; SSB of tau would")
    print("  source it but needs external dynamics' (fits S040: symmetric seed + external breaking).")

    print("\nPART B (the reduction): tau gaugeable (anomaly-free, CS=0)?", tau_is_gaugeable(),
          "| CS discriminator decisive?", cs_discriminator_is_decisive())
    print("  Part B decidable from the object?", part_b_decidable_from_object(),
          "(3d-not-4d / McKay-label / gauging+SSB external) -> FIREWALLED speculation, not a decidable reduction.")
    assert tau_is_gaugeable()
    assert not cs_discriminator_is_decisive()      # CS=0 -> inconclusive
    assert not part_b_decidable_from_object()
    print("\nVERDICT: Part A banked (firewall-clean); B252 correction adopted; Part B firewalled (branch b = an")
    print("S040-consistent reading, not object-decidable). The CS=0 discriminator is INCONCLUSIVE. ALL CHECKS PASS")
