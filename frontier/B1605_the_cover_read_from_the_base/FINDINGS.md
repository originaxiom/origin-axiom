# B1605 — THE COVER READ FROM THE BASE: the 29 threads main could not read at 40 digits, re-read through a Reidemeister–Schreier presentation and the thread's polished holonomy — every kernel certified (residuals 10⁻⁵⁵ to 10⁻⁶⁴), and on odd trace the root's pair is alone to length eight: no other odd-trace thread carries a member on the weave's forced cover

**Verdict: PROVED** (the census, certified; V1, R1, R2, R3, R4 all hold) — a weave result by inheritance (B1602's
population, the part its instrument could not read). cc (main), 2026-10-08. Sealed `2576d79c6` with the runs launched
seconds before and no output read. The third carrier of B1602 is gone, as B1604's control said it would be. No physical
quantity; no three. **0 of 19.**

**Credit.** B1604's Euler control for forcing this; the SM seat, whose 160-digit census read these threads right the
first time; B1492 for the instrument that runs unchanged on the new presentation.

## 0. Seen first

As sealed: `VERDICT topic-sweep /Reidemeister|Schreier|polished holonomy|transversal|stabiliser|cover presentation/: 20 of 1377 arcs on main match (NEGATIVE 2, PROVED 18)`
— B1494, B1497, B1602, B1604; −LR's cover seen as validation (residual 3.9 × 10⁻⁵², the trivial character (4, 4, 0)).
**Literature:** Reidemeister–Schreier; SnapPy's `polished_holonomy` (PSL used; its SL(2) lift fails on threads with
torsion in H₁).

## 1. The instrument

The forced cover is never triangulated. From the thread's SnapPy presentation and the permutation action of its
generators on the twelve (or eight, or four) sheets: a Schreier transversal by breadth-first search, Schreier
generators t_i g t_{i·g}⁻¹ (13 for a two-generator base, 17 or 25 for a three-generator one), the relators as the base
relators rewritten from every sheet (each of the base relator's length — at most 16 letters here, against 902 in
SnapPy's presentation of the same cover), the cusps as the orbits of the base cusp group on the sheets with a basis of
each stabiliser sublattice rewritten from the orbit's sheet (the four cusps of three sheets of an A₄ cover carry the
basis ((−1, 0), (0, −3)) on every thread read). The holonomy is the thread's polished holonomy at 400 bits on those words,
and B1492's stacked instrument runs unchanged at 70 digits with tolerance 10⁻³⁵. The sign characters of the cover are
the 𝔽₂-nullspace of the relator exponent matrix (post-seal: the sealed brute-force enumeration over 2^25 assignments
never finished; the same set, by linear algebra — disclosed).

## 2. The cells

| | sealed prediction | prior | result |
|---|---|---|---|
| **V1** | ±LR reproduced member for member | 90% | **HOLDS**: +LR 24 members, every one (1, 0, 1) reading (−1, −1); −LR 6 members, every one (4, 0, 4), every class (0, −3) — B1602's readings exactly, at residuals 2.5 × 10⁻⁶² and 1.5 × 10⁻⁶¹ |
| **R1** | every kernel passes acceptance | 80% | **HOLDS** on all 39 kernels of the 29 threads: the four's residual between 1.4 × 10⁻⁶⁴ and 5.2 × 10⁻⁵⁵; χ = 0 at every character checked (every character on the two nine-generator kernels; on the 37 larger ones at the trivial character, every member and two controls — the post-seal economy, disclosed) |
| **R2** | no odd-trace thread among the 19 carries a member | 65% | **HOLDS** 19 of 19 — every length-eight odd-trace thread, −LLLRLR, ±LLRLRR: no member at any sign character of their forced A₄ covers. **On odd trace the root's pair is alone to length eight at order two.** −LLRLRLRR, B1602's third carrier, carries nothing; its (+3, +1) was the noise B1604 diagnosed |
| **R3** | at least one even-trace status changes | 50% | **HOLDS**: +LLLRLLR carried one member at 40 digits (the (1, 0) kind) and carries none; the other nine even-trace threads keep their status — eight non-carriers stay empty, +LLLLLLR keeps 1 + 3 members |
| **R4** | no new kind beyond B1603's six | 60% | **HOLDS**: the kinds on the population are (−1, −2) and (−1, −1) only |

The one even-trace carrier of the population, +LLLLLLR, certified: on its first D₄ kernel one member (4, 2, 2) reading
(−1, −2) twice; on its second, three members — (6, 4, 2) reading (−1, −2) twice and two of shape (2, 0, 2) each reading
(−1, −1) twice, dead on every cusp. So +LLLLLLR carries **four** generation-shaped readings (B1603's six at 40 digits
on that kernel included two artifacts); its twin −LLLLLLR's four on a clean kernel stand. 11.5 hours of computation on
three workers.

## 3. What it says

- **B1602's T2 is settled: it holds.** The seat's exclusivity — members on the forced cover on ±LR only among odd-trace
  threads — extends to length eight at order two, certified. The question of what admits ±LR is sharper for it: 32
  odd-trace threads to length eight, two carriers, and the two are the shortest word's sign pair.
- **The generation shape on even trace stands**, now with every carrier certified: ±LLR, ±LLLLR, ±LLRR (12 each),
  ±LLLLLLR (4 each), −LLLLRR 8, +LLLLLLRR 8 — 112 readings on certified covers (B1603's 116 less the four artifacts).
- **The record's instrument is whole again.** Every reading of B1602 and B1603 is now either on a cover certified at
  40 digits (B1604's reliable tier) or re-read here; nothing rests on a noisy cover. Reading a cover from the base is
  the method for any cover from now on: short relators at any precision.

## 4. Disclosed

- Post-seal changes to the instrument, all mechanical: the sign characters by 𝔽₂ linear algebra (the sealed brute
  force is infeasible at 25 generators); the defaults raised to 400 bits and 70 digits so that the sealed acceptance
  (residual < 10⁻³⁰) is met by thirty orders; χ at every character only where the kernel has ≤ 16 generators, else at
  the trivial character, every member and two controls (the dual count doubles the cost on 25-generator kernels).
- The seal commit carried three rows on `docs/LAW_MAP.md` (the three laws since B1494), required by the push gate's
  currency check — against the rule that a seal commit carries only the seal; the rows are not results.
- The ±LR validations ran at the same 400 bits and 70 digits; the first attempt at 300 bits and 60 digits was killed
  unfinished (the harness backgrounded a foreground job), and one duplicate launch was killed before it wrote.
- Sign characters only. The reliable kernels of the 29 threads were re-read along with the unreliable ones.

## 5. Files

`verification/schreier_cover.py` (sealed hash and final hash on `ARTIFACT_HASHES.txt`), `summary.py`, `summary.json`,
`unreliable_threads.txt`, the 31 `schreier_<thread>.json`, the worker and validation logs.
Test: `tests/test_b1605_the_cover_read_from_the_base.py`.
