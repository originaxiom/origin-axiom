# B1049 — the full suite found five red locks that 94 targeted tests did not

**Status: banked (frontier). Repair arc. No mathematics asserted or disturbed; Gate 5 untouched;
nothing to `CLAIMS.md`.**

---

## What happened

Two arcs banked **green**: B1047 on **88** targeted tests, B1048 on **94**, both with **28 gates
green**. The first full suite to run to completion on an uncontended box — **4074 tests, 48
minutes** — returned **five failures**.

| | test | |
|---|---|---|
| 1–2 | `test_b1037_band_dispositions.py` | **RED SINCE B1043 — five arcs.** |
| 3 | `test_b967_retraction_sweep.py` | B1048's own FINDINGS, **invisible to the sweep before commit**. |
| 4–5 | `test_repo_gates.py`, `test_b887_gate_audit.py` | cascade of 3. |

> ### This is the **third** instance of the mechanism Review 42 named and B1041 recorded as having already recurred: **gates are fast and do not cover what the locks cover**, and a suite nobody runs to completion hides red locks at HEAD.

---

## Defect A — the per-line exclusion idiom is defeated by markdown wrapping

Four arcs independently wrote the same idiom: *to measure a gap without counting the rows you
yourself wrote, drop every **LINE** naming this arc or a later one, then search what remains.*

**Prose wraps. The idiom does not.** B1043's ladder bullet:

```
- ... **B1032** already corrected the rung to name **two** live routes; **B1043** adds that the
  φ-fixed cluster's own open question (B141 Item 4) was closed by B564 — which is about the
  `SL(3)` φ-fixed locus, **not** about generations, and changes no rung.
```

The **author token** (`B1043`) is on line 1; the **citation** (`B141`) is on line 2. A per-line
filter drops line 1 and keeps line 2, so **B141 reads as curated by nobody**. B1037's band count
fell **37 → 36** and its lock went red — *at B1043, and it stayed red for five arcs.*

### The sibling sweep — the rule `ERROR_LEDGER` gained one arc ago, applied at the first chance

*"The repair is not complete until the FILE is swept for siblings."* Swept, with each consumer's
**actual** predicate over all five curated surfaces:

| consumer | orphaned citations | status |
|---|---|---|
| **B1037** | `B141`, `B564` | **RED** — the failure that surfaced |
| **B1032** | `B141`, `B564` | **latent, green by luck** — it counts B885/B889/B890/B891, not B141 |
| B1031 | *none* | its predicate targets `**X33**`; the bullet reads `**X33 (three generations)**` |
| B1048 | *none* | its window starts after B1043 |
| `law_siblings.py` | *none* | genuinely unaffected — its targets are single-line headlines |

> **The draft of this arc said THREE consumers carried it. The arc's own check said TWO.**
> Claiming three would have been `E11` (overextended record) *inside the arc about latent defects*.

**All four now share one implementation, `scripts/checks/md_blocks.py`** — the idiom is wrong even
where it happens not to bite. The module **names its four consumers in its own docstring**, because
B1035's finding was that shared code filed as a research arc becomes a shadow library; this one
lives in `scripts/checks/` with the other instruments and declares who imports it.

---

## Defect B — the retraction sweep could not see the arc that was running it

`retraction_sweep._tracked_md()` used `git ls-files *.md` — **committed files only**. So a new
arc's own `FINDINGS.md` was **invisible to the sweep that arc ran**, and its violations first
appeared in the *next* run, after banking.

**That is exactly how B1048 shipped two live uses of the two phrases it had just registered.** Its
own sweep said clean; its own gate run said 28 green. Neither could have caught it. Repaired with
`-co --exclude-standard`, which shows the sweep the working tree an author is about to bank while
still honouring `.gitignore`.

**This is a general shape, not a one-off:** any instrument that enumerates through
`git ls-files` is blind to the work being done. It is worth checking the others.

---

## And one measurement corrected: the suite is **48 minutes**, not 81

`BANKING_PROTOCOL` row 18 recorded **81 minutes at B1041**. That figure was measured **while two
suite runs competed for the same box** — and *both of those runs were worthless anyway*, because
the working tree changed underneath them while they ran.

**Three lines added to the protocol row:**

- **A run against a MOVING TREE discharges nothing either.** Start it against a **committed** tree
  and stop editing until it lands, or the run is a partial run wearing a complete run's exit code.
- **48 minutes, measured on an uncontended box** (4074 tests, 3949 passed / 120 skipped).
- **Targeted runs do not substitute, measured:** 88 and 94 targeted tests, 28 gates green, five
  failures on the next full suite. *A targeted run tests what you thought you touched.*

**Provenance.** `verify.py` (24 checks) · `tests/test_b1049_wrapped_exclusion.py` ·
new: `scripts/checks/md_blocks.py` · repaired: `B1031`, `B1032`, `B1037`, `B1048` verify scripts,
`scripts/checks/retraction_sweep.py`, `frontier/B1048_.../FINDINGS.md` ·
`docs/BANKING_PROTOCOL.md` row 18.
