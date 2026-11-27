# SM-R614 — the discrete symmetry surviving 27 → SM: on the root, nothing beyond the SM survives

*Page of the SM seat, 2026-11-26, for register row P-614 (main's page M53). The sealed card is
`relays/cards/SM_R614_the-discrete-remnant-of-27-to-sm.md`. Data-free and exact. Main's checkout was read at
be8c83d4f. No value of any of the 19 is touched.*

## 0. The verdict

- **In GENESIS's setting the residual is trivial.** The flat closing leaves SM × U1-η. Break U1-η with a vev on a 27
  singlet (ν^c, N or both) and the unbroken group's component group modulo the SM is trivial.
  - The ℤ/5 that the naive rule assigns to a charge −5 vev is already an element of the SM group. exp(2πi η/5) lies in
    the SM's hypercharge times its centre.
  - So **no discrete symmetry beyond the SM survives.** None is a matter parity. None forbids ν^cν^c.
- **At the E₆ level, the memos' setting:**
  - The surviving *torus* is exactly the SM torus, as memo 77 says.
  - The surviving *group* is larger. It is Spin(10) (dimension 45, rank 5) for any vev in the ν^c–N plane of one 27,
    because ν^c and N form a doublet of SU(2)_β. It is SU(5) (dimension 24, rank 4) for ν^c and N in two 27s.
  - So a 27-only breaking never reaches the SM.
- **Memo 76's census reproduces exactly:** 15 gradings, none odd on all 15 matter states, each odd on exactly 8.
  - All 15 lie in the SM torus. Its "14 extra E₆ remnants" are gauge elements of the surviving group, not extra
    symmetries.
  - Exactly one of them is central in the SM, the ℤ/6 shadow.
- **Matter parity:**
  - With N only it survives: B1805's z₂, odd on the 16 (Q, u^c, e^c, d^c, L, ν^c) and even on the 10 and the 1.
  - With any vev that touches ν^c it dies.
- **27³:** 45 zero-sum triples, none containing two SM singlets. B1418 (iv) is reproduced on main's own weights.

## 1. A bug, fixed after the run (disclosed)

- **The bug.** The sealed script `relays/sm_r614/run.py` (SHA-256 3c0d41bdb158ef68) stopped at its block-A assertion.
  None of the four SM embeddings matched B1303's table. Its output is `relays/sm_r614/r614_run.txt` (SHA-256
  2ffc72075d32557e).
  - The cause is one line. When the colour convention is flipped so that Q carries a 3, the flip also turned the colour
    singlets' label 1 into −1. No colourless state could then match.
- **The fix.** `relays/sm_r614/posthoc_run.py` (SHA-256 bf4b863919f9083c) is the sealed script with that line changed:
  the flip now applies to triplets only. It differs from run.py in that line, its docstring and its output file name,
  and in nothing else.
  - Its output is `relays/sm_r614/r614_run_posthoc.txt` (SHA-256 6b9f9d3d36351245) and
    `relays/sm_r614/r614_results_posthoc.json` (SHA-256 c17b7ce673d9b685).
- **The fix is labelling only.** It changes no computation downstream of block A. After it, all four embeddings
  reproduce B1303's table.

## 2. Results against the sealed expectations

| | expectation (prior) | result | |
|---|---|---|---|
| A1 | at least one of four embeddings reproduces B1303's table (90%) | 4 of 4 (after the fix) | holds |
| B1 | η = 3γ; constant; equal on ν^c, N; ⊥ SM roots, Y; β·η = 0; traces 0 (90%) | all true; ν^c = N = −5 | holds |
| B2 | η in the coroot lattice (85%) | coordinates (−5, −10, −12, −8, −4, −6), integer, gcd 1 | holds |
| E1 | N only: dim 45, rank 5, SM inside; parity, ν^c odd too (85%) | 45, 5, yes; 16 odd, 10 and 1 even | holds |
| E2 | ν^c only: dim 45, rank 5; no matter parity (60%) | 45, 5; none | holds |
| E3 | ν^c + N in one 27: dim 45, rank 5, SM inside (80%) | 45, 5, yes, for (1, 1) and (1, 2) | holds |
| E4 | two 27s: dim 24, rank 4; identity = V_SM; trivial; no parity (75%) | 24, 4; V_SM; trivial; none | holds |
| E5a | 15 gradings even on both doors (80%) | 15 | holds |
| E5b | none odd on all 15 (85%) | 0 | holds |
| E5c | each odd on exactly 8 of 15 (60%) | all 8 | holds |
| E5d | all 15 lie in the SM torus (80%) | 15 of 15 | holds |
| E5e | exactly one is SM-central (50%) | 1 | holds |
| G1 | identity dim 4 = SM for each singlet vev (90%) | 4, for ν^c, N and both | holds |
| G2 | residual modulo SM trivial; exp(2πi η/5) ∈ SM (75%) | trivial; yes | holds |
| G3 | no matter parity (90%) | none, also with ν^c required odd | holds |
| G4 | ν^cν^c allowed by every residual element (90%) | true (vacuously: no residual) | holds |
| M1 | 45 triples; none with two singlets; −2 × singlet no weight; η-neutral (90%) | 45; 0; no; all neutral | holds |
| P | P1, P2, P4 fail; P3 naive 5, 10, 5/3 while the lattice answer is fixed (95%) | as expected (below) | holds |
| C2 | the 2μ(ν^c) vev leaves ℤ/2 and a matter parity (55%) | ℤ/2 yes; matter parity **no** | **half fails** |

**The plants:**
- P1: with a vev on H_u, the SM is not in the stabiliser and V_SM is not in the kernel. Both are false, as they must be.
- P2: neither ψ nor χ is equal on ν^c and N. Both checks are false.
- P3: the naive ℤ/|q| rule gives 5, 10 and 5/3 for η, 2η and γ. The lattice gives the trivial group for all three. The
  naive rule fails, including at the "right" normalisation.
- P4: no torus element is odd on Q, u^c and H_u at once. It is not found.
- C1: E1's parity is found, as it must be.

**C2 does not fire as expected.** A charge 2μ(ν^c) vev does leave a nontrivial ℤ/2 modulo the SM. That ℤ/2 is not a
matter parity inside SM × U1-η. Reading, as inference: matter parity is (−1)^{3(B−L)}, and B − L does not lie in V₅ =
V_SM + ℝη. A 351′-type field therefore yields a parity only in a setting with more abelian room than the Y₃ closing
leaves. That is outside this row.

## 3. Reading

- **GENESIS's question, on the root.** "Dirac against Majorana: decided by the discrete symmetry left when the extra
  abelian factor is broken." On main's weights, in its U1-η normalisation, that symmetry is trivial when U1-η is broken
  by any 27 or 27̄ singlet vev.
  - Inference: a 27̄ singlet has the same weights negated, so the lattice is the same.
  - Dirac is therefore protected only while U1-η is exact, which is B1365's statement. Once it breaks, no symmetry
    forbids a Majorana mass.
  - Whether a Majorana mass is *generated* is a question about sources. 27³ and the 78 have none (B1418 iv, reproduced
    here). The record offers (27·27̄)² (B1418 v).
- **The row's text needs one scope correction.** "Only the SM torus survives" is true of the torus. The group surviving
  27-only vevs at the E₆ level is Spin(10) or SU(5), never the SM. This is the E₆ analogue of B1805(e).
- **The rest of the row stands on main's weights:**
  - the trivial ψ remnant: in E3 and E4 the torus has no components;
  - no matter parity among the surviving gradings;
  - parity kept by a singlet-only vev, at rank five;
  - no Majorana-shaped 27³ term.
- **The "14 extra" are not extra.** Memo 76 named 14 of its gradings extra E₆ remnants. They are elements of the
  surviving SM torus.

## 4. What is NOT checked

- **The connectedness of the Q₈ line's centraliser** (SM × U1-η taken as connected). This is an inference: the
  centraliser of SU(2)_β is SU(6) up to centre, and SU(6) is simply connected. −1 ∈ SU(2)_β is shown to lie in the
  torus V₅, a fact that cannot fail for a root. Weyl-type disconnected components are not searched. If one existed,
  it could add a discrete symmetry this page misses.
- The component groups of the non-abelian E₆-level stabilisers (only their tori are computed).
- Higgs content beyond 27 and 27̄; any potential, vacuum or holomorphy argument.
- Main's B1652 rules the E₆ frame refuted for the Standard Model. Everything here is the root's bookkeeping.
- No second computation: B1418's numerical code and the cloud memos share no code with this one but answer narrower
  questions.

## 5. Draft of the dated GENESIS note (text only; GENESIS is main's)

> **[2026-11-26, SM seat, R614; P-614]** On the root, in main's 27 weights and B1303's normalisation
> (U1-η = (3χ − 5ψ)/4, −5 on both ν^c and N), breaking U1-η by any 27 or 27̄ singlet vev leaves no discrete
> symmetry beyond the SM: exp(2πi η/5) is an element of the SM group. So nothing protects Dirac neutrinos once U1-η
> is broken, and no matter parity survives. A Majorana mass then needs a source: none in 27³ or the 78 (B1418 iv),
> one in (27·27̄)² (B1418 v).
> Scope: the Y₃ closing's centraliser is taken as connected (inference), and the root only (B1652).
