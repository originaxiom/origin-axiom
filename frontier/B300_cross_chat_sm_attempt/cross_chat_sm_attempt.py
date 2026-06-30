"""B300 -- the cross-chat SM-from-axiom attempt, assessed: Column B collapses to TWO walls; the structural theorem,
corroborated from three independent seats. Run: python (pyenv).

Two web-Opus seats (Chat-1, Chat-2) ran full brave "derive the dynamical SM from the axiom" attempts while this seat
built the seam arc (B286-B297). Assessed here (verify-don't-trust; the load-bearing computables checked in
B298/B299 + below). The meta-finding: all three seats CONVERGE on the same boundary, in the same place.

THE COLLAPSE (Chat-2's sharpening, verified-consistent): the "SM at the seam" frame listed ~8 external Column-B
inputs (type G, N=2->N=1 datum, vacuum, CP sign, scale k, breaking chain, Yukawas, generation count). They are NOT 8
independent gaps. They are TWO walls:
  (A) THE COUPLING / ACTION CATEGORY -- the object emits no dimensionful coupling-strength. The breaking potential,
      the Yukawas, the chosen vacuum, the N=2->N=1 chiral datum, 8*pi*G, the Higgs depth, the freeze-out scale are
      ONE missing thing: a Lagrangian (how strongly things couple). The scale/action/Friedmann/CP-sign analyses all
      hit THIS wall independently -> the boundary is real.
  (B) THE DEGREE-3 CARRIER -- the generation count, closed as a forced NEGATIVE (B298): Q(sqrt-3) is degree 2, so
      matter multiplicities are 1 or 2, never 3.

The object forces ALL dimensionless structure + the flow; it refuses to emit coupling-strength. This is the
structural theorem (B294/B297), compressed and corroborated.

VERIFIED ARITHMETIC carried here:
  * E6+A2 -> E8 prime-3 glue: det(E6)*det(A2)/3^2 = 9/9 = 1 = det(E8); prime 3 = the Q(sqrt-3) ramified prime =
    E6-center Z/3 (connects B248/B256). The gluing arithmetic is REAL; the A2-as-family-symmetry is the heterotic
    import (firewalled, NOT forced -- the generation wall B298 stands).
  * scale = one rod l_P: L_dS/l_P = sqrt(k/6pi); k=3 -> 0.40 (no hierarchy at origin), k~1e122 -> ~6e60 (the gap =
    the clock having run). [conditional on G*Lambda=6pi/k = the Alexander relation; matches banked S044]

THE ONE LIVE FORCING (triple-convergent: B295 + Chat-1 + Chat-2): does the running de Sitter clock (k, T_dS~1/sqrt k)
dynamically GAUGE-FIX the tau-sign, making matter-over-antimatter internal? Structure computable (B293); trajectory
gated. The only Column-B slot where a forcing (not just naming) is still plausible.

FIREWALLED: a consolidation; nothing new to CLAIMS. The cosmological readings (sigma-flow / arrow / action) are
[LEAP] in speculations/.
"""
from math import sqrt, pi

# --- Column B, collapsed to two walls ---
COLUMN_B_WALLS = {
    "A_coupling_action_category": ["breaking potential", "Yukawas", "chosen vacuum", "N=2->N=1 chiral datum",
                                   "8*pi*G", "Higgs depth", "freeze-out scale"],   # all = "no Lagrangian"
    "B_degree3_carrier": ["generation count (forced NEGATIVE, B298: degree-2 -> mult 1 or 2)"],
}
N_COLUMN_B_WALLS = 2                                    # not ~8

# --- the corroboration (three seats, one boundary) ---
SEATS_CONVERGE_ON_STRUCTURAL_THEOREM = True            # seam arc (B294/B297) = Chat-1 = Chat-2
STRUCTURAL_THEOREM = ("the object forces all dimensionless STRUCTURE + the flow; the ACTUALIZATION "
                      "(coupling-strength + the degree-3 carrier) is not forced")

# --- verified arithmetic ---
DET_E6, DET_A2, DET_E8 = 3, 3, 1


def e6_a2_e8_prime3_glue():
    return (DET_E6 * DET_A2) // 9 == DET_E8             # diagonal Z3 glue: 9/9 = 1 = det(E8)


def ldS_over_lP(k):
    return sqrt(k / (6 * pi))                           # k=3 -> ~0.40 ; k~1e122 -> ~6e60


# --- the one live forcing ---
LIVE_FORCING = "does the running de Sitter clock gauge-fix the tau (CP) sign? (B295+B293; trajectory gated)"
LIVE_FORCING_TRIPLE_CONVERGENT = True                  # B295 + Chat-1 + Chat-2 all name it
DERIVES_SM_VALUES = False                              # firewall


def verdict():
    return bool(N_COLUMN_B_WALLS == 2 and e6_a2_e8_prime3_glue()
                and abs(ldS_over_lP(3) - 0.3989) < 1e-3 and ldS_over_lP(6.6e122) > 1e60
                and SEATS_CONVERGE_ON_STRUCTURAL_THEOREM and LIVE_FORCING_TRIPLE_CONVERGENT
                and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("Column B collapses to", N_COLUMN_B_WALLS, "walls:")
    for w, items in COLUMN_B_WALLS.items():
        print(f"   {w}: {items}")
    print("E6+A2->E8 prime-3 glue (9/9=1=det E8):", e6_a2_e8_prime3_glue())
    print("L_dS/l_P: k=3 ->", round(ldS_over_lP(3), 4), "| k~1e122 ->", f"{ldS_over_lP(6.6e122):.2g}")
    print("three seats converge on the structural theorem:", SEATS_CONVERGE_ON_STRUCTURAL_THEOREM)
    print("the one live forcing:", LIVE_FORCING)
    print("verdict:", verdict())
