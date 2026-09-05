# B1258 — 2T CANNOT SELECT THE EMBEDDING, and neither can the SO(10) grading: two object-internal tests, both blind, one by a theorem

**Date:** 2026-09-05 · **Seat:** cc · **Status:** NEGATIVE (exact; three MB12 controls, one of which convicts this arc's own first statement of its mechanism)

## The question

**B1257** named a canonical selector: Brieskorn–Slodowy picks the **subregular** orbit uniquely, and
that is the embedding giving three chiral generations. But a canonical criterion is not the object's
say-so. **Earning I-25 requires the OBJECT to confirm it.** This arc runs the two natural
object-internal tests. **Both come back blind** — one of them provably.

## Test 1 — the 27|2T branching (B327's own gate). BLIND, and forced

| | χ on 2T's seven classes |
|---|---|
| **27**, principal *and* subregular | **(27, 27, 3, 0, 0, 0, 0)** — identical |
| **78**, principal *and* subregular | **(78, 78, −2, −3, −3, −3, −3)** — identical |

**The mechanism** (verified per modulus, not asserted):

- **λ = 1:** χ_Symⁿ = n+1, so the sum is the **dimension** — 27 (and 78) for both by construction.
- **λ = −1:** χ = (n+1)(−1)ⁿ, and **all indices are even** in both, so it is again the dimension.
- **λ of order m ∈ {3,4,6}** (2T's remaining classes): χ_Symⁿ depends **only on n mod m**, and the
  index multisets agree at every one:

| | mod 3 | mod 4 | mod 6 |
|---|---|---|---|
| principal `n = {16,8,0}` | [0,1,2] | [0,0,0] | [0,2,4] |
| subregular `n = {12,8,4}` | [0,1,2] | [0,0,0] | [0,2,4] |

**So the equality is FORCED, not accidental.** 2T is simply too small: its eigenvalues are 12th roots
of unity, and the two decompositions are congruent modulo exactly that.

> **SCOPE CORRECTION TO A BANKED ARC.** B327's `27|₂T` branching gate — used to sharpen the mass
> hierarchy CRUX to *"one representation-theoretic lookup"* — **is blind to the principal-vs-subregular
> distinction.** B327's conclusions about `n₁ = n₂` are untouched (it proved them by self-duality, for
> *any* SU(2)-factoring embedding, which is correct and is exactly why the gate cannot separate these).
> What is corrected is any reading of that gate as fixing *which* embedding.

## Test 2 — compatibility with the SO(10) grading D₂. BLIND, differently

Neither candidate makes the **16** (D₂ = +1) a union of complete sl₂ strings, and neither makes the
**10+1** one either. Consistent with **B1255**'s `[C18, D₂|W18] ≠ 0`: the object's gradings and its
sl₂ structure are **transverse, not aligned**. The SO(10) grading has no preference between them.

## Consequence

**I-25 stays UNEARNED**, and the search space for its discriminator is **narrowed by two**: it is not
the finite-group branching (by theorem) and not the SO(10) compatibility (by computation). B1257's
Brieskorn selector still stands as the only principled criterion on the table — but it remains a
statement about **E₆**, not yet a statement the **object** has confirmed.

## Controls (MB12, both directions)

- **This arc's own first statement of the mechanism was WRONG and is exhibited as wrong:** "χ_Symⁿ is
  periodic mod 12 on every class" **fails at λ = 1**, where χ = n+1 grows without bound. The selftest
  asserts the naive version is false, so the corrected per-modulus argument cannot silently revert.
- **The character test is not vacuous:** a 27-decomposition whose indices differ mod 12
  (`n = {10,9,5}`) gives a **different** character, exhibited.
- Dimensions reconstruct to 27 and 78 in every decomposition used; the principal 78 reproduces E₆'s
  exponents (1,4,5,7,8,11 → 3+9+11+15+17+23).

## Verification

`verification/two_t_is_blind.py` — standalone.

- **Feeds on:** B1257 (the selector), B1256 (I-25), B1255 (the transversality), B327 (the gate now
  scoped), B883 (the 27), B1250 (D₂).
- **Registers:** no change to I-25 (still UNEARNED); a **scope correction** on B327.
