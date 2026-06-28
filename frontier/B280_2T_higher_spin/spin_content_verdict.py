"""B280 verdict (pyenv-safe; heavy GAP in spin_content_2T_gap.py).

The 2T = SL(2,3) higher-spin content: spin-1|2T = rho_3 (the triplet); spin-3/2|2T = 2+2 (two distinct 2-dim
irreps), NOT 3+1. The latter is a NEGATIVE: there is no triplet+singlet, so 'three generations + a Higgs from the
A_4/2T spin-3/2' does not hold. Plus the E6 SU(6)xSU(2) branching 27=(15,1)+(6bar,2) (Weyl-verified). FIREWALLED;
nothing to CLAIMS.md.
"""
TWO_T_DIMS = (1, 1, 1, 2, 2, 2, 3)
SPIN1_MULT = (0, 0, 0, 0, 0, 0, 1)          # = rho_3
SPIN32_MULT = (0, 0, 0, 0, 1, 1, 0)         # = 2 + 2 (two distinct 2-dim irreps)
THREE_GENERATIONS_FROM_SPIN32 = False        # killed: no 3+1 split

# E6 ⊃ SU(6)xSU(2)_R  (Weyl-character verified, branchings.py):
E6_27_UNDER_SU6_SU2 = "(15,1) + (6bar,2)"    # as SU(2): 15·(j=0) + 6·(j=1/2)


def verdict():
    return (SPIN1_MULT[TWO_T_DIMS.index(3)] == 1
            and sum(SPIN32_MULT[i] for i, d in enumerate(TWO_T_DIMS) if d == 2) == 2
            and SPIN32_MULT[TWO_T_DIMS.index(3)] == 0
            and not THREE_GENERATIONS_FROM_SPIN32)


if __name__ == "__main__":
    print("spin-1|2T  =", SPIN1_MULT, "(= rho_3)")
    print("spin-3/2|2T =", SPIN32_MULT, "(= 2+2, NOT 3+1)")
    print("27 under E6 > SU(6)xSU(2):", E6_27_UNDER_SU6_SU2)
    print("verdict:", verdict())
