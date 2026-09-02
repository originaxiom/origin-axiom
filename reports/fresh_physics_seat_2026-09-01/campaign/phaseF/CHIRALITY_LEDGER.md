# Phase F — the chirality sweep: what the record did with orientation, and the seat's verdict

**Date:** 2026-09-02. **Owner's instruction:** "before you conclude the chirality verdict, please sweep the repo
because we dealt with it, and get the results." **Method:** 17 packets, 101 arcs (every arc on any head whose
name or FINDINGS mentions chirality / orientation / mirror / amphichirality / parity heavily) plus 7 top-level
documents (CLAIMS, TERMINOLOGY, RETRACTIONS, ERROR_LEDGER, LAW_MAP, THEOREM_LEDGER, VERDICT_LEDGER, THE_FORCED_AND_THE_FREE,
P000, P019), read by cheap sonnet agents into 147 structured rows (`results/chirality_sweep.tsv`, `results/DIGEST.md`).
Every row below was read by the seat; every judgment is the seat's. Owner rule 1 satisfied: the sweep came first.

## 1. The record's settled position (and the seat's independent check)

The record dealt with chirality thoroughly and, by August 2026, correctly. Its final position, in its own words:

| statement | where | status | seat check |
|---|---|---|---|
| m004 is amphichiral (Sym = D4, order 8, `is_amphicheiral()`; CS ≡ 0) | B128, B713, B1163, B1224, B1226 | STANDS, COMPUTED | R43/R50/R51/R54: reproduced |
| No object-canonical datum can orient m004: any automorphism-invariant datum is mirror-fixed (theorem) | B1163 addendum 2026-08-26 | STANDS | R54 §6 is the same theorem in the even/odd form |
| Parity law: object-canonical archimedean data are exactly the mirror-even dimensionless ones; orientation, CS sign, torsion sign are mirror-odd and observer-supplied | B1168 | STANDS (C6 completeness open) | R54 §6 |
| "Awareness = mirror-even; CHOICE = the mirror-odd orientation bit, observer-supplied" | B1169 | STANDS (core) | R54 §6, independently derived before reading B1169 |
| The mirror acts on traces as complex conjugation: mirror = c = generator of Gal(ℚ(√−3)/ℚ) | B1174, B8154, B1208, B289, B318 | STANDS, COMPUTED | R54 §4: 132 explicit word-pairs realise the conjugate character |
| The rule σ itself is orientation-reversing (det −1); its mapping torus is Gieseking; m004 is the double tick; orientability and amphichirality are bought together at tick two | B466, B467, B1083, B1234, P019 A6, THEOREM_LEDGER C5 | STANDS, COMPUTED | R54 §1–2: reproduced (m000 orientation cover ≅ m004; F commutes with A) |
| The founding rule a→ab, b→a is a basepoint on a free K4-torsor; swap = C-type bit, reversal = P-type bit; the arrow is monoid non-surjectivity, not a torsor bit | B1083, THE_FORCED_AND_THE_FREE §0 | STANDS, COMPUTED | R54 §3 (rule ~ mirror by SL(2,ℤ)); R54d (2-letter language reversal-closed; `bb` has no preimage is B1083's) |
| "Which chirality" is a free, transitive Galois ℤ/2 torsor with no fixed point: chirality is the observer's fiber-functor choice | B713 (verdict NEGATIVE on object-intrinsic chirality), B717, B994, B8114 | STANDS | agrees |
| Orientation is an AXIOM in the record's own chain (C5 "the most expensive fork"; C18 "the observer's closings") | THEOREM_LEDGER C5, C18; P019 A6 | STANDS | agrees; this is the honest form |
| Dehn filling supplies chirality only through the oriented slope; (p,−q) is the mirror; magnitude 5 forced, sign not | B286, B338, B432, B434, B944 | STANDS | the slope sign is the same bit (R54 §6) |
| The metallic family: amphichiral ⟺ block sequence is a cyclic palindrome (GHH 2008 corollary); chiral bundles need a non-palindromic gluing order, "a free choice" | B127, B128, B134, B136, B145, B146, B848, CLAIMS P34/P35 | STANDS, COMPUTED | agrees; classification, never a side |
| The ℤ/2's are distinct legs of one Galois V4: c (mirror, √−3), the √3 form-class swap, γ5 (√5, time/basepoint); B766's closing lattice has rank 3 {c, θ, γ5} | B1174, B1164, B766, B945 | STANDS, COMPUTED | R54e: Sym(m004)=D4 has exactly 4 linear characters (mirror × time-reversal) plus one doublet; θ is the SL/PSL lift sign, not a manifold symmetry |

**Seat verdict on the question "does anything derive an orientation from the rule?":** No, and the record already
proved it (B1163, B713, B1083). The seat's R54 reproduces the theorem independently and states the complete list of
tracker options (§3 below). This is not a defect of the program; it is its cleanest theorem.

## 2. Defects the sweep surfaced (seat judgments)

| # | defect | evidence | seat judgment | class |
|---|---|---|---|---|
| F1 | **B571's dossier and REPORT say "the object BREAKS c abundantly and computedly"** (B470 letter tower, B469 residue, B568 arrow, B565-H1 non-real traces) and STANDS unretracted; B572 says "σ IS a genuine, free, intrinsic orientation residue" | B571 CHIRALITY_DOSSIER.md:9-16, REPORT.md:112-119; B572 | Under B1163's theorem, "breaks c" means "has mirror-odd data", which every object with a non-real invariant has. The data are real; the SIGN is not the object's. B470's chiral members are covers/fillings (other manifolds), not m004; B565-H1's non-real trace is a mirror-odd datum with a chosen embedding. The wording contradicts the settled position and no scope note was propagated. | RETRACTION_NOT_PROPAGATED (scope) |
| F2 | **"σ̄ not conjugate to σ (exhaustive over 24 permutations)"** is cited as a computed time arrow (B532-I6 Probe 1, B571 item 5) | PROGRESS_LOG "B532-I6", B571 | The test is over letter permutations only; that is not a conjugacy test. The underlying fact is nevertheless true as a LANGUAGE arrow for the **4-letter** rule (R54d: 9 forbidden bigrams, no factor of length 2–10 has its reversal), and false for the owner's **2-letter** rule (R54d: reversal-closed at every length; R54c: reversal = inner conjugation by a⁻¹). B1083 relocates the 2-letter arrow to monoid non-surjectivity. The record should say which object the arrow belongs to. | CLAIM_EXCEEDS_COMPUTATION (test), object-conflation |
| F3 | **B1181/B1186 used the vacuous `is_isometric_to(reverse_orientation copy)` test** for the family-wide amphichirality closure, although B470 (July), B128, B1226 had documented its vacuity and named the valid test | B1181 verification/reproduce.sh; R51 | Regression against a known caveat; R51 shows 74 of the 112 family members are chiral. Already relayed (§1 of the relay). | RETRACTION_NOT_PROPAGATED (method) |
| F4 | **B723's chirality clause (Galois-sheet / β=1 SSB) is refuted by B942 and B957, but B723's arc_verdict still reads PROVED and LAW_MAP's B717 row still asserts the clause without a banner** | B1004 FINDINGS:29; B1040 ledger:25; LAW_MAP#B717 | The structure "measurement = fiber-functor choice" survives; the group identification does not. The verdict file and the LAW_MAP row need the banner. | RETRACTION_NOT_PROPAGATED |
| F5 | **B783 types the a↔b letter complement as γ5 (the √5 Galois bit)**; B1083 types the swap as the C-type (chirality) bit | B783 P16.2; B1083 §1 | R54 §3 and R54e: the swap J has det −1 and, composed with the SL(2,ℤ) re-basing P, commutes with A: it is an orientation-reversing symmetry of m004, i.e. the mirror c, not γ5. B1083 is right; B783's γ5 identification does not survive (letter frequencies 1/φ, 1/φ² are not exchanged by √5 ↦ −√5, which sends 1/φ to −φ). | CONTRADICTED (B783 sub-claim) |
| F6 | **B211 and B713 use `is_isometric_to(reverse_orientation)` as a corroborating witness** | B211, B713 probe3 | Both carry a valid witness alongside (CS = 0 to 1e−15; the Seifert-form anti-congruence). Not load-bearing. | OK (noted) |
| F7 | **RETRACTIONS.md has no chirality row** although B723's clauses were refuted and B132 withdrew its chirality-arithmetic reading in-arc | DOC:RETRACTIONS.md | The refutations live in later arcs and in-arc corrections only; the central ledger does not carry them. | RECORD |
| F8 | **B582 "the handedness of the meeting is set by the same two exponents that carry the object's own arrow"** | B582 FINDINGS:48-53 | Proves a chiral construction exists (two copies glued with a θ-odd twist); does not derive which of the slots {4,8}, i.e. which hand. The sentence reads as a derivation; the computation is an existence result. | CLAIM_EXCEEDS_COMPUTATION (wording) |
| F9 | **B321#2 "Im(w) > 0 selects the geometric structure over its mirror"** is cited as a chirality tracker | B321, B285/B318 | Im(w) > 0 is the choice of embedding ℚ(√−3) ↪ ℂ. It names the chosen bit; it does not derive it. Consistent with B1163 once read that way. | OK (scope) |

Counts: 147 rows; RULE_INTRINSIC 14 (all of them derive amphichirality, the det −1 of σ, or the P-type arrow, never a
side; the seat re-read each), OBSERVER_CHOICE 41, ARITHMETIC_GALOIS 17, GEOMETRY_CS_OR_TORSION 10, FILLING_SLOPE 6,
NONE_OBJECT_AMPHICHIRAL 23, UNSTATED 12, NOT_ABOUT_CHIRALITY 24. Status: RETRACTED 2, SUPERSEDED 4, REFUTED_BY_LATER 1,
OPEN 5, CANNOT_CHECK 1, STANDS 134. Valid amphichirality instruments in use: `symmetry_group().is_amphicheiral()`
(B128, B134, B136, B145, B713, B1224, B1226, B1163), Chern–Simons (B286, B432, B434, B470, B849, B755), the Seifert-form
anti-congruence (B713), the cusp-map determinant (B1226, B755, R54e). Vacuous instrument used load-bearingly: B1181, B1186 only.

## 3. What the sweep adds to the record's position (from R54, computed)

1. The rule's mirror image and the rule are conjugate by an orientation-preserving map (P = [[−2,−1],[−3,−2]]); reading
   direction is inner. The rule has no handedness of its own. (B1083 states this as the K4-torsor; R54 gives the conjugator.)
2. The complete list of sign-type tracker options is the character table of Sym(m004) = D4: four linear characters
   (mirror-parity × time-reversal-parity) and one doublet. Each odd factor costs one chosen bit; a doublet costs one
   labelling. B766's rank-3 lattice {c, θ, γ5} is this list plus the SL/PSL lift sign θ. Nothing else is possible.
3. The 2-letter rule has no language arrow (reversal-closed, Sturmian); the 4-letter rule has one. The record's arrow
   claims should name the object.

## 4. Verdict the owner asked for, in one paragraph

The record dealt with chirality and reached the right answer: the object is amphichiral, the mirror is complex
conjugation on ℚ(√−3), no object-canonical datum can orient it, and the orientation is a declared axiom (C5) or an
observer's closing (C18). The seat's independent computation (R54) reproduces every step and adds the exhaustive
list of tracker options. What remains defective is propagation: four places (B571/B572 wording, B723's verdict file and
the LAW_MAP row, B1181/B1186's instrument, B783's γ5 typing) still say something the settled position contradicts, and the
central RETRACTIONS ledger carries none of it. Those are edits for cc to make by hand; nothing here is banked by the seat.
