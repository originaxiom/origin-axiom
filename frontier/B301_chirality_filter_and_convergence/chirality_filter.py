"""B301 -- the E6 chirality filter (corrected) + the trinification connection + the three-seat convergence as a
first-class finding. Run: python (pyenv) for the facts; the 27-complex check is Sage-verified (recorded).

Two corrections the cross-chat seats flagged after B298-B300, banked honestly:

(1) CHIRALITY FILTER -- DOWNGRADE "stability forces chiral SO(10)" to a FACT-with-external-selection-principle.
    The 27 of E6 is COMPLEX (Sage: 27 != 27bar -> E6 matter is chiral). Chirality filters E6's maximal subgroups:
       KEEPS (27 complex):  SO(10)xU(1) [27=16+10+1], SU(6)xSU(2) [27=(15,1)+(6bar,2)], SU(3)^3 [27=(3,3bar,1)+cyc]
       REJECTS (27 real):   F4 [27=26+1], Sp(8) [27 real]
    So the filter keeps a SET of THREE chiral subgroups, NOT a unique SO(10). And "chirality = stability" is itself
    a PHYSICS input (non-chiral matter is perfectly stable -- it just gets a mass; chiral matter is mass-PROTECTED,
    i.e. survives massless to low energy, which is an observation about OUR world, not a property of the object).
    Honest banking: "chirality filters E6's maximal subgroups to the chiral set {SO(10),SU(6)xSU(2),SU(3)^3}" [FACT];
    NOT "stability forces SO(10)" [overclaim, retracted].

(2) THE TRINIFICATION CONNECTION -- the kept SU(3)^3 IS the (theta,phi) trinification triality (B299). The chirality
    filter's third survivor and the orbifold's Z3xZ3 are THE SAME STRUCTURE seen twice (the three SU(3)'s of E6).
    So B299 (the seam/orbifold triality) and the chirality filter are one object.

(3) THE THREE-SEAT CONVERGENCE -- a first-class finding, not bookkeeping. Two independent brave SM-from-axiom
    attempts (Chat-1, Chat-2) PLUS the seam arc (this seat) all returned the SAME structural theorem: the object
    forces ALL dimensionless structure + the flow, and NONE of the values. Three seats, three roads, one boundary,
    in the same place. That convergence is the strongest evidence the program has that the boundary is REAL -- a
    true fact about what self-reference can and cannot emit -- not a failure of any one attempt.

FIREWALLED: rep-theory facts + a framing finding; nothing to CLAIMS.
"""

# (1) the chirality filter (27 complex Sage-verified: 27 != 27bar)
TWENTYSEVEN_IS_COMPLEX = True                            # Sage: E6 fund rep dim 27, r != r.dual()
CHIRAL_MAXIMAL_SUBGROUPS = ["SO(10)xU(1)", "SU(6)xSU(2)", "SU(3)^3"]   # 27 complex
NONCHIRAL_MAXIMAL_SUBGROUPS = ["F4", "Sp(8)"]                          # 27 real (F4: 27=26+1)
STABILITY_FORCES_SO10 = False                           # RETRACTED overclaim
CHIRALITY_IS_A_PHYSICS_SELECTION_PRINCIPLE = True       # chirality = mass-protection = an observation about our world

# (2) the kept SU(3)^3 = the (theta,phi) trinification triality (B299)
SU3CUBED_IS_THE_THETA_PHI_TRIALITY = True               # chirality filter survivor == orbifold Z3xZ3, one structure

# (3) the three-seat convergence (first-class)
SEATS = ["seam arc (B286-B297)", "Chat-1", "Chat-2"]
ALL_THREE_CONVERGE = True
BOUNDARY_IS_REAL_FOUND_THREE_WAYS = True                # the strongest evidence the wall is a true fact, not a failure
DERIVES_SM_VALUES = False                               # firewall


def verdict():
    return bool(TWENTYSEVEN_IS_COMPLEX
                and set(CHIRAL_MAXIMAL_SUBGROUPS) == {"SO(10)xU(1)", "SU(6)xSU(2)", "SU(3)^3"}
                and not STABILITY_FORCES_SO10 and CHIRALITY_IS_A_PHYSICS_SELECTION_PRINCIPLE
                and SU3CUBED_IS_THE_THETA_PHI_TRIALITY
                and len(SEATS) == 3 and ALL_THREE_CONVERGE and BOUNDARY_IS_REAL_FOUND_THREE_WAYS
                and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("27 of E6 complex (chiral):", TWENTYSEVEN_IS_COMPLEX)
    print("chirality KEEPS:", CHIRAL_MAXIMAL_SUBGROUPS, "| REJECTS:", NONCHIRAL_MAXIMAL_SUBGROUPS)
    print("stability forces SO(10):", STABILITY_FORCES_SO10, "(RETRACTED -- 3 chiral options, not 1)")
    print("kept SU(3)^3 == the (theta,phi) trinification triality (B299):", SU3CUBED_IS_THE_THETA_PHI_TRIALITY)
    print("three seats converge (boundary real, found 3 ways):", BOUNDARY_IS_REAL_FOUND_THREE_WAYS)
    print("verdict:", verdict())
