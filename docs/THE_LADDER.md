# THE LADDER — what the programme does not yet contain, as rungs to climb

**Standing document. Updated every time a rung moves.** Companion to `THE_FRAMEWORK.md`
(what we *have*). This file is what we *lack*, stated as ingredients toward a complete
account rather than as a list of failures.

**Why it exists (owner directive, 2026-08-09):** *"map the negatives, what exactly the
programme doesn't contain yet, as an ingredient towards a complete account, and we keep
updating that as the ladder we aim to climb."* Five times on 2026-08-08 this seat declared
something absent that the repo already held. A standing map is the fix: **before saying
"the object does not provide X", find X on this ladder.** If X is not on it, X has not
been checked, and the honest answer is *"not checked"*, not *"absent"*.

**Rung grades**
- **BLIND** — never asked. No arc addresses it. *Saying "the object lacks this" is unearned.*
- **HOLE** — a gap **inside** something we already claim. The most valuable rungs.
- **BROKEN** — we claimed it and the claim does not hold. Repair owed.
- **BOUNDED** — a theorem with a named mechanism. Not a gap; a known edge.
- **OPEN** — a live surface with a computation someone can run.

---

## A. BLIND — never asked (saying "absent" here is unearned)

| # | rung | evidence | first move |
|---|---|---|---|
| **X1** | **Does the framework derive quantum mechanics or assume it?** Hilbert space, Born rule, superposition | **2 arcs** (B725, B182) | a specification ledger first, as B950 did for the SM |
| **X2** | **Black holes · entropy · holography** | **2 arcs, 0 PROVED** | **subsumes ℓ/G₃**: `ℓ/G₃ = (2/3)c` (Brown–Henneaux, verified), Cardy `S = 2π√(cL₀/6)`. Blocker to state honestly: m004 is **cusped**, not AdS₃ with a conformal boundary |
| **X3** | Dark matter | 1 arc | ledger, not probe |
| **X4** | Inflation | 3 arcs | ledger, not probe |
| **X5** | Big bang / initial condition | 3 arcs | ledger, not probe |
| **X6** | Strong CP / θ_QCD | 3 arcs | L110 has **no registered obligation set** |
| **X7** | Neutrino mass | 6 arcs, all ledger mentions | — |
| **X31** | **MARKOV BLANKET** — the statistical-independence / boundary structure, named by the owner as part of the chain | **0 arcs.** *(A naive grep now returns 2 — **B984 and B988, the arcs that RECORD the absence**. **Registering a gap creates hits for the gap**, so the coverage count self-inflates; a future review must exclude recording-arcs or it will read this as covered.)* **CONFLATION HAZARD:** the corpus is full of **Markov *triples* / the Markov cubic** — a *different object* | define what a Markov blanket would even be for this object before probing |
| ~~**X32**~~ | **RE-GRADED 2026-08-09 by Review 41 — NOT blind; it was COMPUTED.** **B20 and B37**: *"the trace map has **invariant-memory and feedback** but **never reads its invariant**, failing the operational self-model criterion"* — under fixed operational definitions. So the object **has feedback and an invariant**; what it lacks is **self-modelling**. That is a result with a mechanism, not an absence | the live question is not *does it have feedback* but **what would make it read its own invariant** — and B717 already frames that as an observer closing |

## B. HOLE — inside what we already claim

| # | rung | why it matters |
|---|---|---|
| ~~**X8**~~ | **RE-GRADED TO BOUNDED 2026-08-09 by B987 — not a hole.** The doublet is the **10 ⊂ 27** (B884: *the so(10)-vector as the Higgs block (3,1)+(3̄,1)+(1,2)+(1,2)*, on the object's own frame). **No tension with B978** — that no-go scopes the **adjoint**; matter mass is the **cubic**, 27³ ⊃ 16·16·10, and B884 computed the table (7.7-order gap, 11 coupled cells vs 275 exact zeros). **Residue: doublet–triplet splitting, and it is BOUNDED** — B298/B299 place it as **external, needing a colour choice**, like chirality, rank and scale. | It looked like a hole because three correct arcs had never been stated together — and **P3 caught it in one query**, the first of the day's six instances caught by an instrument rather than the owner |
| **X9** | **The twelve exotics** (27 = 16+10+1) — any E₆ model must make them heavy | L134 |
| **X10** | **L138's scope** — it fired, but **a canonical orbit is not a canonical VEV** | the only live route to a distinguished VEV |
| ~~**X11**~~ | **CLOSED 2026-08-09 by B991 — BOUNDED, mechanism named.** Verified symbolically: under q → λq the anomaly conditions scale as **λ¹, λ¹, λ¹, λ³** — **all homogeneous**, so the solution set is a **cone**, never isolated points. **Direction derivable (B864: b = c = 0 forced); normalisation not, by the form of the equations.** Impossible for *everyone*, so it is closed rather than owed. **Residue:** any arc claiming to derive a normalisation must **exhibit the non-homogeneous condition it used** |
| **X12** | Is the SMT's u(1)³ actually **(Y, χ, ψ)**? **Inferred, not computed** | B953 flags itself |

## C. BROKEN — repairs owed (cc3's relational re-read, 2026-08-08)

| # | rung | status |
|---|---|---|
| **X13** | **L73 abelian invisibility is FALSIFIED, not narrowed.** \|H₁ torsion\| = \|2−tr(M)\|; the sister **m003** has tr = −3 ⟹ **5, not a unit**. A commensurable manifold is abelian-**visible**, at the hearing prime | rewrite as an m004/golden-row statement, then recompute on m003, m206, silver row |
| **X14** | **L98 one-organ-or-two — SCOPED 2026-08-09.** Entry condition now stated, from both sides. **B646's own recommendation, adopted but never executed:** *design a statistic that separates the hypotheses **structurally** instead of pushing depth* — N3 sat at **~1.3σ against a 2σ bar with depth-15 gaps SHRINKING**, so depth was already the wrong axis. **cc3's three defects:** one golden-row word, no non-commensurable control, and a **binary hypothesis space where B730 forces a V₄**. **THE DESIGN PRINCIPLE, from the failure itself:** the original statistic was **boundary-condition dependent** (periodic → 2 organs, open → 1) — *a statistic whose answer flips with the BC is measuring the BC, not the organ structure*, so **the structural separator must be BC-INVARIANT** | **(1)** construct a BC-invariant statistic and **verify the invariance before running it on the object**; **(2)** then both rows, golden **and silver** (the non-commensurable control B855 says the repo has never had); **(3)** three-way, not binary. **Two-outcome, so it cannot come back empty: if no BC-invariant statistic separates the hypotheses, "how many organs" is ILL-POSED at this level — a real result** |
| **X15** | **Six OVER-WIDE closures** — L54 (most dangerous), L1, L57, L84, L93 need scope-correction notes; **L77 should be withdrawn outright** | scope notes, not reopenings |
| **X16** | **The eleven faces describe what the object is NOT.** Face-attachment was induced from `kill_graph`, which classifies **kills**; positives were never attached (B805's own words) | the **twelfth face** — character-variety / trace-map substrate — is *Layer 0 of the framework*: the Fricke–Vogt surface, the **L/R shears**, the I=1/4 selector |
| **X17** | **`scripts/forcing/build.py` ingests only files named exactly `FINDINGS.md`** — **45 arcs never ingested**, including **B1–B5** | fix the glob **before** re-running attachment, or the re-run inherits the blind spot |
| **X18** | **B501, B502 are genuine file-drawer** — sealed, never reported, exempted on a **numbering collision** with the audit seat | B982; B473/B565/B570 remain an unverified-exemption debt |

## D. BOUNDED — theorems with named mechanisms (edges, not gaps)

| # | rung | the mechanism |
|---|---|---|
| **X19** | rank reduction | centralizers contain a maximal torus ⟹ **measurement is rank-preserving** (B952); all routes closed (B959, B960) |
| **X20** | matter mass from the adjoint | **78 ∉ 27 ⊗ 27** (B978/V5) |
| **X21** | **scale** | **amphichirality forces CS = 0**, which deletes the integer-quantized term `k·I_CS` from Gukov's `k·I_CS + iσ·I_grav`, leaving only the **unquantized** σ (with `G_N = 1/4σ`). *Normalisation check owed before this is a claim* |
| **X22** | time · 4d · Lorentzian signature | all the observer's; **no canonical Wick rotation** (B716); thermal time fails on identity — tracial II₁, **trivial modular flow** (B721) |
| **X23** | the 4d lift | **exists and is canonical** (B277, monodromy **φ = RL** — A7's bit), but is **N=2 (non-chiral)** and the **6d type is a free input** |
| **X24** | the 27-VEV | input in every framework, canonical nowhere — 𝕆P² homogeneous (B962) |

## E. OPEN — live surfaces with a runnable computation

| # | rung | the computation |
|---|---|---|
| **X25** | **the two ends' quantized asymmetry** | **CS = 0 at E₆, CS = π²/5 at E₈** — the quantized term dies at one end and survives at the other |
| **X26** | **L81(c)** — cc3's highest-value item | the repo named the C-twisted play *"the (−A₁)-bundle, trace −3"* and **independently** identified trace −3 as **the sister**. Joined: **chirality is what the object and its sister AGREE on; the θ-even channel IS the sister-difference** |
| **X27** | **L105** — the first executed **golden-vs-silver** cross-row control | the control B855 says the repo never had; returns a **structural difference, not a null** |
| **X28** | **the curvature sign transition** | Λ<0 → Λ=0 → Λ>0 on one cone-angle curve (B248). *The near-zero observation is a **hook**, firewalled, not a claim* |
| **X29** | **L141** — the anomaly layer is scale-free **by theorem** ('t Hooft anomalies are RG-invariant) | the one part of QFT a scale-free object may speak about |
| **X30** | **L144** — B167's five-door map is POSTULATED, orphaned, pre-cascade | its door-5 dismissal rests on a premise B862/B864/B892 overturned |

---

## HOW THIS FILE IS USED — binding

1. **Before writing "the object does not supply X"**, find X here. Not present ⟹ the honest
   words are **"not checked"**, and the first action is to add the rung, not to conclude.
2. **A rung moves only with a banked arc**, cited inline — same rule as `LAW_MAP.md`.
3. **BLIND never becomes BOUNDED in one step.** It must pass through OPEN: something has to
   be computed before an edge can be claimed.
4. **BROKEN rungs outrank new frontiers.** A repair is worth more than a new BLIND rung,
   because a broken claim is actively misleading every downstream reader.
5. The counterpart rule from `THE_FRAMEWORK.md` applies here too: **a closure survives the
   relational re-read exactly when its scope sentence names no manifold** (cc3, 2026-08-08).
