# PREREGISTRATION — is the object's su(5) real?  Testing `A`, not `Stab(s)`

**Sealed 2026-08-17, committed BEFORE compute.** Rule 1.

## THE CLAIM UNDER TEST IS MY OWN PREVIOUS RESULT

"`su(5)` is real in no real form — 254 of 254" was computed as
`Stab(s) ∩ Stab(τs)`: the τ-stability of the stabiliser of the **pure spinor alone**, a
61-dimensional algebra whose τ-stable part is `so(10)`.

**But the `su(5)` never came from `Stab(s)`.** It came from the composed object

    A = Stab(e_i, ebar_j, s)      dim 34, Killing rank 24

— two trivial-character idempotents and the ω-covariant pure spinor, in one annihilator.
**`A` was never tested for τ-stability.** 254 cases, all of a different algebra.

## WHY IT MIGHT DIFFER

`A` is cut out by three conditions, two of which are the idempotents: their coordinates lie
in the base field and they are permuted by `Gal(K) ≅ S₃`. `Stab(s)` carries no such
structure. So `A` may be τ-stable where `Stab(s)` is not.

## THE COMPUTATION

`B = A ∩ τ(A) = Stab(e_i, ebar_j, s, τe_i, τebar_j, τs)` — six conditions.
For antilinear τ, `A ∩ τ(A)` is the largest τ-stable subalgebra of `A`, and its τ-fixed
points form a real form of it. **The Killing rank of `B` is the question.**

## CONTROLS — run before anything is read

1. `A` reproduces at **(34, 24)**. If not, stop.
2. τ maps the 27 onto the 27-bar, **27 of 27**.
3. `τ(e_i)` is a genuine 27-bar rank-1 idempotent — verified by the **stabiliser-dimension 61
   gate**, not assumed.
4. `τ∘τ = id` on the objects used.

## DECLARED OUTCOMES — both live, neither preferred

| Killing rank of `B` | reading |
|---|---|
| **24** | **the `su(5)` has a real form.** `E₆ → so(10) → su(5)` closes over ℝ, chiral throughout, **ledger unchanged at four imports** — nothing new is chosen; I merely stopped testing the wrong object. Relay to cc at once, unsoftened. |
| **45** | `so(10)` again. The chirality/reality tension is **structural**: this object's chirality lives in the ω-sector (needs `√−3`) and reality symmetrises ω with ω², destroying it. That competition is then the reason it stops at rank 5, and it is a real finding. |
| anything else | reported as found, class named, no story attached. |

## THE FALSE-POSITIVE GUARD

I want the 24. That is exactly why it must be gated hardest. A rank-24 result is **not**
accepted unless: all four controls pass in the same script; it reproduces at ≥3 primes; and
the skeptic phase fails to refute it. Recall this session already produced one near-miss in
this direction — `ℚ(√77)` named from a single prime on a biased sample.

## THE FALSE-NEGATIVE GUARD

Equally: a rank-45 result is **not** accepted as "the tension is structural" until framer C
has ruled on whether `A ∩ τ(A)` is even the right notion of real points. **I have mis-framed
this question nine times**, most recently on the Baez–Schwahn item whose stated subject *was*
the class error. The test being wrong is a live hypothesis, not a formality.

## IF IT COMES OUT 24

The 254-case result is **withdrawn and re-scoped, not deleted** — it was true of `Stab(s)`
and false of `A`. The corpus already carries one true-conclusion-on-a-wrong-argument
(`B971` on orbifold projections). That pattern is not repeated silently.
