# P-INSTRUMENT — NOTES: the construction, the mid-run discovery, the honest verdict

**Probe:** P-INSTRUMENT, the listener-map crossing cell, VALUE_PROBE_WAVE_CHARTER.
**Verdict: INSTRUMENT-NULL.** Read section 4 first if short on time; sections 1–3 are the
full derivation and the self-attack that the verdict rests on.

---

## 1. The construction

**The instrument (recap, all pre-existing/banked, not re-derived here):** SU(3) at level 2's
six-primary Kac-Peterson modular data; R = T, L = S⁻¹T⁻¹S; the conjugation weld C (θ); the
DERIVED listener pair u3, u6 (B1070/B1071, sealed and proved — the unique pair fixed
individually by all 16 elements of Gal(ℚ(ζ₆₀)/ℚ) inside the minimal exceptional orbit of
Aut(2T×2I) on ℂP¹_odd). This bench independently rebuilt all of this in mpmath 50-digit
precision (own cyclotomic-free route — dense complex exponentials reduced numerically at
high precision rather than the corpus's exact ℚ(ζ₆₀) symbolic ring) and reproduced, exactly:
B593's single m=1 value (1/(2φ) + i·sin(2π/5)/√5, to 50 digits), B856's full five-row
period-5 table, h(5) = −1 exactly, and the Kac-Peterson modular identities (S unitary &
symmetric, S² a permutation, (ST)³ ∝ S², all four gates PASS at 50 digits).

**The one free parameter.** u(θ) = cos(θ)·u3 + sin(θ)·u6, θ ∈ [0, π) — the real great circle
through u3 and u6 (u3 ⊥ u6, both real vectors in the canonical weight basis, so "real linear
combination" is the "no extra phase convention" default, not an arbitrary pick). This is the
literal extension, to a full circle, of the exact segment B856/B1070 already used (11 sample
points; then theorem-exact) to close gap G5 of `docs/LISTENER_MAP_SPEC.md`.

**Why exactly one parameter.** B1070/B1071 proved Re(ζ⁻¹u†M_odd(g)u) is constant over the
WHOLE of ℂP¹_odd (a 2-real-dof space) — the only room for a calibration is in
Im(ζ⁻¹u†M_odd(g)u) = ⟨n(g), Bloch(u)⟩, which depends on both real coordinates of u. Fixing
ONE equation (the calibration) on the unrestricted 2-dof sphere leaves a whole residual
circle of undetermined u's — "the other predictions" would not be well-defined numbers at
all unless u is restricted to a named 1-dof curve first. That restriction is this
construction's one genuinely discretionary modeling choice, and it is attacked directly in
§3.

## 2. The two curves (and why not four)

A sweep of the whole "period-5 collapsing" short balanced-word family named in B856 FINDINGS
C4 (R^mL^m, L^mR^m, m=1..4 — 8 words) found that **every word's `\|h(θ)\|` on the real great
circle equals EITHER curve A's or curve B's, exactly**:

| curve | representative word | tone (Re h) | \|h(θ)\| range, θ∈[0,π) |
|---|---|---|---|
| A | RL | 1/(2φ) = (√5−1)/4 ≈ 0.309017 | [0.309017, 0.587785] |
| B | R²L² | −1/2 | [0.500000, 0.951057] |

LR, R⁴L⁴, L⁴R⁴ reproduce curve A's `\|h(θ)\|` identically; L²R², R³L³, L³R³ reproduce curve
B's identically (max residual 0 over the sweep). Mechanism: every sign relation found among
the 8 words' Bloch axes either flips only the wy-component (invisible to the real-θ curve,
which only ever sees wx, wz) or flips (wx, wz) together, sending Im h(θ) → −Im h(θ) (i.e.
h → conj(h)), which leaves `\|h\|` unchanged. **So this whole 8-word family supplies at most
2 independent `\|h(θ)\|` curves, not 4 or 8** — reported here as a direct, computed
self-attack finding, not assumed.

## 3. THE MID-RUN DISCOVERY (found while executing PRECOMMIT's Branch 1/2, before any
verdict was drawn — reported here in full, in the spirit of this corpus's own self-audit
convention, e.g. B856 FINDINGS §0)

Running PRECOMMIT's calibration (solve `\|h_A(θ)\| = target`) produced, generically, **4
roots θ in [0, π)**. All 4 were carried forward as instructed (no cherry-picking). **All 4
gave the identical predicted `\|h_B(θ)\|`, to 50 digits.** That is not expected generically
(four different θ's landing on the same downstream value) and was investigated rather than
shrugged off.

**Root cause, verified two independent ways:** (1) exact closed-form comparison of the
Pauli/Bloch axes: `(tone_B, wx_B, wz_B) = −φ · (tone_A, wx_A, wz_A)` exactly (mpmath
`identify()` gives closed radical forms for each component; the ratio is `−φ` to 50 digits
on every component); (2) independent brute-force evaluation `u(θ)† · weld(word) · u(θ)` at
12 random θ (not using the closed form at all) confirms **`h(R²L², θ) = −φ · h(RL, θ)`
exactly, for every θ on the curve** (worst residual 1.1×10⁻⁵⁰). This is *not* a full 2×2
matrix identity — `M_odd(R²L²) ≠ −φ·M_odd(RL)` as matrices (checked directly; the
off-diagonal antisymmetric part, wy, does not carry the same factor) — it holds specifically
for the real-linear-combination family this probe uses.

**What this means for the construction: it is degenerate for this word pair.** The
calibration never actually used θ as a free continuous coordinate in any way that reached
the prediction — `\|h_B(θ)\|/\|h_A(θ)\| = φ` identically, for every θ, so fixing `\|h_A\|`
fixes `\|h_B\|` by a constant rescaling regardless of which root is chosen or, indeed,
regardless of calibration at all. **The intended "1 continuous input → forced prediction"
crossing collapsed into a ZERO-PARAMETER, forced RELATION** — Type Law
(`frontier/B1032_type_law`) clause (i), "a relation among measured quantities," consumes
*zero* anchors (stronger than the originally-planned T2-style calibration, in the sense of
R11's own hierarchy, but a different claim than what PRECOMMIT set out to test).

**Sanity check this is not itself new physics smuggled in:** the ratio is recoverable
directly from numbers already sitting in the banked B856 table (`h(m=2,u3)/h(m=1,u3)`,
computed from the already-published table entries, also gives `−φ` to the table's quoted
precision) — this is an unnoticed recombination of already-banked numbers, not a new
computation about the object at the level of "new data." What IS new here: confirming it
exact (50 digits, two independent methods) and confirming it extends across the *whole* real
great circle, not just at the single point u3.

**Consequence for "at least 3 predictions":** honestly, no. The whole 8-word short family,
restricted to the one non-arbitrary curve available, supplies exactly ONE independent
real-valued object-side curve (θ ↦ `\|h_A(θ)\|`); every sibling word's value is pinned to it
by an exact, forced, zero-freedom relation (conjugation for the m↔5−m partners; this
golden-ratio scaling for the RL↔R²L² pair). Manufacturing a third independent number would
require either a different curve (reopening the "which curve" choice this NOTES file already
flags as the construction's one soft spot) or reaching into longer words/other conjugacy
classes outside the named period-5 family (an open-ended search this probe declines, since
picking words until three "work" independently is exactly the scan-and-pick numerology the
charter's binding discipline forbids). **This is reported as a computed boundary of what
this specific, honestly-scoped instrument can deliver — not a shortfall in effort.**

## 4. THE VERDICT

Both the originally pre-committed branch tests and the sharpened, honest post-discovery
ratio test were run (same pre-committed targets throughout — PMNS e-row, both mass
orderings; no new SM number was chosen after seeing any result):

| test | predicted | measured (NO / IO) | result | excess beyond box edge | ≈ total σ (3σ box convention) |
|---|---|---|---|---|---|
| Branch 1 (A→B): `\|U_e1\|` | 0.88879 | [0.8092,0.8345] / [0.8091,0.8343] | **MISS** | 4.29 / 4.32 half-widths | ≈15.9σ / ≈16.0σ |
| Branch 2 (B→A): `\|U_e2\|` | 0.50793 | [0.531,0.5676] (both) | **MISS** | 1.26 half-widths | ≈6.8σ |
| Direct ratio: `\|U_e1\|/\|U_e2\|` | φ = 1.61803 | [1.4257,1.5716] / [1.4255,1.5712] | **MISS** | 0.637 / 0.643 half-widths | ≈4.9σ |
| Range screening: `\|U_e3\|` | unreachable by either curve, any θ | [0.1437,0.1555]/[0.1447,0.1562] | **excluded a priori** | n/a (below both curves' minima 0.309, 0.500) | zero look-elsewhere |
| CKM bonus: `\|V_ud\|,\|V_us\|,\|V_ub\|` (exploratory only) | 0.88879 (same B-value) | 0.974 / 0.225 / 0.0037 | **MISS** (closest: Vud, 8.8% relative) | — | not part of primary verdict |

All three independent framings of the primary test agree in direction (the object's forced
ratio, φ ≈ 1.618, sits systematically ABOVE the measured e-row ratio, ≈ 1.43–1.57) and all
three exclude decisively (≥4.9σ-equivalent in the most conservative framing). This is a
clean, powered miss, not a near-miss or an ambiguous result.

**Look-elsewhere, settled honestly (revising PRECOMMIT's advance estimate downward, now that
the degeneracy is understood — the corrected number is smaller, i.e. the test is MORE
decisive than priced in advance, not less):** PRECOMMIT priced "which curve calibrates" at 1
bit, treating Branch 1 and Branch 2 as two independent trials. They are not — both solve the
identical relation `\|h_B\| = φ\|h_A\|` for a different variable, so they rise or fall
together (and did: both MISS, same direction). The honest look-elsewhere for the PRIMARY
claim (the forced relation `\|U_e1\|/\|U_e2\| = φ`) is **zero bits**: no anchor, no scan, no
branch choice that could have changed the outcome (all 4 calibration roots agree; both
solve-directions test the same relation; both mass orderings agree). The only real
designer choice upstream was the curve itself (§3's flagged soft spot) and the e-row
selection (reused from B1075's own prior, published criterion, not fresh).

**INSTRUMENT-NULL.** The coupling channel, extended by this construction's one honestly-
scoped continuous parameter, still carries no detectable SM content — extending V-3's null
and the prior 7-for-7 coupling-channel record to the one configuration (a continuous
calibration) those seven crossings could not test. This is the expected, honest result,
declared as such in PRECOMMIT before compute.

## 5. The case that this is NOT numerology (attacking the construction one more time, as instructed)

- **Is θ secretly absorbing more than one degree of freedom?** No — if anything, the
  opposite: θ turned out to absorb **zero** effective degrees of freedom in the specific
  comparison that was run (§3). The construction has exactly one continuous dof by design
  (a 2-dof space minus a named 1-dof restriction), and the actual test performed did not
  even need it (a zero-parameter relation was what got tested). There is no hidden second
  knob: the only discretionary choice anywhere in the pipeline is the curve itself (declared
  and attacked below), and it is fixed BEFORE seeing any comparison value.
- **Is the "prediction" actually another fit?** No — φ was not chosen to match anything; it
  is the exact, forced ratio of two already-banked coupling values (§3's B856-table check),
  confirmed independently by direct computation. No adjustable constant was tuned to
  approach the measured ratio (≈1.43–1.57); φ (≈1.618) sits outside that range and nothing
  in the pipeline was free to move it closer.
- **Is the curve choice (real great circle through u3, u6) doing hidden fitting work?**
  This is the construction's real soft spot, named honestly rather than hidden: a DIFFERENT
  1-dof curve through u3, u6 (any other meridian, i.e. a nonzero relative phase between the
  u3- and u6-components) would generically see a nonzero wy-contribution and would report
  DIFFERENT numbers. The curve used here was fixed by criteria stated BEFORE any SM
  comparison (it is the literal continuation of an already-existing, independently-motivated
  segment from B856/B1070, and "real coefficients in the canonical basis" is the
  no-extra-convention default) — but a different, equally defensible curve was not tried and
  compared, so this construction cannot claim to have searched the space of curves and found
  this one special. It reports what one natural, pre-existing, non-cherry-picked curve gives,
  honestly, and no more.
- **Is the e-row / PMNS choice doing hidden work?** No — reused verbatim from B1075's own
  prior, already-published, structural reason (δ-independence; the only row with genuine
  exclusion power), not re-selected here for fit quality.
- **Given the verdict is NULL, none of this needs to survive a numerology attack for
  banking purposes** — the attack above is recorded so that IF a future, differently-cured
  version of this instrument (a different curve, honestly motivated in advance) ever
  produces a hit, the attack surface it must survive is already on record.

## 6. What is, and is not, being claimed

- **Claimed:** an honest, independently-reproduced, 50-digit-verified execution of the
  charter's P-INSTRUMENT probe, using a genuinely one-continuous-parameter construction built
  from the object's own field data, calibrated once, compared to measured PMNS values,
  found NULL.
- **Claimed, as a side finding, independent of the SM verdict:** an exact new closed-form
  relation, `h(R²L², θ) = −φ · h(RL, θ)` on the real great circle through u3, u6 — golden-
  ratio-exact, verified two independent ways, not previously stated as a law anywhere found
  in this corpus (though recoverable from already-banked numbers) — worth a LAW_MAP row on
  its own merits regardless of the NULL crossing verdict; flagged for the banking seat's
  judgment, not banked here (this probe's mandate is the crossing question).
- **Not claimed:** that the coupling channel has been exhaustively re-searched for a hit
  (this probe touched exactly one curve and one word-pair-derived relation inside one small
  word family); that the curve choice is uniquely forced (§5); that "at least 3 independent
  predictions" was delivered (§3 explains why, honestly, it was not, for this specific,
  non-arbitrary construction).
