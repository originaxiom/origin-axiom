# B1618 — THE WEIGHTED CELL AT ω: given τ = ω, Dirac masses are degenerate at ω for every weight — the inner automorphisms make every mass matrix diagonal in the three parity lines at every τ, and U cycles the three entries; near ω they stay equal at leading order — so the tagged postulate τ = ω cannot give the observed hierarchy within the weave

**Verdict: PROVED** (Q2 and Q3 hold; Q1 holds for the Dirac term and fails in the stronger direction for the Majorana
term). cc (main), 2026-10-08. Sealed `434782554` before the run (its push carried two currency notes, commit
`f4b5cbb3f`, disclosed). "Given τ = ω" (the owner's tagged postulate). No data read. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /weight|automorphy|elliptic fixed|modular form|degenerate mass|inner automorphism|parity grading/: 82 of 1389 arcs on main match (NEGATIVE 11, OPEN 6, PROVED 65)`
— B1617, B1615, B1616, W20/W21; the audit (codex) lane at `f5da7ce4a`. **Literature:** modular forms at elliptic fixed
points; the near-fixed-point mechanism (cited).

## 1. The computation (`weighted_at_omega.py`; `weighted_at_omega.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **Q1** | the subspace fixed by the inner automorphisms and the sign is the three-dimensional diagonal in T̄ ⊗ T and in Sym² T, preserved by U | 85% | **Dirac: HOLDS** (dimension 3, preserved by U). **Majorana: FAILS in the stronger direction** — dimension 0: with the sign's eigenvalue taken as +1 (even weight), no Majorana coupling survives at all |
| **Q2** | for every 24th-root phase the U-eigenspace is at most one-dimensional and gives three equal masses | 85% | **HOLDS** — U's eigen-phases on the diagonal are 1, ω, ω² (0, 8, 16 twenty-fourths), each one-dimensional, each giving masses (1, 1, 1) |
| **Q3** | U permutes T's parity lines as a 3-cycle | 90% | **HOLDS** — the lines carry the parity characters (a, b) = (−, +), (+, −), (−, −) and U sends them 0 → 1 → 2 → 0 |

## 2. What it says

Given τ = ω, **the Dirac masses are degenerate at ω for every weight**: the inner automorphisms fix every τ with
automorphy factor 1 and act on the matter as the parity signs, so every coupling that is a function of τ is diagonal in
T's three parity lines; at ω the stabiliser U cycles the three lines, and every eigenvector of a cyclic shift has entries
of equal modulus. Near ω the relation propagates order by order (Q3 is its input): the three entries vanish to the same
order with equal leading moduli — quasi-degenerate, never the observed hierarchy. **So the tagged postulate τ = ω, which
main recommended, cannot be the source of the fermion hierarchy within the weave.** A hierarchy among the three diagonal
entries needs a point where the parity sectors behave differently — the cusp (large Im τ), where the three half-period
theta characteristics separate as different powers of q — a different postulate for τ, the owner's to make.

## 3. Disclosed

- **A modelling hole:** the sign −I has automorphy factor (−1)^k; the instrument imposed eigenvalue +1 for the sign, so
  the Majorana result (none) covers even total weight only; odd weight (the sign's −1 eigenspace) is not computed.
- The outcome was argued in conversation before the seal (disclosed there).
- The seal's push was blocked by the doc-currency gate; SM_SPECIFICATION_LEDGER and RETRACTED_PHRASES were brought
  current in a separate commit (`f4b5cbb3f`).

## 4. Files

`verification/weighted_at_omega.py` (sealed, unchanged), `weighted_at_omega.json`, `weighted_run.txt`. Test:
`tests/test_b1618_the_weighted_cell_at_omega.py`.
