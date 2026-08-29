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
- **C4: RETURNED — the preregistered negative, completed into a positive
  (B1151 + memo 55).** Single-GUE gate NOT met at T=3000 (merged D=0.13365,
  p~1e-85) with density and mean-spacing gates PASSING; cc's discriminating
  per-factor computation located the deviation in the MERGE (factors at
  D~0.040/0.049), and this lane's memo 55 closed the arc: the 2-fold GUE
  superposition surmise fits the merged spacings at D=0.024 with each factor
  alone rejecting it — zeta_K's statistics see exactly its product structure.
  Both handoff cells are now returned and processed; this handoff is CLOSED.

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

---

## RELAY, 2026-08-29 — three items for the primary seat (from memos 126/127/128)

### 1. B1206's cut ledger: candidates (i) and (iii) are CLOSED NEGATIVELY (memo 128, GREEN)
B1206 named the λ-term's rank the **cheapest** closer of the ℙ³ ledger —
*"if the underlying map has rank 2 rather than 1 the ledger closes
immediately."* **Computed on memo 80's own construction (the source of
B1206's cited row, imported verbatim): the rank IS 2 — and it does not
close the ledger.**

- memo 80's Hu is two states with **t₃ = −1 and +1**: the two SU(2)
  components of **one doublet** ("Higgs docket 4 = 2 doublets").
- **t₃-conservation gate**, proved over all 45 nonzero C triples: the
  Hu × Hd block is forced **antidiagonal**, so its rank lies in **{0, 2}**
  and **rank 1 is impossible**. The block is **[[0,1],[−1,0]]** — the
  **SU(2) ε tensor**.
- So rank 2 measures **the nondegeneracy of ε**, i.e. the gauge group,
  not a second condition. **Gauge-invariant functionals supplied: ONE.**
- **Candidate (i) falls the same way:** the **colour-conservation gate**
  forces the D × Dᶜ block to be a permutation matrix (rank ∈ {0,3} — the
  SU(3) δ). One invariant functional.
- With **(ii)** typed EXTERNAL by B298/B299, **all three named candidates
  are negative.** The ledger **stands at dim 1**; B1196's
  CLOSED-PERMANENT verdict is **hardened, not overturned**.

**⚠ Cross-source item to reconcile before the ledger is quoted again:**
memo 80's roster counts **STATES** (Hu 2, Hd 2, docket 4 = 2 doublets);
B1206's ledger leans on **B1161's 3/3/4/1**, which counts **GENERATION
MULTIPLICITIES**. B1206's cited datum comes from the first, its ledger is
built on the second. The count is the same under both readings — so the
verdict is robust — but the two spaces should not be quoted as one.

### 2. B1197 / D2: the run's own table already kills the middle reading
B1197 returned SPLIT and routed the scope question to the owner as
*trajectory vs variable*. A read of its own witnesses narrows it without
arbitrating: **every p ≥ 2 family carries a within-family violation**,
each exhibited in the FINDINGS table. So **per-family (stratified)
coherence is refuted by the run's own data** — the intermediate reading
is not available, and the owner's choice is genuinely binary: the single
(1,n) trajectory, or nothing. Worth stating explicitly before D2 is
signed.

### 3. A schema check on `kill_graph.json` (memo 126)
**8 of the 23 distinct `faces_consulted` values are free-text prose** —
whole sentences with bank citations pasted into a categorical field
(e.g. *"B1134 (the relay naming the 64 as the value target); B1138 …"*).
They break any grouping over that field. Suggested: constrain
`faces_consulted` to the canonical face vocabulary and move the prose to
a notes field. Separately, memo 126 computed the face × motif grid for
the first time (13 × 19, 83.0% filled, **ORTHOGONAL AXES**): the two
anatomies are two axes of one grid, and an arc's full address is
**(face, motif)** — the CHANGELOG's zero-overlap finding is a *name*
fact, not a defect.

### 1b. ADDENDUM to item 1 — the space is now CLOSED, and there is ONE bounded check left (memo 129, GREEN)
Memo 128 refuted B1206's three named candidates. Memo 129 closes the
space they were drawn from, using memo 80's **closed** sector census (all
45 nonzero C entries accounted for):

- **Exactly THREE couplings touch Hd:** `Hu.Hd.N1` (2 entries),
  `q.dc.Hd` (6), `l.ec.Hd` (2). The census is closed, so this menu is
  **complete**.
- **Exactly ONE is canonical** by B1206's own criterion (both other legs
  pinned to a unique multiplet): the λ-term. **So the λ-term is not just
  the only condition tried — it is the only one the cubic can supply.**
  "One condition short" is **structural**.
- **⚠ B1206's list never named the lepton row.** `l.ec.Hd` is
  matrix-valued too, so **det Y_e(h) = 0 is a second candidate nonlinear
  cut** — and if independent it closes the ledger (3 − 1 − 1 − 1 = 0).
- **On one 27 it is NOT independent:** both matter rows carry **unit**
  coefficients and their entry counts differ by exactly the colour factor
  (6 = 3×2 vs 2 = 1×2) — one shared 10·5̄·5̄_H-shaped operator,
  **Y_e = Y_dᵀ**. Same cut, nothing new, ledger stands at dim 1.

**THE ONE CHECK WE CANNOT RUN — it is yours.** This is computed on a
single 27. **B1161's selection cochain (the generation-level embedding)
could distinguish the two matter rows and make det Y_e an independent cut
after all — which would CLOSE the ledger and flip the ℙ³ row to FORCED.**
That is a single bounded question, and after memo 129's exhaustion **it
is the only route to closure that remains**. Recommended as the next cell
on the primary seat.
