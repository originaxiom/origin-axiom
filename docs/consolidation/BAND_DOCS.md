# Consolidation Refresh — the `docs/` pass (in progress)

**Status:** IN PROGRESS. Spine complete; registers mapped; ~8 of ~60 `docs/` files read in
full. Working note on a feature branch — nothing banked, `main` untouched.

**Executes:** `docs/THE_CAMPAIGN.md` § *THE CONSOLIDATION REFRESH*, the owner's second
instruction — *"read every doc in `docs/`"*.

---

## 1. The register map (what the programme keeps, and where)

Measured, not recalled:

| register | size | what it is | enforcement |
|---|---|---|---|
| `LAW_MAP.md` | **185 rows**, 6 sections (A object arithmetic · B stage/ear · C the chord · D meta-laws · F cascade+value · E the walls) | the banked laws | `law-map-provenance` — **traceability only**; the doc's own caveat: ~4 % cite a lock, *"treat an unlocked law row as a claim about the bank, not a checked fact"* |
| `THEOREM_LEDGER.md` | **C1–C43** | THE CHAIN: axiom→theorem, five labels (`THEOREM`/`CENSUS`/`IDENTITY`/`NO-GO`/`AXIOM`/`COROLLARY`) | `chain-locks` — **path resolution only** (see §3) |
| `ERROR_LEDGER.md` | **E1–E36** | one row per *error class*, not per incident | reviews check the window's errors against the taxonomy |
| `OPEN_LEADS.md` | 250 KB | `L1…L154`, with a disposition column | `relay-debt` |
| `HINT_LEDGER.md` | 155 KB | `H#` pre-decision observations (METHOD.md's generative register) | staged: NOTICED→CHECKED→PROMOTED/DORMANT/KILLED |
| `SEAL_LEDGER.md` | 113 KB | preregistration hashes | `seal-provenance` |
| `CAMPAIGN_STATUS.md` | 166 KB | the live board | `doc-currency` |
| `INPUT_COMPLETENESS_LEDGER.md` | 12 items | mandatory checklist for any SM-facing cell | filled in-prereg |
| `PRACTICES.md` | 38 KB | *the* register of agreed practices, with a GATED/TESTED/SCHEDULED/MANUAL column | `practices-register` |

**The governing insight behind this layout** (`GOVERNANCE` §12): *"Freeze the substrate;
generate the views; govern by metadata."* Five jobs with contradictory optimal layouts — lab
bench, bank, navigation, communication, history — so the tree is append-only and everything a
reader navigates is a regenerated view.

---

## 2. THE CHAIN, read in full (C1–C43)

Structure: Part I genesis (C1–C6, priced by B749), Part II the object's forced structure
(C7–C15), Part III the no-go chain (C16–C17), Part IV the open frontier (C18–C23), Part V the
cascade and value layer (C24–C43).

**Its most valuable property is that it prices its axioms.** C3, C4, C5 are declared
`[AXIOM — PRICED]`, each with a computed fork:

- **C5 orientation** — *"the discarded det −1 sibling **IS** the Gieseking manifold — m004's own
  orientation double cover parent… **Orientation = choosing the child of the parent.**"*
- **C4 the geometric carrier** — *"**ℚ(√−3) is bought at geometrization and nowhere earlier**"*
  (x²+3 stays irreducible over ℚ(√5); all four redundancy witnesses failed exactly).
- **The chain's total price:** *"exactly two FRAGILE forks: F5 orientation and F6 the puncture."*

This is unusually honest architecture: the axioms are not just declared, their *alternatives are
named objects*.

**Note for the P-thread (band B0–B99 §6):** C12 carries the trace-map sector-splitting as
*"the trace map is **θ-equivariant**"*, citing B48/B54/B64. It does **not** cite B62 and does
**not** identify θ with the opposition involution or with the substrate record swap. The
correction to that band's row is recorded there.

---

## 3. DEBT ROW — `chain-locks` cannot enforce the bar THE CHAIN sets for itself

**Confidence: high. Verified by reading the gate source and counting the test functions.**

THE CHAIN's stated admission bar (its own §preamble):

> *"Admission per the sealed prereg fd934b27: exact statement + banked computation location +
> **green lock**."*

`scripts/gates/gates.py::gate_chain_locks` implements:

```python
paths = re.findall(r"tests/(test_[A-Za-z0-9_]+\.py)", b)
if not paths: bad.append(...)
for pth in paths:
    if not os.path.isfile(os.path.join(ROOT, "tests", pth)): missing.append(...)
```

**It checks that the cited file EXISTS. It never checks that the file tests the link.** So a
link citing a real file that contains nothing about it passes silently, and the gate reports
*"ok (N links, every non-AXIOM one locked)"*.

**The confirmed instance, disclosed by the ledger itself and re-verified here:**

C2 cites `tests/test_b749_genesis_forks.py`. That file contains exactly four test functions:

```
test_f5_parent_matrix_squares_to_m004_monodromy
test_f6_being_field_distinct_from_monodromy_field
test_f4_shadow_variants_fail_structurally
test_f7_witness_is_quadratic_self_similar_non_metallic
```

**There is no F3 test** — exactly as B998's audit found (*"F3 is a citation to a test that does
not exist"*). B1003 then wrote `tests/test_b1003_f2_f8_locks.py`, closing **F2 and F8**;
**F3 still has no lock.** The gate passed throughout, and passes now.

**Why this is a structural finding, not a nitpick.** The repo's own enforcement doctrine
(`WORKING_RULES.md`) is that *"a practice not in that table is not an agreed practice"* and that
**gates fail closed**. Here the gate is *open by construction* for the property it names: it
enforces *citation hygiene*, not *lock existence*. B998 found the defect **by hand**; no gate
could have. That is the same shape as the three gates an earlier audit found *"passing while
the files they guarded had been deleted"* — fixed then by making gates fail closed on a missing
subject, but the subject here is a missing *test*, not a missing *file*.

**Disposition:** REGISTER as an `OPEN_LEADS` row + an `ERROR_LEDGER` instance under **E6**
(*transcript-grep lock*) or a new class. **Recommended fix, cheap:** have `chain-locks` also
require that the cited file contain at least one test function whose name or body mentions the
link's own arc id, and report the coverage fraction the way `COVERAGE.md` does for views. This
converts an unenforceable bar into a measured one rather than dropping it.

**Scope, honestly:** this does not mean the chain's links are false. C1 (Morse–Hedlund) and C2
(Hurwitz/Lagrange extremality) are **classical results, cited not re-proved** — the ledger says
so. What is unlocked is the *repo's* assertion that they are locked *here*.

---

## 4. What the enforcement layer measures about itself (collected)

The programme is unusually willing to measure its own instruments. Collected in one place for
the first time:

| instrument | its own measured coverage | source |
|---|---|---|
| `LAW_MAP` locks | **~4 %** of 113 rows cited a test lock; *"UNENFORCED INDEX WITH TRACEABLE PROVENANCE"* is the **decided posture**, after *"lock all 113"* was rejected as an unfunded mandate | `gate_law_map_provenance` docstring, R33-4 |
| the generated views | arcs with authored verdict **930/943 (98.6 %)**; kill-graph coverage **≈66 %** (95 % CI 56–80 %), so the closed-door map projects *"about two-thirds of the programme's negatives, not all of them"* | `docs/views/COVERAGE.md` (B801, seeded random sample of 60) |
| the recurrence atlas | top-3 concept coverage **0.995** in B201–400 vs **0.629** in B801–900; **14 of 14** current concepts have no word in its 19-word lexicon | B1008 |
| `chain-locks` | **not measured** — and per §3 it measures path resolution, not locks | this note |
| the test suite | **cannot run at all** on a fresh clone (see band B0–B99's infrastructure note) | measured here |

**The pattern worth naming:** every instrument that was *measured* turned out to cover
substantially less than its name implies, and in every case the programme published the number
rather than the name. The un-measured instruments are the ones to check next.

---

## 5. The falsification apparatus, and where it actually bites

- **`WHAT_WOULD_COUNT.md`** is the programme's only *whole-programme* seal, written 2026-08-09
  — *"Every **arc** in this repository carries a two-outcome seal. The **programme** carries
  none."* Tiers 0–4; Tier 0 done, Tier 1 substantially done, **Tier 2 (one sealed dimensionless
  ratio) not done and with no live candidate since B1005.**
- **The three grades** — DERIVED / REPRODUCED / FITTED — with the programme's own examples of
  each, including its own REPRODUCED result (`sin²θ_W = 3/8`, *"worth zero as a ToE claim"*).
- **`INPUT_COMPLETENESS_LEDGER.md`** — 12 mandatory items for any SM-facing cell. Its second
  application (B792/B797) self-audits to **8 PASS, 3 N/A, 1 PARTIAL**, and its own item-10 note
  is the sharpest sentence in the file: *"The protocol had already ruled Tests 1–2 inadmissible
  before they ran… the result worth carrying forward is not the null but that **rung 1
  (algebraicity) is the only admissible comparison available**."*
- **`NOVELTY_AUDIT.md`** — adversarial prior-art passes with the stance *"assume known, try hard
  to find prior art before concluding novel."* Verdicts sampled: R1 **PARTIALLY-KNOWN** (the
  amphichirality mechanism is Goodman–Heard–Hodgson 2008; only the integer-block-length
  palindrome lift is the project's), R2 **KNOWN** (Kitano–Nozaki) *with the project's own framing
  qualified against it*, R3 **KNOWN / standard**.

---

## Reading status

- [x] the spine: `GOVERNANCE`, `METHOD`, `WORKING_RULES`, `ARCHITECTURE`, `TERMINOLOGY`,
      `CLAIMS`, `THE_CLAIM`, `THE_FRAMEWORK`, `THE_LADDER`, `THE_CAMPAIGN`,
      `COMPUTE_THE_PROGRAM`, `WHAT_WOULD_COUNT`, `UNIQUENESS_THEOREM`, `PROVENANCE`,
      `AUDIT_REPORT`, `RETRACTIONS`, `REPRODUCIBILITY` (structure)
- [x] `THEOREM_LEDGER.md` (C1–C43, full)
- [x] `INPUT_COMPLETENESS_LEDGER.md` (full)
- [x] `views/REVIEWER.md`, `views/COVERAGE.md` (full)
- [x] `ERROR_LEDGER.md` (taxonomy E1–E36; bodies pending)
- [x] `LAW_MAP.md` (structure + all 185 row titles; bodies pending)
- [x] `NOVELTY_AUDIT.md` (R1–R3; R4+ pending)
- [ ] `OPEN_LEADS.md` (250 KB) · `CAMPAIGN_STATUS.md` (166 KB) · `HINT_LEDGER.md` (155 KB) ·
      `SEAL_LEDGER.md` (113 KB) · `PRACTICES.md` · `STRUCTURE_TO_NATURE_MASTERPLAN.md` ·
      `THE_END_TO_END_CHAIN.md` · `progress/REVIEWS.md` (247 KB, 35 reviews) · ~45 others
- [ ] root ledgers: `PROGRESS_LOG.md` (1.25 MB, 717 entries) · `CHANGELOG.md` (857 KB)
