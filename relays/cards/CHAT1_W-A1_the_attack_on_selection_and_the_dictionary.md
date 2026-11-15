# Card W-A1: the attack on selection and the dictionary

**Seat:** the web seat (chat1). **Opened:** 2026-11-15, at the author's request to carry out W-V1's attack. **Kind:**
`result:` (data-free).

**The author's ruling, 2026-11-15, early afternoon (frame C at τ = i).** The seat may evaluate frame C at τ = i and
near it on the act's axis, and print the outputs. It may compare nothing with data or with any value on record. Every
other firewall line stands.

**The goal, in one line.** Derive the dictionary's gauge structure from level 5's Weil representation; sort every open
choice by how it can settle; read frame C at τ = i.

**Part 1, the dictionary (`wa1_weil.py`; pure algebra, no frame).** The Weil representation ρ of SL(2, 𝔽₅) on ℂ⁵ =
functions on 𝔽₅.
- **D1.** ρ(S) and ρ(T) generate a group of order 120, and ρ(−I) = ρ(S)² is the parity f(x) ↦ f(−x), with eigenvalue +1
  three times and −1 twice.
- **D2.** ℂ⁵ = 3 ⊕ 2, both irreducible. The commutant of ρ is 2-dimensional.
- **D3.** Its unique traceless element, scaled to 3 on the 2, is 6Y = diag(−2, −2, −2, 3, 3) = (I − 5P)/2.
- **D4.** The centraliser of P in SU(5) has a Lie algebra of dimension 12 = 8 + 3 + 1. exp(2πi·Y) is diag(ω̄, ω̄, ω̄, −1, −1)
  (ω = e^(2πi/3)), with determinant 1, and lies in the centre of SU(3) × SU(2). So the group is S(U(3) × U(2)) =
  (SU(3) × SU(2) × U(1))/ℤ₆.
- **D5.** On Λ^even(ℂ⁵) the eigenvalues of 6Y and their (colour, weak) content are one generation in SIXY's values: Q 1
  (3, 2); u −4 (3̄, 1); e 6 (1, 1); d 2 (3̄, 1); L −3 (1, 2); and 0 (1, 1).
- **D6.** Over those 16 states, the anomaly sums vanish: ΣY, ΣY³, SU(3)²Y and SU(2)²Y.
- **D7.** Λ¹'s doublet has 6Y = 3 = SIXY's H.
- **Plant:** the same construction with a non-central element of ρ, ρ(T), in place of P does not give SIXY's values.

**Part 2, the choices audit.** A table in the note: every open choice of the record, sorted into settled by equivalence,
settled by consistency, or counted, with its deciding test. No new computation.

**Part 3, frame C at τ = i (`wa1_tau_i.py`).** W-F24's frame (this seat's transcription; canonical end; Theorem 90's
weight; L₂; readings S and S̃).
- **I1.** At τ = i the outputs at the mark and at the twin agree (relative deviation below 1e-6), for every sector ratio,
  in both readings, and for |V| in all four reading pairs. This is a prediction from B1724's S-covariance, from S's map
  of the mark to the twin, and from the trivial end transport at |τ| = 1.
- **I2.** The stabiliser of (i, the mark) acts trivially on the line, so nothing forces a zero there. A prediction: every
  sector ratio at (i, the mark) lies strictly between 1e-8 and 1 − 1e-8.
- **I3.** A prediction from W-F24's height law: every σ₃/σ₁ at (i, the mark) is above 1e-3. There is no large hierarchy
  at τ = i.
- **I4.** Reported: on the act's axis near i (arclength ±0.05, ±0.1), the mark–twin difference, expected to grow from
  zero.
- **Plant:** (i, the mark) against (i, (0, 3/5)) differs by more than 1e-3.
