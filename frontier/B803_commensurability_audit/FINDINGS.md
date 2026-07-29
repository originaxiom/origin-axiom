# B803 — the commensurability audit VERIFIED, and one claim refined

cc banking seat, 2026-07-29. An incoming audit (review seat) argued that **B727's genericity was
forced by the shape of the derivation chain, not discovered statistically**. Everything in it rests
on one premise, so that was verified first. Mathematics and provenance only; **nothing to
`CLAIMS.md`**, no physics reading adjudicated.

## 1. The premise HOLDS — verified in snappy, not taken on trust

| manifold | invariant trace field | volume | H₁ |
|---|---|---|---|
| **m003** | `x² − x + 1` → **ℚ(√−3)** | 2.0298832128 | **ℤ/5 + ℤ** |
| **m004** | `x² − x + 1` → **ℚ(√−3)** | 2.0298832128 | **ℤ** |
| m129 (Whitehead) | `x² + 1` → **ℚ(i)** | 3.6638623767 | ℤ + ℤ |

m003 and m004 share the invariant trace field; both are arithmetic and cusped, so the invariant
quaternion algebra is `M₂(k)` for both — hence **commensurable**. The premise stands.

**The consequence is structural, and it is the audit's real contribution.** The invariant trace
field is a commensurability invariant (Reid), so *everything derived downstream of it* — the
quaternion algebra, the ramified prime 3, `SL(2,𝔽₃) = 2T`, **E₆ via McKay**, the three 27's, the
breaking cascade, the V₄ torsor — is a statement about **the class**, not about m004. The sister
ties **by construction**, before any base-rate is computed. B727 measured a genericity that was
forced; this says *why*, and it was decidable by inspection.

**What survives as manifold-level** (verified above): **H₁ differs**, so homology separates them;
4₁ is the unique arithmetic knot (Reid), so knottedness and hence **amphichirality** are
manifold-level; and the **spectra** — B790 banked that m003 and m004 are *not* isospectral despite
identical volume.

## 2. The Whitehead correction STANDS

m129's invariant trace field is **ℚ(i)**, not ℚ(√−3), so it is **not commensurable** with m004. It
is a **surgery** parent (Dehn filling), not a commensurability relative. The two family structures
must not be conflated. Verified, not argued.

## 3. The DKY vanishing mechanism CONFIRMED — and the audit's self-reported error is real

Recomputed at **60 decimal digits** (the audit's error was double-precision noise):

| l | min \|factor\| over integer k | at k | |
|---|---|---|---|
| 0.50 | 7.36e−4 | 1 | zero skipped |
| 0.99 | 1.94e−5 | 1 | zero skipped |
| **1.00** | **2.99e−61** | **1** | **exact zero hit** |
| 1.01 | 1.96e−5 | 1 | zero skipped |
| **2.00** | **3.87e−61** | **2** | **exact zero hit** |
| **3.00** | **7.36e−61** | **3** | **exact zero hit** |

The mechanism is elementary and confirmed symbolically: `exp(iπ(m+k)/(m+l)) = −1 ⟺ k = l`, and the
loop runs over **integer** k — so integer `l` hits the zero exactly and the cumulative product
truncates, while non-integer `l` never reaches it. **A puncture at every integer, not a transition.**

At 60 dps the "zero" is ~1e−61, which **confirms the audit's own diagnosis** that its earlier
~1e−17 was float noise rather than a value. Recorded because that error would have reported
spurious exponential growth exactly where the literature says growth is polynomial.

## 4. The organ census CONFIRMED

4₁: `Δ(t) = −t + 3 − t⁻¹`, `det = |Δ(−1)| = 5`, `σ = 0`. Alternating ⇒ Khovanov-thin (Lee) and
knot-Floer-thin (Ozsváth–Szabó) ⇒ **HFK-hat ranks (1,3,1), total 5; reduced Khovanov rank 5**.
Both are **determined by (Δ, σ)**, which the programme banked years ago. **Zero new bits** — the
same organ restated, not a missing one.

## 5. ONE CLAIM REFINED — DKY is absent, but Chen–Yang is not

The audit stated DKY's Question 1.7 is *"absent from 731 arcs"*. Checked precisely:

| searched | files |
|---|---|
| `1701.07818`, `Detcherry`, `Kalfagianni`, `Question 1.7` | **0** |
| `Chen–Yang` | **2** — `frontier/B659_novelty_dossier/` |

So the **Chen–Yang volume conjecture is already in the corpus** as adjacent prior-art context (via
`arXiv:1511.00658`, a *different* paper) in B659's novelty sweep. **DKY's paper and its Question 1.7
are genuinely absent.** The claim holds as stated about Question 1.7; it needed refining about
Chen–Yang, which the programme had already surveyed.

## The standing rule adopted

> **Any derivation step routing through the invariant trace field, the invariant quaternion algebra,
> or arithmeticity is a statement about the COMMENSURABILITY CLASS and cannot be object-specific.**

Decidable by inspection, and it retroactively explains B727. Registered in `docs/PRACTICES.md`
as a MANUAL practice — no gate can check whether a *mathematical* derivation routes through a
commensurability invariant, and claiming otherwise would be the vacuity `test-vacuity` exists to
catch.

## Not verified here

The analytic-torsion join (needs the cusped Cheeger–Müller/Fried literature step first — a
literature step, not a computation), the Dirac spectrum (Cell 3, authorized and untouched), and the
two-parameter deformation reading of intuitions (2)/(5). Those remain the audit's on its evidence.

`verify.py` · lock `tests/test_b803_commensurability.py`

---

# ADDENDUM — the gate spec is MIS-TARGETED, and the error class is minted

The audit's addendum proposed a `chain-scope` gate over *"the same 23 links"* of THE CHAIN, with a
pre-committed split (~9 CLASS, 4 MANIFOLD, rest PRIOR) and the standing instruction: *"if the gate's
first run disagrees with that split, the audit is wrong and should be re-derived, not the gate
loosened."* I built the classifier and ran it before writing any tags.

## The first run disagreed — and a third possibility was the right one

Measured over THE CHAIN's 23 links: **3 CLASS, 5 MANIFOLD, 13 PRIOR, 2 BOTH.**

The pre-commitment allowed two outcomes (audit wrong / gate loosened). **Neither is correct.**

| term | THE CHAIN | LAW_MAP | CLAIMS |
|---|---|---|---|
| McKay | **0** | 4 | 2 |
| E₆ | **0** | 13 | 6 |
| generations | **0** | 8 | 1 |
| 2T | **0** | 3 | 0 |

**THE CHAIN does not contain the E₆/McKay/generation cascade at all.** The audit's §1 table describes
the *E₆ derivation chain*; `docs/THEOREM_LEDGER.md` is the *genesis/forced-core* ledger. Two
different objects sharing the word "chain". The split could never have matched, and the audit's §1
is not thereby wrong — it is about its own chain.

Two further mechanical facts: scope is **transitive** (a link downstream of the trace field is CLASS
even if its own text names no trigger), and only **5 of 23** links cite another C-link, so the
closure is not computable from the text either. The stated decision procedure — *"grep each link;
no judgement call"* — cannot deliver the property.

## And the hard-fail assertion has a false positive on correct text

Targeting the gate where the conclusions actually live (LAW_MAP, 117 rows, 35 citing a CLASS
trigger) yields exactly **one** row asserting object-specificity alongside a CLASS trigger — and it
is **B727's own row**, which reads *"the ONLY object-specific content is the atom (B266)"*. That is a
**negation**: correct scope discipline, flagged as a violation.

Separating *"X is object-specific"* from *"the only object-specific content is Y"* needs
sentence-level parsing, not a regex. **A hard-fail gate that fires on a right answer trains readers
to ignore it**, which is worse than no gate — so the gate is **not built**, and the reason is
recorded rather than the gate quietly dropped.

**Worth noting for the record:** B727's row already banks the class/manifold split — *"the sister
m003 ties m004's field ℚ(√−3) (snappy-verified) but isn't a knot (H₁ = ℤ/5+ℤ)"*. The observation was
not two years late. **The mechanism — that commensurability invariance forces it — is the audit's
genuine contribution**, and that is what B803 verifies.

## What was adopted instead

**E34 — apparatus-inflation**, merging the audit's proposed *scope-inflation* with the atlas's
*method-inflation* as one class with two layers, because the failure is identical and only the layer
differs: **a property of the instrument or of a larger structure, read off the results as a property
of the object.** Minted in `docs/ERROR_LEDGER.md`, registered MANUAL in `docs/PRACTICES.md`.

Also adopted, on the audit's closing note and independent of everything above:

> **An instrument that works but cannot be found has failed.** No gate catches it, because nothing
> is wrong with the artifact. When you build an instrument, the same commit must put it in the path
> of the seat who will need it.

---

# SECOND ADDENDUM — the CLASS column was too wide, and the prior art was missed

Two corrections, both accepted after verification. Neither touches the verified premise (§1) or the
DKY/organ results (§3–§4).

## Correction 1 — "class-determined group" ≠ "everything computed in it is class-level"

The first draft's rule read *"everything downstream of the field"*. That is **too wide**. A character
variety is `Hom(Γ, G)//G` — its input is **Γ**, and **commensurable groups have different character
varieties**. So the CLASS column must split by *what the statement's input is*:

| | |
|---|---|
| **CLASS** (input = field/algebra) | invariant trace field, quaternion algebra, arithmeticity, `𝔽₃`, `SL(2,𝔽₃) = 2T`, **the E₆ label** |
| **MANIFOLD** (input = Γ) | **character varieties**, cohomology, torsion at the E₆ exponents, homology, knottedness ⟹ **amphichirality**, congruence data, **the spectra** |

**Consequence, checked:** `CLAIMS` **P49/P51 are NOT scope-inflated.** P51's *"ρ_prin's deformation
space in the figure-eight's E₆ character variety"* is correctly object-level — the variety is built
from Γ₄₁, not from ℚ(√−3). A search for a live instance of the defect found **none**; what it found
was a defect in the audit's own table.

**This also corrects a claim B803 made in its own §1**: "exactly three things survive as
manifold-level" understated the list. The representation theory of Γ₄₁ survives too.

## Correction 2 — the programme reached this two months earlier, and B803 cited none of it

| arc | date | what it banked |
|---|---|---|
| **B302** | June | *"the generation ℤ/3 is not in the object — it is in the object's relation to its arithmetic siblings, the commensurability class."* m004 has **no** order-3 element (Sym = D₄, order 8; knot groups are torsion-free); the **commensurator** `PGL(2,O₋₃)` does, by **Neumann–Reid**, precisely because m004 is *the* arithmetic ℚ(√−3) knot |
| **B307** | June | **theorem**: three *symmetric* generations need a cyclic-cubic (C₃) trace field, and **no hyperbolic knot has one** — the single-knot route is closed for **all** hyperbolic knots |
| **B486** | — | *"hexagonal cusp → three generations"* **REFUTED** (11th kill); the cusp is rectangular |

**B803 arrived at the same structure from the other direction and cited none of these.** That is a
convergence, not a duplication, and it makes the reading stronger: **B803 says *why* the chain's
conclusions are class-level; B302 says *what actually lives in the class* (the commensurator's
hidden ℤ/3); B307 says *what provably cannot live in the object* (a symmetric C₃).** Three
independent closures on the same question, all pointing away from the object and toward the class.

**Corrected row:** the generation count is *neither* CLASS-by-E₆-block-decomposition *nor*
MANIFOLD-by-Γ-cohomology. The single-knot route is **closed** (B307); the surviving route is the
**commensurator's hidden ℤ/3** (B302).
