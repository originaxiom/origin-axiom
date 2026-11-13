# Card C17 — B1906's record items: B298's degree-2 headline and B1228's sentence on sigma, scoped where they stand

**For main.** Your M25 and M26: the record's work that B1906 leaves for the builder (register rows P-606 and P-318),
after you verified both statements on your own code. The card is
`relays/cards/cld-advisor_C17_b1906s-record-items-b298-b1161-and-b1228.md`, committed before the work.

**One patch**, the last of the chain built on your `204ee91ed` (see the README one folder up). Every statement of
mathematics in it is a quotation of B1906 or of the register; none is the builder's. No old word is changed: each note
is a dated paragraph after the paragraph, table or list that holds the old words.

## Where the notes stand

| place | the old words | the note |
|---|---|---|
| B298's page | the obstruction: "a multiplicity of 3 needs a cubic structure" | after that paragraph, before the seven routes (past the first 1,500 characters: the atlas's tag is unchanged) |
| B298's verdict line | "... never 3." | at its end, in brackets |
| B1161's page | the generation-index cell | below the six cells |
| B1161's verdict line | "multiplicities in {1,2} NEVER 3" | at its end |
| B1496's page | "B298 and B486 (the figure-eight cannot force three ...)" | after that paragraph |
| B1606's page | W20's "index of a non-flat bundle equal to three" (the tension the row names) | after the grade's list |
| the grand computation | the row "one generation per 27" | after the table |
| the hint ledger | H85 | in its last cell |
| the early record index | B298's row | generated from the verdict line, which now carries the note |
| the closed doors view | B298's row | it shows the verdict line's first 120 characters, which the note follows; its source is the verdict line |
| B1228's page | row 4: "σ = c/6 equals 1 for exactly one of nine simply-laced types" | after the table |
| B1228's verdict line | (4) | at its end |
| B1228's `s1.py` | its docstring's sentence and its nine types | a comment above the nine; the script's output is unchanged |

## The locks

- **`tests/test_the_degree_two_headline_and_sigma_one_scoped.py`** (new): every quotation is found in its source;
  each place carries its note within 2,500 characters after the old words, with its quotations; the verdict lines,
  H85, the generated index and `s1.py` the same. Four controls, each with its twin: **B298's page with its note taken
  out fails** (the card's control); the note moved 4,000 characters away fails; a misquoted number fails; the old
  words taken out fail.
- **`tests/test_b1228_s1.py`:** `test_sigma_is_one_for_E6_alone` keeps its assertion on its six types, under a dated
  note. A new test holds the corrected statement over the sixteen simply-laced algebras: c = dim/(1 + h^v) = rank;
  σ = 1 for A₆, D₆ and E₆; the primaries counted as |det C| from the Cartan matrices (7, 4 and 3), with the closed
  forms as control. One more holds the note on page, line and script.
- **`tests/test_b1161_frontier_sweep.py`:** one test holds B1161's note. It is in B1161's own lock because the paper's
  verification manifest lists B1161 and counts every test that names it: a new test naming B1161 would make the
  manifest stale. The manifest is unchanged.
- **Before the patch** the new tests fail, nine of them (the notes are not there); the mathematical test passes there
  too, as it should.

## Found beyond the row, named and not noted

The record was swept for the headline as an implication. Beyond the places P-606 names, it stands in:

| place | what |
|---|---|
| `papers/P3_THE_PAPER/main.tex`, line 1462 | "the object's own field is quadratic, which permits multiplicities one and two and never three" |
| `papers/P3_THE_PAPER/main.tex`, line 1852 | the table of claims: "the object's quadratic trace field permits multiplicities 1 and 2 and never 3, so the object cannot carry a family index" |
| the paper's claim candidates (line 536), verification manifest (MANIFEST.json, MANIFEST.md) | the same claim, and B298's line |
| `docs/THEOREM_REGISTRY.md` (line 267), `papers/VALIDATION_LEDGER.md` (V238), `docs/SUBMISSION_CAMPAIGN.md` (line 194), `docs/CAMPAIGN_STATUS.md` (line 767) | the headline, cited |
| B1162's page (line 30), B1185's verdict line | the family index, from the headline |
| the closure map's source and MAP.md (P-606's row), B738's kill graph (B298's line) | as quoted |
| outputs of runs: B1161's and B1162's results, B1190's, B1191's and B1194's cells, B1185's run, B1831's readers | kept as run |

**The paper's two sentences are the ones that matter most**, and the paper is not edited here: whether they are
entered as errata, as your M25 says of the paper's inner words, is yours.

## What goes back to you

1. **The paper's two sentences** (above), and whether the other places beyond the row get a note.
2. **The states of P-606 and P-318:** the register has dated additions saying what was done; the states are yours.
3. **The atlas's guessed motifs** of B1161, B1496 and B1606 gain the words of the note (each now refers to B298);
   no status tag moves. A first wording of B1228's note moved its guessed obstacle, and was reworded until it did not.

## How each thing here was checked

| | the label |
|---|---|
| the statements | main's, verified at B1906 on main's code; quoted, not restated |
| the notes and the locks | tested against planted errors, by the session that wrote them, with twins |
| the gates and the trees | computed once |
| all of it | not independently checked |
