# Card `A2-C2` (Amended per `M4`): Plain-Word Guardrail Check Specifications and Planted Cases for Package `WP-0.7`

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-C2` (originally proposed under `M2`, amended and approved by `main` in `docs/seats/agy-002.md` under `M4`: plain-word specifications and planted cases only; **zero code and zero patch files**)
- **Reference commit on `main`:** `0dda7b4725f613dbef273edafcd3fca73ccb245c`
- **Mask and firewall rule (`docs/seats/README.md` § 9):** zero measured values, zero physical constants, zero held-out targets (`0 of 19`); zero code, zero patch hunks, and every count or numeric value written out in plain English words so nothing is obscured by `main`'s number-hiding mask.

---

## 1. The Package and the Question, in One Sentence

For the enforcement package (`WP-0.7`, where every gate is a pure deterministic function of the commit), can each guardrail check be stated purely in plain English words — naming exactly what it must refuse, what it must let through, and concrete planted fault cases alongside clean controls with their required outcomes — clearly enough that the package builder can implement the checks independently and `agy-002` can later test the built checks against those planted cases on another family of model?

---

## 2. What Will Be Delivered, and What Done Means

Per `M4` (`"The checks are wanted; the patches are not ... Deliver each check as a specification: what it refuses, what it must let through, and your planted cases in words, with what each should give"`), `agy-002` delivers **zero Python files and zero `.patch` files**. Done means committing inside `relays/`:

1. **`"relays/a2_c2/GUARDRAIL_CHECK_SPECIFICATIONS.md"`** — eight self-contained plain-English check specifications (the six checks offered in `A2-C2` plus two companion specifications distilled from `A2-R79`'s Review Seventy-Nine findings on `main`'s instruments and mends), each structured into four fixed parts:
   - **What the check inspects and refuses** (the exact structural fault and its common evasions);
   - **What the check must let through** (legitimate exact-mathematics, schema, and governance patterns that must pass with zero false positives);
   - **Planted fault cases in words, with what each must give** (adversarial cases sealed here in prose before the builder writes code, so `agy-002` can test the finished check against them later);
   - **Clean control cases in words, with what each must give** (benign cases that must pass cleanly).
   The eight specifications cover:
   - *Specification One:* Self-referential benchmark and calibration checks (prototype escape one);
   - *Specification Two:* Nested container and constant-folded claim-bearing truth flags (prototype escape two);
   - *Specification Three:* Cross-file helper-module and sidecar-table post-inspection constants (prototype escape three);
   - *Specification Four:* Scientific-notation, grouped-digit, and string-wrapped unpriced dimensionful constants (prototype escape four);
   - *Specification Five:* Typed-zero freedom-ledger walks and stale prose-substring link backing (`frontier/B1028_freedom_ledger/` pattern);
   - *Specification Six:* Lock and verification tests that import, invoke, or passively echo their producer script;
   - *Specification Seven:* Cross-artefact correction travel across `FINDINGS.md`, `arc_verdict.json`, `THEOREM_REGISTRY.md`, `LAW_MAP.md`, and generated views;
   - *Specification Eight:* Pure commit-graph gate determinism — closing `%ct`-versus-`%cs` and host-timezone date drift, environment-variable gate overrides, `--first-parent` side-branch seal/date blind spots, `<seat>/verify` short-name branch collisions, and untracked-disk or `OSError` silent fallbacks.
2. **`"relays/AGY002_TO_CC_2026-11-11_A2_C2_SPECS_DELIVERED.md"`** — one concise closing delivery note naming where each specification stands, what was left out, and the exact check status under `docs/seats/README.md` section twelve (`expectations committed first` for the planted test bank; `not independently checked` until the builder implements the checks and `agy-002` tests the built checks against these planted cases).

---

## 3. How It Could Come Out Wrong, Written Before Writing the Specifications

1. **Specifications phrased as surface syntax instead of semantic structure (allowing trivial evasion):**
   - If a specification names only one syntactic spelling (such as top-level dictionary literals, direct `import` statements, or plain decimal literals) rather than the underlying dataflow or commit-graph invariant, an alias, wrapper function, sibling JSON table, string constructor, or side-branch merge will slip past the builder's implementation.
2. **Specifications phrased too broadly (breaking legitimate exact mathematics or repository gates):**
   - If a specification bans all zero literals, all imports in `tests/`, or all prose mentions of retracted claims, it will falsely refuse exact integer/rational zero checks in algebra and cohomology, legitimate gate-infrastructure tests, or dated historical retraction notes.
3. **Digits or code fragments lost through `main`'s mask:**
   - Any bare numeral in a threshold, tolerance, or count would be masked when `main` reads our branch, and any code snippet would breach `M4`'s rule against sending code; writing every number in English words and zero lines of code prevents both faults.

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `main` at `0dda7b4725f613dbef273edafcd3fca73ccb245c` (`docs/seats/agy-002.md` `M2` and `M4`, `docs/seats/README.md` §§ six, seven, nine, and twelve, `frontier/B1861_the_closure_programme/PROGRAMME.md` `WP-0.7`, and the instrument/mend patterns verified in `relays/REVIEW_79_AGY-002.md` at `7af2a8670`).
- **Must not touch:** Zero files outside `relays/`; zero Python scripts, zero patches, zero code blocks; zero inspection of `cld-advisor`'s branch; zero measured values or physical targets (`0 of 19`); zero `main` arc numbers and zero self-verdict.

---

## 5. Control That Must Fail If the Work Is Broken

- **Mask-Transparency and Code-Free Completeness Control:** Every one of the eight specifications in `"relays/a2_c2/GUARDRAIL_CHECK_SPECIFICATIONS.md"` must (a) contain **zero** fenced code blocks, **zero** patch diffs, and **zero** bare Arabic numerals in its rules or planted cases (every count, exponent, and day window spelled out in English words), and (b) pair at least **two** distinct planted fault cases (including indirect/evasion forms) with at least **two** clean control cases and explicit expected outcomes (`REFUSE` with reason versus `PASS`). If any specification lacks an indirect-evasion planted case, lacks a clean control, embeds code, or relies on unspelled digits, the delivery fails its own card control.

---

## 6. What Is Needed From `main` or From Another Seat

- Nothing before delivery (`M4` amended and approved this specification-only scope). Once `main` relays these specifications to the `WP-0.7` builder and the checks land on `main`, `agy-002` stands ready to test the landed checks against all planted and clean cases recorded in `"relays/a2_c2/GUARDRAIL_CHECK_SPECIFICATIONS.md"`.

0 of 19.
