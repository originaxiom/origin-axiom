# B1341 — THE OBJECT'S OWN LEAST-ACTION PRINCIPLE, AND WHY IT EXISTS ONLY AT THE DOUBLE TICK

**Date:** 2026-09-12 · **Seat:** cc (this bench) · **Lane:** MATHEMATICS (dynamics layer).
**Depends on:** B21 (the Poisson structure), B37 (the feedback quarantine), B1248 (the object's κ),
B160/B177 (the trace map's regime).
**P0 — the quantifier, stated before computing:** this computes over the **trace map on the SL₂
character variety**, the discrete dynamics the object actually has. It is **not** a 4d Lorentzian
field action, and TOE-ledger row 4 asks for one. Conclusions bank at the dynamics layer.

---

## The order

> *"can we maybe at this point … try to solve other remaining rows, such as action and dynamics? I
> wonder if phenomena that are foundational to the program such as feedback mechanisms … least
> action … got lost or cut at some point."*

This arc **attempts** the row instead of reporting its status, and answers the "lost or cut"
question by measurement.

## 1. What the sweep found: nothing was cut, and nothing was joined

`already_banked` over the named roles, on a corpus of 1300+ arcs:

| term | corpus hits | settled arcs |
|---|---|---|
| `feedback` | **4** | B20, B37 — both *quarantine* arcs |
| `least action` | 135 | **0** joining it to the trace map |
| `product` | 74 | **0** |
| `shadow` | 29 | **0** |
| `qualia` | 4 | 1 (B1169, OPEN) |

**Feedback was not lost and not cut.** B37 gave it an operational definition, *measured* that the
trace map has feedback **and** an invariant, found it fails a stronger self-model criterion, and
fenced only the **awareness** reading. The mechanism was left on the table. B21 separately banked
that *"the half-step trace map is anti-Poisson and its square is Poisson."* **Nothing in the corpus
joins B21 to least action.** That join is this arc.

## 2. B21 recomputed, not taken on trust

`verification/b1341_least_action.py`, six pre-registered questions, all PASS.

* Fricke–Vogt `I = x² + y² + z² − 2xyz − 1` is invariant under `T(x,y,z) = (z, x, 2xz − y)` ✓
* **det(DT) = −1**, **det(D(T²)) = +1** ✓ — B21 reproduced from scratch
* and the bracket itself flips: `{x,y} = 2z − 2xy` transports to minus itself ✓

## 3. THE THEOREM — the object's tick admits no action principle

> A discrete Lagrangian `L(a,b)` generates, through the discrete Euler–Lagrange equation
> `∂₂L(a,b) + ∂₁L(b,c) = 0`, a map that **always** preserves `ω = ∂₁∂₂L · da ∧ db`. Preserving a
> 2-form forces determinant **+1**. An orientation-**reversing** map of a surface preserves no area
> form at all. **Therefore an anti-symplectic map has no discrete Lagrangian.**

Confirmed independently by exhaustive solve: over the general quadratic ansatz the DEL relation is
always `q(a + c) + 2(p+r)b = 0` — `a` and `c` enter with the **same** coefficient — while the
recursion needs them **opposite**. No solution.

**And the theorem reaches the object.** Q6e: `T` pulls the invariant (Gelfand–Leray) area form
`ω = dx ∧ dy / I_z` back to **−ω** on *every* leaf, not just the one where the map linearises. So:

> **The object's fundamental tick is anti-variational. There is no action whose stationarity gives
> it. The first step that has one is the double tick.**

This is a *derived* statement about the object, not an imported one.

## 4. The genesis carries the same bit

The paper's genesis paragraph: *"the golden morphism is `L·P`, and **orientation squares it** to
`LR`"*, and *"the genesis's one bit is the swap's placement inside the tick."*

| object | matrix | det | trace |
|---|---|---|---|
| `L` (the shear) | `[[1,1],[0,1]]` | **+1** | 2 |
| `P` (the swap) | `[[0,1],[1,0]]` | **−1** | 0 |
| `L·P` (the genesis morphism) | `[[1,1],[1,0]]` | **−1** | **1** |
| the trace map's half step, linearised | `[[0,1],[1,1]]` | **−1** | **1** |

Same determinant **and** same trace — characteristic polynomial `λ² − λ − 1`, the golden. **These
are one mechanism, not two coincidences.** The genesis morphism is orientation-reversing *because it
carries the swap*; the trace map inherits exactly that, which is why its half step is anti-Poisson;
and the same squaring repairs both.

**So the record's one genesis bit and the record's dynamical obstruction are the same object**, and
the object itself says why the physical step is the double tick: it is the first orientation-
preserving one, hence the first one with an action.

## 5. The action, and the scope correction that nearly went unnoticed

On the leaf `I = 0` the map linearises (`x = cosh t` ⇒ `t_{n+1} = t_n + t_{n−1}`, the Fibonacci
recursion), the double step is `[[1,1],[1,2]]`, and its generating function is

> **`S(u, U) = u²/2 − uU + U²`**

verified to reproduce the map exactly.

**But the object is not on that leaf.** B1248 gives the once-punctured-torus fibre of `m004` the
parabolic commutator **κ = −2**; the two corpus conventions relate as `I = (κ − 2)/4`, so the
object's leaf is **`I = −1`**. Q2's linearisation *fails* there (checked, not assumed), and the
explicit `S` above does **not** apply to the object.

**What the object's leaf is, instead:** `x² + y² + z² = 2xyz`, which under `x = 3α/2` is **Markov's
`α² + β² + γ² = 3αβγ`**. The object's phase space is **the Markov surface**, and the trace map on it
is the Vieta/Markov move.

That is worth naming on its own. The paper invokes Markov for the **selection of the parameter** —
Hurwitz extremality whose second value `2√2` is Markov's, "the Markov root", "the least real
quadratic discriminant". Here the *same* Markov surface appears as the **phase space of the
object's dynamics**. Two roles for one object, and the corpus never joined them either.

## 6. What this does and does not move

**Moves.** TOE row 4 read *"input, not derived"*, and the chain status row 14 read *"the 4d dynamics
is absent."* Both are still true of the **4d** action. What is no longer true is that the object
supplies no variational structure: it supplies one, at the double tick, with a derived obstruction
explaining why not at the single tick — and the obstruction is the record's own genesis bit.

**Does not move.** One degree of freedom on a surface is not a field theory. There is no Lorentzian
signature here, no locality, no propagator. Anyone reading this as "the action is derived" is reading
it wrong; row 4's requirement is untouched.

**The honest summary:** *the object has an action for its own dynamics, provably only at the double
step, and the reason is the bit the paper already names at the genesis.*

## 7. The answer to "were feedback and least action cut?"

Neither was cut. **Feedback** was defined, measured, and fenced at the awareness reading — and the
mechanism then went unused for 1300 arcs. **Least action** was never asked about at all, though the
fact that settles it (B21) has been banked since the twenties. The failure mode is not deletion; it
is **two banked facts sitting eleven hundred arcs apart with nothing joining them** — the same
mechanism B1338 measured in the anti-rediscovery instrument and B1339 in the chain status.

---

# ADDENDUM (same day, before the arc was a day old) — TWO OF THE FIVE FINDINGS ARE B448'S, AND THE HEADLINE GETS BETTER

**This bench rediscovered banked water and is correcting the arc rather than leaving the claim
standing.** §5's Markov identification and §4's det-−1 echo are **not new**. Both are in **B448**
(the heartbeat adjudication), banked long before this arc.

## What B448 already had, verified here against its own text

B448's verdict line: *"the exact T₁ periodic-orbit field tower on the cusp locus **kappa=-2 (the
Markov surface)**."* Its Part C:

> *"The classical anchor: κ=−2 **is the Markov surface** (`x²+y²+z² = xyz`; scaling x=3a gives the
> Markov equation `a²+b²+c²=3abc` … the integer T₁-orbit of (3,3,3) walks the Markov tree).
> **Classical territory — a credibility anchor, no novelty claimed.**"*
>
> *"T₁ itself is the **half-monodromy**: `T₁² = L∘R` verified; the half corresponds to the
> **det-−1** Fibonacci matrix `C=[[1,1],[1,0]]`, `C² = A`."*

Checked on this bench: B448's `T₁(x,y,z) = (z, x, xz−y)` and B37's `T(x,y,z) = (z, x, 2xz−y)` are
**one map** under the half-trace rescaling (`2·T(x,y,z) = T₁(2x,2y,2z)` exactly); `det(DT₁) = −1`,
`det(D(T₁²)) = +1`; and **`C = L·P` identically**, with `C² = L·R`. So B448's "det-−1 half-monodromy"
and this arc's "genesis morphism `L·P`" are **the same matrix**, and B448 got there first.

**Corrections to the arc above:**

* §5's *"the corpus never joined those either"* is **WRONG** and is withdrawn. B448 joined them, and
  explicitly claimed no novelty for it because it is classical.
* §4's det/trace table stands as arithmetic but **is not this arc's finding**. Credit: B448.
* §1's table should read: the roles were not un-joined; **this reader failed to read the join.**

## The process failure, recorded against B1338

The pre-flight sweep **worked**. `already_banked --wide "Markov surface trace map leaf phase space"`
returned **B448 as the top hit, 6 of 7 terms**. What it printed beside it was the FINDINGS **title**
— *"the heartbeat adjudication: two handoffs, one exact orbit-field tower"* — which does not contain
the word Markov. The **verdict line** does, in its first sentence. **This bench read the title and
moved on.**

So B1338's finding needs a sibling: the instrument's blind spots were the subject there; here the
instrument was not blind and **the reader was**. The concrete defect is that `already_banked` prints
a FINDINGS row's *first heading* and a SETTLED row's *claim line*, and B448 matched on the FINDINGS
surface, so its claim line — the one carrying "Markov surface" — was never shown. **Registered as a
fix for the instrument: for a FINDINGS-surface hit, print the arc's `claim_one_line` too.**

## What actually survives as this arc's own

1. **The theorem (§3).** A discrete Lagrangian's Euler–Lagrange map preserves `ω = ∂₁∂₂L·da∧db`,
   hence has determinant +1; an orientation-reversing map of a surface preserves no area form; so
   **an anti-symplectic map has no discrete Lagrangian.** B21 banked the anti-Poisson fact and B448
   banked the det −1; **neither drew this consequence, and nothing in the corpus does.**
2. **The leaf-level form (Q6e).** `T*ω = −ω` for the invariant Gelfand–Leray form on **every** leaf —
   which is what makes the theorem reach the object rather than only the leaf where the map
   linearises.
3. **The join, which is the real result and is better than what was banked above.**

## THE SHARPENED HEADLINE: the double tick is not a choice — it IS the monodromy

B448 verified that **`T₁` is the half-monodromy and the figure-eight monodromy is `T₁²`**. This arc
proves that **`T₁` has no action principle and `T₁²` does.** Put together:

> **The object's action exists exactly at its monodromy, and fails exactly at the formal square root
> of the monodromy.**

The "double tick" was never a modelling choice or a convenience. `T₁` is not a thing the object does
— it is a square root of the thing the object does, and it is precisely that square root which is
anti-variational. The geometrically real map — the monodromy of the figure-eight bundle — is the one
with a least-action principle.

And the record now has **three independent reasons the physical step is the double one**, which is
the part no single arc had:

| reason | where |
|---|---|
| **orientation** — `L·P` carries the swap, det −1; squaring restores it | the paper's genesis paragraph |
| **geometry** — `T₁` is the half-monodromy; the monodromy is `T₁² = L∘R` | **B448** |
| **variational** — `T₁` is generated by no Lagrangian; `T₁²` is | **this arc** |

Three faces of one det = −1. The arc's verdict stays **PROVED**, on the theorem and this join; the
Markov and det-−1 observations are re-credited to B448 and claimed by nobody here.
