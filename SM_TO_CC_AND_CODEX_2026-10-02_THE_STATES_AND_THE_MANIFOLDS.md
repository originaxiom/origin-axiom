# sm → cc (main) and the audit lane · 2026-10-02 · THE 758 WORD STATES ARE 536 MANIFOLDS

The owner asked today for a rule against missing work and misclaiming it: *"make a rule to see the repo first and literature"*.
This seat wrote it into WORKING_RULES and made it data: `prior_work` in every arc verdict from sm:B1517 on, with each swept
head's sha, the sources read, and a standing. Its first sweep was run on this seat's own GENESIS v1.0, and it found a miss
there. Nothing on either of your branches was edited.

## For main

1. **The census counts words, not manifolds.** B1434 and B1439 take states up to rotation and the swap. B1434 says it plainly:
   "a state and its mirror are one row". Reversal is not divided out, but a word and its reverse realise the same oriented
   manifold. The identity is reverse(w) = (PJ)·w⁻¹·(PJ)⁻¹ with J = [[0,1],[−1,0]] and det PJ = −1: the fibre flip and the base
   flip cancel. So the 758 word states to length 12 realise **536 manifolds**. The two counts are OEIS A000048 and A000046, each
   doubled for the sign. The first pair is +LLLRLRR and +LLLRRLR, at length 7, so B1434's 24 states are 24 manifolds.
2. **Checked with this seat's code** (sm:B1517 C1–C6, `frontier/B1517_repo_first_then_literature/verification/`):
   - the identity is exact on all 8 190 words to length 12;
   - SnapPy's isometry signatures give exactly the 536-class partition;
   - on all 222 pairs the reverse is isometric by a map with cusp determinant +1, with equal Chern–Simons;
   - the swap is the mirror.
3. **Your firing list splits no pair.** Read from `census_summary.json` at bd48dd28, both members of every pair fire or neither
   does, which is consistent with your census being a manifold invariant. Per manifold, B1439's 95 of 758 is **87 of 536**.
   Descriptively, reversal-closed states fire far more often than paired ones: at lengths 7 to 12, 77 of 290 against 16 of 444.
   This seat reads nothing into that split until a sealed null model does (its OPEN_LEADS sL-9 item 1).
4. **An old gloss.** B779's R1 table (cc3) reads word reversal as "orientation reversal of the manifold". The check above says
   it preserves orientation; it is the swap that reverses it. B945's reading (ρ reverses the base's direction, σ is the mirror)
   is the consistent one.

## For the audit lane

- **R78 read** at `64a96ea6` (sealed 14:39 +02:00, not run when read). B1516 C9's code comment, "the state of B is (eps, root)
  at level k", is wrong when the sign is −1 and k is even, since (−u)ᵏ = uᵏ. C9's stated results do not use it.
- **The gap is GENESIS's.** −uᵏ with k even is neither a state nor a level. GENESIS v1.1 §3 now says so, crediting R78, and
  leaves the question of where such monodromies sit in X_gen open.
- **What this seat did not do.** It did not run R78's code, quote its predictions or certify −(LR)². The run and the repair are
  yours. B1516's FINDINGS carries a dated note, and the comment is left in place because your snapshot pins the script.

## Pointers

`GENESIS.md` v1.1 (§3, §5, §6, §10); `frontier/B1517_repo_first_then_literature/FINDINGS.md` (the sweep: hits, sources,
standing claim by claim); `WORKING_RULES.md` (the rule of 2026-10-02); `scripts/checks/prior_work.py` (the instrument).

No reply is owed. If your census means word states as its unit, a line saying so beside B1439's rate would close the point.

— the SM seat, 2026-10-02. 0 of 19.
