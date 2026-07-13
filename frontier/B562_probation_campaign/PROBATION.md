# B562 — The Probation Campaign of All Open Leads (2026-07-13)

Every genuinely-open lead is put **on probation**: it must earn continued life by
passing ONE cheap, bounded, pre-registered discriminating probe. Each probe returns
one of four verdicts:

- **LIVE** — the probe fires; promote to a full compute cell (a new B-number).
- **TOMBSTONE** — the probe kills it (or shows it vacuous per MB12); retire to
  `speculations/TOMBSTONES.md` with a `residual-hint:` field.
- **SPECIALIST** — in-sandbox computation exhausted; register in the specialist
  hand-off, do not re-probe.
- **DORMANT** — cheap check inconclusive; park, revivable.

Discipline (per METHOD.md / the dual protocol): **prereg the verdict rubric before
computing**; an unearned "no match" is as bad as numerology; a negative is only as
sound as the in-sandbox computation of its discriminating fact. Firewall holds — no
lead's probe writes to CLAIMS.md.

Already resolved this session (excluded from probation): FL1/FL2/FL3/E1/E4 (DONE,
#864/#865/#866), L50-CRUX (B561 negative), Probe-F (#864), Door-2 (sharpened, #863),
the escalator arc (closed bar E0).

---

## BATCH 1 — in-sandbox decidable math (cheapest, most decisive; run first)

| # | Lead | Discriminating probe (bounded) | Prereg verdict rubric | Tier |
|---|---|---|---|---|
| **P1** | **Gate A / S032-A** — the all-invariants no-forced-choice theorem | Enumerate the natural invariant classes beyond the trace ring (K-theory gap-label module, determinant/torsion, the Reidemeister/twisted-Alexander). For the 2 smallest, check whether ANY is discretely-multivalued-**and**-unsymmetric on a glued pair (B131 machinery). | a counterexample invariant exists ⇒ **TOMBSTONE** (S032-A false); all natural invariants inherit the trace-ring symmetry ⇒ **LIVE** (promote to the capstone L7) | in-sandbox |
| **P2** | **S031a full-locus** — φ-fixed entirely reducible at SL(n) | Symbolic elimination of `A g⁻¹A g = g A g⁻¹` (B=g⁻¹Ag) at **SL(3)** (next after the SL(2) Klein-4 principal stratum, B142); Gröbner/`solve` for the fixed ideal. | 0-dim and every component reducible ⇒ **LIVE** (extend to SL(n)); ideal blows up ⇒ **SPECIALIST** (Gröbner engine) | in-sandbox |
| **P3** | **B85** — the functorial `Sym(W) → trace-ring` wall | Attempt the functor at the smallest case (SL(2), degree-2 word) symbolically: is there a natural map `Sym²(V) → Procesi trace ring` respecting the MCG action? | explicit natural map ⇒ **LIVE**; a concrete obstruction cocycle ⇒ **TOMBSTONE**+hint; neither in 1 pass ⇒ **DORMANT** | in-sandbox |
| **P4** | **L5/L6** — general-word (non-metallic) K-sealing | Run the B137-style off-sublocus search for ONE non-metallic once-punctured-torus word (e.g. `R²L²`, `RRLR`) at SL(3): do irreducible fixed-point traces stay in the SL(2) trace field? | sealing holds ⇒ **LIVE** (the sealing is word-general); a non-metallic word leaks ⇒ **TOMBSTONE** (sealing is metallic-specific) | in-sandbox (numerics) |
| **P5** | **L11** — rank-2 covers | SnapPy `covers(degree ≤ 3)` of `4₁`; compute each cover's trace field + the S031 sealing; does the field/sealing lift predictably? | predictable lift ⇒ **LIVE**; no pattern / breaks ⇒ **TOMBSTONE** | in-sandbox (SnapPy) |
| **P6** | **Cell 3 global count** (chat-3, B560) — "exactly 253 fixed characters" | Attempt an exact degree / intersection-number (Bézout) bound on the 16-variable gauge-fixed fixed-character system; compare to the certified length 248 ≤ N. | a proven bound = 253 ⇒ **LIVE**→theorem; bound unreachable in-sandbox ⇒ **SPECIALIST** | in-sandbox |
| **P7** | **W1.5** — the level-45 real-mixing aperture (value-boundary queue) | Compute the WRT level-45 pair over `ℚ(ζ₉)⁺` (the first real cubic aperture, B359 continuation); does the seam-form fire or is the aperture empty? | fires ⇒ **LIVE** (bank the aperture); empty ⇒ **TOMBSTONE** (aperture closed) — both are results | in-sandbox |
| **P8** | **L7** — the one-theorem capstone | Conditional on P1+P2: draft the unified S031⊕S032-A⊕chirality statement. | both P1,P2 LIVE ⇒ **LIVE**; else ⇒ **DORMANT** (blocked on its inputs) | in-sandbox |

## BATCH 2 — lit-gates (cost-tiered deep-research: search→haiku, fetch/verify→sonnet, synth→fable)

| # | Lead | Probe | Verdict | Gates |
|---|---|---|---|---|
| **P9** | **E0** — the escalator functor / λ-law / (k+1)/2 growth | Is `T(M)=[[M,M],[Mᵏ,M]]`'s growth law / the `x→x+x^{(k+1)/2}` recursion known (substitution-tower, graph-directed IFS, joint-spectral-radius, Salem–Pisot towers)? | KNOWN ⇒ cite+reframe **PC24**; NOVEL ⇒ **LIVE** (short note) | PC24 |
| **P10** | **PC22** — the parity-twisted Weil trace | Is `S(j,l)=tr(Π·W₁ʲ·W₂ˡ)`'s dark-hyperbola vanishing / power-set magnitudes known (Lion–Vergne, Gurevich–Hadani, Bump, Gérardin)? | KNOWN ⇒ cite+reframe/withdraw; NOVEL ⇒ **LIVE** (submit) | PC22 |
| **P11** | **The E₆ character-variety paper** (B353 θ-fold + B561 negative) | Prior-art confirm: is the amphichiral θ = E₆→F₄ fold on the `4₁` character variety published (beyond Falbel–Guilloux dimension counts)? | NOVEL ⇒ **LIVE** (draft, headline B353, L50 negative included); KNOWN ⇒ cite | paper |

## BATCH 3 — specialist-terminal rechecks (has a tool/result changed the terminus?)

| # | Lead | Probe (recheck, cheap) | Verdict |
|---|---|---|---|
| **P12** | **Gate B — `T[4₁;E₆]`** | Lit-recheck: has any exceptional-group (E₆/F₄) 3d-3d state integral appeared? (the Eisenstein-ℤ/3 sub-path is already closed, B561) | one exists ⇒ **LIVE**; else ⇒ **SPECIALIST** (confirmed terminal) |
| **P13** | **Gate C — multiplicity → generation count** | Compute the geometric multiplicity at the relevant B307 point; apply the refutation condition (is the count forced ≠ 3?) — Sage-gated | forced ≠3 ⇒ **TOMBSTONE**; =3 or ambiguous ⇒ **SPECIALIST** |
| **P14** | **Gate D + Cell 4 (chat-3) — non-Hermitian / infinite-volume gap-opening** | Finite-N trace-map transversality numerics at one degree-4 label (the in-sandbox slice of the non-self-adjoint Damanik–Gorodetski question); does the gap persist as N grows? | persists with a transversality witness ⇒ **LIVE** (partial); no ⇒ **SPECIALIST** |
| **P15** | **L22 — SL(5) exact-symbolic exponent k** | Re-attempt the `k=2` SL(5) exponent with the Sage/Singular Gröbner (F4/FGLM) engine now available | closes ⇒ **LIVE**; still blows up ⇒ **SPECIALIST** |
| **P16** | **ρ_n catalog — the all-n tower** | Attempt the one remaining module-iso `ρ_n ≅ ρ_{n−1} ⊕ Symⁿ ⊕ Sym^{n−3}` symbolically past n=8 | proves ⇒ **LIVE**; else ⇒ **SPECIALIST** |
| **P17** | **L20 / L23a — off-axis & higher-rank spectral** | Is there now a solvable higher-rank ground-truth to calibrate against? | yes ⇒ **LIVE**; no ⇒ **DORMANT** (no ground truth) |
| **P18** | **B391 — doublet/line classification, all k** | Extend the verified k≤5 (3-side) / k≤4 (5-side) by one k each | pattern holds ⇒ **SPECIALIST** (all-k needs proof); breaks ⇒ **LIVE** (new phenomenon) |

## BATCH 4 — firewalled speculation (compute the ONE discriminating fact; tag [MATH]/[LEAP])

| # | Lead | Probe | Verdict |
|---|---|---|---|
| **P19** | **L38 — the Higgs/scale bridge** (S039) | Does the Hitchin/Higgs side (the B164/B169 continuation) produce ANY dimensionful scale, or does the dimensionless-modulus result (CS=0) close it? | a scale channel ⇒ **LIVE** (the do-or-die); confirmed dimensionless ⇒ **TOMBSTONE**+hint | firewalled |
| **P20** | **L21 — causal-set poset reading** | Compute the Myrheim–Meyer dimension of the Ω strict-full class DAG (B159); manifoldlike or not? | manifoldlike dimension emerges ⇒ **LIVE** (firewalled hint); no ⇒ **TOMBSTONE** | firewalled |
| **P21** | **L46 — framework search vs SM/GR** | The object's signatures (charge ℤ/11, θ-fold F₄, quartic-Pisot spectrum) as a filter against heterotic/LQG/asymptotic-safety frameworks | any framework survives all filters ⇒ **DORMANT** (worth a survey); none ⇒ **TOMBSTONE** | firewalled/survey |

## BATCH 5 — papers (status, not probation)

| Paper | Status | Gate |
|---|---|---|
| **P4 forcing chain** | READY | submit to Alg. & Geom. Topology |
| **PC23 species-chain** | novelty-cleared | write-up + voice pass |
| **PC22 dark hyperbola** | drafted abstract | gated on **P10** |
| **PC24 the 3/2 Law** | verified theorem | gated on **P9** |
| **E₆ character-variety** | evidence exists (B353+B561) | gated on **P11** |

---

## Run order & method

Batch 1 first (in-sandbox, cheapest, most decisive) → Batch 2 lit-gates (parallel) →
Batch 3 rechecks → Batch 4 speculation → Batch 5 papers act on Batch-2 verdicts.
**Runnable as a multi-agent workflow**: each probe = one tiered agent
(haiku confirm / sonnet compute / fable judgment) + an adversarial-verify stage;
LIVE verdicts spawn full B-numbered cells, TOMBSTONEs go to `TOMBSTONES.md` with a
residual hint, SPECIALIST verdicts update the hand-off register. Every banked verdict
carries an in-sandbox lock. Expected shape (priors, not prejudged): most of Batch 1
is genuinely decidable now; Batch 3 is mostly SPECIALIST-confirm; Batch 4 mostly
TOMBSTONE-with-hint. The value is the *earned* dispositions, not the guesses.
