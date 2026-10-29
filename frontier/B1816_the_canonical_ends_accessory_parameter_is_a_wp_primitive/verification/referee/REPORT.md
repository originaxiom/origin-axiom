# Referee report, B1816 (P-481): accessory parameter as a Weil-Petersson primitive

**VERDICT: PASS WITH CORRECTIONS.** The numerical identity and all constants reproduce. The interpretive layer (label, "picks no point", "PROVED", the monotonicity sentence) needs rewording.

Scripts and outputs are in this folder: chk1.py (own 5-point stencil), chk2.py, chk3.py, chk4.py, chk5.py, chk6.py, chk7.py, with chk*.out, firat.txt and mcm.txt.

## Findings

1. **OK. Identity regenerated at new points with a different method.**
   - Method: chk1.py uses 5-point Richardson stencils, relative steps 2e-3 and 5e-4 (the draft used a 2-point 1e-4). Roots are continued by a straight line in steps of 0.03 from B1667's nearest stored root, with Newton residual below 1e-9.
   - Im dC/dτ̄ divided by the FN route (1/2 of the Jacobian determinant of (ℓ,t) in (x,y)), at step 5e-4:

   | τ | ratio | Re/abs |
   |---|---|---|
   | 0.4+1.5i | 1 − 8e-12 | 2.6e-11 |
   | 0.1+4i | 1 − 3e-12 | 2.7e-11 |
   | -0.2+1.1i (Re τ < 0) | 1 − 1.5e-11 | 2e-12 |
   | 0.35+2.5i | 1 − 5e-11 (step 2e-3) | not extracted |

   - The draft's 4e-9 to 9e-9 offsets are its own 2-point stencil error. The identity is exact to roughly 1e-11.
   - The det is positive, so |det| hides no sign: Im dC/dτ̄ = +(1/2)det(∂(ℓ,t)/∂(x,y)) exactly.
   - Factors: C = 2c and the 1/2 are consistent with the numerics. Convention check: the draft's t formula equals y = 2 coth(ℓ/2) cosh(t/2), the standard cusp FN twist.
   - Also confirmed: (0.4+1.5i)'s c = 0.36522 and (0.15+3i)'s c = 0.65668 match the stored grid.

2. **OK. The branch is the uniformising one at the points used.**
   - uniformisation_check (min Im u over the cell) at my points: 0.096 at 0.4+1.5i, 0.116 at 0.35+2.5i, 0.143 at -0.2+1.1i, 0.126 at 0.15+3i. All are positive, with Markov at 1e-14 and tr P0 = -2.
   - The control root c = -4.122 gives Im u min = -0.58, with traces 9.35, 2.16, 13.29. The gate does discriminate.
   - MINOR: verify_wp.py itself never re-runs the gate at its four points. It relies on continuation, so a gate call should be added to it. Continuation with 0.05 steps from gated roots can only jump if two real-holonomy roots collide, and none was seen.

3. **MINOR / wording. The control weakens what the numerics prove.**
   - The identity holds on any real-holonomy root, so it is a statement about the holonomy map being (anti)symplectic. It is not a test of "WP of τ".
   - What makes the true branch "WP of τ" is that its holonomy Teichmüller point equals τ.
   - Independent evidence of that, which the draft does not have, is item 4 below: the total volume computed from the true-branch density alone equals the Wolpert value.
   - Gate plus volume is sufficient. The draft's handling is correct but the volume check is missing. Adding it is recommended.

4. **OK, and strengthens the claim. The Stokes volume is verified numerically, not just asserted.**
   - chk4.py: Gauss quadrature of h = Im dC/dτ̄ over F ∩ {y<1} (6×4 nodes per half) gives 0.0455244.
   - chk6.py: the x-average of Re c at y = 1 gives 0.0455245.
   - These agree to 2e-7. So ∫_F h = c(∞) with no input from theory.
   - chk5.py: c(y) continued to y = 15, with a free fit c = A − B/(y+e)². A = 0.82242 against π²/12 = 0.822467, and e = 0.851 against δ = 0.8825. A fit with δ fixed gives A = 0.822475 and B = 2.4697 against 3π²/12 = 2.4674.
   - Hence V = π²/12 and the cusp constant (π²/2) are consistent. The volume is the 1/2-normalised ω; this equals π²/6 for dℓ∧dt, which is Wolpert's known value for H/PSL(2,Z).

5. **OK. Tail table and δ.**
   - P = 1 − 12 Re c/π² on the stored grid gives 0.2016 (Y=3), 0.3723 (Y=2), 0.1576 (Y=3.5) and 0.1267 (Y=4), as the draft states. 3/(Y+δ)² gives 0.1990, 0.3611, 0.1562 and 0.1258.
   - The relative error of 3/(Y+δ)² against P falls monotonically: 4.8e-3 (Y=4.5), 5e-4 (10.5), 1.9e-4 (15).
   - π/ℓ − y runs 0.8579 (Y=3), 0.8631 (3.5), 0.8668 (4) towards δ = 0.8825, with the gap shrinking roughly as 1/Y². The convergence is slow, but consistent.
   - Hyperbolic comparison: 3/(πY) is the exact tail for the same total (unit) normalisation, and (π/4)/y² is its density at WP's volume. Both are consistent.
   - Re c is x-independent to 1.6e-4 at Y=2. The draft says "10⁻⁴"; this is fine as rounding.

6. **MINOR. Normalisation provenance.**
   - McMullen (Thm 1.5, mcm.txt) uses ω = dℓ∧dτ and states d(iθ) = ω. Redoing the draft's own pairing chain gives d(iθ) = h dx∧dy with h = Im dC/dτ̄ = (1/2)det, i.e. 1/2 of the McMullen ω.
   - So the "derivation from McMullen" fixes the constant only through a pairing convention. The 1/2 is fixed by the numerics, matched to Wolpert's ½Σdℓ∧dτ as the reader read it in his 2008 survey.
   - The relation to McMullen is therefore up to a convention-dependent factor of 2, and the numerics are the arbiter.
   - Also: McMullen's own text credits Takhtajan-Zograf (1.1) for the Schottky version, d(σF − σS) = −iω. Under that reading, the draft's claim is the ℘-reference analogue.
   - The 1-D holomorphy step is sound: any holomorphic correction to the reference 1-form is closed in one complex dimension.

7. **Literature. Confirmed in part, one phrase not found.**
   - Fırat arXiv:2306.08599 is titled "Hyperbolic string tadpole". His §3.3 is "The Weil-Petersson metric and the volume of M_{1,1}(L)". There he states, near eq. (3.32), that to his knowledge the relation between his on-shell action and the Kähler potential for g_WP hasn't been proven. He says he will not argue it, and fixes the constant A at the cusp.
   - The setting is the one-bordered torus / hyperbolic singularity of length L, so the punctured torus is L=0. The phrase "Monte Carlo volume" was not found in the text, only the §3.3 volume check.
   - McMullen arXiv:math/0010022: the abstract and Theorem 1.5 are stated for general S (M_{g,n}). I could not verify the draft's remark about punctures beyond that. I did not re-read §2 or §7.
   - Wolpert and the other sources were not re-fetched.

8. **CONFIRMED-PROBLEM. "It picks no point" and the "monotone" sentence.**
   - The draft says "h_WP has no interior extremum on the checked range". The raw density h in the τ-plane is not an invariant function, so this is vacuous.
   - The invariant ratio ρ = h·y² (WP density over hyperbolic area density) is a smooth function on the orbifold. By invariance it must have critical points at the elliptic points i and ω.
   - Measured (chk7.out):

   | τ | ρ |
   |---|---|
   | 0.02+i | 0.9611 |
   | 0.1+0.995i | 0.9614 |
   | 0.3+0.954i | 0.9638 |
   | 0.49+0.872i (near ω) | 0.9661 |
   | 0.5+1.2i | 0.9571 |
   | 0.5+2i | 0.8886 |
   | 0.5+3i | 0.7831 |

   - So ρ is lowest at i along the boundary and rises to a maximum at ω, a ~0.5% effect, then falls into the cusp. The density relative to area is not monotone on F, and its maximum is the ω elliptic point.
   - It is not a "selection": a density's maximum is not a measure-selected point, and the ~0.5% variation is tiny. But the sentence as written is wrong.

9. **MINOR / overclaim. "PROVED".**
   - Numerics reproduce to 1e-11 and the volume closes to 2e-7, and the derivation is a convention-dependent reading of McMullen. Neither the check nor the claim is preregistered (the "Seen first" sweep is pending).
   - The identity is of Weil-Petersson / holonomy-symplecticity type for any real branch (item 3). So "PROVED" is fair only for "verified numerically to 1e-11 and consistent with the sources, derived modulo one step not in a source".

10. **CONFIRMED-PROBLEM (label). "ADMITTED by naturality".**
   - The draft's own control shows that Im dC/dτ̄ = pullback of the FN symplectic form for every real-holonomy root. So the instrument does not compute a WP-specific potential; it computes a holonomy-pullback gradient, and WP-of-τ only on the gated branch.
   - Hyperbolic area is also native (conformal structure). The draft concedes this, so "admitted" is true of both, and the label does not discriminate.
   - It is true that the accessory parameter is a primitive of the WP form and not of the area form, and that is a genuine, nontrivial identification. It is just not an admission test.

## Recommended wording

- Replace "PROVED" with "VERIFIED numerically (1e-11, 6 off-axis points; volume closure 2e-7) and consistent with McMullen/Takhtajan-Zograf; derivation modulo a normalisation convention".
- Replace "ADMITTED by naturality (the instrument computes its potential)" with "On the uniformising branch the accessory parameter is a primitive of the WP Kähler form (not of the hyperbolic area form); this is a property of the holonomy of any real-holonomy branch and is certified as WP-of-τ by the uniformisation gate. Both WP and area are frame-native; this does not rank them."
- Replace "It picks no point. WP's density is monotone into the cusp, and h_WP has no interior extremum on the checked range." with "No clock studied here selects a point. The WP-to-area density ratio ρ = h·y² is 0.961 at i, rises to 0.966 at ω (its maximum, a 0.5% variation) and falls to 0 into the cusp; it is not constant, but the variation is far too small to be a selector."
- Add a line to verify_wp.py's report: Im u ≥ 0.096 at each used point (my runs), and the control's Im u min = -0.58.
- Note that the draft's 1e-8 is a stencil error; the identity is exact to ~1e-11.
- State the normalisation: with McMullen/Mirzakhani ω = dℓ∧dτ, ∂C/∂τ̄ = (i/2)·h(dℓ∧dt).
