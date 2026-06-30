"""B305 verdict (pyenv; E6-root facts Sage-verified, recorded) -- the Eisenstein trinification grading.

VERIFIED: E6 -> SU(3)^3 trinification at the Eisenstein point u=2pi i/3 (height==0 mod 3 -> 9 roots = A2^3); the
grading eigenvalue is omega=e^{2pi i/3} in Q(sqrt-3) (the figure-eight's atom, B266/B285); the orbifold (theta,phi)
(B299) is the triality permuting the three SU(3)'s. REFUTED (2nd time): the saddle u=i pi/3 (height==0 mod 6) gives 3
ORTHOGONAL roots = SU(2)^3, NOT SU(3). The cascade is E6 -> SU(3)^3 -> SU(2)^3 x U(1)^3, not -> SU(3).

This module re-derives the surviving-root COUNTS in pyenv from the E6 height distribution (Sage-verified), and records
the component structure. FIREWALL: the trinification grading is standard E6; the object connection is the Eisenstein
omega; "which SU(3) is color" + the deformation-as-RG reading are external/firewalled. Nothing to CLAIMS.
"""

# E6 positive-root height distribution (Sage-verified, B304)
E6_HEIGHT_DIST = {1: 6, 2: 5, 3: 5, 4: 5, 5: 4, 6: 3, 7: 3, 8: 2, 9: 1, 10: 1, 11: 1}

# Sage-verified component structures:
EISENSTEIN_MOD3_COMPONENTS = [3, 3, 3]                   # A2^3 = SU(3)^3 = trinification
SADDLE_MOD6_COMPONENTS = [1, 1, 1]                       # A1^3 = SU(2)^3 (orthogonal), NOT A2=SU(3)

# --- the facts ---
TRINIFICATION_AT_EISENSTEIN = True                       # E6 -> SU(3)^3 at u=2pi i/3 (height==0 mod 3)
GRADING_EIGENVALUE_IS_EISENSTEIN_OMEGA = True            # omega=e^{2pi i/3} in Q(sqrt-3) = B266/B285 atom
THETA_PHI_IS_THE_TRINIFICATION_TRIALITY = True           # B299: the orbifold Z3xZ3 permutes the three SU(3)'s
SADDLE_IS_SU2_CUBED_NOT_SU3 = True                       # Chat-1 "SU(3)" refuted (2nd time)
CASCADE = "E6 -> SU(3)^3 (trinification) -> SU(2)^3 x U(1)^3"   # NOT -> SU(3)

# --- not forced / firewalled ---
WHICH_SU3_IS_COLOR_IS_EXTERNAL = True                    # the trinification triality permutes them (B299/B301)
DEFORMATION_AS_RG_IS_LEAP = True                         # u=energy-scale, char variety=RG, topology=Higgs -> firewalled
DERIVES_SM_VALUES = False


def mod_counts():
    """# positive roots with height == 0 mod 3 and mod 6, from the E6 height distribution (pyenv re-derivation)."""
    m3 = sum(c for h, c in E6_HEIGHT_DIST.items() if h % 3 == 0)
    m6 = sum(c for h, c in E6_HEIGHT_DIST.items() if h % 6 == 0)
    return m3, m6


def verdict():
    m3, m6 = mod_counts()
    return bool(m3 == 9 and m6 == 3                       # 9 (trinification) and 3 (saddle) surviving positive roots
                and sum(EISENSTEIN_MOD3_COMPONENTS) == 9 and EISENSTEIN_MOD3_COMPONENTS == [3, 3, 3]
                and SADDLE_MOD6_COMPONENTS == [1, 1, 1]
                and TRINIFICATION_AT_EISENSTEIN and GRADING_EIGENVALUE_IS_EISENSTEIN_OMEGA
                and THETA_PHI_IS_THE_TRINIFICATION_TRIALITY and SADDLE_IS_SU2_CUBED_NOT_SU3
                and WHICH_SU3_IS_COLOR_IS_EXTERNAL and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    m3, m6 = mod_counts()
    print(f"surviving positive roots: mod 3 (Eisenstein) = {m3} (A2^3 trinification), mod 6 (saddle) = {m6} (SU(2)^3)")
    print("trinification at Eisenstein omega (B266/B285 atom):", TRINIFICATION_AT_EISENSTEIN)
    print("(theta,phi) = the trinification triality (B299):", THETA_PHI_IS_THE_TRINIFICATION_TRIALITY)
    print("saddle = SU(2)^3 not SU(3) (Chat-1 refuted, 2nd time):", SADDLE_IS_SU2_CUBED_NOT_SU3)
    print("cascade:", CASCADE)
    print("verdict:", verdict())
