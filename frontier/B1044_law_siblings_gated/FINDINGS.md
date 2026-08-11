# B1044 — the topic search per restoration, made mechanical

**Date:** 2026-08-11 · **Lane:** the consolidation refresh — fixing its own method. Gate 5
untouched; zero anchors; nothing to `CLAIMS.md`; **no mathematics asserted or disturbed.**
**Files:** `verify.py` → `results.json` (9 checks) · lock `tests/test_b1044_law_siblings.py` ·
instrument `scripts/checks/law_siblings.py` · gate **`law-siblings`** (the **27th**) · registry
`docs/consolidation/LAW_SIBLINGS.md`.

**B1043** measured the defect — a band groups arcs by **banking date**, a law is a statement about
**what an arc says**, and B1039 restored a conjecture as open that **B564 had closed** — and
registered the fix as an owner decision. **The decision came back: fix it as I judge best.**

---

## 1. WHY IT IS AN INSTRUMENT AND NOT A RULE

The obvious fix is the one B1043 already named: *keep the band sweep, add a topic search per law at
restoration time*. **Written as a rule, it would have joined the others.** This refresh's own
findings say so twice:

- **Review 42** prescribed *"a partial run is not a run"* — **it recurred within two days** (B1041).
- **`THE_LADDER` X31** named self-inflation — **it recurred ten times across nine arcs** (B1042).

> **Naming is not gating.** So the fix is a sweeper, a registry and a gate.

## 2. THE POSTURE, TAKEN FROM THE REPO RATHER THAN INVENTED

**Candidates are TRIAGED, not capped** — the corpus's own posture for exactly this shape
(B821/B823, the blind-arc gate: *"this gate fails only on UNTRIAGED arcs — it asks for a judgement,
not a number"*). A hard-fail on every candidate would **fire on right answers and train readers to
ignore it**, which is `E34`'s recorded reason for leaving a related class ungated.

The gate also **fails closed** if the sweeper disappears: a missing sweeper is exactly the state in
which a restored law quietly leaves its siblings behind.

## 3. WHAT IT FOUND, AND WHAT WAS DONE WITH IT

**Seven candidates across four restored laws** — `isomonodromy` at **zero**, the control that shows
a law *can* be band-local.

**Six consolidated onto their laws' rows, retiring the debt:**

| arc | law | what it is |
|---|---|---|
| **B33** | the tower | the **spectral** face of the module law, at `n = 2,3` |
| **B232** | the tower | **the same law differentiated** — the step form is the difference of the band form, verified `n = 3..12` |
| **B522** | the tower | the **filtration theorem** — *"full proof NOT reached"*, but **the best known progress on the very prize B1038's row listed as open**, and the row now says so |
| **B75** | the metallic exponent | *degree=rank is a two-parameter `(m,n)` phenomenon* — the **first** statement that the exponent is not rank-bound |
| **B77** | the metallic exponent | *the signed scalar law `[A,B] = (−1)^{n−1} µ^n`* — **the sign half** of `[A,B] = ±µᵏ` |
| **B106** | the metallic exponent | Dehn-filling fixed points with root-of-unity neutral eigenvalues — **exactly the finite-order-µ stratum B198's own correction blames for the illusory multi-exponent readings**, i.e. the stratum the law must be read *off* |

**One left in debt, deliberately.** **B257** is **RELATED**: it shares the discriminant/branch-point
vocabulary but states a fact about the **Euclidean transition**, not the peripheral exponent. *The
fingerprint matched a word, not a statement.* It stays a candidate, triaged, **and still in debt**,
because it is owed a row of its own on a different law.

> **A registry that only ever says "same law, consolidate it" is a rubber stamp.** This one
> disposes both ways on its first use.

## 4. TWO SELF-MEASUREMENT BITES, INSIDE THE INSTRUMENT BUILT AGAINST THIS CLASS'S COUSIN

1. **B1043's LAW_MAP row names every candidate**, so the sweeper's **first run reported ZERO** —
   rows that *register* debt read as rows that *consolidate* it. That is **E37**, in the tool.
2. **The obvious fix was wrong and made things worse.** Dropping any line that names the registrar
   also drops **that row's real citations** — a LAW_MAP row is **one line** — so B117, B122, B121
   and B118 abruptly read as *uncited*. Caught because the candidate count went *up*, from 7 to 10.

**Both fixed by excluding registry rows BY PURPOSE (their headline) rather than by mention.** And
the same trap decided where B257's judgement lives: **naming it on `LAW_MAP` would make an
unconsolidated arc read as consolidated**, so the judgement sits in the registry and the arc stays
in debt where it belongs.

---

**Verdict: PROVED.** 9 checks. **27 gates green** — and the 27th was caught missing from
`PRACTICES.md` by the `practices-register` gate within a minute of being added, which is the
machinery doing precisely its job.

**What this does not do.** It does **not** re-disposition the corpus by topic — L164's larger
option, which would re-open every closed band. It makes the *per-restoration* check mechanical,
which is the cheap half, and the half that would have caught B564 for the price of one grep.
