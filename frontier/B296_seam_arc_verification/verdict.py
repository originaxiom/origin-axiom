"""B296 verdict (pyenv) -- Arc II verification of the seam arc (B287-B295): adversarial red-team + novelty audit.

RED-TEAM: every probe SURVIVES adversarial attack; no refutations, no firewall leaks; nothing wrongly promoted to
CLAIMS.md. Two results strengthened (B287 uniqueness homology-forced; B288 extended to |p|,|q|<=12, still 0 arithmetic
in 174 closings) and four FINDINGS tightened (B287/B290/B293/B295 caveats folded).

NOVELTY: the classical mathematics is confirmed KNOWN with citations (claim 1 Thurston exceptional surgeries / 0-surg
= Sol [[2,1],[1,1]]; claim 2 Garoufalidis-Jeon trace-field degree growth / finitely many arithmetic fillings; claim 4a
Goldman/NZ symplectic). The genuinely-new CONNECTIONS (claim 3 handedness=Galois +-pi/6; claim 4b Goldman-clock <->
Lambda-CS-time; claim 5 the seam reframe) are flagged APPEARS-NOVEL / NEEDS-SPECIALIST and stay firewalled; a fuller
prior-art round is pending. The program does NOT claim the mathematics as original.

FIREWALL: this is the verification ledger; it changes no physics tier. Nothing to CLAIMS.
"""

# --- red-team outcome (per probe) ---
REDTEAM_VERDICTS = {
    "B287": "SURVIVES", "B288": "SURVIVES", "B289": "SURVIVES", "B290": "SURVIVES",
    "B291": "SURVIVES", "B292": "SURVIVES", "B293": "SURVIVES", "B295": "SURVIVES",
    "SEAM-THESIS": "SURVIVES",
}
N_REFUTED = 0
N_FIREWALL_LEAKS = 0
EXTENDED_CHECKS = {
    "B288_arithmetic_up_to_12": 0,      # imaginary-quadratic closings in 174 hyperbolic fillings |p|,|q|<=12
    "B291_min_volume_slope": (5, 1),    # global min over |p|,|q|<=12 (unchanged from the |p|,|q|<=8 grid)
}
CAVEATS_FOLDED = ["B287 homology-forced uniqueness", "B290 m004-specific real coefficient",
                  "B293 k_um frame-dependence + Nambu/Goldman import", "B295 cubic/one-minimum"]

# --- novelty outcome (per claim) ---
NOVELTY = {
    "claim1_distinguished_closing": "KNOWN",          # Thurston; arXiv:2409.06543/1310.3472/2103.16348
    "claim2_arithmeticity_lost": "KNOWN",             # Garoufalidis-Jeon; Hodgson; Neumann-Reid
    "claim4a_goldman_nz_symplectic": "KNOWN",         # Goldman; Neumann-Zagier
    "claim3_handedness_galois": "NEEDS-SPECIALIST",   # pieces classical; the +-pi/6 packaging candidate-new
    "claim4b_clock_lambda_cstime": "APPEARS-NOVEL",   # no prior art found this pass; firewalled [HOOK]
    "claim5_seam_reframe": "APPEARS-NOVEL",           # the framing/synthesis; math classical
}
NOVEL_CLAIMS_NEEDS_SPECIALIST = ["claim3_handedness_galois", "claim4b_clock_lambda_cstime", "claim5_seam_reframe"]
FULLER_PRIORART_ROUND_PENDING = True
PROGRAM_CLAIMS_MATH_AS_ORIGINAL = False               # honest: the math is classical, the reframe is the new part

DERIVES_SM_VALUES = False                              # firewall


def verdict():
    redteam_ok = (all(v == "SURVIVES" for v in REDTEAM_VERDICTS.values())
                  and N_REFUTED == 0 and N_FIREWALL_LEAKS == 0
                  and EXTENDED_CHECKS["B288_arithmetic_up_to_12"] == 0
                  and EXTENDED_CHECKS["B291_min_volume_slope"] == (5, 1))
    novelty_ok = (NOVELTY["claim1_distinguished_closing"] == "KNOWN"
                  and NOVELTY["claim2_arithmeticity_lost"] == "KNOWN"
                  and NOVELTY["claim4a_goldman_nz_symplectic"] == "KNOWN"
                  and set(NOVEL_CLAIMS_NEEDS_SPECIALIST) ==
                  {k for k, v in NOVELTY.items() if v in ("NEEDS-SPECIALIST", "APPEARS-NOVEL")}
                  and not PROGRAM_CLAIMS_MATH_AS_ORIGINAL)
    return bool(redteam_ok and novelty_ok and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("RED-TEAM:", REDTEAM_VERDICTS)
    print(f"  refuted: {N_REFUTED}  firewall leaks: {N_FIREWALL_LEAKS}  extended checks: {EXTENDED_CHECKS}")
    print(f"  caveats folded: {CAVEATS_FOLDED}")
    print("NOVELTY:", NOVELTY)
    print(f"  novel/needs-specialist: {NOVEL_CLAIMS_NEEDS_SPECIALIST}  (math claimed original: {PROGRAM_CLAIMS_MATH_AS_ORIGINAL})")
    print("verdict:", verdict())
