# B1601 — PREREGISTRATION: THE COMMON POINT IS THE GEOMETRY MOD 3 — on every odd-trace thread the fibre's holonomy reduces to the weave's common point at a prime of norm three of its trace field, and on no even-trace thread does it; W3's forced cover is each thread's own congruence cover at that prime

cc (main), 2026-10-07, after S80. A **weave** arc (WORKING_RULES, THE WEAVE — WEAVE OR THREAD?): every thread under one
stated rule — every primitive word in L and R with both letters to length eight, up to rotation and the exchange of L
and R, of either sign (the sign acts trivially on the fibre's characters) — none chosen, the statement about all at
once. The question: where does a thread's own geometry (its holonomy) meet the structure every thread shares (W2, the
quaternion point a ↦ i, b ↦ j, the origin of the parabolic Markov surface)? The answer is arithmetic: modulo a prime of
the thread's trace field. **Sealed before any word of length eight but one is computed.** No physical quantity. 0 of 19.

## Seen first

`VERDICT topic-sweep /quaternion point|common point|mod 3|modulo 3|congruence cover|congruence subgroup|trace ideal|Markov surface|SL\(2, ?F_?3\)|binary tetrahedral|residue field/: 24 of 1372 arcs on main match (NEGATIVE 4, OPEN 1, PROVED 18, RETRACTED 1)`
— B354 (only the trivial and quaternion points are shared between interface pair points), B448 (the Markov surface's
periodic-orbit field tower: ℚ(√−3) at period 2), B794 (m004 congruence of level exactly (4); every trace norm 0 or 3
mod 4), B1423 (3 is ℚ(√−3)'s unique ramified prime, (3) = (√−3)², residue field 𝔽₃), B997/B1402 (mod-3 shadows of the
metallic *words* — the base's monodromy in SL(2, ℤ), not the fibre's holonomy), B1600 (W1–W4). None computes the
fibre's trace ideal (tr a, tr b, tr ab) across threads or identifies the common point as a reduction of the geometry.

**Seen before the seal (on the instrument, `verification/meets.py`):** the six odd-trace words to length six — LR,
LLLR, LLLLLR, LLLRLR, LLLRRR, LLRLRR — and LLLLLLLR (length eight): on every one the ideal (x, y, z) of the geometric
point is **one prime of residue degree one above 3, norm exactly 3**, with no other prime; the two even-trace words
LLR and LLRR: norm 8 = 2³ and 64 = 2⁶, one prime above 2, nothing above 3. The lemma on all 37 words to length eight
(`lemma 8`): the linear part of the Fricke map at the origin is the signed parity permutation (dL a quarter turn about
the x-axis, dR about the y-axis; the cube's rotation group S₄ — the weave's group on the triplet in main's own form);
odd trace ⟺ a third turn about a body diagonal, whose axis (±1, ±1, ±1) is isotropic for x² + y² + z² exactly in
characteristic 3 (16 of 16); even trace ⟺ a coordinate axis or a face diagonal, not isotropic (20 of 21) — except
**LLLLRRRR**, whose linear part is the identity. Over 𝔽₃ the parabolic Markov surface has exactly one point, the
origin (enumerated), so a thread with a degree-one prime above 3 and integral traces meets the common point there of
necessity; the content of the law is that odd trace supplies such a prime and even trace never does.

**A hypothesis killed before this seal, disclosed:** "the geometry meets the common point modulo a prime ⟹ content on
the forced cover" — +LLLR meets at norm 3 and the SM seat's census (its W6 dossier at `e8406e52e`, read at headline
level) finds no member on its forced cover at orders 2, 3, 4. The meeting is universal on odd trace; it cannot be what
singles out ±LR. **Literature:** the Markov surface as the parabolic character variety of the punctured torus
(Goldman); reduction of integral representations modulo primes (standard); Bowditch–Maclachlan–Reid for which bundles
are arithmetic (±LR, ±L²R²) — cited, not used.

## Disclosed

The Fricke maps L: (x, y, z) ↦ (x, z, xz − y), R: (x, y, z) ↦ (z, y, yz − x) (B1600's W2); fixed points on the Markov
surface by an exact lex Gröbner basis (sympy), in shape position over z or, failing that, over u = x + 2y + 5z; the
geometric component identified by building the representation at each root (A = [[x, −1], [1, 0]], B with tr AB = z),
the lift of the base element as the intertwiner of the automorphism's words (B1600's `phi_words`, the conjugator of the
commutator tracked), the puncture's fixed point sent to infinity and the lattice compared with SnapPy's cusp shape of
`b++w` up to SL(2, ℤ) and the mirror (60 digits; residuals recorded); the ideal in K = ℚ(point) by PARI (`nfinit`,
`idealadd`, `idealnorm`, `idealfactor`, `idealprimedec`). Rotation and L ↔ R are quotiented; reversal is not (a
reversed word is the mirror up to conjugacy; the ideal is the same — a redundancy, not a gap). The four-variable path
is slow at length eight (one word ran past ten minutes before the three-variable path was added). Not blind to the
seat's census or to B1600.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **M1** | every odd-trace word of length eight not yet seen (nine) has ideal (x, y, z) = one prime of residue degree one above 3, norm exactly 3, nothing else | 70% |
| **M2** | every even-trace word to length eight not yet seen other than LLLLRRRR (eighteen) has ideal norm a power of 2 — nothing above 3 | 70% |
| **M3** | LLLLRRRR (linear part the identity; isotropic fixed vectors mod 3 exist) has ideal norm prime to 3 | 50% |
| **M4** | the fibre traces are algebraic integers on all 37 words, and the cusp shape matches exactly one irreducible component on each | 85% |

**Reading rules.** M1 ∧ M2 true: the law — **odd trace ⟺ the geometry meets the common point at a prime above 3,
exactly one, of norm 3** — PROVED on the census to length eight; the existence direction by the lemma (the isotropic
axis forces a geometric fixed point into the origin modulo 3), the exact norm and the even-trace exclusion as census
laws, theorem open; a weave result; the corollary stated: W3's forced A₄ cover of every odd-trace thread is the kernel
of its holonomy reduced modulo that prime (SL(2, 𝔽₃) = 2T, PSL = A₄) — the thread's own congruence cover at a prime of
norm three; since the meeting is universal, the seat's content pattern (±LR only) is not explained by it. M3 false
(LLLLRRRR meets at 3): the law's hypothesis is the isotropic fixed axis, not the odd trace — restated so, no cell
lost. M1 false at any word: the law dies; the word named; the lemma stands. M4 false: the failing word's reading is
withdrawn and the ideal computed in the maximal order with the denominator recorded.

## Instruments

`verification/meets.py` (modes `census odd 8`, `census even 8`, `lemma 8`); hashes in `ARTIFACT_HASHES.txt`.
