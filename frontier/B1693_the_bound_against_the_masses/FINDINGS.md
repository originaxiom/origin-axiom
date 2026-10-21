# B1693 — B1692'S BOUND AGAINST THE MEASURED MASSES (P-241): ONE HIGGS IS EXCLUDED IN THIS FRAME — THE UP QUARKS' 2–3 HIERARCHY IS SIXTEEN TIMES THE LEPTONS', BEYOND THE FOUR A FLAT LINE CAN GIVE — WHILE THE DOWN–LEPTON PAIR (3.1) IS ALLOWED

**Verdict: PROVED as sealed (both cells hold).** cc (main), 2026-10-21. Sealed `aa36d2667` (sha256 ffe0a6e1) before
`verification/compare.py` ran; its one run committed unread at `4eac2b5b1`. A test of a structure, not a value derived.
0 of 19.
- **The bound (B1692, no data).** In the fibre frame (Λ; B1653's residue coupling and charges), with a flat hypercharge
  line and one covariant Higgs (H-cov), the three charged sectors' m₂/m₃ differ by at most a factor of four.
- **The data** (B1637's hash-pinned transcription of Huang and Zhou 2021, running masses at M_Z, the full SM; each ratio
  with its errors and B1637's 10% running allowance in quadrature): m_c/m_t = 0.00368, m_s/m_b = 0.0187,
  m_μ/m_τ = 0.0589.

| cell | statistic | measured | 3σ band | grade (as sealed) |
|---|---|---|---|---|
| **T1, one Higgs** | max/min of the three m₂/m₃ | **15.98** (leptons over up) | 10.37 – 24.62 | **EXCLUDED** (predicted) |
| **T2, the down–lepton pair** | max/min of m_s/m_b, m_μ/m_τ | **3.14** (leptons over down) | 1.91 – 5.18 | **ALLOWED** (predicted) |

- **What it means.** In this frame one Higgs cannot carry the three charged sectors: the up quarks' second-to-third
  hierarchy is about sixteen times the leptons', and no flat line, no τ and no covariant section tested reaches more
  than four. The up quarks need a Higgs of their own — the pattern of a two-Higgs completion — a structural conclusion,
  not a number. The down–lepton pair, sharing one Higgs, is within the bound: a flat line can supply the d–e split's
  size (the d–e wall's question, P-084), though the line and τ that would give it are not selected (the potential
  selects the half-period line, where the sectors coincide: B1686, B1692).
- **What it does not do.** It derives no mass; it does not show that a line gives the measured 3.14 (only that the bound
  allows it); the 10% allowance's adequacy for the running between the fibre's scale and M_Z is not shown.

## Seen first

`VERDICT topic-sweep /Georgi|Jarlskog|d.e wall|down quarks? (from|and) (the )?(charged )?leptons|cross.sector|two Higgs|2HDM|H_u|second.to.third|2.3 hierarch/
(full text): 37 of 1464 arcs on main match` — chiefly **B1660** (the one-Higgs census at ω on W59's lines, NEGATIVE as
sealed; it states the data's (m_μ/m_τ)/(m_s/m_b) = 3.14 from this same file), B1637 (the ruled-branch fits and this
file's transcription), B1656 and B1659 (the twisted frame; the joint law), B1691 and B1692 (the exponents; the bound),
B308 (the old object: the inter-generation hierarchy not forced). **Literature:** Georgi and Jarlskog (1979) for the
down–lepton pattern; Huang and Zhou (2021, arXiv:2009.04851v2) for the running masses.

(As sealed; copied from `PREREGISTRATION.md`.)

## Disclosed (from the seal)

- **The outcome was largely known before the seal**: B1660 states the down–lepton ratio, 3.14, from this file; main
  recalled the running masses at M_Z from memory while exploring B1692. The priors (95%, 90%) were informed by it. The
  seal fixed the criterion and the uncertainty treatment.
- **A grading change before the seal**, from the allowance's arithmetic: a "consistent" grade needing the upper 3σ edge
  below 4 was unreachable for T2; the grades are EXCLUDED or ALLOWED.

## Files

- `PREREGISTRATION.md` (sealed), `ARTIFACT_HASHES.txt`, `verification/compare.py` → `comparison.json`,
  `compare_run.txt`. The lock: `tests/test_b1693_the_bound_against_the_masses.py`.

> *Correction 2026-10-21 (S167; found by main, targeted).* **T1's exclusion holds for B1692's point coupling (the large-L
> limit), not at the canonical end.** B1692's bound of four fails at L of order one (B1692's correction: spreads of 7.7
> to 10.8 at B1695's best point), and B1695's one-Higgs point (the down quarks and leptons through S, the up quarks through
> the conjugate Higgs of the same field) brings all six ratios within a factor of 1.8, with an up–lepton m₂/m₃ spread of
> 7.7 against the measured 16. So "one Higgs is EXCLUDED in this frame" is scoped to the point coupling; at the canonical
> end one Higgs is not excluded by this test. The sealed computation and its grades stand as computed.
