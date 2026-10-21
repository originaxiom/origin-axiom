## W60. The quark sector with a Wilson line: the quarks resist the colour-centre line, and the full potential puts the line at a half-period, where the matter sees nothing and one parity copy of the Higgs becomes massless (`the_quark_sector_and_the_line.py`; `W60_RULE.md`; post hoc `the_quark_sector_and_the_line_posthoc.py`)

**Why.**
- The owner ruled "W60: quark sector" (2026-10-13), after W59.
- At ω the colour centre's line is seen only by the quarks, which live in the matter's local system ρ_Q. ρ_Q's spectrum
  with a line had not been computed.

**The order.**
- **The rule first** (`W60_RULE.md`, 560c86dff). It fixed the method: the lattice, N, K, t₀, the grid and the special
  points.
- **The script.** Committed before its one run (bcc1396b9). The pre-run review gave the abelian control the reference
  (½, ½), since the untwisted line has a zero mode and Kronecker's form is undefined there. The matter keeps φ = 0.
- **The run.** One run; its output committed unread (752ce95ff).
- **A labelled post hoc** script followed. Its first launch crashed before writing anything (a scalar conversion) and
  was fixed (cf6cd4d8a). Its one run is the one recorded.

**The method.** The spectrum of ρ_Q ⊗ L_φ on the punctured fibre at τ = ω.
- **The lattice.** A triangular one, with the puncture's −1 as a half flux in the one triangle around it.
- **The potential.** From heat-trace differences: two-dimensional (Δ log det) and six-dimensional (ΔV₆).
- **The units.** Everything is in the same heat-trace units as the exact abelian values.

**The read-out (COMPUTED; P2, P3 and P4 as predicted; P1 failed as worded).**
- **P1, the abelian control (failed as worded).** At four of its five points the lattice matches the exact values:
  - Δ log det against Kronecker to 2.6 × 10⁻¹⁰;
  - ΔV₆ against the lattice sum to 1.4 × 10⁻⁴ relative at N = 192, and 5.5 × 10⁻⁴ at N = 96.
  - The fifth point, (½, 0), and the reference (½, ½) are both 2-torsion points. The order-3 rotation makes them
    equivalent at ω, so both values are exactly 0 and the relative error the rule asked for is 0/0.
- **P2, the symmetries (as predicted).** Period ½, φ → −φ and the order-3 rotation hold on the lattice to 4 × 10⁻¹⁴
  in the spectra and 3 × 10⁻¹¹ in the potentials.
- **P3, the matter's two-dimensional term (as predicted).** The fermion's term is lowest at φ ≡ 0 and highest at
  (⅙, ⅙) ≡ (⅓, ⅓): 0.0256, against 0.0227 at the quarter points.
- **P4, the matter's six-dimensional term (as predicted).**
  - The fermion's term is lowest at φ ≡ 0 and highest at (⅙, ⅙) ≡ (⅓, ⅓): 0.512, against 0.455 at the quarter
    points.
  - No point of the N = 96 grid is lower than φ = 0.
  - So the quarks, as fermions, resist the colour-centre line.
- **The read-outs.**
  - **Convergence.** The lowest eigenvalues change by 0.02% to 0.27% from N = 96 to N = 192.
  - **The hand estimate's shape.** The doubled-winding form correlates with ΔV₆ on the grid at −0.9999995. Odd
    windings have trace 0 in ρ_Q, so the line enters the matter only through doubled windings.
  - **The stated content's net term against w = 0** (quarks, and the Higgs in the three parity sectors jointly):
    - +36.9 at the colour-centre line w₀, where the Higgs is blind;
    - −126.5 and −125.5 at the Higgs's own lines (1/9, 1/9) and (2/9, 2/9).
    - So the Higgs's term outweighs the quarks' at those lines, against the rule's "which the counts make unlikely".

**Post hoc (labelled; written after the read-out; W60's JSON unchanged).**
- **PH1, P1 re-scored with absolute errors.** It holds: the largest |ΔV₆ − exact| is 0.0043 at N = 192, against
  values up to 34.
- **PH2, the matter's ΔV₆ as a cosine series of period ½.**
  - It fits the grid to 2 × 10⁻⁹.
  - Its N = 96 values lie within 0.6% of the N = 192 points.
- **PH3, the net six-dimensional term over every line,** for stated contents (fermions −2 per state, a complex doublet
  +2 per parity sector):
  - **With a Higgs** (in the three parity sectors jointly, or in any one), with or without the leptons, the global
    minimum lies on the 2-torsion lines w with 3w equal to the Higgs's parity. Its value is −147.6 in every case.
    - Jointly there are three such minima, one per parity.
    - They lie below the Higgs's own lines (−126) and the colour-centre line (+36.9).
  - **Without a Higgs** the minimum is at w ≡ 0, with value 0, degenerate with the 2-torsion lines.
  - **At those lines** the matter's potential is exactly 0. A half-period line is equivalent to no line for ρ_Q
    (ρ_Q ⊗ χ_p ≅ ρ_Q), so the quarks and the leptons see nothing. d^c and e^c see the same effective twist: no d–e
    split.
  - **The Higgs gains** because one of its three parity copies sees χ_p ⊗ L_{3w} trivial: that copy becomes untwisted.

**What it shows (a READING on the computed facts and the labelled post hoc; given Λ, GENESIS FK11; the content a
dictionary datum).**
- **The quark sector resists the colour-centre line, as predicted.**
  - In ρ_Q the line acts only through doubled windings, where the holonomy is −1. That is also why the matter's
    potential has period ½.
- **D1's route to a d–e split at a symmetric state closes, as the rule's reading predicted, and for a reason it did
  not state.**
  - The minimum is a half-period line, which the matter cannot feel at all.
  - The rule's sub-claim that the Higgs's term would not dominate was wrong at the Higgs's own lines. It does not move
    the minimum.
- **What the minimum does supply: a massless Higgs that carries a parity.**
  - At the selected line one parity copy of the Higgs has a trivial local system, so it has a normalizable massless
    mode on the fibre: the constant (0, 1)-form.
  - C0 found that no such mode exists without end data (its point 3). Here the line supplies it, with no end
    condition. The Higgs's local system is χ_p ⊗ L_{3w}, and the line's half-period cancels the parity's signs.
  - Which parity is chosen is free among three: forced to choose, not forced which. The choice picks one of the units
    of M, so it splits the three alike into one and two.
- **So C0's fork can be revisited without a new postulate.**
  - At τ = ω, on a half-period hypercharge line, the coupling's Higgs is the untwisted copy's mode.
  - The overlaps C0 described (one number per channel times a tensor on M) become computable. That is the next arc
    to propose, rule first.
  - At ω, W50's couplings were degenerate. Whether these are is to be computed.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

**Status.** COMPUTED (the rule first; one run; P2, P3 and P4 as predicted; P1 failed as worded, a 0/0 at a symmetric
point, re-scored post hoc; the net term's minimum found in a labelled post hoc, after one failed launch fixed). A WEAVE
result on the ruled branch, given Λ, at τ = ω, with the content a dictionary datum. 0 of 19.

