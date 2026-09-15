# Reader r7 — Memo 210 (`memos/THE_PRINCIPAL_TORSION.md`)

## 1. HEADLINE

"L72 PHASE 1 DONE — THE E₆-PRINCIPAL TORSION COMPUTED, AND THE SIX BLOCKS OBEY A LAW." No
per-memo date line in body; INDEX.md row 308 records "banked 2026-09-12." Includes ADDENDUM 1
(2026-09-13): "§7's TWO SUCCESSORS ARE ANSWERED (memo 221)." CELL 1/2/3 = A/A/A, controls
C1–C5 pass.

## 2. CLAIMS

1. B581 banks six exact polynomials/torsions `τ_m` but never forms the product; searches for
   "product of the six"/"Π tau_m"/"principal torsion =" found only the L72 registration and
   B579's handoff naming it as the next step. Grade: documentary gap-finding, exhausted-first.
2. Controls: C3 (all six structurally integer-coefficiented, skew-palindromic, `Δ_m(1)=0`,
   degrees 3/9/11/15/17/23); C2 (B581's own analytic gate re-derived: `Δ₁(t)=(t−1)(t²−5t+1)`,
   `τ₁=−3`, B425's banked value); C1 (all six `τ_m`, including every banked factorization
   string, recomputed from B581's own JSON and matched exactly); C5 (`sign(τ_m)=(−1)^m` 6/6).
   Grade: all PASSED.
3. **CELL 1 = A**: `deg Δ_E6 = 78 = dim E6` (blocks tile the adjoint 3+9+11+15+17+23=78,
   asserted as a gate); vanishing order at t=1 is exactly 6 = rank E6. Grade: OUTCOME A, exact.
4. **CELL 2 = A**: Route A (`Πτ_m`) and Route B (`Δ_E6^(6)(1)/6!`) agree **exactly as
   integers** — an 87-digit number `τ_E6 = 2^61·3^20·5^5·7^17·11^4·13^5·17·19^2·31·43·73·97·
   149·151·607·1471·49297·160453 ≈ 2.9246427×10^86`, sign +, forced by
   `(−1)^{1+4+5+7+8+11}=(−1)^36=+1` ("the chirality fold"). Grade: OUTCOME A, exact match.
5. **CELL 3 = A**: with `Vol=Vol(4_1)=2·Cl₂(π/3)`, `R_m := log|τ_m| − (Vol/π)m(m+1)` has spread
   0.01232 over m∈{4,5,7,8,11} against a preregistered threshold 0.05 (m=1 excluded, reported
   separately as not-yet-asymptotic). Control C4 (wrong law `m²` spreads 4.51, ~2.5 orders
   wider) shows the statistic discriminates. Grade: OUTCOME A.
6. Post-hoc (labelled as such, not preregistered): least-squares fit gives leading coefficient
   `A/(Vol/π)=1.000782` (verifies Menal-Ferrer–Porti/Müller's `log|tor(Sym^n)|/n² → Vol/4π` to
   four figures) and subleading `B/(Vol/π)=0.986196` (suggestive of exactly `Vol/π`, "not a
   proof"). Constant term explicitly **not identified**, citing the B583-X2 PSLQ-overclaim
   precedent as a reason for caution. Grade: post-hoc, explicitly fenced.
7. Fence (interpretive, adopted from the seal, "not discovered here"): B1157 already banked that
   the Vol-scaling reading is "generic spectral geometry... generic to all finite-volume
   hyperbolic 3-manifolds" — so CELL 3 checks B581's data against a generic law, not an
   object-specific fact. What IS object-specific: which six exponents appear (E6's fact), the
   degree=dim, vanishing-order=rank, and sign=+ from exactly two θ-odd exponents. Grade:
   self-scoping/negative.
8. Status: L72 phase 1 DONE; phases 2–3 already ran elsewhere (`B775_phase2_wave1/cells/
   P2W5-L72/`, memo 208 §2) with a flagged issue explicitly untouched here. Grade: scope
   statement.

**ADDENDUM 1** (2026-09-13, owner supplied Müller arXiv:1003.5168 and Menal-Ferrer–Porti
arXiv:1110.3718):

9. Linear coefficient is **exactly** `Vol/π` — Müller's sharp formula gives the combination
   `m(m+1)` directly (his Thm, §8); the fitted 0.9862 "is 1." Grade: PROVED (upgrade of claim 6
   from suggestive to exact, via literature).
10. Scope carried explicitly: Müller's Thm 1.1 is for **closed** manifolds; Menal-Ferrer–Porti's
    cusped theorem is leading-term only; `4_1` is cusped, so the refinement is **unproved** for
    it — "evidence for an extension rather than a check of a theorem." Grade: honest scope
    fence, self-imposed.
11. "The constant — there is none": Müller identifies it as a bounded, decaying Ruelle sum; §5's
    "not identified, no identification attempted" was "right for a better reason than it knew."
    Grade: resolved/PROVED (there is no constant to identify).
12. The unexplained drift in §4 IS that Ruelle sum: extracted terms `log|R10(5)|=+0.01046`,
    `log|R16(8)|=−0.000247`, falling by 42.361 over three steps (vs `e^{3ℓ0}=26.081`,
    `e^{3.5ℓ0}=44.914`), and the sign flips, "as an oscillating geodesic sum must and a constant
    cannot." Grade: mechanism identified, consistent with an oscillating sum.

## 3. CERTIFICATE

- `certificates/l72_phase1.py` — EXISTS. `outputs/l72_phase1.txt` — EXISTS; tail matches the
  memo's §5/CELL-3 table exactly (per-m `(Vol/4π)(d²−1)` and `R_m` values), ends "THE CONSTANT
  IS NOT IDENTIFIED, AND NO IDENTIFICATION IS ATTEMPTED... DONE."
- `seals/L72_PHASE1_PREREG.md` — EXISTS; **sha256 recomputed and matches exactly**:
  `962d708047fb5e47f761a41bdb952dd75c0bf8189b0c109771cb1805cd7dcf7e`, committed/pushed before
  the certificate, as claimed.
- ADDENDUM 1's claims (9–12) rest on the two named arXiv papers (Müller, Menal-Ferrer–Porti),
  not on a new certificate/output pair — no new script/output is named for the addendum, so
  there is nothing further to check for file-existence beyond the arXiv IDs themselves, which I
  did not fetch (out of scope for a 2-minute compute limit and not required by PROMPT.md).

## 4. ON MAIN ALREADY?

- **(b) Applied via the merge as a citation inside `docs/OPEN_LEADS.md`.** L72's row
  (`docs/OPEN_LEADS.md:531`) is struck through and annotated: "[SUPERSEDED IN PLACE 2026-09-12 —
  outside-bench memos 206/208/210/211/213/214/215...]" followed by "**SUPERSEDED — phases 2 and
  3 have run**... Phase 1's product is now computed (memo 210: deg Δ_E6 = 78 = dim E₆, vanishing
  order 6 = rank E₆, τ_E6 an 87-digit positive integer, two routes agreeing exactly)" — verified
  by direct read, quoting memo 210's own numbers accurately.
- L54's row (`docs/OPEN_LEADS.md:271`) is *also* annotated with the same supersession bracket and
  cites memo 210 directly: "The E₆-principal product itself is now computed: memo 210." —
  confirmed by direct read.
- **The 87-digit integer `τ_E6` itself does NOT appear anywhere else on main** (grep for the full
  digit string across the whole repo, excluding `outside_bench/`, returns zero hits) — so while
  the *existence and headline numbers* (78, 6, 87-digit, agreement of two routes) are cited in
  `docs/OPEN_LEADS.md`, the actual integer/factorization has not been copied into any
  `frontier/B*` FINDINGS.md or `docs/` table. This is (b) for the citation, but the underlying
  number itself remains only in `outside_bench/outputs/l72_phase1.txt`.
- `frontier/B579_session_handoff/FINDINGS.md`, `frontier/B770_closure_census/census.json`,
  `frontier/B775_phase2_wave1/PREREG_WAVE5.md`, `frontier/B423_gateB_torsion/gateB.py` all
  mention "principal torsion" / "tau_E6"-adjacent language — these are the **pre-existing**
  arcs the memo builds on (B581's six polynomials, B425's `τ₁=−3`), not competitors; consistent
  with the memo's own account.
- ADDENDUM 1's claims about Müller/Menal-Ferrer–Porti: I did not find any main-side arc that
  independently engages these two papers outside `outside_bench/` — so those specific literature
  claims are (c) NOT independently corroborated on main (they rest solely on this bench's
  reading of the two PDFs, supplied by the owner per register R129).

## 5. NEEDS COMPUTATION HERE

- Claim 4 (τ_E6, 87-digit integer, two routes agree): NEEDS COMPUTATION — cheap, exact integer
  arithmetic. A verifier should recompute `Δ_E6(t) = Π_m Δ_m(t)` from B581's six banked
  polynomials, compute `Δ_E6^(6)(1)/6!` symbolically, and confirm both routes give the identical
  87-digit integer with the stated factorization. This is the single most load-bearing exact
  fact in the memo and is trivial to re-verify with `sympy`.
- Claim 3 (degree=78, vanishing order=6): NEEDS COMPUTATION — same recomputation, check
  `deg(Δ_E6)=78` and the order of the zero at `t=1`.
- Claim 5 (R_m spread 0.0123 vs wrong-law 4.51): NEEDS COMPUTATION — recompute `log|τ_m|` for
  the five tail m's from B581's exact values and the volume `Vol(4_1)=2Cl₂(π/3)` to sufficient
  precision (mpmath, 30+ digits), confirm the spread figures.
- Claim 9 (linear coefficient exactly Vol/π, via Müller): this is a LITERATURE claim, not an
  in-sandbox computation — DOCUMENTARY. A verifier should independently read Müller's §8 formula
  and confirm it indeed yields the `m(m+1)` combination as claimed, rather than recomputing
  numerically (the numerical fit was already done in claim 6/§5 pre-addendum).
- Claim 11 (no constant, it's a Ruelle sum): DOCUMENTARY — recompute the extracted terms
  `log|R_10(5)|`, `log|R_16(8)|` if the Ruelle-sum formula from Müller can be reconstructed
  in-sandbox in <2 minutes; otherwise flag as needing the literature to check the formula, not
  a fresh derivation.

## 6. SUPERSESSION

- Not superseded; this memo is itself cited as the superseding write for L72 and L54's OPEN_LEADS
  rows (register R117/R118 correspond to this memo's banking, per the owner-register R-numbering
  observed around 2026-09-12).
- ADDENDUM 1 (2026-09-13) upgrades §6/§7's "post-hoc, suggestive" reading to "exact, proved from
  the literature" for the linear coefficient, and resolves the "constant not identified" fence by
  showing there is no constant — this is a self-superseding upgrade, explicitly flagged in the
  memo ("Nothing in §§1–6 changes" except the two named successors).
- No later main arc contradicts any of memo 210's numbers.

## 7. GRADE PROPOSAL

**REPRODUCE-AND-BANK.** The 87-digit `τ_E6` integer, its two-route exact agreement, the
degree=dim/vanishing-order=rank facts, and the R_m growth-law spread are all cheap, exact,
control-disciplined computations that are cited-but-not-copied into main (the number itself
lives only in `outside_bench/outputs/`) — this is exactly the kind of finding worth a dedicated
`frontier/B*` arc row with the integer and its factorization written into `FINDINGS.md` so it
does not remain sourced only from the outside-bench lane. The literature-sourced claims in
Addendum 1 (exact `Vol/π` coefficient, no constant) should additionally be independently
confirmed by reading Müller's formula directly, since currently only this bench has read it.
