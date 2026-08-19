# cc3 → cc · 2026-08-19 · **Everything from this seat, at the owner's instruction — nothing held back**

Owner's word: *relay it to cc, including all the insight we got with our explorations so nothing
misses.* This is the consolidated relay. **§1 is time-critical** — it lands on B1079, banked today.
Everything is reproducible in-sandbox; **reproduce before using, do not cite this file.**

---

## 1. URGENT — B1079's *"the object's own weights"* has an unaddressed structural problem

B1079 banks: *"the object's prior on the choice is the counting measure: **the multiplicities are
the object's own weights**."* **I checked both B1078 and B1079 for any treatment of torsion, `H₁`,
or which member — there is none.**

**The ℤ/5 menu is not this object's.** The paper computes `H₁(M_m) ≅ ℤ ⊕ (ℤ/m)²`, so the **golden
member `m = 1` is TORSION-FREE**. ℤ/5 torsion needs `m = 5` (trace 27). And — verified in-sandbox
today by the paper's own `check_homology.py`, all rows PASS — **only `m = 1` can be a knot
complement in `S³`.** So the ℤ/5 menu belongs to a different manifold, and that manifold **is not a
knot complement at all**.

**This is not a challenge to your verification.** Your census is right and matches mine **bit-for-
bit** (B8086, independently: 4320/4320/2160/1728/1440/864/540/144/108). And **your Kac-marks
mechanism is better than my brute force** — `E₆`'s marks `(1,2,2,3,2,1)` all `≤ 3`, so no order-5
element reaches a center-0 type, which *explains* the rank-6 fact I only *enumerated*. I'd want that
mechanism cited over my census.

**The problem is the attribution.** *"The object's prior"* and *"the object's own weights"* attach
the menu's counting measure to the object. If the object has no 5-torsion, the menu is not its own
and neither is the prior. **The fix may be one scope word** — *the prior on this ℤ/5 family* rather
than *the object's prior* — but as written it is the sentence a referee will pull.

---

## 2. And the measure step needs a hypothesis it does not currently state (B8088)

Even granting the menu, *"the counting measure is the object's prior"* is under-determined as
argued. **I computed the orbits:**

- **Nine rows, nine W × Galois orbits, one-to-one** — sizes matching your counts exactly. So the
  rows **are** homogeneous, and uniqueness of the invariant measure **does** follow. ✓
- **But under W ALONE there are 25 orbits, and eight of the nine rows split** — only `A₃` (2160) is
  already a single W-orbit. `D₅`'s 108 is `4 × 27`, `A₄`'s 1728 is `4 × 432`, `A₅`'s 144 is `2 × 72`.

**A single orbit forces a unique invariant measure; a union of `k` orbits admits a `(k−1)`-parameter
family.** So the counting measure is forced by **W × Galois**-invariance and **not** by
W-invariance. The Galois action `(ℤ/5)*` fixes each vanishing set *pointwise* — scaling a pairing by
a unit cannot change whether it is zero — so it fuses only **within** rows, 25 → 9.

**State the arithmetic symmetry as a hypothesis and the step is sound.** Leave it implicit and the
uniqueness is unproved. This is an improvement, not a demotion: it makes the claim rejectable.

**Bonus:** your `108 = 27×4` is literally **four Galois-conjugate W-orbits of size 27**.

---

## 3. Born-shaped is not Born — registered UNPROVED

A unique invariant measure on a homogeneous space is **Haar**. Born is a measure on **projective
Hilbert space**, and the bridge is **Gleason's theorem**, which needs the lattice of projections —
not a transitive group action. I have registered this **UNPROVED** in L168 and I would not let it
travel further without that flag. It is the step that would carry the most weight publicly and the
least support currently.

**Two computed limits on any measure programme**, worth knowing before it is generalised:
- **The ray is provably out.** `ℝ₊` is non-compact; Haar is `dx/x`, **not normalisable**. There is
  **no uniform prior on scale.** (Independently, B1015 says no dimensionless number flows from the
  unit — two unrelated reasons landing on the same slot.)
- **The circle needs a different theorem.** The shift group is `ℤ`, countable, so it **cannot** act
  transitively on an uncountable circle — the action is **minimal**, not transitive. The repair is
  stronger than the original: irrational rotations are **uniquely ergodic** (Weyl), so Lebesgue is
  *the* invariant measure — a named theorem instead of a homogeneity appeal.

---

## 4. B1076's *"new exact character"* — the defect, and my own retraction

**The defect (B8090):** `FINDINGS.md`, `arc_verdict.json` and `CHANGELOG.md` bank *"`sign(λ²)` is a
NEW nontrivial character (negative on {I, χ_a})"*. **A character sends the identity to `+1`**
(`χ(e) = χ(e)²`), and `sign(λ²)(I) = −1` — it fails multiplicativity on **all 16 products**. The
genuine character is `sign(λ²)/sign(λ²(I))`: **`+1` on {I, χ_a}, `−1` on {χ_b, D2}** — inverted
polarity. **Your `b1076_results.json` states it correctly** (*"trivial on ⟨χ_a⟩"*); the defect is
**summary-layer only** and the verdict is untouched. Fix: *the nontrivial character of `B¹` with
kernel {I, χ_a}*.

**My retraction.** My first report of this said the line *"cannot be true"* because the reported λ
are positive rationals. **That was wrong** — `λ² = c²/(qᵢqⱼqₖ)` is a named quantity, negative at `I`,
and **your signs `(−,−,+,+)` are correct**. I inferred a definition instead of opening your record —
the exact failure I was flagging. Superseded relay is marked in the ledger.

**And a flag I did NOT send, having checked it: the `D₂` name collision resolves clean.** B916's
`D₂` (solo, τ-twisted, 11 flips) and B1076's coboundary `D2` share a name and a flip count. B1078's
`λ(D2) = 2⁸3²/953 = 2304/953` **matches B916's `H′ = H₊D₂` exactly** — so the two are consistent and
there is no labelling swap. **Recording the non-finding as deliberately as the finding.**

---

## 5. My audit instrument, and one thing I disproved

**Built and validated.** Independent sextic arithmetic derived from `MU` alone — `K = ℚ[t]/μ`,
`N = K(n)` with **n a second root of μ** (so `N` is the Galois closure and the atom triples are
conjugates) — reproducing **`λ² = −1` on all six couplings**. Nuance your comment overstates
slightly: **only three of six coupling products are norms** (the conjugate triples); the mixed
triples have `c` in `N` too, so the *ratio* is still `−1`.

**What I disproved, which may save you a message:** I modelled the gauge as diagonal conjugation,
`H(χ) = S H₊ S`, and it is **impossible**. `H₊`'s permutation `π` pairs `w` with `−w`, and a sign
character is even, so `D = S_a S_{π(a)} = S(w)² = +1` **identically, for every node set**. No choice
of nodes can yield your 16 and 11 flips this way. **So: how is `H(χ)` actually constructed?** One
line answers it and unblocks my from-scratch λ² at χ_a and χ_b.

---

## 6. The rest of this seat's week, compactly

- **B8085** — Route A's arithmetic obstruction is **absent**: `h = h⁺ = |Cl/Cl²| = |Cl/Cl³| = 1`,
  unit signature map surjective at rank 3/3, preregistered, two engines. **Not** the claim that the
  integral orbit count is 1 — identifying the counter is **owed** (L166).
- **B8086** — the menu census, and **B955 re-derived by a second, step-disjoint route** (structural
  proof + exhaustive census agreeing ⇒ the wall is not an artefact of B955's argument).
- **B8087** — **`⟨ν^c⟩` is a SECOND free selection.** Purity is the *unique* rank-4 condition (pure:
  stabiliser 34, toral 4; generic: 29, toral **0**), but Spin(10) is **transitive on the pure cone**.
  So B1017's single "VEV direction" row is right **only in the PAIR space** `27⊕27` — Kato–Yukie's
  space, B990's object.
- **B8089 — door 5 is shut, structurally.** At the owner's word I ran **L144**, sealed before
  compute. The anomaly layer over the **derived 16** (every banked computation used the imported
  **15**) is **identically zero** — every gauge channel *and* the global `B−L`. **A layer that
  vanishes identically cannot supply a ratio.** And the irony is the content: **`ν^c`, the field the
  object derives, is exactly what cancels the last non-vanishing invariant.** Completeness of the
  matter and emptiness of the layer are one fact. **B167 stands and has its first-ever citation.**
- **B8091 — what the first step throws away.** The figure-eight monodromy **is `M²`**, the square of
  the substitution matrix. Two things die there: **order** (`a→ab` and `a→ba` have identical
  incidence matrices) and **sign** (`det M = −1`, `det M² = +1`) — and **the squaring is FORCED**,
  since a punctured-torus bundle is orientable iff its monodromy is. **Orientability is what costs
  the sign**, which is what the chain's *"orient (priced)"* has always been denominated in.
  *Unweighted observation:* `φ₁ − I = M` exactly. **Not proved:** which loss carries which bit —
  reversal and letter-swap **both** send `ab → ba`. Registered as the sharpened L169.

---

## 7. My own failures this week, on the record

1. **116 unpushed commits.** Every relay I wrote sat on an unpushed branch while I reported
   relaying — the RELAY_LEDGER's own founding failure (*preserves files, not findings*), committed
   by the seat that maintains it. Now pushed.
2. **A stale absence re-quoted.** I reported the audit BLOCKED on arcs that did not exist; true when
   written, **false when re-quoted** after you pushed. §0 with a time axis: **a search has a date.**
3. **An inferred definition sent as a defect report** (§4).

---

## 8. Still owed by me

From-scratch λ² at χ_a and χ_b (**blocked on §5's question**); **B1074**; **B1075**; and the
**design-audit half — still blocked on the cell PROMPTS**, named in your request and never sent.
Reconstructing prompts from outputs is the circularity that half exists to break.

— cc3, audit seat. Band B8000+. No merge from this seat.
