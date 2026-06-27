# Hint Ledger

The **generative counterpart** to `../papers/VALIDATION_LEDGER.md`. It exists because the repo had a structural
gap: the only place to record a research idea was `OPEN_LEADS.md`, which admits **decisions to run** — so a hint
had no legal place to exist until it was already strong enough to be an actionable lead. Hints died young.

**Admission bar (deliberately low):** record *anything noticed* — a pattern, a coincidence, an anomaly, a cross-
finding rhyme, an unasked question. **Nothing here is a claim.** This is **not** a decision-to-run ledger.
Recording a hint is not asserting it (`../GOVERNANCE.md §6.2`, the staging principle). The **only judged step** is
**promotion to `OPEN_LEADS.md`** (a decision to run) or to a candidate claim (the verification gate). Governed by
`../METHOD.md`. Firewall (`../ARCHITECTURE.md`): hints may cite math (B/V/P); math never cites hints.

**Lifecycle** (resist adding states): `NOTICED → CHECKED → PROMOTED` | `→ DORMANT` (cheap check inconclusive —
parked, revivable) | `→ KILLED` (**only** via the full promotion gate → `../speculations/TOMBSTONES.md` with a
`residual-hint:` field). The heavy adversarial battery is **forbidden before promotion** (anti-blindness rule 2):
a cheap CHECK may only set a diagnostic flag (`generic?`/`vacuous?`/`non-reproducing?`) and route DORMANT — it may
**not** KILL.

`type ∈ {MATH, HOOK, ANOMALY, PATTERN, QUESTION}`.

## Live hints

| H# | hint | type | noticed | state | flags | disposition |
|---|---|---|---|---|---|---|
| H1 | `\|H₁\| = (2m²+7)²+2 ⇒ \|H₁\| ≡ 3 (mod 4)` for the metallic Seifert duals | PATTERN | 2026-06-27 | NOTICED | — | from B227; see H16 |
| H2 | the recurring **"5" web** — golden period 5; `n=m²+4=5`; `M(4,5)=SM(3,5)`; `40a1` conductor `2³·5`; the golden discriminant 5 shows up on every face | PATTERN | 2026-06-27 | NOTICED | — | see H17 |
| H3 | `content = m = congruence-modulus = gcd(a,b)` — one invariant, four names | MATH | 2026-06-27 | PROMOTED | — | banked B221 |
| H4 | the **hyperbolicity-split motif** — the object recurs on both sides of a hyperbolic/non-hyperbolic divide as *different* manifolds (B217 period/volume; B226 two-SUSY; B229 two-bulks) | PATTERN | 2026-06-27 | NOTICED | — | see H13 |
| H5 | the **determinant = SU(2) level** reading: ordinary `PS−QR=1` (SU(2)₁), super `PS−QR=2` (SU(2)₂) | MATH | 2026-06-27 | PROMOTED | — | banked B229 |
| H6 | the **silver FM `c=5/4`** coincidence: `c=c(SM(6))` but a different coset ⇒ "c-coincidence ≠ CFT identity" | ANOMALY | 2026-06-27 | PROMOTED | — | banked B230 (reinforces the coset criterion) |
| H7 | `E₈+E₆−E₇ → Monster+Fischer−BabyMonster` — the object's dual McKay selects two of McKay's three sporadic-seeding diagrams, excludes the Baby Monster | HOOK | 2026-06-27 | PROMOTED | — | → L46 / S041; see H14 |
| H8 | **heterotic** standard embedding `E₈ → SU(3)×E₆` **skips E₇** in the chiral/N=1 case — the *same exclusion pattern as B210* | HOOK | 2026-06-27 | NOTICED | chat1-verified-lit | see H14 |
| H9 | **level-rank duality** `SU(2)₃ ↔ SU(3)₂` at `q=e^{2πi/5}`, through `(G₂)₁` and `(F₄)₁`; the Fibonacci anyon `= (G₂)₁`. Not an iso (4 vs 6 irreps) — a modular-data duality | HOOK | 2026-06-27 | NOTICED | chat1-verified-lit | — |
| H10 | **S041 correction:** "NCG: no shared data" is wrong. Connes' `ℂ⊕ℍ⊕M₃(ℂ)` encodes primes `{2,3}`; ours `{2,3,5}`; overlap `{2,3}`, golden prime 5 absent — a *partial* rhyme | ANOMALY | 2026-06-27 | CHECKED | corrected | corrected S041 (an unearned-negative caught — rule 7) |
| H11 | the **Kodama state** = `SU(2)` Chern–Simons at `k ~ 6/(GΛ)`; at what Λ does `k=3`? | QUESTION | 2026-06-27 | **CHECKED** | **FIREWALL/HELD; computed** | **COMPUTED (k=6π/GΛ): k=3 ⇒ Λ≈2π/l_P²≈2.4×10⁷⁰ m⁻² (Planck scale, ≈6.28 Planck units); the observed Λ needs k≈6.5×10¹²² (no object structure).** Clean *quantitative* negative — the CC-problem's 122 orders = the gap between the object's natural level k=3 (UV) and k→∞ (IR). Firewall *relocated to k*, not crossed (K018). Run, not prejudged. → S041 |
| H12 | does `c=7/10` (our TCI) appear in **Conway super-moonshine** (the N=1 SCFT module via the Leech lattice)? | QUESTION | 2026-06-27 | **CHECKED** | **DEMOTED (B234)** | building-block: NOT established (2003.13700). The Fibonacci category appears in the Conway SCFT (2512.19640) **but the category is unique ⟹ generic ubiquity, NOT a 2nd moonshine hook** (B234/H26); filed under H17, below the object-specific McKay hook. S041 corrected. |

## QUESTION-pass additions (first cycle, 2026-06-27)

| H# | hint | type | noticed | state | flags | disposition |
|---|---|---|---|---|---|---|
| H13 | does the **hyperbolicity-split motif** (H4) have a single unifying statement across B217/B226/B229 — "golden lives on both sides of every hyperbolicity divide as distinct manifolds"? | QUESTION | 2026-06-27 | **CHECKED** | candidate-synthesis | **B233: YES, stated** — the monodromy class `γ∈SL(2,ℤ)` / `SU(2)₃` data is hyperbolicity-blind and is realized twice: a non-hyperbolic (Sol/Seifert) manifold (algebraic/quantum face) and a hyperbolic manifold (geometric/volume face), never one. Pattern from 3 witnesses; "every axis" not proven. |
| H14 | is the `E₈+E₆−E₇` exclusion (H7) the **same obstruction** as heterotic's E₇-skip (H8)? i.e. is our congruence-quotient obstruction for `2O` ↔ the chirality obstruction for `E₇` reps? | QUESTION | 2026-06-27 | NOTICED | — | the deepest framework-search question |
| H15 | do the **non-SUSY** metallic chains (`Z_{m²+2}` parafermions, the FM family) have their own special structure at the metallic levels `k=m²+2`? | QUESTION | 2026-06-27 | **CHECKED** | earned-negative | **B231: NO — the level `k=m²+2` confers no special chain structure for m≥2.** Built+validated the general `su(2)_k` chain ED (Ising/TCI reproduced); silver `k=6` is a generic `M(7,8)` chain, not SUSY. The metallic mean is a quantum dimension (`λ_m=2cos(π/(m²+4))`) **iff m=1**; B218(anyon-realizable)+B224(SUSY)+B231(qdim=mean) collapse to one boundary `λ_m<2 ⟺ m=1`. |
| H16 | is `\|H₁\| ≡ 3 (mod 4)` (H1) tied to `40a1`'s reduction / the character-variety arithmetic (the conductor `2³·5`)? | QUESTION | 2026-06-27 | NOTICED | — | arithmetic-geometry scout |
| H17 | **why** does `5 = m²+4` at `m=1` govern golden across *every* face (period, anyon level, SUSY coset, conductor) — one reason or a pile-up of coincidences? | QUESTION | 2026-06-27 | **CHECKED** | partial-unification | **B233: NOT a pile-up.** 8/8 faces cascade from one root (golden=m=1, field `ℚ(√5)`, disc 5); the *only* genuine coincidence is `min(m²+4)=5` is also the largest McKay prime (`SL(2,F₅)=2I=E₈`; `E₇` excluded). One cascade + one coincidence — verified exactly (`verify_five.py`). |
| H18 | **(standing physics-parallels prompt)** which of our verified results have known parallels in physics frameworks we haven't examined? (re-run every WIDEN) | QUESTION | 2026-06-27 | NOTICED | standing | spawns per-result sub-scouts; keeps L46/S041 live |

## Compute-cycle additions (2026-06-27)

| H# | hint | type | noticed | state | flags | disposition |
|---|---|---|---|---|---|---|
| H19 | ~~the Fibonacci fusion category in the Conway SCFT as a 2nd moonshine hook; match its F/R-symbols to the object's SU(2)₃~~ | HOOK | 2026-06-27 | **DORMANT (B234)** | **circular-test** | **KILLED-as-posed (B234/H26):** the Fibonacci category is unique ⟹ the F/R "match" is forced ⟹ the test cannot fail ⟹ no object-specific info. `residual-hint:` the *opposite* question (does Conway use `ℚ(√5)`/`40a1`/a chirality beyond the bare category?) is the only informative version; prior = no. Reframed under H17/H28. |

## Chat1/Chat2 handoff (2026-06-27) — registered NOTICED before judging

Two handoffs: **Chat-1** (the computed exploration survey — Paths 1/A/2/3 + 5 discoveries) and **Chat-2** (a critique
of Chat-1 + its own discovery). Every distinct item registered here first; verdicts attach at CHECK (`B234`).

**CHECKED 2026-06-27 via `B234`** (all recomputed, cross-checked): **VERIFIED** — H20, H22, H23, H25, H27, H28, H29
(+ the why-5 co-occurrence). **VERIFIED-and-corrects-our-own-work** — H26 (H19 is circular ⟹ **H12 demoted**,
S041 fixed). **CORRECTED** — H30 (chat2's "same wall" → E₇ is *overdetermined/triple*, distinct mechanisms, with
chat1). **agreed framing** — H31 (H11 wording softened). The strongest new result is **H27** (the trace-1 congruence law); the strongest *method* is **H28** (the
specificity filter, now standing in `S041`).

**Follow-up resolutions (`B235`, 2026-06-27):** **H24 CORRECTED** — F₄ retracted, footprint **3/5** (no
`SU(3)_k⊂(F₄)₁` conformal embedding: `c(SU(3)_k)` never `=26/5`). **H32 CLOSED** — `ℚ(√−7)` does **not** appear
(SnapPy: all `4₁` covers ≤deg 6 keep `ℚ(√−3)` — arithmetic; algebraically the trace-1 ladder closes at `{√5,√−3}`
by unimodularity `det∈{±1}`). **H34 RESOLVED** — the metallic family table m=1..6 (→ L49, the paper's §4, B235) **and** the `SU(3)₂` WRT
level-rank check (B238): `Z(4₁;SU(2)₃)=Z(4₁;SU(3)₂)=−1/φ` (figure-eight coincides via shared `κ=5`), but not a
general level-rank equality — figure-eight-specific.

**Follow-up resolutions (`B236`/`B237`, 2026-06-27, SnapPy+GAP):** **H21 CLOSED** — the coset-coincidence
mechanism verified (Lashkevich/GKO/Qiu refs; `M(4,5)≡SM_1` the same coset, unique; E₇-in-TCI bonus), clearing the
paper's originality gate. **H33 RESOLVED** — silver carries **no `2O`** (GQuotients=0, field-only coincidence); and
chat1's "all metallic bundles carry 2T,2I" is **corrected** to manifold-specific (golden→2T, silver→S₄, bronze→2T+2I;
2O absent throughout).

| H# | hint | type | noticed | state | flags | disposition |
|---|---|---|---|---|---|---|
| H20 | **E₇ exclusion is OVERDETERMINED** — independent mechanisms: Diophantine (`48≠p(p²−1)`, no congruence quotient) + rep-theoretic (E₇'s 56 is real/non-chiral) (chat1 Path 1) | MATH | 2026-06-27 | NOTICED | — | B234 |
| H21 | the coset-coincidence **mechanism** (ordinary GKO = super GKO coset at `SU(2)₃`) is **not stated as a proposition** in the lit; the uniqueness *fact* is Qiu 1986 (via Johnson–Clifford hep-th/0311129); Lässig et al. 1991 write the TCI coset (chat1 Path A) | HOOK | 2026-06-27 | **CHECKED** | **CLOSED (B236)** | refs found (chat1) + **verified by central charges (B236):** super `SM_k=(SU(2)_k×SU(2)_2)/SU(2)_{k+2}` (Lashkevich hep-th/9301093), ordinary M(m,m+1) (GKO); `M(4,5)`≡`SM_1` = the *same* coset `(SU(2)_1×SU(2)_2)/SU(2)_3` (unique over the sweep), c=7/10; uniqueness fact = Qiu 1986. **Bonus:** TCI = `(E₇)₁⊕(E₇)₁/(E₇)₂` (c=7/10) — E₇ in the TCI as a coset algebra (≠ the excluded McKay role). **Closes the H21 gate** on the paper's originality claim. |
| H22 | **character-field = trace-field correspondence:** `2T→ℚ(√−3)`=hyperbolic field, `2I→ℚ(√5)`=monodromy field, `2O→ℚ(√2)`=ABSENT ⟹ E₇ **triply** excluded (chat1 D1) | MATH | 2026-06-27 | NOTICED | — | B234 |
| H23 | the **silver bundle (m=2) carries E₇'s field** `ℚ(√2)` (disc 8) — "what golden excludes, silver includes"; the metallic *field ladder* `M_m=[[m,1],[1,0]]`, disc `m²+4` (chat1 D2) | PATTERN | 2026-06-27 | NOTICED | — | B234 |
| H24 | ~~exceptional-group footprint 4/5 (incl. F₄ via `SU(2)₃↔SU(3)₂→(F₄)₁`)~~ → **3/5** (chat1 D3, **retracted by chat1 + B235**) | HOOK | 2026-06-27 | **CHECKED** | **CORRECTED** | **F₄ RETRACTED (B235):** no integer `k` has `c(SU(3)_k)=c((F₄)₁)=26/5` ⟹ no `SU(3)_k⊂(F₄)₁` conformal embedding ⟹ the route is void. Footprint = **3/5**: G₂ (Fibonacci), E₆ (`ℚ(√−3)`), E₈ (`ℚ(√5)`); E₇ excluded. (The real `(G₂)₁×(F₄)₁⊂(E₈)₁` is generic CFT, not object-specific.) |
| H25 | **SUSY vs E₈ are distinct:** SUSY needs `n=5` exactly; the E₈-*field* needs `squarefree(n)=5` (m=1,4,11,…); `m=4` has the E₈ field but NOT SUSY (`M(19,20)` not super) (chat1 D4) | MATH | 2026-06-27 | NOTICED | — | B234 |
| H26 | **H19 is CIRCULAR** (chat2) — the Fibonacci fusion category is unique (one F-matrix, two braidings), so any Fibonacci system shares the F/R data ⟹ the "match" can't fail ⟹ no object-specific info; the Conway hook is **generic** (Fibonacci ubiquity), NOT a 2nd moonshine crossing; **demote H12 below McKay, file under H17** | ANOMALY | 2026-06-27 | NOTICED | corrects-own-work | B234 → deflate H12/H19, fix S041 |
| H27 | **the trace-1 congruence law** (chat2's discovery) — golden's two fields are one fact with a sign: `disc=1−4·det`, trace-1 ⟹ `disc≡1 (mod 4)`; permits E₈ (`5`,det−1) & E₆ (`−3`,det+1), **forbids E₇** (`ℚ(√2)`, disc 8≡0); next imaginary rung = `ℚ(√−7)` (disc −7) | MATH | 2026-06-27 | NOTICED | — | B234 |
| H28 | the **specificity filter** (chat2's method) — sweep metallic `m`; classify framework overlaps as **golden-specific** (only m=1) / **object-specific** (only `{ℚ(√5),ℚ(√−3)}`) / **universal** (no m-dependence → demote). Turns the framework search from "collect rhymes" to "measure specificity" | MATH | 2026-06-27 | NOTICED | standing-method | B234 → S041 standing filter |
| H29 | the **SL(2,F_p)↔binary-polyhedral bound** (chat2, load-bearing) — only `p∈{3,5}` give exceptional McKay groups (orders `24,120`), `p=5` largest; re-derive the finite-SU(2)-subgroup bound independently before banking | MATH | 2026-06-27 | NOTICED | re-derive | B234 |
| H30 | **caution (chat2):** chat2's "trace-1 congruence = the SAME obstruction as the Diophantine `48≠p(p²−1)`" is an *interpretation* — verify provably-equivalent vs merely-coincident (chat2's own flag) | ANOMALY | 2026-06-27 | NOTICED | cross-check | B234 (my prior: DISTINCT → overdetermined, with chat1) |
| H31 | **caution (chat2):** H11's "122 orders = gap between `k=3` and `k→∞`" is near-tautological (any UV/IR ratio reappears the CC problem) — a clean HELD negative, not insight; don't sell as such | ANOMALY | 2026-06-27 | NOTICED | framing | adjust S041 H11 wording |
| H32 | **lead:** does `ℚ(√−7)` (the next trace-1 imaginary rung) appear in the object's data — a deeper cusp field, a covering, a Markov-level field? (chat2) | QUESTION | 2026-06-27 | NOTICED | needs-snappy | candidate OPEN_LEADS |
| H33 | **lead:** does the silver bundle (m=2) actually carry a `2O` quotient of its π₁, or is `ℚ(√2)` only a field coincidence? (chat1 lead 2 / chat2) | QUESTION | 2026-06-27 | **CHECKED** | **RESOLVED (B237)** | **NO 2O** (GAP GQuotients=0): `ℚ(√2)` is a field-only coincidence. Also **corrects chat1**: the binary-polyhedral structure is manifold-specific (golden→2T, silver→S₄ [not binary 2O], bronze→2T+2I), NOT "all carry 2T,2I"; **2O absent from all three**. |
| H34 | **lead:** `SU(3)₂` WRT of the figure-eight vs `SU(2)₃` (level-rank, B204); + assemble the full metallic table m=1..6 (model, SUSY, McKay, Seifert dual, \|H₁\|) (chat1 leads 1,3) | QUESTION | 2026-06-27 | NOTICED | needs-snappy/compute | candidate OPEN_LEADS |

## Tombstoned hints
*(none yet — killed hints route here with a `residual-hint:` field, per anti-blindness rule 4.)*
