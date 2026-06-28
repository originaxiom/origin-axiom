"""B278 -- consolidation of the E6-bridge arc through B277: the five-wall map v3, with the existence story CLOSED
(B274/B275) and the input-required walls B272 flagged as missing now recorded EXPLICITLY. FIREWALLED (the math is
firewall-clean; physics readings stay in speculations/). Nothing to CLAIMS.md. Supersedes B268's v2 (cites, not edits).

This is the "step back and bank" after the post-B273 push (B274 smoothness, B275 explicit witness, B276 zeta_3
probe, B277 4d-lift characterization). It folds those into the wall map, and -- fixing the gap B272 found -- adds the
family-replication, SM-matter, and Lambda-sign walls as explicit entries rather than leaving them invisible.
"""

# ---- the E6 bridge, as one chain (each link banked + merged) -------------------------------------------------
E6_BRIDGE = {
    "B262": "T[4_1] reconstructed: U(1) + 2 chirals + monopole superpotential (3d-3d, 2 tetrahedra).",
    "B263": "Chern-Simons frame pinned (Neumann-Zagier): A^-1 B = [[0,-1],[-1,0]], unit BF coupling to m.",
    "B264": "E6 character variety tangent space at rho_prin = rank(E6)=6, graded by exponents {1,4,5,7,8,11}.",
    "B265": "{4,8} deformations are E6-Zariski-dense (<principal sl2, exp4/8>=e6); E6-irreducible flat connections exist.",
    "B266": "arithmetic CANONICALLY selects E6: Q(sqrt-3) -> prime 3 -> SL(2,F_3)=2T -> McKay E6; two ends E6/E8, E7 homeless.",
    "B267": "McKay-E6 = character-variety-E6 (exponents, h=12, #roots=36, dim=78, Molien all agree).",
    "B273": "the e6 bracket-coupled quadratic cup-product H^1xH^1->H^2(e6) VANISHES IDENTICALLY (integration to 2nd order).",
    "B274": "rho_prin is a SMOOTH point (boundary/cusp MFP criterion {6,6,12}+regular meridian; cubic obstruction=0) "
            "=> E6-irreducible flat connections exist UNCONDITIONALLY (all orders).",
    "B275": "an EXPLICIT (A,B) flat E6 connection (|R-I|~8e-8, nonzero {4,8}) -- the witness made concrete.",
    "B276": "Z's E6-end arithmetic = Q(sqrt-3): colored Jones degenerates at zeta_3/zeta_6 into O_{Q(sqrt-3)}, "
            "(1-zeta_3)(1-zeta_3^2)=3 -> 2T (a COHERENCE, not a settlement of wall #2).",
    "B277": "wall #4 made precise: canonical N=2* SU(2) lift (fiber Sigma_{1,1}, phi=RL an S-duality element); a "
            "chiral 4d SM is blocked by two NAMED inputs (the N=2->N=1 datum; the free type G = the CRUX).",
}

# status codes: DISSOLVED | REDUCED | CHARACTERIZED (precise input-required statement) | OPEN | QGAP
WALLS = {
    1: dict(name="SL(2,C) holonomy vs compact E6", status="DISSOLVED",
            note="B260: SL(2,C) is the Coulomb branch, not a gauge holonomy. B264/B265/B274/B275: E6-irreducible "
                 "flat connections exist UNCONDITIONALLY (rho_prin a smooth point) with an explicit witness. Closed."),
    2: dict(name="McKay-E6 vs type selection", status="REDUCED",
            note="B266/B267: output-E6 canonically selected and = character-variety-E6. B276: Z's special-value "
                 "arithmetic is the same 2T field (a coherence). Remaining gap = ONLY the CRUX (input=output E6)."),
    3: dict(name="chirality / amphicheiral tau", status="OPEN",
            note="B271: chirality locus = the 26 = E6-Zariski-dense {4,8} directions; tau = E6 outer automorphism "
                 "(+1 on f4, -1 on 26). Available but undetermined; SSB needs external dynamics."),
    4: dict(name="3d (T[4_1]) vs 4d (SM)", status="CHARACTERIZED",
            note="B277: a CANONICAL N=2* SU(2) lift exists (class-S of the fiber Sigma_{1,1}; phi=RL an S-duality "
                 "element; T[4_1] = its duality wall). Chiral 4d SM blocked by two named inputs: the N=2->N=1 datum "
                 "(= wall #3) and the free type G (= the CRUX). Not 'no lift' -- a precise input-required result."),
    5: dict(name="scale / DESI (topological Lambda)", status="QGAP",
            note="unchanged. G*Lambda dimensionless; golden k=3 -> Planck-scale Lambda, 122 orders from DESI."),
}

# ---- the load-bearing conjecture (everything physical hangs here) --------------------------------------------
CRUX = dict(name="input-E6 = output-E6",
            note="the 3d-3d / class-S INPUT type G is a free choice; the arithmetic fixes the OUTPUT (McKay-E6). "
                 "B276 shows a coherence but not 2T acting; B277 shows the 4d lift inherits the same freedom. "
                 "Unsettled in-sandbox; needs a genuine T[4_1;E6] computation or a specialist. STOP-GATE.")

# ---- input-required / specialist walls that B272 found MISSING from the map (now recorded) -------------------
INPUT_REQUIRED_WALLS = {
    "family_replication": "3 chiral generations = 3x27; one figure-eight gives one character variety. The Z/3 is "
                          "the Eisenstein cube-root / cone order (B257), NOT 3 generations. Specialist/SM input.",
    "sm_matter_breaking": "27 -> one SU(5) generation is GENERIC E6, not object-specific (B252/B254); the E6->SM "
                          "breaking chain, exotics disposal, hypercharge are unaddressed. Specialist/SM input.",
    "lambda_sign": "4_1 hyperbolic => Lambda<0 / AdS (B259); observed dark energy is Lambda>0 / dS. The SIGN "
                   "mismatch is SEPARATE from wall #5's 122-order magnitude. Input-required.",
}
ASSUMPTIONS = {
    "principal_embedding": "the E6 character variety is built on the principal sl(2)->e6 (an input, not forced by 4_1).",
    "vacuum_selection": "the object supplies the LOCUS (chirality=E6-density), not the VACUUM; no dynamics/scale/CP phase.",
}


def consistency():
    """The map is complete and honest: 5 walls (1 dissolved, 1 reduced, 1 open, 1 characterized, 1 qgap), the CRUX
    named, and the 3 previously-missing input-required walls + 2 assumptions recorded."""
    statuses = {WALLS[i]["status"] for i in WALLS}
    return (len(WALLS) == 5 and statuses == {"DISSOLVED", "REDUCED", "OPEN", "CHARACTERIZED", "QGAP"}
            and len(E6_BRIDGE) == 11 and len(INPUT_REQUIRED_WALLS) == 3 and len(ASSUMPTIONS) == 2
            and CRUX["name"] == "input-E6 = output-E6")


if __name__ == "__main__":
    print("=== B278: the E6-bridge wall map v3 (through B277) ===\n")
    print("E6 bridge chain (11 banked results):")
    for k, v in E6_BRIDGE.items():
        print(f"  {k}: {v}")
    print("\nFive walls:")
    for i in WALLS:
        print(f"  #{i} [{WALLS[i]['status']}] {WALLS[i]['name']}")
    print(f"\nCRUX (load-bearing): {CRUX['name']} -- {CRUX['note']}")
    print("\nInput-required walls (B272-flagged, now explicit):", list(INPUT_REQUIRED_WALLS))
    print("Assumptions:", list(ASSUMPTIONS))
    print("\nconsistency:", consistency())
    assert consistency()
