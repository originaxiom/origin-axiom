# B1617 — THE WEAVE AT τ = ω: given the owner's tagged postulate τ = ω, the residual symmetry (order 48) keeps the matter triplet irreducible — the masses at ω are degenerate and there is no Majorana mass; near ω they split by powers of ε into a quasi-degenerate pattern, the opposite of the observed hierarchy; weighted modular-form Yukawas are the owed cell

**Verdict: NEGATIVE as sealed** (Z0, Z1, Z4 hold; Z2 and Z3 fail). cc (main), 2026-10-08. Sealed `da3027e03` before the
run. **The owner's ruling (2026-10-08, in this session): τ = ω is a tagged working postulate** — every result here is
"given τ = ω". No data is read. **0 of 19.**

## 0. Seen first

As sealed (the sweep line in the preregistration, 35 arcs) — B1611–B1616, B1612's residual subgroups, W19–W21, B1601 and
LR ≡ ST mod 2. **Literature:** the stabilisers of PSL(2, ℤ); the near-fixed-point mechanism (Novichkov, Penedo, Petcov),
cited, its statement imported and tagged in Z4.

## 1. The computation (`weave_at_omega.py`; `weave_at_omega.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **Z0** | U as a short word, fixing ω; a consistent composition order | 95% | **HOLDS** — U = L⁻¹ then R (images a → b, b → a⁻¹b), fixing ω under the matrix action and its inverse; the move matrices compose in reverse order (M(L∘R) = M_R M_L) |
| **Z1** | the residual group finite, preserving T; the inner automorphisms acting as parity signs | 70% | **HOLDS** — order 48, T preserved; conjugation by a acts on V as (−, −, +, +, −, −) and by b as (+, +, −, −, −, −) — the parity characters |
| **Z2** | T splits into three lines with distinct characters | 60% | **FAILS** — T is irreducible under the residual group (commutant 1): the parity grading (inner, an exact symmetry at every τ) together with U's 3-cycle on the parities acts on T as A₄ does on its triplet |
| **Z3** | at ω three free Dirac couplings, no mass relation; at most one Majorana coupling | 55% | **FAILS on the Dirac part** — one invariant direction, three equal masses (Schur); **holds on the Majorana part** — none |
| **Z4** | three distinct charges on T; non-zero charge differences | 60% | **HOLDS** — U's lift has order 12 on T, eigen-turns ¼, 7/12, 11/12; differences ⅓, ⅔ |

## 2. What it says

**Given τ = ω, the masses are degenerate at the point.** The residual symmetry is larger than the elliptic element: the
inner automorphisms, which fix every τ, act on the matter as the parity grading, and with U's 3-cycle they keep T
irreducible. So an ordinary vacuum at ω gives three equal Dirac masses and no Majorana mass. Away from ω the degeneracy
splits by powers of ε = τ − ω: a quasi-degenerate spectrum, not the observed hierarchy. At a generic τ the grading alone
remains: T splits into its three parity lines and the masses are three free couplings (B1615's count).

**What is owed.** Z3 took weight-0 vacua (invariants). In the modular-flavour reading the Yukawa couplings are modular
forms of weight k, and at a fixed point they lie in the eigenspace of the stabiliser with the automorphy factor's phase,
not in the invariant line — the cell that decides whether τ = ω can give anything beyond degeneracy. It needs the weight
(W20/W21's Hodge-line powers) and the eigenspaces of U's lift on the Higgs representations at the phases ω^k.

## 3. Disclosed

- Z3 covers weight-0 vacua only (stated above).
- The instrument was cleaned before the seal (disclosed there).
- The owner's ruling is recorded on GENESIS v1.34.

## 4. Files

`verification/weave_at_omega.py` (sealed, unchanged), `weave_at_omega.json`, `omega_run.txt`; `adoption/amend.py`
(GENESIS v1.34), `received/GENESIS_v1_33_main.md`. Test: `tests/test_b1617_the_weave_at_tau_omega.py`. Kill-graph entry B1617.
