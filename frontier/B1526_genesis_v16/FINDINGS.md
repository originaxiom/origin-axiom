# B1526 — GENESIS v1.6: MAIN'S v1.5 (THE OWNER'S TWO DECISIONS) AS THE HEAD, THE SM SEAT'S v1.5 ANSWERED BY ITS LINE, AND B1297'S P SHOWN TO BE THE FIBRE'S ELLIPTIC INVOLUTION

**Date:** 2026-10-03. **Verdict: PROVED.** Five checks, C1–C5 (`verification/genesis_v16_checks.py`, 15 s), all pass.
- All five were run and passed before GENESIS.md was written. The pre-write log is kept (`genesis_v16_checks_prewrite_run.txt`).
- The run after writing (`genesis_v16_checks_run.txt`, `genesis_v16_checks.json`) adds one fact: GENESIS.md is the generator's
  output, byte for byte.

**Not sealed.** Each check reads a banked record, re-derives a fact the record already states, or compares texts. No open
outcome is computed. **creates_law is false.** 0 of 19 Standard-Model parameters; I-26 stays UNEARNED.

**Source.**
- **Main's ask.** Its relay of 2026-10-03 (`CC_TO_SM_AND_CODEX_2026-10-03_GENESIS_V1_5_FK1_CONFIRMED_FK12_THE_REGISTER.md`,
  kept as received in `received/`): *"Please take v1.5 as head"*, and *"Nothing asked of either seat beyond taking v1.5 as
  head."*
- **The owner's two decisions**, as main records them (B1460, quoting the owner's *"i aprove your recomendation"*):
  - GENESIS FK1 is CONFIRMED as written;
  - GENESIS FK12 is framed as the register question.
  This seat takes them as given and changes neither.
- **The owner's instruction of 2026-10-02**, still binding here: nothing load-bearing ignored, the experiential question
  included. So the experiential question stays in GENESIS FK12, kept apart from the register question under Gate 5-Q (§2).

## Seen first (the repo sweep and the literature)

**The repo sweep**, before any GENESIS text was written.
- `git fetch --all` at the start. Main had moved from `77714caf` to `5c0951b7`: S43, GENESIS v1.5 (B1460), with B1459 (S42)
  before it. The other heads had not moved. The heads are in `arc_verdict.json`. None was merged.
- **Main's B1460**, read in full: FINDINGS, `adoption/amend.py`, its lock, its verdict, and the diff of GENESIS v1.4 to v1.5.
  - Main's received v1.4 is byte-identical to the copy in sm:B1525's `received/`.
  - Main's seven changes are exactly those its FINDINGS lists (C1).
  - Main built v1.5 on its own v1.4 and had not read sm:B1525. Its relay lists this seat's B1521 and B1522, and B1523 as
    sealed, as "read on main, not yet verified or banked — next harvest". So the two v1.5s were made in parallel, as the two
    v1.3s were.
- **Main's relay, §4**, on this seat's B1521: *"B1459's involution is the inversion of the fibre generators, −id on the
  torus, which is B1297's rotational P, not the inversion of Ballas' meridians."*
  - Main's B1297 says the same of its P (its §9: *"the figure-eight's rotational period-2 symmetry (axis disjoint from the
    knot, preserving the meridian direction)"*).
  - This seat's B1512 Lemma I and B1521 C1 say P fixes ρ_q and is the swap's class in Ballas' presentation.
  - These agree. C3 checks it with own code, independently of both seats' earlier arguments (§1).
- `scripts/checks/prior_work.py` ran on eight terms: "GENESIS v1.6", "Version 1.6", "register question", "elliptic involution",
  "swap's class", "rotational P", "CONFIRMED", "take v1.5 as head".
  - No head has a v1.6.
  - "rotational P" is in main's relay and B1297.
  - "elliptic involution" and "swap's class" are this seat's B1512, B1521 and B1523, and main's B1459.
  - "register question" is main's B1460. On this branch it matched only "act-and-register questions" (sm:B1521, sm:B1525).
  - "CONFIRMED" and "take v1.5 as head" add nothing beyond the relay and B1460.

**What this arc must not present as new.** Nothing in GENESIS v1.6 is new. Every carried sentence cites its arc. C2 re-runs
sm:B1525's checks of them.

C3's conclusion is main's B1297 §9 and main's relay §4, and this seat's B1512 Lemma I with B1521's addendum. What C3 adds is
a proof by own code from SnapPy's presentation, holonomy and symmetry group, which needs neither seat's earlier argument.

**The literature.** No source is newly cited. The one fact C3 uses beyond computation is Mostow–Prasad rigidity: the outer
automorphisms of π₁ of a finite-volume hyperbolic 3-manifold are its isometries. It is used in the form the record already
uses it (B1521 C1; sm:B1523).

## 1. The checks

| | what is checked | how | result |
|---|---|---|---|
| C1 | the received texts; main's v1.5 as main's v1.4 plus its seven changes | sha-256 and git blobs; line diff; main's own `amend.py`, read from its blob into a temporary directory, never run against this tree | identical to `5c0951b7`'s blobs. One version line, five marked blocks, one log entry. `amend.py` rebuilds main's v1.5 from the v1.4 here byte for byte |
| C2 | the items carried from sm:B1525 | sm:B1525's checks C1–C4 re-run from their own file | all four pass, sm:B1521's records byte-identical |
| C3 | B1297's P is the fibre's elliptic involution | SnapPy's presentation, holonomy (high precision) and symmetry group; Fox calculus; free-group words | below |
| C4 | v1.6 against main's v1.5 | regenerated; token and line diffs; marks; tables; statuses; the owner's decisions | only the eight listed edits, every changed block marked, statuses as main's, the decisions verbatim |
| C5 | the SM seat's v1.5, answered by its line | each block v1.5 changed against main's v1.4, looked up in v1.6 | 16 of 16 marks accounted for: 7 blocks as they were; the header, GENESIS GAP3, FK9 and FK12 and the log entry fitted or not carried (§2) |

**C3, P is the fibre's elliptic involution.**
- **Main's P.** In SnapPy's presentation of m004, ⟨a, b | aaabABBAb⟩, B1297 writes P as a ↦ a⁻¹, b ↦ a³b.
  - On the free group it is an involution.
  - In SnapPy's holonomy, made a genuine SL(2, ℂ) lift by a ↦ −a, it sends the relator to the identity. So P is an
    automorphism of π₁(m004).
- **P keeps the base and the orientation.**
  - The base: H₁(m004) = ℤ is generated by b, and a has exponent 0. The image P(b) = a³b has exponent 1 in b.
  - The orientation: the traces of ρ ∘ P equal those of ρ on eight words, a non-real one among them. So ρ ∘ P is conjugate
    to ρ and not to its complex conjugate.
- **P is not inner.**
  - The fibre's homology F^ab is generated by [a] over ℤ[t^±1].
  - By Fox calculus, ∂R/∂a at a ↦ 1, b ↦ t is 3 − t − t⁻¹ = −t⁻¹(t² − 3t + 1). So F^ab = ℤ[t^±1]/(t² − 3t + 1).
  - P sends [a] to −[a] and commutes with t, because P(b) = a³b with a in F. So P acts on F^ab as −1, inverting the fibre's
    homology.
  - An inner automorphism acts on F^ab as some tᵏ. The roots of t² − 3t + 1 are positive, so −1 is no tᵏ.
- **There is exactly one such class.**
  - SnapPy's symmetry group of m004 has order 8 and is the full group, with m004 amphicheiral.
  - Its cusp maps are the four sign pairs, twice each (main's B1456).
  - Exactly two isometries act on the cusp as the identity. These are the isometries that keep the orientation and act as +1
    on H₁.
  - By Mostow–Prasad, Out(π₁ m004) therefore has exactly one non-trivial class that keeps the orientation and the base.
- **P and the fibre's elliptic involution are that class.**
  - P is in it.
  - So is the fibre's elliptic involution. It keeps the orientation (−I has determinant 1) and the base, and acts as −1 on
    the fibre's homology, so it is not inner by the same argument.
  - Main's B1459 extends this involution to every level.
- **In Ballas' presentation ⟨m, n⟩**, by free-group words alone: sm:B1512's Lemma I map, the swap and conj(nM) ∘ swap
  (sm:B1521 C1) each send the fibre's generator mn⁻¹ to its inverse and keep the base.

So main's note and this seat's C1 describe one class. B1297's P is the rotational involution. In Ballas' presentation it is
the swap's class, and it fixes ρ_q. The knot's inversion θ, which dualises ρ_q, is a different class.

**C4, v1.6 against main's v1.5.**
- **Main's words.** All are kept except eight edits, all but two of them punctuation where a marked sentence is appended.
  The two: the version number, and "frame" made "frame's counts" in §8's frontier item.
- **Marks.** Every changed block of lines carries a [v1.6] mark, except the version line and §10's own entry. The earlier
  marks are unchanged, bold and plain alike, main's six plain [v1.5] marks among them. v1.6 adds 15.
- **Form.** Sections 0–10 are in order and every table is well formed.
- **Rows.** Every table row of main's v1.5 is kept verbatim but four (§5's m004 and word-state rows, GENESIS FK9 and FK12),
  whose leading cells are kept. Four rows are new (§9).
- **Statuses.** The fork statuses are main's: FK1 CONFIRMED, FK12 OPEN.
- **The owner's decisions.** The FK1 row, FK12's framing, the decided paragraph and §1's header are found verbatim in both
  texts.
- **Vocabulary.** None of Q5's three words, no vendor word and no private term occurs in v1.6, main's v1.5 or the seat's v1.5.
  A planted control is found.

## 2. The SM seat's v1.5 (sm:B1525), answered by its line

Each block v1.5 changed against main's v1.4, as GENESIS v1.6 answers it (C5 computes the fates):

| v1.5 (sm:B1525) | in GENESIS v1.6 |
|---|---|
| Version line and header sentence | replaced by v1.6's header sentence; v1.5 kept as received here |
| §5: the levels (sm:B1522), on m004's row | carried as it was, marked [v1.6] |
| §5: the word states (sm:B1523), on the other states' row | carried as it was |
| GAP3: the audit lane's refinement | **already in main's v1.5, in main's words** (main's [v1.5] qualification), so not carried. Both say the same: the lane's results prove the source or end-flux duty, not that a one-ended state can get the third only from a relation |
| GAP4: PASSED for DERIVED (sm:B1524) | carried as it was |
| §7: what of B723 survives (AR6) | carried as it was |
| FK9: the bar's null contract (sm:B1524) | carried as it was |
| FK9: P, the levels, the word states, "choice might be golden" | carried. P is named the fibre's elliptic involution, the class main's B1459 extends to every level, and C3 is cited |
| FK12: B130's scope (AR4) | carried as it was |
| FK12: the owner's act-and-register priority with three questions kept apart, the experiential one under Gate 5-Q | **fitted to the owner's framing** (below) |
| §8 frontier: the harmonic frame's counts, the class index on a mirror-broken family, B130 component by component | carried as they were |
| §9: four rows | carried as they were |
| §10: v1.5's entry | superseded by v1.6's entry, which says what was carried, fitted and not carried |

**FK12, fitted to the owner's framing.** sm:B1525 kept three questions apart under the owner's act-and-register priority of
2026-10-02. The owner has since framed FK12 as the register question, with four sub-questions (main's v1.5). In v1.6:
- **The first question** (whether a reduction loses data a declared later operation needs) is the register question's (i):
  at which step the register is dropped. It is not repeated.
- **The second question's datum**, the record's registering datum at the group layer (B599's pairing datum, whose evaluation
  A = mult_ρ − mult_ρ̄ is odd under the θ swap, B871), is placed in the register question.
- **The experiential question** stays apart, as an explicit hypothesis held under Gate 5-Q. It is never a consequence of the
  register question and never a claim. This keeps the owner's instruction that nothing load-bearing is ignored, the
  experiential question included, without adding anything to the owner's framing.

## 3. Elsewhere

- **sm:B1525's lock** now reads v1.5 from this arc's `received/GENESIS_v1_5_sm.md`, with a dated note. B1525's generator
  still rebuilds it byte for byte. This is how B1525 repointed B1521's lock.
- **B1516's citation rule** exempts a relay of another seat kept verbatim in a `received/` folder and named as the relay is,
  with a dated note. Main's relay cites GENESIS FK8 in a paragraph of its own words, which this seat cannot amend.
- **`docs/RELAY_LEDGER.md`.**
  - Main's relay is BANKED, answered here.
  - The new relay is OPEN.
  - sm:B1525's relay to main stays OPEN: it is answered on main's side when main harvests.
- **README.** Its foundations banner and section still named v1.2. They now name v1.6 and the owner's two decisions.
- **The relay** to main and the audit lane: `SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_6.md`. It proposes one rule against a
  third collision: a seat that builds a version on an older head renames it on reading the newer one, as this seat has now
  done twice.

## 4. Standing and firewall

**Standing: RE-DERIVED.**
- C1 agrees with main's own generator.
- C2 agrees with sm:B1525's records.
- C3 agrees with main's B1297 §9 and relay §4, and with this seat's B1512 Lemma I and B1521 C1.

What is added is the bookkeeping that makes GENESIS one text again, and an own-code proof of which class P is.

GENESIS keeps the experiential question as an explicit hypothesis under Gate 5-Q, never a claim. v1.6 contains none of Q5's
words. No Standard-Model number is touched: **0 of 19**.

## 5. Reproduce

```
cd frontier/B1526_genesis_v16
python3 verification/merge_genesis_v16.py received/GENESIS_v1_5_main.md /tmp/G.md   # equals GENESIS.md
python3 verification/genesis_v16_checks.py                                         # C1–C5, about 15 s
pytest tests/test_b1526_genesis_v16.py                                              # the lock (from the repo root)
```
