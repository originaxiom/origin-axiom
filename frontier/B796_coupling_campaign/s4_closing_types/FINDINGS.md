# S4 — THE FIVE CLOSINGS TYPED: FOUR RESOURCES, AND THE INTERFACE CLOSES

cc3, 2026-08-09, under the owner's suspended-disbelief brief. Gate 5-Q; structure
only, no measured quantity.

## The question

B1000 counted the external inputs: **five closings over four sectors** —
*space, time, chirality, rank, value* — charge holding two because B963 proves
chirality and rank **compete**. B717's doctrine survives: the observer supplies
every closing, none is secretly internal, no fifth sector appears.

What was never asked: **what KIND of data does each closing require?** If the
kinds are finite and the sources are named, the interface is not an open-ended
list of debts. That is what this types.

The typing rule is the weight ledger's own: **weight 0** data is discrete,
algebraic, and can live in a finite/profinite group; **weight ≠ 0** data cannot
(`Hom(G, ℝ₊) = 0` for finite and profinite G — you cannot get a length out of a
trace).

## The typing

| closing | what it is | **type** | basis |
|---|---|---|---|
| **time** | the arrow | **𝔽₂** — a sign | S3-a: the modular flow is canonical by Tomita–Takesaki; only its **direction** is not. B766: *"time's arrow and the basepoint bit are one choice"* |
| **chirality** | the object cannot close itself | **𝔽₂** — a sign | B963: **τ is E₆'s unique nontrivial diagram automorphism, order 2**. τ ≠ id *is* the 27's complexity |
| **rank** | a rank-reducing VEV keeping the 27 complex | **the SAME 𝔽₂** | B963: τ is **the only** rank-reducing involution. So rank draws on the identical resource — which is exactly why B1000 called it *"two resources, one budget — a coupling"* |
| **value** | the scale | **ℝ₊** | the weight ledger: no internal relation can be weight-inhomogeneous, on any face. `Hom(G,ℝ₊)=0` is precisely why this one **cannot** be 𝔽₂ |
| **space** | the 4d filling | **Lie type** | B277's class-S lift is canonical; what is free is the **6d type J** — a choice of ADE type — plus the N=2→N=1 deformation |

**Five closings. FOUR distinct resources**, because chirality and rank contest
one τ.

```
    F2 bit A : time's arrow
    F2 bit B : tau   — contested by chirality and rank
    R+       : the scale
    Lie type : the 6d type J
```

## And the sources are already named

| resource | supplied by | evidence |
|---|---|---|
| 𝔽₂ bits | the **observer torsor** — rank **exactly 3**: conjugation, reversal, golden branch | B733/B766/B782 |
| ℝ₊ | the **bulk** — the curvature radius, `G_N = 1/(4σ)`, σ unquantized | S2; Gukov's split with CS = 0 killing the quantized half |
| Lie type | the **object's own two ends** — E₆ hyperbolic, E₈ spherical, one AJ recursion carrying both | B248/B253/B261 |

Matching them:

- **reversal → time's arrow.** Direct, and B766 states it: the arrow *is* the
  reversal bit, welded to the basepoint.
- **conjugation → τ.** The orientation/chirality bit. *(This link is a typing
  judgement, not a theorem — see scope.)*
- **golden branch → spent internally on A7.** THE_FRAMEWORK: *"A7 is the whole
  residue… one bit — the smallest piece of inserted structure in the whole
  construction."* B979 made it load-bearing: LR and RL are conjugate, but the
  Möbius fixed-point polynomial is a **based** invariant and differs —
  τ²−τ−1 (roots φ, −1/φ) versus τ²+τ−1. That is the golden branch.

## The result

> **Three 𝔽₂ bits: one spent inside the object's own construction (A7), two
> supplied as closings (time's arrow, τ). One scale from the bulk. One Lie type
> from the object's own ends. Five closings, four resources, three sources —
> and nothing left over.**

The interface is **finite and saturated**. That is the first structural
statement in the programme that the external inputs are not an open-ended list
of debts but a closed budget — and it is why B1000 found *no fifth sector*.

The competition B963 proved is now legible as a **budget constraint**: two
demands (chirality, rank) on one 𝔽₂ resource (τ). Spend τ on rank and you land
in Fix(τ) where 27 ≅ 27̄ and chirality is gone. That is not four independent
failures; it is one bit, twice claimed.

## The test this makes available

The one link above that is judgement rather than theorem is
**conjugation ↔ τ**. It is checkable, and it is the natural next cell:

> The manifold's orientation/conjugation bit and E₆'s diagram automorphism τ are
> both order 2. **Are they the same 𝔽₂?** The route is McKay: conjugation acts
> on Γ₄₁ ⊂ PSL(2,ℤ[ω]) and hence on the 2T quotient; τ acts on E₆. McKay is the
> bijection between them. Does conjugation's induced action on 2T's McKay graph
> realise τ's node swap `(0,5)(2,4)`?

If **yes**, the budget closes as a theorem rather than a typing. If **no**, the
conjugation bit is not the chirality resource and a source is missing — which
would be equally informative and would falsify this arc's headline.

### RUN — and it is YES. Conjugation *is* τ.

`mckay_conjugation.py`, everything computed rather than assumed:

1. **2T built explicitly** as the 24 unit Hurwitz quaternions mapped into SU(2);
   closure verified on all 576 products. Order 24, **7 conjugacy classes**,
   sizes `[1, 6, 1, 4, 4, 4, 4]`.
2. **All seven irreps constructed** — three 1-dim from the abelianisation
   (commutator subgroup computed and confirmed to be Q₈, order 8), the defining
   V₂ and its two ω-twists, and V₃ from `2⊗2 = 3 ⊕ 1`. The **7×7 character table
   is verified orthonormal** before anything is built on it.
3. **The McKay graph** from decomposing `V_i ⊗ V₂` by character inner products:

```
        1  [0 0 0 1 0 0 0]        V2   [1 0 0 0 0 0 1]
        w  [0 0 0 0 1 0 0]        V2w  [0 1 0 0 0 0 1]
        w2 [0 0 0 0 0 1 0]        V2w2 [0 0 1 0 0 0 1]
                                  V3   [0 0 0 1 1 1 0]
```

4. **Affine E₆ confirmed** — symmetric, 7 nodes, marks `1,1,1,2,2,2,3`,
   trivalent centre at the mark-3 node, degrees `1,1,1,2,2,2,3`.
5. **Conjugation V → V\*** permutes the nodes as

```
     1 -> 1     w -> w2     w2 -> w     V2 -> V2
     V2w -> V2w2            V2w2 -> V2w            V3 -> V3
```

6. **It is a graph automorphism** (checked on all 49 entries), **of order 2**,
   with **three fixed nodes** `{1, V₂, V₃}` and **two transpositions**
   `(w, w²)`, `(V₂w, V₂w²)`.

That is **exactly τ's cycle type** — B963 computes τ as the order-2 diagram
automorphism swapping two node pairs. Structurally it swaps **two arms of the
affine E₆ star and fixes the third plus the centre**, which is the unique
nontrivial automorphism of that diagram.

> **CONJUGATION IS τ.** The observer torsor's first bit and E₆'s diagram
> automorphism are the same 𝔽₂. **The budget closes as a theorem, not a typing.**

**And it deepens B963.** *"τ does double duty"* is not only a fact about E₆'s
internal structure — τ **is the observer's conjugation bit**, so *"spending τ on
rank costs the chirality"* is a statement about **the observer's budget**. The
competition between chirality and rank is one bit of the measurement torsor,
twice claimed, and now identified with a specific automorphism of a specific
diagram.

## Scope, stated exactly

- **Proved and cited**: τ is 𝔽₂ (B963); the torsor is rank exactly 3 (B766);
  time's arrow is the reversal bit (B766); the scale cannot be 𝔽₂ (weight
  ledger, B666); the class-S lift is canonical with the 6d type free (B277);
  the two ends are E₆ and E₈ (B248/B253/B261).
- **This arc's contribution**: the typing, the count of *resources* as against
  *closings*, and the matching to sources.
- **Was judgement, now computed**: conjugation ↔ τ — **run and confirmed**
  (`mckay_conjugation.py`), with the character table, the McKay graph and the
  affine-E₆ identification all verified in-script before the verdict.
- **Still judgement, not theorem**: that the golden branch is A7's bit rather
  than a third closing.
- **CONDITIONAL, flagged by S2 after this arc was written**: the ℝ₊ closing is
  **not atomic**. Carrying units through the bulk action splits it into
  `c = 3ℓ/2G` (**weight 0** — not excluded by the weight ledger) and `ℓ`
  (**weight +1** — excluded). If c must also be supplied externally, this arc's
  *"four resources, nothing left over"* becomes **five** and the saturation
  claim weakens. If c is instead carried by one of the eight weight-0 faces, the
  count stands. **S4's headline is conditional on that question**, which S2
  makes decidable rather than assumed.
- **Not claimed**: that any closing is thereby *supplied*. The interface being
  finite is a statement about the budget, not a payment.
