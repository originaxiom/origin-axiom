# `speculations/` — governance

This folder is the **evolving-ideas room**: the place where the project's speculative readings of the mathematics
are logged *richly* — including their **deaths** and their **held-pending-derivation** items. It exists so that
bravery has a home that does not leak into the proven core. It is the disciplined door, not the suspension of
discipline.

> **One-way firewall.** Speculations **MAY cite proved results** (`B`-probe / `V`-ledger / `P`-claim numbers) for
> traceability. **Proved results and `CLAIMS.md` NEVER cite speculations.** The arrow is one-way: speculation →
> *which calculation to look at*, never speculation → a mathematical conclusion. No content here promotes to
> `../CLAIMS.md` (root GOVERNANCE §5); the **physics chapter stays CLOSED**; the **ρ_n catalog proof stays the
> central math target**. Root `../GOVERNANCE.md` §8 wording binds (a "Lorentzian signature" is a Hessian/quadratic
> form, never "spacetime"; "`A` is the figure-eight monodromy," never "the universe is a knot").

## The two lines that are never crossed

1. **Numerology.** Matching an observed value without a derivation of *why that computed quantity is the physical
   one*. (This is what killed the cosmological-constant formula — see `TOMBSTONES.md` S014.)
2. **The killed spectral identification.** *Tower eigenvalues = masses / operator dimensions.* The tower is
   moduli-space monodromy (`±φᵏ`, a single scale); it is **not** a spectrum of masses (B107; `TOMBSTONES.md` S015).

Every entry in this folder respects both. An entry that brushes either line is logged as **HELD** or **DEAD**,
never as support.

## Proof-status enum

Every speculation carries exactly one status:

| status | meaning |
|---|---|
| `POSTULATED` | a reading proposed but not yet supported by any computation |
| `SUPPORTED` | a **structural** fact of the mathematics underwrites it (cite the `B`/`V`), with the physical reading kept explicitly separate as a `[LEAP]` |
| `TESTED-POSITIVE` | a bounded calculation was run and came out as the reading predicted (still firewalled) |
| `TESTED-NEGATIVE` | a bounded calculation was run and **refuted** the reading (a first-class negative) |
| `HELD(value-matching)` | produces a *number* with **no derivation** of why that number is the physical quantity — see the HELD rule |
| `DEAD` | falsified or shown circular; permanent; lives in `TOMBSTONES.md` with a link to the kill |
| `DORMANT` / `WALLED` | DORMANT = a fine calculation simply not yet run; WALLED = blocked by a *structural* obstruction (e.g. the 3d→4d type-mismatch), not a queued task |

## The HELD rule (the failure mode we already paid for, twice)

A `HELD(value-matching)` item's calculation **MAY be run** — but its result **cannot be banked as support**
without BOTH:
- **(a)** a derivation that the computed quantity *is* the physical one it is being compared to, AND
- **(b)** a **null-hypothesis test** (the exact discipline that killed the cosmological-constant formula: ask how
  often a random object would match as well).

Until both are met, a HELD result is "a number in search of a meaning" and is recorded as such — never promoted to
`SUPPORTED`, never to `CLAIMS.md`. A failed value-match does **not** retroactively make a *structural* sibling
claim `TESTED-NEGATIVE` (e.g. "hierarchies are powers of one scale" stays `SUPPORTED` even if matching a specific
hierarchy value fails — S013).

## What lives here

- `CATALOG.md` — the index: every speculation `S001…S028`, its status, one line, and its evidence/dependency.
- `PHYSICS_EXERCISE.md` — the long-form "assume it is the final theory" exercise (the tiered MASTER), whose only
  legitimate output is the ranked **calculation pointers**.
- `S0xx_*.md` — one short file per **live** speculation (the evolving ones).
- `TOMBSTONES.md` — the **DEAD** speculations as one-paragraph epitaphs, each linking to the kill (the
  `docs/atlas/FAILURE_ATLAS.md`, `../CLAIMS.md` D-rows, or the `V`-ledger).
- `archive/` — superseded long-form documents kept for traceability (`PHYSICS_RESONANCES.md`,
  `COSMOGONY_FROM_THE_VOID.md`).

## What does NOT live here

No mathematical content, proofs, computations, tests, or ledger results. Those live in `../frontier/`,
`../papers/`, `../src/`, and the `V`-ledger. A speculation that becomes a theorem **leaves** this folder (it gains
a `B`/`V` number and migrates); a speculation that dies becomes a tombstone. This folder logs the *journey of the
idea*, never the verdict — the verdict is always elsewhere, cited.

Companion rooms: `../philosophy/` (motivation that is not even a calculation pointer), `../story/` (the honest
narrative), `../ARCHITECTURE.md` (the one-page map).
