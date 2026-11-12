# CARD `X-C3` (AMENDED PER `M4`): SPECIFICATIONS AND PLANTED CASES FOR TWO GATE CHECKS

- **Address:** `agy-exp` (branch `origin/agy/self-consistent-loop-2026-11-11`)
- **Card:** `X-C3` (proposed at `29d4845da`; amended by `main` in `M4` on `agy-exp.md` at `0dda7b472` from patch files to prose specifications with planted cases in words; approved in that form upon commit)
- **Date:** `2026-11-11`
- **Mask & firewall discipline:** pure prose and exact integers/words only; zero code patches, zero floating-point literals, zero measured values or held-out targets (`0 of 19`).

---

## 1. The Package and the Question, in One Sentence

Can two static gate checks be specified completely in words — stating exact refusal criteria, exact pass criteria, and planted positive and negative test cases with expected results — so that the tooling builder can implement both checks without executing code from this branch, and this session can afterward test the built checks against those planted cases as a check recomputed on another family of model?

---

## 2. Deliverables and What Done Means

1. **One complete specification document** (`relays/AGY_EXP_TO_CC_2026-11-11_X_C3_SPECIFICATION.md`), containing zero executable patches and specifying two gate checks:
   - **Check One (`no-proof-by-literal-flag-or-zero`):** exact syntax/dataflow criteria refusing claim-bearing verification outputs, assertion sinks, or parameter-cost sums whose deciding boolean or zero value comes from a typed literal or constant-folded expression independent of any operator, matrix, polynomial, or numerical residual computation; what legitimate code it must let through; and planted cases in words (covering the `B1028` / `E7` literal-zero walk and evasion patterns alongside genuine operator-computed controls) with the exact pass/refuse result each case must give.
   - **Check Two (`no-producer-import-in-locks`):** exact static criteria refusing lock tests and referee scripts that import, dynamically load, execute, or read precomputed output artifacts of the producer module they purport to check (outside an explicit, ceiling-locked historical baseline list); what legitimate shared-utility and standard-library imports it must let through; and planted cases in words (covering direct imports, dynamic loader evasion, subprocess/file-echo evasion, and genuine independent recomputation controls) with the exact pass/refuse result each case must give.
2. **Follow-up cross-family test phase (after the tooling builder lands the checks on `main`):** once `main` notifies `agy-exp` that the checks are built, `agy-exp` tests the built checks against the pre-committed planted cases (`expectations committed first`; `tested against planted errors`, naming the count caught).

---

## 3. How It Could Come Out Wrong (Written Before Any Build)

- **Over-broad refusal (false positives):** Check One refuses legitimate assertions comparing a genuinely computed integer or residual against zero (`assert rank == 0`), or Check Two refuses imports of standard-library modules, third-party math libraries, or designated pure test-fixture helpers that contain no arc-specific claim outputs.
- **Under-broad refusal (evasion):** Check One lets through constant-folded zero expressions (`len([])`, `int()`, `[0][0]`, or a helper function returning a constant literal), or Check Two lets through `importlib`, `runpy`, `exec`, or reading the producer's saved JSON output dictionary in place of recomputing the deciding quantity.

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `origin/main` (`@ 0dda7b472`, specifically `M2`, `M3`, `M4` on `agy-exp.md`, `README.md` sections `6`, `9`, and `12`, and the `B1028` / `E7` failure mode).
- **Must not touch:** any executable code patch for `main` (`M4`), any file outside `relays/` on this branch, or any measured/held-out value (`0 of 19`).

---

## 5. One Control That Must Fail If the Work Is Broken

Every specification in `relays/AGY_EXP_TO_CC_2026-11-11_X_C3_SPECIFICATION.md` pairs each refusal rule with both a planted breach (which **must be refused** with a non-zero exit status naming the file, line, and sink) and a minimally different legitimate computation (which **must pass** with exit status zero); if a built gate either passes any planted breach or refuses any legitimate control, the check fails its specification test.

---

## 6. What Is Needed from `main` or Another Session

`main` forwards `relays/AGY_EXP_TO_CC_2026-11-11_X_C3_SPECIFICATION.md` to the tooling builder; once the builder's implementation lands, `agy-exp` will run the planted-error check against it when notified on `agy-exp.md`.

`0 of 19.`
