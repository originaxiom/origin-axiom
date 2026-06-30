"""B306 verdict (pyenv; E6 cascade Sage-verified, recorded) -- the principal-grading cascade + the left-right SM point.

The principal-grading centralizers of E6 (roots height==0 mod N) form a FORCED pseudo-Levi cascade. The SM-shaped
point is N=5 = the LEFT-RIGHT gauge group SU(3)xSU(2)_LxSU(2)_RxU(1)^2 (contains the SM; SM = break SU(2)_R). Chat-1's
"dim-14 window" and "saddle SU(3)xU(1)^4" are both WRONG (no clean dim-14 centralizer; saddle = SU(2)^3, 3rd refute).

This module records the Sage-verified component structures and re-derives the surviving-root counts (pyenv) from the
E6 height distribution. FIREWALL: the cascade is standard E6 (generic); the object connection is the Eisenstein omega
at N=3/6 (B305); the SM endpoint needs external SU(2)_R-breaking + U(1)-projection; the N=5<->level coincidence and
the deformation-as-RG reading are firewalled. Nothing to CLAIMS.
"""

E6_HEIGHT_DIST = {1: 6, 2: 5, 3: 5, 4: 5, 5: 4, 6: 3, 7: 3, 8: 2, 9: 1, 10: 1, 11: 1}

# Sage-verified cascade: N -> (component sizes, dim, label)
CASCADE = {
    1: ([36], 78, "E6"),
    2: ([1, 15], 38, "SU(6)xSU(2)"),
    3: ([3, 3, 3], 24, "SU(3)^3 (trinification)"),
    4: ([1, 3, 3], 20, "SU(3)^2 x SU(2)"),
    5: ([1, 1, 3], 16, "SU(3) x SU(2)_L x SU(2)_R x U(1)^2 (LEFT-RIGHT, contains SM)"),
    6: ([1, 1, 1], 12, "SU(2)^3 (saddle)"),
}

# --- the findings ---
SM_SHAPED_POINT_IS_N5 = True                            # left-right group; SM = break SU(2)_R
N5_IS_LEFT_RIGHT_GROUP = "SU(3)_c x SU(2)_L x SU(2)_R x U(1)^2"
SM_IS_EXACT_ENDPOINT = False                            # needs SU(2)_R breaking + U(1) projection (external)
CHAT1_DIM14_WINDOW_MATCHES_NO_CENTRALIZER = True        # N=4 dim 20, N=5 dim 16 -> no clean dim 14
SADDLE_IS_SU2_CUBED_NOT_SU3U1_4 = True                  # Chat-1 refuted 3rd time (B304, B305, B306)

# --- object connection / firewall ---
EISENSTEIN_POINTS_OBJECT_RELEVANT = "N=3,6 at omega (Q(sqrt-3), B305)"   # the hyperbolic/E6 end
N5_LEVEL_COINCIDENCE_IS_LEAP = True                     # N=5=k+2 (figure-eight WRT level) but golden/zeta_5 end (B261)
CASCADE_IS_GENERIC_E6 = True                            # standard Borel-de Siebenthal; not object-specific
DERIVES_SM_VALUES = False


def mod_count(N):
    return sum(c for h, c in E6_HEIGHT_DIST.items() if h % N == 0)


def verdict():
    counts_ok = all(mod_count(N) == sum(CASCADE[N][0]) for N in range(1, 7) if N > 1)
    structure_ok = (CASCADE[3][0] == [3, 3, 3] and CASCADE[5][0] == [1, 1, 3] and CASCADE[6][0] == [1, 1, 1])
    return bool(counts_ok and structure_ok and SM_SHAPED_POINT_IS_N5 and not SM_IS_EXACT_ENDPOINT
                and CHAT1_DIM14_WINDOW_MATCHES_NO_CENTRALIZER and SADDLE_IS_SU2_CUBED_NOT_SU3U1_4
                and CASCADE_IS_GENERIC_E6 and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("principal-grading cascade (Sage-verified):")
    for N in range(1, 7):
        comps, dim, lab = CASCADE[N]
        print(f"  N={N}: {comps} dim {dim} = {lab}")
    print("SM-shaped point = N=5 (left-right):", N5_IS_LEFT_RIGHT_GROUP, "| SM exact endpoint:", SM_IS_EXACT_ENDPOINT)
    print("saddle = SU(2)^3 not SU(3)xU(1)^4 (Chat-1 refuted 3rd time):", SADDLE_IS_SU2_CUBED_NOT_SU3U1_4)
    print("verdict:", verdict())
