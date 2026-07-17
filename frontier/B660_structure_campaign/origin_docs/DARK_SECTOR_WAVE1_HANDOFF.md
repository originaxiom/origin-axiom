# DARK SECTOR — Wave 1 Handoff

**Date:** 2026-07-17. **From:** Chat-1. **For:** CC and CC2.
**Status:** Chat-1 computed a PROXY result on SU(3)₂. Every claim
below requires CC verification on the exact E₆ level-2 machinery.
Three caveats flag where the proxy might fail.

---

## WHAT CHAT-1 FOUND (SU(3)₂ proxy, NOT E₆-verified)

Using the banked B238 su3_data at level k = 2 (κ = 5), the weld
operator W = R·L (the figure-eight monodromy) was evaluated on the
6-dimensional representation space of SU(3) level 2.

### Result 1: The singlet hears

The diagonal entry W[(0,0), (0,0)] = −0.2456 − 0.1784i.
|W[(0,0), (0,0)]| = 0.3035 ≠ 0.

The trivial representation's hearing amplitude is NONZERO.
The dark sector (if V₀ maps to the trivial rep) participates
in the quantum hearing at the golden stage.

### Result 2: Equal-modulus diagonal

ALL SIX diagonal entries |W[i,i]| = 0.3035, exactly equal.
Every representation hears with the same modulus. The singlet
is not suppressed relative to the visible-sector representations.

Note: this modulus is NOT 1/(2φ) = 0.3090. The individual diagonal
moduli differ from the trace-derived hearing amplitude. The trace
tr_odd = −1/φ = −0.6180 is a SUM over the off-diagonal-inclusive
structure; the individual diagonal entries have a different modulus.

### Result 3: The dark portal is open and flavor-specific

All cross-terms W[(0,0), other] are nonzero. The singlet couples
to every other representation through the weld operator. The portal
exists at the quantum level.

The cross-coupling moduli take exactly TWO values:

| Target rep | Modulus | θ-parity |
|------------|---------|----------|
| (0,1)      | 0.4911  | odd      |
| (0,2)      | 0.3035  | odd      |
| (1,0)      | 0.4911  | odd      |
| (1,1)      | 0.4911  | even     |
| (2,0)      | 0.3035  | odd      |

Two distinct portal strengths: 0.4911 and 0.3035.

### Result 4: The portal ratio is φ

0.4911 / 0.3035 = 1.61803... = φ to 10 digits.

The dark sector couples to different visible-sector representations
with strengths in the golden ratio. The two portal moduli are
related by the framework's own fundamental constant.

---

## THE THREE CAVEATS (each is a verification task for CC)

### Caveat 1: SU(3)₂ is a proxy, not E₆

The computation used the 6 integrable representations of SU(3) at
level 2. The actual E₆ level-2 computation has a DIFFERENT number
of integrable representations and a DIFFERENT modular data set.
The 6 SU(3)₂ reps correspond to the principal SL(2) blocks of the
27 only in a rough sense — the exact correspondence requires the
branching rules through the chain E₆ ⊃ SU(3)_principal.

**CC's task:** Repeat the computation using the exact E₆ level-2
S and T matrices (banked in the B589/B598 machinery). Compute
W[i,i] for each integrable rep of E₆ at level 2. Check whether:
(a) all diagonal moduli are equal, (b) the cross-couplings take
two values, (c) the ratio of those values is φ.

If the E₆ result DIFFERS from SU(3)₂: the proxy was misleading.
Document and close the SU(3)₂ result as proxy-only.

If the E₆ result AGREES: the portal structure is real at E₆ level 2.
Proceed to Wave 2.

### Caveat 2: The block identification

The identification "trivial rep (0,0) of SU(3)₂ = the V₀ singlet
block of the 27" assumes the principal SL(2) block decomposition
27 = V₁₆ ⊕ V₈ ⊕ V₀ maps cleanly to the SU(3)₂ weight
decomposition. Specifically: V₀ (dim 1) should correspond to the
(0,0) weight, V₈ (dim 9) should correspond to certain weights,
and V₁₆ (dim 17) to others.

**CC's task:** Using the explicit principal SL(2) embedding
(banked in B575), compute which SU(3)₂ integrable representations
correspond to which blocks. Specifically: the highest weight of V₀
is the zero weight. Under the branching E₆ → SU(3)_principal:
which E₆ level-2 integrable rep contains the zero-weight state?
That rep IS the singlet. If it's not (0,0): the identification
is wrong and the portal computation used the wrong diagonal entry.

### Caveat 3: Is the portal ratio universal or knot-specific?

The ratio φ might be FORCED by SU(3)₂ representation theory
(unitarity + charge conjugation symmetry + golden eigenvalue of
the monodromy) rather than by the specific knot. If so: every
once-punctured-torus bundle gives ratio φ at SU(3)₂. That's still
structural, but it's representation-theory, not knot-theory.

**CC2's task:** Compute the same weld diagonal and cross-couplings
for the SILVER word (R²L monodromy) at SU(3)₂ level 2. If the
silver portal ratio is ALSO φ: the ratio is universal
(representation-forced, not knot-specific). If it's DIFFERENT
(perhaps 1+√2, the silver ratio): the ratio is knot-specific
(K020 again — form forced, value chosen).

This test uses only the banked B238 code with a different monodromy
matrix. Minutes of computation.

---

## THE FULL WAVE 1 TASK LIST

### Quick lookups (hours, using banked data)

**W1.1 — CC: The E₆ level-2 singlet hearing.**
Repeat Chat-1's computation on the exact E₆ level-2 modular data.
The weld operator on the full E₆₂ integrable representation space.
Report: the diagonal moduli, the cross-coupling moduli, whether
they take two values, and the ratio.

**W1.2 — CC: The block identification.**
Using B575's principal SL(2) embedding, determine which E₆ level-2
integrable rep contains the V₀ = trivial = singlet component.
Verify or refute the (0,0) identification.

**W1.3 — CC2: The silver portal ratio.**
Compute the SU(3)₂ weld for the silver monodromy R²L = [[3,2],[1,1]].
Report the portal cross-coupling moduli and their ratio. Compare
to the golden result (ratio φ).

**W1.4 — CC: The dark level decomposition at κ = 5.**
Decompose the golden-stage partition function Z₂ into V₀ and
(V₁₆ ⊕ V₈) contributions. Using the V₀ projector on the modular
data: Z₂^(dark) = tr(W · P₀) and Z₂^(visible) = tr(W) − Z₂^(dark).
Report both values. Check: Z₂^(dark) + Z₂^(visible) = Z₂ (banked).

### Portal computation (one session, after W1.1-W1.2 pass)

**W1.5 — CC: The cup product H⁰(D; 27) ⊗ H¹(D; 27) → H¹(D; 27).**
The dark portal at the classical-cohomology level on the mirror-
double. Using the Fox calculus on the double (B637's machinery).
The invariant section (the H⁰ generator) acts on each H¹ class
through the cup product with 27-valued coefficients.

Report: the 5-component portal vector (one number per H¹ class
of the double), exact in ℚ(√-3). Coboundary-invariance control
(the cup product must be representative-independent).

Gate: if W1.1 or W1.2 FAILS (the E₆ result contradicts SU(3)₂,
or the block identification is wrong): W1.5 still runs (it's
independent of the modular data — it uses Fox calculus on the
fundamental group). But its INTERPRETATION changes: the portal
is a classical-cohomology object regardless of the quantum hearing.

### Controls

**C1:** The trivial-coefficient cup product H⁰(D; ℂ) ⊗ H¹(D; ℂ) → H¹(D; ℂ)
must reproduce the known topology of the double.

**C2:** Coboundary invariance of the cup product (shift a representative
by a coboundary, check the product doesn't change).

**C3:** Silver comparison (CC2 runs W1.5 on the silver double in
parallel). Same shape, different values = K020 confirmed at the
portal level.

---

## WHAT WAVE 1 DECIDES

**If the E₆ portal exists (W1.1 confirms nonzero cross-couplings)
AND the ratio is φ (or another specific algebraic number):**
→ Proceed to Wave 2 (Target D: boundary mediation, and Target E:
silver dark sector in full). The dark sector campaign has a discovery.

**If the E₆ portal exists but the ratio is NOT φ (SU(3)₂ proxy
was misleading):**
→ Proceed to Wave 2 with the CORRECT ratio. The portal exists but
has different structure than the proxy suggested. Still a discovery.

**If the E₆ portal is ZERO (the singlet decouples at E₆ level 2):**
→ Check at other levels (k = 3, 4, 5). If zero at all levels:
the dark sector is quantumly deaf despite being topologically
present (h⁰ = 1). Bank the null. The dark sector exists but
doesn't interact through the quantum hearing. Still informative —
it predicts truly non-interacting dark matter, which constrains
direct detection experiments.

**If the block identification is wrong (W1.2 finds the singlet
is NOT the (0,0) rep):**
→ Redo Chat-1's computation with the correct identification.
The portal might still exist with a different diagonal entry.
Not a campaign failure — a correction.

---

## ADAPTIVE PROTOCOL

At the end of Wave 1, the executing seat writes a REDIRECT NOTE:
"given what we found, should Wave 2 change?" If the portal ratio
turns out to be representation-forced (universal across knots):
Wave 2 shifts focus from K020 testing to the boundary mediation
question (is the portal a boundary phenomenon?). If the ratio is
knot-specific: Wave 2 prioritizes the silver full computation.

Seats have tactical freedom within Wave 1 (choosing methods, adding
controls, extending checks) without director approval. Strategic
changes (new targets, dropped targets, SM comparisons) require
the redirect note and director approval.

Gate 5 stands throughout. No SM-facing comparison without a
sealed design. The dark sector campaign computes INTERNAL structure.
Any comparison to measured dark matter properties requires a
separate sealed design approved by the director.

---

## THE QUESTION IN ONE SENTENCE

Does the figure-eight knot complement's E₆ quantum theory have a
dark sector that interacts with its visible sector, and if so, is
the interaction golden?

Wave 1 answers this. Start with W1.1 (the E₆ verification). If it
confirms: the dark sector is alive and the rest follows. If it
refutes: the SU(3)₂ proxy was misleading and we report the honest
correction.

The object was asked. It answered at the SU(3)₂ level. Now we check
whether E₆ agrees.
