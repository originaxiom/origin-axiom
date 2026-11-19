# W-D2: in frame C, the shared doublet mode aligns the cusp mixing at every point, height and column computed, and every |V_ij| and J then falls as a rational power of ε. It leaves the leptons tied to the down quarks. The sector-odd singlet aligns the mixing only where it rivals the triplet, and there the hierarchy is gone. Any singlet, odd or even, splits the leptons from the down quarks, but keeps the hierarchy only in a window of its size that moves with the height

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free. Nothing is compared, and no target is
opened. It was written at the author's word of 2026-11-19: both of the seat's options, the cheaper one first. W-D1 was
the cheaper option; this is the second.

**The record of the run:**
- the card: `relays/cards/CHAT1_W-D2_two_structures_for_the_cusp_mixing.md`, b8b1387ae;
- the script: `relays/chat1_2026-11-19_wd2/wd2_run.py`, 61b7fa898, SHA-256 beginning 5ff950fe. It ran in 92 s;
- the outputs: `wd2_run_out.txt` and `wd2_output.json`, committed as produced at f483a7cc5. A mid-run snapshot of the
  output files was committed at 530cf354e;
- the post hoc read-out: `wd2_posthoc.py`, labelled, committed at 6cbf55ebb before its run. Its output, which reads the
  json only, is at 799dcb050.

**Disclosed.** Before the sealed run, the script's two task functions were run once as a smoke test at height 4, which
is not one of the card's heights. Their printed classes are not used.

## 0. In short

1. **[E] The shared doublet mode (D-1).** It gives two doublets of opposite hypercharge one fibre triplet, so every
   sector reads S.
   - The cusp mixing is aligned at the mark and the twin, at heights 6 to 30, in all three columns.
   - Every off-diagonal |V_ij| and J falls as a rational power of ε = e^(−π Im τ). Each rate is the same in all three
     columns to 2e-4 between heights 20 and 30 (§ 2).
   - The leptons stay tied to the down quarks: |ln D| ≤ 1.3e-36.
2. **[E] The sector-odd singlet (D-2).** In the two worlds the charge rule allows, a singlet aligns the cusp mixing only
   at κ = 10^(1/2), where it is about as large as the triplet's leading component.
   - There the heavy-pair ratio is 0.42.
   - No cell is aligned with heavy-pair ratios of at most 1e-2 (X5 holds).
   - B1968's dichotomy between alignment and hierarchy holds for this structure.
3. **[E] Any singlet splits the leptons from the down quarks, odd or even alike.**
   - The two parities give identical lepton–down ratios once the phase is shifted by π (post hoc P4, exactly 0).
   - With the hierarchy kept (both heavy-pair ratios at most 1e-2), the split reaches |ln D| from 1.4 to 2.4.
   - That happens only in a window of the singlet's size about one decade wide, and the window moves with the height
     (post hoc P3).
4. **[J] What it means.**
   - In frame C the mixing wall is the single doublet's conjugation. Two doublets with one fibre mode remove it, and the
     mixing's exponents are then fixed rationals.
   - That is a counted choice, and it does not touch the leptons.
   - A singlet can split the leptons from the down quarks, but only at a tuned size that depends on the height. That is
     a new continuous datum, not a forced number.

## 1. The expectations, as sealed

| cell | prediction | outcome |
|---|---|---|
| C1 | At κ = 0, W₋ and W₊ are deranged at both points and every D-2 height | **failed as worded.** Eleven of twelve cells are deranged. The twin at height 10 in W₊ is partial: its \|V\| is a cyclic permutation, but one diagonal entry is 0.103, above the card's 0.1 (post hoc P1) |
| C2 | Without the singlet, the leptons equal the down quarks (\|ln D\| ≤ 1e-20) in both readings | holds |
| C3 | (S, S) at x = 0.13 is aligned at heights 6 and 30, as in B1946 | holds |
| C4 | The repeats at 20 more digits change no class, and no \|V\| entry by more than 1e-15 | holds. No \|V\| entry changes in its 12 stored digits |
| X1 | D-1 is aligned at every height of 6 or more, at both points and every column | holds. The least diagonal entry is 0.9933 (the twin, height 6) |
| X2 | Under D-1 every off-diagonal \|V_ij\| falls between heights 20 and 30 at a local rate above 0.1 | **failed as worded.** Every entry falls, but the twin's \|V₂₃\| falls at 0.1000, the threshold itself |
| X3 | Under D-1 the leptons stay tied | holds; at most 1.3e-36 |
| X4 | Under D-2, every φ with κ ≥ 3 aligns, in both worlds and both parities | **failed.** At κ = 10^(1/2), two of the eight phases align in each parity, and only in one world per point: W₋ at the mark, W₊ at the twin. At κ = 10 none aligns |
| X5 | Under D-2, no cell is aligned with heavy-pair ratios of at most 1e-2 | holds. The least heavy-pair ratio among aligned cells is 0.420 |
| X6 | The odd singlet splits the leptons from the down quarks somewhere, and the even singlet nowhere | **failed.** Both split, identically up to a phase shift of π |

## 2. D-1: the shared doublet mode

- **The mixing's rates** are in units of ε = e^(−π Im τ), between consecutive heights from 6 to 30. They are the same
  at x = 0, 0.13 and 1/4 to 2e-4 at the top heights.

| point | \|V₁₂\| | \|V₂₃\| | \|V₁₃\| | \|J\| |
|---|---|---|---|---|
| the mark, (2/5, 4/5) | 3/5 (0.6000 from height 6) | 3/10 (0.3000 from height 14) | 11/10 (1.1000 from height 14) | 2 (2.0000 from height 10) |
| the twin, (1/5, 2/5) | 9/10 (0.9000 from height 10) | 1/10 (0.1000 from height 14) | 1 (1.0000 from height 14) | 11/5 (2.2000 at heights 20 to 30) |

- **The rationals are identified numerically, not derived.** At the twin, 1 = 9/10 + 1/10, so |V₁₃| falls like
  |V₁₂||V₂₃|. At the mark, 11/10 exceeds 3/5 + 3/10.
- **J is non-zero at every height and column,** including x = 0. At the twin J changes sign between heights 8 and 10,
  so its local rates there are not limits.
- **The masses** are B1945's (S, S) cells in these units: at the mark, up (3/5, 1) and down (2/5, 11/10); at the twin,
  up (1/5, 6/5) and down (2/5, 11/10). The run's ratios fall at these rates between heights 6 and 30.
- [J] **What it adds to the record.**
  - B1946 and W-F26 found (S, S) aligned. Here the alignment holds at both points, six heights and three columns.
  - With one fibre mode for two doublets, the same exponents now carry the mixing as well as the masses.
  - So route (d)'s statements free of τ extend to |V| and J in this world. This page makes no comparison.

## 3. D-2: the sector-odd singlet

**The best alignment any singlet reaches** (post hoc P2). The heavy-pair ratio is that of the best cell.

| point | world | best least diagonal, heights 10, 20, 30 | at κ | heavy-pair ratio |
|---|---|---|---|---|
| the mark | W₋ | 0.998, 0.998, 0.998 | 10^(1/2) | 0.420 |
| the mark | W₊ | 0.784, 0.781, 0.781 | 10^(1/2) | 0.642 |
| the twin | W₋ | 0.809, 0.782, 0.781 | 10^(1/2) | 0.642 |
| the twin | W₊ | 0.997, 0.998, 0.998 | 10^(1/2) | 0.420 |

**The split between leptons and down quarks, with the hierarchy kept** (post hoc P3). The table gives the κ = 10^(k/2)
at which the largest |ln D| falls, among cells whose heavy-pair ratios are both at most 1e-2.

| point | world | height 10 | height 20 | height 30 |
|---|---|---|---|---|
| the mark | W₋ | 1.7 at k = −2 | 2.2 at k = −5 | 1.6 at k = −8 |
| the mark | W₊ | 1.6 at k = −8 | 2.0 at k = −16 | 2.0 at k = −24 |
| the twin | W₋ | 1.5 at k = −2 | 1.4 at k = −4 | 2.0 at k = −7 |
| the twin | W₊ | 2.4 at k = −7 | 1.6 at k = −15 | 1.3 at k = −24 |

- Away from that window, either the split falls by about a factor √10 for each half-decade, or the hierarchy is lost.
- The window moves by roughly 2 to 9 half-decades for every 10 units of height. So no fixed relative size of the
  singlet keeps the split at every height.
- [E] **The parity does not matter for the split** (P4). Under both parities the down quarks and the leptons carry the
  same sign of the singlet, so the even singlet at phase φ is the odd one at φ + π.
- [J] This fits the transposition identity P-566 records in B1656's frame: the leptons see the singlet with the
  opposite sign relative to the triplet. It is not derived here for frame C.

## 4. What it means

- [J] **The mixing.**
  - Frame C's cusp mixing fails only through the single doublet's conjugation. Give the up quarks their own doublet
    with the same fibre mode, and the mixing is aligned, with fixed rational exponents and a non-zero J.
  - The open question becomes the object's: does it supply two doublets with one fibre mode? FK15 has a Higgs "forced
    to exist, not forced which", and its type is CHOSEN (Table 1). On the present record this is a counted choice.
- [J] **The sector-odd singlet** is not a route to the mixing. It aligns only by competing with the triplet's leading
  term, and that removes the hierarchy.
- [J] **The leptons.**
  - A singlet does split them from the down quarks, and the split does not depend on its parity.
  - But it keeps the hierarchy only at a tuned size that depends on the height. That adds a continuous datum rather
    than fixing one.
  - The split needed (P-862) is not supplied by any forced number here.
- [J] **The next computation the record lacks** is the two together: the shared doublet mode with a singlet. Does the
  singlet split the leptons while the world (S, S, S) keeps both the alignment and the hierarchy, and in what window?
  This page does not compute it.

## 5. What this page does not do

- It compares nothing and opens no target.
- It does not derive the rationals, and it says nothing about what in the object would give two doublets or a singlet.
- The grid in κ is half-decades and the phases are multiples of π/4. A window narrower than the grid would be missed.

0 of 19.
