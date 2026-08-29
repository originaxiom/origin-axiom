# P3 — THE PAPER: the elaboration

**Owner-approved 2026-08-29.** The portfolio's P3, crafted **owner + cc**, distinct from cc3's
four-paper series. This document is the paper's specification: what it claims, on what evidence, in
what order, and what would kill it. It is not the paper.

---

## 0. The paper in one sentence

> **A single hyperbolic 3-manifold forces the Standard Model's gauge structure, provably withholds
> its values, and prices the observer at exactly one bit — and each of those three is a theorem
> with a stated escape route, not a gap in the argument.**

The paper's whole distinction is that **the negative half is as sharp as the positive half**. Most
"structure from geometry" papers are dismissed because they claim the positive and hand-wave the
negative. This one proves the boundary in both directions and ends on it.

## 1. The genre problem, and the answer

A referee's prior on this subject is set by decades of numerology. The paper must survive being
skimmed by someone who expects numerology. The blueprint (ratified 2026-08-20) is built for that
reader, and every element is a defence:

| element | what it defuses |
|---|---|
| **misses in the abstract** | "they only report hits" — the abstract names sin²θ_W's 16σ miss and V-3 before any success |
| **the non-claims box** (§4 here) | "they'll claim they derived the SM" — an explicit list of what is *not* claimed, on page 2 |
| **the recognition table** (§5) | "this is fitted" — every result that is a *known* GUT fact, labelled reproduced-not-predicted |
| **freedom-ledger methods** | "hidden inputs" — every free choice is priced and counted, and the count is small and explicit |
| **verification in minutes** | "unreproducible" — a reader runs the load-bearing claims from a public repo in under ten minutes |
| **it ends on the wall** | "over-claiming" — the last section is what the object cannot do and why that is a theorem |

**The paper's rhetorical spine is the freedom ledger.** Not "look what we derived" but *here is
exactly what had to be assumed, and it is less than you expect.*

## 2. The three movements

**I — FORCED.** The object supplies the adjoint half of a grand-unified breaking: an E₆ boundary
with the build proved isomorphic to M(𝕆,ℂ) (B882/B904); the **global ℤ₆ form**
[SU(3)×SU(2)×U(1)]/ℤ₆ **derived** (B862, and independently confirmed *and extended* at **B1080** —
uniform over six Weyl realizations, with row 1's full algebra giving ℤ/6 × ℤ/2) — resolving an
ambiguity *the Standard Model itself does not fix*; **hypercharge as the unique gaugeable U(1)** in
the chain's abelian sector, direction only (B864); and the **termination theorem** — the cascade
halts at the SM because the SM is the terminal registerable algebra (B863), with every proper
descent killing registerability while the SM stays chiral.

> **⚠ CORRECTED BY THE SWEEP (B1210).** An earlier draft of this section listed *"the measurement
> cascade landing on su(3)⊕su(2)⊕u(1)³"* among the forced discoveries. **B951 deflates that
> headline**: the landing is exactly the **A₂+A₁ Levi subalgebra** of e₆, and arriving there from E₆
> is **Borel–de Siebenthal (1949) / Dynkin (1952)** — classical, not a discovery. It moves to the
> **recognition table**. What survives as forced is the *chain's termination* and the *global form*,
> not the *arrival*. This is precisely the correction a referee would have made, and it is the
> single most important thing the sweep caught.

**II — WITHHELD.** Not "not yet found": proved. **V-3** is exhaustive — 16 object periods against 22
SM targets, no object period is an SM ratio; natural object invariants are disjoint too (B1129). Ten
independent value-negatives, the tenth reached **by structure rather than by scan** (B1140/B1138:
the 64 of the spacetime branch has invariant content zero, so hypercharge cannot organize there).
Rank reduction is a theorem, not an absence. Scale is Mostow-free by construction. The single cause
behind all of it is stated once and re-used.

**III — THE OBSERVER, PRICED.** What the object cannot supply, it prices. The four "cannot
self-close" probes are **one ℤ/2 class** (B1183). The bit is **relational** — it belongs to a
heterogeneous pair and to neither relatum (B1192) — **selector-free** (B1196: invariant under
simultaneous GL₂(ℤ)-conjugation, so no act of selection is needed), governed by **κ, the founding
Fricke invariant** (B1195: gen_det = −κ/g², so the existence obstruction and the observer-bit
criterion are one invariant), and **irremovable by two disjoint proofs** — a realizer-nullspace
argument and a κ-invariance argument whose mechanism is *the same identity* that makes the founding
climb generate no new invariant (B1203 + B1208). The bit is **spent once, at coordinatization** —
choosing which complex root names ω — and never again, because the trace ring is exactly ℤ[ω] at
every depth. And the object **names itself completely in mirror-even letters and provably cannot
sign itself** (B1184, the quine).

**The closing figure**: the same Φ₃ = u²+u+1 is the partition function's saddle equation, the
founding obstruction κ−2, and the boundary's complex structure, with linking map u ↦ u² = c
(B1200). One invariant, seen from three faces.

## 3. Section architecture

| § | title | claims | evidence |
|---|---|---|---|
| 1 | Introduction: the two halves | the thesis; **the misses stated here** | — |
| 2 | The object | m004, its trace field ℚ(√−3), the E₆/McKay route | B882, B904, B727 |
| 3 | What is forced | the cascade, ℤ₆, hypercharge direction, termination | B892/B961, B862, B864, B863 |
| 4 | **The non-claims box** | *see §4 below* — placed early, deliberately | — |
| 5 | What is withheld, and why it is a theorem | V-3 exhaustive; the ten negatives; rank reduction; scale | B1126, B1129, B1138/B1140 |
| 6 | The observer, priced | one class, relational, selector-free, κ-governed, irremovable, spent once | B1183, B1192, B1195, B1196, B1203/B1208, B1184 |
| 7 | The freedom ledger | every free input, counted and priced | the ledger docs |
| 8 | The recognition table | what is known GUT lore vs what is new | §5 below |
| 9 | Falsifiers | *see §6 below* | — |
| 10 | The wall | the four walls; what a specialist would have to supply | SEAM-A, heterotic import, branch selection, generation-3 |

**Note the ordering choice**: the non-claims box sits at §4, *before* the negative results, so that a
reader who stops early has already seen the boundary. This is deliberate and worth defending in the
cover letter.

## 4. The non-claims box (draft, ready to sharpen)

> **This paper does not claim**: to derive the Standard Model; to predict any measured value; that
> the object is the universe or a model of it; that three generations are forced (the object's
> honest content is **one** generation — the family count is *exhibited* in E₈'s 27×3 and **not
> forced**); that sin²θ_W = 3/8 is a prediction (it is a known GUT relation, **reproduced**, and the
> run to M_Z **misses at 16σ**); that any dynamics, rate, or action is supplied; that the observer's
> bit is consciousness, or that it is not.

## 5. The recognition table (what a referee will already know)

Every item here is labelled **reproduced, not predicted** in the paper itself:
sin²θ_W = 3/8 at GUT level · the E₆ ⊃ SO(10) ⊃ SU(5) chain · anomaly cancellation over the 16 ·
the 27 = 16+10+1 decomposition · Mostow rigidity's scale-freedom · **the landing algebra
su(3)⊕su(2)⊕u(1)³ as the A₂+A₁ Levi of e₆ — Borel–de Siebenthal / Dynkin, added by the B1210 sweep
on B951's deflation** · **the rank-reduction location**: skipping SU(5) is skipping the rank
reduction, and the two units the cascade cannot shed are U(1)_ψ and U(1)_χ, the standard E₆ extra
abelian directions (B953). **What is not standard**: the ℤ₆
global form *derived* rather than assumed; the termination theorem; the exhaustive value-disjointness;
the observer's one-bit pricing with its κ law.

## 6. The falsifier matrix (what kills the paper)

1. **Exhibit a record-computable quantity that differs on the two anchored models** → kills the
   independence/one-bit result.
2. **Exhibit two of the odd-column signs (torsion sense, CS, CP, chirality) as independently
   settable** → kills the correlation claim; the paper predicts a *correlation*, not a sign.
3. **Exhibit an object period that is an SM ratio within the stated tolerance** → kills V-3.
4. **Exhibit a proper descent below the SM that stays registerable** → kills the termination theorem.
5. **Exhibit a second gaugeable U(1) in the chain's abelian sector over chiral matter** → kills B864.
6. **Supply the missing linear condition on the ℙ³** → does *not* kill the paper; it **upgrades**
   a row from PERMANENT to FORCED. This one is live (see §8).

Every falsifier is stated in the paper with the computation that would settle it.

## 7. Tables and figures

- **F1** the breaking chain, with the ℤ₆ form marked as derived
- **F2** the freedom ledger — the single most important object in the paper
- **T1** the recognition table (§5)
- **T2** the value-negative census: 10 routes, each with its discriminating computation
- **F3** the Φ₃ three-face diagram (saddle / founding obstruction / boundary), linking map u ↦ u²
- **T3** the observer's leg table: archimedean orientation (full bit) · finite form-class label ·
  θ the value-kernel · the continuous scale · the rank-reducing VEV

## 8. Ready now vs. gated

**Ready**: movements I, II and III entire; the freedom ledger; the falsifier matrix; the recognition
table. **The thesis does not depend on anything still open.**

**One live row**: the ℙ³ cut ledger currently stands at dim 1 — one canonical linear condition, one
cubic, points needing zero (B1206), with all three named candidates closed (B1208). If codex's
answer on the ℤ/12 character of `l` and `eᶜ` comes back branch (b), the row **flips PERMANENT →
FORCED** and the paper gains a forced Higgs line. Branch (c) would instead give a new structural
negative (the lepton Yukawa absent). **Hold this row open in the draft; it is a row, not a rewrite.**

## 9. The currency hazard — what NOT to inherit

`docs/THE_SM_VERDICT.md` is the natural raw material and **must not be distilled directly.** It grew
by accretion: its §1 table still reads *"three generations, structurally"* (B897/B928) while its own
addenda — 220 lines further down — re-scope the generation count to the open-inputs side (B1033) and
state that the family count three is *exhibited, not forced*. A reader of the table never reaches the
correction. **P3 is written from the current state and each row re-checked against its arc**, not
edited down from that document. The same discipline applies to any row quoted from a ledger with
currency addenda.

## 10. Authorship, venue, sequencing

- **Venue**: J.Phys.A or IJMPA (math-phys, tolerant of a long structural argument with a negative core).
- **Authorship**: the owner's, as with cc3's series — the papers are the one place the name appears
  by design; the repo's attribution rules are unchanged.
- **Sequencing against cc3**: their four papers went submission-ready 2026-08-28. Their paper 4
  (*"What a class invariant cannot supply"*, 57K32) is a **narrow technical no-go** — three specific
  failures for m004, each with an escape route. It is a **component** of our boundary, not our thesis.
  **Preferred order: theirs first, ours cites them as established.** That converts an overlap into a
  citation and costs us nothing.
- **The archive layer** (never counted as papers): DOI'd repo snapshot at submission; the kill graph
  exported as a dataset appendix; the companion index mapping every paper claim → arc → test lock.

## 10b. The claim pool is SWEPT, not remembered (B1210)

This spec was drafted from the thesis as held in mind, and the sweep measured the cost: it cited
**11 of the 85 arcs banked in its own last ten days** and **1 of the corpus's 48 law-creating arcs**.
`CLAIM_CANDIDATES.md` beside this file is the mechanical counterpart — every `creates_law = true`
arc with a PROVED/NEGATIVE verdict, grouped by the section it would serve, with supersession flags.
**Regenerate it whenever the corpus moves** (`frontier/B1210_paper_spine_sweep/verification/`).

The sweep's own instrument needed correcting mid-run and that is worth carrying: a first pass
matched verbs anywhere in an arc's claim and flagged **15 of 24** spec citations as
extended/corrected/withdrawn — mostly noise, because an arc claim is one long sentence about many
things (it read B1159 as *withdrawing* B727 when it cites it, and B978 as withdrawing B862 when it
is the arc that *confirms* it). Clause-scoped matching — the verb within 90 characters of the
reference — gives **5 of 24**, and those five are real. **Report the second number.**

## 11. The build plan

1. **Freeze the claim list** — one line per claim, each with its arc and its lock. Anything without a
   lock does not enter the paper.
2. **Write §7 (the freedom ledger) first.** It is the spine; if it is honest and short, the paper works.
3. **Then §5 and §6** (the negative and the observer) — the parts no one else has.
4. **Then §3** (the forced side) — the easiest to write and the easiest to over-claim; write it last
   on purpose, under the discipline the earlier sections establish.
5. **The companion index built as we go**, not retrofitted.
6. **A hostile read before submission** — the P1 scrutiny-campaign pattern, pointed at our own draft.
