# CHK-2 (2026-11-24): the lanes the load-bearing sweep left unchecked. The agy lane's M-theory chain is Friedmann and Witten's standard relation plus four identifications, and its "zero-parameter lock" on M_11/M_GUT moved by a factor 2.15 between C22 and C37. agy-002's two-sector floor M3 holds in 240 000 trials and is close to sharp, but only under the one-doublet rule: with one Higgs read alike in both sectors it fails in 27 of 60 000. The physical lane's polynomial algebra of 2026-11-20 reproduces from its stated traces. agy-exp's cover homology is computed here a second time

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It was written at the author's word of
2026-11-24: check what the sweep (THE LOAD-BEARING SWEEP, § 4) said it did not check. Nothing is compared with data.

**Read through the mask:**
- the agy lane at b06c8fc1e: the relays C21, C22, C37 and C38, and C22's producer script;
- agy-002 at 9a2af25af: the interior relay (M58) and producer v3's gate G3 (M3);
- agy-exp at 7ecec4119: its four claim cards of 2026-11-24;
- the physical lane at 32514763f: its relay of 2026-11-20 and the note on the normalizable interior doublet.

**Read on the web:** Friedmann and Witten, hep-th/0211269, sections 3 and 4.

**Claim card:** `relays/claims/CLAIM_2026-11-25_m3_holds_only_for_the_conjugated_higgs.md` (§ 0 item 3, with a sealed,
dependency-free script). The other findings here touch nothing on main's picture and are sent as this check only.

**Disclosed.**
- No check card was written. Each script states its expectations in its docstring and was committed before its run:
  `relays/chat1_2026-11-24_chk2/`, scripts at 3dbd74d07 and 067a25f5e, outputs beside them.
- Three scripts are labelled post hoc, each written after an output was read and committed before its own run:
  - `chk_a2_m3_posthoc.py` (ef8835c7a), M3's sharpness;
  - `chk_a2_m3_scope.py` (17912fca0), M3 with one Higgs in both sectors;
  - `chk_others_posthoc.py`, the cubic's unit root. Its test was first run once outside the tree, then committed and
    rerun.
- One expectation of this seat failed as worded (P3 in § 3).

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement.

## 0. In short

1. **[E] The agy lane's M-theory chain (C21, C22, C37).**
   - The M-theory relations are Friedmann and Witten's (4.4), (4.10) and (4.14), with 2κ² = (2π)⁸ M₁₁⁻⁹. They give
     (M₁₁/M_GUT)³ = (2π)³ α_GUT⁻¹ / L(Q), and 2κ²T_M2³ = (2π)² gives T_M2 = M₁₁³/(2π)². C37 transcribes both
     correctly. C22 had 4π³ where the source has 8π³.
   - What makes the chain predictive are four identifications, none in the source:
     - α_GUT = 1/k with k = 40, the least Chern–Simons level of C21;
     - L(Q) set to the hyperbolic volume of a cover of m004: 40 copies in C22, 8 in C37. In the source L(Q) is
       exp(T_ω − T_O), a ratio of Ray–Singer torsions (4q sin²(5πw/q) for a lens space), not a volume;
     - M_GUT/v_EW = e^{S_A}, with S_A = 8π²Q/g² = 48π/5 at Q = 3/25 and g² = 4π/40 (C21; the arithmetic checks);
     - the transverse volume, which C37 leaves free. Its two benchmarks differ by a factor 72.0 in M_Pl.
   - M₁₁/M_GUT moved from 3.939 (C22) to 8.486 (C37). Nothing was compared with data, so this is not post hoc in the
     record's sense. But the lock is a set of choices, and it has already changed once.
2. **[E] Two physics conditions the cards read here do not meet.**
   - Every finite cover of m004 has a cusp and b₁ ≥ 1. This is computed here for all covers up to degree 8 and for the
     cyclic covers of degrees 8 and 40, and it is a theorem in general (half lives, half dies). The source assumes Q
     compact with b₁(Q) = 0, since harmonic one-forms on Q give extra massless adjoint multiplets.
   - A cusp is not compact. Its cross-sections shrink below 1/M₁₁, so the source's regime R_Q ≫ 1/M₁₁ fails there,
     and its Laplacian has a continuous spectrum, so the torsion threshold needs a filling or another argument.
3. **[E] agy-002's two-sector floor M3 holds as stated, and it does not reach the all-S world.**
   - As stated, H_u = h̄·σ and H_d = h·σ (the one-doublet charge rule). In 240 000 random trials in six modes, and
     in 400 adversarial searches, there was no violation.
   - A post hoc search for its sharpness found a least ρ/F of 1.0025 at a nearly real Higgs, where F tends to B1727's
     floor of 1/3. So the bound is close to sharp there.
   - Post hoc, with one Higgs read alike in both sectors (H_u = H_d = h·σ), the floor fails in 27 of 60 000 trials. One
     has ρ = 0.022 against F = 0.074 at |V₃₃| = 0.9996.
   - [J] In the coupling M3 uses (B1736's Y(h; u, w)), S̃ conjugates h up to a sign. So M3's trade-off comes from the
     conjugation, and the all-S world of B1970 and B1977 escapes it. That fits B1977's aligned and hierarchical points.
     M3 should be scoped to the one-doublet world wherever it is applied.
4. **[E] The physical lane's algebra reproduces from its stated inputs** (the note on the normalizable doublet).
   - P₁ = (z + 1)(z² + 1)(z² + z + 1) and P₂ = z⁴ + s z³ − 4s z² + s z + s² follow from the note's traces and
     determinants by Newton's identities and the Hermitian-form symmetry. P₂'s no-unit-root argument is correct.
   - The cubic ten's polynomial z³ − 2s²z² − 2z + s² has one root of modulus exactly 1, at angle 0.03926 × 2π. It is
     not a root of unity, so the claim of zero interior H¹ on every cyclic cover holds.
   - The inputs themselves (the traces and the cochain's block form) are not rechecked. They need the flat connection.
5. **[E] agy-exp's cover homology, a second computation here.**
   - The Gieseking manifold's orientation cover is m004.
   - π₁(m004) has 20 surjections onto D₅, counted as images of its two generators. The irregular 5-fold cover has 3
     cusps and H₁ = Z³; the regular 10-fold cover has 5 cusps and H₁ = Z⁵. The card's own numbers are masked here, so
     main compares.
6. **[J] Two observations for main.**
   - agy-exp's 24-point shell E_τ[6]_prim is the same set as the 24 choices of B1977's 6-part (P-845). Averaging over
     it is one rule for P-845. The uniform weight is an import.
   - agy-exp's Gieseking card fixes the mirror vacuum by the sign of the baryon asymmetry. That sign is an observation,
     so it is a datum used as an input and should be typed so.

## 1. The agy lane's M-theory chain, piece by piece

| piece | source | type here | checked |
|---|---|---|---|
| \|2I\| = 120, \|2T\| = 24, [2I : 2T] = 5, A₅ on the cosets; McKay graphs Ê₈, Ê₆ | C22 § 1 | mathematics, standard | read; the script's group checks are sound |
| Vol(4₁) = (3√3/2) L(χ₋₃, 2) = 6Λ(π/3) = 2.0298832128 | C22 | mathematics | three routes agree to 4.6e-41, SnapPy among them |
| (M₁₁/M_GUT)³ = (2π)³ α⁻¹ / L(Q) | Friedmann–Witten (4.10), (4.14) | imported physics | symbolic; C37 matches, C22 is half |
| 2κ²T_M2³ = (2π)², 16πG₄ = (2π)²/(T³V) | standard; FW (4.4) | imported physics | symbolic, both |
| α_GUT = 1/40 | C21: least Chern–Simons level from lcm(8, 5) | identification | the lcm is right; that a Chern–Simons level is the 4D coupling is not argued in the relays read |
| L(Q) = n·Vol(m004), n = 40 (C22) or 8 (C37) | C22, C37 | identification | FW's L(Q) is a torsion ratio |
| S_A = 48π/5, read as ln(M_GUT/v_EW) | C21 | arithmetic, then identification | 8π²Q/g² checks at Q = 3/25, 1/8, 1/25; Q = 3/25 itself is not checked |
| V̂_⊥ | C22, C37 | free | C37 says so; its benchmarks differ by (M₁₁/M_GUT)⁴ = 5185 in M_Pl² |
| C22's single-anchor control | C22 script | — | a hard-coded two-item list that always raises; it tests nothing |

- [J] The lane's work on this chain is careful in custody and its errata are dated. The issue is the label. "Zero
  parameter" and "blind prediction" overstate a chain with four identifications and a free modulus.
- [J] The existence of a G₂ metric with an ADE locus along a cusped hyperbolic Q is not shown on the cards read. FW's
  SU(5) sits on an A₄ locus (Z₅); how the E₈ and E₆ McKay data enter the gauge group is not shown either.

## 2. agy-002's two-sector floor M3

- **What is tested.** The statement of producer v3's gate G3 (`run_G3_M3`, `F_three_regime_mp`, `S_req_mp`):
  ρ = max(m₂/m₃ of the up and down sectors) ≥ F(t; s_L, |V₃₃|), with H_u = h̄·σ, H_d = h·σ, and general channels.
- **This seat's code** (`chk_a2_m3.py`, numpy) shares nothing with agy-002's but the statement. Its channels are
  general complex 2 × 2 matrices, not fixed singular values (1, κ) as in the producer.

| cell | expectation (in the docstring) | outcome |
|---|---|---|
| M3-a | no violation in 240 000 random trials | holds; least margin 4.2e-3 |
| M3-b | no violation in 400 adversarial searches | holds. Every search ended at the trivial corner ρ = F = 0 (t = 0, S = 0), so it says nothing about sharpness |
| M3-c | the least margin is below 1e-2 | holds, trivially (2e-15 at that corner) |
| post hoc, sharpness | the least ρ/F with F ≥ 1e-3 lies between 1 and 3 | holds; 1.0025 at t = 0.998, F = 0.332, from 200 searches with none below 1 |
| post hoc, scope | with H_u = H_d = h·σ there is no violation (50 %) | **fails**: 27 of 60 000; least margin −0.052 |

- [J] M3 is a valid bound for the world it states. agy-002's M4 applies it to frame C's points. Whether those points
  read the up sector conjugated, as M3 needs, should be stated on that card.

## 3. The physical lane and agy-exp, as computed

| cell | expectation (in the docstring) | outcome |
|---|---|---|
| P1 | P₁ from trace −2, trace of the square −2, determinant −1 | holds |
| P2 | P₂ from trace −s, 8s + s², determinant s²; no unit root | holds; moduli 0.445, 0.654, 1.53, 2.25 |
| P3 | the cubic has no root of modulus 1 | **failed as worded**: one root has modulus 1. Post hoc: it is not a root of unity (orders ≤ 120 tested; a root of unity solving a cubic over Q(ω) has φ(n) ≤ 6, so n ≤ 18). The lane's claim holds, and the unit root is forced by the symmetry, since the degree is odd |
| G1 | m000's orientation cover is m004 | holds |
| G2 | D₅ covers (read-outs) | 20 surjections; irregular 5-fold: 3 cusps, Z³; regular 10-fold: 5 cusps, Z⁵ |

- agy-exp's other two cards are typed from their own import lines.
  - The lepton–down split imports a second doublet, which sees the shell, and the uniform average.
  - The Liouville card imports a Hořava–Witten racetrack, Split-SUSY running and continuous inputs. B1972's verdict
    stands: the mathematics holds, and no record-level claim follows.
- The S₃ statement of the shared-Higgs card is standard: M₂(Γ(2)) is spanned by θ₃⁴ and θ₄⁴, and SL(2, Z) acts
  through S₃ by its two-dimensional irreducible representation (character 2, 0, −1). So the Hom space has dimension 1.

## 4. What this page does not do

- It compares nothing and reads no target.
- It does not check the agy lane's C23 (cosmology) or its prediction bundles v1 to v7. The bundles were not opened.
- It does not recheck the physical lane's traces, or its other notes of 2026-11-20.
- It does not check M4 of agy-002, which applies M3 to frame C's points.

0 of 19.
