# SM-C13b — the read-out at order 10 = 5 × 2 over the mark: does it give the leptons rows of their own?

*Card of the SM seat, 2026-11-14, approved by main in M33 ("structure only, its lepton rows written as differences,
nothing compared"). Committed and pushed, with its expectations, before any of it is computed. **Only differences are
written**: lepton outputs minus down outputs, never an output itself. Nothing is set beside a measured number.*

## 0. What is derived before any run

- **D1: the read-out at order 10 is one average.**
  - The 72 points of order exactly 10 on the fibre form one orbit of SL(2, ℤ). Through SL(2, ℤ/10) =
    SL(2, F₂) × SL(2, F₅), the group acts transitively on (the 3 non-zero points mod 2) × (the 24 non-zero points
    mod 5).
  - Each point of order 5 has three halves of order 10 (and one of order 5), so the 72 are exactly the order-10 points
    over the 24.
  - One change from B1928's argument: SL(2, F₂) ≅ S₃ is not perfect. Its sign, read on a word in L and R, is the
    parity of the word's length. So the mixing step holds within each length-parity class, not across them.
  - Each coset of A₃ still moves the three points of order 2 simply transitively. So the fibre still equidistributes
    over the 72 points in each class, and the limit is ∫ F̄₁₀ dμ, with F̄₁₀ the frame averaged over the 72 points.
  - It is the same at each half of the mark and at every point of order 10. "Over the mark" fixes the level, not the
    point. B1928's hypotheses H1–H3 are inherited, not checked here.
- **D2: what the average does to the lepton rows.**
  - Averaging over the 72 points is unchanged when a sector's charge pair is multiplied by a unit of ℤ/10. It is also
    unchanged by the transposition, which keeps the singular values.
  - The down pair (1, 2) has the unit multiples {(1, 2), (3, 6), (7, 4), (9, 8)}, and its transpose has
    {(2, 1), (6, 3), (4, 7), (8, 9)}.
  - The lepton pair (−3, 6) ≡ (7, 6) has {(7, 6), (1, 8), (9, 2), (3, 4)}, which meets neither.
  - (9, 2) ≡ (−1, 2) lies in the lepton class, so the lepton average is the down step with the doublet's twist
    negated: F̄₁₀^lep = the average of F₍₋₁,₂₎. No identity of this kind forces it to equal F̄₁₀^down. (B1935's centre,
    which negates every charge, is the unit 9 and is already counted.)
  - At order 5 the same algebra gives (−1, 2) ≡ 2 · (2, 1), which is the transposition (B1934). The averaged copy
    there is exact.

## 1. What is computed

Everything is computed with main's frame C as B1928 reads it, imported unchanged from a checkout of main at 847031d5f:
B1927's canon_readout, whose frame() carries the closed-form channel norm. Both of B1928's ends are used (the
constant ends, and B1667's canonical end), and the readings S and S̃ (B1928 leaves S* out). The outputs are the two
ratios of each sector's coupling.

- **K1 (the control at order 5).** On B1928's fine grid (1 046 points of the fundamental domain), F̄₅^lep − F̄₅^down,
  averaged over the 24 points of order 5.
- **K2 (order 10, at B1724's four moduli).** The relative difference of F̄₁₀^lep from F̄₁₀^down, for every end and
  reading.
- **K3 (D2 checked).** At the four moduli, F̄₁₀^lep against the average of the down step with charges (−1, 2). The
  step is SM-C13's explicit-charge copy of the frame's per-sector step, first checked to reproduce frame C.
- **K4 (the plant).** Lepton charges (2, 1) in the same step. The order-10 difference from the down rows must vanish.
- **K5 (the read-out on the whole at order 10).** D(τ) = F̄₁₀^lep − F̄₁₀^down is tabulated on B1928's fine grid; only
  D is kept. ∫ D dμ is computed by B1928's ergodic route: the same 3 000 random words of 40 letters (seed 1924),
  length-weighted, with a jackknife error in 30 blocks. The result is z = |∫ D dμ| / se, for every output and both
  ends.
- **K6.** The same ergodic integral of K1's order-5 difference.

## 2. Expectations, written before any run

| | expectation | prior |
|---|---|---|
| K1 | F̄₅^lep = F̄₅^down at every grid point, end and reading: relative difference ≤ 1e-8 (the bar is set from SM-C13's noise floor of 1.2e-9) | 97% |
| K2 | F̄₁₀^lep ≠ F̄₁₀^down at every modulus, end and reading: relative difference > 1e-6 | 85% |
| K3 | F̄₁₀^lep = the average of F₍₋₁,₂₎ to 1e-8 at every modulus, end and reading | 90% |
| K4 | with lepton charges (2, 1), the order-10 difference is ≤ 1e-8 | 97% |
| K5 | the read-out on the whole at order 10 separates the lepton rows: z > 3 on at least half the outputs, at both ends | 70% |
| K6 | the order-5 integral of the difference is 0 to 1e-8 | 97% |

## 3. What the outcomes mean

- **If K2 and K5 hold:** the read-out at order 10 gives the leptons rows of their own. They differ from the down rows
  exactly by the doublet's twist sign (D2), which is the bit that the tick's parity reads (SM-C13). Whether the read-out
  on the whole should be taken at order 10 is main's question (P-845). Nothing here says the separated rows are right.
- **If K5 fails while K2 holds:** the separation is a property of single moduli that the average over the geodesic
  flow washes out. That would be a structural negative for order 10 as a cure.
- **If K3 fails:** D2's algebra is wrong somewhere, and K2's reading has to be redone.

## 4. Files

relays/sm_c13b/, with its scripts, outputs (differences only) and runs. The page will be
relays/SM_C13b_THE_READ_OUT_AT_ORDER_10.md.
