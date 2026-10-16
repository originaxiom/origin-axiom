# What a grammar of records fixes — the paper (draft 3)

A modular flavour triplet, its couplings, and the boundary of what the grammar leaves free. A draft under scrutiny by
the program's seats, not yet submitted. 0 of 19: no value of the Standard Model is derived, and the paper says so.

- `what_a_grammar_fixes.pdf`: the built paper, 36 pages.
- `tex/`: the sources (`main.tex`, `sections/`, `refs.bib`, `figures/`), and `CONVENTIONS.md`, the conventions the
  paper fixes. Records are row vectors, L = [[1,1],[0,1]], R = [[1,0],[1,1]], χ(L) = i, χ(R) = −i.
- `figscripts/`: one script per figure. The data figures read the record's committed outputs and check them by hash.
  The others recompute from stated formulas or are drawn, as their captions say.
- `checks/`: small checks the paper states that are not arcs of the record. Today there is one: LR and RL generate the
  commutator subgroup of SL(2, ℤ).
- `build.sh`: rebuilds the figures, runs the checks, and builds the PDF (needs Python with numpy, scipy, sympy, mpmath,
  matplotlib, and latexmk).

**Status.** Four hostile reads have been applied, and the bibliography has been checked entry by entry. Every claim
cites the arc of the record that computes it. The seats are asked to scrutinise it
(`docs/handoffs/CC_TO_ALL_SEATS_2026-10-16_SCRUTINISE_THE_PAPER.md`).
