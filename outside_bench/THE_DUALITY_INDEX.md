# THE DUALITY INDEX — the corpus's dualities, inventoried from primary and TYPED by a computed criterion; the index's content is that exactly one of them is expensive
## (outside bench, 2026-08-28; the owner's "go both", part 2; certificate `certificates/duality_index.py`, GREEN; standing document, addendum-only mutations)

**Why this document exists.** The programme has no `DUALITY.md`. Its
dualities are scattered across **141 primary documents** — kill-graph
FINDINGS, `LAW_MAP.md`, `THEOREM_LEDGER.md`, `TERMINOLOGY.md` — with
no single place that says which they are, which act on the object, and
which of them cost anything. A list alone would be bookkeeping. This
index has a **spine**: every duality that *acts* is typed by an exact
computation, and the typing turns out to reprove a banked theorem by
disjoint means.

---

## §1 — THE TWO COLUMNS (the index's organizing claim)

The corpus's dualities are of **two kinds that must not be merged**:

- **OPERATION dualities** — maps that *act* on the record (swap the
  letters, reverse the word, conjugate the field, iterate the Fricke
  map). These can be applied, composed, and priced.
- **VALUE dualities** — pairs of *quantities* the record computes
  (being/hearing, imaginary/real, cancellation/residue). These are
  results, not actions; they cost nothing and compose with nothing.

Merging the columns is the mistake the scattered literature invites,
because both are called "duality" in the same sentences. They are
indexed separately below.

---

## §2 — THE CENSUS (mechanical, no hand-written list)

Extracted by regex over the primary corpus, so the inventory is
auditable rather than remembered: **238 `<X> duality` occurrences
across 49 distinct heads** in 141 documents. The named dualities the
corpus actually carries, at count ≥ 2:

| n | duality | n | duality |
|---|---|---|---|
| 74 | S | 4 | per-unit |
| 50 | self | 4 | gap–chirality |
| 23 | level-rank | 3 | RT |
| 8 | global | 3 | transpose |
| 6 | Poincaré | 3 | Aubry |
| 6 | z | 2 | U |
| 4 | Bloch | 2 | reciprocal, kernel/image, Milnor, chirality, closed-SOL/cusped-hyperbolic |
| 4 | cusped-hyperbolic | | |

⚠ **ERROR FILED AT POINT OF OCCURRENCE.** The first draft of this
section reported 154 occurrences across 44 heads and explained
S-duality's absence as "literature-scan prose rather than banked
arcs." **That explanation was false.** S-duality was absent because
the extractor discarded single-letter heads — a filter artefact, not a
fact about the corpus. The filter is removed, the counts above are the
corrected ones, and S-, U- and z-duality are restored. The verbatim
extraction is in `outputs/duality_index_out.txt`.

---

## §3 — THE SPINE: the operation column, typed exactly

Work in the Fricke character coordinates (x, y, z) = (tr A, tr B,
tr AB) at the record's own point **P₀ = (2, 2, 2−ω)**, with
**κ(x,y,z) = x² + y² + z² − xyz − 2**, so **κ(P₀) = 1+ω** (memo 86).
The four types were **fixed before the run**.

| operation | image of P₀ | κ | type |
|---|---|---|---|
| identity | (2, 2, 2−ω) | 1+ω | SYMMETRY |
| **letter swap a↔b** | (2, 2, 2−ω) | 1+ω | **SYMMETRY** |
| word reversal | (2, 2, 2−ω) | 1+ω | SYMMETRY |
| inversion w ↦ w⁻¹ | (2, 2, 2−ω) | 1+ω | SYMMETRY |
| SL₂ lift sign s_x | (2, −2, −2+ω) | 1+ω | GAUGE |
| SL₂ lift sign s_y | (−2, 2, −2+ω) | 1+ω | GAUGE |
| SL₂ lift sign s_z | (−2, −2, 2−ω) | 1+ω | GAUGE |
| **gal (complex conjugation)** | (2, 2, 1+ω) | **2−ω** | **EXTERNAL** |
| Fricke golden T | (2−ω, 2, 2−2ω) | 1+ω | FLOW |
| Fricke golden T⁻¹ | (2, 2+ω, 2) | 1+ω | FLOW |
| Thue–Morse L | (2−ω, 2−ω, 2−4ω) | **−2** | FLOW\* |

- **GAUGE is decided by computation, not by name:** a map is a gauge
  iff it is the trace action of twisting the SL₂ lift by one of the
  three nontrivial characters F(a,b) → {±1} — a different *point*, the
  same PSL₂ *representation*. All three sign changes are verified to
  be exactly those.
- **FLOW\*** = moves κ but not to its Galois mate: it leaves the fibre
  altogether. Its κ here is **−2**, which is exactly B496's Markov
  surface and memo 124's level-1 triple coincidence — an independent
  re-derivation of that coincidence from the duality side.
- **The object's stabiliser:** of the 8 elements of ⟨letter swap, lift
  signs⟩, exactly **2** fix P₀. **The letter swap is the object's only
  internal duality at its own point** (because x = y = 2); reversal
  and inversion act trivially on the coordinates and add nothing there.

---

## §4 — THE THEOREM THE INDEX PRODUCES

Verified as **polynomial identities in ℤ[x,y,z]** — at every point,
not merely at P₀:

> κ ∘ (letter swap) = κ ∘ s_x = κ ∘ s_y = κ ∘ s_z = κ ∘ T = κ ∘ T⁻¹ = κ,
> **identically**; while κ ∘ L − κ = (x²−xyz+y²−1)(x²−xyz+y²+z²−4) ≠ 0.

Hence the entire internal group — letter swap, the three lift signs,
reversal, inversion, and the whole Fricke action Tⁿ — **preserves κ
exactly**. And κ(gal P₀) = 2−ω ≠ 1+ω = κ(P₀).

> **THEOREM.** No composition of the record's internal operations
> sends gal(P₀) back to P₀. **The mirror is irremovable**, and the
> proof is a one-line invariance argument covering the whole group at
> once.

**PREREGISTERED OUTCOME A**, as recorded before the run: exactly one
operation class is EXTERNAL, so the duality census **independently
reproduces the one-bit count** (memos 107/109/111) — sharing no
machinery with the realizer nullspace search of memo 107.

**FENCE, stated exactly — this proves ONE HALF of the count.**
*Irremovability (≥ 1)* is what is proved here, and it is proved more
strongly than before (a polynomial identity, not a point check).
*At most one* is **not** proved here: that is memo 111's L3 — the
trace ring is exactly ℤ[ω], so Gal = ℤ/2 and no second Galois freedom
exists at any depth. Together they give the count; this cell replaces
the realizer search in the first half only. Note also that both κ
values root X²−3X+3 (memo 109's I3): the invariant *content* is
unmoved while the *value* is not.

---

## §5 — THE VALUE COLUMN (indexed, not recomputed)

| pair | content | source |
|---|---|---|
| being / hearing | ℚ(√−3) vs ℚ(√5), joined by meeting ℚ(√−15) | C7 theorem, Klein four-group V₄ |
| imaginary / real | the tower is non-real at levels 0–1, real from 2 on | memo 124 — crossing at the cusp, irreversible |
| cancellation / residue | κ − 2 = ω², permanent, propagated multiplicatively | memo 125 / B161 / B496 |
| even / odd under the mirror | magnitudes in the KERNEL; torsion signs ODD | memo 110 — 604 fixed, 12,516 flipped |
| forced / free | every value forced; the free list is the observer column | THE_FORCED_AND_THE_FREE, the census |
| object / observer | timeless exact structure vs the seat and its bit | B716/B721, memos 111/112 |
| II₁ / III_λ | tracial equilibrium clock vs thermal, weight-induced | B721 / B723 |
| 27 / 27̄ | conjugate minuscule reps paired by Poincaré duality | the twisted-double cells |

---

## §6 — THE INDEX'S ONE LINE

**Operation dualities are typed by κ: the internal ones are free, and
exactly one — the mirror — moves the founding invariant and is
therefore external. Value dualities pair quantities and cost nothing.
The master index is that split, and its content is that the expensive
side has exactly one element.**

*(Interpretive, labeled: this is the same one bit the quine, the
ledger and the fence theorem each found from their own direction. Four
instruments, one statement — which is evidence that the bit is a fact
about the record rather than an artefact of any one instrument.)*

---

## §7 — REFUTERS

- Exhibit an internal operation of the record that **moves κ**: kills
  §4's identity and the irremovability argument with it.
- Exhibit a **second** external class not in the Galois orbit: flips
  the preregistered outcome to B and forces memos 107/111 to be
  revised.
- Show the letter swap does **not** fix P₀ (it does, because x = y = 2):
  would remove the object's only internal duality.
- Exhibit a named duality in the census that is an **operation** on the
  object and is absent from §3's table: the table would be incomplete,
  and the count would have to be rerun over the enlarged list.

**Scope.** §3's table is a census over an enumerated operation list;
its completeness is the fourth refuter above. Gate 5 untouched — no
measured value enters, and §2 is corpus metadata.
