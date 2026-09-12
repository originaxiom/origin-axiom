# B1343 — DERIVING THE OTHER ADE FACES: the derivation is free, the enrichment is not, and one bridge is closed by a theorem

**Date:** 2026-09-12 · **Seat:** cc · **Lane:** MATHEMATICS (algebra/geometry layer).
**Depends on:** B727 (the faces are one classification), B730 (the arithmetic closure), B1248
(κ = −2), B1257 (Brieskorn–Slodowy), **B1258** (2T is blind), B1341, B1342.
**P0:** this computes over `SL₂(ℤ)` conjugacy and Kodaira's classification. It establishes a
**method** and runs it on one face. It does not derive any new face, and claims no new physics.

---

## The question

> *"if our program is derived from the substitution rule, how can we derive the rest of the faces so
> we see if our principles emerge or enrich?"*

## 0. First, a correction to the forwarded survey

It lists **"singularity theory"** among the terms returning zero. **The face is in the record** — the
corpus spells it *Brieskorn–Slodowy*, *Slodowy slice*, *surface singularity*, not "singularity
theory":

* **B1257** (PROVED) — *"the Slodowy slice to a nilpotent orbit meets the nilpotent cone in
  `dim N − dim O`, and for the **subregular** orbit that is a surface singularity `ℂ²/Γ` of the same
  ADE type — for E₆, **Γ = 2T**, the very group that built E₆ by McKay."*
* **B1258** (NEGATIVE) — the follow-up, and it is the load-bearing one below.

Same failure mode as three others today: the search term and the record's spelling disagree.
`elliptic surfaces`, `Kronheimer`, `ADHM`, `Nakajima` **do** genuinely return zero — that half of the
survey holds.

## 1. Deriving them is free — which is exactly why it proves nothing

The chain is **substitution φ → abelianisation in `GL₂(ℤ)` → trace map → κ = tr[a,b] → ℚ(√−3) → 2T →
E₆ (McKay)**. Every other ADE face is a **standard functor `F` applied to the same `2T`**:

| face | the functor |
|---|---|
| Kleinian / du Val singularity | `2T ↦ ℂ²/2T`, the E₆ surface singularity |
| Kronheimer / ALE | `2T ↦` the hyperkähler minimal resolution |
| Nakajima quiver variety | `2T ↦` its McKay quiver |
| Kodaira IV\* fibre | the E₆ affine Dynkin diagram as a fibre type |
| Minahan–Nemeschansky | a D3 probe of that IV\* singularity |

So **"can we derive them" has the answer *yes, trivially*, and that is B727's fence landing**: the
faces are one classification, so none adds evidential weight for E₆. Deriving them is not the
question.

## 2. The real question, and B1258 makes it a theorem

B1258, verbatim:

> *"**2T is too small**: its eigenvalues are **12th roots of unity** and the two decompositions are
> congruent modulo exactly that."*

2T could not distinguish two candidate embeddings because its characters see only `n mod 12`.
Therefore:

> ### THE BLINDNESS INHERITANCE
> **Any face that is a functor of 2T alone inherits 2T's blindness.** It can supply a *home* — a
> 4-manifold, a `χ ≠ 0`, an SCFT — but it cannot **decide** anything 2T cannot decide.

So the owner's *"emerge or enrich"* splits cleanly:

* **emerge** — the face reproduces E₆. Always true, always free, always worthless as evidence.
* **enrich** — the face **consumes data the substitution supplies beyond 2T**.

And the substitution *does* supply more, all banked: **κ = −2** (the leaf, = the Markov surface,
B1248/B448); the **golden** `λ²−λ−1` (B1341); the **orientation bit `det = −1`** (the genesis swap);
the **specific monodromy `L·R`**; and the **stratum** (B1342: 1 of 4). **A face enriches iff it eats
one of these.** That is the test, and it is checkable per face.

## 3. Running the test on the elliptic face — the bridge is closed

The survey ranked this highest, and it genuinely returns zero in the corpus. `verification/b1343_faces.py`:

**Q1.** Every Kodaira singular-fibre monodromy is **quasi-unipotent**: `det +1` and `|trace| ≤ 2`,
verified by enumerating the classification (I_n trace 2; I\*_n trace −2; II, II\* trace 1; III, III\*
trace 0; IV, **IV\* = Ẽ₆** trace −1, order 3).

**Q2.** The object's monodromy is `L·R = [[2,1],[1,1]]`, **trace 3** — **hyperbolic (Anosov)**.
Trace and determinant are conjugacy invariants, so:

> **The object's monodromy is not conjugate to any Kodaira fibre monodromy. The obvious bridge — *the
> object's monodromy IS a degeneration* — is closed by a theorem**, the monodromy theorem itself.

**Q3.** No iterate escapes: traces of `(L·R)^k` are **3, 7, 18, 47, 123, 322, 843, 2207** — the even
Lucas numbers, the record's own tower (`|H₁(Σₙ)| = L₂ₙ − 2`, B730) — all `> 2`. The no-go survives
reparametrisation.

**Q5, the near-miss, adjudicated rather than admired.** The *half* step `L·P` has **trace 1**, which
coincides with Kodaira **II\***. But `det(L·P) = −1` against every Kodaira monodromy's `+1`, so they
are **not conjugate** — and II\* is **Ẽ₈**, not Ẽ₆, so even the coincidence points at the wrong
group. **Recorded as killed, not as a hint.**

**Q4, where the face *does* touch the object.** The IV\* monodromy has **order 3**, characteristic
polynomial `λ²+λ+1`, eigenvalue field **`ℚ(ζ₃) = ℚ(√−3)`** — *exactly* the object's own forced
**being** face (B730, closed at three). So if the elliptic face is reachable at all, it is through
the **field and the lattice**, never through the dynamics.

But the lattice `E₆ ⊂ NS(S)` **is** `F(2T)`. So by §2:

> **The elliptic face is derivable and cannot enrich.** It would supply a compact `χ = 12` home for
> E₆ — which is a genuine want (`F6 §8.4`, `χ ≠ 0`, doesn't fibre over a circle) — and **zero new
> constraint**.

## 4. The derivation map, for the other two

| face | free data beyond 2T | can it enrich? |
|---|---|---|
| **elliptic / Kodaira IV\*** | a Weierstrass model | **no** — the monodromy bridge is closed (§3); the lattice is `F(2T)` |
| **Kronheimer / ALE** | Kronheimer's theorem: ALE hyperkähler ↔ `(Γ, ζ ∈ ℝ³⊗𝔥)`. 2T fixes the diffeomorphism type; **`ζ` is the only free datum** | **possibly — and this is the one well-posed opening.** *Does the substitution supply `ζ`?* Not answered here |
| **Minahan–Nemeschansky** | the E₆ **mass parameters** (the Cartan) | **no new leverage** — those are the same Cartan the record already cannot fix (JOIN 2, 0/19) |

## 5. The answer, stated plainly

**Deriving the other faces is free and therefore evidentially empty** — that is B727, and it now has
a mechanism: they are all `F(2T)`, and **2T is blind (B1258)**, so they inherit the blindness.
*Emergence* is guaranteed and worthless; *enrichment* requires consuming `κ = −2`, the golden, the
orientation bit, the monodromy, or the stratum.

Tested on the highest-ranked candidate, the elliptic face: **the dynamical bridge is closed by a
theorem** and what remains is `F(2T)`. **One opening survives** — Kronheimer's deformation parameter
`ζ` — and it is the only one of the three where an object-specific datum has anywhere to land.

**The honest caution, unchanged from the survey:** all three are standard, well-populated literature.
Nothing here connects the figure-eight's arithmetic to them, and the one no-go computed above is
evidence that such a connection is *harder* than it looks, not easier.
