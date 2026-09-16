# xB003 — THE MONODROMY ON THE OBJECT'S OWN LEAF: the double tick IS the monodromy (proved), its fixed point sits on the ramified prime of ℚ(√−3), and B1341's missing generating function has trace 5

**Status: banked (frontier, seat branch `sep16-branch`). Verdict PROVED.** Seat `xb`. DESIGN sealed
**POST-HOC and labelled** (one criterion stated in advance in writing, unhashed — see DESIGN).
Gate 5 untouched. Lock: `verification/reproduce.sh`, four cells, every one asserting its own
mathematics.

## What was owed

B1341 proved the half-tick anti-variational and the double tick symplectic, gave
`S(u,U) = u²/2 − uU + U²` on `I = 0`, and recorded — checked, not assumed — that **the object sits
at `I = −1` where that linearisation fails and the explicit `S` does not apply.** That was the gap.

## 1. B1341's "double tick" IS the monodromy — proved, not assumed

`T² = F_R ∘ F_L` **identically**, where `F_L, F_R` are the trace maps induced by the two Dehn
twists `(a,b) ↦ (a, ab)` and `(a,b) ↦ (ab, b)`, whose abelianisations are `L = [[1,1],[0,1]]` and
`R = [[1,0],[1,1]]`, composing to `RL = [[1,1],[1,2]]`, trace 3, det 1 — conjugate to m004's
monodromy `LR`. Both twists preserve κ, so the leaf structure is theirs.

**Independent route.** The fibration's monodromy in the literature presentation, `φ(a) = ab,
φ(b) = bab`, induces — by the trace identities, re-derived here — exactly `F_L ∘ F_R`, which is
conjugate to `F_R ∘ F_L` by `F_L`. Two derivations, same map.

This closes the identification B1341 used and did not prove.

## 2. The fixed point, and where it lands arithmetically

On the object's leaf `κ = −2` — `X²+Y²+Z² = XYZ`, the **Markov surface** (already banked at
**B1347**; the identification is not this arc's) — the monodromy has exactly:

* the **node** `(0,0,0)`, the surface's singular point, where the derivative's eigenvalues are the
  primitive cube roots of unity and 1;
* a **conjugate pair of regular fixed points**, and this is the content:

> **every trace of the pair has norm 3, and equals `2+ω` or `2+ω̄`** — i.e. the fixed point of the
> object's own monodromy, on the object's own leaf, sits on the **ramified prime above 3** of
> `ℚ(√−3)`, the object's own invariant trace field (discriminant −3).

The pair being conjugate is the mirror; that the object is amphichiral is consistent with the two
being exchanged rather than one being preferred.

*(A fixed point is what "fibred" says in trace coordinates: m004's fibre is the structure its own
monodromy leaves alone. That the fibre representation is fixed by the monodromy is classical.)*

## 3. B1341's theorem exhibited on the object's leaf

`D(monodromy)` at the regular fixed point has eigenvalue **1** transverse to the leaf and a pair
**(5 ± √21)/2** on it, **product exactly 1** — symplectic, char poly `λ² − 5λ + 1`. So an action
exists *there*, concretely, and not only in general.

## 4. The gap, filled at the fixed point

In exactly B1341's normalisation:

| leaf | trace | generating function | recursion |
|---|---|---|---|
| `κ = +2` (`I = 0`) — B1341's | 3 | `S = u²/2 − uU + U²` | `c = 3b − a` |
| **`κ = −2` — the object's** | **5** | **`S = u²/2 − uU + 2U²`** | **`c = 5b − a`** |

## Scope — three fences, all load-bearing

1. **Local, not global.** This is the leading (quadratic) part at the fixed point. A hyperbolic
   fixed point of an area-preserving map always carries resonances `λᵃλ^{−b} = λ`, so analytic
   linearisation is **not** automatic and is **not claimed**. What is exact is the derivative and
   hence `S`'s leading term.
2. **`ℚ(√21)`** — **CORRECTED BY ADDENDUM 2: it is NOT un-interpreted.** B425 computed the
   adjoint twisted Alexander polynomial of the object at `ρ_geo` as `(t−1)(t²−5t+1)/t³`, *"roots
   in ℚ(√21) (3-governed)"*; our multipliers are its roots, and this arc is an independent
   second route to it (Fox calculus there, character-variety derivative here). The 5 is the trace
   of the monodromy on `H¹(Σ; Ad ρ)` — the adjoint analogue of the homological trace 3.
   *(ADDENDUM 1 separately reports: the multiplier is **not**
   a function of `tr(M)` — `LLRR` and `LLLLR` share trace 6 and differ — so the 5 is not a
   restatement of the 3; and the `21 = 3·7` / `77 = 7·11` resemblance to the record's fields is
   **declined** as short-catalogue, the `77` firing at m009 rather than at the object.)* The multiplier field has discriminant `21 = 3·7`. It is neither
   `ℚ(√5)` (the genesis) nor `ℚ(√−3)` (the trace field). No reading of it is offered, and none
   should be inferred from its sharing factors with `disc K = 3⁴·7·11` or `ℚ(√77)`. Recorded as a
   computed number awaiting a reason.
3. **Not row 4.** Dynamics at the trace-map layer. The TOE ledger's row 4 asks for a 4d Lorentzian
   field action; this is not one, and nothing here changes that row's status.

## What is NOT claimed

The leaf-as-Markov-surface identification is **B1347's**, not this arc's. The trace map ↔ mapping
class group correspondence and the fixity of a fibre representation under its monodromy are
classical. What this arc adds is the twist decomposition proving B1341's identification, the
regular fixed point and its arithmetic, the symplectic derivative there, and the trace-5
generating function.
