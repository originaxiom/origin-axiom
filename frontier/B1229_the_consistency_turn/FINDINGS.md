# B1229 — THE CONSISTENCY TURN: the method was wrong, not the object

cc banking seat, 2026-08-31. Owner: *"we have to think of completely other approach, be brave go
bold"* / *"step back and back and back and back and search research."* **Gate 5 absolute. Verdict
OPEN — this opens a program; it does not close a row.**

## The diagnosis

`GRAND_COMPUTATION_v0` §6 is a **deletion schedule**: kill an input row by **deriving** it from the
object. That is the hardest move available, and it asks the object to do the one thing **B1225
proves it cannot do — select**. It is why B1216 spent nine agents on row 1 for **zero deletions**,
and why every route this session died at the same wall.

**Physics has never reduced a parameter count by derivation.** It uses **consistency conditions** —
the bootstrap.

**The gap, measured:** `modular bootstrap` → **0 tracked files**. `conformal bootstrap` → 1.
`constructor theory` → 0. `assembly theory` → 0. An entire methodology built for this situation,
never touched.

## The robust core (cited, not assumed)

**Anderson–Moore / Vafa:** in *any* rational CFT, the central charge and every conformal weight are
**rational**. The boundary of a Chern–Simons theory *is* rational. With Brown–Henneaux `c = 6σ`
(B1088, banked, derived twice):

> **σ is rational.** The map's "ONE continuous dimensionless anchor" is not continuous.

## The sharp version

**Mathur–Mukhi–Sen — a complete classification.** Two-character RCFTs with vanishing Wronskian index
are exactly the **Deligne–Cvitanović exceptional series**: seven unitary WZW models, 0 < c < 8.

| g | A₁ | A₂ | G₂ | D₄ | F₄ | **E₆** | E₇ |
|---|---|---|---|---|---|---|---|
| c | 1 | 2 | 14/5 | 4 | 26/5 | **6** | 7 |
| σ = c/6 | 1/6 | **1/3** | 7/15 | 2/3 | 13/15 | **1** | 7/6 |

**ℝ⁺ → 7 values, by consistency alone.** Then the object's own **ℤ/3** — trace field ℚ(√−3), the
trinification (B727/B1161) — keeps only the 3-primary theories, A₂ and E₆:

> **σ ∈ {1/3, 1}. σ becomes ONE BIT. ℝ⁺ → 7 → 2.**

**J never enters.** The session's earlier route died because the literature is explicit that the 6d
type is a **free label** (T[M;G] depends on M *and* on g separately), and because B1228's nomination
carried a **type error** (π₁'s 2T is not the transverse ALE Γ). This route needs no J, derives
nothing from the object, and is untouched by either failure.

## The consistency ledger — every row

| row | consistency condition | result | grade |
|---|---|---|---|
| **σ** | RCFT rationality + MMS | ℝ⁺ → 7 → 2; one bit | **COMPUTED** |
| **the c-bit** | classification of **modular invariants** | it **is** the diagonal-vs-charge-conjugate choice — a ℤ/2. Not deleted, **explained** | STRUCTURAL |
| family / VEV labels | primaries / Cardy states | already finite | STRUCTURAL |
| **the ℙ³ line** | **Cardy's theorem**: consistent boundary states are finite (bijective with primaries) | a *continuum* of them cannot all be consistent | **CANDIDATE — sharpest unrun test** |
| λ | KMS weight; modular flow periodic for a rational boundary | would become a finite label | CANDIDATE |
| **ℓ** | none — and correctly | **not a parameter: a calibration**, permanently | CLOSED-BY-TYPE |

**The c-bit result is worth its own line.** For a ℤ/3 fusion ring the modular invariants are the
diagonal and the charge-conjugate — a ℤ/2. So the c-bit **is** the modular-invariant choice, and
that matches **B1184** exactly: *the theory names itself (the fusion ring) and cannot sign (which
invariant).* Self-naming without self-signing, arriving from a completely independent direction.

## The thesis this opens

> The observer's input list is not a grab-bag of externals. It is **exactly the data specifying a
> modular-invariant boundary CFT** — central charge, modular invariant, primary/Cardy state, KMS
> weight — plus one calibration that is not a number.

That is **why** the object cannot supply them (B1225: it cannot select), and why they are
nonetheless **not arbitrary**: *consistency classifies the menu even where the object cannot pick.*
**B1225 is untouched and is not an obstacle** — a classified finite menu plus a picker **is** a
parameter-free theory with a calibration, which is the map's own goal sentence: *"one measurement
then predicts the rest."*

**End-state if the two candidates land:** `ℓ` + bits and finite labels — **zero continuous
dimensionless parameters.** Not claimed now.

## Fences

- The 7-value list assumes **two characters, vanishing Wronskian index**. Drop it and the menu grows
  — but **rationality (hence discreteness) survives**, and that is the robust core.
- The **ℙ³** row needs the Higgs line to *be* boundary data of the rational theory. Named, not
  assumed; if it isn't, Cardy doesn't apply and the row stays contested.
- **λ**'s periodicity is a candidate, not a computation.
- Nothing promoted to `CLAIMS.md`; no measured value anywhere.

## Reproduce

`sh frontier/B1229_the_consistency_turn/reproduce.sh` · lock `tests/test_b1229_consistency.py`
