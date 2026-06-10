# B148 — κ/Fricke–Vogt pinned; the metallic monodromy = SL(2,ℤ) MCG action; the class-S open question

**Firewall (§0).** κ = tr[A,B] is scale-free (a pure number / ℂ/π²ℤ); it cannot source a dimensionful energy density
without an externally supplied scale. Everything here is **mathematics about the tower's symmetry**, not a bridge to
physics. Physics aspiration is POSTULATED and quarantined; nothing to `CLAIMS.md`.

**What is banked (independently re-derived, symbolic — verify-don't-trust on a handoff):**
- **§1** `tr(ABA⁻¹B⁻¹) = x²+y²+z²−xyz−2 =: κ`; and `κ = 4·I_FV + 2` exactly under the half-trace convention (`x=2X`).
  Both trace maps preserve their own invariant.
- **§2** `tr(RᵐLᵐ) = m²+2`; the Dehn twists `τ_a,τ_b` preserve κ ⟹ the metallic monodromies **are** the SL(2,ℤ)
  mapping-class action; the κ=−2 slice is the **Markov surface**; the Markov root `(3,3,3)` and the Q₈ point `(0,0,0)`
  are two distinct orbits on that surface (not a single point).
- **§3** `RᵐLᵐ` hyperbolic; top eigenvalue = **(metallic mean)²**; fixed slopes = roots of `t²+mt−1=0`; trace field
  **ℚ(√(m²+4))** reduced (m=1 and m=4 both ℚ(√5)).

**What is open (reading/proof, not sandbox):**
- **§4.A** the class-S coincidence question — does the SL(2,ℤ) trace-map action coincide with the known duality/MCG
  action on the class-S theory of the once-punctured torus? (The one mathematically-tractable direction; still math,
  not a firewall crossing.)
- **§4.B** the firewall confirmation — verify in GTZ / Dimofte / Córdova–Jafferis that the complex volume enters the
  3d–3d partition function only as a dimensionless exponent. (The decisive physics-boundary check.)

**Run.** `python -m pytest tests/test_b148_kappa_fricke_metallic.py -q` (5 passed) — pure sympy, pyenv.

Ledger **V137**. See `FINDINGS.md`; anchors `../../knowledge/K017_chirality_is_contingent.md`,
`../../docs/STRATEGIC_SYNTHESIS.md`, `../../docs/OPEN_LEADS.md`.
