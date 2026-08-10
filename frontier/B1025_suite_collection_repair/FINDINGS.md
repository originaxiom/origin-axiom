# B1025 — THE SUITE DID NOT RUN: three unguarded optional imports aborted collection, and the gate that should have caught it measures the wrong thing

**Date:** 2026-08-10 · **Lane:** INSTRUMENT. No mathematics about the object; Gate 5 untouched;
no claim's standing changes. **Scope:** the test suite and one governance gate.

**On sealing:** no preregistration. This is a measured defect with a deterministic reproduction
and a repair, not a two-outcome question — the B979/B957/B960 pattern (recorded as
open-and-shut rather than sealed after the fact).

---

## 1. THE HEADLINE — `pytest -q` executed ZERO tests on a conforming clone

Measured on a fresh clone with exactly `requirements.txt` installed (numpy, scipy, sympy,
matplotlib, pytest — **snappy is commented out as optional**):

```
$ python3 -m pytest -q
ERROR tests/test_b461.py                  ModuleNotFoundError: No module named 'snappy'
ERROR tests/test_b719_scale.py            ModuleNotFoundError: No module named 'snappy'
ERROR tests/test_b849_order_parameter.py  ModuleNotFoundError: No module named 'snappy'
!!!!!!!!!!!!!!!!!!! Interrupted: 3 errors during collection !!!!!!!!!!!!!!!!!!!!
22 skipped, 1 warning, 3 errors in 218.33s (0:03:38)
```

**pytest aborts the entire run on a collection error.** So this is not "three modules skipped."
It is **zero tests executed** — the whole lock layer silent, on the command
`REPRODUCIBILITY.md` gives as the verification path.

`REPRODUCIBILITY.md` and `requirements.txt` both declare SnapPy optional:

> *"Optional — required only for live SnapPy cross-checks of claim P9. The verified figure-eight
> constants are hard-coded and tested without it."*

**The suite was therefore not merely fragile — it contradicted its own stated contract.**

## 2. THE CAUSE, and why it is small

Three module-scope imports, two direct and one indirect:

| locus | form |
|---|---|
| `tests/test_b461.py:2` | `import snappy` |
| `tests/test_b719_scale.py:2` | `import snappy` |
| `frontier/B849_order_parameter/order_parameter.py:22` | `import snappy`, executed at collection time by `tests/test_b849_order_parameter.py` via `spec_from_file_location` + `exec_module` |

**The repo already had the right idiom, in 37 other modules** — `pytest.importorskip("snappy")`
(e.g. `test_b125_snappy_arithmeticity.py`, `test_b100_literature_crosscheck.py`,
`test_snapdata.py`, `test_sieve.py`). Nine further modules import snappy *inside* a function or
`try`, which is also safe. **So the correct pattern was established and these three deviated** —
a drift of exactly the kind `WORKING_RULES` §Enforcement predicts for an ungated practice.

## 3. THE REPAIR

Each of the three now reaches SnapPy through `pytest.importorskip`. **The frontier arc's own
script is untouched** (`order_parameter.py` is a standalone runner that legitimately requires
SnapPy; the guard belongs in the loader) — `WORKING_RULES` rule 9, no banked path disturbed.

**Measured after:**

```
before:     0 tests collected, 3 errors, Interrupted
after:  3837 tests collected in 220.50s, 0 errors
```

## 4. THE LOCK, AND ITS POSITIVE CONTROL

`tests/test_b1025_optional_deps.py` — six locks, AST-based, asserting the structural invariant
rather than a transcript string (`WORKING_RULES` rule 7):

1. no test module imports an optional dep as a **direct child of the module body**;
2. any test that `exec_module`s a frontier script needing an optional dep carries an
   `importorskip` **before** the exec (the indirect form — the one that broke B849);
3.–5. **the positive control (MB12):** the detector *does* flag `import snappy`,
   `from snappy import …`, `import snappy.foo`, and *does not* flag the `importorskip`,
   `try/except`, and in-function forms;
6. a guard on the guard — `sympy`/`numpy`/`scipy`/`pytest` must never enter `OPTIONAL_DEPS`, or
   the lock would push the suite toward skipping its own mathematics; plus a pin that the three
   repaired modules **still reference snappy** (so the repair cannot degrade into deletion).

**Vacuity demonstrated, not asserted.** Re-introducing the bare import into `test_b461.py`
fails locks 1 and 6 (2 failed, 4 passed); restoring gives 6 passed. The criterion can pass
**and** fail.

## 5. THE SECOND FINDING — `chain-locks` enforces citation hygiene, not locks

Found while checking whether any gate covers this class. It does not, and a neighbouring gate
has the same shape of gap.

THE CHAIN states its own admission bar (`docs/THEOREM_LEDGER.md`, preamble):

> *"Admission per the sealed prereg fd934b27: exact statement + banked computation location +
> **green lock**."*

`scripts/gates/gates.py::gate_chain_locks` implements the last clause as:

```python
for pth in paths:
    if not os.path.isfile(os.path.join(ROOT, "tests", pth)): missing.append(...)
```

**It verifies the cited file EXISTS. It never verifies the file tests the link.** A link citing
a real file containing nothing about it passes, and the gate reports
*"ok (N links, every non-AXIOM one locked)"*.

**The confirmed instance — disclosed by the ledger itself, re-verified here.** C2 cites
`tests/test_b749_genesis_forks.py`, which contains exactly four test functions:

```
test_f5_parent_matrix_squares_to_m004_monodromy
test_f6_being_field_distinct_from_monodromy_field
test_f4_shadow_variants_fail_structurally
test_f7_witness_is_quadratic_self_similar_non_metallic
```

**No F3 test** — exactly as B998's audit found (*"F3 is a citation to a test that does not
exist"*). B1003 subsequently wrote `tests/test_b1003_f2_f8_locks.py`, closing **F2 and F8**;
**F3 still has no lock**, and the gate passed throughout and passes now.

**Why it is structural, not a nitpick.** B998 found this **by hand**; no gate could have,
because the gate measures path resolution. This is the same family as the defect an earlier
audit found — *"three gates passing while the files they guarded had been deleted"* — fixed then
by making gates fail closed on a **missing file**. Here the missing thing is a **missing test
inside a present file**, which that repair does not reach.

**Scope, stated honestly:** this does **not** make any chain link false. C1 (Morse–Hedlund) and
C2 (Hurwitz/Lagrange extremality) are **classical results, cited not re-proved** — the ledger
says so in its own text. What is unbacked is the repository's assertion that they are locked
*here*.

**Not repaired in this arc, deliberately.** Tightening `chain-locks` changes what a governance
gate asserts about the bank, and per `GOVERNANCE` §11 whitelists and gate semantics are
*"auditable, versioned amendments only."* Registered as a lead instead, with the cheap fix
named: require the cited file to contain at least one test whose name or body mentions the
link's arc id, and **report the coverage fraction** the way `docs/views/COVERAGE.md` does —
converting an unenforceable bar into a measured one rather than dropping it.

## 6. WHAT THIS ARC DOES NOT CLAIM

- It does **not** claim the suite is green. It claims the suite now **collects** (3837 tests)
  where it previously collected none; a full green run is a separate measurement.
- It does **not** touch any mathematical claim, ledger row, or verdict.
- The `chain-locks` finding is a **defect report with a named fix**, not a fix.

---

**Verdict: PROVED (instrument).** A reproducible defect that silenced the entire lock layer on
a conforming clone, repaired in the repo's own idiom, with a failable regression lock; plus one
further gate defect localized, verified against the ledger's own disclosure, and registered
rather than silently patched.

---

# ADDENDUM (same day) — the full run, and the FAIL-instead-of-SKIP class the first repair did not reach

**The suite has now been run end to end, twice.** This is the measurement the arc above could
not make, because before the repair the suite returned nothing.

| run | result |
|---|---|
| **before** the repair (`--continue-on-collection-errors`, so the abort did not hide the rest) | `28 failed, 3738 passed, 93 skipped, 3 errors` — 73 min |
| **after** the repair | `28 failed, 3744 passed, 96 skipped` — **0 errors** — 84 min |

**The collection abort is fixed and stays fixed.** But the failure count did not move, and the
reason is a second, milder instance of the same contract violation.

## The FAIL-instead-of-SKIP class

Of the 28 failures, **24 were missing dependencies, not mathematics**: 23 `snappy` and one
`networkx`. The 23 sat in **nine modules that import snappy *inside* a test function**. Those
modules *collect* fine — so the first repair never touched them — but on a clone without SnapPy
they **FAIL** where `REPRODUCIBILITY.md` promises the suite stays green. **A failure is not
green.** The defect is the same contract, one level down.

**Repaired**, in the same idiom, across `test_b453`, `test_b455`, `test_b458`, `test_b460`,
`test_b467`, `test_b470`, `test_b654_listening`, `test_qp1_self_naming`, plus two indirect
cases where a *frontier* module does the importing (`test_b152_cs_amphichirality_census`,
`test_b440_foreign_vacuum_control`) and one ordering fix (`test_b455` loaded
`frontier/B455_ethogram_e3_response/integrate.py`, which imports snappy at module scope, *before*
its guard).

## `networkx` was never declared

`tests/test_b565_triality.py` failed with `ModuleNotFoundError: No module named 'networkx'`, and
**`networkx` appears nowhere in `requirements.txt`** — yet it is imported by at least five
frontier scripts (B305, B306, B565, B727, …). This is not an optional dependency being reached
carelessly; it is a **real dependency the install contract never mentioned**. Added to
`requirements.txt` with the reason recorded inline. With it installed, that module passes.

## The lock, extended — and a false-positive caught before it became a "fix"

`tests/test_b1025_optional_deps.py` gains `any_bare_optional_import`, which flags a bare
optional import **anywhere** — module scope *or* inside a function — unless an
`importorskip` for that dependency appears **earlier in the file**.

**The first version of this detector was too crude** and flagged three modules
(`test_b147_arithmetic_chiral_bundle`, `test_b458`, `test_r28_10_stabilizations`) that are
**already correct** — each reaches the dependency *after* a guard, or through a `skipif`
decorator. **They were not "repaired."** The detector was corrected to be guard-aware, and the
positive control re-run to prove it still fires: a bare in-function import is flagged, a guard
placed *after* the import is flagged, a guard placed *before* is not.

*Recorded because it is the arc's own error class in miniature: an instrument reporting an
absence that the source refutes. The fix was to read the source, which is `COMPUTE_THE_PROGRAM`
P3 step 5.*

## WHAT REMAINS RED — four failures, and none is mathematics

| test | cause | disposition |
|---|---|---|
| `test_b837_file_drawer.py` | `new sealed-and-ledgered prereg(s) with no findings report: ['B1024']` | **a PROTOCOL TENSION, not a defect** — see below |
| `test_b616_heldout.py` | a sealed-transcript comparison assertion | not investigated here |
| `test_b646_wave2.py` | `[('MISSING', 'proof_queue/…q3_lemmas.log'), …]` — archive vs manifest | not investigated here |
| `test_b511_d5.py` | an assertion carrying a nested traceback | not investigated here |

**`test_b837_file_drawer` is red on `main`'s HEAD, and it is worth naming precisely.**
`frontier/B1024_l153_bits/` holds only `PREREGISTRATION.md` and `ARTIFACT_HASHES.txt` — no
`FINDINGS.md`, no `arc_verdict.json` — and B1024 **is** the head commit of `main`. But
`COMPUTE_THE_PROGRAM` **P5 requires sealing before compute**, and this lock fires the moment a
prereg is sealed *and* ledgered without a report. **So `main` is red by construction for the
whole interval between seal and report**, and the only relief is a hand-edited frozen exemption
list inside the test. There is no "sealed, awaiting compute" state the lock can recognise.

**Not repaired here.** Adding B1024 to the exemption list would convert a live obligation into a
silent one, which is the failure mode B837 and B982 exist to prevent. The honest fix is a
protocol-level one — a declared *awaiting-compute* state with an expiry — and that is a
governance amendment, not a test edit.

**Net after both repairs: `0 collection errors`, `3744+ passing`, and every remaining failure is
either a dependency the environment lacks or a governance obligation the repository is
deliberately carrying in the open.** No mathematical lock fails.
