# The repository, swept: has the chain been enriched, and have the axioms been reduced?

*Outside referee, 2026-10-01. Requested by the owner: "swipe the repo once more and other branches,
check all existing work before you conclude." Every branch on `origin` was fetched today and read
against `main`. Every mathematical claim below that changes a count was re-derived with my own code
(`referee_2026-09-17/scripts/r14_axiom_checks.py`, exit 0). Ledger counts were recounted row by row
from each branch's own files. Where I only read a result, §7 says so.*

---

## 0. The answer

**The chain has been enriched in depth. It has not been enriched in reach. The axioms have not been
reduced.**

- **Axioms: four, on every branch** — C3 (being is inexhaustible description), C4 (the geometric
  carrier), C5 (orientation) and C18 (the observer's closings). No lane derives any of them.
- **One fork was re-graded, on one lane.** The SM-derivation lane proves the *puncture* follows from
  the carrier axiom (B1380). On that lane's route the entrance has one fragile fork, orientation,
  where main's paper prices two. I verified the theorem. It re-grades a fork inside C4; it does not
  remove an axiom. On the uniqueness theorem's route the puncture stays a declared choice.
- **The price went up by one bit, on the same lane.** B1382 shows the spin lift is *not* assigned by
  the object. It is traded for the parent manifold's Pin type: main's freedom ledger counts this bit
  as 0, the SM lane as 1. I verified the core computation exactly. Main's paper also disagrees with
  itself on this bit (§4).
- **Inputs for a physical reading: unchanged at 4 + 8 = 12 on main.** The SM lane states 4 + 7 = 11.
  That is because its ledger forked on 2026-09-06, before main added four rows; it is not a
  reduction. No UNEARNED identification became EARNED on any branch since 09-17. The one new EARNED
  row (sep16's I-31) is mathematics on both sides, so it reduces no physical input.
- **Standard-Model parameters bought: 0 of 19, on every branch.** The SM lane's own document of
  today says it directly: *"There is no path to the full Standard Model with its 19 numbers in
  sight."*
- **The biggest structural fact is divergence.** `main` has not moved since 2026-09-18. Four active
  lanes hold about 300 commits main has not read (§1). The two verified re-gradings above are relayed
  to main but not applied. Until they are, the paper and the record say different things.

---

## 1. What was swept

Heads as fetched on 2026-10-01. "Past pin" counts commits beyond the commit main's harvest ledger
(`docs/HARVEST_LEDGER.md`) records as last read for that seat.

| lane | head | last commit | unique vs `main` | main's pin | past pin |
|---|---|---|---|---|---|
| `main` | `987c0c8f` | 2026-09-18 | — | — | — |
| `claude/standard-model-derivation-0qt6ao` (seat `sm`) | `76d98eba` | **2026-10-01** | 153 | `f17dd84e`, 09-16, "through sm:B1365" | **78** — 42 new arcs, B1366–B1399 and B1500–B1507 |
| `sep16-branch` (seat `xb`) | `3205984b` | 2026-09-29 | 98 | `c052c857`, the merge base — *"none of it has been read"* | **98** — xB001–xB034 |
| `audit/physical-bridge-2026-09-05` | `c17d8500` | **2026-10-01** | 205 | `5e063851`, 09-15, after R30 | **100** — R31–R70 |
| `claude/paper-review-verification-kaz3f5` (this review) | `013c9ac7` | 2026-09-29 | 21 | `21c47a51`, registration only | 21 (unique) |
| `claude/outside-bench` | `13d2c5b6` | 2026-09-18 | 14 | `8262c6ed`, "memos through 233" | 14 — memos 234–236 |
| `claude/physics-seat-evaluation-8dkbrl` | `659487bb` | 2026-09-06 | 165 | `659487bb` | 0 |
| retired seats (tags `archive/codex-seat-r001`, `cc3-paper-lane`, `braver-questions`, `qor5up`) | — | ≤ 09-15 | — | pinned at retirement | 0 |

The audit lane moved today (R70, below). Nothing else changed since my first pass of this sweep. No
lane is a superset of another. The SM and audit lanes do not merge `main` (590 and 610 of main's
commits are absent from them). sep16 is 16 commits behind `main`.

---

## 2. Axioms: the count, and how they are graded

| entrance item | `main` (paper §axioms, chain table) | SM lane | checked here |
|---|---|---|---|
| **C3** description | AXIOM, priced robust (F2, F4) | unchanged | — (not a mathematical claim) |
| **C4** carrier | AXIOM, geometry-necessary (F8) | unchanged, and now also carries the puncture | — |
| **puncture** (P019 A5b, fork F6) | **fragile fork**, one of two (*"Two fragile forks … orientation … puncture"*) | **implied by C4 = A5 on the words route** (B1380, 09-26); still declared on the uniqueness theorem's matrix route | **holds** — r14 (1) |
| **C5** orientation (A6, fork F5) | fragile fork | *"now the one fragile entrance axiom"*; it overrides minimality (the Gieseking manifold is the least-volume cusped hyperbolic 3-manifold) and *"is the choice that builds the walls"* (B1234) | the volumes match SnapPy: m000 at 1.0149416064 is least among the first 200 non-orientable census manifolds, and m003/m004 are exactly twice it. Global minimality is Adams 1987, cited. B1234's census not re-run |
| **A7** order bit (uniqueness route only; not in the paper) | main's B979: *"A7 is based-level"* | B1379 S4, B1504 T1: an orientation-preserving change of marking swaps LR and RL | **holds** — r14 (2) |
| **C18** observer's closings | AXIOM | unchanged | — |

**The count is four everywhere**, in main's chain document (`AXIOM | 4`), in its paper (*"The
invariant is four"*), in the SM lane's chain document and on sep16.

**What B1380 proves, and what it leaves.** The four surfaces with fundamental group F₂ are the
thrice-punctured sphere, the once-punctured torus, the twice-punctured projective plane and the
once-punctured Klein bottle. No closed surface has that group. A homeomorphism realising σ (or σ²)
has a power that fixes every boundary class up to sign. If any boundary class were nonzero in H₁,
that power of σ's abelianisation would have eigenvalue ±1. Its eigenvalues are φ and −1/φ, so none
does. Only the once-punctured torus, where the boundary is a commutator and vanishes in H₁,
survives. My r14 (1) checks the four surfaces and the eigenvalue step. The argument is basis-free,
and the theorem holds.

The premise it leaves is the one B1380 names: the carrier's group is F₂ itself, not a quotient.
This is argued from C3 and B1379's "no unforced collapse". A reader who lets the carrier carry only
the letter counts recovers the closed torus bundle, which is fork F6's sibling. So the puncture fork
becomes part of C4's statement rather than a separate choice. The four-axiom count does not move.

**What B1379/B1504 prove about A7.** L⁻¹(LR)L = RL with det L = +1. SnapPy finds 8 isometries
b++LR → b++RL, 4 of them orientation-preserving (r14 (2)). So the order bit does not choose the
oriented object. Main's record already said this at the unbased level (B979). The SM lane adds the
explicit orientation and the consequence that no datum at a cusp point can depend on A7.

**What did not happen.** No lane derives C5. B1384's generated state space keeps the Gieseking state
*"in the pre-selection architecture … not shown absent"*. B1380's addendum sharpens the weakness
rather than closing it: minimality, the principle that selects at C1 and C2, would choose the
Gieseking manifold at C5, and C5 overrides it. No lane touches C3 or C18.

---

## 3. Inputs for a physical reading — the identification ledgers

| branch | rows | EARNED / UNEARNED / REFUTED | irreducible sources | axioms + irreducible |
|---|---|---|---|---|
| `main` | 30 | 8 / 14 / 8 | **8** — outside-bench memo 223's certificate re-runs B1266's union-find on the live ledger | **4 + 8 = 12** |
| SM lane | 26 | 8 / 10 / 8 | 7 — its `THE_SM_VERDICT.md`, restated by B1507 today | 4 + 7 = 11 — **a fork artifact**: the lane forked on 09-06 and lacks I-27, I-28, I-29 and I-30, which main raised on 09-07 to 09-09 |
| sep16 | 33 | 9 / 16 / 8 | not recomputed by anyone | at least 12 |

Counted row by row from each branch's `docs/IDENTIFICATION_LEDGER.md`; they match each branch's
`IDENTIFICATION_BASELINE.json`.

**Rows that moved anywhere since 09-17:**

- **I-31 (sep16, EARNED):** *the monodromy's order-3 action at the node ≡ 2T/Q₈.* Verified, r14 (3).
  The map (i, j, k) ↦ (k, i, j) is an automorphism of Q₈ on all 64 products, of order 3, and outer.
  The trace map's derivative at the node is the row's matrix D, with D³ = I. Both sides are the
  object's own mathematics, so this earns no physical input. Its own addendum withdrew the claim that
  the four ℤ/3s are all linked; the arithmetic μ₃ is independent. Minor: the row's note says
  "EARNED 4 → 5", a stale running count; the table has 9 EARNED rows.
- **I-32 and I-33 (sep16, UNEARNED): both are debts from my own round-3 report.** See §8.
- **I-14 (generation grading):** narrowed from 85 candidate gradings to 1. The physics seat's R68
  found this and B1507 re-verified it. The row stays UNEARNED: a smaller menu is not a derived choice.
- **I-26 (a physical vacuum carrying a chiral generation):** still UNEARNED. It is the SM lane's
  first missing bridge (§6). B1500–B1505 show that, in the frames used, the end's chirality is an
  input. The audit lane's R60/R61 limit B1504's broadest sentences to real and root lines. B1507
  records that correction.

**No UNEARNED row was earned on any branch.** That is the direct answer on inputs. The audit lane
keeps an older 24-row copy of the ledger. Since main's pin it has changed no row's status; its added
path-local notes say so themselves (*"No shared I-number or physical status is reassigned … This
does not earn I-10, I-13 or the boundary-count-to-physical-chirality identification"*).
outside-bench's copy is main's, unchanged.

---

## 4. Freedoms: the spin bit went up, not down

Main's paper says two things about the spin lift:

- §ledger, prose: *"What is not yet done is the identification of that selected lift with the sign
  lift selected by the object's spectral period … until it is, the bit is assigned by the extension
  route and the two routes are not yet shown to agree."*
- the claims table: *"the spin lift is assigned by the object's own spectral period, not free —
  settled — lock."*

**These disagree with each other**, inside one manuscript.

The SM lane ran the missing comparison. It is B1175's residual, queued on 08-27 and never run on
main. **B1382 (09-26)** finds that the extension route selects B1141's lift only within Pin⁺; within
Pin⁻ it selects the other lift. m004's two spin structures are exactly the pullbacks of the Gieseking
manifold's Pin⁺ and Pin⁻ structures, one each. So the object does not assign the bit; it trades it
for the parent's Pin type. B1382 says so in its header: *"the freedom ledger's spin bit goes back
from 0 to 1."*

**Verified here** (r14 (4), exact arithmetic in ℚ(ω)):

- the holonomy satisfies the relator, and so does its sign lift; a mixed lift does not;
- the intertwiner equations have rank 3, so W is unique up to scale;
- W·W̄ = +A, so a lift sending a ↦ +A extends only into Pin⁺ and a ↦ −A only into Pin⁻;
- the topological precondition: the Gieseking manifold has H₁ = ℤ and χ = 0, so H²(·; ℤ/2) = 0 and
  both Pin types exist; the cover acts as ×2 on H₁, so each type pulls back to exactly one spin
  structure;
- the cusp traces (2, −2) of B1141's lift.

**B1383 (09-26)** then quotes physics to fix the Pin type: Witten, arXiv:1508.04715 (T² = (−1)^F ⟺
Pin⁺), and Freed–Hopkins, arXiv:1908.09916 (M-theory is Pin⁺). It finds that the bit relocates a
second time, to the role the parent's deck plays: gauged, or as the Standard Model's CP. *"The
freedom ledger's spin bit stays at 1."* I did not re-read those two sources in this sweep.

**Net:** on the SM lane the price is one bit higher than main's claims table states, and the lane
records this honestly. My working notes from the first pass of this sweep read it as "freed"; that
was wrong (§8).

---

## 5. The chain: enriched in depth, not in reach

**`main`** — 57 links: 36 theorems, 6 identities, 8 no-gos, 2 censuses, 1 corollary and the 4
axioms; *"fifty-three of fifty-seven are forced"*. Unchanged since 09-18.

**SM lane** — 42 new arcs since main's pin. I read every arc's header. Each records the price as
unchanged, except B1382, which raises the spin bit from 0 to 1, and B1383, which keeps it at 1. The
table gives what each group claims; §7 says which I checked.

| theme | arcs | what they claim |
|---|---|---|
| the Standard-Model frame | B1366–B1373 | the Standard Model sits in E₆ one way up to conjugacy (B1366, the same result as main's B1430; B1507 notes its short form drops the SM-shaping condition B1430 found necessary); a doublet–triplet pairing (B1367); the object's own SM-unbroken flat connections put their non-abelian part in SL(2)_β (B1368); bulk chirality with the Standard Model unbroken needs a free cusp (B1369–B1373) |
| the index on the tower | B1374–B1378, B1381 | one generation on the object's own tower, at most one per background (B1374, B1375, B1377); no cyclic cover has a rank-one character with h¹ = 2 (B1381); the M6 deck triplet, three-generation-shaped (B1378). B1376 independently agrees with main's B1419 on the arithmetic fillings, which main had already corrected in the paper |
| the entrance | B1379, B1380, B1384, B1385 | genesis audit (A7 based-level; C2 locked; the m010 ratio ladder); the puncture theorem; the generated state space, with m004 as its root and only m004's commensurability class reaching it |
| the spin bit | B1382, B1383 | §4 |
| cusps, ends and chirality | B1386–B1390, B1392, B1393, B1395, B1396, B1500–B1505 | a count of ±2 on an open Eisenstein cusp (B1386, B1387), retired by its own sealed cutoff test (B1388: *"UNSTABLE"*); the ends carry the chirality, and a free cusp is charge-blind at finite energy (B1392, B1395); the end's chirality is an input, no symmetry forces a chiral end, and no known local G₂ model supplies one (B1500–B1505) |
| the three | B1391, B1394, B1397–B1399, B1506, B1507 | the frame cannot give three generations (B1398), and neither can a rank-two Higgs (B1399, sealed: none). B1378's triplet is the deck orbit on s961, the root's only 3-fold cover (B1506): **three vacua with one generation each, not three families in one vacuum.** The fence is July's B521 Gate C and the idea is July's B335 (B1507). I-14: 85 → 1 |
| the verdict | `THE_PATH_TO_THE_SM_2026-10-01.md` | §6 |

The lane's chain document still carries its 09-06 census (43 links, 26/5/6/1/4/1). It adds dated
annotations to C4 and C5 and the generated-state-space convention. It also still reads
*"Currently TWO (the two hierarchy ratios)"* in Part 0, a count main corrected on 09-17. Both are
fork artifacts.

**sep16** — 34 arcs, xB001–xB034. Highlights:

- the node's ℤ/3 (xB005 → I-31);
- the sum of the negatives (xB021: the orientation and order bits are the stabiliser of the object's
  Chern–Simons value);
- my round-3 report re-verified (xB025, which routed I-32 and I-33);
- a G₂-MSSM read (xB029);
- a cross-branch audit (xB034), which corrected four of the seat's own claims of absence.

**audit lane** — R31–R70, conditional results on action and domains at the cone completion of the
cusp. Each is "path-local" and certifies no physical identification. Today's R70: zero-trace bosons
and self-adjoint bulk fermions cannot share a domain under both adopted supercharge profile maps;
finite-action positives exist but change peripheral data; *"No universal chirality kill."*

**outside-bench** — memos 234–236:

- memo 234, the supplied literature read, with four addenda; its own bench error #38 corrects two of
  its "pre-emptions", which were arcs citing the literature rather than claiming it;
- *the assumption ledger*: its A1–A9 are conditions of the G₂-MSSM package, not the uniqueness
  theorem's A1–A7. Its frame reaches only m004, and its A4 (Joyce–Karigiannis needs b₁(Q) > 0)
  fails there: b₁(Y₃) = 0;
- *"the paper already had it"*: all four conclusions were already in the paper.

**Depth versus reach.** In two weeks the record gained real theorems: the carrier theorem, the
Pin-type theorem, the deck orbit on s961, the end-choice theorems. It also gained many careful
corrections of its own earlier statements, and sealed tests that retired its own positives (B1388).
Every one of them sharpens where a boundary is. None of them moves a physical number across it.

---

## 6. The record's own verdict

The SM lane wrote it today (`docs/THE_PATH_TO_THE_SM_2026-10-01.md`), and it agrees with everything
above:

> *There is no path to the full Standard Model with its 19 numbers in sight, and the record's own
> theorems say why: the object fixes priors, not points. There is a path to the Standard Model's
> qualitative content … It needs three bridges the record does not have, and two of them are
> blocked by theorems in the frames the record uses.*

The three bridges:

1. a physical vacuum carrying a chiral generation (I-26);
2. three families in one vacuum (the record's three is an orbit of vacua);
3. the values.

The lane names three changes of premise that could reopen a path, each with a decisive test. Route A,
making main's index physical as a boundary count, is announced as B1508, to be sealed before it runs;
it is not on the branch yet. What it
calls honestly reachable is the Standard Model's structure plus *"the chirality sign, the level bit,
the vacuum direction, the scale and the end datum"*, with 0 of 19 values.

---

## 7. What I verified, and what I only read

| verified with my own code | read only |
|---|---|
| **this sweep (r14):** B1380 carrier theorem; LR/RL oriented isometry, 8 and 4 (B1379 S4, B1504 T1); I-31 including the trace-map Jacobian; B1382's sign law, intertwiner rank and topological precondition | B1383's physics (quoted from Witten and Freed–Hopkins; not re-read here); B1234 (orientation ⟹ amphichirality, 40/40 census) |
| **earlier rounds, relevant here:** B1430's three hypercharges, exhaustive (r13), which is also B1366's content; B1431's separation and its invariance (r12, r12b, GHRS Thms 1.2–1.4); xB021's group theory; E₆: 120 A₂ in one Weyl orbit, 720 commuting (A₂, A₁) pairs in one orbit; the tower identities and h¹(χ²) = 1 at every non-split locus, which B1374/B1375 build on | the runs of B1367–B1378 and B1381; B1384–B1399; B1500–B1506 (G₂ cones, the apex index rule, s961's deck orbit); B1507's re-verifications of the physics seat's R64 and R68; sep16 xB001–xB034, apart from I-31 and xB021; audit R31–R70; outside-bench memos 234–236 |

Everything in the right-hand column is reported as the record states it. No count in §0 rests on it
alone.

---

## 8. My own errors, found by this sweep

1. **I-32 is mine.** Round 3 (09-18) wrote: *"the two bits the manuscript calls withheld and
   relational are exactly the object's own stabiliser."* The structural half is xB021's and is
   verified: {A6, A7} fix CS = 0. The identification with the manuscript's vocabulary was mine, and
   I exhibited no map. xB021's own verdict file records `identifications: []`. sep16 rightly carries
   it as UNEARNED. **I withdraw it.** The consolidated report carried the same sentence in F1 and §4;
   both are corrected in place today.
2. **I-33 comes from my round-3 phrase** *"(pending B1366) a unique Standard-Model embedding."* What
   is now established: for regular embeddings with the Standard-Model shaping of the 27, the
   embedding is unique up to W(E₆). That rests on B1430 and my exhaustive r13. All Cartan
   subalgebras are conjugate and every Weyl element is realised in the adjoint group, so it is also
   unique up to inner automorphism; the row's gap (c) does not weaken uniqueness. What is open, as
   the row says: non-regular A₂ (gap (a)), and how this reconciles with B1415, which I have not read.
   The row should be updated, not closed.
3. **The spin bit.** My first-pass notes read the SM lane as having freed it. It raised it from 0 to
   1 (B1382), and B1383 kept it at 1.

The first is the same failure the paper's ledger exists to catch: an identification asserted
because two sets have the same size. That it came from the referee does not change its class.

---

## 9. What follows

1. **Harvest before anything else.** Main is 13 days behind four active lanes. Two re-gradings
   verified here are relayed but unapplied: B1380 (§2) and B1382 (§4). Until they land, the paper
   prices two fragile forks and a settled spin lift, while the lane where the work was done says one
   and one bit.
2. **If harvested, the paper changes in two places:**
   - §axioms states both routes: on the words route one fragile fork; on the uniqueness theorem's
     route two. This is B1380 §6's own suggestion.
   - The spin-lift claims row and the §ledger paragraph are reconciled, to "traded for the parent's
     Pin type; one bit".
3. **One ledger, recounted.** Merge sep16's three rows into main's ledger. Close I-32 as withdrawn by
   its source. Update I-33 with the regular-embedding result. Then re-run the irreducible-source
   certificate on the merged ledger. Retire the SM lane's "4 + 7 = 11", which is a fork artifact.
4. **The headline does not change:** four axioms; at least twelve inputs for a physical reading; 0 of
   19. The enrichment is real and worth reporting, as structure, fences and theorems, not as
   reduced price.

---

*Reproduction: `python3 referee_2026-09-17/scripts/r14_axiom_checks.py` (SnapPy 3.3.2; about ten
seconds). Branch heads in §1 are from `git fetch --all` on 2026-10-01. The consolidated referee
report is updated in place to match: F1's row and §4's sentence corrected, F8 added, §5 and §7
extended.*
