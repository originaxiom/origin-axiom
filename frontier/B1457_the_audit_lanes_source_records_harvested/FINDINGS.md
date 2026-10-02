# B1457 — THE AUDIT LANE'S RECORDS FROM R32 TO R80 HARVESTED: 116 reports read in full and rowed, its load-bearing algebra re-derived, and one table of what a count needs — an order of the pieces, an open end, and a source or a flux of the right sign — against the objects on which the record has each

**Date:** 2026-10-02 · **Seat:** cc (main) · **Lane:** HARVEST. **Source:** codex's audit lane, pinned at `7b088f50` in a
checkout outside the tracked tree (main's previous pin `5e063851`, 129 commits behind). **Verdict:** PROVED (the
harvest: every item rowed with the lane's own headline first; four re-derivations on this bench, all agreeing).
**Scope:** frame F-HE and the lane's own sourced models · object m004 and its harmonic family, m010, m202, the cone
ends, as each report states · reach single, report by report · hypotheses the lane's, carried with each row. **No
grade of the lane's is raised or lowered without a computation here. 0 of 19.**

## 0. Seen first

- **Repo.** The lane's reports were swept by name over main before being called unread (`harvest_debt.py`: 116 unrowed
  reports and five unrowed relays; main had read the lane through R31 at B1413). `topic_sweep.py "source|sourced|flux
  through|boundary flux|compact core|both cusps|two-cusp"`: *VERDICT topic-sweep: 83 of 1329 arcs on main match
  (NEGATIVE 12, OPEN 6, PROVED 64, no verdict file 1)* (`verification/sweep.txt`). Among them main's earlier harvests
  of this lane: B1302 (the sibling m202, where three appears; R12 to R20 registered as conditional) and B1413 (R21 to
  R31; R27's exact positive on m010 verified in both halves); B1304 rowed its 4d model.
- **The owner's question this harvest answers** (2026-10-02): whether the vacuum test of B1455 was on m004 alone or on
  all allowed relations, and what the lane's conditional vacuum says about a source in other objects.
- **Literature.** Not searched. The lane leans on Corlette, Cooper–Tillmann, Ballas–Long, Braun et al. and
  Pantev–Wijnholt, and says of each what it read; main read none of them for this arc. Nothing below is main's
  statement about those sources.

## 1. What was done

Each of the 116 reports was read in full by one of six reader passes, with the lane's headline and fences quoted
(`verification/readers/`); none was left partly read. Main read itself, in full: R41 (`CURRENT_BALANCE`), R57
(`ROOT_SCOPE_AUDIT`), R76 (`FLAT_VACUUM`), the reception of F01, the premise register, and the seven relays of
2026-10-02. The lane's own tests were run in the pinned checkout (§5). Four pieces of its algebra were re-derived
(`verification/own_checks.py`, with B1455 and B1456):

| the lane's | re-derived here | result |
|---|---|---|
| R41, the flag pairings | K1: tr(ξ_k S) for the complete flag of a rank-four module | (0, 0, 0) for the central direction; (12, 8, 4) for U and (−12, −8, −4) for −U; (3, 2, 1) for E₀₀ − E₄₄; all three vanish exactly on the scalars |
| R47, R48, R54: the q curve under inversion and duality | B1455, two routes; K3 for the longitude traces | (ρ_q∘θ)* ≅ ρ_q and ρ_q* ≅ ρ_{1/q} for every q > 0; traces 3q + q⁻³, 3/q + q³, 3(q² + q⁻²) |
| R57, the natural quotient that forgets order | K2 | q: F₂ → ℤ² commutes with the golden substitution and with the swap on 1 456 words, identifies ab with ba and kills the commutator |
| R78, the signed power | B1456 H4, H7 | −(LR)² is m207; it is the level of no state |

## 2. What a count needs — the lane's results in one table

Every cell is the lane's own statement, quoted or closely paraphrased from the report named, and **read, not
re-derived**, unless marked.

| what is needed | what the lane established | where | its own fence |
|---|---|---|---|
| **an order of the pieces** (a non-split module) | the count lives on the non-split W: "I(W) = −1, I(W dual) = +1, split I = 0"; the split one "admits the inherited harmonic-background construction. The nonzero index above belongs to its NONSPLIT W" | R75; R40 | "not three physical generations in one selected vacuum" |
| **no vacuum without help** | a smooth, complete, source-free, finite-energy flat bundle with an invariant subbundle has an invariant complement; along the non-split direction the potential is a·t² + c·t⁴, a ≥ 0, c > 0, "tending to the split limit" | F01; R76 | "Other actions, sources, physical boundaries, singular metrics and different energy prescriptions have not been excluded" |
| **a source with a direction and a sign** | three balances ∫tr(ξ_k S) = 4∫\|η_k\|² > 0; the central direction pairs to zero "and is the WRONG source direction"; non-central directions pair with the required sign (*table re-derived, K1*) | R41; R80 | "A prescribed positive profile multiplying U is still an external input" |
| **where the source may sit** | "its real residual is smooth and COMPACTLY SUPPORTED … The support need not reach infinity" | R76 | "a constructive localization result, not source dynamics derived from the principle" |
| **or flux through an end** | on a domain with boundary "the negative boundary flux can compensate the positive extension term"; "the verified local cusp and boundary/source route are NOT excluded" | R41; F01; R80 | the allowed flux must be derived "from the same action" |
| **an added source model that works** | "any compact Hermitian trace-free SL5 current can be represented globally by compact fields … Both bulk AND source first variations vanish" | R77 | "infinitely many normalizable positive-kinetic classical flat directions"; "no internal source profile law" |
| **an end law** | at a cone apex the first-order operator is not self-adjoint; 36 boundary classes of signature (18, 18); "No physical handedness is selected" | R68, R72 | "a necessary local linear boundary duty, NOT selection of that half" |

**And against objects** (the lane's counts, each fenced by it as not a physical count):

| object | how it enters the architecture | the count on record | what it lacks |
|---|---|---|---|
| m004, the root, and its harmonic family | the root | zero on every vacuum, by proof (main B1455; the lane's R48 says the same of the classical response) | — it is the uncounted background |
| the same family, non-split | the root | −1 for the ten-type at q = 17 ± 12√2; −3 on levels three and six for a rank-six coefficient induced from the cover (R69, R75) | a source or a flux; "neither a rank nor a deck order is a physical generation count" |
| **m010** | a signed word state (−LLR) | I(V) = 1, I(W) = 1, the exterior square 1 — a ten and a five-bar of one sign (R40; R27 verified on main at B1413) | a vacuum: "an actual positive global background and its normalizable fermion modes are not established" |
| **m202** (two ends) | arithmetic class member, not a cover of the root | a conditional net three with sources on arcs between its cusp ends (R19, R24; "both cusp ends"; "no cusp is privileged") | the sources are "prescribed", not derived |
| a cone end | a completion of a cusp | local profiles; "six seeds are not six particles" (R74) | an end law in the same theory |
| a filling | a relation | flat data descend when the filled slope has trivial holonomy; "geometric handedness is not a four-dimensional fermion index" (R57, the selection-rule intake) | the index does not survive filling by notation |

**The answer to the owner's question, with its grade.** B1455 was on m004 alone. The lane's records say a count is
held only by something beyond the unsourced object, and they name where the record has looked: a second end, a core,
a cone, a cover. **No report derives the source or says which relation supplies it** — every one that touches it
names it as an input still owed. That is read from the lane's reports; the only parts computed on this bench are the
four rows of §1.

## 3. For main, from the lane

- **R78** (signed powers): carried in GENESIS v1.2 and verified in B1456.
- **The act-and-register audit**: its criterion is carried into GENESIS v1.3 at FK12 as the lane's. Its two corrections
  of main's early arcs — B37's detector reads a symbol's presence, not reading-and-branching; B130's empty global
  elimination does not exclude isolated components — are **not checked on main** (lead L243).
- **The boundary-table relay of 2026-09-16**, held on the lane and never rowed on main: the conditional three needs the
  source-arc exterior with both cusp ends, and the three counts — sources removed, split, resolved — must stay
  separate. Rowed here; its mathematics is registered, not verified.
- **Its request for the minimal vanishing statement**: main's candidate is B1297's — a module isomorphic to the dual of
  its pullback by a symmetry of the manifold has index zero — with B1455 as its instance on the SL(4) family. Whether
  it accounts for the zeros on record is lead L242.

## 4. Readers' notes, not each checked by main

In the lane's own files: R69 reports −3 on levels three and six beside R35's received census in which every background
has absolute index one (R35 carries its own caveat); R76's test counts (11, 6 new, 12) are not reconciled in the
report; R44 proves an end with no boundary data while R68 and R72 find apex boundary data on a cone, and the batch
does not say how the two metrics relate; `SOURCE_PROFILE_PROOF` gives a degree-four characteristic polynomial for a
rank-five operator. They are in `verification/readers/` with the place of each.

## 5. The lane's tests on this bench

Run in the pinned checkout, 119 test files (`verification/codex_tests_run.txt`): **1 130 passed, 48 failed, 16 errors, 15 skipped** in 13 minutes. The failures and errors group by library behaviour on this bench rather than by subject: a census file this SnapPy does not carry (8 errors in one file), and four other first errors — a matrix-domain error, an immutable-matrix assignment, a Gaussian coercion and a missing basis bridge — account for 26 more. They were not diagnosed one by one and no scientific conclusion is drawn from them. The lane
reports 24 historical failures retained by design; they are not graded here.

## 6. The fence

Read in full by reader passes; four pieces re-derived. A test that passes here reproduces the lane's finite checks,
which the lane itself says do not certify its continuous arguments. Nothing here promotes a count to physics, and
nothing demotes one. **0 of 19.**
