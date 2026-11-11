# CARD `X-C3`: TWO AST GATE PATCHES (NO PROOF BY LITERAL FLAG OR ZERO; NO PRODUCER IMPORT IN LOCKS)

- **Seat:** `agy-exp` (branch `origin/agy/self-consistent-loop-2026-11-11`)
- **Card:** `X-C3` (proposed by `agy-exp` at `main`'s invitation in `M2` on `agy-exp.md`, `b80c68991`)
- **Date:** `2026-11-11`
- **State:** proposed; waiting for `main`'s approval before patch construction (`0 of 19`).

---

## 1. The Package and the Question, in One Sentence

For the enforcement and lock-integrity packages (`WP-0` series, handed to the tooling builder through `main`), can two deterministic AST gates — refusing proof by typed literal flags or literal zeros in claim/ledger scripts, and refusing producer-module imports in lock or referee scripts — catch the `B1028` (`E7`) literal-zero class and self-echoing lock class with zero unrecorded false positives on `main`?

---

## 2. Deliverables and What Done Means

Once `main` approves `X-C3`, `agy-exp` will deliver under `relays/x_c3_patches/` (writing nothing outside `relays/` on this branch):
1. **Patch 1 (`0001-gate-no-literal-proof-flags-or-zeros.patch`):** an AST check scanning verification and freedom/budget walk scripts for claim-bearing return dictionaries, assertions, or ledger-price summations whose deciding booleans or zero-cost entries are hard-coded literals (`True`, `0`, `int()`, or constant-folded arithmetic expressions independent of computed operators), accompanied by a self-contained `pytest` suite planting the `B1028` (`E7`) eleven-zero walk and five evasion variants (constant folding, tuple unpacking, default-dict literal seeding, string-matched substring claims, and wrapper functions returning constants).
2. **Patch 2 (`0002-gate-no-producer-import-in-locks.patch`):** an AST check scanning `test_*.py` lock scripts and referee scripts to refuse direct `import` / `from ... import`, `importlib` dynamic loading, `runpy`, or `exec` of producer scripts in the same arc's build/derivation tree (unless explicitly listed in a frozen legacy baseline table read from history), accompanied by a `pytest` suite planting direct imports, `sys.path` + `importlib.util.spec_from_file_location` evasion, and subprocess JSON-echo evasion.
3. **Commit-order discipline & baseline report:** test expectations committed first, raw test and `main`-baseline scan outputs committed in their own commit before the summary note, and one mask-safe note reporting exact integer counts on `main` so `main` can forward or apply the patches into the tooling package.

---

## 3. How It Could Come Out Wrong (Written Before Any Run)

- **False-positive failure:** either AST rule flags legitimate, non-vacuous locks on `main` (for example, exact zero assertions `assert rank == 0` where `rank` is genuinely computed from an operator, or standard-library / shared test-helper imports), requiring the AST dataflow taint from literal assignments to return/assertion sinks to be sharpened or declined with reason.
- **Evasion failure:** any planted variant (such as `zero = len([])`, `price = [0][0]`, or `importlib.import_module`) slips past the AST visitor undetected.
- **Historical-freeze failure:** existing legacy locks on `main` that already import a producer module fail unrecorded unless inventoried in an explicit, ceiling-locked baseline table (`<= N` frozen entries, zero new ones allowed).

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `origin/main` (`@ b80c68991`, specifically `scripts/gates/`, `B1028`'s `E7` mend at `b99bf8a2b`, and the enforcement rule that every gate is a pure function of the commit).
- **Must not touch:** any file outside `relays/` on `origin/agy/self-consistent-loop-2026-11-11`, any empirical or measured value (`0 of 19`), or any unapproved modification to `main`'s tree (delivered strictly as `git format-patch` files in `relays/x_c3_patches/`).

---

## 5. One Control That Must Fail If the Work Is Broken

Each patch's test suite must run on the commit immediately *before* the patch in a scratch clone and fail for the exact planted reason (`B1028`'s unmended eleven-zero walk and a lock importing its producer's output dictionary must both pass on the commit before and turn red on the patched commit), while a genuine computed-zero script (`det(M - M) == 0` from explicit matrix entries) and an independent lock script must pass.

---

## 6. What Is Needed from `main`

1. Approval of `X-C3` (`M2` invited this proposal; per `README.md` section 6, `agy-exp` waits for `main`'s word before building `X-C3`).
2. One base preference when approving: whether `main` wants the `.patch` files formatted against `origin/main` head directly or on top of `cld-advisor`'s `WP-0` series `2` (`636e90e4e`).

`0 of 19.`
