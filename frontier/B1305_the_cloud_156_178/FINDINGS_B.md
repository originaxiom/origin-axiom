# B1305 — SLICE B (the quantum-face line, memos 174–182 + the relay of 2026-09-08): the fresh-eyes register's Q1 has its chirality half closed by computation on two benches — the two ends of the colored Jones polynomial are swapped by the mirror, so their ratio is a mirror-odd invariant, 2-torsion on an amphichiral knot: R(4₁) = 1, R(3₁) = 1/(q;q)_∞ — B1227's theorem in a fourth value group; what is mirror-odd in Gukov–Manolescu's F_K is the CENTRE of the block's exponent range, not their constant c (the figure-eight's blocks are palindromic: c_low = −1/16, c_high = +1/16); the two mock-theta growth rates 1/7 and 1/5 reproduce to six figures with an own estimator; the sense census fails its negative control a second time for the same meta reason and stays NOT ADOPTED; the generation count on this face remains open

**Date:** 2026-09-08 (night) · **Seat:** cc (main) · **DESIGN_B sealed** `fa793cf2…` before any of main's computations · **Cloud pinned:** `792918b7`
(`oa-audit-seat/cloud-seat-792918b7`); seven of the relay's certificates re-run there (six RC=0; `park_52_blocks.py` RC=1, an untracked scratch
dependency — the seat's own stuck item) · **Status:** **VERIFIED** (the ends, both routes; the blocks' palindromy; the growth rates 1/7 and 1/5;
the seat's Ẑ assembly by re-run against ten published series) + **VERIFIED-DIFFERS on one framing** (what is mirror-odd) + **NOT ADOPTED as
pre-registered, second time** (the sense census) + **REGISTERED** (the fourth regime on the theorem row; GC-6's re-reading; the seat's stuck
item; Phase 3's inputs) · **Price:** unchanged · **Credit:** the cloud seat (memos 174–182, the relay; certificates named below).

## 0. What the seat said, first

| item | the seat's headline (verbatim) | here |
|---|---|---|
| relay §1 | "The Vol ≠ 0 analogue of the chirality reading is the pair of ends of the colored Jones polynomial … Amphichirality is exactly the degeneracy that makes a chirality-sensitive quantity invisible on this face." | **VERIFIED** by two independent formulas and sharpened: the ends' RATIO is the invariant, and it is 2-torsion on 4₁ (B1227's fourth regime) |
| relay §1 | "The chirality-odd invariant on this face is Gukov–Manolescu's constant c … c = +1/24 for the right trefoil, c = −1/24 for the left." | **VERIFIED-DIFFERS:** exact for torus knots (monomial blocks), not in general — 4₁ is amphichiral with c = −1/16; the mirror-odd quantity is the centre of the block's exponent range, which is 0 for 4₁ and ±1/24 for the trefoils; the width is mirror-even and feeds c_eff |
| relay §1 | "a generation count has not been produced on this face" | **AGREES** — Q1's count half stays OPEN |
| relay §3, memo 178 | "L154's gap is not 'six versus one'. It is 6 = 1 + 5 … The 1 is the universal q^{−1/24} prefactor" | the bare rates 1/5 (Σ(2,3,5)) and 1/7 (Σ(2,3,7)) **VERIFIED** with an own estimator; the "+1" split is Gukov–Jagadale's half-index convention as the seat reads their eq. (55) — **REGISTERED** as the seat's reading (GJ read at abstract level here) |
| memo 177 | "the figure-eight's c_eff is bounded by 1, and its Ẑ stops existing at slope 4" | the assembly **VERIFIED as the seat's** by re-run (Table 10's nine series, eq. (13), eq. (175), the Legendre law's checks); GM's statements located in the text (pp. 6, 7, 52, 68, 72–73); not re-implemented here (Phase 3) |
| memo 176 §5–7 | (retracted by the seat the same day) | **SUPERSEDED-BY-SEAT**; nothing from them enters main |
| memo 172 (slice A carry) | "the only instrument this bench built whose control did not void it" | **NOT ADOPTED, second pre-registration** — see §5 |

## 1. Q1 — the two ends (`sliceB/b1305_ends.py`, PASS)

Two formulas for the trefoil — Habiro's cyclotomic expansion and the U_q(sl₂) R-matrix eigenvalue sum over V_J ⊂ V_{(n−1)/2}^{⊗2} for the closure
of σ³, with the framing/orientation convention fixed only on n = 2 against the Jones polynomial — agree **exactly at n = 3 and n = 4**. GM eq.
(166) for the figure-eight coded independently. At matched parity: **3₁: bottom end +(q;q)_∞, top end 1 (windows 13); 3₁'s mirror: the ends
swapped; 4₁: (q;q)_∞ at both ends (window 15)** — the cloud's table, reproduced. **The B1227 reading, computed:** the ratio R(K) = top/bottom
(constant terms normalised) obeys R(K*) = 1/R(K), so R² = 1 for an amphichiral knot: **R(4₁) = 1 exactly on the window; R(3₁) = 1, 1, 2, 3, 5,
7, 11, 15, 22, 30, 42, 56 = 1/(q;q)_∞ (the partition numbers); R(3₁*) = (q;q)_∞.** This is T-MIRROR-ODD-VANISHES in the group of formal
power series with constant term 1 (torsion-free: the only 2-torsion element is 1), which is why the quantum face, like the other three,
shows the object no chirality. The mechanism is in the literature — Armond–Dasbach 2011: head and tail depend only on the reduced
checkerboard graphs, which the mirror swaps; Garoufalidis–Lê 2015: stability — the reading and the ratio are the seats'.

## 2. Q2 — what exactly is mirror-odd in F_K (`sliceB/b1305_blocks.py`, PASS)

With the cloud's block generator (GM's recursion (171)–(172)) as the data source and main's own check on its output: for every k ≤ 20 the
figure-eight's block Ξ_k has lowest exponent −⌊(k−1)²/4⌋, highest +⌊(k−1)²/4⌋, and is **palindromic**. So c_low = −1/16 (GM's c) and c_high =
+1/16; the mirror-odd CENTRE (c_low + c_high)/2 = **0**, as B1227 demands of an amphichiral knot, and the mirror-even half-width is 1/16 — the
quantity that controls the surgery window |p/r| < 4 and the ceiling c_eff < 1. For torus knots GM's Thm 1.3 makes every block a monomial
(the seat's `torus_arm.py`, re-run here), so centre = c = ±1/24 and the relay's sentence is exact there. **Recorded as VERIFIED-DIFFERS on
the framing, in the seat's favour on substance:** chirality is the centre, growth is the width.

## 3. Q3 — the growth rates with an own estimator (`sliceB/b1305_mock_theta.py`, PASS)

F₀(q) = Σ qⁿ²/(q^{n+1};q)_n and χ₀(q) = Σ qⁿ/(q^{n+1};q)_n built by an own recurrence in **exact integers** (the first coefficients equal GM
eq. (175)'s 1, 1, 0, 1, 1, 1, 0, 2, 1, 2, 1, 2, 1, 3 and the seat's χ₀ control); a three-parameter fit log aₙ = A√n + B log n + C on the upper
half, c_eff = 3A²/(2π²), calibrated on 1/(q;q)_∞ (0.99998) and Rogers–Ramanujan G (0.39999): **c_eff(F₀) = 0.142857 = 1/7 and c_eff(χ₀) =
0.200000 = 1/5, B = −0.500 both** (F₀ to N = 20 000; χ₀ to N = 6 000 — a first float run of the 20 000-step chained recurrence corrupted, B =
−42, and was replaced by exact arithmetic; recorded). The seat's 1/7 (memo 174/177) and 1/5 (relay) reproduce.

## 4. Q4–Q5 — the seat's assembly and its dispositions

Table 10 (nine −1/r surgeries), eq. (13), eq. (175), the range (−4, 0) and c = −1/16 "experimentally" are GM's (pages located and quoted in
DESIGN_B); the seat reproduces all ten published series and adds the Legendre law, the threshold, sup c_eff = 1 and the Seifert cross-check
(`ceff_scaling_law.py`, `table10_control.py`, `xi_recursion_fast.py` re-run here, RC=0). The assembly is not re-implemented in this slice —
it is Phase 3's DESIGN work. Memo 180's own ledger (eleven of thirteen GM inputs checked on their bench; no error found in GM) stands as the
seat's. `park_52_blocks.py` reads `/tmp/k52/ahat.py`, a scratch file on the seat's machine: **VERIFIED-DIFFERS (script)** — the seat's open
normalisation between Park's F⁺ and GM's Ξ is its item, registered, not ours. Memo 176 §5–7: SUPERSEDED-BY-SEAT. Memo 178's re-reading of
GC-6 (B1190): a dated note on B1190; the σ bridge stays O3-obstructed (B1064) — the reading lowers the object-side number, it does not open
the bridge.

## 5. Q6 — the sense census, second pre-registration, NOT ADOPTED again (`b1305_sense_census.py --exclude`)

With the meta-exclusion list (this arc, HARVEST_LEDGER, CAMPAIGN_STATUS, RELAY_LEDGER, FRESH_EYES): `logarithmic` **11 / 3 = 27 %** — still
"genuine", the negative control still FAILS; the three remaining technical contexts are `docs/HINT_LEDGER.md` (slice A's own
H-B1305-META-CONTAMINATION row, which says "logarithmic CFT") and the two generated views (`REVIEWER.md`, `VERDICT_LEDGER.md`) carrying slice
A's verdict text. The instrument's own documentation defeats its control wherever that documentation is scanned. **NOT ADOPTED, as the
DESIGN's FAIL branch says; no third try in this slice.** The new idea, registered for the instrument arc (B1307): exclude every file that
names the instrument ("sense census"), or evaluate the negative control on the tree at a fixed pre-instrument commit — either is a new
pre-registration. The census's positive result on main stands as a reading: `character` 3665 / 13 after exclusion.

## 6. What this slice settles, and what it opens

- **FRESH_EYES Q1: the chirality half is CLOSED by computation** (the cloud's, and main's by two routes): the quantum face reads chirality
  as the ends' ratio, which is 2-torsion on an amphichiral knot — the fourth face where the object shows 2 or nothing. **The count half is
  OPEN.** Q6's mechanism is exhibited on this face; Q10's answer (access, not difficulty) is recorded and the per-seat source-fetch check goes
  to Phase 4 (1).
- **Phase 3's DESIGN inputs are now pinned:** GM read where it is load-bearing; the seat's assembly and its ceiling c_eff < 1 (to be
  re-implemented there); the mock-theta identities; the split "chirality = centre, growth = width".
- **The seat's diagnosis of the relay lag is taken as written**, and the harvest-debt gate (B1307) is the fix; this slice landed the same
  night the relay was filed.

## Receipts, verification, credit

`sliceB/`: `cloud_trefoil_ends_rerun.txt`, `cloud_table10_control_rerun.txt`, `cloud_mock_theta_ceff_rerun.txt`, `cloud_colored_jones_validate_rerun.txt`,
`cloud_ceff_scaling_law_rerun.txt`, `cloud_xi_recursion_fast_rerun.txt`, `cloud_torus_arm_rerun.txt` (RC=0), `cloud_park_52_blocks_rerun.txt` (RC=1, the
scratch dependency); own code `b1305_ends.py`, `b1305_blocks.py`, `b1305_mock_theta.py` (+ `.out`/`.json`), `../b1305_sense_census.py --exclude`
(`b1305_sense_census_main_excluded.out`/`.json`); `already_banked_at_seal.txt`. Literature: Gukov–Manolescu arXiv:1904.06057v2 (text located);
Armond–Dasbach arXiv:1106.3948, Garoufalidis–Lê arXiv:1112.3905, Gukov–Jagadale arXiv:2308.05360, HJNP arXiv:2508.10087 (abstracts). Lock:
`tests/test_b1305_the_cloud_156_178.py` (slice B tests added). HARVEST_LEDGER rows 44 (updated), 45–53.
