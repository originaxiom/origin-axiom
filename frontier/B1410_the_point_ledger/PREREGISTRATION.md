# B1410 — PREREGISTRATION: the POINT ledger and the H5 predicate

**Sealed before any sweep runs.** Standing full-discipline election (owner, 2026-09-14).
Gate 5 untouched: no dimensionful quantity, no measured value, zero anchors under R11.

## 0. DISCRIMINATION FIRST — what would make this informative, stated before any answer exists

The binding practice (`docs/PRACTICES.md`, 2026-09-14) requires this paragraph first.

This arc's question is **structural**, not a value, so the requirement is not precision but
**reachability of the deciding cell**. The whole arc is informative iff the predicate's `OTHER`
verdict is **reachable at all**:

- **If no corpus row can ever classify `OTHER`** — because naming a target the object did not
  generate structurally requires consuming an identification — then **H5 is analytic, not a
  hypothesis.** It is demoted from candidate synthesis to definition and must never again be cited
  as a finding. That is MB12 applied to H5 itself: *a hypothesis that cannot fail is not a
  hypothesis.* **This outcome ends the arc at Phase 1 and is a result, not a failure.**
- **If `OTHER` is reachable**, the ledger is built and the falsifier hunt is a real hunt.

The control that carries the weight (**E67** — vary the thing that can break): the thing that can
break is **which object**, so `object_unique` is a *measurement* against a control family, never a
declaration. `UNTESTED` is not `true`.

## 1. WHY THIS ARC EXISTS, AND WHAT THE PREVIOUS THREE EFFORTS MEASURED

H5 (`docs/OPEN_ITEMS_2026-09-05.md:135-145`) asks for a **point**:

> **FALSIFIER (must be hunted before anyone leans on this):** *"find one banked case where the object
> supplies an other-referential point with no external input."* — **Not banked. Do not cite as a
> result.**

**C16, B750, B1264, B1274 and B1409 are all censuses of REFUSALS.** Enumerating refusals measures
the pattern's *reach* — which is what B1274 said it did — and **cannot contain the falsifier.** The
falsifier lives in the complement: the corpus's banked *positive* points. **That ledger does not
exist.** Three efforts have swept the wrong side of the ledger; this arc builds the other side.

**Not re-derived, cited:** `B1013` already sorted the *refusals*, in its own words:
*"a WALL is a well-posed question that is blocked; a BOUNDARY is a question that presupposes
something the framework denies; a SPECIFICATION is an input no framework derives."* This arc sorts **points**, the complement, and
adopts B1013's vocabulary where it applies. `B750`'s `ledger.json` supplies the schema to copy —
`{id, class, refusal, citation}` plus `can_fail_witnesses` and `excluded_by_criteria` — and its
class `T` (rows T1–T8, *"option-space + symmetry supplied, canonical point proven absent"*) **is**
C16's eight, enumerated and sealed. Any claim that the eight are unnameable is false.

## 2. THE AXIS — fixed here so it cannot move later

H5's phrase conflates two independent axes, and the arc is only well-posed once one is chosen:

- **other-referential** — a property of the **TARGET**: the set the selected element lives in.
- **no external input** — a property of the **DERIVATION**: what the selection consumes.

**This arc types "other-referential" on the TARGET.** Reason, stated in advance: typing it on the
derivation makes H5 analytic by construction (no external input ⟹ the only available referent is
the object ⟹ self-referential ⟹ permitted), and a hypothesis defined to be unfalsifiable is not the
one the corpus wrote down. Both axes are recorded per row, so the alternative reading remains
computable from the same ledger and the choice is auditable rather than hidden.

## 3. THE ROW SCHEMA

```
{ "id":   "P07",
  "arc":  "B862",
  "point": "Z/6",
  "target": { "name": "central quotients of SU(3)xSU(2)xU(1)",
              "size": 4,
              "generated_by_object": false },      # resolved against OBJECT_CLOSURE.json
  "derivation": { "identifications_used": [],      # I-rows the POINT's derivation needs
                  "anchors_T1": 0, "anchors_T2": 0 },   # CROSSING_REQUIREMENTS R11
  "specificity": { "control_family": "...", "object_unique": true|false|"UNTESTED" },
  "prereg": "none" | "<path>",                     # sealed prereg naming the target, if any
  "citation": "frontier/B862_global_form/FINDINGS.md" }
```

`named_by_identifications` (what it takes to *name* the target) is recorded **separately** from
`identifications_used` (what it takes to *derive* the point). Collapsing them is the escape hatch
that would make every row self-referential; keeping them apart is what lets `OTHER` be reached.

## 4. THE DECISION RULE — computed, not judged

`scripts/checks/point_census.py --classify <id>` returns exactly one verdict:

```
OTHER      target.generated_by_object == false
       AND derivation.identifications_used == []
       AND anchors_T1 == 0 AND anchors_T2 == 0
SELF       target.generated_by_object == true  AND specificity.object_unique == true
GENERIC    target.generated_by_object == true  AND specificity.object_unique == false
UNDECIDED  otherwise — printing the clause that failed
```

**`GENERIC` is what stops the exception clause absorbing everything.** H5 says *the object* supplies
points about *itself*; a point any comparable object also supplies is about the **type**, not the
object. The corpus already refused a claim on exactly this ground — `I-17` REFUTED, *"the recurrence
is FORCED, not evidence … only the atom ℚ(√−3) is object-specific"* (B727).

## 5. THE CLOSURE — a rule sealed now, a file built by instrument and frozen by hash

`docs/OBJECT_CLOSURE.json` is **not** hand-written. That is the failure mode this arc exists partly
to repair (see §8). The **rule** is sealed here; the file is emitted by
`point_census.py --build-closure` in the same commit and its sha256 recorded in
`ARTIFACT_HASHES.txt`.

> **Admission rule.** A structure is in the closure iff a **settled** arc states the object
> *generates* it, that arc's derivation consumes **zero** R11 anchors, and the statement is not
> retracted or superseded. Each entry carries its citation.

The closure has a **proved outer edge already banked**, which is what makes it a real boundary
rather than a convenience: B926 W11 — *"the object generates its being (prime 3, ℚ(√−3)) and
provably not its hearing (5, ℚ(√5))"* So `ℚ(√5)` is **out** by a banked theorem, and any row
whose target is built from it cannot be laundered as self-referential.

**Amendments are the headline metric.** Every post-seal addition is dated and names the candidate
that forced it. **One amendment per awkward candidate is H5 losing in slow motion, and it will be
visible in the arc's own report.**

## 6. CAN-FAIL WITNESS (MB12's positive half; B750's own pattern)

A configuration that **would** classify `OTHER`, written before the sweep runs:

> An arc that selects one element of a set defined by an external theory, by a computation
> consuming no UNEARNED identification and no R11 anchor. **Concretely: a selection among the four
> central quotients {1, ℤ₂, ℤ₃, ℤ₆} of SU(3)×SU(2)×U(1)** — a set defined by the Standard Model
> (Tong, arXiv:1705.01853), which is not in the closure under §5's rule.

If no such configuration could be written, Phase 1's vacuity kill has already fired.

## 7. CALIBRATION — named before the sweep, so recall is measured and not assumed

**MUST-RECOVER (positive controls).** B750's `T1–T8` as refusals, and as points: B287's fiber
slope, B1224's `CS = 0`, B1345's `J = 1`, B862's `ℤ₆`, B1248's `ε = −1`.
**MUST-REJECT (negative controls).** Results that are unique but are **computed, not selected** —
no candidate set exists, so there is nothing to choose from: `B680`'s exact identity
`Vol(4₁) = (3√3/2)·L(χ₋₃, 2)`; `B1406`'s graded index `tr(C) = 2`; `B1409`'s dimension
`dim_ℂ H¹(π₁, sl₂) = k`. Each verdict was read at source by this seat rather than taken from a
summary. A sweep that flags
these is measuring the *word* "point" and not the concept; `sense_census.py` is the harness that
says so, and its over-prediction rate on this arc's population is **measured here, not assumed**.
**Recall is reported as a number against these sets.** B1264's failure mode was assuming it.

## 8. THE VERDICT-BLINDING, AND WHY IT IS NOT OPTIONAL

**H5's own text** partitions the programme along this line — `docs/OPEN_ITEMS_2026-09-05.md:139`:
*"The programme's segments split on exactly this line: genesis → object → algebra (self-referential,
39 forced links) vs values/crossings and the closings (other-referential, ten negatives and four
axioms)."* The partition is **drawn along the success/failure line**, so read from outcomes H5
restates *"we succeeded where we succeeded."* The hypothesis carries its own confound. Therefore: **classify from the 240 sealed `PREREGISTRATION.md` files where one
exists** (a prereg names the target before the outcome exists), flag rows without one as `POST-HOC`,
and **publish the 2×2 of target-type × verdict**. If the classifier is reading outcomes, the prereg
and POST-HOC populations disagree measurably.

**B862 is POST-HOC** — its FINDINGS says *"Not preregistered"* — and is graded accordingly. It is
named here, before classification, precisely so that its verdict cannot be reverse-engineered from
the criterion.

## 9. DECLARED PRIORS (stated so the outcome can surprise the seat)

1. **`OTHER` is reachable** — because B862 exists. So I do **not** expect the vacuity kill to fire.
   Confidence: moderate. If it fires anyway, that is the stronger result and the arc ends there.
2. **B862 classifies `OTHER` or `UNDECIDED`**, turning on whether *"Conditional on the cascade
   (P5 + one rule + one owed definition)"* resolves to a non-empty `identifications_used`. I expect
   **UNDECIDED**, and I expect the arc's main work to be pricing that conditional honestly.
3. **H5 survives but with a measured population and a much smaller reach than its prose** — the
   likeliest single outcome.
4. I expect the ledger to be **small** — far smaller than the 1239-arc corpus suggests — because
   most banked results are spaces, laws, or refusals rather than selections.

## 10. NOT LICENSED BY THIS ARC

- No dimensionful quantity (wall 10 / B666, theorem-grade). No value compared to any measurement.
- No claim that H5 is true, false, or banked until one of {FALSIFIED, ANALYTIC-DEMOTED,
  SURVIVED-WITH-MEASURED-POPULATION} is recorded. H5's own text already forbids citing it.
- Nothing reaches `CLAIMS.md`, F2, or Gate 5. This arc asks whether the object can name a point at
  **all** — upstream of every value question, and not itself a crossing.
- A ledger row is **not** a claim that the point is physically meaningful. `B1408`'s standing fence
  applies verbatim: **being discrete buys precision, not relevance.**

## 11. THE SEAT'S OWN FAILURE MODE, AND THE RULE ADOPTED AGAINST IT

Every self-correction this seat made in the preceding window has one shape, and it is **not** the
proxy class E72–E80: each input was verified and the **composition** was asserted. *"B1274 attacked
2 of C16's 8"* (true; true; different populations). *"7 of 12 read"* (6 adjudications; a row seen in
sweep output; seeing ≠ reading). *"Every quote grepped in its source"* (14 greps passed; 7 rows
written; the greps were of the drafts, and writing altered 3). **Two true facts joined into a false
claim, with nothing checking the join.**

> **Rule adopted for this arc: a claim that joins two artifacts is a NEW claim and gets its own
> check, over both artifacts, by ONE command.** Operationally — the ledger rows are emitted by
> `point_census.py`; **FINDINGS quotes the instrument's output rather than narrating it**; and every
> sentence of the form *"N of M"*, *"the same"*, *"two of those"* cites the command that ran across
> both sides.

## 12. WHAT IS SEALED

§0 (the informativeness criterion), §2 (the axis), §3 (the schema), §4 (the decision rule), §5 (the
closure admission rule), §6 (the can-fail witness), §7 (both calibration sets), §8 (verdict-blinding
and B862's POST-HOC status), §9 (the priors), §11 (the join rule). Nothing below the seal may be
edited after push; corrections are appended as dated addenda, per E53.
