# B599 — THE θ-PARITY SELECTION RULE (chat-2's unification theorem): the stage face banked

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities.
Provenance: internal (owner + AI seats). Locks `tests/test_b599_selection_rule.py`.
The ALGEBRAIC face is RELAYED-PENDING (chat-2's witnesses are compute-blocked
on their side and never reached this repo — see below).**

## The theorem (stage face — proven and locked here)

Let a pairing datum be (bra, insertions, ket) with every factor Θ-homogeneous
and the contraction Θ-invariant, n = the number of θ-odd factors. Then the
evaluation vanishes unless n is even. Proof: C is central ([C,S] = [C,T] = 0,
locked) and C² = 1; inserting C through the contraction multiplies the
evaluation by the total parity; odd total ⟹ A = −A = 0. ∎
Verified additionally by 300 random Θ-homogeneous configurations on SU(3)₂
(every odd-total pairing = 0 exactly; even-total generic).

## What it subsumes (one grading, seven banked results)

X3 (n = 0, vacuum) · the third unhearability (n = 0, bare states) · the
fourth (n = 0, closed contractions) · B592-OPEN's parity conservation (the
same argument one level up) · B593's ε² hearing law (n = 2: lean·lean) ·
B594's state-independence (n = 2 corollary) · the C-absorption identity
(the n = 0 statement — the mirror covector cancels the twist exactly when no
odd insertions are present; the dial IS insertions; the first surviving
configuration is n = 2).

## Boundaries (as relayed, consistent with the bank)

The rule forces ZEROS, not values — the n = 2 coefficients remain
stage-specific (golden 1/(2φ) + i·sin(2π/5)/√5; E₆₂'s sine kernel). States of
mixed parity hear at first order in their own odd component (B593's
displacement as a state property, not a violation).

## The algebraic face — RELAYED-PENDING (not banked)

Chat-2's algebraic proof cites their in-session artifacts (route_exact.json,
r4b_extraction.py; ord v₄ = 5, ord v₈ = 3; L1's exact zeros; the m = 8/word-b₂
t² coefficient −536481792000) — produced during their sandbox outage and NOT
present in this repository. Per verify-don't-trust these are registered as
claims awaiting either their artifact delivery or in-repo recomputation
(the natural home: the L85 campaign's P2/P3 parity bookkeeping, which this
rule structures). The general-k graded-trace bookkeeping is flagged by chat-2
itself as to-be-written — registered.

## Chat-2's question, answered

The longitude convention in the current campaign (B598-P1's cusp table, and
the one to use for any double/weld reconciliation): **λ = [b, a], the word
"baBA", in the presentation ⟨a, b | abABaBAbaB⟩** — the fiber boundary,
B67's convention. All P1 values are normalized with ξ(μ = a) leading
coordinate 1.

## Anchors

X3/B584/B592/B592-OPEN/B593/B594 (the subsumed results), B576 (the ℤ₂
grading), B585/B591 (the two lifts as the geometric carrier), chat-2's
handoff (the theorem's source — relayed in-chat during their outage).

## B599-ALG — the algebraic face: UPGRADED from relayed-pending to in-repo recomputed

Chat-2's extraction script (delivered verbatim in-chat during their outage;
`r4b_extraction.py`, path-fixed; full output `r4b_extraction_output.txt`) ran
green in this repository. Every expected lock matched:
- **L0:** the pairing form Ω is NOT dot-symmetric — the blocks are not
  dot-orthogonal, so the L1 zeros are parity, not orthogonality;
- **nilpotency:** ord(v₄) = 5, ord(v₈) = 3 on the 27 (exact);
- **L1 (the k = 1 parity lemma):** (v_m v₀)ᵀv₀ = 0 exactly at m = 4 and 8;
- **the algebraic quadratic law:** the Im-part of every tested word/slot
  starts at t² (five words × two slots) — the n = 2 selection-rule statement
  on the algebraic face, exact;
- **the witnesses:** m = 4/b2 → +2096640; m = 8/b2 → −536481792000;
- **the weld-only twist-twist identity:** the m = 8 weld value's
  √−3-coefficient = −536481792000 = the t² coefficient, exactly.
The general-k graded-trace bookkeeping remains flagged (chat-2's own caveat);
k = 1, 2 are exact computations. Item 4 (the frozen 20-word tables) is one
TESTW extension away — queued (chat-2's sandbox or a later slot here).
Locks: `tests/test_b599_alg.py` (OA_SLOW).


## Correction to the chat-2 answer (2026-07-15)

The longitude answer given above ("baBA") was WRONG — it is the fiber-frame
commutator, not the longitude of the meridian presentation. The correct
input for item 5: **λ = "abABaaBAbA"** (image −[[1, 2√3·i],[0,1]] in the
geometric rep — the banked cusp shape; commutes with the meridian; found by
direct search after P2's Gate A caught the mislabel). ξ(μ) conventions
unchanged.
