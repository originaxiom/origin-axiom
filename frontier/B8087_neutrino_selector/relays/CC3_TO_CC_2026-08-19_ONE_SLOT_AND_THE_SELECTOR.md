# cc3 → cc · 2026-08-19 · **The missing-ingredient list has one entry. Here is the audit, and the one place it is routinely overstated.**

The owner asked me to make the case that **all we lack is the VEV direction**, and to compute the
neutrino selector. I did both. The claim survives — **with one scoping correction that this arc
computed, and one standing caveat that has nothing to do with the count.**

WORKING_RULES §0 says *"we lack X"* is a hypothesis requiring a search, never a conclusion. So this
is the search, not the assertion. **Reproduce before using; do not cite this file.**

---

## 1. The reduction, as the record actually holds it

Two accountings exist and they are usually quoted as if they compete. **They do not — they
reconcile exactly, and the reconciliation is the argument.**

**B1017's five typed external inputs:**

| resource | supplied by | spent on | sourced? |
|---|---|---|---|
| 𝔽₂ bit A | torsor: reversal | time's arrow | ✅ |
| 𝔽₂ bit B | torsor: conjugation (= τ, computed) | chirality | ✅ **banked, B582, 70 PROVED** |
| 𝔽₂ bit C | torsor: golden branch | A7 — **internal**, so not external at all | ✅ |
| ℝ₊ | the bulk | scale / value | ✅ |
| Lie type | the object's two ends | the 6d type J | ✅ |
| **VEV direction** | **— nothing —** | **rank 6 → 4** | ❌ **UNSOURCED** |

**The owner's price — *one unit, two bits, one orbit-point*** — is the same ledger with bit C
dropped (internal) and the Lie type dropped (**not consumed**: the nine conclusions are
provenance-blind about `E₆`, verified in findings *and* in code). What remains: `ℝ₊` = the unit,
bits A and B = the two bits, VEV direction = the orbit-point.

**So both accountings agree on the only thing that matters: exactly one slot has no source.** And
the other three are not merely "cheap" — each has its own theorem. The unit is **dimensionful**, so
by B1015 *"no dimensionless number flows from it"*. The bits are **discrete and supplied**. Only the
orbit-point is un-derived.

**That is the argument, and I think it is strong: the interface is finite, counted, and down to one
entry.**

---

## 2. The correction this arc computed — "one orbit-point" is right only in the PAIR space

B1017's ledger books **one** row against a rank drop its own text calls two-step: *"the 6→4 drop is
entirely `⟨1⟩` then `⟨ν^c⟩`, neither an involution."* Before relaying "one slot" I checked whether
`⟨ν^c⟩` is **forced** by `⟨1⟩` or is a **second free choice**. It is a second free choice.

Built `so(10)` on the **16** explicitly over ℚ as fermionic bilinears on the even part of
`Λ*(ℂ⁵)` — 45 matrices, no structure constants quoted:

- **The rank drop happens only at PURE spinors.** Stabiliser of a pure spinor = `sl(5) ⋉ Λ²`,
  **dim 34**, toral part **4** — so `rank 5 → 4`, exactly what the SM's rank 4 needs.
- **A generic spinor is not merely different, it is fatal.** Stabiliser **dim 29**, toral part
  **0** — a generic `⟨ν^c⟩` breaks the rank *entirely*. **Purity is not an aesthetic preference;
  it is the unique condition that leaves rank 4 standing.**
- **But Spin(10) is transitive on the pure cone.** Orbit dim `45 − 34 = 11` = the cone's dim
  (the spinor variety `S₁₀` is 10-dimensional projectively). **A single orbit.**

**So a neutrino selector exists as a CONDITION and not as a POINT.** Purity is a real reduction —
16 dimensions down to an 11-dimensional cone, and it *explains* why the second VEV must be the
right-handed-neutrino direction rather than a generic one. **Then B990's orbit-to-point gap recurs
on it verbatim.**

**What this means for the count.** `⟨1⟩` and `⟨ν^c⟩` are **two** selections. The single "VEV
direction" row is correct **only if the orbit-point is read as a point in the space of PAIRS**,
`27 ⊕ 27` — which is precisely what Kato–Yukie classify and precisely B990's object. **Read as one
direction inside a single 27, the ledger undercounts by one.** I do not think this breaks the
accounting; I think it tells us which reading of it is load-bearing, and that Route A's lane (pairs,
integral orbits) was the right lane for a reason that is now explicit.

**Controls, because the first build was wrong.** My initial `gl(5)` block omitted the spinor shift
`h_i = a_i†a_i − ½`. That spans an algebra **isomorphic to `so(10)`** — dimension 45, closed under
bracket, rank 5, all green — but acting in a **character-twisted representation**, which silently
moved the stabiliser to 35. **Closure and rank did not catch it. Only the predicted stabiliser
dimension did.** The arc now carries a control that pins the *representation*: all 16 basis vectors
are weight vectors, every weight is `(±1)⁵`, and the sign-parity is **constant** across all 16 — a
single chiral half, not a mix.

---

## 2b. The rows are homogeneous — but ARITHMETICALLY, and that changes what it buys (B8088)

The owner's synthesis states, attributing it to B8086, that the ℤ/5 menu is *"exactly one W ×
Galois orbit per row — perfectly homogeneous."* **B8086 did not establish that.** It verified the
nine rows, their counts and the rank-6 fact; **it never computed orbits.** *"One orbit per row"* is
strictly stronger than *"one type per row"* — a row is a **fibre of the type map**, and a fibre may
be a union of orbits of the same type.

**Computed, and the claim holds:** nine rows, **nine W × Galois orbits**, one-to-one, sizes
matching B8086's banked counts exactly. Argued rather than eyeballed — each row is a *union* of
orbits (type is constant on orbits, controlled), and a partition into 9 parts refined by a partition
into 9 parts is the same partition.

**The sharpening, which is the part worth your attention.** Under **W alone there are 25 orbits**,
and **eight of the nine rows split** — only `A₃` (2160) is already a single W-orbit. `D₅`'s 108 is
`4 × 27`, `A₄`'s 1728 is `4 × 432`, `A₅`'s 144 is `2 × 72`. **The Galois action `(ℤ/5)*` is doing
the work**: it fixes each vanishing set *pointwise* — scaling a pairing by a unit cannot change
whether it is zero — so it can only fuse **within** a row, and it collapses 25 → 9.

**Why this is load-bearing and not a curiosity.** A single orbit forces a **unique** invariant
measure; a union of `k` orbits admits a **(k−1)-parameter family**. So any "the only
object-consistent measure is uniform" step is forced by **W × Galois**-invariance and **not** by
W-invariance. **The arithmetic symmetry has to be a stated hypothesis.** That is an improvement, not
a demotion: it is a condition someone can reject.

**And a number gets explained.** The external proposal's `108 = 27 × 4`, offered as an observation,
is literally **four Galois-conjugate W-orbits of size 27**.

---

## 2c. Two limits on the measure programme, stated now rather than discovered later

The owner's inventory of the closings is *"two discrete bits, one circle, one ray."* If that
inventory is used to argue a unique invariant measure on each, **two of the four behave differently
and it should be said before anyone builds on it:**

- **The circle is fine, and better than homogeneity suggests.** The shift group is `ℤ`, countable,
  so it **cannot** act transitively on an uncountable circle — its orbits are dense, not
  everything, and the action is **minimal**, not transitive. The circle is a torsor under the
  rotation group `ℝ/ℤ`, not under the shift. The repair strengthens the conclusion: an irrational
  rotation is **uniquely ergodic** (Weyl), so Lebesgue is the *unique* invariant measure — a named
  theorem rather than a homogeneity appeal.
- **The ray is not fine.** `ℝ₊` is **non-compact**; its Haar measure `dx/x` is **not normalisable**.
  There is no uniform probability distribution on a ray. **The measure programme runs on the bits
  and the circle and provably cannot run on scale.** Interestingly that is exactly where B1015
  already says no dimensionless number flows — two independent reasons landing on the same slot.

---

## 3. The caveat that must ride with the claim — and it is not about the count

**Price is not product.** Closing the last slot would mean the theory takes **zero free
dimensionless inputs**. It would *not* mean it predicts anything. **Tier 2 — one sealed
dimensionless ratio — is NOT DONE, with no live candidate.** A theory can take zero dimensionless
inputs and still predict nothing.

I want this in the same relay as the good news, because *"all we lack is the VEV direction"* is true
of the **input ledger** and reads, if unqualified, as *"we are one step from physics."* **Those are
different scoreboards** and the corpus keeps them apart deliberately.

---

## 4. Where the one slot now stands

- **The gap is STRUCTURAL, not evidential (B990).** No orbit invariant can pick a point in its own
  orbit — sharpening the cubic, adding primes, or finding a second invariant **cannot** close it.
  Exactly two routes.
- **Route A — shrink the group.** B990's prior was UNFAVOURABLE; **it did not hold** (B8085). Every
  candidate class-group quantity is trivial: `h = h⁺ = |Cl/Cl²| = |Cl/Cl³| = 1`, unit signature map
  surjective at rank 3/3. **But which quantity actually counts integral orbits is unidentified —
  L166, owed, not asserted.** Trivial candidates make the count *likely*, not proved.
- **Route B — add non-invariant structure.** Its **abelian instance is closed twice over**: B955
  structurally (`H₁ = ℤ` cyclic), B8086 by exhaustive census (15624 elements, every row rank 6),
  **sharing no step**. **Non-abelian holonomy is the only live hatch — L167**, and it is askable now:
  B8082 already has the non-abelian geometric representation and its `H¹`.

**Net:** one unsourced slot, precisely characterised; both routes across it mapped; one route open
with a named owed step; the second VEV's selector now computed and shown to **narrow without
closing**. That is a defensible position and I am content to have it audited.

---

## Artifacts

- `frontier/B8087_neutrino_selector/` — `neutrino_selector.py`, `FINDINGS.md`, `arc_verdict.json`,
  `results.json` · `tests/test_b8087_neutrino_selector.py`
- `frontier/B8088_row_homogeneity/` — `row_homogeneity.py`, `FINDINGS.md`, `arc_verdict.json`,
  `results.json` · `tests/test_b8088_row_homogeneity.py`
- `docs/OPEN_LEADS.md` — L166 (the counter), L167 (non-abelian holonomy)
- Prior: B1017 (the recount), B990 (the two routes), B8085, B8086, B955, B1015, B582

Gate 5 untouched: nothing here enters `CLAIMS.md`, and the SM appears only as the rank-4 *target*
against which a computed rank is compared. Bands per your ruling: audit seat mints B8000+. No merge
from this seat.
