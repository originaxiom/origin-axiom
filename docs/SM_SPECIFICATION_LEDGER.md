# THE SM SPECIFICATION LEDGER — what a complete picture must supply

*Purpose (owner directive, 2026-08-08): "we don't yet fully understand the Standard Model
as today's science understands it, in order to know what our side should provide for a
complete picture." This ledger is the missing inventory. `INPUT_COMPLETENESS_LEDGER.md`
governs **how** to compare; `LITERATURE_GAUGE_SM_2026-07-13.md` maps what the literature
says fixes the SM. Neither states **what the SM actually specifies**. This does.*

**Firewall status:** this is a specification of accepted physics plus a column recording
what the object has delivered. It contains no value-matching and nothing promotes to
`CLAIMS.md`. Gate 5 untouched.

---

## A. The complete specification of the minimal Standard Model

### A1. Gauge structure

| item | content |
|---|---|
| algebra | **su(3)_C ⊕ su(2)_L ⊕ u(1)_Y** — dimension **8 + 3 + 1 = 12** |
| global form | the true group is **(SU(3)×SU(2)×U(1))/ℤ₆**, not the naive product — a genuine physical datum (it dictates allowed magnetic/line operators) |
| couplings | **g₃, g₂, g₁** — three numbers, measured |

### A2. Matter content — one generation, all as left-handed Weyl fermions

| field | (SU(3), SU(2))_Y | dim |
|---|---|---|
| Q | (**3**, **2**)_{+1/6} | 6 |
| u^c | (**3̄**, **1**)_{−2/3} | 3 |
| d^c | (**3̄**, **1**)_{+1/3} | 3 |
| L | (**1**, **2**)_{−1/2} | 2 |
| e^c | (**1**, **1**)_{+1} | 1 |
| *(ν^c)* | *(**1**, **1**)_0* | *1 — optional, sterile* |

**15 Weyl fermions per generation** (16 with ν^c — exactly the SO(10) spinor).
**Three generations**, identical in every quantum number, differing only in mass.

### A3. Scalar sector

One complex doublet **H = (1, 2)_{+1/2}**; potential V = μ²|H|² + λ|H|⁴ with μ² < 0.
Gives EWSB: SU(2)×U(1)_Y → U(1)_EM, three Goldstones eaten, one physical Higgs.

### A4. The free parameters — 19 in the minimal SM

| # | block | parameters |
|---|---|---|
| 1–3 | gauge | g₁, g₂, g₃ |
| 4–5 | Higgs | μ², λ (equivalently v = 246 GeV, m_H = 125 GeV) |
| 6–14 | charged-fermion masses | 3 up-type + 3 down-type + 3 charged-lepton Yukawas |
| 15–18 | quark mixing | 3 CKM angles + 1 CP phase |
| 19 | strong CP | θ_QCD (observed ≲ 10⁻¹⁰, unexplained) |

**+7 with massive Dirac neutrinos** (3 masses, 3 PMNS angles, 1 phase) → **26**;
**+2 Majorana phases** → **28**. Neutrino mass is beyond the minimal SM.

---

## B. What today's physics DERIVES vs takes as INPUT

This is the column that decides where a new theory can contribute at all.

### B1. FORCED (theorem-level, in accepted physics)

| fact | mechanism |
|---|---|
| **The hypercharges** | **anomaly cancellation** — [SU(3)]²U(1), [SU(2)]²U(1), [U(1)]³, U(1)-grav are Diophantine conditions that, given the group and the rep *structure*, fix Y up to normalisation. **This is the SM's only computed value-level structure.** |
| even # of SU(2) doublets | Witten's global ℤ/2 anomaly |
| asymptotic freedom of SU(3); β-signs | one-loop β-functions from the content |
| the unbroken subgroup after breaking | centralizer of the holonomy (Hosotani / Wilson line) |
| EWSB pattern, Goldstone count | Goldstone's theorem given the rep |

### B2. CHOSEN / MEASURED — derived by nothing

- **Why SU(3)×SU(2)×U(1)** at all *(the global ℤ₆ form is **derived** — B862)*
- **Why three generations** — derived nowhere in accepted physics
- **All 19 (26/28) parameters** — every one measured, none predicted
- Why m_H ≪ M_Pl (hierarchy), why θ_QCD ≈ 0 (strong CP)
- Neutrino mass mechanism and scale; the flavour hierarchy's *origin*
- Dark matter, dark energy, baryon asymmetry, gravity

> **The honest target for any "complete picture":** B2 is the entire opportunity. Anything
> in B1 that a theory "predicts" it has merely reproduced, and must say so.

---

## C. WHAT THIS OBJECT HAS DELIVERED, row by row

| SM requirement | object's delivery | status |
|---|---|---|
| the gauge **algebra** | second measurement lands on **su(3) ⊕ su(2) ⊕ u(1)³** (B892) | **PARTIAL — see §D1** |
| the global **ℤ₆** form | **DERIVED** — the cascade selects **[SU(3)×SU(2)×U(1)]/ℤ₆** (B862), resolving an ambiguity **the SM itself cannot fix** | **DELIVERED — the strongest row in this table** |
| **3 generations** | generation-shape structural (B897); D₂ carries the entire hierarchy (B928); orbit↔generation bijection (solo, unverified) | **structural, count matches** |
| 15/16 per generation | the **27** and its branchings; the 16 = SO(10) spinor appears in the chain | **structural** |
| **hypercharges** | **DERIVED (B864, 2026-08-03): hypercharge is the UNIQUE gaugeable U(1) in the chain's abelian sector.** Writing Q = aY + bχ + cψ over the generation, the anomaly conditions are grav = 5b+15c, [SU(3)]² = 2c, [SU(2)]² = 2c, **forcing b = c = 0 exactly**; ψ and χ are anomalous over the chiral matter (Tr ψ = 16, Tr χ = 5) so they *cannot* be gauged. **SCOPE: the DIRECTION is derived; the NORMALISATION is not and cannot be — anomaly conditions are homogeneous (B951)** | **DELIVERED (direction); normalisation not derivable in principle** |
| chirality | **not self-supplied** (B713, B760); chiral matter *constructible* via a closing (B582, B576) | **requires an external input** |
| sin²θ_W | **= 3/8** exactly, tree/GUT level (B919) | reproduces a **known GUT relation**, not a measured value |
| the 19 parameters | **none**. Three sealed crossings, three negatives (B915 16σ; B925 by algebra; B929 shape-only) — **and as of 2026-08-09 there is no live candidate to attempt a fourth with (B1005): every one of B687's 23 enumerated invariants is dead, Koide included (B686/B703/B743)** | **absent**; B936 says values are frame-relative, and **WHAT_WOULD_COUNT falsifier 2 has FIRED for the enumerated space** |
| CP | sign = sign(CS) (B303); phase second-order as 3.8·CS² (B340) | **ratio-shaped, untested against measurement** |
| strong CP, hierarchy, ν-mass, DM, gravity | not addressed | **absent** |

---

## D. THE FINDINGS THIS LEDGER IMMEDIATELY SURFACES

### D1. **su(3)⊕su(2)⊕u(1)³ is 14-dimensional. The SM's gauge algebra is 12.**

B892 banks: *"z(x₁, y*) = su(3) ⊕ su(2) ⊕ u(1)³ EXACTLY. Two measurements … take E₆ to the
Standard Model algebra."* Its own arithmetic is dim **14**, derived **11**, centre **3**.

**su(3)⊕su(2)⊕u(1)³ is not the Standard Model algebra.** It is the SM algebra **plus two
extra abelian factors**. The result is real and the arithmetic is right; **the sentence
overstates it.**

This is **not a refutation** — extra U(1)s are entirely standard in GUT descent (SO(10) →
SM leaves U(1)_{B−L}), and rank-6 E₆ descending to rank-4 SM must shed rank somewhere. But
it means the chain is **two steps from the SM, not zero**, and the missing steps are named:

1. **Which u(1) (or combination) is hypercharge?** — the `gauge_dict` obstacle, 48/79.
2. **What breaks the other two**, and at what cost?

### D2. The hypercharge derivation — **ALREADY DONE (B864)**, and this row was wrong

*(Corrected 2026-08-08 by B976. The original text called this "the sharpest available target"
and registered L132 to pursue it. **It had been derived on 2026-08-03.**)*

Anomaly cancellation is, by §B1, **the SM's only computed value-level structure**. And **B864
carried it out inside the chain**: over the chiral generation, ψ and χ are anomalous and
therefore ungaugeable, while **Y is the unique gaugeable direction** — b = c = 0 forced. The
cascade's "strip the dials" rule is thereby a **consequence of anomaly consistency**, not a
definition.

**What genuinely remains** is narrower still, and narrowed again on 2026-08-09: (i) the
**normalisation** is not derivable — anomaly conditions are homogeneous (B951); (ii) ~~whether the
object's u(1)³ from the SMT *is* the (Y, χ, ψ) triple is inferred, not computed (B953)~~ —
**COMPUTED AND SETTLED AFFIRMATIVELY by B992**: z_{e₆}(su(3)⊕su(2)) ∩ Cartan is **exactly
3-dimensional** and is the Levi's centre, while Y, χ and ψ each centralize su(3)_C ⊕ su(2)_L and are
all Cartan elements, so **span(Y,χ,ψ) = the second measurement's u(1)³**. *(B992 also records its
own failed first attempt: the same count on the **full** centralizer returns **9**, not 3 — the
extra 6 are root directions that cannot hold a Cartan element, so restricting to the Cartan is the
content, not a convenience.)*

**So (i) is the only item left in this row, and it is not a gap but a proven impossibility.**

### D3. What "complete" would actually require of us

Against §B2, a complete picture would have to supply: the group; the generation count *with
the reps*; the hypercharges; chirality *without an inserted closing*; and at least ratios
among the 19. **We currently have: the algebra with its u(1)³ now identified as span(Y,χ,ψ) (B992),
the global ℤ₆ form DERIVED (B862 — the one row where we outperform the SM), the generation count
structurally, chirality only via an external closing, and no values.**

**And on the last of those, the position hardened on 2026-08-09.** B1000 measured the external
inputs: **five closings over four incompletenesses**, charge taking **two** — a chirality sign *and*
a rank-reducing VEV — ~~which B963 proves compete for one resource~~ *(corrected 2026-08-10, B1017: the compete-corollary is retracted — the VEV closing is not effected by an involution; the two holes need two resources, the second unsourced)*. B1005 then fired
`WHAT_WOULD_COUNT`'s **falsifier 2**: **no live Tier-2 candidate remains**, since B687's atlas of 23
was the programme's own best enumeration and all 23 are now dead. **Scope, exactly: the falsifier
fires for the ENUMERATED space, not in principle** — "Tier 2 is unreachable" would be an overclaim;
*"Tier 2 has no live candidate"* is what is true, and it is enough to act on. **A fourth crossing
requires a candidate from outside B687's atlas and outside B743's tower.**

**And one row of §D is sharpened, not moved, on 2026-08-12 (B1048).** `WHAT_WOULD_COUNT`
grades **Tier 2** on a **scale lever**, and the corpus's last named candidate for one was the
**boundary-recruited pair (seam) channel**: `B408` banked it as *"the object's single scale-lever
candidate"* with a ratio of 1.2170 — **and killed it in its own body 27 lines later** (max over
embeddings is biased by embedding count; normalised ratio **0.7649 < 1**; *"the object has **no
scale lever in any tested channel**"*). **`B408`'s `arc_verdict` was always `NEGATIVE`, so nothing
in this ledger ever rested on the 1.2170 reading** — but the retraction row and the phrase registry
were 122 arcs late, and are added at B1048.

**What is new here is the strength of the closure, not its direction.** `B426` shows the three
*"real embeddings"* whose maximum produced 1.2170 are the **three Galois conjugates of one cubic
number** (minimal polynomial `1000x³ − 1500x² + 360x − 19` in `ℚ(ζ₉)⁺`, `√5`-free), whose
**arithmetic mean is exactly `1/2`, RMS exactly `√51/10`, geometric mean exactly `(19/1000)^⅓`** —
so **the seam channel's non-growth is a statement of Galois theory, not of statistics.** Scoped
exactly, because B426's own slogan over-reached and is corrected in the same commit: **the
power-mean family contracts for every `p` below `p* = 5.5932…`** and exceeds 1 only as it
degenerates toward `max` — the very bias B408 named. **Every genuine *average* contracts; "every
functional" is false** (`e₁ = 3/2`).

**Net effect on this ledger: none of the B2 rows move.** *"No live Tier-2 candidate remains"*
stands, and now the one candidate that was named is closed by a theorem rather than by a
diagnosis. Restored to `LAW_MAP` as **THE SCALE WALL CLOSES AT THE LEVEL OF GALOIS THEORY**
(B1048, restoring B426); see `docs/RETRACTIONS.md` and `docs/RETRACTED_PHRASES.md` rows 9–10.

---

## E. How to use this ledger

Any SM-facing cell states which row it targets, and whether that row is in **B1 (forced —
reproducing it is not a prediction)** or **B2 (open — the only place credit exists)**. A
cell claiming an achievement in B1 must say "reproduced", never "predicted".

**Maintenance:** rows change only with a banked arc, cited inline.
