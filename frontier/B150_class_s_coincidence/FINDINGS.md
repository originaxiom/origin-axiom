# B150 — class-S coincidence (L14): the trace-map action IS the N=2\* S-duality MCG action on the character variety; τ-modularity and physical magnitude are RHYME (V139)

**A scoping / characterization pass — not a verdict-of-match, no sandbox "match" fabricated.** L14 asks how far the unit's
picture reaches: does the SL(2,ℤ) trace-map / mapping-class action on the once-punctured-torus character variety (B148's
object) coincide with the S-duality / mapping-class action on the Coulomb branch of the class-S theory of the once-
punctured torus? This is reading-and-comparison; the deliverable is a **precise characterization + a comparison table,
every point tagged FORCED / PERMITTED / RHYME** against the actual B148 invariant data. MATH tier (physics-adjacent,
**firewalled**); nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B149 untouched.

## The binding distinction (two different spaces)

The class-S SL(2,ℤ) acts on **two** spaces, and they must not be conflated:
- **(i) the UV gauge coupling τ** (the complex-structure modulus of the punctured torus) — the well-known S-duality
  modularity. This is **not** the trace-map dynamics; it is a **HOMONYM → RHYME**.
- **(ii) the Coulomb-branch / Fricke character variety** — where the trace-map action lives. A coincidence is **FORCED**
  only if the action *on the character variety* reproduces the B148 anchors (hyperbolic classes, λ_m², ℚ(√(m²+4)) fixed
  slopes, the κ cubic, the κ=−2 Markov fiber). Every tag is adjudicated against this distinction.

## §1 — What the class-S object actually is (from the primary literature)

- **The space.** Allegretti–Shan (arXiv:2411.17378) give `M_flat(S_{1,1}, SL₂ℂ) = ` the **Fricke cubic**
  `a²+b²+c²+abc = 2+λ+λ⁻¹` with `a,b,c = −tr α, −tr β, −tr αβ`. GMN (arXiv:0907.3987, *Wall-crossing, Hitchin Systems,
  and the WKB Approximation*) identify the class-S Coulomb branch (on `S¹`) with the rank-2 **Hitchin moduli space** of
  the surface — the same character variety by nonabelian Hodge. **Convention match (verified):** B148's
  `κ = x²+y²+z²−xyz−2 = tr[A,B]` equals `λ+λ⁻¹` (the puncture-holonomy trace), so the Fricke cubic and the B148
  κ-level-sets coincide exactly, and `κ=−2 ⟺ λ=−1`.
- **The group.** Allegretti–Shan: the mapping class group `SL₂(ℤ) ≅ Mod(S_{1,1}) = ⟨σ,τ₊ | σ⁴=1,(στ₊)³=σ²⟩`, generated
  by the **Dehn twists** `τ₊,τ₋` — exactly B148's `τ_a,τ_b`. This `SL₂(ℤ)` *is* the **S-duality group of the N=2\*
  theory**.
- **The action, and the crucial point.** The MCG acts on the skein/character algebra by those Dehn twists, and the three
  ℤ₂-invariant subalgebras are quantized **K-theoretic Coulomb branches** of the 4d **N=2\*** theories (`SL₂`/`PGL₂`,
  Langlands-dual), **permuted by the MCG**. Allegretti–Shan state the duality acts "**on the character variety itself
  through mapping class group transformations, not merely on the coupling τ**." So the physics S-duality is realized as
  the MCG / trace-map action on the character variety — the same action as B148.
- **The dynamics.** Cantat–Loray (AIF 59 (2009) 2927; arXiv:0711.1579, with the companion 0711.1727 *Bers and Hénon,
  Painlevé and Schrödinger*): a mapping class acts **both** as a `GL(2,ℤ)` matrix on homology **and** as a polynomial
  automorphism of the cubic (the trace map / Markov surface); its **dynamical degree / topological entropy = log(spectral
  radius of the homology matrix)**, with hyperbolic / pseudo-Anosov elements. For `RᵐLᵐ` the spectral radius is `λ_m²`.

## §2 — Same object, or only analogous?

**Same object** for the character-variety realization: same variety (the Fricke cubic), same group (`SL₂(ℤ) = Mod(S_{1,1})`),
same generators (the two Dehn twists), same action (the trace map). The Coulomb branches are **MCG-permuted subalgebras
inside** that variety (not the whole variety — the precise relationship). **Different object** for the τ-realization: the
coupling space, not the character variety. So the comparison is FORCED on (ii) and RHYME on (i) — exactly the binding
distinction.

## §3 — The tagged comparison (held to the B148 anchor data)

| comparison point | tag | source | why |
|---|---|---|---|
| the **space** (Fricke cubic = κ level sets = Coulomb/Hitchin moduli) | **FORCED** | 2411.17378; 0907.3987 | same cubic, same trace coords; κ = λ+λ⁻¹ exactly |
| the **group** (SL(2,ℤ)=MCG, Dehn-twist generators = N=2\* S-duality) | **FORCED** | 2411.17378 | same MCG, same generators |
| the **action on the character variety** (not τ) | **FORCED** | 2411.17378 | duality realized as MCG/trace-map on the variety, "not merely on τ"; Coulomb branches MCG-permuted |
| **λ_m²** (top eigenvalue = dynamical degree) | **FORCED** | Cantat–Loray AIF 59 (2009); 0711.1579/0711.1727 | λ_m² is the dynamical degree of the metallic mapping class — invariant of the same action |
| **fixed slopes** `t²+mt−1`, field **ℚ(√(m²+4))** | **FORCED** | 0711.1579 | intrinsic data of the same `SL(2,ℤ)` element |
| **κ=−2 = Markov surface** | **FORCED** | 2411.17378; 0711.1727 | same distinguished fiber (λ=−1) of the same family |
| SL(2,ℤ) **modularity on τ** | **RHYME** | Gaiotto 0904.2715 | HOMONYM: same group name, different space (the coupling); no metallic data |
| a physical **scale / gauge magnitude / the SM** | **RHYME** | K006; L15 | duality fixes no scale; gauge group is **free input**; N=2\* non-chiral — the firewall (L15) |

**Honest nuance on the λ_m²/fixed-slope FORCED tags:** the literature does not single out the *metallic* family; its
invariants are reproduced because it is the *same group acting the same way* — FORCED at the framework level, automatic
for the specific elements. (The metallic family is a specific 1-parameter sub-family of hyperbolic mapping classes; B148
is what distinguishes it, not the class-S literature.)

## Verdict — MIXED (report the table, not a single label)

**FORCED at the character-variety / MCG level** — the SL(2,ℤ) trace-map action on the Fricke character variety **is** the
N=2\* S-duality mapping-class action, reproducing the B148 anchor data. This is the widest reach yet of the one-object
picture, and it is literature-confirmed (Cantat–Loray for the dynamics; Allegretti–Shan for the explicit physics
identification "on the character variety, not merely on τ"; GMN for Coulomb = Hitchin moduli). **RHYME at the τ-modularity
level** (the homonym the binding distinction rules out) **and at the physical-magnitude / gauge-content level** (the gauge
group is free input, no scale is fixed, N=2\* is non-chiral). **Even the FORCED part is mathematics** — it identifies the
tower's symmetry with a known duality action; it does **not** cross to physical magnitude. That boundary (does the complex
volume / any quantity carry a scale) is **L15's separate question** and is untouched here.

*(This refines, not contradicts, the earlier scoping pass that tagged class-S "RHYME/PARTIAL": that answered a different
question — "does SL(2,ℤ) act as a Weyl group / select the SM gauge group" (correctly RHYME). At the level L14 actually
asks — the action on the character variety reproducing the metallic data — it is FORCED.)*

## Reproduce

```
python -m pytest tests/test_b150_class_s_coincidence.py -q     # 5 passed (pyenv): anchor data + comparison-table honesty
python frontier/B150_class_s_coincidence/probe.py              # the anchor data + the tagged comparison + the verdict
```

The probe re-asserts the **B148 anchor data** (the comparison's verifiable LHS, imported from B148) and encodes the
tagged comparison; the test locks the anchor math and the *honesty structure* (every row tagged in {FORCED,PERMITTED,
RHYME} with a primary-source citation; no FORCED tag uncited; τ-modularity is RHYME). The test does **not** unit-test the
literature claims themselves — cited prose is the honest boundary of a reading task.

**Tier.** MATH (physics-adjacent, firewalled). Updates `docs/OPEN_LEADS.md` (L14 status → characterized; L15/H2 still
open, separate). No `CLAIMS.md`. Ledger **V139**. **Anchors:** B148 (the unit's invariant data), B149 (completeness),
`knowledge/K006` (the borrowed 3d-3d/cusp dictionary), `speculations/LADDER_LITERATURE.md` (N=2\* rung), `S024` (Hitchin
rhyme). External: Allegretti–Shan arXiv:2411.17378; Cantat–Loray AIF 59 (2009) 2927 / arXiv:0711.1579, 0711.1727;
Gaiotto–Moore–Neitzke arXiv:0907.3987; Gaiotto arXiv:0904.2715; Terashima–Yamazaki arXiv:1103.5748.
