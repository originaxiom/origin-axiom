# 193 — THE GUARD THAT CAUSED THE DAMAGE

**2026-09-09. Branch `claude/outside-bench`, at `origin/main` = `b94ed03a` (0 behind).**
Occasion: the owner's instruction — *"please fix all u can so cc can see and harvest them"* —
after the full-suite run on a clean `main` left twelve red tests.

All twelve are now green or accurately skipped. Everything below was verified by running it.

---

## 1. The finding: a hygiene guard cannot see the damage its own enforcement does

`tests/test_no_hardcoded_paths.py` forbids the two absolute prefixes it forbids in committed `.py`. The
cleanup that enforced it replaced each bench's absolute checkout prefix with the
**documentation placeholder** `"<repo>/"`. In prose that is the form the guard's own
docstring prescribes. In code it is a **dead path**: Python opens a directory literally
named `<repo>`, which exists nowhere.

The guard went green. **26 committed scripts stopped working.**

    B657 (4), B663 (1), B670 (5), B673 (1), B677 (1)   exec of the B575 / B649 prefixes
    B771 (5), B775 (3), B787 (2)                       cell results.json / output.txt
    B1306 slice C (3)                                  module loads

The B1306 three were live: `test_slice_c_own_rederivations_are_pinned` died on
`FileNotFoundError: .../sliceC/<repo>/frontier/B1275_e8_family_verified/.../e8_family.py`.

**Repaired**, each deriving the checkout root from `__file__` (walk up to the directory
holding `frontier/`). Two `"<repo>/"` strings were LEFT AS TEXT because they are correct as
text: `s2_cp.py`'s docstring and its `data_source` provenance field. `b1122_verify.py`'s
`"<repo>/" + REL_CCB` and `test_b1207_slow_lane.py`'s assertion on that prefix *are* the
convention.

**Verified, not merely edited** — `certificates/dead_placeholder_paths.py`, three controls,
three cells, all on B:

* every `_R("...")` argument names a path that exists (26 of 26);
* the resolver returns this checkout from each file's own depth (3 to 6 levels down);
* **B1306 slice C's three scripts re-run green and rewrote their committed `.json`
  BYTE-IDENTICALLY** (C5 PASS: order 3, fixed dim 6, 72 roots = the E₆ centraliser;
  C2 PASS: h¹(m004; e₆) = 6; C7 PASS: N³ = I, multiplicities 24 and 27+27);
* **B771 cell W3-084 re-runs end to end** — `VERDICT: RESOLVED-A`, all gates PASS — and
  rewrote its committed `results.json` byte-identically.

The detector is AST-based (string literals only), so comments and docstrings never trip it;
its controls require it to fire on a planted dead literal and stay silent on a docstring and
on a provenance label.

### The general form
**A guard written to enforce a textual property cannot detect a semantic break introduced
in the course of satisfying it.** The cleanup and the guard shared a vocabulary; the
scripts did not.

---

## 2. The second finding: `.gitignore` was deleting the evidence locks read

Under the heading *"LaTeX build artifacts (keep .tex and final .pdf, ignore intermediates)"*
sit `*.out`, `*.log` and `*.jsonl`. Those rules match at every depth, so they also matched:

| what | cited by |
|---|---|
| `frontier/*/verification/**/*.out` | the P3 verification package's manifest |
| `frontier/B646_wave2_integration/cc2_packets/**/*.log` | `ORIGINALS_MANIFEST.txt`, by sha256 |
| `frontier/B1062_bridge_cell/*.log` | `test_b1062_bridge.py`, by pinned string |
| `frontier/B1063_refresh_verdict/refresh_windows.log` | `test_b1063_refresh.py` |
| `frontier/B1137_regulator_probe/results/*.jsonl` | `test_b1137_regulator_probe.py` |

Consequence: **five locks could not run on any clone.** They failed with `FileNotFoundError`,
which reads like corruption and is not.

Worse, `test_p3_verification_package.py::test_manifest_is_current` reported
*"MANIFEST.json is stale: run build_manifest.py"* — and **following that instruction on a
clone deletes 20+ real entries** from the reviewer-facing package, because the builder globs
the filesystem. The manifest is not stale: after dropping only the path-shaped entries absent
from this checkout, before and after are equal exactly.

**Repairs.** Negations added for each cited class (one had to be placed *after* the `*.jsonl`
rule — a negation only works if it follows the pattern it undoes, and the first placement
silently did nothing). Three B1062 logs **regenerated from their own scripts in the repo**,
every pinned string reproducing exactly, and committed. The locks now separate the two
failure modes: for B646 a **HASH mismatch is still fatal** (that is the integrity claim) while
a MISSING file is reported as an incomplete archive, *after proving the file is genuinely
untracked*.

**Admissible-MISSING, terms stated** (`scripts/checks/already_banked.py`, 0 corpus hits each):
`b1062_v2_block1`, `b1062_v1_v3`, `refresh_windows.log`. These have **no producer in the
repository**; B1063 holds no script at all. They can only come from a bench that still holds
them.

---

## 3. Three numerical locks, three different diagnoses

**B565 `test_snappy_gate` — `assert 4.0 < 1e-09`.** SnapPy 3.3.2 returns the *other* SL(2,C)
lift. A lift is defined only up to a sign character χ: H₁ → {±1}; relative to the pinned lift
this one has χ(a) = −1, χ(b) = +1, so tr(a), tr(aB), tr(ABB) all come back negated — and
tr(ab) = +2 either way, exactly as that character predicts. The representation is unchanged.
The gate now searches the four characters and requires **exactly one** to reproduce all three
pinned traces. That is *stronger* than the old comparison in the direction that matters: a
per-word "match up to sign" would pass for a rep that is not the holonomy.

**B511/D3.3 — `assert 0.0 > 0.8`.** Not a claim failure: the run overflowed to NaN. The walk
lives in SU(2), but the step (A,B) → (AB,A) grows word length like Fibonacci and the squaring
branches double it. A rounding perturbation is then carried by a very long word, and **a
generic SL(2,C) perturbation of a unitary is loxodromic** — norm growing like exp(cL).
Rescaling by √|det| every 20 steps cannot catch that: **a loxodromic element already has
det 1.** Instrumented: max‖A‖ leaves 1 at step 59, NaN by step 79. Fixed by projecting back
onto SU(2) every step (quaternion part, normalise — exact for a true SU(2) matrix).
*Control:* against the old code the two agree to 5e-13 at 20 steps and diverge to 1.5e-8 at
40 and 4.4e-4 at 60 — the error doubling with each squaring, exactly as the mechanism
predicts. **The claim reproduces**: classical 0.895 > 0.8, wild 0.048 < 0.15, all three mixes
concentrating (0.924 / 0.849 / 0.955).

**B616 — the lock has never passed.** It pins *"observed 2 coarse-tier matches of 378 pairs"*;
the script prints 3 of 390. **Checked, not inferred:** `b616_heldout.py` was run in a worktree
**at `d6eac1ed`**, the commit that landed script and lock together, and printed *"3 coarse-tier
matches of 390 pairs"* there too. The lock was written against an earlier draft and landed
without being run. Re-pinned to what the script produces; the verdict (STILL-AMBIGUOUS) is
unchanged and the three matches are robust (dev 0.0071, 0.0071, 0.0099 against hard-coded
targets, so no bench can see a different count).

**One fragility reported and deliberately NOT patched** — re-pinning that number is main's
call, not this bench's. B616's family cut is `0 < val`, and 14 of the candidates are exact
zeros of the weld computed through `np.linalg.inv`, landing between 2e-32 and 7e-16: their
membership is decided by **the sign of rounding noise**. Both this bench and `d6eac1ed` keep
all 14 (family 65, pairs 390); any cut between 1e-14 and 1e-6 keeps 51 (pairs 306) and leaves
the matches and the verdict untouched.

---

## 4. One guard failing on ordinary English

`test_no_email_addresses_or_reviewer_placeholders` matched `reviewer-(?!style)`, meant for
identifier placeholders like the `reviewer-001` already in `STALE_REFERENCES`. It fired on
the phrase *"a reviewer-facing verification package"* in `CHANGELOG.md` and `PROGRESS_LOG.md`
— and one of those is append-only history, so the prose is not the thing to change. The
pattern now matches the identifier shapes directly. Checked: 001 / A2 / B / 3 flagged;
facing / style / ready allowed.

---

## 5. B1137 regenerated rather than skipped

`test_aggregate_re_derives_from_pinned_grids` re-derives from grids `.gitignore` had removed.
The real grid was **recomputed here** — 216 cells, 837 s, 4 workers — and `aggregate.py` on it
returns **`overall verdict = DISJOINT`** with all 18 targets NONE and zero regulator relations,
reproducing the banked claim. The null grid is being regenerated at the record's own shape
(100 surrogates × 4 H = 400 cells) so the aggregate is not re-derived from a thinner evidence
base than the one it was pinned from. *Caught mid-flight:* running `aggregate.py` with the
real grid alone silently emptied `null_by_H` in the committed `final_report.json` — reverted,
and the aggregate will be re-run only once the null grid exists.

---

## 6. What this session's errors have in common

Nothing here was a wrong theorem. Every one was **a claim about the state of the record that
no one had executed**:

* a placeholder that reads correctly and cannot be opened;
* an ignore rule for LaTeX intermediates that deleted a manifest's originals;
* a lock pinned to output from a draft of its own script;
* a failure message instructing the reader to perform the destructive act;
* a regex for identifiers that matched an adjective.

Each was invisible to reading and immediate on running. **Registers R-193.**

---

*Scope: no mathematical claim of the programme is asserted, revised or retracted here.
Gate 5 untouched. Two arcs' committed outputs (B1306 slice C, B771 W3-084) were reproduced
byte-identically, which is evidence for those arcs and for nothing else.*

---

# ADDENDUM 1 — THE CODEX SEAT'S SEVEN RED TESTS ARE TWO PRESERVED RECEIPTS, AND ONE OF THEM HAS A ROUTE

**2026-09-09.** Occasion: the owner's *"fetch everything stay updated. especially codex seat
and cc seat"*. Read at `origin/audit/physical-bridge-2026-09-05` = `833b939b`
(`0558e846 → 833b939b`, two commits, 1510 lines: R24, total mass-eigenline flux).

Reproduced from this bench in a throwaway worktree: **7 failed, 21 passed**. Earlier in this
session I over-read another seat's failure count as decay. Not this time — I read what each
failure *is* before saying anything.

## Neither failure is a defect

**(a) `test_actual_twisted_connection_transports_both_spin_factors`.** `spin_connection_bridge()`
returns `connection_matches = False`. Localised here: `mapped − expected` **simplifies to the
zero matrix**, and exactly eight off-diagonal entries differ *only* by expansion —
`-I*(a0 - I*a1)/2` against `-I*a0/2 - a1/2`. `sympy.Matrix.__eq__` is structural, so the
identity is true and the boolean is a false negative.

**The seat already found this.** `tests/test_physical_bridge_global_mass_flux_control.py` is
headed *"Exact R24 connection locks, retaining the original raw-comparison failure"* and
asserts all three of `exact_residual == 0`, `raw_comparison_disagrees`, and
`original_structural_boolean is False`. The failing test **is the preserved receipt**; the
exact control passes beside it. That is their own sealed rule — *"Preserve first runs,
failures and original code/tests. Any correction requires a separately sealed follow-on, not
a changed original receipt."* Patching it would destroy the receipt. **Independent
corroboration, not a finding.**

**(b) The six `holonomy_equivariance` failures are one fact, not six.** All six die at
`geometry()`'s deliberate `raise ValueError('no explicit original-to-canonical combinatorial
basis bridge')`, and that failure is sealed as `HOLONOMY_EQUIVARIANCE_FAILURE.txt`,
seal `72e40d9c`, 2026-09-08.

## What is new: the bridge exists, it is just not combinatorial

Measured here, SnapPy 3.3.2, on `m202`:

    Q.isomorphisms_to(K)                          ->  0
    K.isomorphisms_to(K)                          -> 12
    Q.is_isometric_to(K)                          -> True
    Q.is_isometric_to(K, return_isometries=True)  -> 12 Isometry objects

**The manifolds are isometric and K carries its full symmetry group; only the *combinatorial*
map is missing** — `isomorphisms_to` searches combinatorial isomorphisms, and a non-canonical
triangulation is generally not combinatorially isomorphic to its own canonical
retriangulation. So the route as written cannot succeed in general, and no amount of
precision will change that.

The geometric bridge does exist and **carries exactly the interface `iso_data()` consumes** —
`cusp_images()` and `cusp_maps()`, and nothing else. Demonstrated in the worktree with a
two-line fallback:

```python
bridges = Q.isomorphisms_to(K)
if not bridges:
    bridges = Q.is_isometric_to(K, return_isometries=True)
```

`tests/test_physical_bridge_holonomy_equivariance.py`: **10 passed.** Every assertion the six
failures were reaching for — the C₃ fixed characters, the cube-root pair with six-element
stabilisers, the sixfold scalar-invariance argument, the central obstruction on scalar lifts —
**passes on the geometric bridge**.

Not pushed to their branch: their discipline is a separately sealed follow-on, and which
bridge is admissible for R20's certified frame is their adjudication, not this bench's. Filed
here as a capability, per **R90** — *the dependency was a missing combinatorial object; the
capability that removes it is the geometric isometry list, and it costs two lines.*

*Scope: nothing about R24's flux claim is assessed here. Only the reachability of the
equivariance computation, which is what the seven red tests are about.*

---

# ADDENDUM 2 — THE RE-FETCH: CODEX LANDS R24 AND R25, AND A NEW SEAT FOUND THIS BENCH'S DEFECT INDEPENDENTLY

**2026-09-09, second fetch.** Occasion: the owner's *"refetch codex seat again"*.
Addendum 1 read `833b939b`; the seat is now at **`2cac82b9`**, three commits further, and a
**new branch appeared**: `claude/paper-verification-ufp0zn` @ `8dac820e`.

## 1. The codex seat banked, and the banking is honest

Three commits: R24 landed with its findings, and **R25 is new** — the free boundary wall.
Their `GOAL_VERDICT.md` states both in their own words:

* **R24** — the actual positive-source field has total boundary charge `sign(q)·k` for `k`
  prescribed arcs, *"including rounded seams and the complete topological exhaustion. The
  three-arc case gives +3 without assuming three isolated critical points."*
* **R25** — the mass eigenline supports a derived compensating wall with net index `−k` and
  the opposite anomaly polynomial. And then, immediately: ***"For k = 3 this is a mirror
  sector, not a mirror-free completion."***

That second sentence is the seat writing down the thing that costs it the result. R25's
design (addendum 1) preregistered *no* physical selection of `k = 3` and *no* automatic
anomaly cancellation; R25 delivers a cancellation and then names the price. **Preregistered
against its own interest and reported against its own interest.**

They also track their own regression precisely rather than in aggregate: *"341 broad passes
with the same 14 failures/8 errors as R24. No new failed/error IDs"* — and R24's entry names
the one added ID as *"that diagnosed original comparison"*, which is exactly the preserved
receipt addendum 1 identified. **My reading of their red tests is confirmed by their own
ledger.**

`CHIRALITY_REFRESH.md` records all nine remote branches fetched, and corrects B1355's
A-type-only exclusion **against Acharya–Witten §2.3 read directly** — the same primary-source
route memo 192 took, reaching the same conclusion independently.

## 2. A second seat found this bench's defect, the same day, without contact

`claude/paper-verification-ufp0zn` @ `8dac820e` is an independent re-derivation of THE
PAPER's checkable claims. Buried at the end of its message:

> *"Separately, `c_e8_types.py` carried a literal `<repo>` placeholder and could never run;
> it now resolves the root from its own location."*

**Two seats, same day, same defect, no contact.** That is the strongest evidence the class is
real and not an artefact of how this bench looks at things.

**The delta is the size.** That seat fixed **one** file. The sweep here found the same defect
in **26 committed scripts** — including `c_geodir_h1.py` and `c_tits_lift.py` *in the same
directory* — and repaired all of them, with `certificates/dead_placeholder_paths.py` to keep
the class closed. Their fix resolves the root as `parents[4]`, a fixed depth; the resolver
here walks up to the directory holding `frontier/`, which is why one form applied unchanged to
files sitting three to six levels down.

## 3. Where we diverged, and why both halves are kept

On the gitignored `*.out` artifacts the two answers were different:

| | this bench | the paper seat |
|---|---|---|
| approach | commit the artifacts, negate the ignore rule | regenerate from the script when absent |
| cost | generated files in the repository | the lock runs scripts (79 s for `c_tits_lift`) |
| benefit | the lock is instant and the evidence is auditable | nothing generated is committed |

**They compose.** Their form prefers a shipped artifact and falls back to regeneration, so
with the artifacts committed here it takes the fast path, and the fallback keeps the lock
runnable in any clone that lacks them. Adopted, along with their slice-D skip.
*Controlled:* with both `.out` files hidden the test still passes, so the fallback is
exercised and not merely present.

## 4. And the paper the owner is reading has changed

`8dac820e` edits `papers/P3_THE_PAPER/main.tex`. **§8's family-wide amphichirality sentence is
removed** — it had been retracted in this repository on 2026-09-02 (B1181 → B1235,
`arc_verdict` RETRACTED, the test used was orientation-blind) **and the paper still carried
it**; the corrected figure is 112 members, 38 amphichiral, 74 chiral. Also: §2's cusp shapes
were attributed backwards, §2's base rate resolves to 36.2%/31.0%, and Scope 20's *"five of
the six falsifiers"* is corrected to five.

That seat's own diagnosis of why no lock caught the retracted claim is worth keeping: *"The
claim was absent from `MANIFEST.json`, which is why no lock caught it."* **A claim outside the
manifest is outside the guard** — the same shape as this memo's §2, where evidence outside the
repository is outside the lock.

*Rebuilt and handed to the owner, replacing the earlier PDF, which was built from `b94ed03a`
and carries the retracted sentence.*
