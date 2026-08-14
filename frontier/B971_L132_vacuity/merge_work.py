#!/usr/bin/env python
"""Merge the two computation routes into the cell's work.json deliverable."""
import json

su5 = json.load(open('work.json'))          # written by su5_anomaly_verdict.py
e6 = json.load(open('e6_weight_route_out.json'))

out = {
    "cell": "B971_L132_vacuity",
    "lead": "L132",
    "date": "2026-08-08",
    "lane": "MATHEMATICS",
    "gate5": "untouched",
    "claims_md": "nothing",

    "verdict": {
        "L132_status": "VACUOUS on complete 27s -- CONFIRMED by independent recomputation",
        "vacuity_degree": "TRIPLE",
        "layer_1": "every SM anomaly coefficient vanishes on the complete 27",
        "layer_2": "it vanishes SEPARATELY on each SO(10) block -- no 16 <-> (10+1) cross-talk",
        "layer_3": "the 12 exotics are a REAL (vector-like) SM rep, so their contribution is "
                   "identically zero for ARBITRARY vector-like hypercharges -- the check "
                   "carries zero information about the exotic sector",
        "does_Y_fall_out": "NO on the complete 27 (3-dim solution space out of 3); "
                           "NO on the complete 16 either (2-dim: Y and chi both survive); "
                           "YES only on the chiral 15, i.e. after deleting nu_R",
        "selective_power_lives_in": "the truncation 16 -> 15, which is an IMPORTED input",
    },

    "route_1_su5_states": su5,
    "route_2_e6_weight_orbit": e6,

    "routes_agree": {
        "su5_content": "route 2's omega_6 orbit gives {10, 5, 5bar x2, 1 x2} = route 1's "
                       "assembled spectrum exactly; the omega_1 orbit is its conjugate",
        "so10_split": "route 2 recovers 16 + 10 + 1 with psi-grade ratios (1, -2, 4) "
                      "from the Cartan matrix alone -- route 1 had cited that branching",
        "vanishing": "route 1: zero for the 3 SM-relevant abelian directions. "
                     "route 2: zero identically in all SIX e6 Cartan coordinates (stronger)",
    },

    "labels": {
        "COMPUTED": [
            "hypercharge generator on the 5 (unique traceless diag(a,a,a,b,b), 3a+2b=0)",
            "the 10 of SU(5) as Lambda^2(5), with Y and SU(3)xSU(2) labels derived from indices",
            "all four SM anomaly coefficients, per SU(5) irrep and per SO(10) irrep",
            "[SU(3)]^3 and the Witten SU(2) doublet parity",
            "the 27 as an E6 Weyl orbit from the Cartan matrix",
            "sum lambda(H) = 0 and sum lambda(H)^3 = 0 identically in all 6 Cartan coords",
            "the SO(10) and SU(5) branchings, by fundamental-coweight grading",
            "the 27 is complex (omega_1 and omega_6 orbits have different weight sets)",
            "MB12 failure controls: lone 10, lone 5bar, 27 minus e^c, 27 minus the exotic 5",
            "exotic blindness: coefficients identically zero in free y1, y2",
            "solution-space dimensions for Q = aY + b*chi + c*psi over 27 / 16 / 15",
        ],
        "CITED_not_re_derived": [
            "anomaly-coefficient conventions (T(3)=1/2, T(2)=1/2, A(3)=+1) -- standard "
            "normalisation, stated in the script header",
            "Q_em = T3 + Y as the hypercharge normalisation convention",
            "the E6 -> SO(10) x U(1) -> SU(5) x U(1) branching PATTERN in route 1 "
            "(subsequently COMPUTED independently in route 2)",
            "that only the A_n (n>=2) simple algebras have a nonzero symmetric cubic "
            "invariant -- used only as background, the E6 case is computed here",
        ],
    },

    "prior_art": {
        "B864_anomaly_ledger": "computed the same ledger 2026-08-03; its uniqueness result "
                               "is REPRODUCED here (psi over 16: Tr=16, Tr^3=16, [SU3]^2=2; "
                               "chi over 15: Tr=5, Tr^3=125) and SCOPED: it holds over the "
                               "imported chiral truncation, not over the object's 27",
        "B951": "flagged the vacuity as probable; this cell converts it to computed",
        "scout_PRIOR_ART_ANOMALY.md": "independent 2047-subset map; not relied on here",
        "status": "this cell REPRODUCES, it does not discover",
    },

    "non_vacuity_requirements": [
        "(1) the spectrum must NOT be a union of complete E6 irreps -- computed: every "
        "abelian direction in e6 is anomaly-free on a complete 27",
        "(2) it must not even be a union of complete SO(10) irreps -- computed: each of "
        "16, 10, 1 vanishes separately, so the deletion must SPLIT an SO(10) multiplet",
        "(3) the deleted set must not be vector-like -- computed: any real subset "
        "contributes identically zero to the hypercharge conditions",
        "(4) a handedness assignment per state is required for the functional to be "
        "defined at all",
        "(5) even then the check does not select the SM: it selects a 1-dim abelian "
        "direction only relative to whichever truncation was imported",
    ],

    "what_this_does_not_establish": [
        "it does not refute B864; it reproduces and scopes it",
        "it says nothing about whether the object supplies a truncation "
        "(that is the scout's question, answered there, not re-litigated here)",
        "it says nothing about values, generations, the real form, or spacetime",
        "the 2047-subset enumeration is the scout's, not re-run here",
        "no literature search was run from this cell",
    ],

    "reproduce": [
        "python su5_anomaly_verdict.py   -> work.json (pre-merge) + su5_anomaly_verdict_out.txt",
        "python e6_weight_route.py       -> e6_weight_route_out.json + .txt",
        "python merge_work.py            -> work.json (this file)",
    ],
}

json.dump(out, open('work.json', 'w'), indent=2)
print("merged -> work.json")
print("verdict:", out['verdict']['L132_status'])
