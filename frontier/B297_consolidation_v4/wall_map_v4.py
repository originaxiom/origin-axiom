"""B297 -- consolidation of the SEAM arc (B286-B296) into the five-wall map v4. FIREWALLED (the math is firewall-clean;
physics readings stay in speculations/). Nothing to CLAIMS.md. Supersedes B278's v3 (cites, not edits).

The seam reframe (B286) corrected the load-bearing framing: the figure-eight is an OPEN object (a complement), so its
symmetries are open-object symmetries and CLOSING it (Dehn filling = the interaction with the nothing) is where they
break. The seam arc (B287-B295) then worked every implication, and B296 verified the whole arc (red-team + novelty).
v4 folds this in: each wall is re-examined THROUGH the seam, the structural theorem is relocated to the seam, and the
matter map (the Sakharov-style 'where matter comes from' accounting) is recorded.
"""

# ---- the seam arc, as one chain (each link banked + merged) --------------------------------------------------
SEAM_ARC = {
    "B286": "the seam: the figure-eight is OPEN; closing it (Dehn filling) breaks amphichirality and supplies "
            "chirality/CP-sign/scale/clock AT THE CUSP. Curie was a closed-system theorem misapplied. (P011 corrected.)",
    "B287": "the distinguished closing: the fiber/0-slope (0,1) = the UNIQUE Sol torus bundle among the 10 "
            "exceptionals, monodromy EXACTLY A=[[2,1],[1,1]] (P1, A=LR) + the P8 torsion ladder. SELECTIVE.",
    "B288": "the arithmetic census: NO closed filling re-sees Q(sqrt-3) (E6 atom); E6 is an OPEN-object property, "
            "LOST on closing (54-174 closings, 0 arithmetic). Leaning CATALOGUE for the CRUX.",
    "B289": "the CP sign: all 78 closings chiral, forced sign law CS(p,-q)=-CS(p,q); handedness = Q(sqrt-3) Galois "
            "conjugation = the B285 +-pi/6 / tau swap. The sign LAW forced; the SIGN itself external (CP-symmetric).",
    "B290": "the scale ladder: ell_C(1,n)=2pi*i/n+(pi/sqrt3)/n^2 (NZ, cusp-shape-controlled); filling n =/= WRT "
            "level k (independent axes). G*Lambda link HELD (122-order gap).",
    "B291": "the scale-extremal closing: min-vol (5,1)=m003(-2,3); non-arithmetic, not the fiber -> selection is "
            "AXIS-STRATIFIED (different axes pick different closings).",
    "B292": "multiplicity is TRIPARTITE: only the fiber Sigma_{1,1} is a 2-manifold; tower=arithmetic family, "
            "fillings=scale family. None supplies the chiral datum; wall #4 stays blocked (B277).",
    "B293": "the clock = the peripheral symplectic pairing (Goldman {x,y}=2z-xy, kappa Casimir; = NZ frame). A "
            "filling = a Lagrangian/polarization. k(t) trajectory = STOP-GATE.",
    "B294": "the selection verdict: SELECTIVE for the object's own structure (B287), CATALOGUE for SM-values.",
    "B295": "the SSB/gauge status (Chat-2): Curie NOT a hard wall (SSB loophole), but the SSB potential ABSENT "
            "(wrong-tau/golden/cubic) and tau-gauged a stop-gate. Sign external, mechanism OPEN.",
    "B296": "Arc II verification: all probes SURVIVE adversarial red-team (0 refutations/leaks); classical math "
            "KNOWN/cited; novel connections flagged. Firewall-clean.",
}

# status codes: DISSOLVED | REDUCED | CHARACTERIZED | OPEN | QGAP  (+ seam delta)
WALLS = {
    1: dict(name="SL(2,C) holonomy vs compact E6", status="DISSOLVED",
            seam="unchanged. E6 flat connections exist unconditionally + witness (B274/B275)."),
    2: dict(name="McKay-E6 vs type selection (the CRUX)", status="REDUCED",
            seam="SHARPENED by B288: E6 (Q(sqrt-3)) is an OPEN-object property, LOST on closing -- no closing "
                 "arithmetically re-instantiates E6. The CRUX (input=output E6) stays the stop-gate; B288 leans it "
                 "CATALOGUE (the arithmetic lives in the open object, not the actualized closed manifold)."),
    3: dict(name="chirality / amphicheiral tau / CP sign", status="OPEN->MECHANISM-AT-SEAM",
            seam="RELOCATED by B286/B289/B295: closing breaks amphichirality with a FORCED sign LAW "
                 "(CS(p,-q)=-CS(p,q), all 78 closings; handedness = Q(sqrt-3) Galois = the +-pi/6 / tau swap). The "
                 "SIGN itself stays external (object CP-symmetric); the mechanism is OPEN -- NOT a Curie wall (SSB "
                 "loophole, B295), NOT established gauge (tau-gauged a stop-gate). Mechanism at the seam, sign free."),
    4: dict(name="3d (T[4_1]) vs 4d (SM) / multiplicity", status="CHARACTERIZED",
            seam="CLARIFIED by B292: multiplicity is TRIPARTITE (fiber surface / arithmetic tower / scale fillings); "
                 "only the fiber Sigma_{1,1} is a 2-manifold. The chiral datum is in none of them; wall #4 stays "
                 "blocked for B277's two named reasons. Chiral 4d SM = stop-gate."),
    5: dict(name="scale / DESI (topological Lambda)", status="QGAP",
            seam="GENERATED at the seam by B290/B291: the core-geodesic ladder ell_C~2pi/n (NZ) makes scale; a "
                 "min-volume closing exists (B291). But filling n =/= level k, the VALUE is gapped (122 orders), and "
                 "no closing is scale-distinguished toward an SM value. Mechanism at the seam, value HELD."),
}

# ---- the structural theorem, RELOCATED to the seam (B294) ----------------------------------------------------
STRUCTURAL_THEOREM = (
    "The object supplies a CANONICAL CLOSING and all the dimensionless STRUCTURE (the dynamics A=LR; the CP magnitude "
    "pi/6 + sign LAW; the scale ladder 2pi/n; the peripheral-symplectic clock); the ACTUALIZATION of a specific "
    "Standard-Model-valued world is NOT forced (which closing, which CP sign, the scale value, the chiral datum, and "
    "the trajectory are all external or gated). SELECTIVE for the object's own structure; CATALOGUE for SM-values."
)

# ---- the matter map (Sakharov-style, firewalled): 1 of 3 forced ----------------------------------------------
MATTER_MAP = {
    "CP_magnitude_pi_6": "BULK -- forced by the Q(sqrt-3) arithmetic (B285). [math, object-specific]",
    "CP_sign_exists": "SEAM -- forced to exist by the oriented closing, via the same Q(sqrt-3) involution (B289).",
    "which_CP_sign": "EXTERNAL -- object CP-symmetric; mechanism OPEN (B295: not Curie, not established gauge).",
    "baryon_magnitude": "EXTERNAL -- freeze-out / Sakharov out-of-equilibrium (S005, HELD).",
}

# ---- the CRUX (unchanged load-bearing conjecture), now informed by B288 --------------------------------------
CRUX = dict(name="input-E6 = output-E6",
            note="the 3d-3d/class-S INPUT type G is a free choice; the arithmetic fixes the OUTPUT (McKay-E6). "
                 "B288 sharpens: the E6-selecting arithmetic is an OPEN-object property, NOT re-instantiated by any "
                 "closing -- leaning CATALOGUE. Still a STOP-GATE (needs a T[4_1;E6] computation or a specialist).")

STOP_GATES = ["the chiral 4d-SM construction (B292/B277)", "the k(t) cosmological trajectory (B293)",
              "'tau is gauged' + dynamical gauge-fixing of the sign (B295)", "all value-matches (122-order gap)",
              "the CRUX (input=output E6)"]


def consistency():
    statuses = {WALLS[i]["status"] for i in WALLS}
    return (len(WALLS) == 5 and len(SEAM_ARC) == 11 and len(MATTER_MAP) == 4
            and statuses == {"DISSOLVED", "REDUCED", "OPEN->MECHANISM-AT-SEAM", "CHARACTERIZED", "QGAP"}
            and CRUX["name"] == "input-E6 = output-E6" and len(STOP_GATES) == 5)


if __name__ == "__main__":
    print("=== B297: the seam-arc wall map v4 (through B296) ===\n")
    print("Seam arc chain (11 banked results):")
    for k, v in SEAM_ARC.items():
        print(f"  {k}: {v}")
    print("\nFive walls THROUGH THE SEAM:")
    for i in WALLS:
        print(f"  #{i} [{WALLS[i]['status']}] {WALLS[i]['name']}\n       {WALLS[i]['seam']}")
    print(f"\nSTRUCTURAL THEOREM (relocated to the seam):\n  {STRUCTURAL_THEOREM}")
    print("\nMatter map (1 of 3 forced):")
    for k, v in MATTER_MAP.items():
        print(f"  {k}: {v}")
    print(f"\nCRUX: {CRUX['name']} -- {CRUX['note']}")
    print("\nstop-gates:", STOP_GATES)
    print("\nconsistency:", consistency())
    assert consistency()
