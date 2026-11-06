# B1842 — THE CLOSURE INSTRUMENTS (drafts for review; unrun; P-688)

cc (main), 2026-11-05, at the owner's word ("hire other seats to help u prepare 100%"). **Drafts, data-free, not yet run.**
Committed here so the web seat and the SM seat can review them before any confirmation card is sealed. Nothing here is a
result; nothing here computes or reads a held-out value.

- `verification/exact_card_instrument.py`: the frozen-row instrument at the exact end. It is B1835's card instrument (B1726's
  `compute()` Yukawa construction, returning the matrices, with the Dirac neutrino L ν^c, 6Y = (−3, 0)) with the end
  replaced by B1839's: the exact norm of each channel's twisted kernel over B1667's cell minus the horoball at
  L_max(τ) + δ. δ = ∞ is the cusp limit. τ is reduced by T⁻¹. It returns the matrices and extracts nothing.
- `verification/controls_exact.py`: data-free controls.
  - C-ID: the ratios equal the web seat's `ratios()`.
  - C-M / C-PS: the planted relations at the exact end, at δ = 0.3 and ∞. M_ν ∝ M_e where the order divides 6; M_ν ∝ M_u
    and M_e ∝ M_d where it divides 4; ∣U_PMNS∣ = ∣V_CKM†∣ on order-4 lines. Order-5 lines must break them.
  - C-T: the T-law. *Corrected at Review 76 (R76-3, 2026-11-06):* the first C-T compared two calls that `yukawas_exact`
    reduces to identical inputs, so it could not fail. `verification/t_law.py` runs the theta machinery at the
    unreduced τ + 1 (geometry and norms are the torus's own, so δ = ∞): the singular values agree to 6.6e-16, but
    ∣Y∣ entrywise differs by 7.9e-2. The matrices are related by a non-diagonal unitary, not by phases
    (`t_law_run.txt`).
  - C-MIR: the mirror, in moduli.
- `verification/r_extraction.py`: r = Δm²₂₁/Δm²₃₁ from the ν Yukawa's singular values (ascending, the frame's own order),
  with a planted Haar control C-X, and a salted commitment that writes the value unread and prints only its hash.

**Owed before any card uses them** (P-688):
- the controls run — *done 2026-11-06 (S306h, R76-3): every control holds, with C-T corrected*
  (`verification/controls_exact_run.txt`);
- the SM seat's class-constancy control for ν (its §349 S2.1: M_ν(w′) = e^{iφ} M_ν(w) for w′ in w's Higgs-twist class);
- the y_b/y_t extraction under the SM seat's N1–N6 (σ_max(Y_down)/σ_max(Y_up) at the frozen row, one-Higgs triple only, H = I,
  no Kähler weight);
- the σ_δ profile rule;
- the joint p_V of the pair under the matched null (the SM seat's C4b);
- the location-free information budgets (P-611).
