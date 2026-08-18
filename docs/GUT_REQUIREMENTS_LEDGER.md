# THE GUT REQUIREMENTS LEDGER — what a grand unified theory must satisfy

*Companion to `SM_SPECIFICATION_LEDGER.md`, one level up. Same purpose: the programme
says "the GUT chain", "skipping SU(5)", "not Pati–Salam" — but had never written down what
a GUT is actually required to satisfy. Written 2026-08-08 (B952).*

**Firewall status:** a specification of accepted physics plus a delivery column. No
value-matching; nothing promotes to `CLAIMS.md`. Gate 5 untouched.

---

## A. The checklist any GUT must pass

| # | requirement | content | status in accepted physics |
|---|---|---|---|
| 1 | **Embedding** | G ⊇ SU(3)×SU(2)×U(1) with the correct embedding; **rank(G) ≥ 4** | structural |
| 2 | **Anomaly freedom** | automatic for "safe" groups (SO(10), E₆); SU(5) needs 5̄ + 10 | forced |
| 3 | **Matter fits** | SM fermions in GUT multiplets. SU(5): 5̄+10 (15, no ν_R). SO(10): **16** (15 + ν_R). E₆: **27 = 16 + 10 + 1** | structural |
| 4 | **Coupling unification** | the three couplings must meet. **In the non-SUSY SM they do NOT** — they miss badly. MSSM unifies at ≈2×10¹⁶ GeV | hard constraint |
| 5 | **Proton decay** | X,Y exchange gives τ ∝ M_X⁴/m_p⁵. Super-K: **τ(p→e⁺π⁰) > 2.4×10³⁴ yr**, forcing **M_GUT ≳ 10¹⁶ GeV**. **Minimal SU(5) is EXCLUDED by this** | hard experimental bound |
| 6 | **Doublet–triplet splitting** | the Higgs multiplet's colour triplet must sit at M_GUT while its doublet sits at ~100 GeV — a **10¹⁴ tuning**. Unsolved in minimal models (missing-partner, Dimopoulos–Wilczek, orbifold GUTs) | open problem |
| 7 | **Fermion mass relations** | SU(5) gives m_b = m_τ at M_GUT (roughly works) but also m_s = m_μ, m_d = m_e (**fail by ~3 and ~9**) → Georgi–Jarlskog factors | partial |
| 8 | **Neutrino mass** | SO(10)/E₆ contain ν_R ⟹ seesaw; the GUT should explain the smallness | mechanism available |
| 9 | **Monopoles** | GUT breaking to a group with a U(1) factor produces stable ’t Hooft–Polyakov monopoles; their non-observation requires **inflation after/during** breaking | cosmological constraint |
| 10 | **Baryogenesis** | sphalerons wash out B+L, so **B−L** must be generated ⟹ leptogenesis (natural in SO(10)/E₆) | mechanism available |
| 11 | **Explicit breaking sector** | the chain needs actual Higgs reps (SU(5): 24; SO(10): 45/54/126 …) and a stated VEV structure | model input |

## B. E₆ specifically

- **Rank 6.** Chain: **E₆ ⊃ SO(10) × U(1)_ψ ⊃ SU(5) × U(1)_χ × U(1)_ψ**; the general
  extra abelian direction is U(1)_θ = cos θ·U(1)_χ + sin θ·U(1)_ψ (the Z′ literature).
- **27 = 16 + 10 + 1** under SO(10). The **16** is one SM generation with ν_R. The
  **10 + 1 = 12 states per generation are EXOTIC** — a vector-like coloured triplet pair
  (D, D̄), an extra Higgs-like doublet pair, and singlets.
- **The exotics must be made heavy**, or they would have been seen. This is a requirement
  on any E₆ model, not an optional extra.
- E₆ is automatically anomaly-free, and the **27 is complex** — so E₆ can support chiral
  matter (it is one of the few safe chiral GUT groups).
- Z′ bounds from LHC push the extra U(1) gauge bosons to **≳ 4–5 TeV**.

## C. WHAT THIS OBJECT DELIVERS, row by row

| requirement | delivery | status |
|---|---|---|
| 1 embedding | E₆ boundary is structural and banked; the descent reaches su(3)⊕su(2)⊕u(1)³ | **see §D — rank obstruction** |
| 2 anomaly freedom | inherited from E₆ (automatic) | reproduced, not derived |
| 3 matter fits | the 27 and its branchings are banked (B897 and the cascade) | **structural** |
| 3′ **the 12 exotics per generation** | **ADDRESSED (row corrected 2026-08-18).** **B884** grades the 27 at the enhancement point — `27 → [1 | 3,3,2,2 | 6,3,3,2,1,1]` — identifying the so(10)-vector as the Higgs block `(3,1)+(3̄,1)+(1,2)+(1,2)`; **B895** adds that the colour content is `3+3̄`, **vector-like**. Quantum numbers banked (B970/B978) | **structural; no values** |
| 4 coupling unification | sin²θ_W = 3/8 tree-level; the run to M_Z **missed at 16σ** (B915) | **failed, sealed** |
| 5 proton decay / M_GUT | **PARTIALLY ADDRESSED (row corrected 2026-08-18).** **B867 S1** identifies the X,Y content exactly — the SM-step coset is `24−12 = 12 = dim[(3,2)+(3̄,2)]` — and **B881** computes the SM-graded coset commutation table as the mediation skeleton (28 nonzero cells, each single-target). **No lifetime, scale or rate is computed**, and none can be (the dimensionful no-go) | **structure yes, values no** |
| 6 doublet–triplet | touched only via B925's Pati–Salam kill | **absent** |
| 7 fermion mass relations | no values; three crossings negative | **absent** |
| 8 neutrino mass | **STRUCTURALLY ADDRESSED (row corrected 2026-08-18).** **B865**: the chain's singlets land in `(1,1)₀` — **the right-handed-neutrino slot** — and **B867 S1** records them occupying the `ν_R`/Majorana slot. **No mass, no seesaw scale** | **structure yes, values no** |
| 9 monopoles | not addressed | **absent** |
| 10 baryogenesis | **PRECONDITIONS PRESENT (row corrected 2026-08-18).** **B867, PROVED — THE SAKHAROV GATE**: all three preconditions are present in banked structure. S1 the X,Y content `24−12 = 12`; S2 physical KM phases `(N−1)(N−2)/2` gives first-N-with-a-phase `= 3`, and B866's S₃ triple supplies **exactly 3**; S3 the transition is one-time, `V(φ)/κ = −(7+5√5)/12 < 0` with barrier `(5√5−7)/12 > 0`. **B867 fences itself: "NO asymmetry, rate, temperature or epoch is computed"** — the stage, not the play | **structure yes, values no** |
| 11 explicit breaking sector | **NOT "none" (row corrected 2026-08-18).** **B853**: the hearing face carries a complete SSB kit — an order parameter `m = √5/3`, B6's **derived** (not fitted) potential, two vacua that are exact Galois conjugates `φ` and `−1/φ`, conjugate critical values, a barrier at `+0.348κ` and an arrow `V(φ) = −1.515κ < 0`. **B884** supplies the exact invariant cubic; **B885/B886** the vacuum-line/Higgs-block laws as theorems; **B859** the state-space order parameter, `OP = 818626500·√3`, **odd under the breaking symmetry**. What remains unsourced is the rank-reducing VEV **direction** (B1017), not the sector | **structure yes; one direction unsourced** |

---

## D. THE RANK OBSTRUCTION — why MEASUREMENT ALONE cannot reach the SM

> **Heading corrected 2026-08-18.** It previously read *"why the cascade cannot reach
> the SM"*, dropping the word **measurement** and thereby contradicting B952's own
> LAW_MAP row: *"Does NOT say the object cannot reach the SM, only that **measurement
> alone** cannot."* The *fused* cascade (B861/B863/B873/B994) is a subalgebra-menu
> descent, not a centralizer computation — its dimensions run `46 → 25 → 12`, i.e.
> rank `6 → 5 → 4` — and it is **not** rank-preserving. The theorem below is about
> centralizers of subsets of `C`, and is true there.

| algebra | rank |
|---|---|
| E₆ | **6** |
| su(3) ⊕ su(2) ⊕ u(1)³ (the second measurement, B892) | **2 + 1 + 3 = 6** |
| **the Standard Model** su(3) ⊕ su(2) ⊕ u(1) | **2 + 1 + 1 = 4** |

**The second measurement preserves rank exactly.** That is not an accident and not a
defect of the particular computation — it is forced:

> **The centralizer of a set of semisimple elements contains a maximal torus, hence has
> full rank.** The measurement cascade computes centralizers of charges (torus elements).
> **Therefore every measurement in the cascade is rank-preserving, and no number of them
> can ever reach rank 4.**

So the two extra U(1)s are not a rounding error to be tidied away — **they are the
unbroken rank, and they are unbroken by construction.**

**Consequence, stated plainly.** Reaching the Standard Model requires **rank reduction**,
and rank reduction is exactly what a *measurement* cannot do. It requires a genuine
breaking mechanism — a Higgs VEV, a Wilson line / Hosotani flux, or an orbifold projection
— i.e. requirement **#11**, which the object does not currently supply.

This is the sharpest structural statement the programme can make about its own distance
from the SM, and it is a **theorem, not an estimate**. It also explains, after the fact,
why the crossings failed the way they did: they were comparing a rank-6 structure against
rank-4 physics.

---

## E. How to use this ledger

Any GUT-facing cell states which row it targets and whether that row is **forced** (must be
reported as *reproduced*), **a hard experimental bound**, or **open**. A cell claiming to
"reach the Standard Model" must first say how it reduces rank.
