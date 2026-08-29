# B1216 — THE PARAMETER-CLOSURE LOOP, RUN 1: zero rows deleted, one gate written, one regression, one refutation

**Verdict**: `OPEN` · **2026-08-29** · **Gate 5 clean** · 9 agents, ~686k subagent tokens, 20 min ·
full result archived at `workflow_result.json`

## 0. The score, stated the way the adjudicator stated it

> **Zero rows deleted. One gate written. One regression. One refutation.**

**The pre-registration was wrong, and instructively.** This bench predicted *"C3 and C1 can close;
C2 and C4 can only sharpen."* What happened: **C1 closed — negatively, and enlarged its own row.**
**C3 did not close** (it sharpened, sharply). **C2 failed adversarial review.** **C4 delivered
exactly what was predicted** — a gate, not a closure. So the one cell predicted *least* likely to
produce forward motion is the only one that did.

## 1. THE FINDING THAT MATTERS MOST — a vacuity in our own record

The C1 verifier asked that a clause be *struck* for want of a computation. **The adjudicator ran the
computation instead of striking it, and the outcome was worse than striking.**

**B1192/GC-16's supporting clause** — *"X₀ acts as the Galois generator on BOTH spectral fields, so
the class restricts to c"* — **is MB12-VACUOUS.** Re-derived here:

> For hyperbolic P ∈ SL₂(ℤ), det P = 1, so the eigenvalues are {λ, 1/λ} and **the Galois conjugate of
> λ over ℚ(tr P) is exactly 1/λ**. Any X with `XPX⁻¹ = P⁻¹` therefore carries P's λ-eigenline to
> P⁻¹'s λ-eigenline — which **is** P's own 1/λ-eigenline. **Every anti-conjugator swaps the
> eigenlines, by construction.**

Exhibited on this bench for a **det X = +1** anti-conjugator — the mirror-**even** type the record
already calls dead. **The clause has no failing branch, so it supports nothing.**

**Scope, carefully**: this removes one of GC-16's three supporting legs. **The det = −1 sign result is
untouched** — that one does discriminate, and the √2 control below confirms it.

> **This is the second MB12-vacuity in a fortnight** (after B1206's candidate iii), and **both were
> in supporting clauses rather than headlines.** That is the pattern worth naming: this seat's
> headline claims are getting checked; the sentences that *prop them up* are not.

## 2. C1 — the √3-partner is NOT canonical, at two levels

The masterplan's stated closure route for the c-bit is **refuted**. Every script re-run by the
adjudicator; all reproduce.

- **Level 1 (field)**: norm-+1 is satisfied by **30 of 37** real quadratic fields scanned (**81%**),
  and is known-infinite by standard density. **"Norm +1" is the generic condition, not a fine-tuned
  one.**
- **Level 2 (embedding) — previously unflagged in this record**: even fixing the *same* field
  (disc 12), conjugating the partner within its own GL₂(ℤ)-class while holding the object fixed
  changes the outcome — **22 of 60** reproduce the headline DIRECT(det = −1); **38** fall into a
  qualitatively different **TORSOR** regime where no integral realizer exists at all.
- **The counterexample that kills the criterion**: DIRECT(−1) is exhibited for **disc 13** — a
  genuine **norm-(−1)** field (fundamental unit 18 + 5√13), the same "self-coupling-killed" type as
  the golden. **So norm +1 is not necessary** once embedding freedom is admitted. Also disc 21 and
  disc 15.
- **The control that keeps it honest**: a 204-embedding scan of the norm-(−1) **√2** control produced
  only DIRECT(+1) or TORSOR — **never** DIRECT(−1). So the achievable sign **is** a field-specific
  invariant, but **it does not track the unit-norm dichotomy GC-2/GC-16 proposed.**

**Consequence**: "which pair" is supplied at **two** levels, neither pinned by the stated criterion.
The paper must not carry the masterplan's line *"closure means show the √3-partner is canonical."*

## 3. C3 — the ℙ³ did not close, but the question is now ONE binary lookup

**The entire fork collapses to a single external fact**: do the SU(5) components feeding the down leg
(Q via the A-slot, dᶜ via B₆) and the lepton leg (eᶜ via the A-slot, L via the same slot, sharing one
5̄-Higgs) carry the **same** internal ℤ/12 characters, or **different** ones?

- **SAME ⇒ `det Y_e ≡ det Y_d` identically** as polynomials (transpose-invariance of the
  determinant). **Zero new cut. The ledger stays at dim 1 with certainty, not merely plausibility.**
- **DIFFERENT ⇒** the lepton tensor is genuinely independent, `det Y_e` is generically an
  algebraically independent cubic, and **the ledger closes to dim 0.**

**Both branches are now proved**, which is the cell's real product: the search is no longer unbounded,
it is one lookup whose two answers have known consequences.

**AND IT CORRECTED B1215.** My tail enumeration reported the A₁₁ pure-tail pairs as {(0,4), (2,2)}
and **missed (8,8)**, which also satisfies 16 ≡ 4 (mod 12). (8,8) is likewise a repeated direction, so
it also dies by skewness. **Corrected count: 2 surviving (down) vs 1 (lepton).** B1215's *conclusion*
stands — the lepton leg has strictly fewer — but its enumeration was incomplete and is fixed here.

## 4. C2 — REFUTED by its own verifier, and the refutation is correct

The λ cell claimed a theorem-shaped exhaustion. **The adjudicator checked its sources verbatim and
they do not support it**: B850's own FINDINGS says *"Type: III₁ — CONDITIONAL on the cited
reduction"* and *"the reduction remains a DECLARED CITATION"*; B721's probe-3 output says *"There IS
a genuine 'modular flow = geometric flow' bridge in the literature."* **Both are citations, not
in-sandbox derivations, and the cell presented them as "confirmed two independent ways."**

**What survives**: ℚ(√−3) has **unit rank 0**, so its regulator is **identically 1** — that
sub-route is dead by textbook fact, not by search. And B721's Δ = I is a real in-sandbox number
(σ_t(a) − a ≈ 4.59e−41).

**What is withdrawn**: the {II₁, III₁} exhaustion, and the "excluded by TYPE" argument against
λ = r or λ = γ₅ (a finite/continuum cardinality mismatch does not rule out what was claimed).

> **λ is now worse-documented than before the run** — it carries an explicit *"exhaustion was
> attempted and failed"* mark. That is the honest state.

## 5. C4 — the only forward motion: σ gets an acceptance gate

**σ moves from *"one bridge missing, unspecified"* to *"one bridge missing, fully specified, with a
runnable pass/fail test and a documented empty candidate set."*** The missing object is named — the
graded character **χ_∂** of the AdS₃-boundary chiral algebra of T[m004] at **c = 6** — with a
six-clause kind-map: **(K1)** a named module of a named algebra at a *pre-fixed* rational c ·
**(K2)** the correct `q^{h−c/24}` prefactor, not an arbitrary shift · **(K3)** non-negative integer
coefficients after stripping the prefactor — *apply first, it kills candidates for free* ·
**(K4)** c = 6 exactly, which **is** the whole content of σ = 1 · **(K5)** the Cardy 6-vs-1
quantifier — the object supplies **one** cusp-boson unit and a candidate must say where the other
**five** live · **(K6)** it must be the object's own datum, not a WZW model whose central charge
happens to sum to 6.

The B672 coefficients were re-derived from scratch (pentagonal-number expansion) and **K3's failure
is genuine, with a non-empty pass-branch** — the gate can be passed, so it is not vacuous.

## 6. THE GOAL TEST: **NO**

| row | verdict |
|---|---|
| **ℓ** | not in scope — dimensionful, external by design, **permanent boundary, correctly typed** |
| **σ** | **PASSES** the second disjunct: named external object, stated gate, documented empty candidate set. *Not derived — but correctly bounded and testable.* |
| **λ** | **BLOCKS** — no acceptance gate exists at all, and the exhaustion attempt was refuted |
| **the ℙ³** | **BLOCKS** — bounded to an *internal, in-principle-computable* fact this bench does not hold. One lookup away is not closed. |

**Two rows block.** And outside the goal's scope, **the c-bit regressed**.

## 7. THE REPLAN, and one caveat recorded in advance

**R1 — retrieve the ℤ/12 character assignment** (ℙ³; highest leverage by a wide margin; codex holds
it). Then do **not** accept "generically independent" — compute det Y_e explicitly and test whether
it lies in the ideal generated by the λ-term functional and det Y_d (Gröbner/resultant).

> **THE CAVEAT, written before the run rather than after**: **dim 0 is a finite point set.** If the
> ℙ³ closes, the row converts from *continuous* to *finite label* — it **joins B990's already-closed
> category. It does not become a unique prediction.** Anyone quoting a future closure must quote this
> sentence with it.

**R2 — write the λ gate** (cheapest route to the stated goal: λ blocks because it is *ungated*, not
because it is unclosed; C4 proved this repo can gate a row it cannot close). **R3 — compute the
III-type rather than cite it**, or declare a permanent citation boundary; *the adjudicator predicts
the boundary, and says naming it is the result.* **R4 — the ∂M linking pairing** (σ; GC-23's
obstruction applies to the intersection pairing only, and the Poincaré–Lefschetz linking pairing was
never computed — cheap, in-sandbox, could reopen or finally kill the E₆-lattice route). **R5 —
doublet–triplet splitting as external** (cheap; makes R1's fork the only live route). **R6 — the sign
invariant as a theorem** (c-bit; lowest expected yield, highest interest).

## 8. Fences

C1's clause *"restricts to c the same way M1's does"* for disc 13/15/21 — the verifier asked for it to
be struck as uncomputed; the adjudicator **ran it and found it true, but simultaneously found it
vacuous** (§1), so it is retained as *true and non-discriminating*. C3's "sympy-verified
shape-generic" framing is confirmed as dressing — the transpose-determinant identity is fully
generic. The workflow's own outputs are archived verbatim; where this arc states a fact, it was
re-derived on this bench.
