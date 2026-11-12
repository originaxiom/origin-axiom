# SM-C4 — the parameter inventory: names, kinds and what each rests on, with no value on the page

*Card proposed by this seat (M3 on main's docs/seats/sm.md: "the parameter inventory is yours to propose as a card").
A card of a seat's own waits for main's word (§ 6). Proposed at main 0dda7b472, after SM-C3 was delivered.*

## 1. The package and the question

What are the free parameters the record's count of nineteen refers to, and the neutrino sector beside them? For each:
- what kind of parameter it is;
- how it is defined, with its scheme and scale;
- what in the record rests on it, or claims it.

This is part of the first step of WP-4.4 in main's PROGRAMME.md, the names and kinds. WP-4.4 itself is main's and the
owner's: the bar, the null and the look count are not in this card.

## 2. What will be delivered, and what done means

- **One table,** relays/SM_C4_INVENTORY.md, with one row per parameter: the 19 of the Standard Model with massless
  neutrinos, and the neutrino sector's 7 (Dirac) or 9 (Majorana) beside them. Each row has six columns:
  - **its name,** with its usual symbol;
  - **its kind:** gauge coupling, Higgs-sector parameter, fermion mass, quark mixing angle, CP phase, the strong
    vacuum angle, neutrino mass, lepton mixing angle or Majorana phase. Each is also marked dimensionless or
    dimensionful;
  - **its definition,** with the scheme and scale a value would have to name: running, pole or a ratio. Where the
    usual definitions differ, all of them are listed and none is chosen;
  - **what it rests on in the Standard Model:** which term of the Lagrangian it sits in, and which field
    redefinitions remove its siblings;
  - **what the record says about it:** each frame or arc on main that claims it, or names it as out of reach. Each
    gets the grade the record gives it, the GENESIS item it hangs on where there is one, and a harvest or register row;
  - **"no frame claims it"** where none does.
- **The count, computed separately, from the field content alone.** This is a script under relays/sm_c4/, committed
  before the table. It counts the real parameters of the Yukawa matrices less the dimension of the flavour symmetry
  they break, plus what that symmetry leaves unbroken. This is done for:
  - quarks and charged leptons;
  - Dirac neutrinos;
  - a Majorana mass term.

  The table's rows must match these counts.
- **Done means** the table and the script committed, with a note saying which card it closes and what was left out.

## 3. What would count as wrong (written before any table or run)

- **A row count that differs** from the computed count, in any sector.
- **A row with a number in its definition columns:** a measured value, a fit, a central value or a range. The only
  numbers allowed are counts, a group's dimension, and a scale named by its symbol (μ, M_Z), never with a figure.
- **A definition that names no scheme** where the parameter's value depends on one.
- **A "what the record says" entry** that grades a claim above the record's own grade, or cites an arc that does not
  name the parameter.
- **Two rows that are one parameter** under two names. Two names for one row must be said in that row.

## 4. What it rests on, and what it must not touch

- **It rests on:**
  - the Standard Model's Lagrangian and field content (for the definitions and the count);
  - the record on main: GENESIS, the frames' arcs, PROGRAMME.md, the harvest ledger and the point register;
  - this seat's own record.
- **It must not touch:**
  - **any measured value or held-out target.** § 9's firewall holds in full. No value is written, looked up,
    computed or compared, and the page carries none;
  - **any file with agy_ in its path,** any file that audits another lane's values, and any file of targets;
  - **GENESIS and CLAIMS.** They are read, and never edited.

## 5. One control that must fail if the work is broken

**Planted errors against the table's own checks,** in a scratch copy:
- a sector's row deleted, which the count must catch;
- a number written into a definition cell, which a scan of those cells must catch;
- one parameter entered twice under two names, which a check of the symbols against the Lagrangian's terms must catch.

The count of plants caught is reported. If any passes, the table is withheld until the check is mended.

## 6. What is needed from main

- **Main's word on the card** (§ 6). This includes whether its scope is the one meant by "names, kinds and what each
  rests on".
- **Which of main's files may be opened** for the "what the record says" column without touching a target.
  docs/FRAMING_LEDGER.md, docs/TOTAL_INPUTS_SCOREBOARD.md and their JSON files carry test commitments, and may carry
  values. Until main says, this seat opens neither, and the column is built from the arcs, GENESIS, PROGRAMME.md and
  the harvest ledger alone.
