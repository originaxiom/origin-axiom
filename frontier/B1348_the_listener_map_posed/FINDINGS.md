# B1348 — THE LISTENER MAP, POSED AND HALF-DECIDED: existence YES, uniqueness NO, and the freedom is exactly 12

**Date:** 2026-09-13 · **Seat:** cc · **Lane:** MATHEMATICS (the crossing door, L166).
**Depends on:** B238 (the SU(3)₂ modular data), B1011 (the instrument, `ρ₆ = χ⊗V₂(2I) ⊕ V₂(2T)⊗V₂(2I)`),
B641/B856 (the five-tone law and its ear-independence), B1040 (the template/selection discriminant),
B1066 (*"the listener map named as the sole residual door"*), `docs/LISTENER_MAP_SPEC.md` (L166).
**P0:** this answers the spec's **§1.2 existence** and **§1.3 uniqueness** questions. It does **not**
pay I-13, and it performs **no** value comparison — `F2` is absolute and is kept.

---

## What the spec asked, and what had been done

> *"DOES A NONEMPTY, NON-VACUOUS Λ EXIST AT ALL — some rule, stated purely in the domain data, that
> **excludes at least one candidate unit direction** … without referencing u₃/u₆'s numeric
> coordinates or any measured value?"*
>
> Two admissible outcomes: a **POSITIVE CONSTRUCTION** (*"u = the unit direction fixed, up to phase,
> by [a named stabilizer inside 2T×2I or Gal]"*) or a **STRUCTURAL NO** (*"no field-fixed point …
> the u-choice is intrinsically a SELECTION"*). **"Neither has been attempted on THIS instrument."**

## The instrument, rebuilt from scratch (controls first)

Not inherited from B1011 — rebuilt from Kac–Peterson and then compared:

| control | result |
|---|---|
| `S` unitary and symmetric | ✔ |
| `(ST)³ = S²` | ✔ |
| `C = S²` is charge conjugation `(a,b) ↦ (b,a)` | ✔ — fixes `(0,0)`, `(1,1)`; swaps the two pairs |
| **`\|⟨R,L⟩\| = 2880 = \|2T × 2I\|`** | ✔ — **B1011 C1 reproduced independently** |
| `C` central, so its eigenspaces are invariant | ✔ |
| the θ-grading `ℂ⁶ = ℂ²_odd ⊕ ℂ⁴_even` | ✔ — eigenvalues `(−1,−1,+1,+1,+1,+1)` |
| `det` on the odd plane | `ω^±1` — confirming χ's **order 3** |
| **the projective image on the odd plane is `A₅` (order 60)** | ✔ |
| **ℂ²_odd is irreducible** (no common eigenvector of `R`, `L`) | ✔ |
| the exceptional orbits on `ℂP¹_odd` | **exactly `[12, 20, 30]`** — the icosahedral signature |

## EXISTENCE — POSITIVE

Because `ℂ²_odd` is irreducible, **no point of `ℂP¹_odd` is fixed by the whole group**, so the
"fixed by all of `⟨R,L⟩`" form of Λ is dead. But the spec asks only for a rule that **excludes**
candidates, and one exists:

> ### Λ : the directions whose stabilizer in the projective image is of **maximal order 5** — equivalently, the **12-element vertex orbit** of the icosahedral action on `ℂP¹_odd`.

Stated in domain data alone (the group `2T × 2I` and the θ-grading), referencing no coordinate of
u₃/u₆ and no measured value. It cuts a **continuum** down to **12**.

**And a sharper fact, which is not imposed:** the odd plane's **canonical weight basis** —
`f₁ = e₍₀,₁₎ − e₍₁,₀₎` and `f₂ = e₍₀,₂₎ − e₍₂,₀₎`, rational in the weight basis — consists of **two
vertices**. Both have `|Stab| = 5`; the stabilizer is **cyclic of order 5**, a generator exhibited.

**AC4′ (the bench repair's replacement gate) is SATISFIED.** The discriminating quantity is `|Stab|`
on `ℂP¹_odd`; the two-direction witness is `f₁ ↦ 5` against `f₁+f₂ ↦ 1`; and Λ's value is **pinned by
the construction, not chosen**. A random control direction gives `1`. *(AC4 — the five tones — was
**demoted** by the bench repair as non-discriminating, and was deliberately not used as a gate.)*

## UNIQUENESS — NEGATIVE, and structurally

`A₅` acts **transitively** on the 12 vertices. Verified: **five** group elements carry `f₁` to `f₂`.
Therefore:

> **No rule stated in the group alone can single out one vertex.** The two canonical weight
> directions are related by a group element, so even "the direction from the fundamental-weight pair"
> is a choice among group-conjugate alternatives.

This is **B1040's shape** — the u-choice is a SELECTION, not a template — **but now with a number on
it.**

## THE PAYLOAD

> **The listener freedom was an unbounded continuum. It is a set of size 12.** The obstruction to
> cutting further is the transitivity of `A₅`, which is a theorem, not a gap in the search.

Both of the spec's outcomes turned out to be *partly* right, which the spec's own framing allowed:
existence is positive, uniqueness is negative, and the residual freedom is finite and counted.

## FENCES, kept

* **`F2` is absolute and untouched.** Nothing here compares Λ's output to anything. The value-contact
  surface stays closed; re-posing it needs a wholly new arc, a new seal, and the full `R1–R11`.
* **I-13 is NOT paid.** This builds the classification the spec asked to be *posed*. The crossing —
  u constructed from field data, sealed, then compared — remains unpaid and is a separate act (`G9`).
* **`G8` is now half-answered**: the structural no-go does **not** hold at the existence level (a
  non-vacuous Λ exists); it **does** hold at the uniqueness level (transitivity).

## HONEST SCOPE ON METHOD — an owed exactification

The verdict rests on **integers** — stabilizer orders `5` and `1`, orbit size `12`, group order `60`,
the `[12,20,30]` signature — which double precision determines reliably, each cross-checked against
B1011's banked `2880` and against controls that must and do come out generic. **But the spec's own
bar is exact `ℚ(ζ₆₀)` arithmetic with "no float in the verdict line," and this computation is float
with integer-valued outputs. The exact re-derivation is OWED**, and is registered as such rather
than implied.

**Withdrawn before banking:** an attempt to factor the orbit polynomials over ℚ (to locate
Galois-fixed points directly) produced degrees `[1,2,4,4]` and `[2,4,8,8,8]`, but its orbit
decomposition was numerically unstable — it split the 20-orbit and reported five spurious 60s
against step 2's correct `[12,20,30]`. **That result is not banked and no conclusion rests on it.**
The Galois question at the point level therefore remains open; what is established here is the
group-theoretic count, which does not need it.
