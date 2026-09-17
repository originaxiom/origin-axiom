# xB008 — PREREGISTRATION (sealed BEFORE the instrument is built)

**Seat `xb`, `sep16-branch`, 2026-09-17. Written, hashed and committed before any code of this
arc exists; the hash is in `ARTIFACT_HASHES.txt` in the same commit, pushed before the gate is
written, so the order is checkable from this branch's history.**

## P0 — the quantifier

Repository instrumentation. No mathematics of the object, no value, no physics reading. Nothing
promotes to `CLAIMS.md`. Gate 5 absolute.

## Why this instrument

xB005's Q3 asserted that four ℤ/3s were *"all canonically linked"* — hence one fact, hence not
evidence — on links that connected only three of them. **Nothing in the repository caught it.**
xB006 then found why: **B1231's Identification Rule is gated and ledgered on PROMOTIONS only.**
`gate_identification_register` reads `arc_verdict.json`'s `identifications`, a field an arc
declares when it **claims** a sameness — never when it **uses** one to **discard** evidence.

> **The discipline is applied to what the record claims and not to what it throws away.**

xB006 measured the stratum: 30 raw lexicon hits over 798 kills, **3** after hand adjudication, and
the corpus is otherwise disciplined (10 base-rate arguments with the rate computed, 8 naming the
theorem, 3 models). So the instrument must be **narrow, ratcheted, and shipped with the
adjudication** — not the raw regex.

## The design, fixed here before it is written

* a checker `scripts/checks/linkage_kills.py` reusing xB006's **calibrated** lexicon;
* a **baseline** `docs/LINKAGE_BASELINE.json` freezing xB006's adjudication of the present corpus;
* a gate `linkage-kills` registered in `scripts/gates/gates.py`;
* a lock under `tests/`.

**A RATCHET, not a blocker** — deliberately, and for B1231's own stated reason: a hard block on
everything already present would make the fastest path to green **relabelling existing kills as
sound**, which pressures exactly the judgment the gate protects. Frozen hits stay frozen; a **new**
linkage kill with no exhibited link reds the suite **at creation**, which is when xB005's Q3 would
have been caught.

## Cells and two-outcome criteria — declared before writing any code

| cell | criterion | PASS | FAIL |
|---|---|---|---|
| **G1** | **the efficacy claim, and the reason this arc is pre-registered at all**: a replica of xB005's **original** Q3 text, as it stood before Addendum 1, is presented to the gate | the gate **REDS** on it | it does not — the instrument does not do the job it exists for, and this arc reports that and does not ship it |
| **G2** | the corrected Q3 (Addendum 1's text, which names the dissociation) is presented | the gate **PASSES** it — the fix is recognised, so the gate is not merely keyword-allergic | it reds — the gate cannot tell a defect from its repair and must not ship |
| **G3** | the present tree | the gate is **GREEN** — 33/33 becomes 34/34, nothing retroactively red | it reds the tree: the baseline is wrong and the arc says so |
| **G4** | two-way self-test, `--selftest`, planted controls | catches a planted E82 kill **and** clears **B727**, the record's own sound form | either fails — the instrument is miscalibrated, as xB006's S1 required |
| **G5** | the ratchet | a **new** unadjudicated linkage kill reds; removing it returns to green | a new one passes — the ratchet does not ratchet |

## Declared prior

This seat expects **all five to PASS**. G1 is the one that matters and the one that could
embarrass: **if the gate cannot catch this seat's own error — the single error it was designed
from — it is theatre, and this arc will say so and not ship it.**

## Scope and standing limits

* The gate enforces **completeness, never judgment** — B1231's own wording. It cannot tell whether
  a link is *true*; it enforces that the question was asked where a reader can find it.
* **Recall is bounded and inherited**: a kill phrased without one of the lexicon's constructs is
  invisible, the deliberate B806 trade. The gate reduces the class, it does not close it.
* This seat **proposes** the gate on its own branch. Landing it on `main` is `cc`'s call, and the
  relay says so.
* No arc re-verdicted. `creates_law` false.
