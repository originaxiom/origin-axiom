# B970 / L134 — PRIOR-ART SCOUT: the twelve (eleven) exotics of the 27

**Date:** 2026-08-08 · **Lane:** scouting only — **no verdict on the object is offered here.**
**Deliverables:** this file, `prior_art_exotics.json`, `exotics_charges.py`, `exotics_charges.json`.
**Firewall:** specification of accepted physics + a repo audit + one supporting computation.
No value-matching. Nothing promotes to `CLAIMS.md`. Gate 5 untouched.

---

## THE SCOUT'S FOUR ANSWERS, UP FRONT

| | question | answer |
|---|---|---|
| **(a)** | is L134 a discovery? | **NO — it is ~70 % a REPRODUCTION.** The literature half is already banked, twice, in `B951` and `B962`. The ledger's "never addressed" is **false as written** and must be amended. |
| **(b)** | what does E₆ model-building require? | a mass from `κ S D D̄`, with `⟨S⟩` = the **U(1)′-breaking VEV**; a discrete symmetry to kill either the leptoquark **or** the diquark couplings; collider + BBN bounds if light. |
| **(c)** | input or derived? | **INPUT — and, sharper, not even an *additional* input.** It is the **same** input as the 27 VEV, consumed at the **same** step. **Structurally identical to the VEV situation; not a defect peculiar to this object.** |
| **(d)** | is there a no-go? | **no absolute no-go found** (one null certified, others not). There **is** a sharp **conditional** no-go (a trilemma) and a **structural bound**, both stated below. |

---

## 1. (a) WHAT THE REPO ALREADY HAS — the grep, run first

**Search terms:** `exotic`, `16 + 10 + 1`, `leptoquark`, `diquark`, `D Dbar`, `vector-like`,
`vectorlike`, `extra doublet`, `R-parity`, `Z'` — over `frontier/*/FINDINGS.md`, `docs/*.md`,
`knowledge/*.md`, `CLAIMS.md`, and all `*.py`.

### 1.1 The exotic sector IS treated — in two scout documents

| where | what it already establishes |
|---|---|
| **`frontier/B951_l132_scout/PRIOR_ART_HYPERCHARGE.md`**, §"The exotics in 10 + 1, and the requirement that they be heavy" | Names the content: the colour-triplet `Q = −1/3` isosinglet pair **D, Dᶜ** (Robinett's "h"), the exotic doublet pair **H_u, H_d** (the `E, ν_E` leptons), the singlet **S**. Quotes **Langacker RMP 81 (2009) 1199 verbatim** on `W_DQ ~ DQQ`, `Dᶜuᶜdᶜ` and `W_LQ ~ Duᶜeᶜ`, `DᶜQL` ⇒ **rapid proton decay unless their masses (and hence the U(1)′ breaking scale) are comparable to the unification scale**; a TeV Z′ therefore requires the GUT Yukawa relations to be violated. Cites Robinett PRD 33 (1986) 1908 [17444], Rizzo PRD 33 (1986) 3329 [219732] and PRD 34 (1986) 2163 [227115], Hewett–Rizzo Phys.Rept. 183 (1989) 193 [268529], Rosner PRD 61 (2000) 097303 [525750]. |
| **`frontier/B962_vev_scout/PRIOR_ART_VEV.md`**, §Q5c "Exotics, proton decay, doublet–triplet" | The `SU(5)×U(1)_N` branching `27 → (10,1)+(5̄,2)+(5̄,−3)+(5,−2)+(1,5)+(1,0)`; the **vector-like colour-triplet pair D, D̄** of charge ∓1/3; "the exotics are unavoidable — they come with the representation"; **B/L violation is not gauge-forbidden**, suppression needs an **ad hoc discrete symmetry** (`Z₂^L` ⇒ diquarks, `Z₂^B` ⇒ leptoquarks); doublet–triplet splitting is **routed around, not solved** (triplets kept light at TeV with mass from `⟨S⟩`); F-theory version suppresses proton decay geometrically. |
| `docs/GUT_REQUIREMENTS_LEDGER.md` §B | states the exotics and the heaviness requirement, and (§C row 3′) marks them **"not addressed anywhere in the record — absent, a named gap"**. |
| `PROGRESS_LOG.md`, `docs/THE_SM_VERDICT.md`, `docs/OPEN_LEADS.md`, `frontier/B952_gut_ledger_rank/FINDINGS.md` | all four repeat "**twelve exotic states per generation … the record has never addressed them**". |
| `speculations/S049_the_self_mirror_and_matter.md` | notes `16+10+1` is the *physical* decomposition and that the object's principal grading `{17,9,1}` is **not** it. Not about the exotics' mass. |
| `B925`, `B932`, `B590`, `B571`, `B926`, `B298` | the branching `16+10+1` recurs as data. **None treats the exotic sector.** |

### 1.2 CERTIFIED NULLS (exhaustive within their stated scope)

- **N1 — no computed cell.** `grep -rl "exotic|leptoquark|diquark|Dbar"` over **every** `*.py` in
  `frontier/`, `src/`, `scripts/` returns 6 files, and **inspection shows every hit is an
  unrelated use of the word "exotic"** (`B272`, `B278`, `B298`, `B773`, `B778`) plus this cell's
  own new file. **No computation anywhere in the repo has ever touched the exotic sector.**
  **CERTIFIED.**
- **N2 — nothing in the claim layer.** `CLAIMS.md` and `knowledge/` contain **zero** occurrences of
  `exotic`, `leptoquark`, `diquark`. **CERTIFIED.**
- **N3 — no no-go among the modern citers.** Complete citation-graph closure on the canonical
  modern paper (Kang–Langacker–Nelson, recid **758656**): **all 107 citers enumerated
  individually**; **none** claims E₆ exotics cannot be made heavy. **CERTIFIED** (scope: that
  citer set only).

### 1.3 THE VERDICT ON (a)

> **L134's literature half is a REPRODUCTION.** Two prior scouts already established the
> content, the mass mechanism, the proton-decay constraint and the discrete-symmetry fix.
> **What is genuinely absent is the *computation*** — §2 below is the first time anything about
> the exotic sector has been derived on this bench.
>
> **Amendment owed:** `GUT_REQUIREMENTS_LEDGER.md` §C row 3′ ("not addressed anywhere in the
> record") is **wrong**; it should read *"literature-scouted in B951 §exotics and B962 §Q5c;
> **no computed cell**"*. The same correction is owed in `THE_SM_VERDICT.md` §5 row 2,
> `OPEN_LEADS.md` L134, and `PROGRESS_LOG.md`.

### 1.4 AN ARITHMETIC CORRECTION THE REPO NEEDS — **eleven, not twelve**

The ledger says, verbatim: *"**10 + 1 = 12 states per generation are EXOTIC**"*. **10 + 1 = 11.**

Counted from the weights (`exotics_charges.py`, `STATE_COUNTS`):

| block | states |
|---|---|
| the **27** | 27 |
| the **16** | 16, of which **ν_R** = 1 ⇒ a 15-fermion SM generation |
| the **10** of SO(10) | 10 |
| the **1** of SO(10) | 1 |
| **10 + 1 = exotics beyond the 16** | **11** |
| **27 − 15 = states beyond a 15-fermion generation** | **12** |

> **Both numbers are right, of different things.** "Twelve" is the count against a **15**-fermion
> SM generation and therefore **includes ν_R**. The repo's sentences say *both* "the 16 is one SM
> generation **with a right-handed neutrino**" *and* "the 10 + 1 are **twelve**" — those cannot
> both hold. **Fix: say "eleven exotic states beyond the 16 (twelve beyond a 15-fermion
> generation, counting ν_R)".**
> *Not certified:* whether "twelve" is standard literature phrasing was **not** confirmed — the
> web-search budget was exhausted. The arithmetic, however, is not in doubt.

---

## 2. THE COMPUTATION — done here, in-sandbox, cited from nothing

`exotics_charges.py`. Built from the **E₆ Cartan matrix only**: the 27 as the Weyl orbit of ω₁
(minuscule, so the orbit algorithm is exact and complete — asserted, 27 weights, all Dynkin
labels in {−1,0,1}); U(1)_ψ graded by n₁ and U(1)_χ by (n₁, n₂), which is *forced*, not an
ansatz, because a functional annihilating the so(10) [resp. su(5)] simple roots is affine in n₁
[resp. (n₁,n₂)]; hypercharge constrained to the **su(5) Cartan** so it carries no constant term.

**The fits are predictive, not imposed.** ψ was fitted on the **1** and the **16** and
**predicted** ψ(**10**) = −2. χ was fitted on the 16's three pieces plus the singlet and
**predicted** the 10's two pieces at **+2, −2**. Y was fitted on the **16 only** and
**predicted** Y(S) = 0, Y(ν^c) = 0 and the entire exotic 10.

### 2.1 The 27, with every quantum number derived here

| piece | SU(3)×SU(2) | dim | Y | Q_em | ψ | χ | role |
|---|---|---|---|---|---|---|---|
| `S` | (1,1) | 1 | 0 | 0 | **4** | 0 | **EXOTIC** (the **1**) |
| `5̄_SU5` | (3,1) | 3 | 1/3 | 1/3 | 1 | 3 | SM (16) |
| `5̄_SU5` | (1,2) | 2 | −1/2 | 0, −1 | 1 | 3 | SM (16) |
| `10_SU5` | (1,1) | 1 | 1 | 1 | 1 | −1 | SM (16) |
| `10_SU5` | (3,2) | 6 | 1/6 | 2/3, −1/3 | 1 | −1 | SM (16) |
| `10_SU5` | (3,1) | 3 | −2/3 | −2/3 | 1 | −1 | SM (16) |
| `ν^c` | (1,1) | 1 | 0 | 0 | 1 | −5 | SM (16) |
| `5_SU5` | (1,2) | 2 | **+1/2** | 1, 0 | **−2** | 2 | **EXOTIC** — `H_u` |
| `5_SU5` | (3,1) | 3 | **−1/3** | **−1/3** | **−2** | 2 | **EXOTIC** — `D̄` |
| `5̄_ex` | (3,1) | 3 | **+1/3** | **+1/3** | **−2** | −2 | **EXOTIC** — `D` |
| `5̄_ex` | (1,2) | 2 | **−1/2** | 0, −1 | **−2** | −2 | **EXOTIC** — `H_d` |

The exotic sector is exactly what the lead described — a **charge ∓1/3 vector-like colour-triplet
pair**, a **vector-like doublet pair**, and a **singlet** — and here that is *derived*, not quoted.

### 2.2 The four results that matter

**R1. No bare mass exists anywhere inside a single 27.** Zero bilinears have (ψ,χ) = (0,0).
*MB12: this test can pass* — a self-conjugate rep such as the **26** of F₄ does contain
charge-conjugate pairs — *and it can fail*. It is a real test, and it fails.

**R2/R3. The mass-giving direction is unique, and it is the highest weight.** The exotic pair
carries total ψ = −4, χ = 0, so any VEV giving it mass must carry **(ψ, χ) = (4, 0)**. Inside the
27 **exactly one direction does: S** — and `S` is **ω₁ itself**, the highest weight, i.e. **the
rank-1 element of J₃(𝕆) whose E₆ stabiliser is Spin(10)** (`B962`'s computed orbit result).

**R4. The exotics are SM-vector-like and χ-vector-like but ψ-CHIRAL.** Computed:
`vectorlike under {SM: true, U(1)_χ: true, U(1)_ψ: FALSE}`. **U(1)_ψ alone protects them.**

**R5. Therefore, and this is rep-independent:**

> ### **exotic mass ≠ 0 ⟹ U(1)_ψ is broken.**
> The operator carries ψ = −4 as a fact about the E₆ **weight lattice**. Any field, in **any** E₆
> representation, whose VEV gives the exotics a mass carries ψ = +4 ≠ 0 and therefore breaks
> U(1)_ψ. There is no evasion by enlarging the Higgs sector.

**R6. Both dangerous couplings live in the *same* invariants as the ordinary Yukawas.** The
weight-sum-zero test (Sym³(27) contains the E₆ singlet once, so a monomial occurs iff the three
weights sum to zero) gives **exactly four** cubic monomial classes:

| monomial | multiplicity | what it is |
|---|---|---|
| `10 · 10 · 5` | 15 | **up-type Yukawa** (via `H_u`) **and the DIQUARK** `QQD̄` (via `D̄`) |
| `10 · 5̄ · 5̄_ex` | 20 | **down/lepton Yukawa** (via `H_d`) **and the LEPTOQUARK** `QLD`, `u^c e^c D` (via `D`) |
| `5 · 5̄ · ν^c` | 5 | Dirac neutrino |
| `5 · 5̄_ex · S` | 5 | **the exotic mass term** `κ S D D̄` |

This is **why** Langacker's constraint is structural rather than accidental: the Higgs doublets
and the exotic triplets sit in the **same two multiplets**, so the leptoquark and diquark
operators are *components of the very invariants that give the quarks their masses*.
*(The SU(5) tensor structures 10×10 ⊃ 5̄ and 10×5̄ ⊃ 5 are standard SU(5) algebra — cited, not
re-derived; the E₆ charge selection and the monomial census above **are** derived here.)*

**SCOPE.** Everything in §2 is scoped to the GUT chain **E₆ ⊃ SO(10)×U(1)_ψ ⊃ SU(5)×U(1)_χ×U(1)_ψ**,
and "the exotics" means the **10 + 1** of *that* SO(10). It says nothing about the object's own
cascade, whose u(1)³ is a different torus.

---

## 3. (b) WHAT E₆ MODEL-BUILDING ACTUALLY REQUIRES

### 3.1 What gives them mass, and at what scale

**One mechanism, everywhere: `W ⊃ κ_ijk S_i D_j D̄_k`, so `M_D = κ⟨S⟩`.**
Confirmed independently in three sources read this sweep:

- **Kang, Langacker & Nelson**, PRD 77 (2008) 035003 [arXiv:0708.2701, recid 758656]:
  *"a supersymmetric mass arises from the vev of a singlet field S"*; the `λ⁵ S D D^c` term gives
  `m_D = λ⁵ s`. Scalars additionally get soft masses. Benchmarks 300–1482 GeV.
- **King, Moretti & Nevzorov**, E₆SSM review [arXiv:2002.02788]: `κ_ijk S_i (D_j D̄_k)`, with
  *"⟨S₃⟩ = s/√2, breaking U(1)_N gauge symmetry"*, the same VEV *"responsible for the effective
  μ term and D-fermion masses"*.
- **Halverson & Langacker**, TASI [arXiv:1801.03503]: *"the electroweak and U(1)′ breaking scales
  are typically both set by the soft supersymmetry breaking and μ scales. Thus, the Z′ and
  related exotic masses are usually not too much larger than the superpartner masses."*

**The scale is therefore not free — it is the U(1)′-breaking scale.** Two branches exist and
nothing selects between them:

| branch | ⟨S⟩ | exotics | Z′ | cost |
|---|---|---|---|---|
| **GUT-scale** | ~10¹⁶ GeV | decoupled, invisible | at M_GUT | no low-energy E₆ phenomenology at all |
| **TeV-scale** (E₆SSM and kin) | ~TeV | **TeV, light by construction** | TeV | needs discrete symmetries; proton decay is the problem |

`M_D / M_Z′ = κ / (g′ Q_S)` up to O(1) — a **ratio of couplings, not of scales**. Perturbativity
on κ therefore caps how far the exotics can be pushed above the Z′. This is the quantitative
form of R5.

### 3.2 What constrains them

1. **Proton decay — the binding constraint.** Both leptoquark and diquark operators are present
   (R6, computed). Simultaneous presence ⇒ rapid proton decay. **Fix used everywhere: an *ad hoc*
   discrete symmetry** — `Z₂^L` (exotics become diquarks) or `Z₂^B` (leptoquarks), never both
   allowed. Kang–Langacker–Nelson: *"the simultaneous presence of diquark and leptoquark
   operators"* is forbidden by fiat. Nevzorov [1205.5967] proposes a single `Z̃₂^H`.
2. **Langacker's trilemma** (verbatim, banked in `B951`, quoted from RMP 81 (2009) 1199 —
   **cited, not re-derived**): the D, Dᶜ couplings *"are related by E₆ to the ordinary Higgs
   Yukawa couplings"* and give rapid proton decay *"unless their masses (and therefore the U(1)′
   breaking scale) is comparable to the unification scale. A TeV-scale Z′ therefore requires that
   the GUT Yukawa relations are not respected."*
3. **Collider.** Kang–Langacker–Nelson quote m_D ≳ 250 GeV (Tevatron leptoquark) and ≳ 190 GeV
   (quasi-stable). **Stale — 2008 vintage.** Modern LHC vector-like-quark pair-production bounds
   (ATLAS/CMS, recid 1628648, 1353390, 1711260 …) sit near 1.3–1.5 TeV. **Not re-derived here.**
4. **Cosmology.** If the exotics are quasi-stable (decay only through dim-5 operators),
   Kang–Langacker–Nelson §III.3 gives full **BBN** constraints in the (τ, Y_X) plane across the
   10⁻²–10¹² s windows.
5. **A requirement that is easy to miss.** Nevzorov [1205.5967, abstract]: E₆-inspired models
   *"must also include additional TeV scale vectorlike lepton or vectorlike down type quark
   states to render the lightest exotic quark unstable."* **Making the exotics heavy is not the
   end of the obligation — you must also make the lightest one decay.**
6. **Anomalies, and the tie to L132.** King–Moretti–Nevzorov: *"the anomalies are cancelled
   automatically if the low-energy spectrum involves complete representations of E₆"* — so
   **projecting the exotics out costs you automatic anomaly freedom**, and the anomaly check
   becomes non-vacuous exactly when the spectrum is incomplete. This is precisely L132's amended
   gate, arrived at from the other side.

---

## 4. (c) THE SHARP QUESTION — **INPUT, and the *same* input**

**It is an input.** `M_D = κ⟨S⟩` has two free parameters and **nothing derives either**. No source
found this sweep derives the exotic mass scale from anything.

**But the honest statement is stronger than "an input", and it goes the object's way:**

> **Making the exotics heavy is not an *additional* input on top of the 27 VEV. It is the
> *same* input, consumed at the *same* step.**
>
> Computed (R2/R3/R5): the unique direction in the 27 that gives the exotics mass is **S**, which
> **is ω₁, the rank-1 element of J₃(𝕆)**, whose E₆ stabiliser is **Spin(10)** — exactly the VEV
> `B962` already identified as the first of the two forced 27 VEVs. `⟨S⟩ ≠ 0` **is** the step
> `E₆ → SO(10)`, i.e. rank 6 → 5. **So L134 is entailed by the rank-reduction question already
> registered and closed as L133 — it is a corollary, not a second gap.**

**Consequences for how the programme should describe itself:**

- **L134 is structurally identical to the VEV situation** (`B962`'s headline: *the VEV direction
  is always an input; nobody's object supplies one*). **It is not a defect peculiar to this
  object**, and it should not be written up as one.
- **L134 should be merged into the VEV/rank row of the ledger, not carried as an independent
  open item.** Carrying it separately double-counts one gap.
- **The one thing L134 adds that the VEV row does not:** a *sign* that the input is the right
  kind. The selection rule — *which* direction, uniquely — **is** derived, and it lands on the
  same rank-1 orbit the programme already computed. That is a consistency check the programme
  passes, not a new failure.

**The one partial-derivation route, flagged and NOT certified.** In string constructions the
massless spectrum is fixed by topology (bundle cohomology / Wilson-line or hypercharge-flux
projection), so exotics can be *projected out* rather than made heavy, at the price of incomplete
multiplets. Palti [1601.00285] is the clean modern example — and note it **reproduces the same
structure independently**: *"The exotics are not vector-like under the U(1) symmetry and
therefore their mass is naturally related to its breaking scale."* Even there the compactification
is the input. **This sweep did not read a primary source on the Wilson-line projection of E₆
exotics; treat the projection route as UNVERIFIED HERE.**

---

## 5. (d) IS THERE A NO-GO?

**No absolute no-go was found.** Nothing says "there exists an E₆ model that cannot make its
exotics heavy" as a theorem. What exists is sharper than nothing and weaker than a no-go:

| # | statement | status |
|---|---|---|
| **D1** | **The trilemma.** {E₆-related Yukawa relations} + {TeV-scale U(1)′ breaking} + {proton stability} are **mutually inconsistent**. Any two hold; the third must be given up — in practice by imposing a discrete symmetry that breaks the E₆ relations. | Langacker RMP 81 (2009), **cited, not re-derived**; banked in `B951` |
| **D2** | **The structural bound (computed here).** exotic mass ≠ 0 ⟹ U(1)_ψ broken. `M_D/M_Z′` is a **coupling ratio**, not a scale ratio, so the exotics cannot be decoupled while leaving the extra U(1) light. | **derived in §2, rep-independent** |
| **D3** | Independent corroboration in a **different framework** (F-theory SU(5)×U(1) with hypercharge flux): exotics *"are not vector-like under the U(1) symmetry and therefore their mass is naturally related to its breaking scale"*; the spectrum *"does not form complete GUT representations"*; *"the exotics cannot form a complete 10 multiplet"*. | Palti, [1601.00285], abstract read |
| **D4** | The obligation does not end at "heavy": the **lightest exotic quark must also be made unstable**, which in E₆-inspired models requires *extra* TeV vector-like matter. | Nevzorov [1205.5967], abstract read |
| **D5** | String consistency conditions **force** quasi-chiral exotics in many constructions, and *"mass generation for the fermions is sometimes problematic"*. Not a theorem. | Cvetič–Halverson–Langacker [1108.5187]; Halverson–Langacker [1801.03503] |

**NOT CERTIFIED, explicitly:**

- No complete citation closure on **Hewett–Rizzo** (1524 citers) or **Langacker RMP** (1544
  citers). A no-go could hide there.
- INSPIRE full-text probes (`"cannot be made heavy"`, `"exotics cannot"`, `"exotic states cannot
  be"`) are keyword-fragile and returned mostly hadron-physics noise; **absence of a hit is not
  absence of a result.**
- **Hewett & Rizzo, Phys.Rept. 183 (1989) 193** — the comprehensive review — is **pre-arXiv and
  was not read this sweep**; its exotic-sector content is taken at the level of `B951`'s earlier
  scout.
- The Wilson-line / flux projection route was **not** verified against a primary source.
- Modern LHC exotic-quark mass bounds were **not** re-derived.

---

## 6. IF A SEALED CELL IS EVER WANTED

**Do not seal "do the exotics get heavy?" — that is the VEV question again and would double-count
L133/L138.** Three things are genuinely computable and genuinely new:

1. **Read the exotic sector in the object's OWN frame.** §2 is scoped to the GUT chain. The
   object's cascade lands on the **A₂+A₁ Levi** `su(3)⊕su(2)⊕u(1)³` — a **different** rank-3
   torus. *Which of the object's three u(1) charges plays the role of U(1)_ψ, and do the eleven
   exotics stay chiral under it?* Cheap, and it is the only version of L134 that is about **this**
   object. **MB12 check first:** the criterion must be able to both pass and fail — state the
   failing configuration before computing.
2. **The L132 join.** If the object's spectrum is *not* complete 27s, the exotics are partially
   projected out **and** the anomaly check becomes non-vacuous, simultaneously. These are one
   question, not two.
3. **The ledger amendments of §1.3 and §1.4** — corrections, not research; they should be made
   whether or not anything else is sealed.

---

## 7. SOURCES

**Read this sweep (abstract or full text as marked):**

| source | recid / eprint | what it establishes | read |
|---|---|---|---|
| Kang, Langacker & Nelson, PRD 77 (2008) 035003 | 758656 / 0708.2701 | `m_D = λ⁵⟨S⟩`; leptoquark vs diquark vs quasi-stable decay classes; B, L imposed by hand; BBN windows; benchmarks 300–1482 GeV | full text |
| King, Moretti & Nevzorov, E₆SSM review | 1779174 / 2002.02788 | `κ S(D D̄)`; `⟨S₃⟩` breaks U(1)_N and sets both μ and `M_D`; `Z₂^L`/`Z₂^B`; complete 27s ⇒ automatic anomaly freedom | full text |
| Halverson & Langacker, TASI | 1647588 / 1801.03503 | quasi-chiral exotics "extremely common"; forced by string consistency; **"mass generation for the fermions is sometimes problematic"**; Z′ and exotic masses tied to the soft/μ scale | full text |
| Palti, *Vector-Like Exotics in F-Theory* | 1412081 / 1601.00285 | **independent framework, same mechanism**: exotics not vector-like under the U(1) ⇒ mass tied to its breaking scale; incomplete GUT reps | abstract |
| Nevzorov, *E₆ inspired SUSY with exact custodial symmetry* | 1116270 / 1205.5967 | exotics ⇒ FCNC + rapid proton decay; single `Z̃₂^H`; **extra TeV vector-like matter needed to destabilise the lightest exotic quark**; 5D/6D orbifold GUT origin | abstract |
| Cvetič, Halverson & Langacker, JHEP 11 (2011) 058 | 925446 / 1108.5187 | string global-consistency conditions beyond anomaly cancellation constrain exotic matter | abstract |
| Hewett & Rizzo, Phys.Rept. 183 (1989) 193 | 268529 | the comprehensive superstring-inspired E₆ review, 1524 citations | **metadata only — NOT read** |

**Repo-banked, relied on as prior art (not re-derived here):** Langacker RMP 81 (2009) 1199
[777086 / 0801.1345] via `B951`; Robinett [17444]; Rizzo [219732, 227115]; Rosner [525750].

**Citation-graph closure performed:** `refersto recid 758656` → **107 hits, all 107 enumerated**
(`prior_art_exotics.json`, `certified_nulls.N3`).

---

*Scouting document. No verdict on the object. The one computation it contains is scoped, its
fits are predictive rather than imposed, and its MB12 vacuity check is stated in §2.2 R1.*
