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
