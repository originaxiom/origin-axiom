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
| **hypercharges** | **DERIVED (B864, 2026-08-03): hypercharge is the UNIQUE gaugeable U(1) in the chain's abelian sector.** Writing Q = aY + bχ + cψ over the generation, the anomaly conditions are grav = 5b+15c, [SU(3)]² = 2c, [SU(2)]² = 2c, **forcing b = c = 0 exactly**; ψ and χ are anomalous over the chiral matter (Tr ψ = 16, Tr χ = 5) so they *cannot* be gauged. **SCOPE: the DIRECTION is derived; the NORMALISATION is not and cannot be — anomaly conditions are homogeneous (B951).** *The layer's remaining content is now KNOWN to be exhausted (2026-08-20, B1096): over the object's own DERIVED 16, with ν^c, every anomaly channel vanishes identically — see §D4.* | **DELIVERED (direction); normalisation not derivable in principle** |
| chirality | **not self-supplied** (B713, B760); chiral matter *constructible* via a closing (B582, B576) — **a new closing is now on the table** (B1098: the object's own non-abelian holonomy lands at rank exactly 4, su(3)⊕su(3), with a complex 27 witnessed at that landing, B1100) but it is a PRICED CHOICE (1-of-20 sl₂ classes, ~4.3 bits, no selection mechanism claimed), not a derivation, and chirality **at count** is explicitly not claimed there (the four-language wall — B1083/B1084/B1086/B1087 — stands; EWSB outside). See §D4. | **requires an external input; the menu of candidate closings has grown by one, still unpriced-to-zero** |
| sin²θ_W | **= 3/8** exactly, tree/GUT level (B919) | reproduces a **known GUT relation**, not a measured value |
| the 19 parameters | **none**. SEVEN sealed crossings, seven negatives *(updated 2026-08-19 by the stale-absence sweep — this row previously stopped at three)*: B915 16σ; B925 by algebra; B929 shape-only; then a candidate class from OUTSIDE B687's atlas was licensed (the coupling channel, KIND_TABLE/B1020) and run to exhaustion under seal — B1027+B1063 (phases, MISS both sectors), B1066 R-A (probability, MISS), B1066 R-B (tones-vs-sin²θ, MISS), B1075 (tones-vs-moduli, MISS at power, 2026-08-19). B1005's every-enumerated-invariant-dead verdict stands for B687's atlas; the coupling channel's value story is now ALSO closed by its own four seals — B1066's own verdict: *"the value wall stands complete."* See §D5 for what this does and does not leave open. | **absent**; B936 says values are frame-relative, and **WHAT_WOULD_COUNT falsifier 2 has FIRED for the enumerated space AND the licensed coupling channel** |
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

*(2026-08-20: a SECOND, structurally different route to rank 4 now exists alongside this one
— see §D4. It does not answer item 2's question about the compact chain's own u(1)³; it is a
separate landing that reaches rank 4 by an entirely different mechanism, the object's own
non-abelian holonomy rather than a sequence of centralizer measurements.)*

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
*(And, as of 2026-08-20, the layer it sits inside is proven to hold nothing further either way —
see §D4.)*

### D3. What "complete" would actually require of us

Against §B2, a complete picture would have to supply: the group; the generation count *with
the reps*; the hypercharges; chirality *without an inserted closing*; and at least ratios
among the 19. **We currently have: the algebra with its u(1)³ now identified as span(Y,χ,ψ) (B992),
the global ℤ₆ form DERIVED (B862 — the one row where we outperform the SM), the generation count
structurally, chirality only via an external closing (now TWO named candidate closings, §D4), and no values.**

**And on the last of those, the position hardened on 2026-08-09, and hardened again through
2026-08-19.** B1000 measured the external inputs: **five closings over four incompletenesses**,
charge taking **two** — a chirality sign *and* a rank-reducing VEV — ~~which B963 proves compete for
one resource~~ *(corrected 2026-08-10, B1017: the compete-corollary is retracted — the VEV closing
is not effected by an involution; the two holes need two resources, the second unsourced)*. B1005
then fired `WHAT_WOULD_COUNT`'s **falsifier 2**: **no live Tier-2 candidate remains**, since B687's
atlas of 23 was the programme's own best enumeration and all 23 are now dead. **Scope, exactly: the
falsifier fires for the ENUMERATED space, not in principle** — "Tier 2 is unreachable" would be an
overclaim; *"Tier 2 has no live candidate"* is what is true, and it is enough to act on. **A fourth
crossing requires a candidate from outside B687's atlas and outside B743's tower** — met, and then
exhausted: the coupling channel was that candidate, licensed under exactly this bar, and it too is
now spent (four more sealed crossings, four more MISSES — §D5). **As of 2026-08-19, an EIGHTH
crossing needs a candidate outside B687's atlas, outside B743's tower, AND outside the coupling
channel — a strictly higher bar than the one this paragraph originally set.**

### D4. THE RANK WALL'S NON-ABELIAN HATCH — a new, priced, still-incomplete route (2026-08-20)

D1 asked what breaks u(1)³'s extra rank down to the SM's, at what cost. The compact-chain route
(successive centralizer measurements) answers **no route at all**: B952 proved measurement
preserves rank; B959 proved every semisimple/toral construction on the object's actual finite
images (A₄, D₅, S₅) does too, and the outer-automorphism route reaches rank 4 only by making the 27
real; B960 closed the one remaining toral hatch (the adjoint form has no 27 to protect, so the
simply-connected form — where B959's torality argument applies without qualification — is forced by
the mere presence of matter). **B959's headline is now RE-SCOPED, beside its own sealed text**
(`frontier/B959_nontoral_rank4/ADDENDUM_2026-08-20_RESCOPE_TO_TORAL.md` — the addendum is the
citation; nothing sealed was edited), to **"every TORAL route to rank 4 makes the 27 real"** — its
proof never covered the nilpotent stratum, and B1094 named that gap as the wall's one live hatch.

**A genuinely different route now exists, and it does not go through the compact chain's u(1)³ at
all.** B1098 enumerates all twenty sl₂ conjugacy classes of e₆ constructively (saturating the cited
Bala–Carter count, every centralizer's dimension/rank/type matching the standard table) and shows
the object's own hyperbolic holonomy, composed with the A2 class's principal sl₂ (the smallest
faithful representation of the object's fundamental group, Zariski-dense — the density lemma making
every centralizer the unbroken algebra of the object's actual composed holonomy, not a hypothetical
one), lands at **su(3)⊕su(3), rank exactly 4, zero extra u(1)s** — color in one factor, su(2)×u(1)
in the other. This is a **priced choice** (1 of 20 classes, ~4.3 bits, no dynamical selection
mechanism claimed), not a derivation, and it is a separate landing from D1's u(1)³ discussion, not
a repair of it.

**B1100 computed the landing's matter exactly.** The joint weight table tiles the 27 exactly (six
spin-1 triplets plus nine singlets — (3,3̄,1)⊕(3̄,1,3) as triplets, (1,3,3̄) as singlets under the
eaten factor — the trinification branching at proof grade); **the 27 IS complex there** — a
multiplicity-3 weight class with an absent negation class, a basis-free witness — which falsifies
B959's original headline **beyond its toral scope** while leaving B959's proof untouched on its own
toral ground; the hypercharge test is compatible at pattern/generic level (the bijective form is
exactly excluded; the collapse form's degeneracy pattern is hit by the first random direction tried,
not a tuned point), with the exact value-match named as a residual, not silently dropped.

**What this changes, and what it does not.** Changes: D1's "missing steps" are no longer the only
route on the table — there is now a second, independently-derived rank-4 landing with matter
content, structurally unlike the compact chain's. Does not change: chirality **at count** is still
not claimed (the four-language wall — B1083 the origin torsor, B1084 the flat G₂ collision geometry,
B1086 the spectrum law proving chirality-at-count is ZERO on any closed assembly, B1087 the
charge/holonomy non-commutativity — stands over both routes, per B1098's own fence); EWSB remains
outside; the class-choice's ~4.3 bits are priced but not derived.

**Door 5, closed the same week (B1096).** B167's oldest surviving "the wall has no internal door"
lane (`docs/OPEN_LEADS.md` L144) asked whether the one QFT-legal thing a scale-free object may say —
an RG-invariant 't Hooft anomaly, evaluable without a scale — could carry a genuine SM ratio.
Computed exactly over the object's own DERIVED 16 (the chiral content **with** ν^c): every channel
vanishes identically, including the two the imported 15 fails ((B−L)³, (B−L)-gravitational) —
**ν^c, the field the object derives (B876), is exactly what cancels the last non-vanishing
invariant**, and the ℤ₆ global-form congruence 6Y ≡ 4·triality + 3·duality (mod 6) has that unique
solution by exhaustion over all 36 pairs. A layer that vanishes identically cannot supply a ratio;
the door is shut structurally, not merely unexplored — this closes L144.

**Jointly with B1092's purity selector** (the second VEV is a condition on an 11-dimensional cone,
not a point — the same derived ν^c: completeness of the anomaly content and the purity condition on
the VEV side are two faces of one fact), the current honest sentence for THE RANK WALL is: **one
unsourced slot, pair-space-valued, purity-conditioned, arithmetically unobstructed on its
coarse-group half (B1099: the full-group integral orbit is unique at the object's own squarefree
invariant) — open routes = Route A's owed counter-identification (named frontier mathematics,
B1099: no theorem in the literature searched counts integral orbits for this exact classifying
pair) and the non-abelian hatch's still-unpriced selection mechanism; closed routes = every toral
door, twice over, and the anomaly layer, completely.**

### D5. THE VALUE LAYER'S HONEST STATE (2026-08-20)

**Seven sealed crossings, seven negatives**, full account in §C's "the 19 parameters" row. **The
coupling channel is CLOSED** — B1066's own verdict is the section: *"every legal value-adjacent form
has now been posed and answered. The value wall stands complete."* Nothing about the underlying
**instrument** (B593/B856/B1011's welded coupling construction, the Listening Protocol, the
listener-map problem statement) was spent by this: instruments are `instrument: true` in the
corpus's own vocabulary (`docs/PRACTICES.md`), methodology rather than claims. What was spent,
one-shot per crossing (B1063's precedent), is the sealed act of pointing a finished instrument at
data, priced jointly by `docs/CROSSING_REQUIREMENTS.md`'s requirements and
`docs/INPUT_COMPLETENESS_LEDGER.md`'s twelve items (reconciled 2026-08-13: eight shared, four
genuine gaps) — together the programme's **measurement price-list**.

**Two directions remain licensed, and both are computations, not data contacts.** The
coboundary/hierarchy lane (B1074: the hierarchy is coboundary-carried, invisible to H¹; B1076: the
full four-gauge coboundary sweep, two gauges never computed before, finds no value-bearing coset
invariant anywhere, paying its own way in theorems — CCC = 3!·λ coset-wide, a new sign character,
the denom⁴ law) is DECIDED CLOSED at the coset level it tested and hands off *nature supplies the
gauge: which datum picks the coboundary element* as the successor question, with **three named
structural doors as the value layer's only remaining licensed direction — B1076's own targets**:
the gauge-datum question, L154's σ-identification, and B882's arithmetic-S₃-equals-geometric-S₃
conjecture. The listener map's own further identification is named the coupling channel's sole
residual door (B1066) but may not reopen any spent pairing without a wholly new seal
(`docs/LISTENER_MAP_SPEC.md` F2).

**The value layer's emptiness is a fact about values, not about structure — and that second
question has its own single open node.** THE WHY CAMPAIGN's Lane I-3, **the compression question**
— assembling `docs/THE_CLAIM.md`'s controls with Lane I-1's freedom-ledger number (B1028: 0.000
retroactive designer bits against a 4.585-bit conservative output floor) into one sealed compression
statement — has not been banked as its own cell as of B1101. It is the one open node standing
between "nothing was found" and "nothing was ever going to be found, and here is the computed reason
why."

---

## E. How to use this ledger

Any SM-facing cell states which row it targets, and whether that row is in **B1 (forced —
reproducing it is not a prediction)** or **B2 (open — the only place credit exists)**. A
cell claiming an achievement in B1 must say "reproduced", never "predicted".

**Maintenance:** rows change only with a banked arc, cited inline; a change landing while a
certifying suite is running follows the certification envelope (`WORKING_RULES.md` §CE; B1101):
staged in the scratchpad, landed by explicit filename, digests entered by command substitution and
re-verified by the live `seal-digests` gate.

## Currency read 2026-08-13 (window B1018–B1064; head B1064)

- **The CP-phase channel is CLOSED at the value layer (B1063):** the pre-committed NuFIT
  refresh executed once against 6.0 — all four sealed variants miss both targets, the
  decisive clause fired (2.21× tightening), the one-shot is SPENT, routed to the kill
  graph hatch-closed. Any HK/DUNE-era re-pose is a new arc under a new seal. No row moves
  from B2 to B1; the channel's specification row simply records its tested-and-closed state.
- **The B1 side gained citation-grade external confirmation (the novelty sweep,
  `docs/NOVELTY_SWEEP_LEDGER.md`):** sin²θ_W = 3/8's value AND derivation route are
  standard (opened source), T-SMT's endpoint and SU(5)-skipping route are standard
  (Slansky, trinification) — B1-row reproductions correctly labeled "reproduced" all
  along; the sweep's twelve layer-only KNOWNs are the cost-claim's other half.
- **Crossing preregs now fill BOTH checklists** (this ledger's companion rule from THE
  RECONCILIATION in `docs/INPUT_COMPLETENESS_LEDGER.md`): the crossing lane's R1–R11 AND
  the twelve, N/A written as a row — four gap-items (scheme, multi-modal, fit-vs-direct,
  the matched null's hit-branch) cannot ride the R-list alone.

## Currency read 2026-08-20 (window B1065–B1101; head B1101)

- **The coupling channel's closure is now named at ledger level, not left implicit in a row
  update.** §C's "the 19 parameters" row and §D5 carry the full seven-crossing account and the
  instrument/price-list framing; this entry is the pointer.
- **THE RANK WALL moved for the first time since B960, and Door 5 closed structurally** — full
  account in §D4. B959's headline is re-scoped to toral routes beside its own sealed text; the
  non-abelian hatch is open (B1098) with its landing's matter exact and its 27 proved complex
  (B1100); the anomaly layer over the object's own derived content is now known to be exhausted
  (B1096).
- **THE CERTIFICATION ENVELOPE (B1101; `WORKING_RULES.md` §CE)** now governs how any future
  row-change to this ledger lands during a certifying suite, backed by the live `seal-digests`
  gate — see §E.

## Currency read 2026-08-22 (head B1133) — the value question is closed: DISJOINT

The value campaign + value-probe wave (B1124–B1133) tested whether the object supplies the
SM's dimensionless VALUES through every route: tower periods (V-3/B1126), the object's own
natural invariants (B1129), the principled listener-map coupling (B1128, null on the full
sphere per B1132), the two-ended tower (B1133: SINGLE-END, ℚ(√−3) only), and the sharpest
coincidence (B1131: |det φ|=2/3 vs Koide, proven a coincidence). **All negative.** The
object's arithmetic reproduces (C₀–C₄ trace-field, B1124/B1133) but is **DISJOINT** from the
SM's numbers — "physics-shaped, not physics-valued." So every **VALUE** slot in this ledger
remains externally-supplied: the object supplies the STRUCTURE (algebra, the ℤ₆ form,
hypercharge direction, generation shape, the compact-color FORM M(𝕆,ℂ)) but not the numbers.
This is the ledger's value-side verdict, closed by a symmetric sealed sweep — not lowered
ambition; the named-open remainders are only precision (C₅+) and any future out-of-menu
structure. (This read joins the doc-currency watch; head B1133.)
