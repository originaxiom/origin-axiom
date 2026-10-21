# B1692 — THE CUSP WITH A TWISTED LINE PER SECTOR (P-169, PART 1): A FLAT HYPERCHARGE LINE KEEPS THE COVARIANT HIGGS'S EXPONENT IN EVERY SECTOR AND SPLITS THE SECTORS' 2–3 HIERARCHIES BY AT MOST A FACTOR OF FOUR

**Verdict: PROVED (a census, computed; no data).** cc (main), 2026-10-21. POINT_REGISTER P-169 (its first part; the
comparison with the measured masses is P-241, to be sealed). 0 of 19.
- **The setting (the record's own).** The fibre's zero modes with a flat line on the fibre, w = α τ + β/2, each field
  seeing it through its hypercharge 6Y (Q 1, u^c −4, d^c 2, L −3, e^c 6, H 3; B1653's conventions and functions,
  reused verbatim); a sector's residue at the puncture is the rank-one bilinear of its two fields (B1653), and its
  coupling is B1653's Y = coupling(S, M) with the Higgs S = a_i i + a_j j + a_k k for a in M. The Higgs's direction is
  B1691's covariant section (the tagged hypothesis H-cov); one Higgs for the three sectors.
- **The two codes agree.** With no line, B1653's residue coupling and B1645's closed form give the same m₂/m₃ for the
  weight-3/2 section ∂R: m₂/m₃ / |q|^½ = 18.0058, 18.00025, 18.00001 at Im τ = 3, 4, 5 (B1691: 18).
- **The exponent is the line's to keep.** With a line, the m₂/m₃ exponent stays ½ in every sector at every line tested
  (α = k/12, the slopes 0.49–0.50 between Im τ = 3, 4, 5, for ∂R and a weight-7/2 section); m₁ = 0 (a point coupling,
  B1653).
- **The line splits the sectors only by a coefficient, and by at most four.** Writing (m₂/m₃)_s = c_s × the value
  without the line:
  - **at Im τ = 14 on 484 lines** (α = j/120, β ∈ {0, ½, 1, 3/2}), every c_s lies in [1, 4] and the largest spread
    max_s c_s / min_s c_s is 3.99999993; the generic values are 1, 2 and 4 (the commonest triples (2, 2, 2), (1, 1, 1),
    (4, 4, 1), (2, 1, 4), (4, 2, 2)), with 4/3 and 8/3 on isolated lines; **β never matters**;
  - **at finite Im τ** (1.5, 2, 3; 61 lines; four sections — ∂R, two at weight 7/2, one at 15/2) the largest spread is
    3.01, 3.60 and 3.92, rising toward 4;
  - **at W60's selected line** (the half-period, α = ½) the three sectors coincide (c = 2, 2, 2): the d–e wall at the
    potential's state.
  - **the up sector's readings** (a check after the census): with the up quarks read through S̃ = ε conj(S) εᵀ, the
    conjugate Higgs, or conj(S) (B1660's three readings of one Higgs), the largest one-Higgs spread over the lines j/24 is
    3.64 to 3.99999999985 at Im τ = 2, 3, 6 for ∂R and a weight-7/2 section: the bound holds for every reading; the
    conjugate reading reaches 4 with no line (`verification/up_readings.py`, `up_readings_run.txt`).
- **Why.** In the coupling, Y = Xᵀ(εS)Ỹ with X = [C_a v_x] and Ỹ = [C_b v_y], so m₂/m₃ depends on the residue
  doublets v_x, v_y only through their directions. A twisted mode's doublet has components whose cusp exponents differ by
  the twist, so its direction tends to one of two basis lines, except where a field's twist c·α is ≡ ¼ mod ½ (a tie),
  which is where 4/3 and 8/3 appear (on the grid j/24: the leptons at α = 1/24, 2/24, 3/24; the down quarks at 3/24; the two quark sectors at 6/24). Finitely many limiting
  directions give finitely many factors.
- **What it means.** In the fibre frame, given Λ and one covariant Higgs, a flat hypercharge line can make the three
  charged sectors' second-to-third hierarchies differ by at most a factor of four — whatever τ, the line, or the
  section. If the up quarks couple to a different Higgs from the down quarks and the leptons (two Higgs fields), the
  bound applies to the down–lepton pair. Whether the measured ratios respect it is P-241, sealed first.
- **What it does not do.** No data; no mixing; m₁ (a point coupling gives none; B1654's lift per sector is not computed
  here); the twisted Higgs (the Higgs's own charge on the line is carried, as in B1653, by the point coupling's gauge
  invariance, not by a twisted section); the sections tested are four, not all.

## 0. Seen first

`VERDICT topic-sweep /near the cusp|near omega|near ω|q-expansion|residual (charge|symmetr)|exponents? (of|fixed by)|hierarch(y|ies) (from|as) (powers|exponents)|Froggatt|modular weight|discrete exponents/
(full text): 28 of 1462 arcs on main match` (B1691's sweep), and for the line: B1653 (the rank of a point coupling, its
twisted residue and every line on the record), B1656 (the electron's zero at W59's lines), B1657 and B1659 (the
symmetric point; the joint law), B1660 (the census at ω), B1686 (W60's half-period line, the matter seeing nothing).
None computes the sectors' split under a covariant Higgs near the cusp. **Literature:** theta functions with
characteristics; Feruglio and collaborators, and Novichkov, Penedo and Petcov, for hierarchies near fixed points.

## 1. Disclosed

- **Value contact before any seal (main's, in this session).** While exploring, main set the first cross-sector factors
  beside the recalled ordering of the measured m₂/m₃ (leptons > down > up), and after the census set the bound against
  running masses at M_Z recalled from memory (m_c/m_t ≈ 0.0037, m_s/m_b ≈ 0.019, m_μ/m_τ ≈ 0.059): the up–lepton
  spread about 16, above four; the down–lepton spread about 3, below four. No computation touched data. P-241 will be
  sealed with its criterion stated before any data are read and will carry this paragraph.
- **The exploration preceded the census** (`verification/before_the_instrument/`), and the census scripts were written
  after it and run as given. B1653's functions are copied verbatim (`verification/b1653_funcs.py`).

## 2. Files

- `verification/b1653_funcs.py`; `verification/line_census.py` → `line_census.json` (Im τ = 14, 484 lines);
  `verification/finite_census.py` → `finite_census.json` (Im τ = 1.5, 2, 3; four sections); the logs.
- The lock: `tests/test_b1692_the_cusp_with_a_twisted_line_per_sector.py`.
