# B1698 — THE ORDER-5 LINES (P-248): NEGATIVE AS SEALED, NARROWLY — ON THE TICK'S α = 2/5 LINE THE END-DATA HIGGS BRINGS ALL SIX CHARGED-FERMION RATIOS WITHIN A FACTOR OF 2.33 WITH ONE CONTINUOUS NUMBER, BUT 1.7% OF RANDOM HIERARCHIES FIT AS WELL (THE SEALED BAR WAS 1%), AND ON THESE LINES THE DOWN QUARKS AND THE LEPTONS COINCIDE

**Verdict: NEGATIVE as sealed (H1 holds; H2, the decisive cell, fails at 1.675% against 1%; H3 fails).** cc (main),
2026-10-21. Sealed `9c2a50039` (sha256 6cb3ac13) before either instrument ran; the one run committed unread at
`9e5e535bc`. A test of a structure, not a value derived. 0 of 19.
- **The lines (no data).** On w = α τ + b the moves act as L: (α, b) ↦ (α, b − α), R: (α, b) ↦ (α − b, b); the tick's
  sign-fixed lines (det(LR + I) = 5) are S₁ = {(1/5, 2/5), (2/5, 4/5), (3/5, 1/5), (4/5, 3/5)} (L·R) and its swap S₂
  (R·L). With the end-data Higgs ∂R, B1667's canonical end, B1656's coupling, Re τ ∈ {0, ½} and Im τ = 1.5–3.5: one
  continuous number, 96 discrete choices.
- **Against the data** (Huang–Zhou 2021 at M_Z):
  - **H1 (all six within a factor 3): HOLDS** — best on S₁'s (2/5, 4/5) and its conjugate (3/5, 1/5), Re τ = ½,
    Im τ = 3.1, L_max, the up quarks through the conjugate Higgs: worst factor 2.33 (up 0.83, 0.66; down 1.35, 0.68;
    leptons 0.43, 2.29 for m₂/m₃, m₁/m₃).
  - **H2 (at most 1% of random hierarchies fit as well): FAILS** — 1.675% of 4 000 (median 18.8; the 1% quantile 2.08,
    the 5% quantile 3.00): the data sit near the 1.7% level.
  - **H3 (χ² < 16.75): FAILS** — minimum 162.
  - Per line: the α = 2/5 lines are the best of both sets (S₁ 2.33, S₂ 2.68); the α = 1/5 lines miss by 7.9–8.8.
- **The structural miss.** On these lines the down quarks and the leptons come out identical — on all 1 616 rows, to
  10⁻¹² (m₂/m₃ = 0.0253 and m₁/m₃ = 6.39 × 10⁻⁴ for both at the best point) — while the data differ by a factor of 3.1 in
  m₂/m₃ and 3.4 in m₁/m₃ in opposite directions (the Georgi–Jarlskog pattern; P-084, P-094): the order-5 lines cannot
  split d from e, and the best point sits between them. That is why the fit is good in size but not specific. Why, and
  which lines can split them: below (after the seal).
- **What it means.** The tick's own order-5 lines do better than any free scan of the record (one continuous number,
  data at the 1.7% level of random hierarchies, against B1695's 6% with two) — but not at the bar sealed, and with a
  structural reason not to: the line the tick fixes makes the down quarks and the leptons degenerate. In this frame the
  tick's lines do not select the line. The near miss is recorded as such, not as a finding.
- **What it does not do.** The Higgs here carries end data on v₊ (B1697's scope); the unit-free Higgs, β's role
  elsewhere and other lines are not tested; a grid in Im τ.


> *Scope note 2026-10-22 (B1700, P-245).* ∂R's end data are FK10's tagged unit (W46's), not a second datum: given the unit, the weight-3/2 Higgs directions form a three-dimensional space (W46's three), ∂R is its only member holomorphic off v₊ — the coupling triplet R's own end condition — and the only one giving a hierarchy. So this arc holds given Λ, the unit and H-cov in R's own module.

## After the seal (labelled; not part of the sealed test)

- **Why d and e coincide: the order-5 lines are SU(5)-blind.** The line enters a sector through the twists 6Y·w of its two
  sides (B1656). 6Y mod 5 is constant on SU(5)'s multiplets — Q, u, e ≡ 1 (the 10), d, L ≡ 2 (the 5̄), H ≡ 3 — so on a
  line with 5w in the lattice the lepton pair's twists (L, e) are the down pair's (Q, d) swapped: the lepton coupling is
  the down coupling transposed, minimal SU(5)'s Y_e = Y_dᵀ, with the same singular values. By the same count 6Y mod 4 is
  constant on Pati–Salam's SU(4) multiplets (Q, L ≡ 1; d, e ≡ 2), so on a line with 4w in the lattice Y_e = Y_d.
- **The criterion, computed** (`verification/after_the_seal/the_d_e_criterion.py`; the prediction printed before its
  loop): on the lines (1/N, 0), (0, 1/N), (1/N, 1/N) for N = 2–12, at τ = ½ + 2.5 i and 2 i, the down quarks and the
  leptons coincide exactly when the line's order divides 4 or 5 (18 rows, agreeing to 10⁻¹⁴) and differ otherwise (48
  rows, by at least 2.5% in m₂/m₃). On the order-4 lines the first generation of both is massless (m₁/m₃ ≈ 10⁻¹⁵).
  Disclosed: the comparison was rewritten twice after seeing output (first both ratios relatively, which flagged the
  order-4 lines' two numerical zeros); the computation and the prediction unchanged.
- **What it means.** The tick's own lines carry exactly minimal SU(5)'s down–lepton relation — the relation the measured
  masses break by the Georgi–Jarlskog factor of about 3 — so on them no τ, end or reading can meet the data's d–e split.
  A flat hypercharge line splits d from e only if its order divides neither 4 nor 5: W88's orders 9, 11 and 12 (B1697
  item 6, P-250) qualify; the tick's do not. A structural statement about the tick's lines, not a value.
- **Seen (after the seal).** `VERDICT topic-sweep /Y_e ?= ?Y_d|Pati.Salam|quintality|6Y mod|hypercharge mod|bottom.tau|b.τ
  unif|m_b ?= ?m_τ|Y_e ?= ?Y_dᵀ|Y_d\^T/ (full text): 19 of 1470 arcs on main match` — the relations themselves are on
  record (B952 and `docs/GUT_REQUIREMENTS_LEDGER.md` row 7: minimal SU(5)'s m_s = m_μ and m_d = m_e fail by about 3 and 9;
  B1208: a seat's Y_e = Y_dᵀ signature; B925: not Pati–Salam by algebra); none ties a flat line's order to them.

## Seen first

`VERDICT topic-sweep /order.?5|five.torsion|5.torsion|fixed up to sign|det\(LR ?\+ ?I\)|charge conjugation|closing lines|closes around/ (full text): 37 of 1469 arcs on main match (NEGATIVE 4, PROVED 33)` — and B1697's scan (its item 3: B591, B489, B1438, B1444, the SM seat's rows 1209–1213); none tests the
order-5 lines against masses. **Literature:** none beyond the cited arcs.

(As sealed; copied from `PREREGISTRATION.md`.)

## Disclosed (from the seal)

- The fits' α beside 2/5 with b = 0 was known before the seal; no model value on an order-5 line had been computed.
- Both composition orders were included; the Higgs's end data are B1697's stated assumption.

## Files

- `PREREGISTRATION.md` (sealed), `ARTIFACT_HASHES.txt`; `verification/the_order5_lines.py` → `the_order5_lines.json`,
  `the_order5_lines_run.txt`; `verification/compare.py` → `comparison.json`, `compare_run.txt`; `verification/b1656_funcs.py`.
- After the seal: `verification/after_the_seal/the_d_e_criterion.py` → `the_d_e_criterion.json`, `the_d_e_criterion_run.txt`.
- The lock: `tests/test_b1698_the_order5_lines.py`.
