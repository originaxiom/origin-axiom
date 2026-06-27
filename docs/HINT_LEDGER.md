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
| H12 | does `c=7/10` (our TCI) appear in **Conway super-moonshine** (the N=1 SCFT module via the Leech lattice)? | QUESTION | 2026-06-27 | **CHECKED** | partial | **As a c=7/10 *building block*: NOT established** (at most an open bilinear-character-relation direction, 2003.13700). **But the Fibonacci fusion category** (golden/SU(2)₃, B218) **appears as topological defect lines in the Conway SCFT** (Angius et al. 2512.19640, Dec 2025) — the object's golden data touches Conway moonshine as a non-invertible *symmetry*, not a sub-VOA. → H19 |

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
| H19 | the **Fibonacci fusion category appears as topological defect lines (non-invertible symmetry) in the Conway SCFT** (Angius et al. arXiv:2512.19640, Dec 2025) — the object's golden/Fibonacci anyon data (B218, SU(2)₃) connects to **Conway moonshine** as a symmetry, *not* as a c=7/10 sub-VOA | HOOK | 2026-06-27 | NOTICED | from H12 | candidate → `OPEN_LEADS` (a Conway↔Fibonacci scout): does the paper's Fibonacci TDL F-/R-symbol data match the object's specific SU(2)₃ data? firewalled — a category-theory rhyme, not a physics crossing |

## Tombstoned hints
*(none yet — killed hints route here with a `residual-hint:` field, per anti-blindness rule 4.)*
