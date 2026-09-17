# xB008 — the identification discipline, extended from PROMOTIONS to KILLS: a gate that catches this seat's own error

**Status: banked (frontier, seat branch `sep16-branch`). Verdict PROVED. Instrument.** Seat `xb`.
**PREREGISTRATION sealed and pushed BEFORE the gate was written** — sha256
`30bb937bf26c6d02390f794a757d40a1144769bc495761389062e52814af92c6`, committed `91c9b94`.
Gate 5 untouched. Lock: `tests/test_xb008_linkage_gate.py` (10 assertions) +
`verification/reproduce.sh` (five cells).

## The hole this closes

**B1231's Identification Rule is enforced on PROMOTIONS only.** `gate_identification_register`
reads `arc_verdict.json`'s `identifications` — a field an arc declares when it **CLAIMS** a
sameness, and never when it **USES** one to **DISCARD** evidence.

xB005's Q3 asserted four ℤ/3s were *"all canonically linked"* — hence one fact, hence not
evidence — on links that connected only three of them. **Nothing in this repository caught it.**
Nor could B742's negatives hunt: its discriminator was *"a kill never EARNED by computation"*, and
an E82 kill **is** earned, with a **correct** computation — only the step from the links to the
conclusion fails.

> **The discipline was applied to what the record claims and not to what it throws away.**

## The result against the sealed criteria

| cell | sealed criterion | outcome |
|---|---|---|
| **G1** | **the efficacy claim** — xB005's Q3 *as it originally stood* must **RED** | **PASS** — class `C` |
| **G2** | the **corrected** Q3 must **PASS** | **PASS** — class `R` |
| **G3** | the present tree stays green | **PASS** — **33/33 → 34/34**, 0 FAIL |
| **G4** | two-way self-test | **PASS** — catches a planted E82 kill, clears **B727** |
| **G5** | the ratchet ratchets | **PASS** — unfreeze one → reds; restore → green |

**G1 is the cell that mattered.** The seal said: *"if the gate cannot catch this seat's own error —
the single error it was designed from — it is theatre, and this arc will say so and not ship it."*
It catches it. And **G2 is the cell that makes G1 mean something**: a gate that red-flagged the
*correction* as well as the defect would punish the repair and train seats to stop writing "not
evidence" rather than to check their links. It passes the correction.

## What it enforces, and what it deliberately does not

**The standing rule:**

> **A KILL NEEDS THE SAME MAP A PROMOTION NEEDS.**

Write the link graph, list the edges you exhibited, check **connectivity** before writing
*"all N are linked"*. An unlinked member is an **independent** hat and keeps its weight.

**Completeness, never judgment** (B1231's own wording). The gate cannot tell whether a link is
*true*. It requires only that, where a kill discards evidence by asserting a sameness, the link is
named where a reader can find it — **a map, a named theorem or definition, or a computed base
rate**. That last class is the one xB006 measured and it matters: **10 of 30 raw hits** were
base-rate or look-elsewhere arguments **with the rate computed**, a different and sound kind of
argument that must never be flagged.

**A RATCHET, not a blocker** — for B1231's own stated reason. A hard block on what is already
present would make the fastest path to green **relabelling existing kills as sound**, pressuring
exactly the judgment the gate protects. A **new** unexhibited linkage kill reds **at creation**,
which is when Q3 would have been caught.

## The baseline is honest about itself

`docs/LINKAGE_BASELINE.json` freezes **15** entries — and each carries **xB006's hand
adjudication**, not just a name. That is deliberate: the regex alone cannot tell these apart, and
**publishing a raw count as "wrong kills" would be the same over-reach the instrument audits.**
xB006 read every one. Of the 15: **2 are genuine E82 candidates** (`B146`, `B1096` — `B142` no
longer appears, because the base-rate clause now clears it), four have the link **supplied**
(B333's compositum definition, B1276's two named derivations, B1346's B1297 theorem, B559's
theorem), three are ordinary **prose**, one does no kill work, and **two are the MODELS of the
behaviour this gate asks for** — **B1223**, which states the discriminator itself, and **B772**,
which formed a linkage hypothesis, tested it and **refuted its own**.

## Bounded recall, stated not buried

**The lexicon is narrow on purpose** — the B806 lesson: a wide net flags every sentence in this
caps-heavy corpus and gets ignored (xB001 measured 272 candidates from a bare emphatic *"IS the"*,
overwhelmingly false). **A kill phrased without one of these constructs is invisible to the
checker.** It **reduces** the class; it does not close it. A lock asserts this: `by construction`
must stay **out** of the lexicon — it is descriptive prose (B425's *"golden BY CONSTRUCTION"*), was
never in xB006's sealed list, and drove **27 of an initial 46** candidates on its own.

## What this seat does NOT do

**This seat proposes the gate on its own branch.** Landing it on `main` is `cc`'s call, and the
relay says so. No arc is re-verdicted; no arc is retracted. `creates_law` false, nothing to
`CLAIMS.md`, F2 or Gate 5, no value, no generation count.

**Provenance.** `scripts/checks/linkage_kills.py`, `docs/LINKAGE_BASELINE.json`,
`gate_linkage_kills` in `scripts/gates/gates.py`, `docs/PRACTICES.md` register entry,
`tests/test_xb008_linkage_gate.py`, `verification/gate_cells.py` (G1–G5). Cross-refs E82, xB005
Addendum 1 (the error), xB006 (the calibrated lexicon and the adjudication), B1231 (the rule this
extends), B742 (the sweep that could not have caught it), B727/B1223/B772 (the sound forms), B806
(the recall trade).
