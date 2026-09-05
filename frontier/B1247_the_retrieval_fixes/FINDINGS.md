# B1247 — the retrieval fixes: the programme could not reach its own results

**2026-09-05 · cc (banking) · Gate 5 untouched — the A7 computation is symbolic throughout.**

## The diagnosis

Seven arcs banked this window, and **not one was a new computation.** Every finding was already in
the bank and simply unreachable:

- the **genesis theorem** (A1–A7 ⟹ A = LR, machine-checked, lock green) — uncited by the chain for
  **three months**
- the **seam family** (B286–B295) — ten arcs, **one** citation between them, and it was the negative
- **B497**, the four-stratum monoid and the programme's only irreversibility structure — sat **seven
  weeks** while B1157 concluded *"the object supplies no parameter-free dynamical law"* **without
  citing it**
- **B6**, holding the kinetic term B1157 lists as missing — on **zero** surfaces since week one

## The mechanism, located

`scripts/atlas/atlas.py`'s lexicon is **18 hand-authored regex sets, authored 2026-07-01 and frozen**
(B806) — and **~750 arcs have banked since**. It indexes *the objects the programme studies*:
`golden, eisenstein, figure_eight, torsion, metallic, kappa…`

**It has no word for a question.** No motif for arrow, irreversibility, dynamics, monoid, measurement,
collapse, closing, naming, or choice. So a seat asking *"do we have an arrow of time?"* retrieved
nothing — while B497 sat banked under **twelve** object-motifs, not one of which says monoid, strata
or dynamics.

**The index was keyed on nouns, and every question asked of it was a verb.** That is the archaeology.

## The repair, and the test that matters

Seven question-motifs added and re-mined — `arrow` 75, `monoid` 87, `measurement` 283, `closing` 339,
`naming` 38, `choice` 177, `coupling` 358 probes. **Verified by retrieval:**

| arc, excavated by hand this session | now answers |
|---|---|
| B497 the four-verb monoid | **arrow, monoid, measurement** |
| B766 time's arrow = the golden branch | **arrow**, measurement, closing, choice |
| B286 / B287 the seam, the canonical closing | **closing**, coupling |
| B1184 self-naming without self-signing | **naming**, choice, closing |

## The two proxies, replaced by reporters

**`representation_sweep` screened on CLAIM LENGTH** (floor 500): 282 arcs watched, **674 blind** —
and blind hardest to the dense, since the seam family runs 166–197 characters and **B286's 182
relocate the programme's central wall**. The floor is **kept** (so the gate does not regress) and
declared what it is: a gate threshold, not a measure of substantiality. What it cannot see is now
reported, **ranked by in-degree** — and the backlog is **9 arcs, not 154**.

**An in-degree SCREEN was tried first and rejected on its own evidence:** the seam family has
in-degree 1–2, so it would have missed exactly the case that motivated the change. The rejected
design is recorded in the instrument, per the B1240/B1243 practice.

**`--chain-gap`** reports arcs that synthesis surfaces cite and the chain does not, ranked by
surface-degree — validated against the chain **as it stood at B1243, before C46**: it flags B286 (3
surfaces), B294 (2), B287 (1), B295 (1), and correctly does **not** flag B288, which C8 already
cited. It is **not** a build gate: at threshold 1 it is ~688 arcs, because the chain is a curated
spine and absence is the normal case. `CHAIN_COVERAGE.json` gains a `_criterion` naming its feeder;
the review adjudicates and pins what it promotes.

## E58 gains the time-indexed clause

**A claim about a file is time-indexed.** E58 and E59 both assumed a static source; a cross-seat
dispute this session resolved as **neither party's error** — the file moved between reads. *Quote the
SHA you read, not just the filename.*

## A7 re-probed — and the answer is NO

Both orders have exactly **one** stable vacuum: LR → **φ**, RL → **1/φ**, curvature ±√5, product
exactly **1**. So B6's field equation does **not** break A7's tie. What remains is that the two vacua
are expanding vs contracting; requiring the growing one selects LR — but that replaces **one**
declared input with **two** (B6's lift, which B6 itself calls a choice, and reading non-cancellation
as *"the vacuum grows"*). **A7 stays an axiom.** Control: the class conjugate K has stable vacuum
φ² > 1, so the criterion discriminates only *within* the A7 pair.

This is a negative, and it is the point: it killed a seductive reading — *φ is stable, therefore the
bit is dynamical* — **before** it became an unearned identification.

## What lands with this arc

`docs/OPEN_ITEMS_2026-09-05.md` — **26 items across 8 sections**, every point raised in the session,
so that none of it depends on anyone's memory. It includes one thing explicitly **not** claimed: the
candidate synthesis *"the object is complete about itself and empty about everything else"* (H5),
which carries its own falsifier and must be attacked at Review 55 rather than cited.

## B806's tripwire fired, and its demand was MET

`tests/test_b806_lexicon.py` locks the lexicon's size and holds a list of words whose entry *"re-dates
every recurrence claim in the repository"*. It is a deliberate tripwire — its own docstring says
widening must be **"a DELIBERATE, banked act: whoever adds these words … must say so."** It fired on
`measurement`, and it was met by the B829 method rather than bumped:

```
lexicon 19 -> 26 (+7 question motifs)
top-3 WITH new motifs   : [golden, eisenstein, firewall]  coverage 0.8404
top-3 WITHOUT new motifs: [golden, eisenstein, firewall]  coverage 0.8404   change +0.0000
```

**The widening re-dates no recurrence claim** — top-3 unchanged, coverage bit-identical both ways.
The drift from B829's 0.8845 is corpus growth alone. 788 of 1153 probes (68.3%) now carry a question
motif; **15 carry nothing else** — they were blind in the full sense.

**The distinction that made `measurement` admissible**, and it is the arc's real content: every word
still on B1008's list is an **object** word, and admitting one *would* re-date claims about that
object. `measurement` entered as a **question** motif — it indexes what an arc **answers**, not what
it is **about**. The tripwire stays live for the object words.
