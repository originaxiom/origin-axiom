# Conventions for drafting the paper's sections (all drafters)

- **The build.** LaTeX, `main.tex` with the macros defined there: \SL \PSL \Z \R \C \Hb \tr \adj, and \reading{...}
  for a marked reading box.
  - Theorem environments: theorem, proposition, lemma, corollary, definition, censuslaw, remark.
- **Each section's three movements:** the question in words, then the mathematics (statement, proof or cited proof,
  scope), then at most one \reading{}. A reading never states a result.
- **Labels:**
  - sections: sec:intro, sec:grammar, sec:weave, sec:modular, sec:couplings, sec:three, sec:boundary, sec:selection,
    sec:methods, sec:essay;
  - theorems: thm:seed (T1), thm:triplet (T2), thm:theta (T3), thm:isotropy (T4), thm:covariance (T5), thm:index
    (T6), thm:joint (T7, the joint law), thm:phase (the period phase);
  - boundary results: bd:noindex (B1), bd:reducesnone (B2), bd:clock (B3), bd:tribunal (B5), bd:census (B6),
    bd:strength (B7), bd:layers (B8);
  - the inputs table: tab:inputs, in section 2.
- **Figures,** to be scripted, referenced as figures/<name>.pdf:
  - fig_chain (the chain and its prices);
  - fig_seed (144 → 1);
  - fig_joint (two defects and three masses);
  - fig_defect (f = |D|/||R||^2 on the fundamental domain);
  - fig_census (B1660's scoreboard);
  - fig_pullback (B1663: side, speed, defect against p);
  - fig_layers (B1666: layer averages, coherence, the cusp family).

  Use \begin{figure}...\includegraphics[width=\linewidth]{figures/<name>}\caption{...}\label{fig:<name>}\end{figure}.
  The caption states the claim and its scope.
- **Citations:** keys from refs.bib only. Never cite what is not in refs.bib. Write [CITE?] if a citation is needed and
  missing.
- **The record:** cite the program's arcs as "B1659" in prose (the record, not a paper), with the repository's
  reference \cite{OriginAxiomRepo} once per section.
- **Scope and grading:**
  - Every claim is scoped as the record scopes it: the frame, "given the triplet postulate", "on W59's lines at
    τ = ω", "to trace 600".
  - Label census laws as census laws, readings as readings, and scoreboards as scoreboards (the data were seen).
  - Never write "derive" for a value. 0 of 19.
- **Words to avoid:** "proves the Standard Model", "explains", "predicts" (for seen data), "unique" without its
  scope, "the object" (say "the root" or "a thread"), vendor or model names, absolute paths.
- **Style:** plain declarative sentences; definitions in words before symbols; no rhetorical questions in
  mathematical sections; British/American spelling consistent with the abstract (American).
