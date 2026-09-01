# VERIFICATION — T8b (T8_terminality_draft/DRAFT.md)

**Verifier seat:** adversarial verification, 2026-09-01.
**Claimed:** DRAFT-COMPLETE.
**Verdict: DEGRADED** — one substantive finding (the theorem's part (ii) quantifier is silently
widened beyond what B994 computed, and the draft's own §1 menu definition makes two of its §2(ii)
statements false as written), against an otherwise clean transcription. Details, then the minor
notes, then what passed.

Sources checked line-by-line: `frontier/B863_termination/FINDINGS.md`,
`frontier/B994_rule_variation/FINDINGS.md`, `frontier/B861_fused_cascade/FINDINGS.md`,
`frontier/B873_p5_gate/FINDINGS.md` (incl. addendum), `campaign/T4_prior_art/FINDINGS.md`,
`papers/P3_THE_PAPER/main.tex` (falsifiers section).

---

## FINDING 1 (substantive): part (ii) is stronger than B994, and internally inconsistent with §1's own menu definition — the su(3)⊕g₂ gap

This is the one place the draft strengthens a banked arc, and it does so through the definitional
envelope rather than through any changed number.

**The chain of facts:**

1. Draft §1 defines the step menu as the maximal reductive subalgebras "comprising the regular
   maximal subalgebras ... **and the special (S-)subalgebras that pass the exact central-charge
   match**." So on the draft's own definition, the E₆ menu **contains** the registerable special
   candidates, in particular su(3)⊕g₂.
2. B873 §2.5 (the P5 gate) establishes that on the completed menus every conformal special
   completion at step 1 is killed by −1∈W **except su(3)⊕g₂ — "registerable but dim 22 < 46:
   cannot win."** That "cannot win" is a statement under the *dimension-maximal* ranking only.
3. B994 — the sole source for the six-chain enumeration — computes, per its own P0 header,
   **over B861's menus**, whose step-1 row is exactly the four options SO(10)×U(1) / SU(6)×SU(2) /
   Sp(8) / SU(3)³. su(3)⊕g₂ is not in B861's menu and no banked arc computes its descent.
4. Draft §2(ii) then asserts: "*Enumerating EVERY registerable-respecting selection function
   yields exactly six reachable chains, and all six end at the Standard Model.*" And draft §1
   defines a registerable-respecting selection function as **any** map choosing a registerable
   option from **the menu** (the §1 menu, which includes the specials).

**Failure as written:** on the draft's own definitions, a selection function that picks the
registerable option su(3)⊕g₂ at step 1 is registerable-respecting. Its chain is not among the six;
its continuation is computed nowhere in the banked corpus; its endpoint is unknown. "Exactly six"
and "all ... end at the Standard Model" therefore do not follow from B994 on the poset the draft
defines. This is precisely the "strengthening a banked arc" failure mode the verification was asked
to hunt.

**The draft's own patch fails.** §1's parenthetical — su(3)⊕g₂ "cannot win under any
dimension-monotone rule" — (a) does not cover the theorem's quantifier, which is *all*
registerable-respecting selection functions, not dimension-monotone ones (the draft itself lists
"first-listed" and "last-listed," which are not dimension-monotone); and (b) is **false for
min-dim** on the draft's own menu: minimal dimension prefers su(3)⊕g₂ (dim 22) over SU(3)³
(dim 24), so §2(ii)'s claim that "the four named rules — maximal dimension, minimal dimension,
first-listed, last-listed — split into two distinct chains" is also false as written (B994's
min-dim → SU(3)³ result holds only on B861's special-free menu). Two further internal
inconsistencies follow: the [3, 2, 1] options-per-step count and the step-1 "3 of 4" are counts
over the four regular options, not over the §1 menu (on which the step-1 registerable count is 4,
including su(3)⊕g₂). Steps 2–3 are unaffected: B873 §2.5 kills every special at the SO(10)/SU(5)
levels by −1∈W, so [·, 2, 1] survives menu completion; only step 1 has the gap.

**Why DEGRADED and not REFUTED:** the underlying banked mathematics is transcribed correctly, and
the repair is narrow and purely editorial — either (i) define the theorem's menus as exactly the
regular rows B994 computed over and move the specials (su(3)⊕g₂ included) into Fence F1 as part of
the certified-menu import with an explicit restriction of the quantifier, or (ii) have the owner
compute su(3)⊕g₂'s descent and close the gap outright (B873 gives its 27-branching machinery;
this is plausibly a short computation, but it is **not banked** and the draft may not assume its
outcome). Option (i) is the faithful-to-sources fix. As it stands, the section's central novelty
claim — rule-independence over *every* selection function — is stated on a poset for which it has
not been proven.

## Minor notes (no verdict weight individually)

- **M1.** §1's menu definition says specials must "admit a level-1 conformal embedding" /
  "pass the exact central-charge match," yet the SU(3)₉ row discussed in the same sentence is a
  level-**9** embedding (B873 addendum: forced level 9, ΣT = 27). The definition should say the
  c-match at the embedding's forced level, or drop "level-1" from the special clause.
- **M2.** Sp(8) (an S-subalgebra of E₆, per B873's special-candidate list) is presented in §1's
  main regular-looking row rather than with the specials. This follows B861's presentation, so it
  is not a source deviation, but it muddies the very regular/special boundary that Finding 1 turns
  on.
- **M3.** Theorem (i)'s word "Exhaustively" (over structural descents + the conformal case) is
  carried from B863 §2, and B863's §5 non-exhaustiveness fence over exotic conformal embeddings
  IS quoted verbatim in §5 F1 — acceptable, but the theorem statement and its fence are three
  sections apart; a referee will want a pointer from (i) to F1 in the theorem text itself.
- **M4.** The tumbling quote in §3 drops T4's editorial bracket "[i.e. vector-like]" — correct
  handling (the bracket was T4's gloss, not Raby–Dimopoulos–Susskind's text).

## What was attacked and PASSED

**(1) Trace to banked arcs without strengthening — passes everywhere except Finding 1.**
Verified against sources: the four dims 46/38/36/24 and 25/21 and 16/12 (B861 §2); the Sp(8) kill
wording "traceless Λ²(8) of C₄, self-dual" (B861 §2, B994 step 1); the SU(4)⊕u(1) step-3 kill
(B861/B994); the SU(3)₉ forced (2,2) self-conjugate branching, dying "by the gate itself"
(B873 addendum — draft says "fails the criterion outright," faithful); B863's four-row halt table
carried row-for-row including {3: 2, 3̄: 2, 1: 3}, "all su(2)-pseudoreal," full abelianization,
and the positive control; the (b′) conformal row's arithmetic (principal embedding, index 4,
c = 3·4/6 = 2 = c(su(3)₁) — checks: B863 writes 12/6 = 2, identical); "the (3,2) is the last
unpaired complex structure" and "chirality has nowhere smaller to live" (B863 §2 blockquote);
the six chains verbatim (B994); max-dim/first-listed vs min-dim/last-listed pairing (B994 —
correct *on B994's menu*, see Finding 1); the kind-check framed as "consistency check, not input"
(B863 §3); §4's "REPRODUCED, not DISCOVERED" grading (B994's own grade, if anything weakened —
correct direction); §6's falsifier matching P3 main.tex falsifier 4 verbatim in substance, with
the executable-test sentence flagged as an addition in the drafting notes.

**(2) Survival-hypothesis attribution — complete and prominent.** The disclosure is a bolded,
titled block ("**Disclosure: the criterion is not ours**") inside §1, before the theorem, not an
afterthought; all five citations present (Georgi B156 1979; Barbieri–Nanopoulos 91B 1980;
Georgi–Glashow D6 1972; Slansky 1981; Fonseca B897 2015) and each matches T4's bibliographic data.
The claim boundary is drawn in the same paragraph ("What is claimed as new here is *not the
criterion*"), and §3 repeats it. The draft does not read as claiming the criterion. PASS.

**(3) Fonseca delta — referee-checkable.** Both verbatim quotes match T4's full-text-verified
quotes character-for-character in substance (12 embeddings, 5 chiral pairs, unique chiral
solution = 3×27); the upward/downward direction split is stated exactly as T4 priced it; the
concession that a specialist could assemble much of (ii) from Fonseca's tables is carried, not
buried; the bounded-search caveat (16 queries, 4 full texts, paywalled primaries) is in the status
header AND restated as "not found within that bound" — matches T4's bound verbatim. The tumbling
adjacency is priced with the same three distinguishing clauses T4 used. PASS — with the caveat
that Finding 1 slightly changes what the delta's item 2 may claim (the rule-space enumeration is
over the regular menus, and should say so).

**(4) Fences carried, not footnoted.** F1 and F2 are a full numbered section (§5) of the draft
paper section itself, not front-matter or footnotes; all five verbatim quotes verified against
B861 §4, B994 Scope, B863 §5, and B994 "THE LIMIT" (B713/B760 as quoted there, including the
headline "The endpoint is forced by an input the object does not have"); §6 even routes the
menu-attack reader back to F1. F1's deliberate understatement relative to B873's citation-free
self-verification is real and safe (understates, never overstates). The double-conditional closing
of F2 is B994's honest statement, faithfully carried. PASS.

**(5) Gate 5 — clean.** Scanned every numeral in the draft section: all are dimensions, ranks,
Dynkin indices, central charges, multiset counts, or bibliographic data. No coupling, mass, angle,
scale, or measured value appears. The one measured-adjacent count in the sources (the "19
dimensionless numbers") was deliberately rendered numberless in §4, exactly as the drafting notes
declare. The drafting notes (outside the section) mention "19" — the header's Gate 5 claim is
scoped to "the section below," so this is consistent, and 19 is a count, not a measurement,
regardless. PASS.

**Drafting-notes audit:** all three declared deviations check out as described; the per-clause
source map is accurate where spot-checked (every clause I traced landed where the map said).
The notes' referee-prediction paragraph does NOT list Finding 1, which is itself evidence the
widening was inadvertent.

---

## Verdict

**DEGRADED.** The draft is a faithful, well-fenced, Gate-5-clean transcription on four of the five
attack axes, but its central theorem's part (ii) quantifies over a poset (specials included) on
which the banked arc (B994, computed over B861's special-free menus) does not license it, its
own §1 registerable special su(3)⊕g₂ is a live counterexample-candidate no banked arc disposes of
below the ranking assumption, and two subsidiary §2(ii) statements (the min-dim chain; "3 of 4")
are false on the draft's own definitions. One narrow editorial repair (restrict the theorem's
menus to the regular rows and move the specials into F1) restores full fidelity; owner may
alternatively compute the su(3)⊕g₂ descent, which is not currently banked. DRAFT-COMPLETE is not
sustained as claimed; DRAFT-COMPLETE-MODULO-ONE-REPAIR is.
