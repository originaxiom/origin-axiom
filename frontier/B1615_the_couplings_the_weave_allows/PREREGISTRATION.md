# B1615 — PREREGISTRATION: THE COUPLINGS THE WEAVE ALLOWS — a parameter count for the masses: how many couplings the weave's group leaves, and what mass spectra its own residual symmetries give

cc (main), 2026-10-08, after S92. A weave arc on the value side (the owner's reopening). Nine of the nineteen are
fermion masses. B1611 put the CP phase and B1612 the mixing angles outside the weave's group; this arc asks the same of
the masses: the weave's group G on the matter triplet T, the couplings it allows, and the mass spectra a vacuum keeping
one of the weave's own residual subgroups produces. **Sealed before `couplings_on_the_weave.py` runs.** The measured
charged-lepton ratios (m_e/m_τ ≈ 2.9 × 10⁻⁴, m_μ/m_τ ≈ 0.059) are known to the reviewer — the imported expectation,
stated. 0 of 19.

## Seen first

`VERDICT topic-sweep /Yukawa|mass matrix|mass hierarch|mass ratio|Schur|couplings|Clebsch|charged lepton/: 57 of 1386 arcs on main match (NEGATIVE 3, OPEN 8, PROVED 46)` — B1611 (G, its automorphisms; T ⊗ T = 1 + 2 + 3 + 3 with a complex singlet, T ⊗ T̄ = 3 + 2 + 3 + 1), B1612
(the residual subgroups RL, RRL of TM1), B1606 (the puncture conditions), the SM seat's §1 ("a flavour group alone gives
no masses: Schur makes an unbroken triplet degenerate"), the value campaign (B1126 V-3: no object period is an SM ratio); the SM seat's W34 (the observer layer on the weave: no private states on all 758 threads for the adjoint, by Menal-Ferrer–Porti; private states at the common point from rank three) and W35 (main's B1612 reproduced with the seat's code), lane `eb4e97801`.
**Literature:** Schur's lemma; Clebsch–Gordan decomposition; the residual-symmetry approach to mass matrices (Lam) —
standard.

## Disclosed

- The predictions are reasoned: the singlet of T ⊗ T has a complex character (B1611), so no G-invariant bilinear of T
  alone exists; Schur makes the singlet-Higgs mass matrix scalar; a cyclic residual group with distinct eigenvalues on T
  leaves three free entries.
- The Clebsch–Gordan matrices are read from the irreducible pieces of T̄ ⊗ T (B1611's decomposition routine); a vacuum
  "keeps" a residual subgroup when it is fixed by its generator in the Higgs's representation.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **C1** | (T ⊗ T̄)^G = 1 (Schur); (T ⊗ T)^G = (Sym² T)^G = (Λ² T)^G = 0 (no Majorana-type mass for T alone); (T ⊗ T ⊗ T)^G ≤ 1 | 80% |
| **C2** | every irreducible of T ⊗ T̄ occurs once: one coupling per Higgs representation | 90% |
| **C3** | a singlet Higgs gives three equal masses | 99% |
| **C4** | no vacuum along a residual subgroup's fixed directions gives a hierarchy: every non-zero ratio m₁/m₃, m₂/m₃ is at least 0.1, and none equals the charged leptons' (2.9 × 10⁻⁴, 0.059) | 85% |
| **C5** | RL has three distinct eigenvalues on T: at the charged leptons' residual symmetry the three masses are three free parameters | 95% |

**The reading, written before the run (the cells can only lower it).** If C1–C5 hold: the weave's group leaves the
masses free — three per sector at the residual symmetry that gives TM1 — and its own couplings with vacua along its own
residual subgroups give degenerate or order-one spectra, never the observed hierarchy. The masses, like the phase and
the angles, are not in the group: they need a forced modulus (the fibre's τ, which the weave's object M₁,₂ leaves free
except at its orbifold points) or dynamics. 0 of 19, with the masses' location named.

## Instruments

`verification/couplings_on_the_weave.py`; hashes in `ARTIFACT_HASHES.txt`.
