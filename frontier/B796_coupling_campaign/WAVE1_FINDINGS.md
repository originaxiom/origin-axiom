# B796 WAVE-1 FINDINGS (interim; prereg sealed 8424a335 before compute)

cc3 audit seat, 2026-07-29. Owner greenlight; executed independently;
cc = merge gate. Gate 5-Q. Nothing to CLAIMS.

## CELL 3 — SPIN FORK: EXECUTED (exact, sympy)

Setup verified: exactly two SL(2,C) lifts (mixed sign assignments
FAIL the relator, consistent with H¹(m004;Z/2) = Z/2): ρ₁ = (A, B)
(the banked Riley lift), ρ₂ = (−A, −B).

Exact peripheral trace patterns (meridian a; longitude bABaaBAb,
parabolic, c-entry 0 in both lifts):

    ρ₁: (tr m̃, tr l̃) = (+2, −2)
    ρ₂: (tr m̃, tr l̃) = (−2, −2)

VERDICT (per the sealed fork):
- **Convention-independent half: ρ₁ (the Riley lift) is NON-Lie under
  BOTH sign dictionaries ⇒ its Dirac spectrum is DISCRETE ⇒ the
  Dirac–Hejhal follow-up is AUTHORIZED unconditionally.**
- Convention-dependent half: under C1 (tr = −2 ⟺ trivial along the
  curve) ρ₂ is the Lie structure ⇒ essential spectrum ℝ ⇒ the
  fermionic spectral-action family CLOSES for ρ₂; under C2 neither
  lift is Lie. Resolving C1-vs-C2 is ONE named literature lookup
  (Bär's sign dictionary) — flagged, not assumed.
- Cross-check: the two structures are distinguished by cusp data;
  consistent with P52 (τ fixes both spin structures — τ acts on each,
  neither is exchanged).

Artifacts: cell3_spin_fork.py / .txt.

## CELL 2 — DOUBLET SURGERY, STAGE 0: GATE FAILED ⇒ ABORT (as designed)

The validation gate ran on three certified mult-1 newforms
(r = 4.900085373, 5.912917882, 7.406615600) with the correct O₃-dual
embedding (O₃^∨ = d1·O₃, d1 = 1 + i/√3; module map ν = p + qω ↦
integer coords (p−q, 2p+2q) in Λ*; base points resolve at machine
distance 0). Result:

    raw λ_π7 ≈ 0 on both testable forms (the coefficient at the
    O₃^∨-point of π₇ VANISHES to instrument precision);
    T1 eigen-relations: rel dev ~1 for all α ∈ {−1, 0, 1};
    T2 multiplicativity (7 = π·π̄): rel dev ~1;
    μ₆-averaged variant: c(1)-average near-cancels (expected — Γ₄₁'s
    cusp stabilizer has no unit rotations; the average is not
    justified for newforms and behaves accordingly).

**BANKED FACT (re-scoped per chat1's relay, 2026-07-29): the NAIVE
Bianchi–Hecke construction fails on Γ₄₁ mult-1 newforms at level (4),
with a STRUCTURED residual at split primes; the lift/CM reading is
UNTESTED.** Not banked: "Hecke fails for Γ₄₁" — that stronger reading
is unearned. Scoping facts:
- The gate ran on MULT-1 FORMS ONLY (r = 4.900085373, 5.912917882,
  7.406615600), per the sealed prereg — chat1's mult-2
  precondition concern (arbitrary basis of a 2-plane is not a Hecke
  eigenvector; Rayleigh ≈ 0 for generic vectors on a trace-0 plane)
  does NOT apply to this run. It WILL apply to Stage 1, where
  simultaneous diagonalization on each 2-plane is the required
  method, not a per-vector test.
- TWO signatures, separated per chat1: (i) λ_π₇ ≈ 0 raw on the forms
  r = 4.900 and 7.407 — a STRUCTURED ZERO at a split prime
  (7 ≡ 1 mod 3), classically the fingerprint of CM forms or
  base-change LIFTS; (ii) diffuse order-1 deviations in all relation
  families — the signature of a wrong double-coset construction.
  Also (iii): on r = 5.913 the coefficient c(1) at the d1-point
  near-vanishes (support pattern, distinct from (i)). Different
  causes possible; no single explanation is banked.
- NEW SOURCE (chat1, provenance hunt; NOT yet in-repo — verify
  before citing in any write-up): **Steil 1999, "Eigenvalues of the
  Laplacian for Bianchi Groups", IMA vol. 109, Springer, 617–641** —
  covers D = 1, 2, 3, 7, 11, 19; proves the spectra are NOT simple;
  states some eigenvalues are LIFTS from PSL(2,Z). Lifted forms
  satisfy BASE-CHANGE relations, not naive Bianchi–Hecke — if some
  of the 17 are lifts, the abort is the correct outcome of the WRONG
  construction, not evidence against Hecke theory.
- THEORY-FIRST TEST: **RAN, and the level-1 lift reading is
  REFUTED** (chat1, 2026-07-29): the base-change archimedean
  normalization fixed from Then's published Picard table is
  r_K = 2·r_Q (two exact 8-digit matches, one rule, zero fitted
  parameters). First possible PSL(2,Z) level-1 lift:
  r = 2·9.5337 = 19.067 — 1.4× ABOVE our scan ceiling 13.5. **None
  of the 43 eigenvalues (parent forms included) can be a level-1
  base-change lift.** Scope: this closes Steil-type level-1 lifts;
  the level-variant (base change of Γ₀(4)-forms over Q, if it
  applies to Γ₄₁ newforms) is NOT excluded by this test and is the
  one remaining lift avenue — flagged, untested.
- LIVE READINGS for the split-prime zero, discriminable: (i) **CM** —
  forces vanishing at a DENSITY-½ set of primes, not one; the test
  is a_π at ~10 primes, count the zeros; (ii) **wrong double-coset
  construction** — predicts diffuse order-1 error, NOT a zero
  tracking splitting. The a_π census is the next Cell-2 computation.
Stage 1 remains BLOCKED pending: (a) the Steil read (now for CLASS
LABELS, not multiplicities — the gate ran mult-1 only), (b) the
correct level-(4) operator, (c) simultaneous diagonalization for the
2-planes.

Instrument note (E31 discipline, on the record): the gate's own
construction caught two embedding errors before producing a trustable
verdict — (i) O₃^∨ ≠ (i/√3)·O₃; (ii) the module map is complex
multiplication by d1, not the additive dual-basis map. Both fixed
with exact integer coordinates; base-point lookups then resolve at
distance 0. The failures above are therefore statements about the
RELATIONS, not the lookup.

## CELL 1 — GH LADDER: SCAN DONE, PRIORITY REFINEMENTS IN

scanE (r ∈ (10, 13.5), dr = 0.002): **27 dips, no exceptional
eigenvalues.** The three pre-stated GH rungs all have dips at the
predicted positions. Priority refinements (GH-first):

    GH rung #2 (pred. 12.5016): r = 12.50010017, λ = 157.252504,
      S-dev = 5.7e−10 → **OLD (PARENT), STABLE — CONFIRMED**
    GH rung #3 (pred. 13.2960): r = 13.29316271, λ = 177.708175,
      S-dev = 8.9e−9 → **OLD (PARENT), STABLE — CONFIRMED**
    GH rung #1 (pred. 11.0086): **CONFIRMED after cluster
      resolution** — r = 11.008113359, λ = 122.178560, stable to
      1.8e−15, S-dev = 8.0e−10 → OLD (PARENT), mult 1. The wide
      bracket had fallen into the adjacent mult-2 newform at
      10.99654819 (λ = 121.924, Δr = 0.0116); fine scanF (dr = 5e−4)
      re-found the genuine simple dip and the tight bracket decided
      it. GH's 122.19 vs computed 122.1786: the same last-digit
      pattern as 51.014 vs 51.0132.

RUNG-#1 STATUS CHANGE, explained (per chat1's demand for the
separated values): the "unresolved cluster" was RESOLVED by
computation, not folded on proximity — the dedicated fine scan
(dr = 5e−4) separated TWO objects: the mult-2 NEWFORM at
r = 10.99654819 (λ = 121.924072, S-dev 0.99) and the mult-1 PARENT
at r = 11.00811336 (λ = 122.178560, S-dev 8.0e−10), 0.0116 apart;
the tight bracket (±2e−3 < spacing) then refined the parent to
1.8e−15 two-system agreement. CORROBORATION NUMBER (chat1's
base-rate): P(≥2 rungs by chance) = 9.5e−5 — ~10,000:1; three rungs
stronger still.

**CELL 1 VERDICT: ALL THREE pre-stated GH rungs CONFIRMED as parent
(S-invariant) eigenvalues** — 122.178560 (r = 11.00811336),
157.252504 (r = 12.50010017), 177.708175 (r = 13.29316271). The
sealed falsifier did NOT fire; the GH transcription — including the
previously uncorroborated 122.19 — is computationally
retro-corroborated (targeted confirmation; the solver was never
tuned to any of them; deviations |Δλ| = 0.011–0.076 are
1996-FEM-scale, growing with r as expected).

Full window results: 26 stable distinct eigenvalues in (10, 13.5),
45 with multiplicity, of which THREE parent; the 12.71 shoulder was
spurious (gone at dr = 5e−4). No exceptional eigenvalues. V₁ budget
in-window: expected 4.17, found 3, z = −0.57, PASS — **as a ±2σ
SCREEN only. Completeness scope limit (chat1's quantitative form of
the B791 caveat, adopted): sub-leading Weyl terms are 43–60% of the
leading term for r ≤ 13.5, dropping below 10% only near r ≈ 60; the
budget CANNOT assert the 43 are complete at this r. No completeness
claim is made or implied for the paper dataset.** Combined
certified spectrum r < 13.5: **43 distinct, 72 with multiplicity,
4 parent forms (7.072004, 11.008113, 12.500100, 13.293163)**.
Remaining Cell-1 piece: the parity census (requires the
J-normalization check first — does z ↦ −z̄ normalize Γ₄₁; part of
the cell, not assumed) — in progress, not blocking the verdict.

Instrument lesson banked (E31-adjacent, self-caught): a golden
bracket wider than the local eigenvalue spacing FALLS INTO the
deeper adjacent well — refinement brackets must be narrower than
the observed minimum spacing at that r (here 0.0116); the fine
rescan protocol (dr = 5e−4) is the standing remedy.

## CELL 9 LADDER — rung (i) status

Feasibility ANSWERED (cell9_feasibility_probe): reachable; arb
installed. Rung (i) (25-digit) prereg with its (d, H) power box is
the next seal after Wave 1 lands.
