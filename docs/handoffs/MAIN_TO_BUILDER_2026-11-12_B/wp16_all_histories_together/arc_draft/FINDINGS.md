# B[[N]] — All histories together: a product over threads, and the law of the rates at which sectors cancel

*Main, 2026-11-12 (S306p). A first exact object for the plan's package WP-1.6 (the law and the weight), and what it says
for WP-1.5 (the root, selection and thread results). It grew out of the owner's question of that day on selection
(register row P-831) and the test he asked for. Exact arithmetic for the identities and the level-15 value; double
precision, with every rate computed twice, for the sectors of levels 2 to 13 and the graphs of levels 2 to 100. No
measured number is read, no value of the modulus is used, and nothing is given a physical meaning. 0 of 19.*

## 1. The answer first

- **"All histories together" has an exact form, and it is a product over threads.** In any sector, the sum over every
  history of n moves is the n-th power of one matrix, the sum of the two moves. Its generating function is a product
  with one factor for each thread and one for each of the two letters (an identity of Amitsur's, 1980). No thread is
  chosen: the threads are to the whole what the primes are to the integers.
- **The two moves, acting together, are a walk that never turns back on a three-valent graph.** At levels 3, 4 and 5
  that graph is the tetrahedron, the cube and the dodecahedron.
- **The law does not weigh, and it still gives numbers.** With every history counted once, each sector cancels at a
  definite rate per move:
  - **two never cancel:** the trivial sector and the parity of the number of moves;
  - **an even sector** (the sign −1 acts as +1) cancels at exactly 1/√2 or at 1/2, unless the level's graph has an
    eigenvalue beyond 2√2 in it (Ramanujan's bound), and then slower;
  - **an odd sector** (the sign acts as −1) cancels no slower than √3/2, and at exactly √3/2 when the element of order
    three fixes no vector in it.
- **The first sector beyond the bound is at level 15.** It is one sector of dimension four: the join of level 3's
  fundamental doublet with the level-5 doublet in which the move L has trace 1/φ. The graph's eigenvalue in it is
  −(1/φ + √2 φ), exactly, and its rate is 0.893614. It is beyond the bound because φ is larger than √2. Its twin under
  √5 → −√5 stays at 1/√2.
- **On the record's ladder taken at once (level 60) it is the only one,** with its twist by the parity. **It is not the
  slowest of all levels:** to level 100 the graph is beyond the bound at 48 levels, and level 48 has a larger
  eigenvalue, 2.931852. Nothing larger was found to level 100.
- **The record's own triplet is covered by the same law.** The two moves are the two generators of the braid group on
  three strands, one of them inverted, and the law extends to every module of that group. On the triplet the sum of
  the two moves has characteristic polynomial x³ − √2 x² + x + √2, exactly; the triplet cancels at 0.753248 per move.
- **Looking back** (§ 7): all 88 sets of least departures on record are whole mirror orbits.
- **What this does not do:** it selects nothing. The slowest sector changes when the inverse moves are counted as
  separate histories (§ 6), and it changes with the range of levels. No rate is given a meaning.

## 2. What is proved

Write S = L R⁻¹ L and U = L R⁻¹.

| | statement | proof |
|---|---|---|
| Z1 | In SL(2, ℤ): S² = −1, and with U₃ = S⁻¹L, of order 3, L = S U₃ and R = −S U₃⁻¹. A positive word in L and R is, up to the sign, an alternating word in S and U₃^{±1}: a reduced word of the free product ℤ/2 ∗ ℤ/3 = PSL(2, ℤ) | integer matrices; every positive word to length 10 |
| Z2 | det(1 − u(ρ(L) + ρ(R))) = ∏ over Lyndon words w of det(1 − u^{|w|} ρ(w)), for any two square matrices. The Lyndon words in two letters are the two letters and one word for each primitive cyclic word with both letters | Amitsur's identity, cited; checked to order 10 on (L, R) and to order 8 on a pair of 3 × 3 integer matrices that have nothing to do with the moves |
| Z3 | In the defining representation det(1 − u(L + R)) = (1 − u)(1 − 3u), a thread's factor is 1 − tr(w) u^{|w|} + u^{2|w|}, and ∏ over threads (1 − tr(w) u^{|w|} + u^{2|w|}) = (1 − 3u)/(1 − u)³ | from Z2; checked to order 14 on 2,536 threads |
| B1 | L and R⁻¹ satisfy the braid relation, S² = U³ is central, L = U⁻¹S and R = U S⁻¹. In an irreducible unitary sector where S² = c: L + R = U⁻¹(1 + U⁻¹)S. So the singular values of the averaged move (L + R)/2 are \|cos(t/2)\|, t over the arguments of U's eigenvalues; its rate is at most the largest; \|det\| is their product | three lines of algebra, from U³ = c |
| Z4, even | c = 1: the averaged move is ρ(S)(3P₁ − 1)/2, with P₁ the projection on the vectors U fixes and ρ(S) a Hermitian involution. On a plane where the two are in general position at angle t its two eigenvalues multiply to 1/2 and add to (3/2) cos 2t: a complex pair of modulus exactly 1/√2 when \|3 cos 2t\| ≤ 2√2, a real pair otherwise. 3P₁ρ(S)P₁ is the adjacency operator of the level's three-valent graph (vertices the cosets of U, edges S). The other eigenvalues are ±1/2 | the theory of two subspaces; the graph's operator read off |
| Z4, odd | c = −1: the averaged move is (√3/2)·Σ·D with Σ a Hermitian involution and D = P_ω − P_ω̄. So the rate is at most √3/2; where U fixes no vector, D is an involution too, Σ D is unitary, and every eigenvalue has modulus √3/2 | the same algebra |

## 3. What is computed

**Levels 2 to 13, every sector** (`rates_by_sector.py`): 171 sectors new at their level. Each rate is computed twice,
on two independently drawn bases, and the two agree.

| | count | rates with the two moves |
|---|---|---|
| even sectors | 85 | 1 (one: the parity of the number of moves), 1/√2 (75), 1/2 (9) |
| odd sectors | 86 | √3/2 (13: the two-dimensional ones of levels 3, 4, 5, 6, 8, 10 and four characters of level 12), then values from 0.8285 down |

- The thirteen at √3/2 are exactly the odd sectors in which U fixes no vector.
- The three-valent graph of each level from 2 to 13 obeys Ramanujan's bound. Its largest eigenvalue below 3: 1 at
  levels 3 and 4, √5 at 5, 2 at 6, (1 + √17)/2 at 7 and 12, 1 + √2 at 8, 1 + √3 at 9 and 11, φ² at 10, 2.825573 at 13.
- The graph is two-coloured exactly at the even levels: that is the parity of the number of moves.

**Levels 14 to 100, the graphs** (`level_graphs_further.py`, dense, to 32; `level_graphs_sparse.py`, to 100; the two
agree where both ran): 87 levels.

- **Beyond the bound at 48 of them,** first at 15, then 29, 30, 34, 37, 40, 43, 45, 47, 48, and from 51 on at most levels. **Within it at 39:** 14, 16 to 28, 31, 32, 33, 35, 36, 38, 39, 41, 42, 44, 46, 49, 50, 54, 57, 62, 64, 66, 76, 78, 79, 83, 93, 98 and 100.
- **The largest eigenvalue below 3 found to level 100 is 2.931852,** at level 48, six times, and again at 96. It agrees with 1 + 2 cos 15° to thirteen digits; that is not proved here. Its sector is even at level 3 and at level 16, so it is not a join of two odd sectors.
- **The level-15 value, 2.906280, is the second largest.** It is found again at level 40, where no divisor has it: there it is 1/φ + √2 φ to thirteen digits, four times, in a sector odd at level 5 and odd at level 8, a join of two doublets again (`the_sectors_at_40_and_48.py`). And at the multiples of 15 and 40.
- **Every other eigenvalue beyond the bound that is new at its level lies between 2.8284 and 2.8846.**
- **Level 60,** read with sixty eigenvalues from each end: beyond the bound only ±2.906280, four times each; the next is 2.826120, twelve times.

## 4. The sector at level 15

Two routes, then an exact proof.

- **From the graph** (`the_sector_at_15.py`): the level-15 graph has the eigenvalue −2.9062796, four times. The central
  element that is +1 modulo 3 and −1 modulo 5 has trace −4 on that eigenspace: the sector is odd at level 3 and odd at
  level 5.
- **As a tensor product** (`the_join_at_15.py`): the three two-dimensional odd sectors of level 3 and the two of level 5
  are cut out of their groups' algebras, and the six joins are formed. Five cancel at 1/√2. One cancels at
  0.893614264: level 3's doublet in which S L has trace 1, with level 5's doublet in which L has trace 1/φ.
- **Exactly** (`the_join_at_15_exact.py`; arithmetic in the field of fifteenth roots of unity): the sum of the two moves
  in that join has characteristic polynomial x⁴ + 2(φ − 1)x³ + (4 − 3φ)x² + 4(φ − 1)x + 4, which is
  (x² + (1/φ + √2 φ)x + 2)(x² + (1/φ − √2 φ)x + 2). The first factor has real roots because
  (1/φ + √2 φ)² − 8 = φ + 2√2 − 4 > 0, which is φ > √2. In the twin the polynomial is the conjugate under √5 → −√5,
  and both of its factors have complex roots.

## 5. The record's triplet

The triplet (B1610's matrices, as B1866 reads them) is a module of the double cover: S² = i on it. By B1 the singular
values of its averaged move are cos 15°, cos 45° and cos 75°, and the determinant has modulus √2/8. Its
characteristic polynomial for L + R is x³ − √2 x² + x + √2; with x = √2 y that is 2y³ − 2y² + y + 1, irreducible over
the rationals, of discriminant −152. The eigenvalues of the averaged move are 0.509336 ± 0.554941 i and −0.311565, so
the rate is 0.753248.

**A thread's factor in the triplet** (`the_triplets_thread_factors.py`; exact, in the ring of 24th roots of unity). The
two moves act on the triplet by a permutation of the three parities with phases, so a thread does too, and its
permutation is its class of harvest row 917. Of the 2,536 threads to length 14, 1,102 are 3-cycles, exactly those of
odd trace, 898 are transpositions and 536 the identity. An odd-trace thread w contributes the factor
1 − det T(w) u^{3|w|}, and det T(w) = (−1)^{|w|} exp(iπ(#L − #R)/4): one number for each thread, which is 1 exactly
when the thread has an even number of letters and as many L as R modulo 8. The product over all of them and the two
letters is 1 − √2 u + u² + √2 u³, to order 14.

The three theta constants in their classical transformation are another module of the same kind:
(x − √2)(x − 1)(x + 1), a rate of exactly 1/√2.

## 6. What it means for the plan, and what it does not show

- **For the root and selection (WP-1.5).** The sum over histories is a product over threads, so a statement about the
  whole is a statement about the product, and a statement about one factor is a thread result. The root's thread is
  the shortest factor with both letters. Nothing in the product marks one factor.
- **For the law and the weight (WP-1.6).** With every history weighted alike nothing concentrates on the modulus
  (B1868). The same unweighted sum does give each sector a rate. So the unweighted law is not empty of numbers; what
  it lacks is a reason to read one sector rather than another.
- **For the swap and the hand (WP-1.4).** The sum over histories is symmetric in the two letters: exchanging L and R
  leaves the sum of the two moves, and so the whole generating function, as it was. So every quantity read from the
  unweighted sum is the same for a sector and for its mirror image, and no hand can be read from it. A hand needs a
  declared bit or a weight that is not symmetric in the two letters; the unweighted law holds neither.
  **More, computed** (`mirror_pairs_of_sectors.py`, 171 sectors of levels 2 to 13): the exchange of the two letters
  permutes the sectors, and on every one of them it is complex conjugation. A sector is its own mirror exactly when
  its character is real; otherwise its mirror twin is its complex conjugate. At a prime level every sector is its
  own mirror exactly when −1 is a square modulo the level (2, 5, 13), and twins exist at 3, 7 and 11: both doublets
  of the golden level are their own mirror, and two of level 3's three doublets are twins. The reason: a thread and
  its reverse are conjugate modulo every level to 13 (224 threads to length 10, no exception), though in the
  moves' group itself they are in general different threads. So the sectors cannot tell a thread from its mirror
  image, and on them the swap and complex conjugation are one involution, not two. This does not pick a sheet.
- **The other clock.** Here a history is graded by its number of moves. Graded by the length of its closed geodesic
  instead, the same product over the same threads is Selberg's zeta function of the level's surface in the sector,
  whose zeros are the eigenvalues of the surface's Laplacian (standard, and cited, not proved here). The state built
  and checked in B1885 is one such eigenfunction. So the record's open question of the clock (register row P-439) is
  the choice between two gradings of one product: the first gives the algebraic rates of this arc, the second the
  Laplacian's spectrum. Nothing here decides between them.
- **Which histories are counted is not free of the record's forks.** With L and R alone each history is counted once,
  as a reduced word: Z1, and the record's own normal form for positive words (B1867, register row P-764). With the
  inverse moves added as separate letters, words that cancel to the same history are counted separately, and the
  rates change: the slowest sector is then a different one at 11 of the 12 levels from 2 to 13. Whether a history is
  its reduced word is the foundation's fork on the moves (GM5b, GM5d), and it is not derived here.
- **Not shown:** that any rate is a mass, a coupling or a lifetime; that the level-15 sector is distinguished among
  all levels (it is not: § 1); a bound on how slowly a sector can cancel as the level grows; the law's sharp form for
  modules of the double cover beyond B1.

## 7. The test that started it, looking back

The owner's test of 2026-11-12 had two parts. Looking forward is §§ 1 to 6. Looking back
(`orbit_closure_of_the_picks.py`, which imports B1869's enumerator unchanged): every set of least departures that the
record's rule gives, on the golden, silver and bronze backgrounds, for every level set, reading of "not detected" and
measure of B1869's run, to 20 letters. There are 88 such sets. Every one is closed under reversal: 27 hold a single
departure that is its own mirror, and the other 61 are unions of mirror pairs and of departures that are their own
mirror. The planted case, a least set with one member of a mirror pair removed, is reported as not closed. So no
pick the record has made by that rule is one member of a mirror orbit.

## Seen first

`python3 scripts/checks/topic_sweep.py` for the zeta functions of the moves, walks that do not turn back, products
over threads and Ramanujan's bound: 29 of 1,643 arcs match in full text and one register row. B423 and B451 hold a
dynamical zeta and a resonance of the trace map on one thread. B1676 holds the mean of the tick's operator over
primitive words. Register row P-369 notes that the thread words are the modular surface's primitive closed geodesics.
B1868 holds the level-5 walk's second modulus, √3/2 eight times, which is the two doublets of level 5 here. None
holds the product over threads, the walk as one that does not turn back, or the law of the rates. For level 15: B355,
B367, B383, B387, B689 and B924 are results on one thread at that level; none concerns the sum over histories.

**The literature:** not searched. Used and named: Amitsur's identity for the characteristic polynomial of a sum of
matrices; the classification of the two-dimensional modules of the three-strand braid group (Tuba and Wenzl); the
theory of two subspaces (Halmos); Ihara's and Bass's relation between a graph's eigenvalues and those of its walk that
does not turn back; Ramanujan's bound for a three-valent graph. That the three-valent graphs of levels 3, 4, 5 are the
tetrahedron, the cube and the dodecahedron is classical.

## Disclosed

- **Main's proposal to the owner that rates would select with no choice was refuted the same hour** by the condition
  main had stated (the survivor changes with the set of moves). This arc keeps the mathematics and drops the proposal.
- **A first report to the owner said that the level-15 sector outlasts every other to level 32.** That is true to 32
  and false beyond: the run to 100 was made afterwards, and he was told.
- **The library's eigenvalue routine failed on the first form of the rate computation** (one impossible value, then no
  convergence): each sector's part of the group algebra holds as many copies as its dimension. The computation now
  cuts out one copy first, and every rate is computed twice.
- **Double precision** for the sectors and the graphs: a rate is given to nine digits and "exactly" is said only where
  § 2 proves it or § 4 computes it in exact arithmetic.
- **Nothing was predicted before it was seen.**

## Reproduce

```
python3 -B frontier/B[[N]]_[[slug]]/verification/orbit_closure_of_the_picks.py
python3 -B frontier/B[[N]]_[[slug]]/verification/rates_by_sector.py
python3 -B frontier/B[[N]]_[[slug]]/verification/the_weaves_zeta.py
python3 -B frontier/B[[N]]_[[slug]]/verification/level_graphs_sparse.py
python3 -B frontier/B[[N]]_[[slug]]/verification/the_join_at_15_exact.py
python3 -B frontier/B[[N]]_[[slug]]/verification/the_braid_law.py
python3 -m pytest -q frontier/B[[N]]_[[slug]]/verification/
```
