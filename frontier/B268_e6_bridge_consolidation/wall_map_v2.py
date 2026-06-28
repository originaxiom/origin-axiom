"""B268 -- consolidation of the E6-bridge arc (B262-B267): the five-wall map v2, the E6-bridge ledger, and the
audit of skipped/deferred sub-choices. FIREWALLED (the math is firewall-clean; the physics readings stay in
speculations/). Nothing to CLAIMS.md. Supersedes B259's wall map (which it cites, not edits).

This is the "step back and bank" after six merged results. It restates the five-wall map with the B262-B267
progress folded in, records the E6-bridge as one coherent chain, and inventories what was optional/skipped so the
next phases (T[4_1] Rungs 2-3; walls #3/#4; the integrability rigor upgrade) pick up nothing dropped.
"""

# ---- the E6 bridge, as one chain (each link banked + merged) -------------------------------------------------
E6_BRIDGE = {
    "B262": "T[4_1] reconstructed: U(1) gauge + 2 chirals + monopole superpotential (3d-3d, 2 tetrahedra).",
    "B263": "the Chern-Simons frame pinned (Neumann-Zagier): A^-1 B = [[0,-1],[-1,0]], unit BF coupling to m.",
    "B264": "the E6 character variety tangent space at the principal rep = rank(E6) = 6, graded by exponents "
            "{1,4,5,7,8,11}; directions {4,8} lie beyond F4.",
    "B265": "those deformations integrate (geometric rep is a smooth point) and are E6-Zariski-dense for the "
            "{4,8} directions (Sage: <principal sl2, exp4/8> = e6 (78); exp5/7/11 trapped in f4 (52)) => "
            "genuine E6-irreducible flat connections on the figure-eight EXIST.",
    "B266": "the arithmetic CANONICALLY SELECTS E6: trace field Q(sqrt-3) -> ramified prime 3 -> SL(2,F_3)=2T -> "
            "McKay E6; the figure-eight group itself surjects onto 2T. Two ends: Q(sqrt5)/5 -> 2I -> E8; "
            "E7 (2O) never SL(2,q) -> homeless (reproduces B256). One mechanism for E6/E8/E7.",
    "B267": "the McKay-E6 (arithmetic) and the character-variety-E6 (geometric) are ONE E6: the McKay graph (affine "
            "node removed) reproduces B264's exponents; h=12, #roots=36, dim=78, Molien=(1+q^12)/((1-q^6)(1-q^8)) "
            "all agree. Wall #2's remaining gap is now purely physical.",
}

# ---- the five-wall map v2 (was B259; statuses updated by B260/B264/B265/B266/B267) ---------------------------
# status codes: THEOREM (proven impossible as stated) | DISSOLVED (was a wall, shown to be the wrong question)
#               | REDUCED (open, but cut down to a single named gap) | OPEN | QGAP (quantitative obstruction)
WALLS = {
    1: dict(name="SL(2,C) holonomy vs compact E6",
            v1_status="THEOREM (for the holonomy-breaking bridge)",
            v2_status="DISSOLVED",
            update="B260: SL(2,C) is the Coulomb branch of T[4_1] (a fugacity coordinate), not a gauge holonomy, "
                   "so 'no hom into compact E6' (B247) is about the wrong object. B264/B265: genuine "
                   "E6-irreducible flat connections EXIST near the geometric rep. The wall was a category slip."),
    2: dict(name="McKay-E6 vs a dynamical gauge group / type selection",
            v1_status="OPEN (with a hidden extra step: input-E6 != output-McKay-E6)",
            v2_status="REDUCED (to one physics conjecture; Lie-theoretic side de-risked)",
            update="B266: the output-McKay-E6 is canonically selected by the trace field's ramified prime (chain of "
                   "theorems; the figure-eight group surjects onto 2T). B267: that E6 and the character-variety E6 "
                   "coincide on all Lie invariants. Remaining gap = ONLY 'does the 3d-3d INPUT type equal the "
                   "manifold's arithmetic type?' -- a sharp physics conjecture, no math obstruction left."),
    3: dict(name="chirality / amphicheiral tau",
            v1_status="OPEN (object-undecidable, externally decidable)",
            v2_status="OPEN (targeted next)",
            update="unchanged. The object is CP-symmetric (B252); SSB of the amphicheiral tau is the sharp, "
                   "well-posed question needing external dynamics. Phase: walls #3."),
    4: dict(name="3d (T[4_1]) vs 4d (SM)",
            v1_status="OPEN (uncomputed lift)",
            v2_status="OPEN (targeted next)",
            update="unchanged. The class-S / 4-manifold lift is a framework but uncomputed for this object. "
                   "Phase: walls #4. (T[4_1] Rung 3 partition functions are the prerequisite handle.)"),
    5: dict(name="scale / DESI (topological Lambda)",
            v1_status="QGAP (122 orders) + FIREWALLED hook",
            v2_status="QGAP (122 orders) + FIREWALLED hook",
            update="unchanged. G*Lambda dimensionless; golden k=3 -> Planck-scale Lambda, 122 orders from DESI. "
                   "S043 hook stands as a rhyme, not contact."),
}

# ---- the audit: sub-choices we passed while choosing (optional/skipped-but-important) -----------------------
# status: PLANNED (scheduled in a named phase) | DONE | DROPPED (justified)
SKIPPED = {
    "t41_rung2": dict(what="T[4_1] Rung 2: the flavor symmetry precisely + the cusp Weyl Z/2 (m<->1/m) -- does it "
                           "enhance to SU(2)? (S033; the one honest place wall #2 gets tested, not asserted)",
                      from_="B262", status="PLANNED (Phase 2: T[4_1])"),
    "t41_rung3": dict(what="T[4_1] Rung 3: the partition functions (state integral / index / holomorphic blocks) "
                           "reproduce B250 (complex vol), B260 (A-poly), B261 (colored Jones); also the wall-#2 "
                           "test 'does Z[T[4_1]] know about 2T / the ramified prime?'",
                      from_="B262", status="PLANNED (Phase 2: T[4_1])"),
    "integrability_cup_product": dict(what="B265 CITED smoothness (Menal-Ferrer-Porti) for integrability rather "
                                           "than computing the cup-product obstruction H^1 x H^1 -> H^2 directly; "
                                           "the obstruction vanishing at rho_prin is the optional rigor upgrade.",
                                      from_="B264/B265", status="PLANNED (Phase 3: rigor upgrade)"),
    "wall3_chirality_ssb": dict(what="SSB of the amphicheiral tau as a chirality source -- a well-posed question "
                                     "needing external dynamics; never computed.",
                                from_="B252/B259", status="PLANNED (Phase 4: walls #3)"),
    "wall4_4d_lift": dict(what="the class-S / 4-manifold lift of T[4_1]; never computed.",
                          from_="B253/B259", status="PLANNED (Phase 4: walls #4)"),
}


if __name__ == "__main__":
    print("=== B268: the E6-bridge arc, consolidated ===\n")
    print("E6 bridge (B262-B267), one chain:")
    for k, v in E6_BRIDGE.items():
        print(f"  {k}: {v}")

    print("\nFive-wall map v2 (status change vs B259):")
    code = lambda s: s.split("(")[0].strip()          # leading status code, ignoring the annotation
    for k, w in WALLS.items():
        arrow = "" if code(w["v1_status"]) == code(w["v2_status"]) else f"   [{code(w['v1_status'])} -> {code(w['v2_status'])}]"
        print(f"  #{k} {w['name']}: {w['v2_status']}{arrow}")
    changed = [k for k, w in WALLS.items() if code(w["v1_status"]) != code(w["v2_status"])]
    print(f"\n  walls with a status-code change: #{changed}  (#1 dissolved, #2 reduced); #3/#4 targeted next; #5 unchanged.")
    assert set(changed) == {1, 2}

    print("\nAudit -- skipped/deferred sub-choices (nothing dropped silently):")
    for key, s in SKIPPED.items():
        print(f"  [{s['status']:<26}] {key} (from {s['from_']})")
    assert all(s["status"].startswith(("PLANNED", "DONE", "DROPPED")) for s in SKIPPED.values())
    assert len(E6_BRIDGE) == 6
    print("\n  => arc banked; 5 deferred items all assigned to a phase. PASS")
