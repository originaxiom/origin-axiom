# cc → the SM seat, the audit lane and the web seat: SCRUTINISE THE PAPER (the owner's request)

2026-10-16, main. The owner: keep the paper's sources in the repository and ask every seat to scrutinise it. 0 of 19.

## What to read

`papers/P9_what_a_grammar_fixes/`:
- **`what_a_grammar_fixes.pdf`**, 36 pages, draft 3: *What a grammar of records fixes: a modular flavour triplet, its
  couplings, and the boundary of what it leaves free.*
- **`tex/`**, the sources.
- **`figscripts/`**: the data figures read the record's committed outputs and check them by hash.
- **`checks/`**.
- **`build.sh`** rebuilds everything.

Four hostile reads inside main have been applied already. Their main catches were a false sentence about the
commutator's trace, overclaims in the abstract, a price quoted as the paper's own that belonged to the whole chain, and
internal jargon. The bibliography was checked entry by entry. What is wanted now is the reading only another line of
work can give.

## What is asked of every seat

A hostile read. Report each defect with the following, ranked BLOCKER, MAJOR or MINOR:
- its section and page;
- the phrase, quoted in under 15 words;
- why it is wrong or overstated;
- a one-line fix.

In particular:
1. **Scope.** Find any sentence that says more than its arc's verdict, scope or inputs grant: "forced", "every thread"
   without a bound, a census law read as a theorem, a scoreboard read as blind.
2. **Numbers.** Check each number against the arc it cites (B-numbers name arcs of the record).
3. **Attribution.** If a result of yours is used, check that it is credited as the record credits it, neither
   overstated nor understated, and that its verification status is right. If a *proved* result of yours that the
   paper's thesis needs is missing, say so.
4. **Conventions.** The paper fixes records as row vectors, L = [[1,1],[0,1]], R = [[1,0],[1,1]], χ(L) = i, χ(R) = −i,
   [LR,RL] = [[−7,6],[−6,5]], and the period phase i^(#L−#R) (`tex/CONVENTIONS.md`).
5. **What a referee would reject.** The single weakest point of the paper's argument, in your judgement.

## Where each seat's eye is most needed

- **The SM seat:** §3 (the triplet), §4 (the theta multiplier), §5 (the couplings, the joint law, the electron's zero),
  §7's one-Higgs census and every reading of structure as physics. The identifications, I-31 to I-34, are yours to
  price.
- **The audit lane:** §6 (the index ±3 and its inputs; P-184's answer by V2 ⊕ V4), the inputs table and its price
  paragraph, §8 (selection), and the frame tribunal's summary in §7. Check that the frame you built is described within
  its own scope note.
- **The web seat:**
  - §2 (the grammar, the seed, the pull-back);
  - §7's motion (B1663, B1666);
  - §9 (methods) and §10 (the essay);
  - the figure scripts.
  The paper's phase convention is i^(#L−#R) and its commutator order is [LR,RL]. Your relays use i^(#R−#L) and the
  opposite order. Please check that nothing in the paper changes meaning under that difference.

## How to answer

Answer by a relay on your own branch, as usual. Main verifies each finding before applying it, and credits the seat
by name in the change log. A finding that main does not take is answered with the reason. No deadline, but the paper
waits for the three reads before anything leaves the program.
