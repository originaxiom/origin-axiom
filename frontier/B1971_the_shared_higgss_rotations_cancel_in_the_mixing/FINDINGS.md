# B1971 — Under the two-doublet reading the shared Higgs's own rotations cancel in the cusp mixing: every mass state lies along one direction of a null frame, the mixing is the permutation between the two sectors' frames, and what survives is set by the channels

**Verdict: PROVED** for the checks N1 to N5:
- N2's identities are exact (sympy);
- N1 and N3 to N5 are numerical, at heights 20 and 30 and the column x = 0.13, at 40 + 2 Im τ digits or more;
- N1 is main's second computation of the web seat's W-D2 D-1 rate table.

Main, 2026-11-24. Data-free: nothing is compared, and no target is opened. Register rows P-860 (d) and P-847. **0 of 19.**

What this arc is for: the record has found three times that, when every sector reads S, the cusp mixing aligns but
comes out too small:
- B1742, October, B1656's frame: with τ fitted, |V_us| came out at 0.19 of its measured value;
- the web seat's W-D2 D-1: the mixing falls with height;
- B1970: the reading is derived given I-37 and holomorphy.

This arc finds the mechanism. It is not a new frame, and it does not fix the size.

## Seen first

- **Swept:** `VERDICT topic-sweep /null frame|nearly null|nullity|shared Higgs|Higgs.s own rotation|cancel.*mixing|mixing.*cancel|a = 1/2|mixing too small|falls with height/: 12 of 1711 arcs on main match (NEGATIVE 3, PROVED 9); 9 register rows match (DONE 5, QUEUED 4)`.
  `already_banked.py` on the same terms found B1645, B1644, B1646, B1651, B1654, B1655 and B1691. They were read for
  their bearing, and none computes a mixing.
- **What the record already holds, and is used here unchanged:**
  - **B1739 (PROVED):** the record's Higgs is nearly null, with h·h = η⁶/4 exactly. N3 finds the same identity in
    frame C's closed-form variables, so the Higgs's nullity is B1739's and is not claimed here.
  - **B1742 (PROVED):** two nearly null directions read S everywhere give alignment and a hierarchy, with the mixing
    too small.
  - **B1736 / B1966 / B1969:** the closed form Y = u hᵀ + h uᵀ − (u·h)1 + w[h]_×, the identity Y h = (h·h)u, and
    det Y = (h·h)(w² + u·u)(u·h).
  - **B1945:** frame C's mass exponents and its split.
  - **B1946 and B1963:** the all-S mixing aligned at points of order 5, and unaligned at some points of orders 8
    and 10.
  - **B1962:** frame D1 deranged under every reading.
  - **B1970:** the all-S reading, derived given H1 to H3.
- *Dated correction (2026-11-24, after landing; B1972's reading of the seats' relays).* Seats had parts of this arc
  earlier, in relays to main that main had registered by name and had not read before computing:
  - **agy-002's A2-P879 (2026-11-20; harvest row 1995).**
    - Its T1 is the null-frame reduction to an exact 2×2 block (B1966's E4 in sympy).
    - Its T4(a) is the up sector's w = 0 at every point of order 5, which is N2's premise.
    - Its T4(b): up and down share q_L = 1, so their channel residues are rank one with one left spinor. That is the
      channel-side reason the sectors align.
  - **The agy lane's C8 (2026-11-21; harvest row 1993).** It gives the exact all-S mixing exponents, in |q| units:
    (3/10, 3/20, 11/20) at a = ±2/5 and (9/20, 1/20, 1/2) at a = ±1/5. That is N1's table, so N1 is a third computation
    after W-D2's and C8's.
  - **The agy lane's C1 (2026-11-20).** It gives the all-S alignment at the 20 points of order 5 with a ≠ 0.

  **What remains new here:**
  - every mass state's null-frame assignment;
  - the cancellation of the Higgs's own rotations (N4);
  - the census at orders 8 and 10 and its failures on a = 1/2 (N5).

  The cause of the miss and the rule now kept are in B1972's Seen first.
- **What is new here:**
  - the second computation of W-D2's D-1 rates on main's code;
  - the null frame that every mass state lies along, and the permutation it gives;
  - the cancellation of the Higgs's own ε^(1/2) rotations in V;
  - the census at orders 5, 8 and 10, with its exceptions located.
- **The literature:**
  - a mixing small because both sectors share one rotation is the textbook alignment mechanism of flavour models
    (aligned textures; for example, the "alignment" limit of two-Higgs-doublet models);
  - that the leading rotations cancel in V = U_u†U_d is standard perturbation theory.
  - No outside result computes frame C, so none is cited for the numbers.

## 1. N1 — W-D2's D-1 rates, computed again on main's code (`verification/rates.py`, `rates_run.txt`)

- **Setup.** Frame C with every sector reading S, through B1945's `parts`, unchanged. Points: the mark (2/5, 4/5)
  and the twin (1/5, 2/5). Heights 20 and 30. Rates in units of ε = e^(−π Im τ), as W-D2 gives them.

  | point | ∣V₁₂∣ | ∣V₂₃∣ | ∣V₁₃∣ | ∣J∣ | W-D2 |
  |---|---|---|---|---|---|
  | the mark | 0.600 | 0.300 | 1.100 | 2.000 | 3/5, 3/10, 11/10, 2 |
  | the twin | 0.900 | 0.100 | 1.000 | 2.200 | 9/10, 1/10, 1, 11/5 |

- **Every entry agrees with W-D2's table.** W-D2 computed the twin's J on one interval only, and this computation
  uses the same interval, 20 to 30.
- **The mass rates are B1945's S cells, doubled to ε units.**
  - The mark: up (3/5, 1), down (2/5, 11/10).
  - The twin: up (1/5, 6/5), down (2/5, 11/10).
- **This is a second computation.** It shares the frame's code with B1945, and nothing with W-D2's own assembly.

## 2. N2 — the exact identities (`verification/identities.py`, `identities_run.txt`)

- **I1.** Y h = (h·h)u and hᵀY = (h·h)uᵀ, for every h, u and w (B1966's E1).
- **I2.** Frame C's up sector has no '1' channel, so w = 0 there. Then:
  - Y u = (u·u)h;
  - Y (u×h) = −(u·h)(u×h).

  For w ≠ 0 the first becomes Y u = (u·u)h + w(h×u).
- **I3.** With w = 0, Y acts on span(h, u) as h → (h·h)u and u → (u·u)h. Its eigenvalues there are
  ±√((h·h)(u·u)), and det Y = (u·h)(h·h)(u·u), which is B1969's law at w = 0.
  - *A sign error in this arc's first statement of I3 (−(u·h)(h·h)(u·u)) was caught by its own check before
    landing.*
- **I4.** The null basis n = (1, 0, i)/√2, n̄ = conj(n), e = (0, 1, 0) is unitary, with n·n = n̄·n̄ = 0, n·n̄ = 1
  and e·e = 1. Here · is the bilinear product of the closed form.

So in the up sector:
- **the heavy state is u×h,** with eigenvalue −(u·h);
- **the light pair lives in the plane of h and u,** where the coupling acts only through the two nullities h·h and
  u·u.

## 3. N3 — the frame's vectors in the null basis (`verification/invariants.py`, `verification/nullbasis.py`, their runs)

- **The closed form is the frame.** The channels (u, w) come from the channel matrix by B1968's conversion, and h is
  solved from the closed form. The frame's coupling then equals Y(h, u, w) to a relative residual of 1e-71 at height
  20 and 1e-91 at height 30, in both sectors at both points.
- **B1739's identity holds in frame C:** h·h / (η⁶/4) = 1 at every height computed. So h·h falls at rate 1/2 while
  |h|² grows at rate 1/2, and the Higgs's nullity falls at rate 1 at every point. The Higgs triplet does not depend
  on the point.
- **Coordinates, relative to each vector's size:**

  | vector | along n | along n̄ | along e | its nullity's rate |
  |---|---|---|---|---|
  | h (every point) | 1 | 0 (dominant) | 1/2 | 1 |
  | u_up, the mark | 0 (dominant) | 3/5 | 3/10 | 3/5 |
  | u_up, the twin | 1/5 | 0 (dominant) | 1/10 | 1/5 |
  | u_down, both points | 1/10 | 3/10 | 0 (dominant), with w of the same size | 2/5 (u·u + w²) |

- **The mass states.** Every left singular vector at both points lies along n, n̄ or e. Its other coordinates fall at
  the rates printed in `nullbasis_run.txt`.

  | sector, point | light | middle | heavy |
  |---|---|---|---|
  | up and down, the mark | n | n̄ | e |
  | up and down, the twin | n | e | n̄ |

- **How the up sector reads by I2.**
  - At the mark, u lies along the Higgs's conjugate null direction. So u×h lies along e, and the heavy state is e.
  - At the twin, u lies along the Higgs's own null direction, so h and u nearly coincide and the heavy state is the
    Higgs's own direction n̄.
- **The down sector,** whose w ≈ ±i u_e, takes the same assignment as the up sector at both points.

## 4. N4 — the cancellation (`nullbasis_run.txt`; the arithmetic below)

- **The naive estimate.** Each entry V_ij = Σ_k conj(U^u_ki) U^d_kj is a sum of three terms. Its naive rate is the
  least, over the coordinates k, of the sum of the two coordinates' rates.
- **The naive estimate holds for some entries:**
  - the mark: V₁₂, 0.6, and V₂₃, 0.3;
  - the twin: V₂₃, 0.1.
- **It fails for every entry whose naive leading term runs through a coordinate of rate 1/2:**

  | entry | naive rate (through a coordinate of rate 1/2) | computed rate |
  |---|---|---|
  | the mark, V₁₃ | 0.5 | 1.1 |
  | the mark, V₃₁ | 0.5 | 0.9 |
  | the twin, V₁₂ | 0.5 | 0.9 |
  | the twin, V₁₃ | 0.6 | 1.0 |
  | the twin, V₃₁ | 0.6 | 1.2 |

- **Why these terms are the Higgs's.** Among the inputs, rate 1/2 occurs only in the Higgs, as its e coordinate. The
  channels' coordinates fall at 1/10, 1/5, 3/10 and 3/5.
- **So the rotations the shared Higgs induces are the same in both sectors and cancel in U_u†U_d,** and every
  surviving entry is set by the channels.
- **At the twin, the two sectors' coordinate rates are identical in every cell.** The whole leading rotation is
  common, and only V₂₃ survives at the naive rate 1/10.

## 5. N5 — the census (`verification/bits.py`; `bits_run_30_5.txt`, `bits_run_30_8_10.txt`)

- **Setup.** At height 30 and column 0.13, every point of order 5, 8 and 10 (orders 8 and 10: the points whose
  largest denominator is the order). For each point: the dominant null-basis direction of every mass state, and the
  mixing's least diagonal |V|.
- **Order 5:**
  - all 24 points are aligned;
  - every state is clean (dominant coordinate at least 0.99);
  - the two sectors' assignments agree at every point.

  | how many points | the up channel | the down channel | the assignment, both sectors |
  |---|---|---|---|
  | 10 | along n | along e, w/u_e = +i | (n, n̄, e) |
  | 10 | along n̄ | along e, w/u_e = −i | (n, e, n̄) |
  | 4 | along n̄ | along n̄ | (n, e, n̄) |

  So at order 5 the up channel's null direction and the down channel's sign of w/u_e are locked together.
- **Orders 8 and 10: 112 points, 104 aligned.**
  - The assignments agree at 110 points.
  - The mixing is aligned at no point where they disagree.
  - **All 8 unaligned points lie on the line a = 1/2,** and every point of that line in the census is unaligned:
    order 8, b = 1/8, 3/8, 5/8, 7/8, least diagonal 0.608; order 10, b = 1/10, 3/10, 7/10, 9/10, least diagonal
    0.737 to 0.875.
  - On that line both sectors' channels lie along e. The light pair is not along n or n̄: its dominant coordinate is
    0.74 to 0.94. It lies in their plane at an orientation the leading order does not fix, and that orientation
    differs between the sectors.
  - So the 1-2 block mixes at order one while the heavy state stays aligned.
- **Every state is clean at 96 of the 112 points.** The other 16 are the 8 points on a = 1/2 and the 8 points of order
  8 at a = 1/4 and 3/4. At the latter the light pair is a mixture with dominant coordinate 0.816, the same in both
  sectors, and the mixing is aligned.
- **Exact counts** are in the runs' SUMMARY lines.

## What it means

- **The record's two-doublet mixing is small for a structural reason.**
  - The Higgs is shared and nearly null, so it rotates both sectors the same way.
  - The mixing sees only what the channels add, at the channels' own rates.
  - This is the "too small" of B1742 and W-D2, explained. It is not cured.
- **The wall read as a specification.** An aligned mixing of the right size needs a relative rotation between the up
  and down frames that is larger than the channels' differences.
  - Frame C has only the channels' differences (this arc).
  - Frame D1's opposite twists derange the mixing (B1962).
  - So a principled structure must give a rotation between these two, and none on record does.
- **The line a = 1/2 is the one place where the 1-2 mixing is order one with the heavy state aligned.**
  - Its orientation is set beyond leading order, and is not computed here.
  - It is not on the act's line, which is of order 5 (B1943).
  - Nothing here reads that against any measured number.
- **For the input ledger:**
  - nothing changes;
  - the all-S reading's standing is B1970's, given H1 to H3, found after the look;
  - the mixing's size remains open under P-860 (d).

## What is open

- **The closed form of the census:** which points' up and down assignments agree, as a congruence on the point's
  characteristics with the sector charges, derived from the theta constants' leading phases. At order 5 the two bits
  are locked; why they are is not derived here.
- **The rates of every |V| entry in closed form** from the null-frame coordinates, including the cancelled entries'
  surviving terms.
- **The orientation of the light pair on the line a = 1/2,** beyond leading order.
- **The census at other heights and columns.** B1963 reports twelve unaligned points of orders 8 and 10 on its grid,
  and this census finds eight at one height and column.
