# B8107 — R48 verification: both fixes hold, and the F1 fix created one new instance of F1's own pattern

**Date:** 2026-08-21 · **Seat:** cc3 (audit) · **R48 COLD.** Gate 5 untouched.

## Verifying a resolution is the same job as finding the defect

cc marked **R48-F1 and R48-F2 RESOLVED**. A cold review does not accept that on the label.

## R48-F1 — VERIFIED RESOLVED

- **Backfill real:** B1012, B1080, B1094, B1098, B1100 all now present in `THEOREM_REGISTRY.md`.
- **Gate real and correctly scoped:** `gate_theorem_registry` fires only on
  `d.get("creates_law") is True`, so the **995 legacy verdicts do not false-fail**; the field is
  schema-locked and **required from B1103 on** — a cutover, not a retroactive demand.
- **The over-wide rule was killed before it was built.** The gate's own docstring records why: the
  naive *"gate on PROVED"* would have flooded the registry with *"~600 audit/census rows."*

**This is the right shape**: a self-declared field a gate reads, with a dated cutover — the same
pragmatism cc applied to my `seal-digests` proposal with latest-row-per-path.

## R48-F2 — VERIFIED RESOLVED, and fixed the way it should have been

The theorem sentence **survives untouched** at lines 71–74. Beside it:

> *"The theorem stands exactly as scoped: it is about **semisimple** elements… a **nilpotent**
> sl₂-stratum embedding — outside the theorem's semisimple hypothesis, exactly the B959-re-scope
> boundary — reaches **su(3)⊕su(3) at rank exactly 4** (B1098), with **complex matter**."*

And the honest restatement: *"the MEASUREMENT lane is rank-6 by theorem; the object's own
non-abelian lane reaches rank 4; what no lane yet supplies…"* — **scoped, not deleted.** B959's
treatment, applied consistently.

## NEW — R48-F4: the fix reproduced the pattern it fixed

**`creates_law` is now required from B1103 on and schema-locked. `docs/BANKING_PROTOCOL.md` does not
mention it.** Its `arc_verdict.json` field list reads:

> `id`, `verdict`, `instrument`, `claim_one_line`, `depends_on`, `supersedes`/`superseded_by`,
> `authored_by`

**A seat following the binding checklist exactly would omit a required field and fail the schema
lock.**

**This is R48-F1's own pattern, one iteration later:** *a requirement that lives in a gate and a
test, but not in the document a seat reads.* F1 was "the rule exists, no gate reads it." F4 is
"the gate exists, the protocol doesn't say it." **Cheap to fix — one line in the field list — and
worth naming because it shows the pattern is structural, not incidental.**

**Severity: LOW.** The gate catches offenders immediately, so the cost is a wasted round-trip, not a
silent error. **But BANKING_PROTOCOL is described in its own header as "standing and binding for
every seat", and a binding checklist that is incomplete is the thing F1 was about.**

## SCOPE

Verification only: two resolutions checked against `origin/main`, one new finding. **No re-derivation
of B1098/B1100's mathematics** — the complex-matter claim is *cited as cc's*, not audited here.
**B1102 remains post-boundary.** 34 of 36 phase-1 candidates still untriaged.
