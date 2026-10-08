# B1620 — THE BREAKING THE WEAVE ALLOWS: on every subgroup of the weave's group, three distinct masses need an abelian residual, the masses stay free, and no mixing family short of the full four reaches the quark data — the weave's symmetry reduces none of the Standard Model's 13 flavour parameters (under all three mass tensors); with couplings in τ alone every mixing matrix is a permutation, so the observed mixing needs a vacuum that breaks the parity grading; and outside the weave the principle's own word splits the three parity sectors 1 + 2 — the clock's parity bounded, the two letter-reading parities one orbit of the inflation φ

**Verdict: PROVED** (all six sealed cells hold; A3's lepton clause is sharper than sealed, B2's record law sharper than
sealed). cc (main), 2026-10-08. Sealed `aa28a42e6` before the run. The owner agreed on 2026-10-08 to restate the goal:
derive the Standard Model's structure, and how many free numbers the principle leaves and why. Every claim here is about
the weave (every subgroup, none chosen), never one thread's. Part A reads no data in its sealed cells; the post-seal
grading of A3's data clause reads only what B1612 transcribed. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /subgroup lattice|breaking pattern|residual symmetr|parameter count|free parameter|Sturmian|parity of|Rote|deterministic random walk|discrepancy/: 58 of 1391 arcs on main match (NEGATIVE 9, OPEN 7, PROVED 42)`
— B1611, B1612, B1615–B1618, B1083, B107, B1347. **Literature:** the commissioned brief, read before the seal: the
parity classes of the Fibonacci prefixes at density ¼; the record scaling φ⁶; the Rote sequences'
critical exponents (Dvořáková–Medková–Pelantová, arXiv:2003.06916); OEIS A273129; no published discrete-flavour model
reduces the 13 by a definite number (King–Luhn 2013; Feruglio–Romanino 2021); residual groups at modular fixed points
are normally abelian (Novichkov–Penedo–Petcov 2021). **After the seal and before the grading:** the SM seat's W38–W41
(@ `e077e4ba0`) and the audit lane's relay of 2026-10-08 (@ `c8c910a77`) were read (harvest rows 1049–1056).

## 1. The computation (`breaking_the_weave_allows.py`, sealed, unchanged; `breaking_the_weave_allows.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **A1** | the subgroup lattice computed, classes up to conjugacy listed | 98% | **HOLDS** — **68 subgroups in 26 conjugacy classes**, orders 1 to 96 |
| **A2** | three distinct masses only on an abelian image; such subgroups exist | 95% | **HOLDS** — 20 of the 26 classes allow three distinct masses, of orders 1, 2, 3, 4, 6, 8, 12 and 16. Post seal (P1): **on all 68 subgroups, T restricted to H is a sum of characters exactly when H is abelian (57 of 68)** |
| **A3** | minimal mixing freedom 0 (fixed patterns, none in the data); every data-compatible pair needs ≥ 1 free lepton parameter and the full four in the quarks — the weave reduces none of the 13 | 70% | **HOLDS** — see §2 |
| **B1** | the four parity classes at frequency ¼ each, to 10⁻³ | 99% | **HOLDS** — to 7 × 10⁻⁸ at N = F₃₅ = 14 930 352 |
| **B2** | (−1)ⁿ bounded by 1; (−1)^A and (−1)^B unbounded, records growing by factors near φ⁶ | 90% | **HOLDS, sharper** — (−1)^(A+B) = (−1)ⁿ never exceeds 1. The a-walk reaches 13 and the b-walk 12. Successive record positions alternate the exact ratios 1 + 2/√5 = 1.8944 and 5 + 2√5 = 9.4721, whose product is φ⁶ = 17.944: **one record per unit of height, two per factor φ⁶**. And the b-walk's records sit at the a-walk's positions times φ (574 924 / 355 322 = 1.61803) |
| **B3** | at the Fibonacci lengths the class cycles (1,0), (1,1), (0,1), never (0,0) | 99% | **HOLDS** at every F_j to F₃₅ |

## 2. Part A graded: the post-seal checks (disclosed in §4)

**The sealed tensor, T̄ ⊗ T** (`post_seal_pairs.py`, the free unitaries U(m) on each repeated character's piece; and
`post_seal_tensors.py`, the invariant mass matrices themselves; the two agree). Every ordered pair of three-mass
subgroups: 57 × 57 = 3249 pairs. The family dimension is the rank of the map to the nine |V_ij|² and J:

| family dimension | pairs | pass the CKM block test | pass the PMNS block test | reach the data (fit) |
|---|---|---|---|---|
| 0 (fixed) | 1089 | 0 | 0 | — |
| 1 | 939 | 0 | 0 | — |
| 2 | 744 | 0 | 264 | **PMNS: yes** (the TM-type families, the minimum) |
| 3 | 144 | 0 | 144 | PMNS: yes |
| 4 (the full mixing) | 333 | 333 | 333 | both |

- **Masses:** every three-mass subgroup leaves at least three free complex couplings in its sector, so no charged-fermion
  mass is fixed.
- **Quarks:** no pair whose family has fewer than four dimensions passes even the necessary test (block sums within
  3σ). The CKM needs the full four.
- **Leptons:** the smallest family reaching NuFIT 6.0's 3σ ranges has **two** parameters (the TM type, one angle and
  one phase: P10's family). Families of dimension 0 and 1 never reach them. The sealed "at least one" is right, and two
  is the sharp number.
- **The control:** the fixed pairs give 8 distinct patterns. They include all six of B1612's full patterns; the other two
  are the permutation and one pattern with a zero entry. None passes either data set.

**W39's tensors, T ⊗ T and Sym² T** (`post_seal_tensors.py`): the same pairs, the masses as the singular values of an invariant matrix and the left-handed
rotations from M M†:

| tensor | three-mass subgroups (all abelian) | pairs | CKM: smallest family reaching | PMNS: smallest family reaching |
|---|---|---|---|---|
| T̄ ⊗ T (sealed; B1615) | 57, orders 1–16 | 3249 | **4** (no pass below) | **2** |
| T ⊗ T (W39; with an antisymmetric part) | 24, orders 1–8 | 576 | **4** (no pass below) | **2** |
| Sym² T (W39; E₆'s cubic, one 27 Higgs) | 16, orders 1, 2, 4, 8 | 256 | **4** (no pass below) | **4** (no pass below) |

- **The 13 are unreduced under every tensor.**
- **The leptons' reduction depends on the tensor.** Under Sym² T no residual of order 3 is viable, because the 3-cycle's
  complex characters pair into degenerate masses (W39's "(|a|, |b|, |b|)"). No family short of the full four then passes
  even the PMNS block test, so **TM1 (P10) is allowed by no residual pair under Sym² T in the record's frame.**
  FALSIFIER_REGISTER carries the scope note.
- The family's block sums were checked to be shared at two random points of every pair, which is the premise of the
  block test.

**Couplings in τ alone** (`post_seal_inner.py`; the SM seat's relay §41.2 asked). The inner automorphisms fix every τ
with automorphy factor 1. Their two lifts generate an abelian K of order 4 that splits T into its three parity lines. So
at every τ the residual of a coupling depending on τ alone contains K. Among the 10 subgroups containing K, the viable
ones (orders 4, 8, 16 for T̄ ⊗ T; 4 and 8 for T ⊗ T and Sym² T) give, for every pair, **a mixing family of dimension 0,
and every pattern is a permutation**. The data exclude a permutation: the CKM's closest, the identity, sits 331σ away
(B1612 D2), and the PMNS has no zero entry. **So given Λ, with couplings in τ alone, the weave allows no mixing angle at
any τ.** The observed mixing needs a vacuum that breaks the parity grading, or several Higgs representations per sector
(the seat's reading, confirmed). B1618's odd-weight addendum agrees for the Majorana term.

## 3. What it says

**For the restated goal's second half, the symmetry side is now counted on the whole weave.** The weave's group (order
96) fixes no flavour number on any of its 68 subgroups: masses free and the CKM free (all four), under the tensor B1615 used and under the two the SM
seat reads given Λ. The PMNS can be reduced to two free parameters (the TM-type families, P10's TM1 among them) under
T̄ ⊗ T and T ⊗ T, and not at all under Sym² T in the record's frame. With the gauge side (the gauge three a selection, B1606) and the record's
bounds (no dimensionful number from the object, B811/B1012; no hypercharge normalisation, B991): **of the 19, the
principle so far fixes none. Its derived content is structure:** the flavour three, the hand as a convention, CP as the
swap, TM1 allowed under T̄ ⊗ T and T ⊗ T (P10, two relations if the leptons' residual is the TM type; not under Sym² T), and now the condition that the observed
mixing needs a vacuum that breaks the parity grading.

**Outside the weave, the principle's own word separates the parity sectors 1 + 2.** The fixed-point word of the rule
σ: a → ab, b → a visits the four parity classes equally (B1), so it selects no sector by frequency. But it distinguishes
one. The clock's parity (−1)ⁿ = (−1)^(A+B) counts letters without reading them and stays bounded. The two characters
that read the letters wander without bound, logarithmically, and are one walk up to the inflation φ (B2). At the
substitution's own scales the rule's 3-cycle on the parities is exact (B3), and only the statistics of the whole word
break it. On T the three parity sectors are the three lines B1618 found, with characters (a, b) = (−, +), (+, −),
(−, −). The clock's line is (−, −), the line the parity grading and the 3-cycle U treat like the others. **This is a
forced 1 + 2 split, supplied by the principle and not by the weave, and it is elementary:** its content is that the
rule's time counts both letters (A + B = n). Whether it is physical — TM1's special column, or a third-generation
distinction — needs a coupling that reads the word, not only τ. That is the next question, not this arc's claim.

## 4. Disclosed

- **The post-seal checks** (`post_seal_pairs.py`, `post_seal_tensors.py`, `post_seal_inner.py`) were written after the
  sealed run. They grade the sealed text's clauses that the sealed instrument does not compute: A2's "abelian", and
  A3's "data-compatible". The SM seat's W39 and the audit lane's relay were read before they were written, and the
  T ⊗ T and Sym² T runs answer them. No data beyond B1612's transcription (PDG 2025 CKM, NuFIT 6.0 |U| ranges) is read.
- **A bug caught in them before any reading was taken:** the family-dimension rank used a relative-only threshold, so
  pure rounding noise counted as rank (the inner cell reported dimension 2 for families whose every pattern was a
  permutation). An absolute floor of 10⁻⁵ (rounding error ~10⁻¹⁰) was added and every post-seal run repeated. The
  T̄ ⊗ T tally was unchanged by it.
- The fits in `post_seal_tensors.py` were moved from Nelder–Mead on the max-objective to L-BFGS on a smooth squared
  objective, for speed, before its results were read.
- The block test is necessary, not sufficient. Every "reach" is decided by a fit over the family.
- Part B was not blind (§0). The instrument recomputed the brief's numbers to N ≈ 1.5 × 10⁷. The exact record ratios and
  the φ-lag between the two walks are new here.
- **Frame:** the record's lifts, where the character c is physical (W24's E₈ embedding). GENESIS FK11 is open (the SM
  seat's §39.3), and in a frame with a U(1) on T, Sym² T gains a singlet.

## 5. Files

`verification/breaking_the_weave_allows.py` (sealed, unchanged), `breaking_the_weave_allows.json`, `breaking_run.txt`;
post seal: `post_seal_pairs.py` / `.json`, `post_seal_tensors.py` / `.json`, `post_seal_inner.py` / `.json` with their
run logs. Test: `tests/test_b1620_the_breaking_the_weave_allows.py`. Related addenda of the same day: B1618
(`ADDENDUM_2026-10-08_the_odd_weight_majorana_case.md`), B1619 (`ADDENDUM_2026-10-08_two_neutral_executed.md`).
