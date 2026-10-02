# B1517 — SEE THE REPO FIRST, THEN THE LITERATURE: the rule made data, and its first sweep. GENESIS v1.0's 758 states are 536 manifolds (PROVED)

**Date:** 2026-10-02 · **Seat:** sm · **Lane:** governance, and the mathematics of the state space · **Not sealed.** Every
result below is an exact identity or an exhaustive count over a stated finite family, decided at design. The one descriptive
split (C5) is not read here. It goes to the null model that OPEN_LEADS sL-9 item 1 will seal.

---

## 0. The request, and the answer in brief

The owner, verbatim: *"i ljust lets make sure we dont miss any work and misclaim about it. make a rule to see the repo first and
literature"*.

1. **The rule.** WORKING_RULES, the rule of 2026-10-02, SEE THE REPO FIRST, THEN THE LITERATURE, applies before an arc is
   designed and before any sentence says that a result is new, first, absent, ours, or what another work states. It also has a
   row in `docs/PRACTICES.md`.
2. **The instrument.** `scripts/checks/prior_work.py` runs the repo leg on every head and checks the form of the record. Its
   self-test has twelve controls, and they fire in both directions.
3. **The record.** `prior_work` is required in every `arc_verdict.json` from B1517 on, with each swept head's sha, the terms,
   the hits, the literature sources and a standing. `tests/test_arc_verdict_schema.py` enforces its form and refuses novelty
   wording that the standing does not allow.
4. **The first application** swept GENESIS v1.0's own claims and found a miss in GENESIS itself. The 758 states of its census
   are words. **A word and its reverse realise the same oriented manifold, so the 758 states realise 536 manifolds** (§3). The
   identity was within reach in the repo (B945, B134) and in the literature (Goodman–Heard–Hodgson 2008). The base rate the
   next arc was to build on, main's 95 of 758, is 87 of 536 per manifold. GENESIS is amended to v1.1.
5. **The sweep also found** that the audit lane's R78, sealed today, targets B1516 C9's signed-level bookkeeping (§4.1), and
   that an old record misreads word reversal as orientation reversal (§4.2).

## 1. The rule and its instrument

- **Rule text:** `WORKING_RULES.md`, the last section. In five steps:
  1. the repo first;
  2. the literature second;
  3. both legs recorded as data;
  4. no claim beyond what the sweep saw;
  5. a later miss corrected where it stands, credited, logged and relayed.
- **Instrument:** `scripts/checks/prior_work.py`.
  - It runs `absence_sweep.py` on every head, deleted history and the working tree, and `already_banked.py` on the banked
    verdicts.
  - `--json` writes a skeleton record and `--check` validates one.
  - `validate()` is the single definition of a well-formed record; the schema test imports it.
  - The self-test controls: it accepts a well-formed block. It rejects an unknown standing, a head without a sha, a standing
    with no literature queries, a source without a read date, NOT-CHECKED without a reason, and RE-DERIVED resting on nothing.
    The repo leg finds a planted term, reports a fresh nonce absent, and records more than one head with its sha. Its skeleton
    is well formed, and the recorded ref names carry no vendor word.
- **One instrument defect, caught on first use.** The first summary printed "PRESENT (0 files across heads)" for a term found
  only in this arc's uncommitted rule text. The summary now separates the heads, deleted history and the working tree, and says
  when a term is in the working tree only.
- **A second, caught by the attribution gate.** The first record wrote the swept branch names as they are, and some carry a
  vendor word that the repo keeps out of tracked files. The tool now writes that word as "seat", using the gate's own
  encoded list, so the record still names each head and its sha identifies the commit.
- **Schema:** `PRIOR_WORK_REQUIRED_FROM = 1517`.
  - The new `test_novelty_wording_rests_on_the_sweep` refuses certain phrases in a FINDINGS body from B1517 on unless the
    standing is NEW-AS-SWEPT or EXTENDS and literature queries were recorded. The phrases are "novel", "for the first time",
    "not in the literature", "no prior work", "nobody has" and similar; quotations and block quotes are excluded.
  - `test_novelty_check_can_fail` shows the check firing on planted text.

## 2. The first sweep: GENESIS v1.0's claims

### 2.1 The repo leg

Fetched all remotes, then swept nine heads: this branch, main, the audit lane at `64a96ea6`, and the other seats' branches, each
with its sha in `arc_verdict.json`. The terms were "word reversal", "758 signed word states", "A000048", "A000046",
"palindrom", "Goodman" and "up to rotation and swap", plus the IDs and claims of GENESIS.

| hit | where | bearing |
|---|---|---|
| "The states are taken up to rotation and swap; a state and its mirror are one row." | main B1434 FINDINGS (bd48dd28) | the census divides out the mirror; it does not divide out reversal |
| "758 signed word states (length 2 to 12)"; 95 of 758 at their own level | main B1439 FINDINGS and `census_summary.json` (bd48dd28) | the count GENESIS quotes; a rate per word |
| ρ (reverse) and σ (swap) as the bundle's two involutions; GHH's amphichirality criterion | B945 (cc, 2026-08-07), this branch | the repo had the operation that identifies the pairs |
| Goodman–Heard–Hodgson 2008 cited (arXiv:0801.4815) | B134; CLAIMS P34; NOVELTY_AUDIT | the repo had the source |
| "word reversal = orientation reversal of the manifold" | B779 `R1_galois_orbits.md` (cc3) | contradicted by C4 (§4.2) |
| R78: signed powers and cyclic levels, sealed 2026-10-02 14:39 +02:00, not run when read | audit lane `64a96ea6` | tests B1516 C9's level assignment at −(LR)² (§4.1) |
| "A000048", "A000046" | no head; this arc's own working-tree text only | the census counts had never been matched to OEIS |

### 2.2 The literature leg

Queries: OEIS for the necklace counts; "Goodman Heard Hodgson commensurators punctured torus bundles"; "Guéritaud canonical
triangulations once-punctured torus bundles"; "Gieseking manifold punctured torus bundle monodromy"; "first homology mapping
torus coker".

| source | where | read | what it states |
|---|---|---|---|
| OEIS A000048 | the sequence | 2026-10-02 | n-bead necklaces, 2 colours, primitive period n, no turning over, colours interchangeable: 1, 1, 2, 3, 5, 9, 16, 28, 51, 93, 170 at n = 2 to 12 |
| OEIS A000046 | the sequence | 2026-10-02 | primitive n-bead necklaces, turning over allowed, complements equivalent: 1, 1, 2, 3, 5, 8, 14, 21, 39, 62, 112 at n = 2 to 12 |
| Goodman, Heard and Hodgson, "Commensurators of cusped hyperbolic manifolds", Experimental Math. (2008), arXiv:0801.4815 | §3, Lemma 3.2 and Theorem 3.1 (read on ar5iv) | 2026-10-02 | each φ ∈ SL(2,ℤ) is conjugate to ±φ_w with w determined up to cyclic permutation; the monodromy triangulation has one tetrahedron per letter and is canonical (from Lackenby); symmetry types include a palindromic word (a rotation by π) and a word whose reversal swaps L and R (a glide reflection) |
| Guéritaud, "On canonical triangulations of once-punctured torus bundles and two-bridge link complements", Geom. Topol. 10 (2006) | Prop. 2.1; §3.2 (ar5iv) | 2026-10-02 | the word is unique up to cyclic permutation; a word of period m gives m ideal tetrahedra |
| Chun, Gukov, Park and Sopenko, "3d-3d correspondence for mapping tori" (2019), arXiv:1911.08456 | §2.2, eq. (11) (ar5iv) | 2026-10-02 | H₁ = ℤ ⊕ coker(φ − 1) for genus-one mapping tori, b₁ by trace |
| Wikipedia, "Gieseking manifold" | the article | 2026-10-02 | a once-punctured torus bundle with monodromy (x, y) ↦ (x + y, x); double cover the figure-eight knot complement; H₁ = ℤ; it cites Adams (1987) for minimal volume, which was not opened |

### 2.3 Standing, claim by claim

| GENESIS v1.0 claim | repo | literature | standing |
|---|---|---|---|
| §3: 758 states to length 12 | main B1439; B1516 C4 | OEIS A000048, doubled | KNOWN (a classical count), credited in v1.1 |
| §3: each state "is realised as" a bundle | — | GHH Lemma 3.2 and Theorem 3.1 | **incomplete in v1.0**: the realisation is two-to-one on 222 states (§3); amended |
| §3: a word of length n gives n ideal tetrahedra | B1516 C5 | GHH Lemma 3.2; Guéritaud §3.2 | RE-DERIVED, credited in v1.1 |
| GM2: every hyperbolic class is ± a cyclic word | B1516 C9 | Guéritaud Prop. 2.1; GHH Lemma 3.2 | RE-DERIVED |
| T-ROOT's torsion formula | B1516 C2 | CGPS eq. (11) | RE-DERIVED, credited in v1.1. The selection "exactly m004 and m000" is derived here from it; no source read states it in that form, and it is not claimed new |
| m000 is the bundle of LP, and m004 its orientation double cover | B1516 C5, C6 | Wikipedia, "Gieseking manifold" | KNOWN |
| m004's level torsion 1, 5, 16, 45, 121, 320 | B1516 C6 | not searched in this sweep | NOT-CHECKED |
| the independence witnesses (C8) and "four inputs suffice" | B1516 C1, C8 | not searched in this sweep | NOT-CHECKED; not claimed new |
| §3 levels: the n-fold cover of (ε, w) is (εw)ⁿ | B1516 | — | correct; R78 shows the signed bookkeeping around it is incomplete (§4.1) |

The NOT-CHECKED rows are the sweep's honest reach. GENESIS claims neither of them as new.

## 3. The finding: a word and its reverse are one manifold (C1–C6)

**Statement.**
- For every word w in L and R, reverse(w) = (PJ)·w⁻¹·(PJ)⁻¹, with P = [[0,1],[1,0]], J = [[0,1],[−1,0]] and det PJ = −1.
- So the bundles of εw and ε·reverse(w) are homeomorphic, preserving orientation. Conjugation by PJ reverses the fibre's
  orientation and inversion reverses the base's, so the composite preserves both together.
- The swap, swap(w) = PwP with det P = −1, gives the mirror image.
- GENESIS's census divides out the swap but not reversal. So **its 758 states realise 536 manifolds**: twice OEIS A000048
  (758) against twice OEIS A000046 (536).

**Proof of the identity.** Write Lᵀ = PLP = R and Rᵀ = PRP = L. Then wᵀ is P·reverse(w)·P, and wᵀ = J·w⁻¹·J⁻¹ for det w = 1.
C6 checks the identity exactly on all 8 190 words of length 1 to 12.

**Checks** (`verification/census_by_manifold.py`; run record `census_by_manifold_run.json`; about 4 s with SnapPy 3.3.2):
- **C1.** 758 word states, per length 1, 1, 2, 3, 5, 9, 16, 28, 51, 93, 170 (unsigned). This is OEIS A000048, and an own
  Möbius formula agrees.
- **C2.** Up to rotation, swap and reversal there are 536 classes, per length 1, 1, 2, 3, 5, 8, 14, 21, 39, 62, 112: OEIS
  A000046. Every class has one or two states, and the 222 pairs are each a word and its reverse. The first pair is at length 7:
  +LLLRLRR and +LLLRRLR. Below length 7 the census and the manifolds coincide, so B1434's 24 states are 24 manifolds.
- **C3.** SnapPy's isometry signatures of all 758 bundles give exactly 536 manifolds, and the partition is C2's. No signature
  failed.
- **C4.** On all 222 pairs:
  - the reverse is isometric by a map whose cusp maps have determinant +1, and Chern–Simons agrees mod 1/2;
  - the swap admits a determinant −1 isometry, and Chern–Simons is negated mod 1/2;
  - on 220 of the pairs the swap admits only orientation-reversing isometries; the other two manifolds are amphichiral.
- **C5.** Main's B1439 firing list (93 states at lengths 7 to 12, quoted in `main_B1439_firing_own_states.json` with its
  source) splits no pair: both members of a pair fire, or neither does. That is consistent with main's census being a manifold
  invariant. Per manifold, main's 95 of 758 word states (12.5 %) is **87 of 536 manifolds (16.2 %)**. Descriptively, at every
  length from 7 to 12, reversal-closed states fire far more often than paired ones: 77 of 290 against 16 of 444 (8
  manifolds). This is not a test. A null model has to take it as an input (sL-9 item 1).
- **C6.** The identity above, exact, with det PJ = −1 and Lᵀ = PLP = R.

## 4. Two more things the sweep found

### 4.1 Signed powers, and B1516 C9's comment (the audit lane's R78)

The audit lane sealed R78 at 14:39 +02:00 today (`64a96ea6`). It tests whether reducing a signed monodromy to "its unsigned
primitive root, with the sign attached to the root, at level k" reconstructs every signed monodromy as a cyclic cover. Its test
case is U = −(LR)².

B1516 C9's code carries exactly that assignment, in a comment: "the state of B is (eps, root) at level k". The assignment is
wrong when the sign is −1 and k is even, since (−u)ᵏ = uᵏ. C9's stated results do not use it: it asserts only that every
hyperbolic class is ± a positive word, and that every level-1 word is a census state.

The gap the comment hid is GENESIS's. For u primitive and k even, −uᵏ is a legal signed monodromy that is neither a state nor a
level. GENESIS v1.1 §3 says so and leaves its place in X_gen open. R78's sealed run, including its geometric certification of
−(LR)², is the audit lane's. This arc does not run it and does not quote its predicted outcomes. B1516 FINDINGS carries a dated
note, and ERROR_LEDGER has a row.

### 4.2 B779's parenthetical

B779's R1 table (cc3, July) glosses θ as "word reversal = orientation reversal of the manifold". C4 contradicts that: on every
pair the reverse is orientation-preservingly isometric, and it is the swap that reverses orientation. B945's reading stands. In
it ρ reverses the base's direction (the flow's time) and σ is the mirror, and the two compose to the orientation-reversing
symmetry that GHH's criterion detects. B779's record is not edited here. The relay carries the note.

## 5. What changed

- `GENESIS.md` v1.1:
  - §3: the reversal identity, the 536 manifolds with the OEIS credits, the tetrahedra credit and the signed powers;
  - §4: T-ROOT's formula credited;
  - §5: the per-manifold rate;
  - §6: a count names its unit, and arcs from B1517 carry `prior_work`;
  - §10: the version log.
- `tests/test_b1516_genesis_v1.py` now pins the head line by form and v1.0 by its log entry.
- README: the census sentence says 758 states and 536 manifolds.
- Notes and ledgers:
  - B1516 FINDINGS: a dated note at C9;
  - OPEN_LEADS sL-9 item 1: rates name their unit, and C5's split is an input;
  - ERROR_LEDGER: two rows;
  - one relay to main and the audit lane;
  - RELAY_LEDGER: the audit lane read at `64a96ea6`;
  - the alias table, the campaign board and the logs.

## 6. What is not claimed

- **Nothing here is new mathematics.** The identity is classical in substance. It is the GL(2,ℤ) classification of
  punctured-torus bundles, which GHH's symmetry types reflect. The counts are OEIS's. The arc's contributions are the rule, the
  record, and finding that GENESIS's census line had missed the identity.
- **C3 is numerical.** It uses SnapPy's canonical retriangulations, without interval verification. The partition also follows
  from C6 and the classification, but the general "no other coincidence" is that classification, which this arc cites and does
  not re-derive beyond length 12.
- **C5's split is descriptive.** It is not evidence of anything until a sealed null model reads it.
- **R78's outcome belongs to the audit lane.**

## 7. Files and locks

- `verification/census_by_manifold.py`: C1–C6, with `--snappy` for C3 and C4.
- `verification/census_by_manifold_run.json`: the run record.
- `verification/main_B1439_firing_own_states.json`: main's list, quoted with its source and sha.
- `scripts/checks/prior_work.py` (the instrument), `tests/test_arc_verdict_schema.py` (the schema and the wording check), and
  `tests/test_b1517_repo_first_then_literature.py` (the lock).

I-26 stays UNEARNED. 0 of 19.
