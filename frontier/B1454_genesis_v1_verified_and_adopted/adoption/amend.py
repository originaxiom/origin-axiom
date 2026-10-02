#!/usr/bin/env python3
"""B1454 -- GENESIS v1.0 (the SM seat's, as received) -> GENESIS v1.1 (main's), as a list of explicit changes.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.1 and differs from what this produces

Every change is one entry below: an exact string of v1.0 and what replaces it.  Each is asserted to occur exactly
once, so the script fails if the received text is not the text the changes were written against.  Lines that add
content are marked [v1.1] in the page; relabelling (sm: on the seat's arc numbers, "the SM seat" for "this seat")
is not marked line by line and is listed in the version log.
"""
import hashlib, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_0.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_0 = "13fb8daa11fcdfb9d6d19b3eeb3a403108ffd0aa489f3abd27be358681ae0ca7"
ARC = "frontier/B1454_genesis_v1_verified_and_adopted"

CHANGES = [
 # ---- header --------------------------------------------------------------------------------------------------
 ("**Version 1.0 · 2026-10-02 · arc B1516 · canonical.**",
  "**Version 1.1 · 2026-10-02 · canonical.** v1.0 is the SM seat's (its arc sm:B1516). v1.1 is main's verification and\n"
  "adoption of it (arc B1454): the same statement, the seat's arc numbers marked `sm:`, and main's amendments, each marked\n"
  "**[v1.1]** where it adds content. The version log (§10) lists every change; the v1.0 text as received is kept at\n"
  "`" + ARC + "/received/GENESIS_v1_0.md`."),
 ("- `philosophy/P000_what_is_not_nothing.md`, `philosophy/P019_the_genesis_axiom_chain.md` and\n  `philosophy/P022_the_generated_state_space.md`;",
  "- `philosophy/P000_what_is_not_nothing.md`, `philosophy/P019_the_genesis_axiom_chain.md` and the SM seat's P022, the\n"
  "  generated state space (on its branch; not on main);"),
 ("- `docs/THE_END_TO_END_CHAIN.md` and the README's state-of-the-programme section.",
  "- `docs/THE_END_TO_END_CHAIN.md` and the README's state-of-the-programme section;\n"
  "- **[v1.1]** Layer 0 of `docs/THE_FRAMEWORK.md` and the hypothesis line of `docs/THE_CLAIM.md` §1."),
 ("is this seat's proposal and waits for the owner's\nconfirmation. Everything else here restates the record as it stands, checked by B1516's own code\n"
  "(`frontier/B1516_genesis_v1/verification/foundations_checks.py`).",
  "is the SM seat's proposal and waits for the owner's\nconfirmation. Everything else here restates the record as it stands, checked by the SM seat's own code (sm:B1516)\n"
  "and re-derived on main by other routes (B1454, `" + ARC + "/verification/genesis_own.py`)."),
 # ---- section 0 -----------------------------------------------------------------------------------------------
 ("  Nothing in a later section is used to justify an earlier one.",
  "  Nothing in a later section is used to justify an earlier one.\n"
  "- **[v1.1] Whose number is whose.** `sm:B…` is an arc of the SM seat (its ranges are B1350–B1399 and B1500–B1599). A\n"
  "  B-number that is bare or written \"main B…\" is main's, and so is every B-number below B1278. R-numbers and F01 are\n"
  "  the audit lane's.\n"
  "- **[v1.1] Before saying the record lacks something** that bears on an item here, sweep it:\n"
  "  `scripts/checks/topic_sweep.py`, and for B1–B500 `docs/EARLY_RECORD_INDEX.md`, whose verdict lines predate today's\n"
  "  vocabulary (WORKING_RULES, the rule of 2026-10-02)."),
 # ---- section 1 -----------------------------------------------------------------------------------------------
 ("  unique seed \"would be the suspicious outcome\", and that the member is contingent. P019's \"to a unique object\" departed\n"
  "  from this, and P022 corrected it on 2026-09-27. The generated state space (§3) is P000's stance made precise, not a\n"
  "  retreat from it.",
  "  unique seed \"would be the suspicious outcome\", and that the member is contingent. P019's \"to a unique object\" departed\n"
  "  from this, and P022 corrected it on 2026-09-27. The generated state space (§3) is P000's stance made precise, not a\n"
  "  retreat from it.\n"
  "- **[v1.1] PF1 has a mathematical form in the record, and it is a reading, not a derivation.**\n"
  "  `philosophy/P008_non_cancellation_is_fricke_vogt.md` (motivation, never a premise) names it: non-cancellation is\n"
  "  κ = tr[a, b] ≠ 2 for the two letters, the Fricke–Vogt invariant, with κ = 2 the locus where the cancellation\n"
  "  completes. The mathematics it points at is banked: κ = 4·I_FV + 2 (B148); κ = 2 is codimension one, spectrally\n"
  "  trivial and the one fibre with positive-measure spectrum (B161, B162); four banked faces are one commutator trace\n"
  "  (B309, B518). **κ names two quantities** (ERROR_LEDGER E72): the fibre's commutator trace, −2 at the root, which is\n"
  "  the parabolic cusp and Minsky's punctured-torus condition (B160, B1404); and the knot group's meridian commutator\n"
  "  trace, with κ − 2 = ω² (B285, B309). Every use says which."),
 # ---- section 2 -----------------------------------------------------------------------------------------------
 ("Fork F9 is robust to word length three and fragile at four (main B749 addendum). |",
  "Fork F9 is robust to word length three and fragile at four (main B749 addendum; computed in B1323, corrected at B1414). |"),
 ("so faithful word realisation and the surface category stay premises. B749 F8: the anatomy needs geometry. |",
  "so faithful word realisation and the surface category stay premises. B749 F8: the anatomy needs geometry. **[v1.1]** "
  "Main has not verified sm:B1380 (its lead L239 (a)). A sweep of main's verdict lines (B1454) found no arc that derives "
  "the faithful F₂ carrier or the surface category from a weaker premise; B749 F8 and B1003 compute what is lost without "
  "the carrier, which is a different thing. |"),
 ("whose squares are the word states LᵐRᵐ (B1516 C10). |",
  "whose squares are the word states LᵐRᵐ (B1516 C10). **[v1.1]** Main's early record on the swap: ±LP are the only square "
  "roots of LR in GL(2,ℤ), and LₐR_b has an orientation-reversing integer square root exactly when a = b (B14; re-derived, "
  "B1454 G11); P is the unique primitive-pair exchange involution up to sign, forced by (LX)² = LR and not by the "
  "substrate axioms (B16, B19); every metallic bundle double-covers a non-orientable one (B469); the founding torsor's "
  "two bits are the swap and the reversal (B1083). |"),
 # ---- section 3 -----------------------------------------------------------------------------------------------
 ("polynomial τ² − τ − 1 of LR against τ² + τ − 1 of RL (B1516 C3).",
  "polynomial τ² − τ − 1 of LR against τ² + τ − 1 of RL (B1516 C3). **[v1.1]** B979: at the based level the bit is\n"
  "load-bearing and it is one bit — it is where φ enters rather than −φ or φ². B1323: it is the placement of the swap\n"
  "inside the tick, (LP)² = LR against (PL)² = RL."),
 # ---- section 4 -----------------------------------------------------------------------------------------------
 ("Minimality points the other way: m000 has half the volume and one tetrahedron (B1380; B749 F5 FRAGILE, \"the parent\"). The most fragile link of the chain (fork FK2). |",
  "Minimality points the other way: m000 has half the volume and one tetrahedron (B1380; B749 F5 FRAGILE, \"the parent\"). The most fragile link of the chain (fork FK2). "
  "**[v1.1]** What the choice costs is computed (B1234): eight banked walls — no dimensionful quantity, CS = 0, chirality "
  "not self-supplied, the CP sign external among them — pass through amphichirality, which an orientation double cover "
  "has by construction (40 of 40 census double covers, against 6 of 200 one-cusped orientable manifolds); and the "
  "arithmetic route to E₆ does not need the squaring, since π₁(m000) has the same 48 surjections onto 2T. What dropping "
  "SE2 would break is not computed. B1003 locks the prices of all seven forks. |"),
 ("  golden matrix LP on the once-punctured torus, whose bundle is m000 → its square LR by orientation (SE2). Main splits T4\n  into a theorem and a criterion (its C2a and C2b).",
  "  golden matrix LP on the once-punctured torus, whose bundle is m000 → its square LR by orientation (SE2). Main splits T4\n  into a theorem and a criterion (its C2a and C2b; B1323)."),
 ("  more selector of it, and, like the others, a chosen one.",
  "  more selector of it, and, like the others, a chosen one. **[v1.1]** The others in the record: the systole (B92), the\n"
  "  volume minimum among torsion-free positive words (B197), the unique unitary anyon and the unique superconformal\n"
  "  chain (B218, B224, B228), the only knot complement of the family (B251: H₁(M_m) = ℤ ⊕ (ℤ/m)²). They do not all\n"
  "  agree: arithmeticity keeps m = 1 and m = 2 (B125). B1323's census: seven self-application criteria pick φ, and the\n"
  "  smallest Pisot number of any degree is not φ."),
 ("- None of the routes derives its axioms from anything weaker (UNIQUENESS §6; main B1422).",
  "- None of the routes derives its axioms from anything weaker (UNIQUENESS §6; main B1422).\n"
  "- **[v1.1] The words route and the records route are one construction in two presentations**, not two derivations\n"
  "  (B1323, machine-checked: the Sturmian morphisms abelianise onto exactly the non-negative GL(2,ℤ) matrices; ledger\n"
  "  C1 ↔ UNIQUENESS A2 + A4, C5 ≡ A3, C4 ↔ A1)."),
 ("*\"The root has none and cannot, since its fibre has no finite character\"* (main B1434).",
  "*\"The root has none and cannot: its fibre has no finite character.\"* (main B1434)."),
 # ---- section 5 -----------------------------------------------------------------------------------------------
 ("to physics (identification I-26) is UNEARNED.** Each is a named hypothesis.",
  "to physics (identification I-26) is UNEARNED.** Each is a named hypothesis. **[v1.1]** F-MC is main's oldest frame and\n"
  "is of a different kind: it goes from the root's arithmetic to a gauge algebra, not from flat bundles to counts."),
 ("| F-CI | Class-index frame | main's index I = n(V) − n(V*) on reducible non-split doublet modules in the E₆/27 frame; generation-shaped backgrounds | main, B1297 and B1418–B1451; verified here (sm:B1374, sm:B1375) |",
  "| F-CI | Class-index frame | main's index I = n(V) − n(V*) on reducible non-split doublet modules in the E₆/27 frame; generation-shaped backgrounds | main, B1297 and B1418–B1451; verified on the SM seat's branch (sm:B1374, sm:B1375) |\n"
  "| F-MC **[v1.1]** | McKay cascade frame | the root's trace field ℚ(√−3) has one ramified prime, which gives π₁ → 2T; McKay gives E₆; the fused cascade ends at su(3) ⊕ su(2) ⊕ u(1)³, with the global form [SU(3)×SU(2)×U(1)]/ℤ₆ and the hypercharge direction | main: B248, B266, B862–B864, B892, B992–B994; one theorem with its counted hypotheses in `docs/THE_CLAIM.md` §1 (B1014) |"),
 ("**A result is a statement\nabout a frame applied to an object, never about the architecture as such.**",
  "**A result is a statement\nabout a frame applied to an object, never about the architecture as such.**\n\n"
  "**[v1.1] F-MC by object.** Run on the root only. Reaching E₆ is generic — about one manifold in three, five of seven\n"
  "grammars (B993, B996) — while the golden is the unique metallic grammar whose own-conductor shadow is a McKay group\n"
  "(B997, B1002); m004's siblings have no door (B1019); m000 has the same door (B1234). Its inputs beyond the root are\n"
  "counted: five typed external data in `docs/THE_CLAIM.md` §1 (B1014, B1017), eleven irreducible identifications\n"
  "(B1266), 39 of 43 ledger links forced (B1123), the freedom ledger (B1028). Never computed on another word state."),
 # ---- section 6 -----------------------------------------------------------------------------------------------
 ("The tag lives in `arc_verdict.json` (field `scope`) and in each kill-graph entry (field `scope`). From B1516 on,\n"
  "`tests/test_arc_verdict_schema.py` requires it of every new arc, and `tests/test_b1516_genesis_v1.py` requires it of every\n"
  "kill-graph entry this seat wrote from B1369 on. A negative blocks only where its tag reaches (WORKING_RULES, the amended\n"
  "mandate of 2026-10-01).",
  "The tag lives in an arc's verdict file (field `scope`) and in each kill-graph entry (field `scope`). **On main**, from\n"
  "B1454 on, `tests/test_arc_verdict_schema.py` requires it of every new arc and of every new kill-graph entry. **On the\n"
  "SM seat's branch**, its schema test requires it from sm:B1516 on, and every kill-graph entry it wrote from sm:B1369 on\n"
  "carries one. A negative blocks only where its tag reaches (WORKING_RULES on main, the rule of 2026-10-02 on scope;\n"
  "the SM seat's amended mandate of 2026-10-01)."),
 # ---- section 7 -----------------------------------------------------------------------------------------------
 ("- **GAP5, dynamics.** Topology yields integers and discrete structure. The 19 values need moduli, symmetry breaking and\n  running, which the architecture does not have.",
  "- **GAP5, dynamics.** Topology yields integers and discrete structure. The 19 values need moduli, symmetry breaking and\n"
  "  running, which no frame has produced. **[v1.1]** v1.0 said the architecture \"does not have\" them; as a statement\n"
  "  about the record that is too strong. Main's sweep of dynamics and chirality concluded that neither is missing as\n"
  "  structure (B944): a monodromy-preserving flow and a positive-entropy Painlevé VI solution (B169, B317), the root's\n"
  "  own gravitational action with no free dimensionless constant (B1088), an action that exists exactly at the\n"
  "  monodromy (B1341), a native gauge system (B715) — and no intrinsic time (B721). The gap is the narrower one: none\n"
  "  of it has been turned into a potential, a breaking or a running that fixes a value."),
 # ---- section 8 -----------------------------------------------------------------------------------------------
 ("- the genesis paths of `paths/PATHS.md` never touched: 18 of 25 at main's B1422.",
  "- the genesis paths of `paths/PATHS.md` never touched: 18 of 25 at main's B1422 (**[v1.1]** counted again at B1454:\n"
  "  of the 25 enumerated paths 1 is dead, 3 are stalled, 3 are in progress and 18 are untouched; E21, a stalled\n"
  "  instantiation of a listed mechanism, is the registry's 26th row);\n"
  "- **[v1.1]** F-MC on any state other than the root."),
 # ---- section 9 -----------------------------------------------------------------------------------------------
 ("| the X_gen convention | B1384; P022 | §3 |",
  "| the X_gen convention | B1384; P022 | §3 |\n"
  "| **[v1.1]** \"the four letters are the axioms\" (aAbB = A1–A4); the bridge equation κ = tr[a, b] | `docs/THE_FRAMEWORK.md` Layer 0; B309, B518; P008 | GM1, GM5a, SE2 and GM2 in that order; PF1's mathematical form (§1) |\n"
  "| **[v1.1]** \"the six axioms A1–A6 and one bit A7\" plus five typed external data | `docs/THE_CLAIM.md` §1 | the records route (§4) and F-MC's hypotheses (§5) |\n"
  "| **[v1.1]** C18, the observer's closings | THEOREM_LEDGER | not part of the genesis: an input of F-MC (§5) |"),
 # ---- section 10 ----------------------------------------------------------------------------------------------
 ("  - The principle's single wording is proposed and awaits the owner (FK1).",
  "  - The principle's single wording is proposed and awaits the owner (FK1).\n"
  "- **v1.1 · 2026-10-02 · main B1454.** Verified and adopted on main.\n"
  "  - Verification: v1.0's ten checks re-derived with main's own code by other routes (continued fractions and a\n"
  "    linear-algebra conjugator in place of a box search; Burnside's count against the enumeration; cyclic covers in\n"
  "    place of bundle codes), all agreeing; every citation of a main record checked against that record.\n"
  "  - Relabelled, not changed: the SM seat's arc numbers carry `sm:`; its first-person references to itself and to its\n"
  "    branch now name the SM seat; paths that exist only on that branch are named as such.\n"
  "  - Added (marked [v1.1]): PF1's mathematical form and the two quantities called κ (§1); main's early record on the\n"
  "    swap at GM5c, and that sm:B1380 is unverified on main at GM4 (§2); B979 and B1323 on the order bit (§3); the cost\n"
  "    of SE2 from B1234, the other selectors of m = 1, and the two routes as one construction (§4); **the frame F-MC**,\n"
  "    main's McKay cascade, with its counted inputs (§5); the scope tag's enforcement on main (§6); the path-registry\n"
  "    count and F-MC's frontier (§8); three crosswalk rows (§9).\n"
  "  - Corrected: the quotation of B1434 (§4), which v1.0 gave with a word changed; GAP5's \"does not have\", an absence\n"
  "    the record contradicts (§7).\n"
  "  - Unchanged and still the owner's: FK1."),
]

RELABEL = [  # applied after CHANGES, in order; the count of each is asserted
 ("this seat's older Yₙ", "the SM seat's older Yₙ", 1),
 ("| this branch, B1368–B1399 |", "| the SM seat's branch, B1368–B1399 |", 1),
 ("| this branch, B1509–B1515; the audit lane, R40–R76 |", "| the SM seat's branch, B1509–B1515; the audit lane, R40–R76 |", 1),
 ("| this branch, B1355–B1365 and B1500–B1505 |", "| the SM seat's branch, B1355–B1365 and B1500–B1505 |", 1),
 ("reproducing this seat's level census", "reproducing the SM seat's level census", 1),
]


def build():
    raw = open(SRC, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SHA_V1_0, "the received v1.0 is not the text these changes were written against"
    t = raw.decode("utf-8")
    for old, new in CHANGES:
        assert t.count(old) == 1, ("not found exactly once", old[:90], t.count(old))
        t = t.replace(old, new)
    for old, new, n in RELABEL:
        assert t.count(old) == n, (old, t.count(old))
        t = t.replace(old, new)
    t, k = re.subn(r"(?<![:\w])B(13[5-9]\d|15\d\d)\b", r"sm:B\1", t)
    assert "this seat" not in t and "this branch" not in t and "verified here" not in t
    return t, k


def main(argv):
    t, k = build()
    if "--check" in argv:
        cur = open(OUT).read() if os.path.exists(OUT) else ""
        if "**Version 1.1 ·" in cur and cur != t:
            print("GENESIS.md is at v1.1 and differs from amend.py's output"); return 1
        print("VERDICT genesis-amend: PASS (%d changes, %d relabels, %d arc numbers marked sm:)" % (len(CHANGES), len(RELABEL), k)); return 0
    open(OUT, "w").write(t)
    print("wrote GENESIS.md v1.1: %d changes, %d relabels, %d arc numbers marked sm:" % (len(CHANGES), len(RELABEL), k))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
