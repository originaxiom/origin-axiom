# B1659 — THE JOINT LAW: in B1656's twisted frame the coupling's determinant and adjugate factor through the Higgs's and the matter's defects, exactly, for every Higgs and every matter

**Verdict: PROVED.** Every cell holds as sealed. cc (main), 2026-10-15.
- Sealed `f4b12d788` (sha256 8123044b) before the run. The output was committed unread at `c98fbe782` (one run,
  about 140 s, exit 0; the instrument unchanged since the seal, sha256 84756480).
- **0 of 19. No data.**
- POINT_REGISTER P-168, after B1658, whose T1 is this law on the null cone. J1, J2, J2b and J2c are identities over
  M₂(ℂ) × M₂(ℂ). J3 is on B1656's sector matter at ω, a frozen piece.

## 0. Seen first

As sealed: `VERDICT topic-sweep /joint law|adjugate|det Y|antisymmetric pairing|two defects|product of (the|their) defects|tr\(eps/: 7 of 1430 arcs on main match (NEGATIVE 2, OPEN 2, PROVED 3)`
— the precedents B1644 and B1658; the rest in other senses. Read: B1656, B1657, B1658, the SM seat's W90, W93, W94 and
its relays §138–§139. **Literature:** the adjugate of a bilinear family of 3 × 3 matrices; the polar form of a
quadratic form; Cayley–Hamilton for the singular values (e₁, e₂, e₃ from ∣∣Y∣∣², ∣∣adj Y∣∣², ∣det Y∣²).

## 0b. Disclosed

In full in the preregistration's §0b and §5. In short:
- main's exploration and the census attempts are kept beside the seal, with no census number claimed;
- two readings were withdrawn before the seal: that the law "unifies" B1657's vacua, and that the two frames "differ"
  (a labelling artefact found by the first reviewing agent, which main verified and told the owner);
- two read-only reviewing passes; the second made the thresholds seed-robust and separated the geometric-mass law from
  the SM seat's Y² identity.

## 1. The sealed run (`verification/the_joint_law.py`, unchanged; `.json`, `_run.txt`)

| cell | prediction | kind | result |
|---|---|---|---|
| **J1**, the determinant law | det Y − 4 det S det M tr(εSMᵀ) ≡ 0 | identity (sympy) | **HOLDS:** residual 0 |
| **J2**, the adjugate law | adj Y − det S·A(M) − det M·P A(S) ≡ 0 | identity (sympy) | **HOLDS:** residual 0 |
| **J2b**, the null cone | A(pqᵀ) = q̃p̃ᵀ, not the transpose; adj Y = det S·A(M) and ∣∣A∣∣ = 2∣∣M∣∣² at 200 draws | identity | **HOLDS:** exact; 1.8 × 10⁻¹⁵, 4.4 × 10⁻¹⁶; the transpose fails |
| **J2c**, the symmetric form | N = Mε: Y(S, Nε⁻¹) = Y(N, Sε⁻¹); tr(εSMᵀ) = −polar(S, N); det N = det M | identity (sympy) | **HOLDS:** all three exact |
| **J3**, the sector matter | W59's 18 lines at ω, three sectors, L ∈ {5, 50, 500}, random S (324 cases): J1, J2 and the spectrum from (e₁, e₂, e₃) | identity, evaluated | **HOLDS:** 4.2 × 10⁻¹⁷ (∣∣Y∣∣³), 2.1 × 10⁻¹⁶ (∣∣Y∣∣²), 1.6 × 10⁻¹⁵; the leptons' det M null to 7.6 × 10⁻¹⁵ (non-trivial only on the quarks) |
| **J4**, corollaries | m₁ = 0 for null M, null S, S = M; geometric masses at N = S; both light masses first order | identities; (d) a test | **HOLDS:** 2.0 × 10⁻¹⁶, 1.9 × 10⁻¹⁶, 5.3 × 10⁻¹⁷; geometric to 4.1 × 10⁻¹⁴; slopes 0.99996 and 1.00009 (10 cases) |
| **J5**, controls | a perturbation breaks J1; A for P A breaks J2; N ≠ S departs from the geometric law; B1657's det form (a check) | tests; (d) a check | **HOLDS:** ≥ 3.6 × 10⁻³; ≥ 2.3 × 10⁻²; median 0.54; 8.8 × 10⁻¹⁶ |

## 2. What it shows

- **The joint law.** In B1656's twisted frame:
  - det Y(S, M) = 4 det S det M tr(εSMᵀ);
  - adj Y(S, M) = det S·A(M) + det M·P A(S), with P = diag(1, −1, −1) and A the explicit quadratic of the
    preregistration's §1.

  Both hold for every Higgs and every matter in M₂(ℂ), not only to first order. B1658's T1 is the restriction to the
  null cone.
- **The masses in closed form.** The squared masses are the roots of x³ − e₁x² + e₂x − e₃, with e₁ = ∣∣Y∣∣²,
  e₂ = ∣∣det S·A(M) + det M·P A(S)∣∣² and e₃ = 16∣det S det M tr(εSMᵀ)∣².
  - **m₁ = 0 if and only if** the Higgs is null, the matter is null, or the pairing vanishes. This covers B1656's
    electron on W59's lines, whose matter is null.
  - In the hierarchical limit the middle mass reads the sum of the two defects' terms, with interference. The lightest
    is their product, times the pairing, over the other two masses.
  - Both light masses are first order in the defects.
- **The symmetric form.** With the matter labelled N = Mε, the coupling is symmetric in Higgs and matter, and
  det Y = −4 det S det N polar(S, N): defect × defect × pairing, the shape of B1657's (a·a)(v·v)(a·v).
  - At the coincident point N = S the masses are exactly geometric, m₁m₃ = m₂², as in B1657's frame at Y(v; v).
  - The SM seat's identity Y(v; v)² = (v·v)²𝟙 holds there. Here Z(S, S)² is not proportional to 𝟙, so the geometric
    law is a separate statement.
  - Whether the two frames are linearly equivalent is not claimed.

## 3. What it does not show

- Any value, or any comparison with data. The census of the inverse map under P4 waits for a search shown reliable in
  the data's own regime (main's attempts disagreed across optimisers).
- Which Higgs or which matter.
- The first generation's size against nature.
- The interacting weave. This is one τ, a frozen piece, and the SM seat's §139 places ω on the arena's singular fibre.

## 4. Credit

- **The first reviewing agent** found the labelling (N = Mε) that makes the coupling symmetric. That turned a claimed
  disagreement between the frames into an agreement.
- **The second reviewing agent** made the thresholds robust.
- **The SM seat:** W93's check of B1658, which this extends, and its geometric-mass identity, whose twisted-frame
  counterpart is J4(e).

## Addendum (2026-10-21, B1684)

> *Scoped 2026-10-21 (P-214, completed at Review 66).* J3 is evaluated on W59's eighteen lines at ω. W59's mathematics is now verified on main (B1684): at τ = ω the eighteen lines are exactly the minima of the Higgs alone. They are not the state the SM seat's later potential selects: its W60 puts the full potential's line at a half-period, and its W62 finds that state not stationary in τ (headline on main, P-222). So it is a read-out at an input state. The cells and numbers are unchanged.
