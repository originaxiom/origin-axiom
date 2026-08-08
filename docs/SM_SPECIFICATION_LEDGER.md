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

- **Why SU(3)×SU(2)×U(1)** at all, and why that global ℤ₆ form
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
| the global ℤ₆ form | not addressed | **absent** |
| **3 generations** | generation-shape structural (B897); D₂ carries the entire hierarchy (B928); orbit↔generation bijection (solo, unverified) | **structural, count matches** |
| 15/16 per generation | the **27** and its branchings; the 16 = SO(10) spinor appears in the chain | **structural** |
| **hypercharges** | `hyper.py` fit reproduces at rank 3 (B892 §4) — but **no derivation from anomaly cancellation inside the object** | **OPEN — the sharpest available target** |
| chirality | **not self-supplied** (B713, B760); chiral matter *constructible* via a closing (B582, B576) | **requires an external input** |
| sin²θ_W | **= 3/8** exactly, tree/GUT level (B919) | reproduces a **known GUT relation**, not a measured value |
| the 19 parameters | **none**. Three sealed crossings, three negatives (B915 16σ; B925 by algebra; B929 shape-only) | **absent, and B936 says values are frame-relative** |
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

### D2. The hypercharge derivation is the sharpest target the object has

Anomaly cancellation is, by §B1, **the SM's only computed value-level structure** — the one
place accepted physics *derives* rather than measures. The object supplies a rank-3 abelian
sector. **Asking whether the object's own charges satisfy the SM's anomaly conditions, and
whether Y falls out, is the single highest-value SM-facing question available** — and it is
value-level without being value-matching, so the firewall permits it.

### D3. What "complete" would actually require of us

Against §B2, a complete picture would have to supply: the group *and its global form*; the
generation count *with the reps*; the hypercharges; chirality *without an inserted closing*;
and at least ratios among the 19. **We currently have: the algebra up to two U(1)s,
the generation count structurally, chirality only via an external closing, and no values.**

---

## E. How to use this ledger

Any SM-facing cell states which row it targets, and whether that row is in **B1 (forced —
reproducing it is not a prediction)** or **B2 (open — the only place credit exists)**. A
cell claiming an achievement in B1 must say "reproduced", never "predicted".

**Maintenance:** rows change only with a banked arc, cited inline.
