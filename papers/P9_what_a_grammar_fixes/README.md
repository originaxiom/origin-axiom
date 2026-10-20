# What a grammar of records fixes — the paper (draft 9)

**Draft 9 (2026-10-20).** Drafts 7 and 8 were prepared on another line of the record at the owner's request, while
main was away. Main verified them claim by claim, and they are ported here with main's amendments. The record's
CHANGELOG (S145, S146) has the details and the credit.
- **§4.1** (the half floor at weight one; the determinant character det ρ = χ_η⁹; the moves' anomaly; the couplings'
  determinants and the strong angle) cites main's arcs: B1636 and B1671 for the floor and the phase law, and B1674 for
  the anomaly.
  - A sentence on M₆ is corrected: E₆ alone spans it.
  - The strong angle at weights two and three is stated as differing from its free constant term by a multiple of π
    only where CP is conserved, not as "vanishing".
  - θ̄ is noted as one of the nineteen and not fixed.
- **§8.** The proposition "no thread keeps a record" cites B1675 and defines its private states: the kernel of the
  restriction to the puncture, four-dimensional at rank three.
- **N3 (§7)** is scoped as a statement about one thread. The golden rule a → ab, b → a is LP, whose square is LR. The
  weave of all Sturmian wordings is not computed here.
- **Table 1.**
  - The count of two records (GM1) is priced as a postulate.
  - The coherence of the lifts on M₁,₂ is closed to shear-word length 7 after an odd η-twist (B1672).
- **Proposition 1's matrices** are displayed, after a reader's text extraction scrambled the in-line ones.
- **The appendix tables** come before the References (draft 8's F2).
- **The author line** is set at the owner's decision of 2026-10-20 (P-202).
- Draft 8's F1–F5, an outside referee report on draft 6, are kept.
- `verify.sh` runs the checks and 49 lock files.
- A separate session's edits of 18–19 October, which marked six of Table 1's priced inputs as "derived", were checked
  and declined (B1672, B1673).

A modular flavour triplet, its couplings, and the boundary of what the grammar leaves free. A draft under scrutiny,
not yet submitted. 0 of 19: no value of the Standard Model is derived, and the paper says so.

- `what_a_grammar_fixes.pdf`: the built paper, draft 9.
- `tex/`: the sources (`main.tex`, `sections/`, `refs.bib`, `figures/`), and `CONVENTIONS.md`, the conventions the
  paper fixes. Records are row vectors, L = [[1,1],[0,1]], R = [[1,0],[1,1]], χ(L) = i, χ(R) = −i.
- `figscripts/`: one script per figure. The data figures read the record's committed outputs and check them by hash.
  The others recompute from stated formulas or are drawn, as their captions say.
- `checks/`: five small checks the paper states that are not arcs of the record: the commutator subgroup, the cusp
  law, the fixed-length Lyapunov estimate, the positive words, and the sources' hygiene.
- `build.sh`: rebuilds the figures, runs the checks, and builds the PDF (needs Python with numpy, scipy, sympy, mpmath,
  matplotlib, and latexmk). `verify.sh` runs the checks and the 49 locks of the cited arcs.

**Status.** Four hostile reads have been applied, and the bibliography has been checked entry by entry. Every claim
cites the arc of the record that computes it. The seats are asked to scrutinise it
(main's handoff CC_TO_ALL_SEATS_2026-10-16_SCRUTINISE_THE_PAPER.md, in main's docs/handoffs/).
