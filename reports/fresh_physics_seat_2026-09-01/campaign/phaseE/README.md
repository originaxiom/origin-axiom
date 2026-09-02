# Phase E — the reader red flags, verified at the source

Phase B's readers raised 2494 red flags; the seat re-verified only the ones it promoted into the synthesis. The four
kinds that bear on the thesis (the owner's T2 rule: "a bit-vs-value type match is a licence to ask, not evidence")
are worked here: IDENTIFICATION_BY_TYPE 161, SELF_REFERENTIAL_LOCK 128, CLAIM_EXCEEDS_COMPUTATION 65, FITTED_VALUE 36
(390 flags over 369 arcs/tests/log entries; 62 packets in `packets/`).

- **E-1 (agents, mechanical):** for each flag, locate the text, decide whether the flag's premise HOLDS, and classify
  SELF_CAUGHT (the arc names and fences it) / UNCAUGHT (asserted as a result) / RETRACTED_LATER / FLAG_WRONG, quoting
  the decisive lines verbatim (`workflow_phaseE_flags.js`, run wf_c88d8365-b92).
- **E-2 (seat):** every UNCAUGHT flag is read and judged: does the identification sit on the thesis spine
  (combinatorics → m004 → arithmetic → E6 → SM bookkeeping), and what does the computation actually license? The
  result is an identification ledger for the relay, plus R-cells where a number can be checked.
