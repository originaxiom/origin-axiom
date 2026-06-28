"""B272 -- adversarial verification pass over the E6-bridge arc (B262-B271): what survived, what was corrected,
and the EXTENDED gap map (the walls the 5-wall map was missing). FIREWALLED. Nothing to CLAIMS.md.

Two independent audit agents + orthogonal hand-checks re-derived the riskiest claims from scratch (motivated by the
earlier Sym-convention bug that produced a clean-looking WRONG answer). Core math survived; framing had three
overclaims (now corrected in the respective FINDINGS); and the 5-wall map was missing several real walls.
"""

# ---- what survived independent re-derivation (method != the banked code) -------------------------------------
CONFIRMED = {
    "dim H^1(Sym^2k)=1 all k": "3 independent methods: exact Q(sqrt-3) arithmetic, mod-p Fox over large primes "
                               "p in {61,103,9973,99991}, + convention re-validated. Matches Thurston (k=1) & MFP.",
    "fig-8 group ->> SL(2,F_3)=2T": "GAP StructureDescription = SL(2,3), order 24; omega->1, t->2 mod (sqrt-3) "
                                    "re-derived; b^2 + a are the standard transvections.",
    "binary-polyhedral only q in {3,5}": "by isomorphism to the SU(2) finite-subgroup list + Frobenius-Schur "
                                         "indicators (faithful quaternionic 2-dim irrep only at q=3:2T, q=5:2I).",
    "E6-Zariski-density of {4,8}": "Sage re-run: <prin sl2, exp 4/8>=78=e6; exp 5/7/11 ->52=f4. Dynkin fact correct.",
    "tau-fixed = TYPE F4, tau OUTER": "rank 4 + dim 52 + semisimple (Killing nondeg) => uniquely F4; diagram "
                                      "automorphism (1 6)(3 5) has Cartan signature (+1)^4(-1)^2 => outer (EIV).",
    "cup-product check non-vacuous": "rank d^1 = 2 < 3 (H^2 1-dim, proper im); Q(xi) != 0; Q(xi) in im d^1 is a "
                                     "real vanishing (a random vector is not).",
    "Vol(4_1)=2.0298832, shapes e^{i pi/3}": "SnapPy volume() = 2.02988321281931; both ideal tetrahedra z=e^{i pi/3}.",
    "tau-broken = E6-density (exact)": "at the tangent level: a deformation generates e6 iff it has a {4,8} "
                                       "component iff it breaks tau. Exact identification, not loose.",
}

# ---- overclaims found, and the correction applied (to each FINDINGS) -----------------------------------------
CORRECTIONS = {
    "B265 'E6-irreducible connections EXIST'": "SOFTENED -> 'expected to exist'. Solid: dim H^1=6=rank + "
        "Zariski-density. NOT proven: integrability of the {4,8} directions (the e6 bracket-coupled cup product "
        "H^1 x H^1 -> H^2(e6) is uncomputed; B270 did only the SL(2)/exponent-1 block). MFP is the dim count, not "
        "an E6 smoothness theorem. Residual open item: the {4,8} obstruction.",
    "B267 'five independent invariants => one E6'": "REFRAMED -> a consistency check. The geometric side is E6 by "
        "construction; once the arithmetic side is E6, h/dim/exponent-sum/Molien agree automatically. Genuine "
        "content = exactly 2 facts: arithmetic INDEPENDENTLY lands on E6, and its exponent set matches B264's "
        "grading. (e6_coherence.py hard-codes the E6 Dynkin; the real McKay(2T) derivation is in B266.)",
    "B266 'only q in {3,5}' justification": "FIXED -> the stated reason skipped q=4 (=A5, the icosahedral near-miss "
        "to 2I=SL(2,5)). Correct exclusions: q=2 (S3), q=4 (A5, trivial center), q>=7 (too large). Decisive "
        "criterion = faithful quaternionic irrep, not the center test alone. Conclusion unchanged.",
}

# ---- the EXTENDED gap map: walls the 5-wall map (B259/B268) did NOT contain ----------------------------------
# kind: CRUX (load-bearing single point) | WALL (real obstruction, absent from the map) | ASSUMPTION (free choice)
GAPS = {
    "input-E6 = output-E6": dict(kind="CRUX", in_5wall="wall #2 (reduced)",
        note="THE load-bearing conjecture. The 3d-3d correspondence's TYPE G is a FREE CHOICE; nothing forces it "
             "to equal the arithmetic McKay-E6 (B266). B268's 'REDUCED, no math obstruction left' understates how "
             "much hangs on this single unproven coincidence. The entire bridge rests here."),
    "family replication (3 generations)": dict(kind="WALL", in_5wall="ABSENT",
        note="SM has 3 chiral families = 3x27; one figure-eight gives one character variety. Deflated ELSEWHERE "
             "(B257: the Z/3 is the Eisenstein cube-root / cone order, NOT 3 generations; B254 dead) but NO wall "
             "for it appears in the 5-wall map. A reader of B268-B271 would not see this obstruction."),
    "SM matter content / E6->SM breaking": dict(kind="WALL", in_5wall="ABSENT",
        note="27 -> one SU(5) generation is GENERIC E6, not object-specific (B252/B254); B207 = a NEGATIVE for a "
             "GUT breaking chain; B247 only generic centralizers. Disposal of exotics, hypercharge, the breaking "
             "chain: unaddressed and absent from the map."),
    "cosmological-constant SIGN": dict(kind="WALL", in_5wall="wall #5 is magnitude-only",
        note="figure-eight is hyperbolic => Lambda<0 / AdS (B259 STONE 1: Lambda=-1); observed dark energy is "
             "Lambda>0 / dS. The SIGN mismatch is SEPARATE from the 122-order magnitude gap and is flagged only in "
             "speculations/ (S042/S043), invisible in the wall map. All the E6 structure lives on the Lambda<0 end."),
    "principal sl(2)->E6 embedding": dict(kind="ASSUMPTION", in_5wall="implicit in B264",
        note="the 'E6 character variety' (B264) is deformations of the principal-COMPOSED geometric rep; the "
             "principal embedding is an input, not forced by the geometry. A free choice, disclosed as a "
             "construction but not flagged as a choice."),
    "no dynamics / vacuum selection": dict(kind="ASSUMPTION", in_5wall="walls #3/#5",
        note="even granting chirality=E6-density (B271), the object supplies the LOCUS, not the VACUUM; chirality "
             "stays undetermined; no scale (G, Lambda magnitude, masses); CP-symmetric (no CP phase, B252)."),
}


if __name__ == "__main__":
    print("=== B272: adversarial verification pass over B262-B271 ===\n")
    print(f"CONFIRMED (independently re-derived): {len(CONFIRMED)}")
    for k in CONFIRMED:
        print(f"  [OK] {k}")
    print(f"\nCORRECTIONS applied to banked FINDINGS: {len(CORRECTIONS)}")
    for k, v in CORRECTIONS.items():
        print(f"  [FIX] {k}\n        {v[:96]}...")
    print(f"\nEXTENDED GAP MAP (beyond the 5 walls): {len(GAPS)} items")
    for k, g in GAPS.items():
        print(f"  [{g['kind']:<10}] {k}  (5-wall: {g['in_5wall']})")

    crux = [k for k, g in GAPS.items() if g["kind"] == "CRUX"]
    absent = [k for k, g in GAPS.items() if g["in_5wall"] == "ABSENT"]
    print(f"\n  load-bearing CRUX: {crux}")
    print(f"  real walls ABSENT from the 5-wall map: {absent}")
    assert crux == ["input-E6 = output-E6"]
    assert set(absent) == {"family replication (3 generations)", "SM matter content / E6->SM breaking"}
    assert len(CONFIRMED) == 8 and len(CORRECTIONS) == 3
    print("\n  => core math survived; 3 framing overclaims corrected; 2 real walls + the Lambda-sign were missing")
    print("     from the map; the bridge's single load-bearing point is input-E6 = output-E6. PASS")
