# xB015 — PREREGISTRATION (sealed before the verification code exists)

**Seat `xb`, `sep16-branch`, 2026-09-17. Sealed, hashed and pushed before any cell of this arc's
`verification/` runs.**

## P0

Hyperbolic geometry, Chern–Simons invariants, commensurability. Named mathematics. No value, no
generation count, no physics reading, nothing to `CLAIMS.md`. Gate 5 absolute.

## Why this arc exists — the owner's instruction, verbatim

> *"it still doesn't cross B1012's wall, which is about a dimensionful quantity while a ladder gives
> a dimensionless index. — lets verify it for mistakes, and investigate it priperly so we squeze the
> real lead out of it"*

The quoted sentence is **mine**, written into `xB014`'s verdict twice. The owner did not accept it
and asked for it to be checked. This arc checks it.

## DISCLOSURE — what was already computed before this seal

**This is not a blind arc and must not be read as one.** Before writing this file the seat ran
exploratory computations that produced the numbers K2, K3, K5, K6 and K8 below now predict. That
exploration is *why* the predictions are sharp. The seal's honesty therefore rests on two things,
not on blindness:

1. **Every exploratory number is re-derived by the committed `verification/` code from scratch**,
   with its own controls; nothing is carried across by hand.
2. **The kill conditions below are binding and were written down before the confirmatory run.**
   A cell that misses its stated prediction kills the cell, and K7 is preregistered to be reported
   as a NEGATIVE whatever this seat would prefer.

The one genuinely blind cell is **K7** — whether any of this crosses the wall. Its prior is stated
below and it is expected to fail.

## The sweep, done first (xB010's rule)

Read, not cited:

* **B1012** — the wall itself. `S = (t/2)ĉ + (t̄/2)ĉ̄ = −CS·k − Vol·σ`, hence **`∂S/∂k = −CS`
  identically**, and *"blind-to-k ⟺ CS = 0 ⟺ the object equals its mirror."* Its §2 closes:
  *"the closure explains why c stays free: the surviving level is the UNQUANTIZED one (σ, not k) —
  if it were k, c = 6k would be quantized, and it is not."*
* **B1015 / `DECLARATION.md`** — the sealed anchor set. **A1 = ℓ, dimensionful, and the declaration
  states in terms that no dimensionless number flows from it.** **A2 = c = 6σ**, named there as
  *"the one continuous **dimensionless** external coupling"*, and priced on the ground that *"the
  object is provably blind to the quantized level k (∂S/∂k = −CS ≡ 0, B1012), so σ is the only
  level the observer can set and the object cannot."*
* **B1088** — the action card: *"The action has **ZERO free dimensionless constants**."*
* **B303** — the cusped amphichiral object has CS = 0; every closing has CS of a definite sign.
* **B1224** — amphichirality forces CS to be **2-torsion**: `CS ∈ {0, ¼}` mod ½, six of six.
* **B1235** cell 1 — the 112-family split by chirality: **38 amphichiral, 74 chiral**; m202 and
  s118 named chiral at CS = 1/12; B1181 retracted for using `is_isometric_to`.
* **B1136** — the genericity control on m004's wins, whose table says amphichirality is
  *"shared with ALL thirteen others"* of the 14 shape-field manifolds.
* **B1186** — the family is 112 (shape field ⊆ ℚ(√−3)), t06829 the corrective member.
* **B152 / B128** — the amphichirality method gate (`is_amphicheiral` on `is_full_group`), and
  **B128's M-B, which already killed "CS ∝ #R−#L"**. Any revival of that law in this arc is a
  known-dead claim and must be reported as such.
* **B145** — *"there is no arithmetic chiral o-p-t bundle in range"*, and *"the strongest canonicity
  (arithmeticity) ⟹ amphichirality"*, scoped to o-p-t words of length 2–7.
* **xB007** — the character-variety layer is blind to exactly one datum, the ℤ/2 separating
  m003 from m004 (`det(φ_*−I) = ±1`, the −I that PSL quotients away).
* **A5** (`THE_FRAMEWORK` Layer 0) — *"the first mixed closure is torsion-free"*: the axiom that
  selects m004 over its sister.

**Nothing found in the sweep states the K6 law.** If a prior arc does state it, K6 becomes a
re-derivation and says so.

## The cells, with predictions and kill conditions

**K1 — the type of the wall.** Re-derive `S = −CS·k − Vol·σ` and `∂S/∂k = −CS` symbolically from
Gukov's split at `t = k + iσ`, `ĉ = i(Vol + i·CS)`, and re-derive the Brown–Henneaux closure
`c = 6σ`. Then classify A2.
*Prediction:* A2 is **dimensionless**, so the quoted sentence's stated ground is false.
*Kill:* if the split does not reproduce `−CS·k − Vol·σ`, or if A2 is dimensionful, the sentence
stands and this arc stops here.

**K2 — the family's CS index.** Over B1186's 112 members: is CS rational, and is `24·CS ∈ ℤ`?
*Prediction:* 112/112, with the reduced index `24·CS mod 12` **surjective onto ℤ/12**.
*Kill:* one irrational member, or an index outside `(1/24)ℤ`, or a non-surjective spectrum (then
it is a partial pattern, not an index, and must be reported as one).
*Instrument guard, declared:* `Fraction.limit_denominator(D)` with tolerance `τ` is only a rationality
test when `1/D² ≫ τ`. A large `D` with a small `τ` calls **every** float rational. Both the family
and the control must use the same sound `(D, τ)`.

**K3 — the base rate.** The same test over `OrientableCuspedCensus[:3000]` **minus** the family.
*Prediction:* < 5 %.
*Kill:* ≥ 20 % — then `24·CS ∈ ℤ` is generic and K2 means nothing.

**K4 — the mechanism, derived and not observed.** Verify CS multiplicativity under finite covers,
`CS(M̃) = n·CS(M)` mod ½, with a **non-vacuous control**: a manifold with irrational CS (m015).
Then the derivation: `CS(m004) = 0` + a common finite cover forces every commensurable manifold's
CS to be torsion, hence rational with bounded denominator.
*Kill:* any cover failing multiplicativity; or the control returning rational CS (an instrument that
rationalises everything proves nothing).

**K5 — the load-bearing commensurability step.** K4's derivation needs *"any two members share a
finite cover"*, which the family's definition (shape field ⊆ ℚ(√−3)) does **not** give for free —
it needs arithmeticity, and shape fields with large denominators (t06829: 98) are exactly where that
could fail. Test `vol/v₀ ∈ ℤ` for all 112 (necessary), with `v₀` **re-derived** from
`L(χ₋₃,2)` and not taken from the record; and **exhibit an explicit common cover with m004** for at
least three members, at least two of them chiral.
*Kill:* if no explicit common cover can be exhibited, K4's derivation is **not licensed** and K2 must
be downgraded to an empirical regularity. This must be reported, not quietly dropped.

**K6 — the bit.** For once-punctured-torus bundles, is `CS(b+-W) − CS(b++W) = ¼` mod ½ for **every**
word W?
*Prediction:* exact, at 50 digits, over every cyclically-non-constant word of length ≤ 8.
*Kill:* one mismatch. *Also required:* the failed law `CS ∝ #R−#L` must be re-run and re-killed
(B128's M-B) so that this arc cannot be read as reviving it.

**K7 — does any of this cross the wall? (the blind cell, prior: NO).** Given K1–K6, attempt to fix
`σ` or `c` from the family. *Declared prior:* **it does not.** The index is topological and
quantized; `σ` is continuous and unquantized; nothing here supplies an equation between them.
*What would count as crossing:* a derivation of a numerical value for `c` or `σ` from the family's
own data with no new input. *Preregistered reporting rule:* this cell is reported as NEGATIVE unless
such a derivation is exhibited and survives its own control. Any weaker outcome — a structural
resemblance, a matching denominator, a suggestive coincidence — is a **LEAD**, named as one, and
does not upgrade the verdict.

**K8 — the correction owed to B1136.** Recompute amphichirality over B1136's 14 under the B152 gate.
*Prediction:* B1136's *"shared with ALL thirteen others"* is **wrong**; 7 of the 14 are chiral.
*Kill:* if all 14 are amphichiral under the gate, this seat's reading is wrong and B1136 stands.

## What this arc will NOT claim

* Not that a ℤ/12 index is a physical scale.
* Not that the k-coupling is measurable, nor anything about `k`'s value.
* Not `CS ∝ #R−#L` (B128's M-B killed it; K6 re-kills it).
* Not that arithmeticity of any member is established by volume alone (K5's necessary condition is
  necessary only, and the arc says so).
* No identification (E82's class), no Gate-5 contact, nothing to `CLAIMS.md`.

## The seat's prior, declared

K1 **fails my own sentence** — I expect to be shown wrong, which is the point of the arc.
K2, K5, K6 **pass**. K3 **passes** (low). K7 **fails** — the wall stands for σ. K8 **corrects B1136**.
The arc's honest best case is a **reframing plus one correction**, not a crossing.
