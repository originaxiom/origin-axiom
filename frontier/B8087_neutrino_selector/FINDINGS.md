# B8087 — the neutrino selector: ⟨ν^c⟩ is a CONDITION, not a POINT

**Date:** 2026-08-19 · **Seat:** cc3 (audit) · **Verdict: PROVED.** Reproducer
`neutrino_selector.py`. Gate 5 untouched — the SM enters only as the rank-4 *target* against which
a computed rank is compared; no SM quantity is produced.

## The question, and why it had to be asked before relaying anything

B1017's ledger books **one** resource, *"VEV direction"*, against a rank drop its own text calls
two-step: *"the 6→4 drop is entirely `⟨1⟩` then `⟨ν^c⟩`, neither an involution."* If those are two
independent selections the ledger understates the price. The owner asked for the neutrino selector;
this is it.

## Instrument

`so(10)` on the **16** built explicitly over ℚ as fermionic bilinears on the even part of
`Λ*(ℂ⁵)` — 45 matrices, no structure constants quoted:
`so(10) = Λ²(ℂ⁵) ⊕ gl(5) ⊕ Λ²(ℂ⁵)*`, `10 + 25 + 10 = 45`.

## Result

| spinor | stabiliser | orbit | rank after breaking |
|---|---|---|---|
| **pure** | `sl(5) ⋉ Λ²` = **34** | **11** | **4** |
| generic | **29** | 16 | **0** |

**Purity is the unique rank-4 condition.** A generic `⟨ν^c⟩` does not merely give a different
group — it destroys the rank entirely (toral part **0**). Only at a pure spinor does `rank 5 → 4`,
which is what the SM's rank 4 requires. **So the second VEV being the right-handed-neutrino
direction is not a physics preference; it is the only direction leaving rank 4 standing.**

**But Spin(10) is transitive on the pure cone.** Orbit dim `45 − 34 = 11`, and the spinor variety
`S₁₀` is 10-dimensional projectively, so its affine cone is 11-dimensional. **One orbit.**

## Reading

A neutrino selector exists **as a condition** — purity, a closed condition cutting 16 dimensions
down to an 11-dimensional cone, a real reduction. **It does not produce a point.** B990's
orbit-to-point gap recurs on the second VEV verbatim; `⟨ν^c⟩` is **not forced** by `⟨1⟩`.

**Consequence for the ledger.** `⟨1⟩` and `⟨ν^c⟩` are **two** selections. B1017's single row is
correct **only if the orbit-point is read as a point in the space of PAIRS**, `27 ⊕ 27` — which is
exactly what Kato–Yukie classify and exactly B990's object. Read as one direction inside a single
27, **it undercounts by one.** This does not break the accounting; it fixes which reading is
load-bearing, and shows why Route A's lane (pairs, integral orbits) was the right lane.

## THE CONTROL THAT MATTERED — the first build was wrong

The initial `gl(5)` block omitted the spinor shift `h_i = a_i†a_i − ½`. That spans an algebra
**isomorphic to `so(10)`** — dimension 45, closed under bracket, rank 5, **every structural check
green** — but acting in a **character-twisted representation**, which silently moved the stabiliser
to 35. **Closure and rank did not catch it. Only the predicted stabiliser dimension did.**

The arc therefore carries a control that pins the **representation**, not the algebra: all 16 basis
vectors are weight vectors, every weight is `(±1)⁵`, and the sign-parity is **constant** across all
16 — one chiral half, not a mix. *An isomorphism check is not a representation check.*

## SCOPE

`so(10)` on the 16. Nothing about the member, the class, the sisters or the rows. Says nothing
about whether the pair is *attainable* — only that the second component is a free choice once the
first is made.
