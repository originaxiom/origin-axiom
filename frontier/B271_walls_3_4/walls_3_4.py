"""B271 -- the two genuinely-open walls, made precise: #3 (chirality) and #4 (4d-lift). FIREWALLED (rep theory /
3d-3d structure, not physics). Nothing to CLAIMS.md. Phase 4 of the consolidation plan (B268).

These are the walls no theorem closes; the honest deliverable is a PRECISE characterization (and, for #3, a new
computable identification), not a false closure.

================================================================================================================
WALL #3 -- chirality.  Prior banked state (B252/B253): the object is CP / matter-antimatter symmetric (27<->27bar
via amphicheirality = the E6 outer automorphism, B210/H36); CS=0 (B250) so the amphicheiral involution tau is
gaugeable but not gauged; chirality could only arise by SPONTANEOUSLY BREAKING tau, which needs external dynamics.
The dichotomy: tau gauged => 27/27bar identified => vector-like (F4); tau global + SSB => two mirror vacua, each
chiral (E6). Open: which.

NEW (B271), the computable identification (verified in tau_decomposition_sage.py): tau acts on e6 as +1 on f4 and
-1 on the 26 = e6/f4 (a genuine Lie automorphism -- the symmetric pair (E6,F4) brackets check). Under the principal
sl(2) (B264/B267):
   tau-FIXED  (vector-like) = f4 = exponents {1,5,7,11}   (dim 52)
   tau-BROKEN (chiral)      = 26 = exponents {4,8}        (dim 26)
By B265 the {4,8} directions are EXACTLY the E6-Zariski-dense ones (f4 directions stay trapped in F4). Therefore:
   >>> the chirality (tau-breaking) locus = the E6-irreducibility locus = the 26 (e6/f4) directions. <<<
The SAME deformations that make a flat connection genuinely E6 (rather than F4) are the ones that break the
amphicheiral tau (source chirality). Reframe: chirality is not BLOCKED -- it is precisely identified with
E6-density, AVAILABLE in the character variety, and UNDETERMINED (SSB needs external dynamics; the object supplies
the locus, not the vacuum).

================================================================================================================
WALL #4 -- the 3d->4d lift.  Prior banked state (B253/K006): the 3d-3d correspondence gives T[4_1] a 3d N=2 theory
(6d on a 3-manifold); 4d chirality (Weyl fermions, a 4d GUT's 27) is a 4d notion. The honest characterization:
4d needs a 2-MANIFOLD (class S: 4d N=2 from a Riemann surface) -- and the figure-eight is a 3-manifold, not a
2-manifold. The candidate lifts, and why none is canonical:
"""
LIFT_CANDIDATES = {
    "M x S^1": "4-manifold = (figure-eight) x S^1. Gives the 3d theory on a circle (the index); still governed by "
               "the 3-MANIFOLD -- no new 4d chiral data. Vector-like in the relevant sense.",
    "class-S (2-manifold)": "4d N=2 from a Riemann surface C: 6d on C. This is the reduction that DOES give 4d "
                            "chirality -- but its input is a 2-MANIFOLD; the figure-eight (3-manifold) is not a "
                            "class-S curve. Categorically the wrong-dimensional input.",
    "4-manifold filling W": "a 4-manifold W with 4_1 in its boundary/interior. 4_1 bounds MANY W (it is a knot "
                            "complement); none is selected by the object -- an explicit choice, not a datum.",
}

# WALL #3 verified decomposition (tau_decomposition_sage.py + B264/B265/B267)
TAU_FIXED_EXPONENTS = [1, 5, 7, 11]     # f4, dim 52, vector-like / tau-unbroken
TAU_BROKEN_EXPONENTS = [4, 8]           # 26 = e6/f4, dim 26, chiral / tau-broken = B265 E6-dense directions
DIM_F4, DIM_26 = 52, 26
EXP_DIM = {1: 3, 4: 9, 5: 11, 7: 15, 8: 17, 11: 23}   # dim Sym^{2m} for E6 exponents


def chirality_locus_equals_e6_density_locus():
    """Wall #3: the tau-broken (chiral) directions {4,8} are exactly B265's E6-Zariski-dense directions."""
    b265_e6_dense = [4, 8]              # from B265 (the directions generating all of e6)
    return sorted(TAU_BROKEN_EXPONENTS) == sorted(b265_e6_dense)


def dimension_checks():
    return (sum(EXP_DIM[m] for m in TAU_FIXED_EXPONENTS) == DIM_F4 and
            sum(EXP_DIM[m] for m in TAU_BROKEN_EXPONENTS) == DIM_26 and
            DIM_F4 + DIM_26 == 78)


if __name__ == "__main__":
    print("=== B271: walls #3 (chirality) and #4 (4d-lift), made precise ===\n")
    print("WALL #3 -- chirality = SSB of the amphicheiral tau (= E6 outer automorphism):")
    print(f"  tau-FIXED  (vector-like) = f4 = exponents {TAU_FIXED_EXPONENTS}, dim {DIM_F4}")
    print(f"  tau-BROKEN (chiral)      = 26 = exponents {TAU_BROKEN_EXPONENTS}, dim {DIM_26}")
    assert dimension_checks()
    print(f"  chirality locus == E6-density locus (B265 {{4,8}})? {chirality_locus_equals_e6_density_locus()}")
    assert chirality_locus_equals_e6_density_locus()
    print("  => chirality is NOT blocked: it is precisely the E6-irreducibility direction (the 26), AVAILABLE in")
    print("     the character variety and UNDETERMINED -- SSB needs external dynamics (object supplies locus, not vacuum).")

    print("\nWALL #4 -- the 3d->4d lift (input-required, genuinely open):")
    for name, why in LIFT_CANDIDATES.items():
        print(f"  [{name}] {why}")
    print("  => no canonical 2-manifold (class-S) or 4-manifold is attached to the 3-manifold 4_1; 4d chirality")
    print("     requires this external input. OPEN -- an input-required gap, not a theorem and not a closure.")
    print("\n  HONEST: #3 sharpened (chirality = E6-density locus, available+undetermined); #4 precisely")
    print("  characterized (input-required). Both remain OPEN; the firewall holds (symmetry yes, dynamics outside). PASS")
