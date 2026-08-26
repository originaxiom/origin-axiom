# COMPUTE HANDOFF → the banking seat (i9 / 64 GB) — the two hours-scale C-lane cells
## (outside bench, 2026-08-25. Owner-approved split: cc runs the long computations locally; the cloud seat executes the rest. Both scripts are resume-safe (checkpoint files), deterministic, and carry their preregistered gates in the docstring — run them as-is, iterate freely, bank on your side with the usual two-bench credit.)

### STATUS UPDATE 2026-08-26 (from main @ 9d6979db, B1147)
- **C3: RETURNED — HONEST NEGATIVE, exactly per the preregistered gate.** The
  seat ran the full N = 400…4000 ladder at 120 dps (19 rungs, raw values banked
  in B1147 `verification/c3_ladder.txt`). Sanity anchor c₀·3^{1/4} = 1 exact to
  ~20 digits: GREEN. c₁/c₂ recognition: only ~17/13 stable digits at N=4000 —
  fails the ≥60-digit gate; PSLQ returns spurious million-size coefficients.
  **NOT-RECOGNIZED at this depth — banked as the preregistered negative
  (B1147).** Continuation named: extend the ladder well past N=4000 and/or
  raise dps; the convention-free raw ladder is banked for that restart.
  This lane's outcome ledger: C3 CLOSED-NEGATIVE at this depth.
- **C4 (large-T GUE): still grinding on the i9; banks separately.** Gates
  unchanged below.

### C4 — large-T GUE for ζ_K = ζ·L(χ₋₃)  (`certificates/c4_gue_larget.py`)
- **What:** the preregistered continuation of the banked `gue_bench.py` down payment
  ("re-run at much larger T before drawing any conclusion"). Default T = 3000
  (≈5,400 merged zeros — vs 108 at T=130); `python3 c4_gue_larget.py 3000`.
- **Gates (preregistered):** unfolded mean spacing within 0.01 of 1; verdict
  GUE-consistent iff p_GUE > 0.01 AND p_Poisson < 1e−6 AND D_GUE < D_Poisson;
  otherwise bank the negative honestly. Density gate: merged count vs
  N(T) = (T/π)log(T√3/(2πe)) within O(log T).
- **Cost:** ζ zeros via `zetazero` are cheap; the L(χ₋₃) scan dominates —
  expect a few hours at T=3000 on the i9. Checkpoints: `c4_zeros_zeta.txt`,
  `c4_zeros_L.txt` (safe to kill + re-run; it resumes).
- **Standing caveat to carry into the bank note:** GUE is generic
  (Montgomery/Katz–Sarnak, B1142) — this certifies the universality class at
  scale, never object-specificity. The interesting failure mode is the
  density gate, not the spacing gate.

### C3 — Kashaev/Ohtsuki ladder at large N  (`certificates/c3_ohtsuki_large.py`)
- **What:** ⟨4₁⟩_N on the ladder N = 400…4000 (step 200) at 120 dps;
  strip N^{3/2}·e^{N·Vol/2π} (Vol computed in-run as 2·Cl₂(π/3), not pasted);
  fit the 1/N series; extract c₁ (currently PROVISIONAL at ~30 digits) to a
  target ≥60 stable digits and c₂ to first recognition; PSLQ both against the
  preregistered frame {1, π, 1/π, √3, Vol, mixed} with maxcoeff 10¹².
- **Gates (preregistered):** stability = digits agreeing between two shifted
  fit windows (printed); recognition requires ≥60 stable digits; c₀·3^{1/4} = 1
  is the sanity anchor. NOT-RECOGNIZED is a bankable outcome.
- **Cost:** the ladder is O(N) per rung at 120 dps — roughly an hour or two
  total on the i9; checkpoint `c3_ladder.txt` (resume-safe). If stability
  digits come out low, extend the ladder (edit `NS`) and/or raise `mp.dps` —
  the script is deliberately simple to iterate on.
- **Convention warning (important):** before comparing constants with the
  banked record, align the expansion convention with `DEFLATION_RUN` /
  `ASYMPTOTIC_CHANNEL` (the corpus's C₀…C₄ tower uses its own normalization).
  The raw ladder values in `c3_ladder.txt` are convention-free — bank those
  alongside whatever constants you extract.

### What the cloud seat is running meanwhile (no overlap)
C1 (the VI.3(a) Weyl-law coefficient, derived symbolically + validated on the
108-zero census) and C2 (the Habiro/cyclotomic tower for 4₁, exact in ℤ[ζ]).
Results land as memos 38/39 on this branch.
