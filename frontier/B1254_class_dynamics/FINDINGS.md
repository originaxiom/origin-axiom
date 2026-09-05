# B1254 — THE ORIENTATION CLASS HAS A DYNAMICS, AND IT MOVES IN EXACTLY ONE STRATUM

**Status: banked (frontier). Verdict PROVED.** `verification/class_dynamics.py`, selftest green
(rc captured directly, E39). Gate 5 clean: no measured value.

Joins two things the repo already held and which had never met.

| | |
|---|---|
| **B1248** (2026-09-05) | `det X ≡ 2 − κ` in `K*/(K*)²`, κ = tr[A,M] the Fricke–Vogt invariant — so the orientation class is **ε = squarefree(2 − κ)** |
| **B497** (2026-07-10) | End(F₂) has **four strata** on X(F₂), each with an **exact κ-law**. *"The program to date = stratum 1 of 4."* |

## The join

A stratum multiplies `(κ − 2)` by an explicit factor **F**. Because ε is a **square class**, F acts
on it through **its own square class** — so a factor that is a perfect square leaves ε untouched
**even though κ itself moves**.

| stratum | citizen | κ-law | F | ε |
|---|---|---|---|---|
| **1** | Aut, metallic a→aᵐb | `κ′ = κ` | 1 | **PRESERVED** |
| **2** | A→A², B→B² (det 4) | `κ′−2 = (κ−2)·x²y²` | **(xy)²** | **PRESERVED** |
| **3** | Thue–Morse a→AB, b→BA | `κ′−2 = (κ−2)(x²+y²−xyz)` | odd degree | **CAN CHANGE** |
| **4** | non-injective a→ab, b→ab | image ⊆ {κ = 2} | — | **UNDEFINED** |

**Stratum 3 is the only stratum that can move the orientation class**, and the proof is **parity, not
search**: `x² + y² − xyz` has **total degree 3**, and an odd-degree polynomial is never a perfect
square.

**Stratum 2 is the sharp one.** Its κ-law is non-trivial — κ genuinely changes — yet the factor is
`(xy)²`, so **the class passes through untouched**. B497 records what this stratum is at matrix
level: *"A→A² is literally transfer-matrix decimation — the RG face is matrix-level, not metaphor."*

**And B497's U1** — the reducible locus `κ = 2` is invariant under **every** endomorphism — is
exactly the locus where `2 − κ = 0` and ε is undefined. **The locus on which the class dies is
absorbing.**

## Why this was not already known

**B1157 banked *"the object supplies NO parameter-free dynamical law"* without citing B497.** That is
our own finding at **B1247** (2026-09-03), which located the mechanism: the atlas lexicon was 18
noun-motifs frozen 2026-07-01 with **no word for a question** — no motif for arrow, irreversibility,
dynamics, monoid, measurement, collapse, closing, naming or choice — so **B497 sat seven weeks** under
twelve object-motifs, not one of which says *monoid*, *strata* or *dynamics*. **B6**, holding the
field equation `□τ + κ(τ² − τ − 1) = 0` with an **earned** potential (critical points φ and −1/φ;
τ = 0 not a solution), has been on **zero surfaces since week one**.

> **The dynamics was never missing. It was unreachable.**

## Fences

- **No physics reading of the strata.** B497 fences the physics verb-names to `speculations/S063`;
  that fence is kept here. The statement is about κ and square classes.
- B1157's negative is **not** retracted by this arc: its scope is the ∞-place dynamical-law reading.
  What this arc shows is that a κ-dynamics exists and acts non-uniformly on ε — a different object.
- Three of the four strata have never been worked; the programme has lived in stratum 1.
- No measured value; no crossing. Gate 5 clean.

## Dependencies

B1248 (the class), B497 (the strata and κ-laws), B1247 (the retrieval fix that made B497 reachable),
B6 (the field equation, cited as the other unreachable dynamics), B1157 (the negative, scoped).
