# B1693 — PREREGISTRATION: B1692'S BOUND AGAINST THE MEASURED MASSES (P-241) — can one covariant Higgs with a flat hypercharge line carry the three charged sectors' second-to-third hierarchies, which B1692 says it can split by at most a factor of four?

cc (main), 2026-10-21, after S161. **Sealed before `verification/compare.py` runs and before its data are read in this
arc.** A test of a structure (B1637's value-contact checklist), not a value derived. 0 of 19.

## The question and the cells

B1692 (PROVED, no data): in the fibre frame (Λ; B1653's residue coupling and charges), with a flat hypercharge line and
one covariant Higgs (B1691's H-cov), each sector's m₂/m₃ is c_s × a common function of τ and the section, with
max_s c_s / min_s c_s ≤ 4 over every line, the four sections tested, Im τ ≥ 1.5, and B1660's three readings of the up
sector. So:

| cell | statistic (masses at M_Z) | prediction | prior |
|---|---|---|---|
| **T1, one Higgs** | S₁ = max/min over (m_c/m_t, m_s/m_b, m_μ/m_τ) | **EXCLUDED**: S₁'s lower 3σ edge above 4 | 95% |
| **T2, the down–lepton pair** (two Higgs fields, the down quarks and the leptons sharing one) | S₂ = max/min over (m_s/m_b, m_μ/m_τ) | **ALLOWED**: S₂'s lower 3σ edge not above 4 | 90% |

Grades: EXCLUDED if the lower 3σ edge exceeds 4, ALLOWED otherwise (the central value and both edges reported). σ of
each ratio: the data's two relative errors and B1637's 10% running allowance, in quadrature; S's log-σ from its two
ratios.

**The reading, written before the run.** If T1 is EXCLUDED: in this frame one Higgs cannot carry the three sectors; the
up quarks need a Higgs of their own (two Higgs fields, the pattern of a two-Higgs-doublet completion) — a structural
statement, not a number. If T2 is ALLOWED: the down–lepton split (the d–e wall's question, P-084) is within what a
flat line can supply, though the line and Im τ that would give it are not selected (the potential selects the
half-period line, where the sectors coincide: B1686, B1692). If T2 is EXCLUDED: no line in this frame splits the down
quarks from the leptons as measured, even with two Higgs fields.

## Seen first

`VERDICT topic-sweep /Georgi|Jarlskog|d.e wall|down quarks? (from|and) (the )?(charged )?leptons|cross.sector|two Higgs|2HDM|H_u|second.to.third|2.3 hierarch/
(full text): 37 of 1464 arcs on main match` — chiefly **B1660** (the one-Higgs census at ω on W59's lines, NEGATIVE as
sealed; it states the data's (m_μ/m_τ)/(m_s/m_b) = 3.14 from this same file), B1637 (the ruled-branch fits and this
file's transcription), B1656 and B1659 (the twisted frame; the joint law), B1691 and B1692 (the exponents; the bound),
B308 (the old object: the inter-generation hierarchy not forced). **Literature:** Georgi and Jarlskog (1979) for the
down–lepton pattern; Huang and Zhou (2021, arXiv:2009.04851v2) for the running masses.

## Disclosed

- **The outcome is largely known before the seal.** T2's central value is on the record (B1660: 3.14 < 4); main recalled
  the running masses at M_Z from memory while exploring B1692 (m_c/m_t ≈ 0.0037, m_s/m_b ≈ 0.019, m_μ/m_τ ≈ 0.059;
  S₁ about 16) and set the bound against them (B1692's Disclosed). The priors above are informed by this. The seal fixes
  the criterion, the allowance and the uncertainty treatment, not the outcome's novelty.
- **A design change before the seal.** A first draft graded T2 CONSISTENT only if S₂'s upper 3σ edge fell below 4; the
  two 10% allowances alone make that band at least 0.42 wide in log, so for a central value near 3 the cell could never
  pass. The grades are EXCLUDED or ALLOWED. The change was made from the allowance's arithmetic, not from the data.
- **The data file** is B1637's transcription, on main since B1637 (2026-10-13) and read there; in this arc only its keys were
  printed (no values) before the seal. Its sha-256 is pinned in `compare.py`.
- **The scale.** B1692's bound is a statement at the fibre's scale; the comparison is at M_Z with B1637's 10% allowance
  per ratio for the running of same-type ratios (KIND_TABLE's R2: slow). Whether 10% covers the running between the
  fibre's scale and M_Z is not shown here.

## Instrument

`verification/compare.py` (reads only the pinned file); hashes in `ARTIFACT_HASHES.txt`.
