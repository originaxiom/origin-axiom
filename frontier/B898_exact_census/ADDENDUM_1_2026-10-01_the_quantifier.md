# B898 — ADDENDUM 1 (2026-10-01): the dichotomy is a statement about the axes and the two pure planes, not about the torus

**What this arc computed stands.** The four axes are exactly as reported: ad(x₈) ≡ ad(x₁₆): {0³⁰, 48 real};
ad(x₁₄) ≡ ad(x₂₂): {0¹², 66 imaginary}.

**What its prose claimed beyond the computation does not.** The FINDINGS say the torus C splits "with no mixed or
generic-complex directions", and the verdict line says "NO generic-complex eigenvalue exists anywhere on C". The script
classified ad(xₙ) for the four axes only. On any direction with both a split and a compact component the spectrum is
{0¹², 18 imaginary, 48 generic complex}, exactly (B1433: characteristic polynomial t¹²·f₆³·f₁₂·f₁₂′³, Sturm counts).
The pure sums x₈ + x₁₆ and x₁₄ + x₂₂ keep their type.

**Corrected statement.** *The four charges are type-twins in pairs, split and compact; the split plane and the compact
plane keep their types; a direction mixing the two has 48 generic-complex eigenvalues.*

**How it was found.** An outside audit of the structure paper gave the counter-example x₈ + x₁₄ in August 2026. It
reached main in a seat checkpoint read on 2026-09-30 and was recomputed on this arc's own frame, not cited.

**The lock.** `test_no_generic_complex_anywhere_on_C` asserted the four axes under a name that said "anywhere". It is
renamed `test_no_generic_complex_on_the_four_axes`. The mixed directions are locked by `tests/test_b1433_signature_scope.py`.

Corrected in the same landing: THEOREM_LEDGER C29, THEOREM_REGISTRY T-SIGDICH, the LAW_MAP row, the structure-paper
skeleton. See `frontier/B1433_the_signature_dichotomy_holds_on_the_axes/`.
