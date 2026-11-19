# W-D2: on the act's line in frame C, the shared doublet mode aligns the cusp mixing at both points, every height and every column computed. Every |V_ij| and J then falls at a rate identified numerically as a rational multiple of π Im τ. The leptons stay tied to the down quarks, and the record calls choosing (S, S) after the look post hoc. The sector-odd singlet aligns the mixing only where the hierarchy is gone. A singlet carried with the same sign by the down quarks and the leptons splits their first generation, never their second, and only in a window of its size where the mixing is not aligned

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free. Nothing is compared, and no target
is opened. It was written at the author's word of 2026-11-19: both of the seat's options, the cheaper one first. W-D1
was the cheaper option, and this is the second. This version applies its referee read's corrections; the first version
was 08d3d5998.

**The record of the run.**
- **The card:** `relays/cards/CHAT1_W-D2_two_structures_for_the_cusp_mixing.md`, b8b1387ae (22:43:01).
- **The script:** `relays/chat1_2026-11-19_wd2/wd2_run.py`, 61b7fa898 (22:45:12), SHA-256 beginning 5ff950fe. It
  ran in 92 s.
- **The outputs:** `wd2_run_out.txt` and `wd2_output.json`, committed as produced at f483a7cc5. A snapshot of the
  output files taken mid-run is at 530cf354e.
- **The post hoc read-out:** `wd2_posthoc.py`, labelled, committed at 6cbf55ebb before its run. Its output, which reads
  the json only, is at 799dcb050.

**Disclosed: the smoke test.** The script's two task functions were run once as a smoke test at height 4, which is not
one of the card's heights. That was after the card's commit and before the script's. The script was not changed after
the test, and its printed classes are not used.

**Typing.** [E] means established on record, by the run or by the referee's independent recomputation. [J] means this
seat's judgement.

**The referee's recomputation.** The referee's read wrote its own per-point assembly: its own theta sums, η, coupling
and SVD, importing only the norms and the tables. It reproduced every stored number to 11.3 digits or better, and every
class in 1 760 cells of D-2 and in 12 controls.

## 0. In short

1. **[E] D-1, the shared doublet mode.** Two doublets of opposite hypercharge share one fibre triplet, so every sector
   reads S.
   - On the act's line, at the mark and the twin, the cusp mixing is aligned at heights 6 to 30, in all three columns.
   - Every off-diagonal |V_ij| and J falls at a rate that is identified numerically, not derived, as a rational
     multiple of π Im τ (§ 2).
   - The leptons stay tied to the down quarks.
   - The referee's control: (S̃, S̃, S̃) is also aligned at these two points. So on the act's line the global reading
     bit is not where the alignment comes from.
2. **[E] D-2, the sector-odd singlet.** In the two worlds the charge rule allows, a singlet aligns the cusp mixing only
   at κ = 10^(1/2).
   - That happens at four phases, in one world per point. The heavy-pair ratio there is 0.420.
   - No cell is aligned with heavy-pair ratios of at most 1e-2 (X5).
   - [J] This is B1740's dichotomy, on this grid: a Higgs that is not null aligns the mixing and loses the hierarchy.
3. **[E] The split between leptons and down quarks.**
   - The relation: in frame C, Y_lep(R + s·1) = λ·Y_down(R − s·1)ᵀ exactly, with |λ| = 1 (§ 3).
   - So a singlet carried with the same sign by the down quarks and the leptons splits their first generation. With the
     hierarchy kept, |ln D₁| reaches 1.3 to 2.4.
   - It never splits their second generation: |ln D₂| ≤ 0.092 in every cell, and ≤ 0.014 with the hierarchy kept.
   - The split appears only in a window of the singlet's size about one decade wide, and the window moves with the
     height.
   - Every cell in the window is partial or deranged: its least diagonal entry is at most 0.151.
   - No cell has both the alignment and the split.
   - A singlet odd between the down quarks and the leptons gives D = 1 exactly.
4. **[J] What it means.**
   - On the act's line the mixing wall is the single doublet's conjugation. But the record has ruled that choosing
     (S, S) after the look is a post hoc selection (B1946; P-861, DONE). P-847's note of 2026-11-15 requires both
     same-reading options to be declared and sealed.
   - A second doublet frees the up sector's reading again, and "one fibre mode" sets it to the aligning value. That is a
     counted choice, made with the result known.
   - No structure computed here gives the split between leptons and down quarks together with the alignment and the
     hierarchy.

## 1. The expectations, as sealed

| cell | prediction | outcome |
|---|---|---|
| C1 | At κ = 0, W₋ and W₊ are deranged at both points and every D-2 height | **failed as worded.** Eleven of twelve cells are deranged. The twin at height 10 in W₊ is partial: its \|V\| is a cyclic permutation, but one diagonal entry is 0.103, above the card's 0.1 (post hoc P1) |
| C2 | Without the singlet, the leptons equal the down quarks (\|ln D\| ≤ 1e-20) in both readings | holds |
| C3 | (S, S) at x = 0.13 is aligned at heights 6 and 30, as in B1946 | holds |
| C4 | The repeats at 20 more digits change no class, and no \|V\| entry by more than 1e-15 | holds. The script compared 12-digit strings, which cannot see 1e-15. The referee's repeat at full precision finds a largest change of 5.9e-76 |
| X1 | D-1 is aligned at every height of 6 or more, at both points and every column | holds. The least diagonal entry is 0.9933, at the twin at height 6 |
| X2 | Under D-1 every off-diagonal \|V_ij\| falls between heights 20 and 30 at a local rate above 0.1 | **failed as worded.** Every entry falls, but the twin's \|V₂₃\| falls at 0.09999989, just below the threshold, in every column |
| X3 | Under D-1 the leptons stay tied | holds. The bound 1.3e-36 is the working precision's floor on an exact identity; the referee finds ≤ 7.7e-51 at more digits |
| X4 | Under D-2, every φ with κ ≥ 3 aligns, in both worlds and both parities | **failed.** At κ = 10^(1/2) only the odd phases 0 and π and the even phases π/2 and 3π/2 align, in W₋ at the mark and W₊ at the twin. In the other world the best least diagonal is 0.78 to 0.81. At κ = 10 nothing aligns (least diagonal ≤ 0.88, heavy-pair ratio 0.754). The reason the card gave fails: a Higgs dominated by the singlet does not align the two sectors, because their channels differ (B1945 § 3b) |
| X5 | Under D-2, no cell is aligned with heavy-pair ratios of at most 1e-2 | holds. Every aligned cell has a heavy-pair ratio of 0.420 |
| X6 | The odd singlet splits the leptons from the down quarks somewhere, and the even singlet nowhere | **failed, and impossible as worded.** In both of the card's parities the down quarks and the leptons carry the same sign, and the phase grid is closed under φ → φ + π. So the even singlet's values are the odd singlet's, permuted. The prior should have been 0, and the failure says nothing about frame C |

## 2. D-1: the shared doublet mode

- **The rates** are in units of ε = e^(−π Im τ), between consecutive heights from 6 to 30.
  - Between heights 20 and 30 the three columns agree to 1.3e-5.
  - The rates match the rationals below to 1e-7, except the twin's J, which matches to 4e-5 on that single interval.

| point | \|V₁₂\| | \|V₂₃\| | \|V₁₃\| | \|J\| |
|---|---|---|---|---|
| the mark, (2/5, 4/5) | 3/5 (0.5999 to 0.6000 from height 6) | 3/10 (0.3000 from height 14) | 11/10 (1.1000 from height 14) | 2 (2.0000 from height 14; from height 10 at x = 0) |
| the twin, (1/5, 2/5) | 9/10 (0.9000 from height 10) | 1/10 (0.1000 from height 14) | 1 (1.0000 from height 14) | 11/5 (2.2000 between heights 20 and 30 only) |

- **The pattern of the rates.** At the twin, 1 = 9/10 + 1/10, so |V₁₃| falls like |V₁₂||V₂₃|. At the mark, 11/10 is more
  than 3/5 + 3/10.
- **The mixing's rates and the masses' rates.** They lie on the same grid of tenths. They coincide only for |V₁₂| at
  the mark, whose 3/5 is the up m₂/m₃ rate, and |V₁₃| at the mark, whose 11/10 is the down m₁/m₃ rate.
- **J** is non-zero at every height and column, x = 0 included. At the twin it changes sign between heights 8 and 10,
  so its local rates there are not limits.
- **The masses** are B1945's (S, S) cells, in these units:
  - the mark: up (3/5, 1) and down (2/5, 11/10);
  - the twin: up (1/5, 6/5) and down (2/5, 11/10).
- **[E] The scope is the act's line.**
  - B1963 finds (S, S) itself unaligned at 12 points of orders 8 and 10.
  - B1964 says the heavy pair's alignment under (S, S) depends on each sector's channels.
  - The referee's control (S̃, S̃, S̃) is aligned at both points here, with least diagonal 0.976 at the twin at height 6.
    B1946 found (S̃, S̃) deranged at height 30 at other points of order 5.
- **[E] The record's standing of D-1.**
  - In every number of frame C, D-1 is the world (S, S, S).
  - B1946 says reading (S, S) is not the fix, and that choosing it after the look would be a post hoc selection. P-861
    (DONE) records the choice as post hoc.
  - P-847's note of 2026-11-15 requires both same-reading options to be declared and sealed, with the look counting
    them.
  - [J] The second doublet changes the typing, not the numbers. P-847's charge rule binds the relative reading only for
    one doublet. A second one frees the up sector's reading, and "one fibre mode" sets it to the aligning value, which
    is now known. So D-1 is a counted choice made after the look, and route (d)'s statements in this world (THE
    MAGNITUDE LEDGER § 4 (d); W-D1) would carry that in their look ledger.
- **[J] Two openings, neither computed.**
  - The shared mode exists because frame C's Higgs carries no line. In frame D1 the Higgs's twist scales with q_H, so
    two doublets of opposite charge carry opposite twists. Whether a shared mode exists there is open.
  - The usual reason for two doublets of opposite hypercharge with no conjugate is a holomorphic Yukawa coupling. P-847
    records holomorphy of the reading as an untested candidate that would select S.

## 3. D-2: the singlet

- **The relation between leptons and down quarks, derived.**
  - On the act's line the lepton sector's weighted matrix is λ times the down sector's transposed, with |λ| = 1
    (B1934 § 3). The referee checked this to 1e-110.
  - For every reading R of the triplet, εR is symmetric, and ε is antisymmetric.
  - The coupling Y_ab = Σ (C_aᵀ ε H C_b)_mn M_mn therefore gives Y_lep(R + s·1) = λ·Y_down(R − s·1)ᵀ. The referee
    checked this to 1e-80 at every cell it computed.
  - So the leptons' ratios at s are the down quarks' at −s, and |ln D| is even in s.
  - A singlet with the same sign on the down quarks and the leptons, as in both of the card's parities, can split them.
    One with opposite signs gives D = 1 exactly (the referee checked to 1e-93).
- **The best alignment any singlet reaches** (post hoc P2; the heavy-pair ratio is that of the best cell):

| point | world | best least diagonal, heights 10, 20, 30 | at κ | heavy-pair ratio |
|---|---|---|---|---|
| the mark | W₋ | 0.998, 0.998, 0.998 | 10^(1/2) | 0.420 |
| the mark | W₊ | 0.784, 0.781, 0.780 | 10^(1/2) | 0.642 |
| the twin | W₋ | 0.809, 0.782, 0.781 | 10^(1/2) | 0.642 |
| the twin | W₊ | 0.997, 0.998, 0.998 | 10^(1/2) | 0.420 |

- [J] 0.420 lies below B1968's floor of 0.457 for triplets at heights 1 to 10. A singlet lies outside B1968's search, so
  the two do not conflict.
- **The first generation's split, with the hierarchy kept** (post hoc P3). The table gives the largest |ln D₁| over cells
  whose heavy-pair ratios are both at most 1e-2, and the κ = 10^(k/2) where it falls. Every such cell is partial or
  deranged.

| point | world | height 10 | height 20 | height 30 |
|---|---|---|---|---|
| the mark | W₋ | 1.7 at k = −2 | 2.2 at k = −5 | 1.6 at k = −8 |
| the mark | W₊ | 1.6 at k = −8 | 2.0 at k = −16 | 2.0 at k = −24 |
| the twin | W₋ | 1.5 at k = −2 | 1.4 at k = −4 | 2.0 at k = −7 |
| the twin | W₊ | 2.4 at k = −7 | 1.6 at k = −15 | 1.3 at k = −24 |

- **The second generation** is not split: |ln D₂| ≤ 0.014 wherever the hierarchy is kept, and ≤ 6e-4 at heights 20 and
  30.
- **On the small-κ side of the window** the split falls by about √10 per half-decade. On the large-κ side in W₋ the
  hierarchy is lost. In W₊ at heights 20 and 30 the split falls to a minimum, then rises again by about √10 per
  half-decade. At height 10 its fall stalls.
- **How the window moves.** It moves by 2 to 3 half-decades per 10 units of height in W₋, and by 8 to 9 in W₊.
  - On the three heights the motion is linear on the log scale. Relative to |c_max|, the window's κ follows about ε^0.10
    in W₋ and ε^0.30 in W₊, ±0.02 at the grid's resolution. That is the referee's numerical observation, not derived.
  - [J] So a singlet whose size carries its own cusp exponent would stay in the window at every height. The datum the
    split needs may then be a discrete exponent, not a continuous number.
  - Either way, the window lies where the mixing is not aligned.

## 4. What it means

- **[J] The mixing.**
  - On the act's line, frame C's cusp mixing fails only through the single doublet's conjugation. Two doublets with one
    fibre mode align it, with rates identified numerically on a grid of tenths and a J that is not zero.
  - The record has ruled that choosing (S, S) after the look is post hoc (B1946; P-861). The second doublet changes the
    typing, not that standing.
  - Whether the object supplies two doublets with one fibre mode is open. FK15 is OPEN, and its banked half is that the
    Higgs's "which" is not forced. The Higgs's type is CHOSEN in the paper's Table 1.
- **[J] The sector-odd singlet** is not a route to the mixing. It aligns only at one size, κ = 10^(1/2), and there the
  hierarchy is gone.
- **[J] The leptons.**
  - A singlet splits the first generation of the leptons from that of the down quarks, never the second.
  - It does so only in a window of its size where the mixing is not aligned.
  - So no structure computed here gives the split P-862 asks for together with an aligned, hierarchical mixing.
- **[J] What the record lacks** is the two structures together: the shared doublet mode with a singlet carried with the
  same sign by the down quarks and the leptons. Two questions remain:
  - whether the window's first-generation split survives where (S, S, S) keeps the alignment and the hierarchy;
  - whether anything splits the second generation.

  This page does not compute them.

## 5. What this page does not do, and its limits

- It compares nothing and opens no target.
- It does not derive the rationals, and it says nothing about what in the object would give two doublets or a singlet.
- **Its limits:**
  - D-2 ran at one column, x = 0.13.
  - Only the two points of order 5 on the act's line were computed: no a = 0 point, and none of B1963's exceptional
    orders.
  - The heights go up to 30 only.
  - The twin's 11/5 for J rests on one interval.
  - The grid in κ is half-decades and the phases are multiples of π/4. A window narrower than the grid would be missed.
  - The json stores |ln D| as an absolute value and no lepton ratios, and the printed output lists the aligned cells
    only by count. The json holds every cell.

0 of 19.
