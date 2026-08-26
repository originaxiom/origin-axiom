# TRACE THREE — the record's two arithmetic ends are the unit answer and the ramified answer to one equation, and the one meridian that drives both is a three-step clock on matter and a golden clock on geometry
## (outside bench, 2026-08-26; forty-ninth memo; the atlas's `two_ends` unity pattern given its first exact mechanism; one machine-caught error filed below)

### The question
The recurrence atlas's top two structural motifs — the **golden end** (ℚ(√5),
56% of probes) and the **Eisenstein end** (ℚ(√−3), 53%) — were identified as
one object by the `two_ends` unity pattern, but only statistically: no single
exact computation ever exhibited the mechanism joining them. This cell does.

### THE FACTS (`certificates/trace_three.py`, all exact over ℚ and ℚ(q))

- **FACT 1 — the golden end comes from the clock.** The fiber substitution is
  *rediscovered in-run* by exact matrix search over reduced words (U='bA',
  V='abAA', target a·V·a⁻¹): the unique length-≤5 match is φ(V) = VU⁻¹VV, and
  its abelianization is the matrix [[0,−1],[1,3]] with characteristic
  polynomial **x² − 3x + 1**: trace 3, det **1 (a unit)**, discriminant 5.
  Roots φ², φ⁻². This is the monodromy tick on H₁(fiber) — the cat map.
- **FACT 2 — the Eisenstein end comes from the conserved number.** κ = tr[a,b]
  = 1+q (re-verified in-run from the ℚ(q) holonomy) has minimal polynomial
  **X² − 3X + 3**: trace 3, norm **3 (the ramified prime)**, discriminant −3.
- **THE MECHANISM.** Both ends are monic quadratics of **trace 3**; the only
  difference is the constant term d, and disc = 9 − 4d:
  | source | polynomial | d | disc | field |
  |---|---|---|---|---|
  | the clock (Fact 1) | x²−3x+1 | 1 = unit | 5 | ℚ(√5), golden |
  | the integral (Fact 2) | X²−3X+3 | 3 = ramified | −3 | ℚ(√−3), Eisenstein |
  The object supplies both witnesses itself — one from its dynamics, one from
  its conservation law. The two ends are the unit answer and the ramified
  answer to the same trace.
- **FACT 3 — one meridian, two clocks.** The same generator a acts:
  - on the **fiber lattice** with spectral radius φ² — an exponential clock,
    entropy 2·log φ > 0, exactly the roots of Fact 1's polynomial;
  - on the **carrier Ψ = ℂ²⊗27** (memo 46) as a unipotent with nilpotency
    degree **EXACTLY 3**: (ρ_Ψ(a) − I)² ≠ 0, (ρ_Ψ(a) − I)³ = 0, computed by
    exact 54×54 rational matrix powers. A polynomial clock, zero entropy.
    Mechanism: e_r raises the h-weight by 2, so ρ27(e)² = 0 on the internal
    doublets and the spinor factor is likewise 2-step; the Kronecker product
    composes two 2-step factors to depth 2 + 2 − 1 = 3.
  Matter's internal time under the meridian is finitely deep (three exact
  steps, then nothing); geometric time is hyperbolic (golden exponential).
- **FACT 4 — the beat's role.** gal fixes Fact 1's polynomial coefficientwise
  (it is rational: the golden clock is untouched by the mirror) and permutes
  the roots of Fact 2's inside ℚ(√−3) (κ ↔ gal κ, memo 41): **the mirror
  stirs only the Eisenstein pair.** The invisible bit lives entirely at the
  ramified end; the golden end is mirror-blind.

> **TRACE THREE: the record's two arithmetic ends are the unit answer and the
> ramified answer to a single equation — trace 3 — with the object supplying
> both witnesses itself: its clock's characteristic polynomial (disc 5) and
> its conserved number's minimal polynomial (disc −3). And the one meridian
> that drives both reads matter and geometry at different depths: three exact
> steps on the carrier, golden exponential on the fiber.**

### Error filed (machine-caught, preregistration did its job)
The first draft preregistered nilpotency degree **4** for Fact 3, from a
mis-set weight ladder (assuming the internal doublets carried a 3-step e).
The assert failed: the machine returned **3**. Root cause: e_r raises the
h-weight by 2, so ρ27(e)² = 0 already on the doublets — both tensor factors
are 2-step and the composite depth is 2+2−1 = 3, not 4. The certificate's
docstring, assert, and prose were corrected and the full cell rerun clean.
Filed here at the point of occurrence per the standing rule (lane error #3).

### What this feeds (the climb note)
This is the exact seed the atlas's `two_ends` pattern was missing: golden and
Eisenstein are not two coincidentally frequent fields but the **det-1 and
norm-3 completions of the same trace-3 form**, produced by the object's clock
and the object's first integral respectively. Flagged for the banking seat as
an atlas-level annotation candidate (the unity pattern can now cite a
mechanism, not just co-occurrence). Interacts with: memo 41 (κ's all-3
invariant content), memo 43 (the substitution and its det-1 trace-3
abelianization, here re-found blind), memo 46 (the carrier the meridian is
3-step on), THE_CORE_QUESTION §5 (invariant content at the ramified prime).

### Fences
Fact 1's search is exact but bounded (words of length ≤ 5 in U,V; the found
substitution matches memo 43's independently discovered one). "Entropy" and
"clock" are standard dynamical readings of exact spectral facts, not new
computations. The unit-vs-ramified reading is arithmetic fact; that it
*explains* the atlas percentages is INTERPRETIVE and labeled as such.
Kinematics only; Gate 5 untouched.

### Certificates
`certificates/trace_three.py`; output `outputs/trace_three_out.txt`
(vendored copy re-run in-lane, byte-identical).

### One sentence for the ledger
The golden end and the Eisenstein end are one question — trace three — asked
twice, answered once by a unit and once by the ramified prime, by the object's
own clock and the object's own conserved number; and the meridian that beats
both clocks gives matter exactly three steps of internal time while geometry
gets the golden exponential.
