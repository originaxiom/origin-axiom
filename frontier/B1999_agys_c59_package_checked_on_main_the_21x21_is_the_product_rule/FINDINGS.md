# B1999 — the agy lane's C59 package checked on main: its 72° up-sector phase and its mirror CP theorem hold exactly; its "zero-parameter" 21 × 21 boundary-Dirac matrix is the ordered 7-fold product rule rewritten, and the hierarchy it shows is set by the chain's length and choice of chain

**Verdict: PROVED for its checks (the identity exact, on main's code only; items 2 and 3 and item 4's response REPRODUCED on the
seat's own frame C function by main's code, its sealed output to 4 × 10⁻⁸ on 8 of 8 chains; main's own frame C recompute of items
2 and 3 owed, P-884 Q3).** Main, 2026-11-25, at the author's question ("is this true", then "are u sure ure not
downplaying or sabotaging anything"). Data-free. Harvest row 2002; register row P-884. **0 of 19.**

## Seen first

- **The lane's summary,** relayed by the author, and its card AGY-C59 (the lane's local commit `e4d220b75` on this machine, not yet pushed; its pushed branch `origin/agy/cusp-action-2026-11-20` ends at C56, `36f06f522`).
  - C57 and C58 carry the same claims and stopped before output.
  - C59's producer and output are copied verbatim to `verification/seat_copy/`; their SHA-256 match the seat's committed
    SCRIPT_SHA256 and OUTPUT_SHA256.
- **Main's own line:**
  - B1993 and B1994 (the (3, 3, 3) torus and ω's symmetry LR⁻¹);
  - B1971 and B1973 (frame C's mixing on m004's order-30 thread);
  - B1972 (agy-exp's banking candidates checked: identities by construction counted as such).
  - The author's ruling of 2026-11-25 put the order-30 line on hold and asked for no Standard-Model-shaped pass/fail cells.
- **Swept** (`scripts/checks/topic_sweep.py`): `VERDICT topic-sweep /Schur complement|boundary-Dirac|waveguide|product rule|holonomy|amphicheiral|Jarlskog/: 85 of 1740 arcs on main match (NEGATIVE 16, OPEN 6, PROVED 63); 36 register rows match (DEC`. Nothing on main checks this package; B1972 is the precedent for a
  seat's package checked.
- **The literature (standard):**
  - The Schur complement of a block-bidiagonal chain is the ordered product of its blocks: the transfer-matrix identity.
  - Hierarchies from products of Yukawa-like blocks along a chain are the deconstruction and clockwork constructions.
  - The Markoff triple (3, 3, 3) and the commutator subgroup of SL(2, ℤ) are classical.

## Custody

The checks were run in main's scratchpad before CARD.md was written. The card says so; there were no blind expectations.
Frame C's Yukawa values come from the seat's own sealed function, imported read-only under the author's ruling of
2026-11-24. Everything built on them is main's code. The identity check uses main's code only.

## The results

**Item 1 (E1): the mathematics holds; the conclusion does not follow.** U = LR, V = L⁻¹R⁻¹ and (UV)⁻¹ have trace 3, are
GL(2, ℤ)-conjugate to LR, and are cycled by LR⁻¹. On the torus they are loops; in m004, LR is the gluing map. That the
hexagonal torus's shortest loops lie in the golden class is classical. It does not make the whole select m004.

**Item 2 (E2): holds exactly on the seat's frame C function, reproduced by main's code** (`check_c59_run.txt` (3)); main's own
frame C recompute is owed. After 12 steps, on all 8 orbits:
- the up sector's phase is e^{∓2πi/5}, at 72.0° (agreement 10⁻³⁸);
- the down and lepton phases are 1 (10⁻³⁸).

That the phase forces the ±R_σ fold is the lane's reading: the fold is a construction, and the phase does not imply it.

**Item 3 (E3a): holds exactly on the seat's frame C function, reproduced by main's code** (`check_c59_run.txt` (4)); main's own
frame C recompute is owed. From each of the 8 mirror walls, clockwise and counterclockwise
chains give:
- identical CP-even outputs (10⁻³⁸);
- J_cw + J_ccw = 0 (10⁻⁴⁰).

Which wall is used moves |J| from 0.0011 to 0.0256, in four values that come in pairs. Reading the half as "the universe
choosing matter" is an interpretation.

**Item 4 (E4): the construction is the product rule** (`schur_identity_run.txt`).
- **The identity:** the 21 × 21 matrix has diagonal blocks Y₀ᴴ, Y₁, Y₂ᴴ, …, Y₆ᴴ and superdiagonal −s·I. Its Schur complement
  over the 18 × 18 interior is exactly (H₆ ⋯ H₀)ᴴ/s⁶ = Y₀Y₁ᴴY₂ ⋯ Y₆/s⁶, to 4 × 10⁻⁴¹ for 20 random block sets and three
  steps s.
- **What "zero parameters" amounts to:** the step cancels in every ratio, to 2 × 10⁻⁴¹. That is the only sense in which
  the matrix has none. It re-expresses the discrete product rule it was said to replace; the Z factors are sums of its partial
  products.

**Item 4, the response to its choices** (`check_c59_run.txt`). Main's driver reproduces the seat's sealed values on 8 of 8
chains, to 4 × 10⁻⁸ relative. The difference is the L₂ input: the probe's 15-digit typed value against the seat's solved one.

- **The chain length K moves the depth of the hierarchy.** On the seat's own reference chain:

  | K | up m₁/m₃ | up m₂/m₃ | |V₁₂|, |V₂₃|, |V₁₃| | |J| |
  |---|---|---|---|---|
  | 1 | 3.5 × 10⁻⁵ | 0.57 | 0.10, 0.27, 0.046 | 0 |
  | 3 | 5.3 × 10⁻¹⁰ | 0.20 | 0.16, 0.096, 0.058 | 0.0009 |
  | 5 | 6.2 × 10⁻¹⁴ | 0.067 | 0.16, 0.15, 0.072 | 0.0016 |
  | 7 | 3.9 × 10⁻¹⁸ | 0.043 | 0.16, 0.15, 0.072 | 0.0017 |
  | 9 | 5.3 × 10⁻²² | 0.026 | 0.16, 0.18, 0.075 | 0.0020 |
  | 11 | 1.0 × 10⁻²⁶ | 0.044 | 0.16, 0.14, 0.075 | 0.0015 |

  The lightest ratio falls about 10⁻⁴ for every two blocks; the down and lepton sectors do the same.
- **The choice of chain moves everything by one to two orders.** At K = 7, from all 96 starting sheets:

  | output | range |
  |---|---|
  | up m₂/m₃ | 0.0035 to 0.36 |
  | down m₂/m₃ | 0.010 to 0.56 |
  | lepton m₂/m₃ | 0.0023 to 0.42 |
  | |V₂₃| | 0.15 to 0.95 |
  | |J| | 2 × 10⁻⁴ to 0.029 |

  - The ordering u > d > e in m₂/m₃ holds on 36 of the 96 chains.
  - The seat's own sealed output shows its four spectra. The lepton m₂/m₃ is 0.0031 on one pair of walls and 0.35 on the other.
  - The package reports the "(a₅/5) = +1, wall v₀" one.
- **What holds across the choices (credit):**
  - a single frame-C Yukawa already has one very small singular value in the up and lepton sectors (3.5 × 10⁻⁵ and
    1.9 × 10⁻⁴ at K = 1);
  - the mixing moduli barely move with the chain length once K ≥ 3 (0.16, about 0.15, about 0.07);
  - J vanishes at a point and not along a chain.

## What the package is, read in its own terms

- **Two exact results in frame C on m004's order-30 thread:**
  - the up sector's fifth-root 12-turn phase;
  - the mirror's CP antisymmetry.
- **A classical identity on the systoles.**
- **A linear-chain reading of the product rule, which is legitimate but adds no evidence.**
- **The hierarchies in the summary are not derived with zero parameters.** Their depth follows the number of blocks and
  their pattern follows the chain chosen. The thread (m004), the level (30), the sector charges and the wall are choices as
  well.
- **The card's conditions are Standard-Model-shaped,** as the summary and the card show ("u > d > e", "|V_us| > |V_cb| >
  |V_ub|", "|J| > 3/2000"). They were written after the lane's scratch probe had shown the numbers. Main reads none of the
  outputs against data.

## What is open (P-884)

- **E3b,** the claim that unbroken G_SM covariance requires an odd K and selects K = 7, is not checked here. If it holds, K
  is fixed within the frame, but the wall and the thread are still chosen.
- **C49 to C56** are registered by name (harvest row 2002), not read in full.
- **Items 2 and 3 on main's own frame C implementation,** not the seat's function, so that they move from REPRODUCED to
  VERIFIED.
