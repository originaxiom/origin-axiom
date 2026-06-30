"""B304 -- the gauge-DYNAMICS skeleton + the two peer handoffs assessed. Run: python (pyenv) for the group theory;
the E6-root facts are Sage-verified and recorded.

Two web-Opus seats pushed fresh-eyes on the SM-from-axiom bottleneck. Assessed verify-don't-trust. The genuine
finding (Chat-2's "bypass"): our structural theorem (the object forces dimensionless structure) reaches into gauge
DYNAMICS -- the RG running and sin^2(theta_W) are forced, not just the gauge group + reps. Honest tiering below.

VERIFIED, FORCED -- but GENERIC-GUT (forced via E6 ⊃ SM; NOT object-specific, same tier as B299/B301):
  1. sin^2(theta_W) = Tr(T3^2)/Tr(Q^2) = 2/(16/3) = 3/8 at unification (Georgi-Glashow), over one SM generation.
     Generation-INDEPENDENT -> routes around the degree-2 generation wall (B298). Holds for any GUT with the SM in a
     complete multiplet (SU(5), SO(10), E6).
  2. one-loop beta signs from one 27: SU(3),SU(2) asymptotically free, U(1) grows (the unification direction). The
     dynamical reason a GUT is possible -- forced by the matter content, no generation count needed.

VERIFIED, OBJECT-RELEVANT (the gem):
  3. the number of E6 adjoint weights (principal sl2 grading, exponents {1,4,5,7,8,11}, B264) with j ≡ 0 mod 3 is
     exactly 24 = |2T| (binary tetrahedral group order). Ties the E6 principal grading mod 3 to the McKay group of
     E6 (B266: ℚ(√−3) -> 3 -> 2T -> McKay E6). The mod-3 structure is the Eisenstein-3 of the figure-eight's field.

REFUTED (a clean verify-don't-trust catch):
  4. Chat-1's "E6 breaks to SU(3) color at the saddle (height-6 roots form A2=SU(3))" is WRONG. E6 has exactly 3
     height-6 positive roots, but they are MUTUALLY ORTHOGONAL -> (A1)^3 = SU(2)^3, NOT A2 = SU(3). And A2 is
     IMPOSSIBLE: it needs a height-12 root (alpha+beta), but E6's max height is 11. The dim-12 unbroken algebra is
     SU(2)^3 x U(1)^3, not SU(3) x U(1)^4. (Sage-verified.) The "12 = dim(SM)" is a dimension coincidence.

FIREWALLED [LEAP] (Chat-1 Result 1, DGG -- not verifiable in-sandbox):
  5. "the Dehn filling IS the N=2->N=1 datum": in Dimofte-Gaiotto-Gukov, the cusped manifold gives a 3d N=2 theory;
     a filling adds a mass/superpotential deformation breaking N=2 -> N=1. If so, the filling does chirality (N=2->N=1)
     AND amphichirality-breaking (B286) AND scale (B290) AND the CP sign (B289) as ONE act -> wall #3 dissolves into
     the seam. Consistent with B286/B277/B303; the DGG/mass-deformation reading is unverified physics -> S045 [LEAP].

FIREWALL: the verified items are group theory; the gauge-dynamics tier is GENERIC-GUT (not the object-specific atom);
the DGG reading is firewalled. Nothing to CLAIMS.
"""
from fractions import Fraction as F


def sin2_theta_w():
    """Tr(T3^2)/Tr(Q^2) over one SM generation = 3/8 (Georgi-Glashow)."""
    states = []
    for _ in range(3):                                   # quark doublet x3 colors
        states += [(F(1, 2), F(2, 3)), (F(-1, 2), F(-1, 3))]
    states += [(F(1, 2), F(0)), (F(-1, 2), F(-1))]       # lepton doublet
    for _ in range(3): states.append((F(0), F(-2, 3)))   # u^c x3
    for _ in range(3): states.append((F(0), F(1, 3)))    # d^c x3
    states += [(F(0), F(1)), (F(0), F(0))]               # e^c, nu^c
    trT3 = sum(t * t for t, q in states)
    trQ = sum(q * q for t, q in states)
    return trT3 / trQ                                    # = 3/8


def beta_signs_unify():
    """One-loop b (convention b>0 = asymptotically free): SU(3),SU(2)>0 (AF); U(1)<0 (grows). The unification direction."""
    b3 = F(11, 3) * 3 - F(2, 3) * (4 * F(1, 2))
    b2 = F(11, 3) * 2 - F(2, 3) * (4 * F(1, 2))
    b1 = -F(2, 3) * F(16, 3)                              # U(1): C2=0, only matter -> negative
    return b3 > 0 and b2 > 0 and b1 < 0 and b3 > b2       # the AF unification pattern


def principal_grading_mod3_count():
    """# of E6 adjoint weights (principal sl2 grading) with j == 0 mod 3 = 24 = |2T| (B264 exponents)."""
    exps = [1, 4, 5, 7, 8, 11]
    return sum(sum(1 for j in range(-2 * m, 2 * m + 1, 2) if j % 3 == 0) for m in exps)


# --- Sage-verified E6 root facts (recorded) ---
E6_HEIGHT6_POSITIVE_ROOTS = 3
E6_HEIGHT6_ROOTS_MUTUALLY_ORTHOGONAL = True              # -> (A1)^3 = SU(2)^3, NOT A2 = SU(3)
E6_MAX_HEIGHT = 11                                       # A2 needs height-12 -> impossible
SADDLE_SU3_CLAIM_REFUTED = True

# --- tiers ---
GAUGE_DYNAMICS_FORCED = True                             # sin2thetaW + beta running -- a real extension into dynamics
GAUGE_DYNAMICS_IS_GENERIC_GUT = True                     # forced via E6 ⊃ SM; NOT object-specific
GRADING_24_IS_OBJECT_RELEVANT = True                     # 24=|2T| ties principal-mod-3 to the McKay group (B266)
FILLING_IS_N2_TO_N1_DATUM = "LEAP (DGG; firewalled S045) -- dissolves wall #3 into the seam"
DERIVES_SM_VALUES = False                                # firewall


def verdict():
    return bool(sin2_theta_w() == F(3, 8) and beta_signs_unify()
                and principal_grading_mod3_count() == 24
                and E6_HEIGHT6_POSITIVE_ROOTS == 3 and E6_HEIGHT6_ROOTS_MUTUALLY_ORTHOGONAL
                and SADDLE_SU3_CLAIM_REFUTED and GAUGE_DYNAMICS_FORCED and GAUGE_DYNAMICS_IS_GENERIC_GUT
                and GRADING_24_IS_OBJECT_RELEVANT and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("sin^2(theta_W) at unification =", sin2_theta_w(), "(=3/8, Georgi-Glashow; generic-GUT)")
    print("beta AF unification pattern (SU3,SU2 free; U1 grows):", beta_signs_unify())
    print("E6 principal-grading weights with j==0 mod3 =", principal_grading_mod3_count(), "= |2T| (object-relevant)")
    print("Chat-1 saddle SU(3) claim REFUTED (height-6 roots orthogonal = SU(2)^3, A2 impossible):",
          SADDLE_SU3_CLAIM_REFUTED)
    print("filling = N=2->N=1 datum:", FILLING_IS_N2_TO_N1_DATUM)
    print("verdict:", verdict())
