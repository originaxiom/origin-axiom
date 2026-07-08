# P4 panel v1 — adjudication (every finding verified before acceptance)

**The panel: 5 agents, 55 tool uses, 28 min. Raw findings verbatim in
`PANEL_v1_findings.md`. Verdict: the panel caught TWO BANKED ERRORS, deflated the headline
theorem into a stronger two-line form, found a 45-year literature the lit-gate missed,
and identified a class-group refinement that upgrades the breathability story. Every
FATAL/MAJOR below was independently re-verified before acceptance (sympy/session log).**

## CONFIRMED — banked corrections (already applied: B470, B471, registry ×5)

1. **[FATAL, correctness] Theorem E′ false in generality** — the palindromic-alphabet
   argument covers two-block products only; rev·swap reverses the BLOCK sequence.
   Counterexample verified: A₁A₂A₃. Chain rungs remain word-mirror (locked ≤ 8); the
   standard-word near-palindrome lemma is the open proof route. Banked correction in
   B470/BREATH_HIERARCHY + B471 + registry T-MIRROR.
2. **[MAJOR ×3, all seats] "family = breathability locus" false** — verified: A₁³ is a
   rooted composite (X₁³); [[19,30],[12,19]] is breathable at metallic trace 38 and not
   conjugate to A₆ (ℤ[√10], h = 2; genus obstruction + exhausted small-conjugator
   search). **The corrected—and better—theorem: breathable traces = metallic traces;
   A_m = the principal breather; family = locus ⟺ h⁺(m²+4) = 1.** Banked in B471 +
   registry T-BB.
3. **[MAJOR, hostile] Theorem A is a generic symmetric-pair identity** — verified
   symbolically: for symmetric A, B ∈ SL(2), BA = (AB)ᵀ gives tr[A,B] = 2 − (M₁₂−M₂₁)².
   The metallic content is exactly M₁₂−M₂₁ = mn(n−m). Two-line proof; the square is the
   transpose (elliptic) involution; the paper's weight moves to the Cohn identification.
   Registry T-UNIQ updated; the novelty gate REDIRECTED to the symmetric/palindromic
   corner of Markov theory.
4. **[MAJOR, hostile] The Hannay–Berry gap** — W_m at level N is the quantized cat map;
   the lit-gate for §4 must run against Hannay–Berry 1980, Degli Esposti, Kurlberg–
   Rudnick (the repo's own B376 already knew the identification; the draft failed to
   carry it). Registry T-KQ lit-gate widened. "We could not locate" items (e),(f) are
   SUSPENDED until that gate runs.
5. **[MAJOR, overclaim] "certifiably non-algebraic to degree 8"** — PSLQ is a
   height-bounded exclusion, not a certificate. Registry phrasing corrected; the same
   fix goes into the draft.

## CONFIRMED — draft-v2 obligations (structure/prose; no bank impact)

6. [FATAL, structure] §4.3 unrefereeable: Par, P_a, Q_b, channels, tiers, dark — all
   undefined in-paper; the master table must be printed. → §4.0 definitions block +
   the 36-cell table inline.
7. [MAJOR] The W_m ↔ A_m bridge: state the Weil rep with citation (Nobs–Wolfart /
   Gérardin), the R ↦ D, L ↦ (FDF*)* lemma, ord(W₁) = 20 / ord(W₂) = 12 as a
   proposition; F(iii): genuine-rep-at-odd-level for the scalar, and the ⟸-only honesty
   (converse = verified-on-240 or prove faithfulness on non-central classes).
8. [MAJOR] Theorem E: split into word-level and manifold-level chains; state the
   word-mirror ⟹ amphichiral bridge lemma (rev·swap = transpose word — standard-shaped,
   cite); the "balanced ⟹ frozen residue" clause gets its actual lemma in §4 (the
   residue = det(Par·W(w)) = −ω^{#L−#R}, frozen ⟺ balanced — the content exists in the
   banked record (B470-RF3), it was simply never imported into the paper) or is cut.
9. [MAJOR] Abstract fixes: the definite-article monodromy claim (drop/scope);
   "closes exactly at (2,3)" → closure SET characterized by F(iii), (2,3) = the minimal
   nontrivial address (verify minimality); the hierarchy's domain = words in {R,L};
   strictness claims scoped to the witnessed arrows.
10. [MAJOR] §1's framing sentence needs its hypotheses (discrete/faithful/type-preserving);
    the §3→§4 bridge paragraph (the level is a chosen case study; no quantization functor
    claimed; point to open problem 4).
11. [MINORs] Theorem D converse one-liners (det(B−I) = −t²; B's CH); C(iii) notation
    tr([·]^{±1}) + the two silent lemmas; seam-term discipline (one definition, one use);
    "stage" as terminology at first use; Fricke identity citation precision.

## REJECTED / DOWNGRADED (referee findings that did not survive verification)

- (none rejected outright this round; two hostile-seat rhetorical points — "the
  corrections ledger undermines credibility" — are judgment calls deferred to the owner;
  the same seat's own verdict conceded the ledger "would survive hostility if the
  mathematics is right," which it now is.)

## The panel's net effect

Draft v1 → v2 is a REWRITE of §3–§4's claim structure around three stronger theorems
(the symmetric-pair mechanism; the principal-breather/class-group statement; the
closure-set characterization), one new definitions block, one imported lemma, and a
suspended novelty section pending the Hannay–Berry gate. The panel paid for itself
several times over — and confirmed the charter's premise: our own agents found what a
journal referee would have found, before a journal referee could.
