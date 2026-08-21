# P-INSTRUMENT — PRECOMMIT (sealed before any comparison to measured values)

**Date:** 2026-08-21 · Probe P-INSTRUMENT of the VALUE_PROBE_WAVE_CHARTER · exploratory,
NOT a CROSSING_REQUIREMENTS-numbered "eighth crossing" (that document's §4 currently states
there is no licensed candidate class; this probe is the wave's own attempt to construct one,
under the charter's own separate seal). Gate 5: no SM number enters the object-side
construction below (Part A). SM numbers enter ONLY at Part C (comparison), after this file
is written and hashed conceptually by being committed to disk before Part C runs.

## Part A — what is already computed, object-side only (recap; full derivation in NOTES.md)

The instrument is the coupling channel's welded form (B593/B856/B1011), independently
rebuilt on this bench in mpmath 50-digit precision and cross-checked exactly against the
banked values (B593's m=1 complex number; B856's five-row period table; h(5)=-1). The
listener pair u3, u6 is the DERIVED pair (B1070/B1071, sealed, proved) — not re-derived
here, taken as given, exactly as those seals license.

**The one free parameter.** u(θ) = cos(θ)·u3 + sin(θ)·u6, θ ∈ [0, π) — the unique real
great circle through u3 and u6 on the odd sector's Bloch sphere (u3 ⊥ u6, both real vectors
in the canonical weight basis, so this is literally the "no additional phase convention"
locus: the real span of the two already-derived, Galois-fixed anchor points). This is the
SAME curve B856/B1070 already used (as a finite sample) to close gap G5 — extended here to
the full circle and used for a different purpose (a calibration, not a spread-test). θ is
the single calibration constant, in the sense of the wave charter and CROSSING_REQUIREMENTS
R11's T2 slot — but this probe does NOT claim to BE the programme's T2 anchor (R11 notes T2
is provisionally spoken for by σ/L154, an unrelated quantity); θ is this exploratory probe's
own, separately-scoped calibration, disclosed as such throughout.

**Why exactly one parameter, not two.** A general point of ℂP¹_odd carries 2 real degrees
of freedom. B1070/B1071 proved Re(ζ⁻¹u†M_odd(g)u) is constant over the WHOLE of ℂP¹_odd —
so the only place a calibration can bite at all is the imaginary channel, Im(ζ⁻¹u†M_odd(g)u)
= ⟨n(g), Bloch(u)⟩, which depends on both real coordinates of u. Restricting to a single
named curve (the real great circle above) is what collapses the 2 real dof to exactly 1 —
without that restriction, one calibration equation would leave a whole residual circle of
u's undetermined, and "the other predictions" would not be well-defined numbers at all. The
restriction to THIS curve (rather than some other meridian) is the construction's one
declared, non-forced modeling choice; it is priced (below) and attacked directly in NOTES.md
rather than hidden.

**SELF-ATTACK FINDING (computed on this bench, before writing this file, still object-side
only — no SM number used to find it):** the short balanced-word "period-5" family
(B856 FINDINGS C4: R^mL^m, L^mR^m, R^{2m}L^{2m}, ... all collapse 15→5) was swept for
m=1..4 on both R^mL^m and L^mR^m (8 words total). Every word's Bloch axis w(g) = (wx,wy,wz)
agrees with EITHER R¹L¹'s or R²L²'s axis up to a signed coordinate permutation that is
ALWAYS the identity permutation (only signs flip, never a genuine mixing) — and critically,
every sign pattern found either (a) flips only wy, invisible to the real-θ curve (which only
sees wx,wz), or (b) flips (wx,wz) together, which sends Im h(θ) → −Im h(θ) identically,
i.e. h(θ) → conj(h(θ)), i.e. |h(θ)| is UNCHANGED. Consequence: **on the real great circle,
there are only TWO independent |h(m,θ)| curves in this whole word family**, not four (or
eight). Calibrating one leaves exactly ONE genuinely independent further prediction from
this family — not three. This is reported honestly rather than padded; see "what counts as
a prediction" below for how the ≥3-comparison-point request is met without overstating the
independent content.

**The two curves, exact (mpmath-identified closed forms, ℚ(√5)):**

| curve | word | tone (Re h, θ-indep.) | amplitude A = √(wx²+wz²) | \|h(θ)\| range over θ∈[0,π) |
|---|---|---|---|---|
| **A** | RL (m=1) | 1/(2φ) = (√5−1)/4 | 1/2 | [1/(2φ), 0.5877853] ≈ [0.309017, 0.587785] |
| **B** | R²L² (m=2) | −1/2 | φ/2 = (√5+1)/4 | [1/2, sin(2π/5)] ≈ [0.500000, 0.951057] |

(LR, R⁴L⁴, L⁴R⁴ reproduce curve A's \|h(θ)\| exactly; L²R², R³L³, L³R³ reproduce curve B's
\|h(θ)\| exactly — verified on this bench, all 8 words, max residual 0.)

## Part B — the pre-committed calibration + prediction plan

**Target kind (fixed by KIND_TABLE.md, not chosen for fit):** \|h(θ)\| is an
amplitude-modulus-kind quantity; the licensed SM partner is CKM/PMNS moduli \|V_ij\|
(KIND_TABLE Part 1). PMNS is primary (matches the coupling channel's banked contact
history and the fully-cited, version-pinned box table already computed at B1075); CKM is a
labeled BONUS sister-transplant (AC3 spirit), not part of the primary verdict.

**Range-compatibility screening (interval arithmetic only — the coarse magnitude of the
already-published NuFIT 6.1 e-row boxes vs. the two curves' OWN ranges above; this is not a
fit, it decides only whether a comparison is well-posed at all, before any match-quality is
examined):** the PMNS e-row is used because B1075 already identified it as the coupling
channel's only δ-independent (genuinely constraining) row — reusing that criterion, not
re-selecting it here. |U_e3| ≈ 0.144–0.156 is below BOTH curves' minima (0.309 and 0.500) —
**excluded for any θ, zero look-elsewhere, before calibration.** |U_e1| ≈ 0.809–0.834 is
inside curve B's range but above curve A's maximum (0.588) — reachable by B only. |U_e2| ≈
0.531–0.568 is inside BOTH curves' ranges — the only entry either curve can be calibrated
on if the other curve is to have a live (in-range) target left to predict.

**This forces the assignment down to exactly two live, symmetric options** (only these two
leave a nonzero, in-range prediction target):

- **Branch 1 (PRIMARY, stated reason: RL is the historically first/simplest word — B593's
  original single computation, before the family existed):** calibrate θ from
  \|h_A(θ)\| = |U_e2|; PREDICT \|h_B(θ*)\| vs |U_e1|.
- **Branch 2 (CROSS-CHECK, declared in advance, not discovered post-hoc):** calibrate θ
  from \|h_B(θ)\| = |U_e1|; PREDICT \|h_A(θ*)\| vs |U_e2|.

Both branches are run and reported; neither is suppressed regardless of outcome. The choice
of which branch is "primary" is a genuine 1-bit designer freedom, priced below.

**Calibration multiplicity.** The equation \|h(θ)\|=target is a degree-2 trig equation in
cos(2θ); a numerical scan already shows up to 4 roots θ ∈ [0,π) for a target strictly
inside the open range. PRE-COMMITTED RULE: the PRIMARY reported branch takes the smallest
θ ≥ 0 solving the calibration equation (nearest to u3 itself — a deterministic, fit-blind
rule fixed here, before the roots are computed against the real target value). ALL roots
are additionally computed and reported for transparency; a secondary "any-root" grading is
reported with its own (2-bit) look-elsewhere price, clearly separated from the primary
single-root grading.

**Both mass orderings (NO, IO) are compared, per B1075 precedent; neither is chosen after
the fact.**

**BONUS / not part of the primary verdict — CKM sister-transplant.** Predict \|h_A(θ*)\|
and \|h_B(θ*)\| (both branches' θ*) against the CKM e-row analogue |V_ud|, |V_us|, |V_ub|.
Values used: PDG global-fit standard magnitudes |V_ud|≈0.97435, |V_us|≈0.22500,
|V_ub|≈0.00369 (long-stable across PDG editions to the quoted digits) — **sourcing caveat,
disclosed:** this session's live web-search budget was exhausted before a fresh citation
could be pulled (checked; the search tool reported the session quota spent), so these are
carried from training knowledge, not freshly fetched — the same class of limitation this
corpus already discloses rather than hides when it happens (cf. B1075's nu-fit.org
certificate note). Given both curves' ranges (A: [0.309,0.588], B: [0.500,0.951]) sit far
from CKM's near-0.97-or-near-0.22-or-smaller landscape, this bonus is expected, in advance,
to be a clean range-driven miss or near-miss — stated before computing it.

## What counts as a "prediction" here, honestly

**Independent object-side content: ONE real number (θ), producing exactly ONE independent
further real number (the other curve's \|h(θ*)\|) beyond the number consumed to fix θ.**
The task's "at least 3" aspiration is met at the level of comparison POINTS (2 PMNS e-row
entries across 2 branches + 3 CKM bonus entries × 2 branches = several comparison points),
never at the level of independent object-side facts — conflating the two would be exactly
the DOF-inflation this corpus's own error ledger names (B856 C2). The verdict below grades
the ONE genuine prediction (Branch 1's |h_B(θ*)| vs |U_e1|, and symmetrically Branch 2's) at
full strength, and treats everything else (other branch as cross-check, CKM as bonus) as
supplementary, separately-priced context.

## Look-elsewhere ledger (priced in advance)

| freedom | bits |
|---|---|
| which curve calibrates (Branch 1 vs 2) | 1 |
| calibration-branch multiplicity (up to 4 roots; PRIMARY uses a fixed deterministic rule, 0 bits; "any-root" secondary grading, priced separately) | 0 (primary) / 2 (secondary) |
| mass ordering (NO vs IO, both graded, not selected) | 0 |
| e-row selection (reuses B1075's own pre-existing, published criterion — not fresh) | 0 |
| CKM bonus row/entry (3 entries × 2 branches, bonus only, not in primary verdict) | log2(6) ≈ 2.58 (bonus ledger only) |

**Primary test total: 1 bit** (the calibration-direction choice). This is a much smaller
look-elsewhere burden than B1075's 5.17 bits, precisely because the range-screening above
already did the excluding that a blind search would otherwise have to price.

## Precision budget (R6-style)

PMNS e-row boxes are known to 3–4 significant figures (NuFIT 6.1, 3σ). A "hit" is graded at
the box-edge level (inside the cited 3σ box = hit; the sealed grammar below states what
counts as a genuine hit vs. a near-miss vs. a clean miss, mirroring B1075's own R9 shape-only
downgrade).

## Declared prior (R8-style, honest, written before compute)

**MISS EXPECTED.** Every prior coupling-channel value contact (7 for 7: B1027+B1063,
B1066 R-A, B1066 R-B, B1075) missed at power, and V-3 proved no raw object period equals an
SM ratio. Adding one continuous, honestly-scoped calibration parameter to an otherwise
forced instrument is a genuinely new configuration (not a repeat of the 7 prior misses,
which used zero continuous freedom) — informative either way: a hit would be the
programme's first, and would need to survive the numerology attack below before banking; a
miss extends the coupling channel's null to the one configuration the prior 7 crossings
could not test.

## Outcome grammar (fixed before any comparison)

- **INSTRUMENT-PREDICTS**: the PRIMARY branch's prediction lands inside the target's 3σ box
  (either ordering), AND survives the numerology attack (NOTES.md: is θ secretly absorbing
  more than the claimed one degree of freedom; is the range-screening doing hidden fitting
  work). Flagged LOUDLY for cc3's mandatory 3rd opinion before any banking.
- **INSTRUMENT-NULL**: the PRIMARY branch's prediction misses the target box, in both
  orderings. The expected, honest result.
- **NEEDS-STRUCTURE**: the comparison cannot be run as designed (e.g., no real θ solves the
  calibration equation) — names the missing object datum exactly.

## Gate 5 check on this file

No measured SM value has entered the CONSTRUCTION in Part A (θ is a symbol until Part C
substitutes a number). The measured PMNS/CKM values appear in Part B/C only, as comparison
targets, exactly as every prior sealed crossing in this corpus has done.
