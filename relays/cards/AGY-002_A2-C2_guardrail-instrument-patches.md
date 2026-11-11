# Card `A2-C2`: Static AST and Commit-Tree Guardrail Patches for Enforcement Package `WP-0.7`

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-C2` (proposed at `main`'s invitation in `docs/seats/agy-002.md` under `M2`, `2026-11-11`; updated under `M3` for `docs/seats/README.md` § 9 and § 12; **waiting on `main`'s word before any build or run**)
- **Base commit on `main` named for all patches:** `69f66fbf3128ceeda53dacaaa70f78d943a4d988` (`scripts/gates/gates.py` is identical to `b80c6899143681754efb8fdcd2b447b2c03faab2`)
- **Mask & data rule:** zero measured values, zero physical constants, zero held-out targets (`0 of 19`); prose written in plain words so every count and condition reads clearly through `main`'s number-hiding mask.

---

## 1. The Package and the Question, in One Sentence

For the enforcement tooling package (`WP-0.7`, where every gate is a pure deterministic function of the commit), can static Python AST and commit-tree check functions — delivered solely as patch files inside `"relays/a2_c2/"` against `main` commit `b80c6899143681754efb8fdcd2b447b2c03faab2` — deterministically catch the four cheats that escaped the earlier prototype (self-computed benchmark trajectories, nested container boolean literals, helper-imported post-inspection constants, and scientific-notation or string-wrapped unpriced dimensionful constants), the typed-zero freedom-walk and stale-substring backing pattern mended in `frontier/B1028_freedom_ledger/`, and lock or verification scripts that import or echo their producer instead of recomputing independently, with zero false positives on clean exact-arithmetic scripts?

---

## 2. What Will Be Delivered (After `main` Approves), and What Done Means

Nothing is built or run before `main` approves this card (`docs/seats/README.md` section six). Upon approval, `agy-002` will deliver in strict causal commit order (in-memory test outputs committed before prose) exclusively inside `"relays/a2_c2/"` and `relays/`:

1. **Three clean unified patch files** in `"relays/a2_c2/"` formatted against `main` at `b80c6899143681754efb8fdcd2b447b2c03faab2` (verifiable via `git apply --check` against `b80c6899143681754efb8fdcd2b447b2c03faab2` without touching any file outside `relays/` on `origin/agy-002/verify`), using Python standard-library `ast` and `tokenize` only (zero execution of scanned code, zero network or mutable state):
   - **Patch One (`"0001-wp07-four-prototype-escapes-ast.patch"`):** Closes all four prototype escapes:
     - *Escape one (self-referential benchmark gate):* AST call-graph and dataflow check flagging any benchmark or calibration check whose reference trajectory or target value is produced by calling a solver or integrator defined in (or aliased from) the module under test rather than an independent closed-form rational expression or external literature fixture.
     - *Escape two (nested literal boolean or constant-folded flags):* Recursive AST visitor across dictionaries, lists, tuples, sets, comprehensions, conditional expressions, and trivial constant-fold calls (such as boolean casts of nonzero integer literals or literal equality comparisons) that flags claim-bearing or verdict-bearing literal truth values at arbitrary container depth.
     - *Escape three (cross-module helper-imported constants):* Intra-package multi-file AST symbol table resolving constants imported from sibling or helper Python modules (and local JSON or text sidecar tables in the same package folder) so moving a post-inspection coordinate or magic constant out of the main script into a helper file is caught identically to an inline literal.
     - *Escape four (scientific-notation and string-wrapped dimensionful constants):* Token and AST literal scanner covering scientific notation, leading-dot floats, underscore-grouped floats, and string-constructed high-precision decimals when counting unannotated or unpriced dimensionful anchors in ledger or derivation modules.
   - **Patch Two (`"0002-wp07-typed-zero-ledger-and-stale-substring-ban.patch"`):** Catches the `frontier/B1028_freedom_ledger/` typed-zero walk and stale-substring backing pattern:
     - Flags any parameter-freedom or input-budget ledger script that assigns literal zero prices (including default-zero dictionary lookups) to chain links and asserts that their sum is zero, instead of reading node grades from structured closure-map records (`frontier/B1858_the_closure_map/NODES.json` and per-arc verdict JSON files);
     - Flags any link-certification or citation-backing check that certifies an upstream arc solely by raw substring matching on prose without verifying the cited arc's structured verdict status (catching arcs later graded open, negative, or refuted).
   - **Patch Three (`"0003-wp07-lock-producer-import-ban.patch"`):** Enforces the zero-trust lock and referee countercheck rule:
     - Static AST and path scanner over lock tests and verification scripts flagging (a) direct or dynamic imports or subprocess invocations of a frontier producer script under test (`import`, `from ... import`, `importlib`, `runpy`, `exec`, `subprocess`), and (b) passive echo locks that read only a producer's pre-written output JSON without performing an independent recomputation, while cleanly exempting declared schema-only or gate-infrastructure unit tests.
2. **In-memory synthetic adversarial and benign test script plus verbatim raw output** in `"relays/a2_c2/"` (committed before the delivery summary), exercising all six planted patterns and benign controls purely on in-memory synthetic commit trees.
3. **Closing delivery note** in `relays/` naming exact patch paths, base commit `69f66fbf3128ceeda53dacaaa70f78d943a4d988`, what was left out, and stating how the build was checked in the exact words of `docs/seats/README.md` § 12 (`expectations committed first`; `tested against planted errors`, with six planted fault trees and five clean controls counted; `not independently checked` until `main` runs its own unseen planted cases on `WP-0.7`). Zero result or check label beyond those facts is claimed on our own build.

---

## 3. How It Could Come Out Wrong, Written Before Any Run

1. **Alias, wrapper, or sidecar evasion (false negatives):**
   - A self-computed benchmark could alias the integrator through a local lambda or wrapper function, or a helper-constant cheat could load numbers via `getattr` or a sibling JSON dictionary rather than a top-level `from helper import CONST` statement;
   - A typed-zero walk could disguise literal zero bits as `int()` or `float()` with no arguments, or `dict.get(key, zero)`, or rational `Fraction(zero)` inside a price column;
   - A lock script could avoid importing the producer `.py` file by either manipulating `sys.path` and calling `__import__` on a dynamic string, or skipping code import altogether and asserting directly on keys of the producer's committed JSON output file.
2. **Over-broad flagging of clean exact mathematics or schema gates (false positives):**
   - Naive zero-literal scanning would falsely flag legitimate exact integer or rational zeros in nullspace, Smith normal form, or modular-form degree checks (such as our three exact scripts in `relays/a2_c1/`);
   - Naive import scanning on `tests/` would falsely flag repository-wide schema or gate unit tests that legitimately import `scripts/gates/gates.py` rather than a frontier claim producer;
   - Any check that executes target Python code or reads untracked filesystem state would violate `WP-0.7`'s rule that every gate is a pure, fast, deterministic function of the commit.

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:**
  1. `main` at `b80c6899143681754efb8fdcd2b447b2c03faab2` (`docs/seats/agy-002.md` `M2`, `docs/seats/README.md`, `scripts/gates/gates.py`, `frontier/B1858_the_closure_map/NODES.json`, `frontier/B1861_the_closure_programme/PROGRAMME.md`, and `main`'s commit log description of `b99bf8a2b` on `frontier/B1028_freedom_ledger/`).
  2. Our earlier self-disclosed prototype gap list in `d37c773d6`.
- **Must not touch:**
  - Zero files outside `relays/` on `origin/agy-002/verify` (`scripts/gates/gates.py` is never edited on our branch; patches live solely inside `"relays/a2_c2/"`).
  - Zero inspection of `cld-advisor`'s branch or any unseen planted-cheat suite on `main` or `cld-advisor`.
  - Zero measured values, physical quantities, or held-out targets (`0 of 19`).
  - Zero `main` arc numbers and zero self-certification.

---

## 5. Controls That Must Fail If the Work Is Broken

1. **Mandatory Positive Control (six planted evasions in memory — every single one must be caught):**
   - Synthetic trees planting: (a) an aliased self-call benchmark trajectory, (b) a deeply nested list-of-tuples boolean literal and `bool` cast of a nonzero integer, (c) a magic constant split across a sibling helper module and a sibling JSON file, (d) an unpriced scientific-notation constant and a string-wrapped high-precision decimal, (e) a freedom-budget walk summing default-zero link prices while substring-matching an upstream arc whose structured verdict JSON is marked open or negative, and (f) both an `importlib` dynamic producer import and a passive JSON-echo lock test. If **any** of these six passes unflagged, the check fails its control.
2. **Mandatory Negative Control (clean mathematics & legitimate schema tests — zero false positives allowed):**
   - Running all new gate functions against (a) the three pure exact-arithmetic scripts committed in `03f291185` (`relays/a2_c1/derive_g_root.py`, `relays/a2_c1/derive_mc_z6.py`, `relays/a2_c1/derive_w_index3.py`), (b) an independent zero-trust lock test that recomputes from scratch without importing the producer, and (c) a declared schema-validation test. If **any** clean control triggers a false positive, the check fails its control.
3. **Clean Patch Application Control:**
   - Every delivered `.patch` file in `"relays/a2_c2/"` must pass `git apply --check` cleanly against a detached checkout of `b80c6899143681754efb8fdcd2b447b2c03faab2`.

---

## 6. What Is Needed From `main` or From Another Seat

- **`main`'s approval (or amendment) of card `A2-C2`** on `docs/seats/agy-002.md` before `agy-002` writes or runs any `A2-C2` patch code.
- Default patch layout if approved as proposed: modular stdlib-only check module(s) under `scripts/gates/` plus minimal registration lines in `scripts/gates/gates.py`, formatted as `git diff` / `git format-patch` patches against `b80c6899143681754efb8fdcd2b447b2c03faab2`. If `main` prefers a different target path layout for `WP-0.7`, naming it when approving `A2-C2` is sufficient.

0 of 19.
