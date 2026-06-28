"""B266 surjection verdict (pyenv-safe; the heavy GAP computation is verify_surjections.py).

Records the verified (sage-python + GAP GQuotients) finding that the E6 and E8 ends are arithmetically ASYMMETRIC
at the group level: pi_1(4_1) genuinely surjects onto 2T=SL(2,F_3) (E6 leg) but NOT onto A_5 or 2I=SL(2,F_5)
(E8 leg). Confirms Stuebner 2025 (arXiv:2502.06488). FIREWALLED; nothing to CLAIMS.md.
"""
# surjections up to automorphism (sage-python + GAP, 2026-06-28)
SURJECTION_COUNTS = {"2T = SL(2,3)": 2, "A5 = PSL(2,5)": 0, "2I = SL(2,5)": 0}

E6_LEG_GENUINE = SURJECTION_COUNTS["2T = SL(2,3)"] > 0      # the figure-eight's own trace field, ramified prime 3
E8_LEG_SURJECTION = SURJECTION_COUNTS["2I = SL(2,5)"] > 0   # False: E8 end is field-level (Q(sqrt5)/5), not a 4_1 surjection
CONFIRMS = "Stuebner 2025 (arXiv:2502.06488): pi_1(4_1) does not surject onto A5, hence not onto 2I"


def verdict():
    return E6_LEG_GENUINE and not E8_LEG_SURJECTION


if __name__ == "__main__":
    print("counts:", SURJECTION_COUNTS)
    print("E6 leg genuine:", E6_LEG_GENUINE, "| E8 leg a 4_1-surjection:", E8_LEG_SURJECTION)
    print("verdict (asymmetric ends):", verdict())
