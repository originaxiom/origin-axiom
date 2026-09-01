# R06 — RECOMPUTATION of B1134 (THE SIMULTANEOUS CLOSING) + B1135 (THE GAUGE CLOSING)

**Cell:** reports/fresh_physics_seat_2026-09-01/recompute/R06_simultaneous_closing/
**Date:** 2026-09-01. **Discipline:** BLIND-FIRST honored: own root system, own
Chevalley basis (Frenkel–Kac cocycle, NOT B1102's vendored module), own Weyl BFS,
own GF(2) lift solver, own signature/character machinery — written and RUN, with
all numbers on disk (r06_results.json, r06_run.log), BEFORE opening any arc
verification script, results JSON, or test lock.

## VERDICT: MATCH (B1134 and B1135 both reproduced digit-for-digit; one PARTIAL
subclause and one vacuity note, detailed below)

## Files read BEFORE computing (claim-side only)
- frontier/B1134_simultaneous_closing/FINDINGS.md
- frontier/B1135_gauge_closing/FINDINGS.md
- frontier/B1114_lorentz_double/FINDINGS.md (hatch/I1/I2 definitions)
- frontier/B1125_compact_color/FINDINGS.md (signature conventions, (5,3) anchor)
- frontier/B1127_antilinear_completion/FINDINGS.md (antipodal-class context)

NOT read before computing: verify_simul_closing.py, verify_gauge_closing.py,
b1134/b1135_results.json, any tests/ lock, B1102's e6_bracket_vendored.py.
The cell dir already held e6_lib.py + sweep.py from this cell's earlier
interrupted session (same blind discipline asserted in their headers; they import
nothing from the arcs). This session re-derived and re-verified every
load-bearing formula in them line-by-line before running, and added: an explicit
Killing-structure assertion, an exact float64 fast path for the full bracket
check, and a staged exact Gram computation.

## Files read AFTER my numbers were on disk (diff phase)
- frontier/B1134_simultaneous_closing/b1134_results.json, verify_simul_closing.py (skim)
- frontier/B1135_gauge_closing/b1135_results.json
- tests/test_b1134_simultaneous_closing.py, tests/test_b1135_gauge_closing.py

## Independent construction
- E6 roots by reflection closure from the Bourbaki Cartan matrix (72 roots,
  highest (1,2,2,3,2,1)); Chevalley basis via a bimultiplicative F2 cocycle,
  rescaled to [e_a,e_{-a}] = +h_a; VALIDATED not trusted: full Jacobi via
  ad([x,y])=[ad x, ad y] on all 3003 basis pairs (0 failures), all N=+-1,
  [e,f]=h exact on all 72 roots. NOTE: my bracket sign convention is the
  OPPOSITE of the arcs' ([e,f]=+h vs their -h / <e,f>=-1); characters and
  signatures are basis-independent, and both conventions produced identical
  censuses — the E23 convention risk is resolved, not assumed away.
- Killing form computed directly as tr(ad ad); verified exactly = 24*A on the
  Cartan block, kappa(e_a,e_{-a}) = +24, zero elsewhere. All signatures use
  kappa itself (immune to the E49 fake-form class).
- A2+A2+A2 from the extended diagram: FA={a1,a3}, FB={a5,a6}, FC={a2,-highest};
  Aut(Phi(E6)) verified to induce the FULL S3 on the three factors (2592
  union-preservers), so the census cannot depend on which factor is "color";
  the census was nevertheless run for ALL THREE labelings — identical results.
- Own BFS: |W(E6)| = 51840, -1 not in W; Aut(Phi) = W u (-1)W (103680).
- Signed lifts: own GF(2) RREF solver (72 sign vars; cocycle rows
  x_a+x_b+x_{a+b} = [eps(a,b) != eps(sa,sb)]; c_{-a}=c_a rows; involutivity
  rows x_{sa}=x_a); EVERY enumerated solution re-verified against the raw
  un-eliminated system (guards the arcs' error-#15 ordering-bug class).
- theta^2 = I checked as an exact matrix identity, and the FULL bracket
  automorphism condition ad(theta e_i) = theta ad(e_i) theta (equivalent to all
  3003 pairs) checked exactly on EVERY candidate — stronger than the banked
  40-trial spot-check; the literal pair-by-pair 3003 check additionally run on
  every hit (0 failures everywhere).
- Character chi and per-slot (pos,neg): exact combinatorial formula (Cartan
  eigenspace dims + per-root-orbit terms over the verified kappa structure),
  cross-checked against an independent exact Fraction congruence
  diagonalization of kappa on the +-1 eigenspaces on every hit, 8 random
  non-hits, and all controls — all agree, zero radicals/zeros.

## RESULTS (mine, blind) vs BANKED — B1134
| quantity | mine | banked | |
|---|---|---|---|
| involutive slot-swappers | 48 (24 W / 24 dW) | 48 (24/24) | MATCH |
| (swapper,lift) pairs | 480 (lifts/swapper in {8,16}) | 480 | MATCH |
| color-signature census | (4,4):216 (5,3):240 (0,8):24 | same | MATCH |
| chi on all 24 (0,8) hits | -26, global sig (26,52) | -26 all | MATCH |
| chi<->color bijection | (4,4)<->+6 (5,3)<->+2 (0,8)<->-26 | same | MATCH |
| theta^2=I + full 3003 bracket | 0 failures on ALL 480 | rep 0, spot 40-trial | MATCH (stronger) |
| so(3,1) double on hits | (3,3,0) all 24 | (3,3) all 24 | MATCH (see vacuity note) |
| distinct hit swappers | 6 (4 hits each, all in W) | 6 | MATCH |
| checksum | 3505/3505 chi in {6,2,-14,-26,-78}; all five witnessed | same set | MATCH |
Identical under all three color labelings.

## RESULTS vs BANKED — B1135
128 factor-preserving involutions (64/64), 2000 conjugations; W coset sterile:
1000x ((5,3)^3, chi=+6); flip coset per-slot marginals 900:(4,4)/100:(0,8) on
each slot with EXACT joint factorization (9+1)^3; compact-count -> chi:
0->+2 (729), 1->-14 (243), 2->+2 (27), 3->-78 (1); physics row: 243, all
chi=-14 (neg dim 46 = so(10)+u(1)), other slots (4,4), positions 81/81/81.
ALL digit-for-digit MATCH with b1135_results.json and the lock.

## Controls (the instrument can find the excluded thing)
- Planted compact conjugation (Chevalley involution omega, sigma=tau o omega):
  chi=-78 exact, ALL three slots (0,8), 0 bracket failures — the detector sees
  compact color and -78 when present.
- E49 fake-form control: a sign pattern violating the cocycle gives chi=-10 —
  exactly the historical E49 signature — OUTSIDE the checksum set, with 72
  bracket failures. The classification checksum has teeth.
- Antipodal (sigma=-1) solver control: 64 = 2^6 involutive lifts recovered (not
  collapsed); family chis {-78,-14,+2}, matching the banked antipodal control's
  chi set (their 64-row tally 1/-78, 27/-14, 36/+2).
- Identity lift: chi=+6, exact (42,36,0) — split E6(6) anchor.
- 8 random exact-congruence cross-checks of the combinatorial signature: all agree.

## Notes
- VACUITY NOTE (one clause only, census unaffected): the "gives an so(3,1)
  double, signature (3,3)" property holds AUTOMATICALLY for every
  swapper-family (swap + automorphism) candidate — verified empirically on
  random non-hit candidates, all (3,3,0) — so within the swept swapper family
  that clause could not have failed; it discriminates only against
  non-swappers (omega gives (0,3,3): 3-dim degenerate, no Lorentz double).
- PARTIAL (one subclause): the novelty split "4 of 24 hits inside B1127's
  NEG o pi_mirror torsor / 20 outside" references B1127's torsor construction,
  which this cell did not rebuild; what IS independently reproduced is the
  aggregate structure it rides on (24 hits = 6 distinct swappers x 4 lifts
  each, n_distinct_hit_swappers = 6 = banked) and the banked correction that
  all 6 hit swappers act fixed-point-freely on the color A2 (my count of
  color roots fixed by each hit swapper: 0, all 24 hits).
- Everything exact (integer/Fraction); float64 used only as an exact integer
  carrier in BLAS matmuls (all values << 2^53). Gate 5: nothing measured
  enters — pure root-system combinatorics and exact linear algebra.

## Artifacts
- e6_lib.py (own validated Chevalley e6), sweep.py (own sweep), r06_run.log,
  r06_results.json, r06_results_partial.json — all under this cell dir only.
