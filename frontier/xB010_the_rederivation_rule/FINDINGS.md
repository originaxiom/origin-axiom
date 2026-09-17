# xB010 — THE RE-DERIVATION RULE: a banked result is a HYPOTHESIS, not an answer — written, gated, and eaten by its own author

**Status: banked (frontier, `sep16-branch`). Verdict PROVED. Instrument.** Seat `xb`.
**PREREGISTRATION sealed and pushed BEFORE any code existed** — sha256
`5ec6f8c5da5c5e6abbe206952bb93983d24d6e3f0481b9972f819c9b51e3abfe`, commit `b5ac068`.
Lock: `tests/test_xb010_rederivation.py` (8 assertions) + `verification/reproduce.sh` (5 cells).
Gate 5 untouched.

## The instruction

> *"Always sweep the repo to see if what you plan to do doesn't already exist. If it does,
> **redo it anyway**, because if it's negative it might be misinformed, bugged or wrongly done —
> verify verify."* — the owner, 2026-09-17

## The gap, verified rather than assumed

**B1202** requires `already_banked.py` before any MISSING/OPEN claim; the absence-sweep rule
requires a complete sweep before an absence is even a finding. **Both govern ABSENCE.** Re-read
here: `already_banked.py`'s own output says **"SETTLED OR SCHEDULED MATERIAL EXISTS FOR THESE
TERMS. Read it BEFORE writing MISSING/OPEN"** — **read**, not **re-derive**.

> **Nothing covered the case where the sweep FINDS something. A banked result was treated as an
> ANSWER. It is a HYPOTHESIS.**

**The asymmetry that makes this urgent.** A wrong **positive** gets re-tested downstream, because
people build on it. **A wrong negative is never re-tested, because it stopped everyone.** A bad
kill is silent and permanent. Measured in one session: **B742 revived 2 of 33** re-adjudicated
kills; this seat's own **xB005 Q3 was a wrong kill**, caught only because the owner said
*reverify*; **B146's justification was wrong** though its kill survived; and this seat's single
unverified acceptance — *"the verification package FAILS"* — **was itself wrong**, its own missing
dependencies.

## The rule

**Sweep first, always. When the sweep FINDS something the planned work touches or leans on,
RE-DERIVE it before accepting it** — own code where feasible, the discriminating fact computed
in-sandbox (extending **E4** and **E3**). **Priority: banked NEGATIVES that would stop the work.**
Then **declare** it.

> **CITE ≠ RE-DERIVE.** Citing is using an arc's conclusion. Re-deriving is computing the
> discriminating fact again and comparing.

**Scope, narrowed in the seal rather than silently:** *redo everything the planned work touches or
leans on, and declare anything you did not redo and why.* "Redo all 1248 arcs" is not a rule anyone
can follow, and a rule nobody can follow is not read.

## The result against the sealed criteria

| cell | outcome |
|---|---|
| **R1** | **PASS** — in `WORKING_RULES.md` **and** `docs/PRACTICES.md`, both carrying CITE ≠ RE-DERIVE and the `NOT_RERUN` escape |
| **R2** | **PASS** — bound by a **frozen roster** of 1257 arcs, not a numeric cutoff, **and xB010 is not on it** |
| **R3** | **PASS** — 34/34 → **35/35**, 0 FAIL |
| **R4** | **PASS** — honest `NOT_RERUN` accepted; bare one caught; `CONFIRMED` with nothing recomputed caught |
| **R5** | **PASS** — the rule's own motivating statistic **re-derived, not cited** |

**R2 — why a roster and not a cutoff, demonstrated not asserted.** Seat-prefixed ids parse small:
`xB009 → 9`. **Any numeric cutoff would have exempted this seat's own arcs forever** — the author
would have written a rule that could never bind him. The roster binds by identity.

**R4 — the cell that could go wrong by design.** An **honest `NOT_RERUN` with a stated reason
PASSES.** A rule that forbade saying *"I did not re-run this"* would not produce re-derivation, it
would produce **false declarations** — the B1222 shape turned on ourselves, and the reason
`identification-register` is a ratchet. **Silence is what is made impossible, not honesty.**

**R5 — the author eats it first.** The statistic this rule *argues from* was re-derived from B742's
**artifacts**, not its prose: `recompute/` holds exactly **32** target directories, and tallying the
verdict column of its own table gives **REVIVED = 2**. Both confirmed. And **B146 is among them** —
B742 recomputed it in July; **xB006 re-tested it today and found its kill sound but its
justification wrong.** Two passes, two different defects. That is the case for this rule, made by
the rule's own subject matter.

**And the honest limit is declared rather than glossed.** B742's stated **30 RECONFIRMED** is **not**
independently confirmed here — this arc's row-parser tallies 8, because the table carries formats
the regex misses. Declared **SCOPED**, not CONFIRMED. **Not disputed — unverified by this arc**,
which is exactly the distinction the rule exists to make visible.

## Mechanism

`rederived: [{arc, outcome, what|why}]` in `arc_verdict.json`, outcome in
**CONFIRMED · CORRECTED · SCOPED · NOT_RERUN**, read by `gate_rederivation`
(`scripts/checks/rederivation.py`), bound by `docs/REDERIVATION_ROSTER.json`. **Completeness, never
judgment** — the gate cannot tell whether a re-derivation was real, only that the question was
answered where a reader can find it.

Noted for the record: on the first run the suite's own `tracked-deps` and `practices-register`
gates red, demanding the new files be tracked and the new gate registered — **the second time today
the instrumentation caught its own author.**

## What this seat does not do

**Proposes it on its own branch.** Landing it on `main` is `cc`'s call; the relay says so. No arc
re-verdicted, none retracted. `creates_law` false, nothing to `CLAIMS.md`, F2 or Gate 5.
