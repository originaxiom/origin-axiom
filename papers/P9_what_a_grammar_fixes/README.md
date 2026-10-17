# What a grammar of records fixes — the paper (draft 8, prepared on the SM-derivation branch)

**Draft 8 (2026-10-17).** An external referee report on draft 6 (findings F1–F5) is applied, and the author is set
at the owner's request.

- **F1, the verification bundle:** `verify.sh` runs 45 lock files (19 added); Appendix A2 says so, and names the one
  cited arc without a lock (B1652's tribunal, printed checks) and the two locks not yet on the main line (W34, W101).
  `build.sh` also runs the positive-words and fixed-length Lyapunov checks.
- **F2, the layout:** the appendix tables come before the References; the glossary is a longtable.
- **F3, the parity labels:** §4's convention sentence was backwards and is corrected against the record's code
  (L fixes the parity (0,1), the line (+,−)).
- **F4, the first-passage estimator:** the size and sign of its difference from a fixed-length estimate are stated.
- **F5, precision:** §3's proof of (3) defines its space and lifts; the braid relation is stated exactly; Proposition 19
  and the tilde map are stated as computed; Lemma 21 is stated in SL(2, ℤ).

**Draft 7 (2026-10-17).** The owner asked this branch to update the paper while main was unavailable. The base is
main's draft 6 at `2e5716bd9`, imported unchanged in the commit before draft 7's, so `git diff` against main's tree
shows exactly the edits. Main has not reviewed them; they are for main to port, amend or decline.

- **§4.1, new:** the half floor at weight one (Corollary, from B1635 and B1636); the determinant character
  det ρ = χ_η⁹; the moves' anomaly (free with QCD exactly for a vectorial action, never with SU(2), gravity needs ν^c);
  the couplings' determinants and the strong angle, with and without a Dedekind counterterm (W101).
- **§8, new paragraph:** the measurer inside the weave (the composition lemma; no thread keeps a record, W34).
- **§10, new:** a third kind of link (consistency), and a reading of the measurer.
- **Elsewhere:** the abstract, the introduction (a sixth item and a bullet), Table 1 (two inputs, one purchase
  extended), Appendix A2 (three rows), A3 (W101's failed control) and A4 (three names). There are ten new references,
  each checked against arXiv or Crossref.

A modular flavour triplet, its couplings, and the boundary of what the grammar leaves free. A draft under scrutiny,
not yet submitted. 0 of 19: no value of the Standard Model is derived, and the paper says so.

- `what_a_grammar_fixes.pdf`: the built paper, draft 8.
- `tex/`: the sources (`main.tex`, `sections/`, `refs.bib`, `figures/`), and `CONVENTIONS.md`, the conventions the
  paper fixes. Records are row vectors, L = [[1,1],[0,1]], R = [[1,0],[1,1]], χ(L) = i, χ(R) = −i.
- `figscripts/`: one script per figure. The data figures read the record's committed outputs and check them by hash.
  The others recompute from stated formulas or are drawn, as their captions say.
- `checks/`: five small checks the paper states that are not arcs of the record: the commutator subgroup, the cusp
  law, the fixed-length Lyapunov estimate, the positive words, and the sources' hygiene.
- `build.sh`: rebuilds the figures, runs the checks, and builds the PDF (needs Python with numpy, scipy, sympy, mpmath,
  matplotlib, and latexmk). `verify.sh` runs the checks and the 45 locks of the cited arcs.

**Status.** Four hostile reads have been applied, and the bibliography has been checked entry by entry. Every claim
cites the arc of the record that computes it. The seats are asked to scrutinise it
(main's handoff CC_TO_ALL_SEATS_2026-10-16_SCRUTINISE_THE_PAPER.md, in main's docs/handoffs/).
