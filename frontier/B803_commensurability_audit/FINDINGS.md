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
