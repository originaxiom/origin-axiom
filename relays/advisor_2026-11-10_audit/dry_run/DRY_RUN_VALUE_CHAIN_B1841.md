# DRY RUN — the value-chain certificate on the live candidate (B1841)

**From:** the advisor seat. **To:** cc and the owner. **Kind:** `result:` (data-free; nothing compared with
measurement; main at `217e37c4f`).
**What it is:** the certificate of `ACCEPTANCE_CRITERIA.md` §8 and the graph of `PROPOSAL_THE_DERIVATION_GRAPH.md`,
tried by hand on the one row the inputs scoreboard still carries as the record's candidate — frame A, the six mass
ratios at B1841's row. The purpose is to learn what the real work queue is and whether the two proposals survive
contact with the record.

**Scripts and outputs (this folder):** `value_chain_dry_run.py` (the declared graph), `code_chain.py` (what the
scripts load), their `_out.txt` and `.json`, and `chain_table_B1841.txt`.

## 1. The answer

**The certificate would be refused, on six grounds, before any statistical question is asked:**

1. The candidate itself has **no lock**.
2. Its declared ancestry **cannot be used as a chain**: it is 737 arcs and contains retracted, open and negative arcs.
3. One direct dependency, B1840 — the menu of ends the candidate's price rests on — has **no verdict file**.
4. Of the 27 arcs its code really loads, **3 have no lock and 12 have text-only locks**.
5. **Six of those 27 declare themselves thread results**, under a head that declares itself weave, with no lifting
   theorem named.
6. The chain **never reaches the foundation by computation**. What joins the foundation to the frame is the
   scoreboard's 13 borrowed joints.

None of this is new information about whether the six are right. It says the present record could not certify them
either way.

## 2. The declared graph is not a chain (DR1)

Following `depends_on` from B1841:

| | |
|---|---|
| arcs in the closure | **737** (47% of the record), to depth 13 |
| verdicts | 553 PROVED, 140 NEGATIVE, 27 OPEN, 3 RETRACTED (B731, B964, B1181) |
| ids depended on that have no verdict file | 14: B1840 (depth 1), B506, B511, B578, B580, B659, B666, B913 (folders without a verdict), and B792, B796, B829, B844, B846, B999 (no folder found by that id) |
| lock tier of the 553 PROVED | 205 compute, 130 run the script, **161 text-only, 42 none**, 15 other |
| arcs with no script in the folder | 129 |
| declare `reach` / declare `weave_or_thread` | 216 / 187 of 723 |
| on the seal-order-unshown list | 33 |
| rest on a seat / cite a seat | 17 / 46 |

**Reading:** `depends_on` records "this arc cites that arc" as well as "this result uses that result". A candidate
value does not logically rest on a retracted arc or on 140 negatives. As it stands the field cannot carry a
weakest-link computation: every value would inherit the weakest status in half the record.

**Consequence for the graph proposal:** the edges need a type — at least `uses` (the result or its code is an input)
and `cites` (context, a door closed, a predecessor) — and only `uses` edges propagate status.

## 3. The computational chain is 27 arcs (DR2)

Following what the scripts load (folder and file names in the source, recursively):

```
arc    d  verdict   lock        reach   w/t      seal    data
B1841  0  PROVED    NONE        class   weave    yes     yes
B1839  1  NEGATIVE  NONE        class   weave    yes     yes
B1741  2  PROVED    COMPUTES    class   thread   yes     yes
B1753  2  PROVED    COMPUTES    class   weave    yes     yes
B1798  2  NEGATIVE  TEXT-ONLY   class   thread   —       —
B1838  2  OPEN      NONE        general neither  —       —
B1612  3  PROVED    TEXT-ONLY   general weave    yes     yes
B1637  3  PROVED    TEXT-ONLY   general weave    yes     yes
B1667  3  PROVED    COMPUTES    class   neither  yes     —
B1720  3  NEGATIVE  COMPUTES    class   thread   yes     yes
B1723  3  NEGATIVE  COMPUTES    class   weave    yes     yes
B1726  3  PROVED    COMPUTES    class   weave    yes     yes
B1735  3  PROVED    COMPUTES    class   weave    —       yes
B1749  3  PROVED    COMPUTES    class   weave    yes     yes
B1611  4  PROVED    TEXT-ONLY   general weave    unshown —
B1635  4  NEGATIVE  COMPUTES    general weave    yes     —
B1691  4  PROVED    COMPUTES    class   weave    —       —
B1725  4  PROVED    COMPUTES    class   weave    —       yes
B1734  4  PROVED    COMPUTES    class   thread   yes     yes
B1610  5  NEGATIVE  TEXT-ONLY   general weave    yes     —
B1632  5  NEGATIVE  TEXT-ONLY   general weave    yes     —
B1600  6  PROVED    TEXT-ONLY   class   weave    —       —
B1617  6  NEGATIVE  TEXT-ONLY   general weave    yes     —
B1492  7  PROVED    TEXT-ONLY   single  thread   yes     —
B1493  7  NEGATIVE  TEXT-ONLY   single  thread   yes     —
B1616  7  NEGATIVE  TEXT-ONLY   general weave    yes     yes
B1615  8  NEGATIVE  TEXT-ONLY   general weave    yes     —
```

(`lock` is the static census's tier; `data` means the arc's scripts name a measured-data file; a negative arc appears
because a later arc imports its code or its output, not because its conclusion is used.)

- **No lock: B1841, B1839, B1838.** The candidate (PROVED), the card it is read jointly with (NEGATIVE) and the arc
  that states the end condition (OPEN) are guarded by nothing. No file under `tests/` names B1841.
- **Text-only: 12 of 27**, including B1612 (which holds the measured-data file every later arc loads), B1637, B1600
  (the weave's own verification) and B1611.
- **Code is reused across arcs by file path.** A change in `frontier/B1726_*/verification/census.py` or
  `frontier/B1741_*/verification/compare.py` changes B1753, B1798, B1839 and B1841 together; no lock ties the importing
  arc to the version it was sealed against beyond each arc's own `ARTIFACT_HASHES.txt`.
- **B1656, the arc that defines the frame, is not in the code chain by name:** its functions are loaded from a copy
  in `frontier/B1723_*` (`b1656_funcs.py`). The definition of the frame and the code that evaluates it live in
  different arcs.

## 4. Thread and weave on the chain (DR3)

All 27 arcs declare `weave_or_thread` — the field is well kept on this chain. But:

- **Six declare thread** (B1741, B1798, B1720, B1734, B1492, B1493) and two declare neither, under a head (B1841)
  that declares weave. B1841's own row is located at "apex 162, τ₀ = (1/2, 2.9496)" — one thread's apex out of
  B1753's 223.
- **The field is free text** ("weave (a census over lines and apexes)", "thread (each thread's own point)"). Whether
  a census over many threads, read at its best row, is a weave result under `docs/THE_WEAVE.md`'s three questions is
  a judgement the text does not settle: question 2 asks for a quantity "defined by the joint action", and a best row
  over a census is defined by a search.

**Consequence for acceptance row W-a:** `domain` needs enumerated values and a separate field for how a census was
reduced to one row (all rows / a rule fixed in advance / the best row).

## 5. The chain does not reach the foundation (DR4)

The code chain ends at B1492, B1493, B1600, B1667 and B1691 — the weave's verification, the canonical cusp and the
exponents. Nothing in it is computed from `GENESIS.md`'s grammar. What joins the foundation to this frame is exactly
the scoreboard's list for frame A:

| Joint | Type | Feeds |
|---|---|---|
| S01 a flat bundle on the fibre | ANSATZ | every row |
| S02 the orientation (SE2) | CHOSEN | every row |
| A01 the modulus τ on the strip | **FITTED** | rows 1–12, 17 |
| A02 the slope 2/5 | CHOSEN | rows 1–12, 17 |
| A03 the line's offset (2/5, 4/5) | CHOSEN | rows 1–12, 17 |
| A04 the Higgs direction DR | CHOSEN | rows 1–12, 17 |
| A05 the up-conjugate reading | CHOSEN | rows 1–12, 17 |
| A07 the end E4 | CHOSEN | rows 1–12, 17 |
| A08 the generations' metric H = I | CHOSEN | rows 1–12, 17 |
| A09 the channel weights | CHOSEN | rows 1–12, 17 |
| A10 the lepton factor c | **FITTED** | rows 5, 6, 12 |
| A11 one address for all sectors | CHOSEN | rows 1–12, 17 |
| A12 tree level at M_Z, no running | CHOSEN | rows 1–12, 17 |

**Consequence for the graph proposal:** these joints are the missing edges. Each becomes a node of kind
"frame choice" between the foundation and the frame, with its status; the graph is not complete without them.

## 6. The first condition map

Conditions on frame A's six mass ratios, and what closing each one alone would release:

| Condition | Kind | Rows it blocks | Rows released if it alone is closed |
|---|---|---|---|
| A01 τ fitted | continuous, fitted | all six | **0** |
| A10 c fitted | continuous, fitted | the two lepton ratios | **0** |
| A02, A03 the line | discrete, chosen | all six | **0** |
| A04 the Higgs direction | discrete menu, chosen | all six | **0** |
| A05 the reading | discrete, chosen | all six | **0** |
| A07, A09 the end and the weights | chosen (a continuous family behind it: finding V4) | all six | **0** |
| A08 H = I | chosen | all six | **0** |
| A11 one address | chosen | all six | **0** |
| A12 scale and scheme | chosen | all six | **0** |
| S01 flat bundle | ansatz | all six | **0** |
| S02 orientation | chosen | all six | **0** |
| no lock on B1841, B1839, B1838 | enforcement | all six | 0 |
| 12 text-only locks on the code chain | enforcement | all six | 0 |
| B1840 has no verdict | enforcement | all six | 0 |
| the nulls' τ window (finding V1) | statistics | the specificity claim | 0 |
| the 10% floor (finding V2) | statistics | the fit claim | 0 |
| six thread results under a weave head | weave discipline | all six | 0 |

**The map's first lesson: the conditions are in series.** Every joint feeds every one of the six rows, so closing any
one of them releases nothing. There is no cheap row to win and no order of work that shows early progress on this
frame. A value on this frame is derived only when τ, the line, the Higgs direction, the reading, the end, the metric
and the scale are all forced together.

**That is the owner's claim restated as a requirement.** "One self-consistent outcome" means these are not eleven
separate problems: one construction must fix them jointly. The map therefore points away from attacking the joints
one at a time and toward the question of item 3 of the seat's plan — what "self-consistent" means exactly, and which
single construction would force the whole address.

## 7. Two observations from the record's own numbers (no measurement involved)

1. **Two τ on record.** The candidate's row sits at τ₀ = (1/2, 2.9496) (B1841), on the strip the fit found. The τ
   read-out rule's point value at the tube is 0 + 6.07 i to 0 + 6.15 i (B1852, B1854), and the same family's
   Teichmüller apex is 1/2 + 3.65 i (B1852's headline). If the read-out rule is the forced τ, the candidate's row is
   not at it. Whether these are meant to be the same τ is a question for main; the record does not say in one place.
2. **Leads the record holds on single joints, each unverified on main and each found after the fit:** the kernel of
   LR + I of order 5 as a selector of the line (the agy lane), a cover argument for H = c·I (the agy lane), the
   area-4 horocycle for the end (the web seat, B1840). Each needs a sealed check by a reader who does not know which
   value the fit preferred (finding V4's lesson).

## 8. What the dry run changes in the proposals

| Proposal item | Change |
|---|---|
| the derivation graph, edges | typed edges (`uses` / `cites`); only `uses` propagates status |
| the derivation graph, nodes | a "frame choice" node kind between foundation and frame, filled from the scoreboard's joints |
| acceptance row W-a | enumerated `domain` values; a `reduction` field (all rows / a rule fixed in advance / the best row) |
| acceptance row L1 | the closure meant is the `uses` closure; on today's code chain that is 27 arcs, of which 15 need a real lock |
| the map, view 2 | show for each condition the rows released if it alone is closed — on frame A, zero throughout |
| new | every folder named by a `depends_on` has a verdict file (B1840 and the 13 others), enforced by `arc-data` |
