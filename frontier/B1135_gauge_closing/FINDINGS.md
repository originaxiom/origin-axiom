# B1135 — THE GAUGE CLOSING: the factor-preserving branch closes into E₆(−14) (compact heart = the SO(10) GUT), and the checksum set becomes a functional taxonomy

**Status: banked (frontier). Verdict PROVED (the MATH: the factor-preserving involutive
conjugations close the gauge branch, and the physical one-compact-slot row lands in
E₆(−14) whose maximal compact is so(10)⊕u(1)). Harvest arc — the cloud seat's TWELFTH memo
F-1 / THE GAUGE CLOSING (golden_gate commit `943db85`), verified TWO-BENCH: the cloud
seat's canonical sweep + THIS bench's fully independent re-derivation (own factor-preserving
involution search, own generalized per-slot signature, own GF(2) sign-lift solver; only
B1102's banked-and-locked Chevalley e₆ imported; the reused infra design is B1134's own
already-verified machinery, re-typed not live-imported). The MATH is confirmed exact with
NO discrepancy. Cloud seat credited. Gate 5 untouched. Lock
`tests/test_b1135_gauge_closing.py`.**

## The question (the factor-preserving complement of B1134)

B1134 THE SIMULTANEOUS CLOSING swept the factor-SWAPPING involutions (the 48 slot-swappers
that swap two of the three A2 slots) and found the SPACETIME branch: swap → Lorentz so(3,1),
plus compact color → forced into E₆(−26) = M(𝕆,ℂ). F-1 sweeps the FACTOR-PRESERVING
involutions (no swap) — the complement — and asks what the observer's *gauge*-side closings
are.

## THE THEOREM (verified exact, two-bench)

Sweeping ALL **128** factor-preserving involutions of Aut(Φ(E₆)) = W(E₆) ∪ δW (64 in W, 64
in the diagram-flip coset) × all involutive signed Chevalley lifts (**2000** conjugations
total):

- **The W coset is STERILE:** all **1000** W-coset conjugations give (sl(3,ℝ))³ inside split
  E₆(6) (χ=+6). No compact slot is reachable without the flip — **gauge compactness requires
  the outer 27↔27̄ (diagram-flip) coset.** Compactness carries charge-conjugation content.
- **The flip coset factorizes slot-by-slot as (9+1)³ = 1000:** each A2 independently takes
  **9 closings to su(2,1) and exactly 1 to compact su(3)** (verified at the per-slot marginal
  level — 900:100 = 9:1 on each slot, genuine multiplicative independence, not just the
  aggregate); **sl(3,ℝ) never appears on the flip side.** The global form is a function of the
  compact-slot count alone: **0 → E₆(2) (χ=+2, 729), 1 → E₆(−14) (243), 2 → E₆(2) (χ=+2, 27),
  3 → E₆(−78) (1)** (the binomial C(3,k)·9^{3−k}).
- **The physics row = one compact slot** (243 of them, all χ=−14): the compact slot is su(3)
  (0,8), the other two slots are su(2,1) (signature (4,4), maximal compact **u(2) = su(2)⊕u(1)**
  with 4 non-compact directions), and the global host is **E₆(−14)**, maximal compact
  **so(10)⊕u(1)** (compact dim 46 = 45+1, cross-checked on every one of the 243). A
  representative passes the FULL 3003-pair Chevalley-bracket automorphism check with **0
  failures**, θ²=I exact.

> **THE FORK NOW HAS REAL-FORM LABELS.** The spacetime branch closes into **E₆(−26) =
> M(𝕆,ℂ)** (compact core f₄; B1134); the gauge branch closes into **E₆(−14)** (compact core
> **so(10)** — the one-family SO(10) GUT); the *unclosed* object is split **E₆(6)** — literally
> the Chevalley ℚ-span the whole programme computes in; mixed even-count closings give **E₆(2)**;
> the total closing is compact **E₆(−78)**. So **B1119's checksum set {−78, −26, −14, +2, +6}
> — banked as nothing more than "the characters the classification allows" — is a FUNCTIONAL
> TAXONOMY: the five real forms of E₆ are the five things an observer can do to this object.**
> (Verified: the compact-dimension signature {36, 38, 46, 52, 78} matches the computed
> negative-eigenvalue count on every one of the 2000 conjugations, 0 mismatches; −26 is
> correctly ABSENT from this family — it requires the swap, so F-1's factor-preserving family
> is disjoint from B1134's factor-swapping one, not an instrument break.)

## THE INDEPENDENT VERIFICATION (this bench, own code)

Own script `verify_gauge_closing.py` (imports only B1102's vendored e₆; the sweep/signature
code freshly authored, the involution family changed from factor-swapping to
factor-preserving and the per-slot signature generalized to all three slots), results pinned
in `b1135_results.json`, full run in `b1135_run.log`. Every quantitative claim reproduced
**digit-for-digit, no discrepancy**: the 128 count and its 64/64 split, the 2000 total, the
nine-row menu with exact multiplicities, the W-coset sterility, the (9+1)³ factorization at
both joint and per-slot-marginal level, the compact-count→χ map, the one-compact-slot
E₆(−14) row with so(10)⊕u(1) compact dimension, the full-3003 automorphism on a
representative, and the checksum. A cleaner outcome than B1134's (which carried a 4/24
novelty over-statement); F-1's math has no analogous defect.

## THE FENCES (frame choices and cited items — integrate the math, quarantine the framing)

- **The slot → physics assignment (which A2 is "color" vs "EW room") is a FRAME CHOICE**, not
  a computed fact. The menu's clean 3-fold position symmetry shows it directly: the compact
  slot in the one-compact row lands at index 0/1/2 with exactly 81/81/81. Verified: the
  signatures, dimensions, real forms. Not adjudicated: the labels.
- **su(2,1)-as-Higgs-doublet and 16-as-one-family are INTERPRETIVE readings**, carried from
  the memo, not verified here. What is verified: su(2,1)'s maximal compact is u(2)=SU(2)×U(1)
  with a complex-doublet's worth (4) of non-compact directions; the global host is E₆(−14).
- **27 = 16 ⊕ 10 ⊕ 1 under E₆ ⊃ SO(10)×U(1) is CITED standard** (Slansky 1981; any GUT text),
  dimension-consistent (16+10+1=27), not independently recomputed.

## What it settles, and what it opens

**SETTLED (structure):** the observer's gauge-side closings are exhausted (within
factor-preserving involutive conjugations); the physical closing lands in E₆(−14) whose
compact heart is the SO(10) GUT algebra; and the E₆ real-form taxonomy is complete — five
forms, five observer jobs. Beside B1134, the object's fork (spacetime vs gauge) now carries
exact real-form labels on both prongs, both landing in the object's own exceptional real
forms.

**OPEN (typed in the memo; G-1 greenlit this session):**
- **G-1 (the Y-selection, greenlit):** do B1102's 18 hypercharge directions land
  σ-compatibly inside the gauge closing's u(2)? — now posable on the RIGHT branch (E₆(−14),
  where electroweak lives). A structural compatibility question (Gate 5-safe); if it reaches
  hypercharge *normalization* it is the values-as-regulators door (firewalled, R48-3).
- **G-2:** the e₇/e₈ ladder — is "any two of three" E₆-specific?
- **G-3:** the 27 under E₆(−26) vs E₆(−14) side-by-side matter table.

## Credit + relay

The result is the **cloud seat's** (twelfth memo F-1, golden_gate `943db85`). Integrated here
under B1135 per integrate-don't-merge, re-derived independently before banking (clean, no
correction needed). The relay is credited in `docs/RELAY_LEDGER.md`. Gate 5 untouched.
