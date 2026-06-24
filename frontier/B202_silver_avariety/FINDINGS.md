# B202 — the silver SL(3) A-variety: no tidy `[A,B]=c·µᵏ` (the figure-eight's `M³=L` is non-generic)

**Date:** 2026-06-24. **Status:** completes the SL(3) metallic-A-polynomial direction begun in B201 (the silver
character variety). **Result (validated):** the silver (m=2) bundle has a **correct commuting cusp meridian
`µ=A⁻²t`** (B154; verified `cdev~1e-9` on all four components), but **none of its four character-variety components
carries a tidy matrix A-variety relation `[A,B]=c·µᵏ`** — whereas the figure-eight's Dehn-filling components do
(`W1: c·µ³ = M³=L`; `W2: c·µ⁻³ = M³L=1`). So **the figure-eight's tidy Dehn-filling A-variety is non-generic in the
metallic family**; the silver A-variety is "all Falbel-size." Standalone character-variety / low-dim-topology math;
**no physics; nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger V195. (Resolves OPEN_LEADS L23(a).)

## Method (pairing-free, validated against B71)

`k` is read as the **matrix exponent**: the integer with `[A,B]·µ⁻ᵏ` a scalar matrix (the B71 `symbolic_dehn` /
B198 criterion). This is gauge- and eigenvalue-ordering-invariant — unlike eigenvalue-ratio relations `MᵃLᵇ`, which
*scramble* across scattered Sage-sampled points (the magnitude-sort of `µ`-eigenvalues reorders), the bug that sank
an earlier attempt (B201 Part 2). **Gate:** on the figure-eight, this recovers exactly `W1 → k=3` (score ~1e-10…1e-14
over 6 reps) and `W2 → k=−3`, with the geometric V0 giving no constant `k` — i.e. it reproduces B71's `M³=L`/`M³L=1`
and the V0 "no tidy form." So the method is sound; the silver result below is trustworthy.

## Result — silver has no tidy A-variety relation

Sampling reps on each of the four silver components (Sage `variety(QQbar)` on `Fix(T_2²)`, B201), realizing
`(A,B)` (B71 `realize`), solving the silver monodromy `t` (word `A³BA²B`, B154), and forming `µ=A⁻²t`:

| silver component | commuting-meridian reps | best matexp score (median) | tidy `[A,B]=c·µᵏ`? |
|---|---|---|---|
| comp0 (geometric `{x1=x4,x2=x5}`) | 6 | **16.1** | **NO** |
| comp1 `{x1=x4}` | 5 | **6.5** | **NO** |
| comp2 `{x2=x5}` | 5 | **2.8** | **NO** |
| comp3 (new `{trA+trA⁻¹=−1,…}`) | 6 | **1.2** | **NO** |

Every component has reps with `µ=A⁻²t` genuinely commuting with `[A,B]` (`cdev<1e-5` — the *correct* cusp meridian,
B154's `φ_m([A,B])=Aᵐ[A,B]A⁻ᵐ`), yet the best matrix exponent `k∈[−8,8]` leaves `[A,B]·µ⁻ᵏ` far from scalar
(score O(1), never `<1e-6`). So **no silver component reduces to a clean `[A,B]=c·µᵏ`.**

**Why (structural, from B201):** the silver "Dehn-filling-type" components are `{x1=x4}` / `{x2=x5}` — *not* the
trace-1 `{x1=x4=1}` of the figure-eight's W1 (the component that gives `M³=L`). The figure-eight's tidy components are
a special low-trace degeneration absent in the silver family. The silver geometric component, like the figure-eight's
V0, is Falbel-size (no tidy form, B71/B199).

## What this means for "the metallic A-polynomial on the geometric component"

The integer exponent `k` (B198/B199) is a *cusp-point* shadow of the A-variety. B202 shows the **continuous** A-variety
relation is **tidy only for the figure-eight's special Dehn-filling components**; for silver every component is
Falbel-size, so a closed-form silver SL(3) A-polynomial is **NEEDS-SPECIALIST** (worse than the figure-eight's
141-poly, consistent with B199's SL(3)-geometric verdict). The honest metallic A-polynomial picture at SL(3) is now
complete: **SL(2) tidy (B67/B69); SL(3) figure-eight tidy only on the trace-1 Dehn-filling components (B71); SL(3)
metallic (silver) — no tidy component at all (B202).**

## Firewall
Standalone character-variety / low-dim-topology mathematics. No physics; nothing to `CLAIMS.md`; P1–P16 untouched.

## Reproduction
- `sage-python avariety.py` — the figure-eight matexp gate (W1→k=3, W2→k=−3, V0 none) + the silver per-component
  no-tidy result (correct commuting `µ=A⁻²t`, matexp score O(1)); dumps `reps.json`.
- `tests/test_b202_silver_avariety.py` (pyenv, numpy-only) — loads the shipped reps: figure-eight W1 → `[A,B]=c·µ³`
  (k=3, score<1e-6); silver → `µ` commutes (cdev<1e-4) but no tidy exponent (score>1e-3). 2 passed.
- `reps.json` — the shipped reps (2 figure-eight W1 + 3 silver) for the deterministic test.
