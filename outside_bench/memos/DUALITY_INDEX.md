# THE MASTER DUALITY INDEX — built, and it proves a theorem: the mirror is irremovable by a κ-invariance identity, and it is the ONLY expensive duality
## (outside bench memo 127, 2026-08-28; certificate `certificates/duality_index.py`, GREEN; standing document `THE_DUALITY_INDEX.md`; the owner's "go both", part 2)

**Exhaust-before-building, first.** Tree sweep of `origin/main`:
**no `DUALITY.md`, no duality index of any kind**; the word appears in
**141 primary documents** with no place that collects them. The gap is
real, so the build proceeds.

**The organizing claim (§1 of the standing doc):** the corpus's
dualities are of two kinds that must not be merged — **OPERATION**
dualities that *act* on the record (and can therefore be priced) and
**VALUE** dualities that *pair quantities* (and cost nothing). Both
are called "duality" in the same sentences, which is why the scattered
literature reads as one undifferentiated pile.

- **D1 — the census, mechanical.** Regex extraction over primary, no
  hand list: **238 `<X> duality` occurrences across 49 distinct
  heads**. Leaders: S (74), self (50), level-rank (23), global (8),
  Poincaré (6), z (6), Bloch / cusped-hyperbolic / per-unit /
  gap–chirality (4 each).
- **D2 — the operation table, exact.** Every candidate applied to the
  record's own Fricke point **P₀ = (2, 2, 2−ω)**, κ(P₀) = 1+ω, and
  typed by a criterion fixed before the run. Result: letter swap,
  reversal, inversion **SYMMETRY**; the three SL₂ lift signs **GAUGE**
  (decided by computation — each is verified to be the trace action of
  a nontrivial character F(a,b) → {±1}, i.e. a different point but the
  same PSL₂ representation); T and T⁻¹ **FLOW**; Thue–Morse L **FLOW\***
  (leaves the fibre, κ ↦ **−2**, which is exactly B496's Markov
  surface and memo 124's level-1 coincidence — re-derived here from
  the duality side); **gal alone is EXTERNAL** (κ ↦ 2−ω).
  Of the 8 elements of ⟨swap, lift signs⟩ exactly **2 fix P₀**: the
  **letter swap is the object's only internal duality at its own
  point**, because x = y = 2.
- **D3 — the invariance identity.** κ ∘ (letter swap) = κ ∘ s_x =
  κ ∘ s_y = κ ∘ s_z = κ ∘ T = κ ∘ T⁻¹ = κ **identically in ℤ[x,y,z]**,
  while κ ∘ L − κ = (x²−xyz+y²−1)(x²−xyz+y²+z²−4) ≢ 0.
- **D4 — THE THEOREM.** The whole internal group preserves κ; gal moves
  it. **Therefore no composition of internal operations returns
  gal(P₀) to P₀ — the mirror is irremovable**, proved for the entire
  group at once by a polynomial identity rather than point-by-point.
  **PREREGISTERED OUTCOME A**: exactly one external class, so the
  duality census **independently reproduces the one-bit count** with
  machinery disjoint from memo 107's realizer nullspace search.

**FENCE — this is one half of the count, stated exactly.**
*Irremovability (≥ 1)* is proved here, and more strongly than before.
*At most one* is **not**: that remains memo 111's L3 (the trace ring is
exactly ℤ[ω] ⟹ Gal = ℤ/2 ⟹ no second Galois freedom at any depth).
Together they give the count. Both κ values root X²−3X+3 (memo 109's
I3), so the invariant *content* is unmoved while the *value* is not.
Completeness of the operation list is a stated refuter, not a claim.

**ERROR FILED AT POINT OF OCCURRENCE.** The first draft of the census
reported 154 occurrences / 44 heads and attributed S-duality's absence
to "literature-scan prose rather than banked arcs." **False** — the
extractor was discarding single-letter heads. Filter artefact, not a
fact about the corpus; the filter is removed and the corrected counts
(238 / 49, with S, U and z restored) are what stands above.

**Interpretive, labeled:** this is the same one bit the quine (107),
the ledger (111) and the fence theorem (109) each reached from their
own direction. Four instruments, one statement — evidence that the bit
is a fact about the record rather than an artefact of any instrument.
Gate 5 untouched.
