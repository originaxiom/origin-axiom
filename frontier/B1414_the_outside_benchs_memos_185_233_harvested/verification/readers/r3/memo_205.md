# Reader r3 — memo 205 (L142_THREE_FACTS)

## 1. HEADLINE
"L142 ANSWERED — THREE FACTS, THE AGREEMENT IS OF OUTPUTS — and the successor
question now has an answer." **2026-09-12.**

## 2. CLAIMS
1. Two proposed morphism tests are rejected before the run as vacuous/basis-only:
   `GL₂(ℚ)`-equivalence of the cubics is VACUOUS (3-transitivity of PGL₂(ℚ) on ℙ¹ +
   Galois-stable root triples ⇒ cannot fail, MB12); `GL₂(ℤ)`-equivalence would
   measure basis conventions (B866's rescaling example cited). — **stated as a trap, rejected pre-run**
2. **CELL 1 = B**: `Hom_{e6}(27,78) = 0` by Schur — μ's site (adjoint 78) and
   B969's/this bench's site ((x14,x22), the matter 27) are inequivalent irreducible
   representations, so no morphism between them can exist. — **PROVED (theorem, not search)**
3. **CELL 2 = B**: within the 27, the two pencils are NOT conjugate — kernel
   invariant differs ((0,3) vs (0,3) but charpolys differ), rank_product (27,24) —
   no `T ∈ GL(27)` carries one to the other; positive and bite controls both fire. — **PROVED**
4. **CELL 3 = B**: six sites/constructions (x8, x16 on compact kernel; two
   (x14,x22) branch cubics; μ itself; B866's adjoint-pencil μ as C4 reproduction),
   each an irreducible cubic over ℚ with resolvent squarefree part 77, **all
   generate K**; the bite control (unrelated resolvent-77 cubic) correctly returns
   "does not generate K." — **VERIFIED (6 positive instances + 1 negative control)**
5. C6 (added mid-run, verified): K's smallest model `x³−12x−5`; μ factors over it as
   `[1,2]`, so both models generate the same field. — **VERIFIED**
6. **THE ANSWER: L142 = THREE FACTS, THE AGREEMENT IS OF OUTPUTS.** — **stated verdict**
7. **The successor question ("what property of the charge space makes every
   construction return the same cubic") is answered by memo 204**: the common
   cubic IS the object's trialitarian invariant `L`, attached to its D₄ by
   `π*: H¹(F,G₀⋊S₃)→H¹(F,S₃)`. — **imported from memo 204, not this memo's own computation**
8. Three instrument failures recorded, all in controls not cells: coefficients to
   ~5×10¹¹ stalling factoring (fixed via smallest model); dense-random-matrix and
   unimodular-replacement positive controls both had entries that grew too large
   (fixed via a permutation conjugator, verified `T·Tᵀ=I` and non-trivial). — **instrument-fragility findings, not math claims**
9. Explicitly NOT done: does not prove no relation of any kind between the sites,
   only no morphism of the two named kinds; produces no value/ratio/prediction;
   does not bear on B882 beyond what memo 204 already settled. — **explicit scope limit**

## 3. CERTIFICATE
`outside_bench/certificates/l142_three_sites.py` exists.
`outside_bench/outputs/l142_three_sites_out.txt` exists. Its final verdict block
(quoted): *"L142 ANSWERS: THREE FACTS. THE AGREEMENT IS OF OUTPUTS."* followed by
a full restatement of CELL 1/2/3 = B/B/B and the residue/successor framing — this
**agrees exactly** with the memo's headline and claim 6.
**Seal**: `outside_bench/seals/L142_THREE_SITES_PREREG.md`, memo states sha256
`8226e745503a63b0115e612800c19ec14893e0d7adad4a9f1b3357f387d36d87`, sealed before
the certificate was written. Computed here: `shasum -a 256
outside_bench/seals/L142_THREE_SITES_PREREG.md` →
`8226e745503a63b0115e612800c19ec14893e0d7adad4a9f1b3357f387d36d87` — **MATCHES
exactly.** No addendum changed this seal.

## 4. ON MAIN ALREADY?
- Claim 6 (L142 answered, B/B/B): **(c) NOT on main.** `docs/OPEN_LEADS.md:1050-1057`
  (the L142 row itself, with a 2026-08-12 evidence-note dated *before* this memo)
  still reads: *"Not adjudicable by opinion... An output-level agreement is not a
  morphism — **the lead's demand stands**, and the μ-pencil site remains blocked on
  L135's remaining half."* The row has **not** been updated to reflect memo 205's
  closure (B/B/B, "THREE FACTS, THE AGREEMENT IS OF OUTPUTS"), dated a month
  later. `docs/OPEN_LEADS.md:1801-1805` (row L163, referencing L142) similarly still
  treats L142's three-sites question as **re-posing**, not closed.
- Claim 7 (successor answered by memo 204: L = the object's trialitarian invariant):
  **(c) NOT on main** in the same OPEN_LEADS location — no line in the L142 row
  cites memo 204's or memo 205's resolution the way `docs/OPEN_LEADS.md:1917`
  (L173) explicitly cites memo 197 by number (contrast case, see memo 197's r3
  report). Not independently checked whether B882/B1077's arc files mention the
  trialitarian-L identification of memo 204 — out of scope for this memo's grading
  beyond noting the L142 row itself is stale.
- B969 (the occasion arc): **(a) already on main** as a fully executed arc, per the
  memo's own uncontested statement; not re-verified here beyond that acknowledgment.

## 5. NEEDS COMPUTATION HERE
- Claim 2 (Schur/Hom_e6(27,78)=0): DOCUMENTARY in the strict sense (a representation-
  theory fact about e6's irreducible 27 and 78 being inequivalent) — trivially
  re-checkable by dimension/highest-weight lookup, not a numeric search.
- Claim 3 (pencils not conjugate): recompute the two ordered pairs' joint kernels,
  characteristic polynomials, and rank products in the 27-dimensional
  representation and confirm charpolys differ — a sympy/exact-linear-algebra
  re-run, expected: kernel dims (0,3) both, charpolys NOT equal, rank_product
  (27,24).
- Claim 4/5 (six cubics all generate K, bite control does not): factor each of the
  6 listed cubics over K's splitting field (or check root membership over K's
  smallest model `x³−12x−5`) and confirm all 6 succeed and the bite control
  (`x³−6x²−14x+18`) fails. Population: the 6 named cubics + 1 control; expected: 6
  True / 1 False.

## 6. SUPERSESSION
Not withdrawn. The memo's own "successor question" is explicitly answered by the
**later** memo 204 (cited inside memo 205 itself, §6), which is consistent, not
contradictory — memo 205 pre-dates 204's numbering in the narrative but is banked
after it (2026-09-12 vs memo 204's undated-here reference; INDEX.md orders 205
after 204 by number). No INDEX.md row after 205 retracts it. However, **the arc
this memo was meant to close (`docs/OPEN_LEADS.md` L142) itself was never updated**
— see §4 — which is a live register-lag matching memo 207's own diagnosis pattern,
just not caught by memo 207 (which covered L53/L72/L78/L174, not L142).

## 7. GRADE PROPOSAL
**REGISTER** (with a flagged register-lag) — the mathematics (CELL 1/2/3, all B) is
solid, theorem-driven where possible, seal-verified (hash matches exactly), and not
disputed by anything on main; but `docs/OPEN_LEADS.md`'s own L142 row has not been
updated to reflect this closure a month later, so the documentary write-back this
memo earns is itself still outstanding — a one-line fix to L142's row, not a new
computation.
