# SPECIFICATION OF TWO STATIC GATE CHECKS FOR CARD `X-C3` (`M4` AT `0dda7b472`)

- **Address:** `agy-exp` (branch `origin/agy/self-consistent-loop-2026-11-11`)
- **Card:** `X-C3` (`relays/cards/AGY-EXP_X-C3_two-mathematical-gate-checks.md`, amended per `M4` on `agy-exp.md` at `0dda7b472`)
- **Date:** `2026-11-11`
- **Form:** specification in plain words with planted cases and expected results (zero executable patches, zero floating-point literals, `0 of 19`).

---

## Overview and Shared Operating Rules

Both checks are pure static functions of the repository tree (inspecting Python abstract syntax trees and path relationships only, executing no target code and reading no network state). Each check exits with status zero when every scanned file conforms, and exits with status one when one or more violations are found, printing one deterministic diagnostic line per violation naming the file path, line number, check identifier, and offending symbol or sink.

For historical compatibility on `main`, each check accepts at most one frozen allowlist table recording pre-existing legacy paths that predate the gate, accompanied by a ceiling assertion that the allowlist length may only decrease over time and that zero newly added files may enter it.

---

## Check One — `no-proof-by-literal-flag-or-zero`

### A. Purpose

Prevent the failure class exemplified by `B1028` (`E7`), in which a verification script, budget/freedom walk, or theorem check certifies an invariance, extension, vanishing-phase, or zero-bit/zero-parameter claim by assigning a typed constant (`True`, `False`, `0`, or a constant-folded expression) to a claim-bearing dictionary entry, return field, or assertion variable rather than computing that quantity from an explicit mathematical object.

### B. Scope of Scanned Files

All Python scripts under `frontier/**/verification/*.py`, `scripts/**/*.py` that emit verification records, and `tests/**/test_*.py` (excluding test files dedicated specifically to testing the gates themselves).

### C. Exact Refusal Criteria (What It Must Refuse)

Define a **constant-tainted expression** inside a function or module body recursively as:
1. Any literal constant (`True`, `False`, integer `0`, empty container literal, or string literal).
2. Any call to a zero-argument type constructor or constant-producing built-in on constant-tainted arguments (`int()`, `bool(1)`, `len([])`, `sum([])`, `min([0])`, `max([0])`, `abs(0)`, `round(0)`).
3. Any unary, binary, subscript, slice, conditional, or comprehension expression whose operands and loop bounds are all constant-tainted (for example `0 * x` when `0` short-circuits, `1 - 1`, `[0][0]`, `(True, False)[0]`, or `{k: 0 for k in ("a", "b")}`).
4. Any local or module variable whose **all** reaching assignments in that scope are constant-tainted, and any call to a local helper function whose `return` expressions are all constant-tainted.

Check One **must refuse**:
1. **Claim-dictionary literal sinks:** Any dictionary key-value entry inside a `return` statement, JSON serialization payload (`json.dump`, `json.dumps`), or summary record whose key name denotes a mathematical claim, status, invariance flag, vanishing defect, or parameter/bit count — specifically keys matching claim tokens (`holds`, `verified`, `reproduced`, `passed`, `invariant`, `extends`, `acyclic`, `vanishes`, `is_`, `has_`, `all_`, `ok`) or cost/defect tokens (`bits`, `cost`, `price`, `inputs`, `free_params`, `defect`, `theta`, `error`, `residual`) — when its value expression is **constant-tainted** with boolean value `True` or numeric value `0`! *(Exception: metadata keys naming schema versions, fixed dimension indices, seed integers, or explicit failure returns `False` inside error branches are not refused.)*
2. **Tautological assertion sinks:** Any `assert <expr>` statement where `<expr>` (or the left-hand side of a comparison `assert lhs == 0` or `assert lhs is True`) is **constant-tainted** (for example `flag = True; assert flag`, or `cost = sum([0, 0, 0]); assert cost == 0`).
3. **Constant-list budget walks (`B1028` / `E7` pattern):** Any list, tuple, or table of tuples/dicts representing a multi-step parameter, freedom, or bit-cost ledger in which every numeric cost slot is constant-tainted `0` and the total cost is formed by summing those literal slots without deriving the slot values from computed set cardinalities, matrix ranks, or solver degrees of freedom.

### D. Exact Pass Criteria (What It Must Let Through)

Check One **must let through** (exit status zero):
1. **Comparisons against literal zero or `True` when the tested quantity is computed:** `assert rank == 0`, `assert defect == 0`, `assert is_invariant is True`, or `return {"holds": residual < tol, "rank": r}` whenever `rank`, `defect`, `is_invariant`, `residual`, and `r` depend via dataflow on matrix/vector operations, group-word evaluations, polynomial roots, file parses, or external solver calls.
2. **Accumulator initialization followed by non-constant update:** `total_defects = 0` or `all_ok = True` at the top of a non-empty loop when the loop body reassigns or updates that variable from a non-constant-tainted expression (`total_defects += row_defect`, `all_ok = all_ok and check_row(x)`).
3. **Explicit negative-result or error reporting:** returning `{"holds": False}` when an early guard detects a broken precondition, or setting non-claim structural constants such as `dim = 3`, `seed = 42`, or `order_modulus = 4`.
4. **Selection-cardinality log/count formulas when the candidate pool is enumerated:** computing a discrete choice count from `len(candidates)` where `candidates` is built by filtering an enumerated mathematical set (`len(qualifying) == 1` gives zero remaining ambiguity within that set only if the script computes `qualifying` from explicit predicates rather than typing `0`).

### E. Planted Test Cases for Check One (Expectations Committed Before Build)

Each case below is a self-contained single-file Python snippet fed to Check One in isolation:

- **Planted Breach `P1-1` (The `B1028` / `E7` eleven-zero walk):** A script defines an eleven-row list of `(step_name, 0)` tuples, computes `total_inputs = sum(c for _, c in steps)`, asserts `total_inputs == 0`, and writes `{"total_inputs": total_inputs, "holds": True}` to JSON.
  - **Expected result:** **REFUSED** (flags both the constant-zero ledger summation sink and the literal `"holds": True` claim key).
- **Planted Breach `P1-2` (Constant-folded arithmetic & container evasion):** A script sets `zero_val = len([]) + (3 - 3)` and `ok_flag = [True, False][0]`, then returns `{"vanishes": ok_flag, "theta_defect": zero_val}`.
  - **Expected result:** **REFUSED** (constant-taint propagation catches both `zero_val` and `ok_flag`).
- **Planted Breach `P1-3` (Helper-function indirection evasion):** A script defines `def compute_monodromy_extension(mat): return True` (ignoring its parameter `mat`), assigns `ext = compute_monodromy_extension(M)`, asserts `ext`, and returns `{"extends_to_cover": ext}`.
  - **Expected result:** **REFUSED** (inter-procedural constant-return taint marks `compute_monodromy_extension` as constant-returning, so `ext` is constant-tainted at both `assert` and `return`).
- **Planted Breach `P1-4` (Loop that never updates the literal accumulator):** A script initializes `bar_theta = 0`, loops over three matrices computing `d = trace(M)` without modifying `bar_theta`, and returns `{"bar_theta": bar_theta}`.
  - **Expected result:** **REFUSED** (`bar_theta` has only one reaching assignment, which is literal `0`).
- **Planted Legitimate Control `L1-1` (Genuine exact matrix-rank zero):** A script constructs an explicit integer coboundary matrix `D0` and cocycle matrix `D1` from group words, computes `prod = matmul(D1, D0)` by explicit loops, sets `defect = max(abs(x) for row in prod for x in row)`, asserts `defect == 0`, and returns `{"d1_d0_vanishes": defect == 0, "residual": defect}`.
  - **Expected result:** **PASSED** (`defect` depends on `prod`, which depends on loop arithmetic over `D1` and `D0`; comparing `defect == 0` is a genuine predicate, not a constant literal).
- **Planted Legitimate Control `L1-2` (Loop accumulator updated by genuine check):** A script initializes `all_passed = True` and `mismatch_count = 0`, iterates over twenty-seven covers updating `mismatch_count += int(compute_room(cov) != 0)` and `all_passed = all_passed and (mismatch_count == 0)`, asserts `all_passed`, and returns `{"holds": all_passed, "defect": mismatch_count}`.
  - **Expected result:** **PASSED** (both variables have non-constant reaching updates inside the loop).

---

## Check Two — `no-producer-import-in-locks`

### A. Purpose

Enforce zero-trust independence in lock tests (`tests/**/test_*.py`) and referee/verification audit scripts: a lock that checks a banked claim must construct the mathematical operators or run an independent check rather than importing the arc's producer script and asserting on its pre-packaged return dictionary, or reading the producer's saved output file and echoing its fields without recomputation.

### B. Scope of Scanned Files

All lock test files matching `tests/**/test_b*.py` (or `tests/**/test_*.py` paired with `frontier/B*`) and any script in `frontier/**/verification/` whose filename matches `*referee*.py` or `*lock*.py` (outside the frozen legacy baseline allowlist).

### C. Exact Refusal Criteria (What It Must Refuse)

Check Two **must refuse**:
1. **Direct static imports from `frontier/` producer modules:** Any `import ...` or `from ... import ...` statement inside a lock or referee script whose resolved target lies under `frontier/B*/` (whether directly or after manipulating `sys.path.append` / `sys.path.insert` to point into `frontier/B*/`).
2. **Dynamic module loading or code execution targeting `frontier/` scripts:** Any call in a lock or referee script to `importlib.import_module`, `importlib.util.spec_from_file_location`, `runpy.run_path`, `runpy.run_module`, `__import__`, `exec`, or `eval` whose path or module-name argument references (directly or via path-joining from repo root / `frontier`) a `.py` file inside `frontier/B*/`.
3. **Subprocess execution of the producer script as the sole check:** Any `subprocess.run`, `subprocess.check_output`, or `os.system` invocation inside a lock test that executes a Python producer script under `frontier/B*/` (re-running the builder's own script tests reproducibility at best, not an independent lock, unless the test file is explicitly tagged as a schema/CLI smoke test rather than a mathematical lock).
4. **Pure artifact-echo lock (reading saved producer JSON/text with zero computation):** Any `test_b*.py` lock file in which every `assert` statement inspects values loaded from `frontier/B*/**/*.json` (or `.txt` / `.jsonl.gz`) while the test file defines zero mathematical helper functions, performs zero matrix/algebraic/symbolic operations, and calls zero shared verification libraries — catching locks that merely assert `json.loads(path.read_text())["status"] == "PROVED"`.

### D. Exact Pass Criteria (What It Must Let Through)

Check Two **must let through** (exit status zero):
1. **Standard-library and third-party mathematical imports:** `math`, `fractions`, `itertools`, `collections`, `functools`, `hashlib`, `json`, `gzip`, `pathlib`, `numpy`, `scipy`, `sympy`, `mpmath`, `snappy`, `pytest`, and similar general-purpose packages.
2. **Designated shared test-infrastructure or gate modules:** imports from `tests/conftest.py` or `scripts/checks/` / `scripts/gates/` when testing repo-wide gates (as opposed to `test_b*.py` importing `frontier/B*/`).
3. **Artifact cross-comparison paired with independent recomputation:** a `test_b*.py` lock that reads `frontier/B*/.../output.json` **and** independently computes the deciding mathematical quantities in its own functions, asserting `independent_value == recorded_output["value"]` (this is a legitimate consistency check between an independent lock computation and the committed record, provided the file contains genuine mathematical computation and not dictionary-key lookups alone).
4. **Frozen legacy allowlist entries:** pre-existing `test_b*.py` files recorded in the one-time historical baseline list at the commit introducing the gate, provided no new file is added to that list and no existing allowlisted file adds new producer imports.

### E. Planted Test Cases for Check Two (Expectations Committed Before Build)

Each case below is a synthetic `tests/test_b9999_planted.py` snippet paired with a dummy `frontier/B9999_planted/produce.py` and `frontier/B9999_planted/out.json`:

- **Planted Breach `P2-1` (Direct `sys.path` + producer import):** `test_b9999_planted.py` appends `frontier/B9999_planted` to `sys.path`, runs `from produce import run_claim`, and asserts `run_claim()["count"] == 48`.
  - **Expected result:** **REFUSED** (flags `sys.path` injection + producer import from `frontier/B9999_planted`).
- **Planted Breach `P2-2` (`importlib.util.spec_from_file_location` evasion):** `test_b9999_planted.py` loads `ROOT / "frontier" / "B9999_planted" / "produce.py"` via `spec_from_file_location` + `exec_module` without touching `sys.path`, then asserts on `mod.RESULT`.
  - **Expected result:** **REFUSED** (flags dynamic module load targeting `frontier/`).
- **Planted Breach `P2-3` (`subprocess.run` re-execution evasion):** `test_b9999_planted.py` runs `subprocess.run([sys.executable, str(ROOT / "frontier/B9999_planted/produce.py")], check=True)` and asserts exit code zero.
  - **Expected result:** **REFUSED** (flags subprocess execution of a `frontier/` producer script inside a lock).
- **Planted Breach `P2-4` (Pure JSON echo lock with zero recomputation):** `test_b9999_planted.py` imports only `json` and `pathlib`, loads `frontier/B9999_planted/out.json`, and asserts `data["status"] == "PROVED" and data["orbits"] == 2800` with zero algebraic or numerical computation anywhere in the test file.
  - **Expected result:** **REFUSED** (flags pure artifact-echo lock lacking independent computation).
- **Planted Legitimate Control `L2-1` (Pure independent recomputation lock):** `test_b9999_planted.py` imports `itertools` and `numpy`, constructs the presentation matrices of the group from scratch, computes the orbit count `n_orb` via explicit breadth-first closure, and asserts `n_orb == 2800`.
  - **Expected result:** **PASSED** (zero `frontier/` code touched; genuine independent computation).
- **Planted Legitimate Control `L2-2` (Independent recomputation cross-checked against committed JSON):** `test_b9999_planted.py` computes the twenty-seven companion room counts independently using its own matrix rank routine, loads `frontier/B9999_planted/out.json` to verify SHA-256 and key-by-key agreement `assert computed_rooms == recorded["rooms"]`, and imports zero code from `frontier/`.
  - **Expected result:** **PASSED** (artifact read is paired with genuine independent computation, and zero producer code is imported or executed).

---

## Summary of Expected Planted-Error Tally

When the tooling builder implements Check One and Check Two and this session tests them on another family of model:
- **Check One** must catch **four of four** planted breaches (`P1-1` through `P1-4`) and pass **two of two** legitimate controls (`L1-1`, `L1-2`).
- **Check Two** must catch **four of four** planted breaches (`P2-1` through `P2-4`) and pass **two of two** legitimate controls (`L2-1`, `L2-2`).

`0 of 19.`
