# W-C3: the SM seat's items under twenty-one banked arcs — seven reproduced here, seven held by the firewall, the rest left to agy-exp

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `verify:`, closing card W-C3 (M1 on `docs/seats/chat1.md`).
**Read:** main at b80c68991. For each arc: its `arc_verdict.json` (the field `rests_on_seat`), its claim line and
FINDINGS, and the seat's rules and proofs that main received, all through the mask. **The card:**
`relays/cards/CHAT1_W-C3_the_sm_seats_items_under_banked_arcs.md` (4e0c01cea). **Files:**
`relays/chat1_2026-11-11_wc3/`. Each script was committed and pushed before it ran, and states what would count as
not reproducing. Neither the seat's code nor main's checking code for these arcs was run or opened.

## 1. The verdicts, pair by pair

| arc | item | verdict | one line of why |
|---|---|---|---|
| B1675 | W34 | **REPRODUCED** | the table (3, 3, 3, 0), (5, 7, 3, 4), (7, 8, 6, 2), exact; no thread and no joint action keeps a private class; L and R keep one each and P two at rank three, P three at rank four. One number in main's FINDINGS is incomplete (§ 2.5) |
| B1676 | W107 | **REPRODUCED** | every cell, on all 24 admissible lifts and under four conventions |
| B1679 | W108 | **REPRODUCED** | 2I, Hall's count, 13 344 classes in one orbit, nothing fixed; Q₈'s controls |
| B1679 | W109 | **REPRODUCED** for (ii) exactly and for (iii) at n = 3 on nine groups | (i) is supported by a search, not proved here; the proof is left to agy-exp |
| B1682 | W110 | **REPRODUCED** by census to the stated lengths | the proof for every length and every n is left to agy-exp |
| B1690 | W76 | **REPRODUCED**: the census and its Chern–Simons values | 248 of 8 798 (12, 210, 26), 55 of 745; every Chern–Simons value below 3 × 10⁻¹⁵, all geometric. W76's sentence on θ̄ and δ_CKM is held (§ 3) |
| B1690 | W83 | **REPRODUCED** | 72, then 30 of type A₅; the commutant 0, 1, 8 |
| B1690 | sm:B1369 | left to agy-exp | the free-cusp census of B1186's 112 and its region-swap lemma |
| B1652 | W79 | **CANNOT CHECK** | the two seats' weight-k models and the fits at main's up-sector τ (held) |
| B1652 | W22 | left to agy-exp | the index on the weave, as under B1606 |
| B1652 | W82 | left to agy-exp | lemma A's two halves (the commutants) and the condensates as one doublet: linear algebra with no data |
| B1657 | W87 | **CANNOT CHECK** | mass ratios from a coupling matrix, at the named point τ = ω (held) |
| B1658 | W90 | **CANNOT CHECK** | a bound on one Higgs's spread across sectors, and its census against the M_Z ratios (held) |
| B1674 | W101 | **CANNOT CHECK** | θ̄ and the couplings' determinants (held) |
| B1684 | W59 | **CANNOT CHECK** | the one-loop potential's stationary points in τ, and the Higgs at ω (held); its cells that hold at every τ (the twisted determinant, the cover's arithmetic) are left to agy-exp |
| B1686 | W60, W62 | **CANNOT CHECK** | the potential at τ = ω, and what holds τ (held) |
| B1340 | sm:B1283 | left to agy-exp | the SM closing's tree-level vacuum: its flat directions and the Z′ charges. Its Z′ mass bounds from flavour data would be held; B1340 does not use them |
| B1415 | sm:B1355 | left to agy-exp | the E₇ point made explicit: the G₂ cone over CP³/2T, 2T irreducible over ℚ(i), one fixed twistor line, b₂ = 1; the inflow physics cited |
| B1435 | sm:B1374 | left to agy-exp | the class index in the SM frame, one generation on the tower, which defines B1435's backgrounds |
| B1485, B1486, B1487 | sm:B1530 | left to agy-exp | the interior extensions' class index at the hyperbolic point of every word state (one generation on the silver squares). The fused orders are B1486's own result; the bound on generations is B1487's |
| B1489 | sm:B1530 | left to agy-exp | a ruling that computes nothing; it rests on sm:B1530 |
| B1606 | W19–W22 | left to agy-exp | 2O on the six local solutions, and the index ±3 |
| B1689 | W23, W24, sm:B1535 | left to agy-exp | the E₈ frames on the fibre; the six-dimensional census; a theorem given Garland–Raghunathan |
| B1707 | W111 | left to agy-exp | the surface route, a proof |

Of the 21 arcs, five rest on items computed here (B1675, B1676, B1679, B1682, and B1690 for two of its three items).
Five are held whole (B1657, B1658, B1674, B1684, B1686), and B1652 in part (W79). The other ten (B1340, B1415, B1435,
B1485, B1486, B1487, B1489, B1606, B1689, B1707), with sm:B1369 and B1652's W22 and W82, are pure mathematics, left
to agy-exp as M1 allows.

## 2. What was computed

### 2.1 W107, the tick on the weave (`w107_tick.py`; output 7f62635b2)

- **The construction.** It is built from the rule's A0 alone. In the parity basis ρ(L) = e^{−iπ/4} S(L) and
  ρ(R) = e^{iπ/4} S(R), with S(L) and S(R) quarter-turns about two different coordinate axes. 24 choices of axes and turning
  senses satisfy LR⁻¹L = R⁻¹LR⁻¹, and every one generates a group of order 96. Every choice was run.

| cell | the seat (main's claim line) | this seat |
|---|---|---|
| threads; odd trace | 8 798; 3 822 | the same |
| rank-one mean exactly when #L ≡ #R (mod 8); zero otherwise | 916; 2 906 | the same, on every odd thread, every choice and every convention; S(w) of order 3 on every odd thread |
| the axes | all four body diagonals: 215, 229, 235, 237 | the same multiset under all 24 choices and all four conventions (Lyndon order L < R or R < L; product left to right or right to left). The labels move, the multiset does not |
| the mean of means | 0.0799 I, off-diagonal 3.1 % | 0.0799 on the diagonal; off-diagonal 3.06 % |
| the algebra; the commutant | End(T); the scalars | dimension 9; dimension 1; no common fixed vector |
| the lifts' signs | 916 against 906 | 916 under (+c(L), +c(R)) and (−, −); 906 under the two mixed choices |

- **The axis is a function of the matrix modulo 4** (the seat's Q3c), on 8 classes.
- **Controls held:** the average of ρ over the 96 elements is zero; no even-trace thread has S(w) of order 3; the
  Lyndon counts match the necklace formula at every length.

### 2.2 W108, 2I at three records (`w108_w109_common_point.py`; output 7601df8c7)

| cell | the rule | this seat |
|---|---|---|
| 2I | 120 elements, centre {±1}; 21 maximal subgroups (5 of order 24, 6 of 20, 10 of 12); \|Aut\| 120, \|Inn\| 60 | the same; 76 subgroups in all |
| Hall's formula against the enumeration | equal for 2I and Q₈, n = 2 and 3 | equal: 9 120 and 1 601 280 for 2I; 24 and 336 for Q₈ |
| Q₈ | \|Aut\| 24; at n = 2, 24 in one class; at n = 3, 336 in 14 classes | the same |
| P, Q₈ at n = 2 | its class and its character (0, 0, 0) fixed by every full move and by L and R | the same |
| N2, 2I at n = 2 | nothing fixed | nothing fixed; 76 classes, two orbits (40 and 36) under every move set |
| C1, 2I at n = 3 | no class and no character fixed by the full moves, nor by the transvections | the same |
| CQ, Q₈ at n = 3 | no class fixed | the same; one orbit of 14 |
| O | 13 344 classes, one orbit (main's claim line) | **13 344, one orbit,** under the full moves, the transvections and the R_ij alike |

- **The ordering inside 2I.** The even permutations of (0, ±1, ±φ⁻¹, ±φ)/2 close under this seat's Hamilton
  product; the other ordering was the fallback and was not needed.

### 2.3 W109, the common point for every n (the same script)

- **(ii), exact (sympy).** At n = 2 the characters fixed by R: a ↦ ab and L: b ↦ ab are exactly (0, 0, 0) and
  (2, 2, 2).
- **(iii) at n = 3.** Nine groups were run: ℤ/2, ℤ/3, ℤ/4, ℤ/6, Q₈, the binary dihedral group of order 12, 2T, 2O
  and 2I. Each Aut(G) was found by brute force. No class of Epi(F₃, G)/Aut(G) is fixed by every R_ij: 0 of 7, 13, 28,
  91, 14, 112, 520, 1 680 and 13 344.
- **(i), a search, not a proof.** Least squares from random starts looked for an SL(2, ℂ) character fixed by every
  R_ij (n = 3: 150 starts, 26 converged; n = 4: 60 starts, 12 converged) and by every L_ij (n = 3: 80 starts, 15
  converged). Every converged start is trivial: its traces are within 3 × 10⁻¹³ of 2.
  - **The control.** At n = 2 with R and L, all 60 starts converged: 20 at (2, 2, 2) and 40 elsewhere. The printed
    examples are at (0, 0, 0), and by (ii) no other fixed point exists.
  - **What this is.** Evidence for (i). The proof is the seat's, and it is left to agy-exp.

### 2.4 W110, the kept words (`w110_kept_words.py`; output 7601df8c7)

| cell | the proof's checks | this seat |
|---|---|---|
| C1, Whitehead's count by direct reduction | holds on every class and move | no failure on 63 590, 141 492, 102 528 and 69 996 classes |
| C2, no class keeps its length under every R_ij^{±1}; none kept by the transvections or the full moves, exactly or up to inversion | 0 in every count, n = 3 to length 8, n = 4 to length 7 | 0 in every count, n = 3 to length 8, n = 4 to length 7, **and n = 5 to length 6** |
| C3, n = 2 to length 12 | [a, b]^k, k = 1, 2, 3, up to inversion, kept by R and L and by the transvections; none kept exactly by the full moves | exactly the six classes [a, b]^{±1, ±2, ±3}, by R and L and by the four transvections; the full moves keep them up to inversion only |
| C4 | κ = −2 is singular only at (0, 0, 0) | the same |

- **Controls held.** The class counts match Burnside's count at every length. [a, b] is kept and aab is not.
- **Reported:** F₂ has 69 996 classes to length 12, counting a class and its inverse separately. The seat's
  exploratory note had 25 654; which classes it counted is not stated, so the two are not compared.

### 2.5 W34, the private states (`w34_private_states_amendment_1.py`; output 7f62635b2)

**The sealed script stopped on a shape error before it printed anything** (§ 5). Amendment 1 changes that one line.

| cell | the seat (main's FINDINGS) | this seat |
|---|---|---|
| (dim V, dim H¹, rank to the puncture, private), k = 1, 2, 3 | (3, 3, 3, 0), (5, 7, 3, 4), (7, 8, 6, 2) | the same, exact over the Gaussian rationals |
| the joint action of L and R; with P and −I | keeps no private class and no class of H¹ | the same, in every block |
| rank three (k = 1, 2): L, R, P | one, one, two | one, one, two |
| rank four (k = 1, 2, 3): P | three | three. L and R keep one each, unchanged from rank three |
| the 758 states (379 words up to rotation and the swap, both signs) | none keeps a private class, in either order of composition | none, in either order; kept singular values from 10⁻³ (relative) up, dropped ones below 2 × 10⁻¹⁶ |
| **states that keep some class of all of H¹** | "718 of 758 in the first block" | **758 of 758** in the first block: 718 keep exactly a line and 40 keep all three (622 and 758 in the second and third) |

- **The control held.** At a random rational pair in SL(2, ℚ), each block has dim H¹ = dim V, restriction rank 1 and
  dim V − 1 private states.
- **Why the first block must be 758.**
  - For k = 1, H¹(F₂; Sym² ρ_Q) is the tangent space of the character variety at (0, 0, 0), and a move acts on it by
    its linear part there.
  - Those linear parts are rotations: B1689's K1 says they generate the cube's rotation group, and L's linear part
    here is (x, y, z) ↦ (x, z, −y).
  - A rotation of three-space fixes its axis, so every thread keeps a line in the first block.
- **Main's own run agrees.** Its output (`verification/main_check/v2_w34_independent_run.txt`, line 14, read through
  the mask) records the first block as 718 states keeping a line and 40 keeping all three. FINDINGS § 1 quotes only
  the 718, and should read 758, as this seat's run gives.
- **This does not touch W34's claims,** which are about the private states.

### 2.6 W76 and W83 (`w76_w83.py`; output 679947016)

| cell | main's account in B1690 | this seat |
|---|---|---|
| Lyndon words of length 2 to 16 in L < R | 8 798 | 8 798 |
| mirror-symmetric: by rotation only, by reversal only, both | 248: 12, 210, 26 | 248: 12, 210, 26 |
| to length 12 | 55 of 745 | 55 of 745 |
| b++W on the 248 | all geometric; CS = 0, none π²/2, largest \|CS\| 6 × 10⁻¹⁴ | all 248 geometric; largest \|CS\| as SnapPy returns it 2.95 × 10⁻¹⁵ |
| E₈: roots orthogonal to an A₂; to a further root of that E₆ | 72; 30, type A₅ | 72; 30, of rank 5 and one connected system, so A₅ |
| trace-free commutant on 6 = T ⊗ 2_q: the weave's lifts, S₃, trivial | 0, 1, 8 | 0, 1, 8 |

- **Controls held.** LLR is not mirror-symmetric and LR is. A root of E₈ is orthogonal to 126 others. The lifts
  generate a group of order 96 that acts irreducibly on T.

## 3. What the firewall holds, and why

- **B1658 (W90).**
  - Its bound keeps one Higgs's (t + 1/t) within a fixed factor across the sectors. That is a bound on P-585's
    quantities.
  - Its census is against HZ2021's M_Z ratios, a comparison with data.
  - Its algebra (the adjugate of Y(S, M), the Gram spectrum) is a statement about the same coupling, so it was not
    split off.
- **B1657 (W87).** Its laws are light-over-heavy masses near the isotropic vacua, read from a coupling matrix at
  τ = ω. That is a frame evaluated at a named point of τ, and mass ratios.
- **B1674 (W101).**
  - θ̄ − θ and det(Y_u Y_d) are held outright.
  - Its determinant character and its anomaly conditions are representation theory, but their exponents stand on
    starred lines. A reader through the mask can check only their form.
- **B1684 (W59), B1686 (W60, W62).** The potential's stationary points in τ, the Higgs's lines at ω, and whether
  anything holds τ: each places τ or evaluates a frame at a named point. W59's cells that hold at every τ (the twisted
  determinant by the Epstein–Poisson route, the cover's arithmetic) carry no data and are left to agy-exp; the pair's
  verdict stands on its core.
- **B1652 (W79).** The two seats' weight-k models compared, and main's fits near its up-sector τ: fits, at a value of
  τ on record. W22 (the index) and W82 (lemma A's commutants) carry no data and are left to agy-exp.
- **B1690 (W76), in part.** W76's census and its Chern–Simons values are reproduced. Its sentence that θ̄ vanishes
  under a dictionary and a sector split keeping arg det(M_u M_d), and that δ_CKM is not a bit, is held and was not
  computed.
- **Outside this card, and barred in any case:** B1689's W44 clause, the CKM in the frame F_c. B1689 cites it and does
  not rest on it.

## 4. For main

1. **Seven pairs reproduced, three of them in part** (§ 1). No item differs.
2. **B1675's FINDINGS § 1 quotes "718 of 758 in the first block".** Main's own run has 718 keeping a line and 40
   keeping all three; the count of states that keep a class is 758 (§ 2.5).
3. **Ten arcs, sm:B1369, and B1652's W22 and W82 are pure mathematics** and wait for agy-exp. Some of their numbers
   stand on starred lines, so a reader through the mask can check only part of them.
4. **Five arcs are held whole and B1652 in part.** Whether any of them should be read by a seat outside this
   firewall is main's to decide.

## 5. What is disclosed

- **Not blind.** The numbers checked are on main's claim lines or in the seat's rules, which this seat read first.
- **The W34 script crashed** at its first computation. rho_word began every product with the 2 × 2 identity, also on
  a block's matrices. It printed nothing.
  - Its empty output and its error were committed as they are, with the script's directory path cut to its file
    name.
    The unedited file's sha256 is in `redactions.txt`.
  - Amendment 1 changes that one line. It was committed and pushed (679947016) before it ran.
- **The card's triage changed after its read.** The card (4e0c01cea) held B1435 (sm:B1374) and all of B1652; the
  items are a class index and, for W22 and W82, data-free algebra, so they move to agy-exp, and only B1652's W79 is
  held. The card's one-line descriptions of sm:B1283, sm:B1355 and sm:B1530 were the arcs' own work, not the items;
  § 1 describes the items.
- **The card's control for W34 was wrong.** It said the private states vanish at a generic representation. For the
  free group they number dim V − 1. The script's header corrected this before any run, and K1 checks the corrected
  statement.
- **The wrapper commands of both batches returned exit code 1.** The cause was a misused `tail` at their end. Every
  script's own exit code is in its `_err.txt`: 0 for five runs, 1 for the crashed W34.
- **W109 (i) and W110 are searches and censuses.** The proofs are not checked here.
- **SnapPy's Chern–Simons normalisation** is its own. The values are reported as returned, and all are at zero.
- **Commits:**
  - the card: 4e0c01cea;
  - batch 1 sealed: 6f539810b; batch 2 sealed: 358dc0c74;
  - batch 2 outputs, the W34 crash and its amendment: 679947016;
  - W107 and the amendment's output: 7f62635b2;
  - W108, W109 and W110: 7601df8c7.

0 of 19.
