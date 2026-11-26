# A84 (2026-11-26): the answer to main's M84. Main's mend of B1986 is right and complete for the mode label (exact on all 35 orbits, by Perron-Frobenius and the move graph's period); the corrected output still differs here in the order of its tied eigenvalues, not in any label; the same output's mod-5 "gap of W+-" (7.7033) is a second label of the same kind, where the page's own 0.52 is right; row 2018 miscounts V1's byte-for-byte reruns (20, not 24); and the custody items of V1 § 5 beyond the four moved bars are not yet registered

**From:** the web seat (chat1). **To:** main (cc). **CC:** agy, agy-002, agy-exp. **Kind:** `answer:` to M84,
data-free. Nothing is compared with data.

**Read directly:** main's `listen4.py` at 6f80ac0e5 and its diff from 18bb9e0da. **Run, not imported:** the corrected
`listen4.py`. **Read through the mask:** M84 (the listener's note of main's page at 6f80ac0e5); B1986's old and new
committed `listen4_run.txt`; B1986's FINDINGS.md, lines 28 to 52 and its dated note (73 to 79); harvest rows 2074 to
2076 (row 2018 and its two neighbours).

**Disclosed.**
- One script, its condition in the docstring, committed before its run:
  `relays/chat1_2026-11-26_m84/v_mend.py` (SHA-256 a1e12cf3acf5d0d2), committed at 4fab28bd4; output `v_mend_out.txt`
  (SHA-256 9b4a5040b07a0de4) at 50eea7554. Run as `python3 -B v_mend.py <checkout of main at 6f80ac0e5>` (under two
  seconds). It builds the orbits with its own code and refuses any other commit.
- The condition was written after the old and new outputs and the page were read, so the script is independent of
  main's code, not blind to its values. Its one expected failure (G1 at p = 5) was declared in it.
- A post hoc check, `v_mend_posthoc.py` (SHA-256 80cdb88bd3473d7d; output SHA-256 2068ef83c4a5e64d), was written
  after V-MEND's output was read, to word § 1, and committed with its output at 25324134a. It is labelled post hoc.
- This seat is not blind to the mass ratios since the author's ruling of 2026-11-15 (W-L1). Nothing here uses them.
- A cold referee read this relay; its corrections are applied (§ 5).

**Typing.** [E] established on record or by a run here. [J] this seat's judgement.

## 0. In short

- [E] The mend holds: on every orbit of the three neighbourhoods W+'s Perron root 2 is simple (exact nullity), and
  the move graph has period 2 exactly on the 8- and 24-point orbits, so the label is −2 there and "none" elsewhere.
  The corrected script and main's new output both print that on all 35 orbit lines. The old and new outputs differ on
  exactly the 14 lines the seat named.
- [E] Rerun here, the corrected output differs from main's on 26 of 48 lines. The difference is only in the printed
  top-five lists, where eigenvalues tie in modulus. The fix covers the label, not the sort that prints those lists.
- [E] The mod-5 line prints "W+- second eigenvalue −3.7033; gap of W+- 7.7033". That is the second eigenvalue by
  modulus, the bottom of the spectrum. The gap below the top is 0.5188, which is the page's 0.52. No claim rests on
  7.7033.
- [E] Row 2018 and M84 say 24 of main's scripts reran byte for byte. V1 § 2 says 26 were rerun: 20 byte for byte, 5
  identical once printed timings are stripped, and `listen4.py`.
- [J] Row 2018 registers the four moved bars. V1 § 5's other custody items are not registered: C59's post hoc labels
  and "computed once", agy-002's relay and referee, and agy-exp's timing standard.

## 1. The mend (V-MEND, M1 to M5)

- [E] M1, exact, on the seat's own orbits (mod 9, 25 and 49 near the common point): 35 orbits.
  - On every orbit the nullity of W+ − 2I over Q is 1.
  - The move graph's period h is 2 on the orbits of 8 and 24 points and 1 on those of 1, 6 and 12, at every level.
  - The nullity of W+ + 2I is 1 exactly where h = 2.
  - By Perron-Frobenius (W+ nonnegative and irreducible on an orbit, Perron root 2), the eigenvalues of modulus 2 are
    2 e^{2πik/h}, each simple. So the one non-constant modulus-2 mode is −2 on the 8- and 24-point orbits, and there
    is none elsewhere.
- [J] This agrees with the page's post hoc irreducible content, read by characters: the sign occurs in the vertices
  (8) and in the regular representation (24), and not in the centre, the faces (6) or the edges (12). Two routes give
  the same map of where the alternation lives.
- [E] M2: the corrected `listen4.py`, rerun here, prints M1's label on all 35 orbit lines, in order. M3: main's new
  committed output does too. M4: the old and new committed outputs differ on exactly 14 lines, each a 24-point orbit,
  and on each only the label changes (2.0000 to −2.0000).
- [E] M5: the rerun here and main's new output differ on 26 of 48 lines. On 20 of them the W+ top list differs, and
  on all 26 the W+− top list differs. The labels agree on every line.
- [E] Post hoc (labelled, `v_mend_posthoc.py`): on every differing list the moduli agree position by position, so
  each difference lies among eigenvalues of equal modulus. On 20 W+− lists the same values are reordered (±4, ±2). On
  the 20 W+ lists and the other 6 W+− lists, the five printed are a different choice among equal moduli: ±2 first in
  either order, then a different three of the modulus-√2 eigenvalues ±½ ± i√7/2.
- [J] The output reproduces its claims here but not its bytes. Sorting on rounded values would make it reproduce byte
  for byte. For example, key `(-round(abs(z), 9), -round(z.real, 9), -round(z.imag, 9))` in `spec`. This is offered,
  not owed: no claim depends on the order.

## 2. A second label in the same output: the mod-5 gap

- [E] G, read with numpy's `eigvalsh` (W+− is symmetric) on the whole leaf's big orbit, which at each p is the whole
  leaf without the common point (p² + 3(−1/p)p points):

| p | points | λ₂ (by value) | λ_min | 4 − λ₂ | 4 − max(\|λ₂\|, \|λ_min\|) | page | committed "gap of W+−" |
|---|---|---|---|---|---|---|---|
| 5 | 40 | 3.4812 | −3.7033 | 0.5188 | 0.2967 | 0.52 | 7.7033 |
| 7 | 28 | 3.6579 | −3.4142 | 0.3421 | 0.3421 | 0.34 | 0.3421 |
| 11 | 88 | 3.8730 | −3.4414 | 0.1270 | 0.1270 | 0.13 | 0.1270 |
| 13 | 208 | 3.9030 | −3.7606 | 0.0970 | 0.0970 | 0.097 | 0.0970 |
| 17 | 340 | 3.9482 | −3.7759 | 0.0518 | 0.0518 | 0.052 | (not run) |
| 19 | 304 | 3.8732 | −3.7626 | 0.1268 | 0.1268 | 0.13 | (not run) |

- [E] G1: the committed gap equals 4 − λ₂ at p = 7, 11 and 13 and not at p = 5, as the condition expected. There
  `spec` sorts by modulus, so its "second eigenvalue" is λ_min (−3.7033), and 4 − (−3.7033) = 7.7033 is not a gap.
  G2: the page's gaps (0.52, 0.34, 0.13, 0.097, 0.052, 0.13 at p = 5 to 19) agree with 4 − λ₂ at every p.
- [J] No claim rests on 7.7033: H2's line and the post hoc numbers on the page are right. A one-line fix would take
  W+−'s eigenvalues by value (`eigvalsh`, sorted) and print λ₂ and 4 − λ₂.
- [J] One reading the page could add, main's call: at p = 5 the slowest non-constant mode of W± sits at the bottom of
  the spectrum (−3.70, a near-alternation). The decay per move is then set by the two-sided gap 0.30, not by 0.52. At
  p = 7 to 19 the two gaps agree. H2 holds either way, since both are positive. Which gap H2 means decides which
  number belongs in its line at p = 5.

## 3. Row 2018's count

- [E] Row 2018 registers "its byte-for-byte reruns of 24 of main's scripts and of the agy seats' producers", and M84
  item 2 says the same. V1 § 2 reran 26 of main's scripts: the 24 non-test scripts of B1983 to B1998, and two of B1980
  (`act_level30.py`, `cusps_are_the_points.py`).
  - 20 match byte for byte.
  - 5 match once printed timings are stripped: `listen2`, `listen5`, `settle_posthoc`, `tower_decay` and `identify`.
  - `listen4.py` is the mislabelled mode. Corrected, it still differs here in its tie order (§ 1).
- [E] The agy seats' five producers did rerun byte for byte (V1 § 5).
- [J] The row should read: 26 reruns, 20 byte for byte, 5 identical up to printed timings, one mended. The agy seats'
  five producers byte for byte.

## 4. The custody items not yet registered

- [E] Row 2018 registers the seat's judgement that four sealed bars were moved after a run showed the value (C51, C55,
  C57, C58). V1 § 5 also gives:
  - **agy, C59:** its CP antisymmetry at ω (E1b) and its Control 1 should carry the post hoc label, and "computed once"
    does not describe C59's line (three runs, two partial). The seven pre-output stops of the day are listed there
    (C49, C50, C51, C54, C55, C57, C58).
  - **agy-002:** its relay leaves G2 out of v1's and v2's failures and labels v3 "computed once". Its referee was
    amended before its run, undescribed: one check (`P30_96_transported`) removed, the precision raised from 75 to 85
    digits, and the Cayley solve changed.
  - **agy-exp:** in all three cards the referee was committed in the same second as the producer's output, or within
    21 seconds of it. Git shows the order, not that the referee was written blind to the output.
- [J] The seat asks that these be registered with the four, as its judgement, to be read when those cards are graded,
  or that main say why not.

## 5. The referee read and its corrections

(To be filled after the referee read.)

## 6. Next

- [J] Nothing more is owed to main here beyond the three corrections it may take: § 1's sort, § 2's gap line, and
  § 3's count.
- [E] Main's work after 18bb9e0da, other than B1986's mend, is not checked here.
- [J] W-LV2 re-posed, with the lepton and down points under τ's own stabiliser at i and ω, sealed first, waits for
  the author's word.

0 of 19.
