# B1602 — PREREGISTRATION: THE FORCED COVER ON EVERY THREAD — the common point's cover on all 74 threads to length eight, read at every sign character of the four: does content follow the arithmetic, the parity class, or the thread?

cc (main), 2026-10-07, after S81. A **weave** arc: every signed thread to length eight (37 words, both signs; SnapPy's
`b+±w`), none chosen, one instrument — the cover the common point forces on each thread (W3: A₄ for odd trace, D₄ when
the act fixes one parity, V₄ when it fixes all three), every kernel of a surjection whose restriction to the fibre is
the parity map, and the four read at every sign character by B1492's stacked index. A *member* is a character with an
interior class (n > 0) — the SM seat's "content", the supply every generation-shaped count needs. **Sealed before any
thread of length six to eight is read, except as disclosed.** No physical quantity. 0 of 19.

## Seen first

`VERDICT topic-sweep /forced cover|A4 cover|tetrahedral cover|congruence cover|sign character|interior class|member/: 94 of 1374 arcs on main match (NEGATIVE 17, OPEN 4, PROVED 72, RETRACTED 1)`
— B1600 (W3), B1601 (the forced A₄ cover is the odd-trace thread's congruence cover at a prime of norm three; the seat's
census rows reproduced at order two on ±LR, ±LLLR), B1492–B1494 (the stacked index, the companions' members),
the SM seat's W6 census, now complete (`the_lines_census.json` @ 52c2f8db5, twelve of twelve at orders 3 and 4: members
on the forced A₄ cover on ±LR only; generations on +LR only), and its W7 (@ 48e9c2200: at a state's resolving tick, members
only on the pair of parities the state's symmetry exchanges — ±LLRR, ±LLR, ±LLLLR — never on all three), read at headline
level before this seal; its W8–W10 and sm:B1552 (sealed, running: the chiral triplet's count) read at headline level, not
used here.

**Seen before the seal, on the instrument:** odd trace — +LR 24 sign members (1, 0, 1), −LR 6 members (4, 0, 4),
+LLLR and −LLLR none (B1601's controls). Even trace — **+LLRR** (arithmetic, tr 6; the act fixes all three parities):
four V₄-kernels, members on every one (5, 6, 6, 27; structures (2, 0, 2), (4, 0, 4), (4, 2, 2), …), interior classes of
the four at the trivial character on three; **+LLR** (not arithmetic, tr 4; fixes one parity): two D₄-kernels, members
on both (11 and 5; (2, 0, 2), (4, 2, 2), (6, 4, 2)), two interior classes at the trivial character on one. **A
hypothesis killed before this seal, disclosed:** "content on the forced cover ⟺ the thread is arithmetic" — LLR is not
arithmetic and carries; so the seat's pattern (content only on ±LR) is a property of the odd-trace covers, where
Theorem G makes content three-or-nothing, not of arithmeticity as such. **Literature:** Johnson–Millson bending (a
totally geodesic surface gives a class in H¹(N; ℝ^{3,1}), the four's untwisted part) and Bader–Fisher–Miller–Stover
(finitely many totally geodesic surfaces on a non-arithmetic manifold) — a candidate mechanism for content, not used,
not tested here.

## Disclosed

The instrument is B1600's `forced_cover.py` generalised (`verification/forced_every.py`): surjections enumerated on
SnapPy's generators; the forced ones selected by the fibre's image (A₄: the composite to ℤ/3 equals the thread's map to
ℤ mod 3; D₄: the fibre lands in a Klein four-subgroup; V₄: the fibre is onto); kernels distinguished by the words to
length five they kill; every kernel read, since the sign choices of the extension τ are not located in SnapPy's
generators — the forced cover is among them. Ranks numerical at 40 digits with B1492's tolerance; sign characters only
(orders three and four not read); SnapPy's `b+-w` is the −w thread. Not blind to the seat's census or to B1601.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **T1** | the eight unseen odd-trace threads of length six (±LLLLLR, ±LLLRLR, ±LLLRRR, ±LLRLRR) carry no member on any forced A₄ kernel | 85% (the seat's complete census at orders 3–4; order two is this arc's) |
| **T2** | the twenty odd-trace threads of length eight carry no member on any forced A₄ kernel | 60% |
| **T3** | every even-trace thread to length eight (42 signed; +LLRR, +LLR seen, 40 unseen) carries a member on at least one forced kernel | 55% |
| **T4** | no odd-trace thread but ±LR has an interior class of the four at the trivial character on its forced cover, and at least half of the even-trace threads do | 60% |

**Reading rules.** T1 ∧ T2 true: content on the forced cover is exclusive to ±LR among odd-trace threads to length
eight — the seat's pattern extended at order two by main's instrument, as a weave census — and, with T3, content is
generic on even trace: the rarity on odd trace is the 3-cycle's (Theorem G: the three lines carry together or not at
all), and ±LR is where three-or-nothing resolves to three. T2 false at a thread: named; the ±LR exclusivity dies at
length eight and the candidate rule becomes whatever the carrier shares with ±LR (checked first: its trace field, its
ideal norm pattern from B1601). T3 false at a thread: the even-trace content is not generic; the carriers listed
against arithmeticity and the parity class. Nothing here is a count of three; the owner's "did we derive three" stays
no.

## Instruments

`verification/forced_every.py`; hashes in `ARTIFACT_HASHES.txt`.
