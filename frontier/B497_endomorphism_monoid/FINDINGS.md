# B497 — The Monoid Campaign, Phase 0: the four strata and the two universal laws (verified, banked)

**The exploration-seat handoff ("the endomorphism monoid of the object", 2026-07-09/10) independently
re-derived by the banking seat — every claim from scratch (`verify_monoid.py`: Cayley–Hamilton for each
trace map, random exact SL(2,ℚ), F_p guards, free-group witnesses, triangular/diagonal proofs for the
universal laws). ALL VERIFY. Campaign registered in PREREGISTRATION.md (phases 0–Z, committed before
compute). Supersedes-and-extends B496 (the TM citizen = stratum 3, already banked; not re-banked).
Firewall: the physics verb-names live in speculations/S063 only. Nothing to CLAIMS.md.**

## The classification (C1) — the four strata of End(F₂) on X(F₂)
**Hopf dichotomy** (CITED: Nielsen–Schreier + F₂ Hopfian via Mal'cev; Lyndon–Schupp §I.4): im(φ) rank 2
⟺ φ injective; rank ≤ 1 ⟺ ker φ ≠ 1. Crossed with det(abelianization):

| stratum | citizen | trace map (verified) | κ-law (verified exact) |
|---|---|---|---|
| **1** inj, det ±1 (Aut) | metallic a→aᵐb, b→a | the program's (T_gold = (z, x, xz−y) at m=1) | **κ′ = κ** |
| **2** inj, \|det\| ≥ 2 | A→A², B→B² (det 4) | (x²−2, y²−2, xyz−x²−y²+2) | **κ′−2 = (κ−2)·x²y²** |
| **2′** (det −2) | period-doubling a→ab, b→aa | (z, x²−2, (x²−1)z−xy) | (stratum-2 family) |
| **3** inj, det 0 | Thue–Morse a→AB, b→BA | (z, z, xyz−x²−y²+2) **= B496** | **κ′−2 = (κ−2)(x²+y²−xyz)** |
| **4** non-inj (rank ≤ 1) | a→ab, b→ab | factors through one variable | **image ⊂ {κ=2}** |

Witnesses (all verified in the free group): stratum 3 injective — (AB)(BA) = AB²A ≠ BA²B = (BA)(AB), so
⟨AB,BA⟩ is free of rank 2 and Hopfian-ness forces injectivity (**I1**); stratum 2 — A²B² ≠ B²A²;
stratum 4 — φ(AB⁻¹) = 1 exactly (kernel witness). The x²−2 component of stratum 2 is the **Chebyshev
map**; via the banked P3 anchor (L+R = Ising transfer matrix), A→A² is literally transfer-matrix
decimation — the RG face is matrix-level, not metaphor. The program to date = **stratum 1 of 4**.

## The two universal laws (C2, C3) — verified
- **U1 (classicality absolutely conserved).** The reducible locus κ=2 is invariant under **every**
  endomorphism of F₂. One-line proof (banked as the *use*; the lemma is KNOWN-FOLKLORE): reducible =
  simultaneously triangularizable, and words in triangular matrices are triangular. Verified on 20 random
  endomorphisms (random words as images). Consequence: **(κ−2) divides (κ′−2) for every substitution** —
  the per-verb multiplier is the table's polynomial (1, x²y², x²+y²−xyz, …).
- **U2 (the classical floor is toral).** On κ=2, parametrized by eigenvalue characters (α,β), every
  endomorphism acts through its **abelianization matrix** on the character torus — verified exactly for
  representatives of all four strata. The classical shadow of the whole monoid is **M₂(ℤ) acting on a
  torus**: cat maps (stratum 1), expanding toral endomorphisms (2), projections (3), constants (4).

**The two-story picture (banked as the structural reading).** X(F₂) = the classical floor (κ=2, abelian,
toral) + the quantum floors (κ≠2, irreducible). The units navigate all floors preserving each; every
singular verb crushes the quantum floors toward the classical one with its exact polynomial multiplier;
the Markov surface κ=−2 is destroyed by TM off every level set (B496 Q1: ejection, κ′=2+4z²).

## The TM citizen upgrades (C4) — beyond B496
- **I2 (one collapse, two levels).** TM's abelianization [[1,1],[1,1]] has rank 1 with image ℤ·(1,1) —
  the **same diagonal** as the character-variety collapse to x=y (B496 T3). Verified.
- **I3 (the dilation).** φ_TM is injective (I1), so the **ascending HNN mapping torus**
  G = ⟨A,B,t | tAt⁻¹=AB, tBt⁻¹=BA⟩ is well-defined — the *same functor* (mapping torus) that builds the
  figure-eight group from the Fibonacci automorphism. The natural extension of the doubling on the
  classical floor is the **dyadic solenoid** (CITED, classical).
- **I-D (the headline, mathematics only):** TM is **injective on F₂ yet singular on every abelian
  shadow** — nothing is destroyed; information is relocated into non-abelian structure invisible to all
  commuting observables. Apparent collapse downstairs (H₁, the character torus), exact reversibility
  upstairs (F₂, the HNN dilation). [The physics naming of this shape is S063, firewalled.]

## The degree ledger (C5) — verified exactly
- **Fibonacci trace map: degrees 2, 3, 5, 8, 13, 21, 34, 55 — the Fibonacci numbers themselves**
  (dynamical degree φ). The object computes its own name.
- TM: 3, 5, 11, 21, 43, 85 (dyn degree 2; = B496 T5). Decimation: dyn degree 2 (Chebyshev).
- Entropy statements remain **CITED-CONDITIONAL** (Gromov / Dinh–Sibony upper bound; noncompactness
  caveat). The ledger banks the integer sequences, not entropies.
- The two constants log φ and log 2 are the two classical renormalization universality classes
  (quasiperiodic/Farey vs period-doubling; Minkowski-? as the coordinate change) — CITED as literature
  anchor, not claimed.

## Tiering
| item | status |
|---|---|
| C1 strata + citizens' trace maps + κ-multipliers | **EXACT, BANKED** (re-derived + F_p) |
| Hopf dichotomy | CITED (Lyndon–Schupp; Mal'cev) + banked witnesses |
| U1 | KNOWN-FOLKLORE lemma; the *use* (per-verb multiplier table) banked |
| U2 | **EXACT, BANKED** (all strata) |
| I1/I2 | **EXACT, BANKED** (free-group witnesses) |
| I3 HNN/solenoid | well-definedness banked (needs only I1); solenoid CITED |
| C5 ledger | **EXACT** (integer sequences); entropy CITED-CONDITIONAL |
| novelty (four-strata frame; κ-factorizations; doubling curve) | **PENDING Phase 1 gates** (research window ~Jul 14): Axel–Peyrière/Bellissard; polynomial-semigroup/Fricke; Sapir/Mutanguha |
| the verb names (evolution/renormalization/decoherence/erasure) | FIREWALLED → speculations/S063 |

## Reproduce
```
python3 verify_monoid.py                      # all Phase-0 claims
pytest ../../tests/test_b497_monoid.py        # locks
```

## The campaign queue (per PREREGISTRATION)
Phase 1 novelty gates (BLOCKED until the research window). Phase 2 the geometry of the singular verbs
(Q2 Mutanguha hyperbolicity of the TM mapping torus — cite-and-apply; is it a 3-manifold group, expected
NO → the "geometry-less sibling" theorem; Q3 the decimation mapping torus). Phase 3 THE INTERACTION
PROGRAM (the six-lens superplan: joint κ=2 toral dynamics gold×TM; product substitution; joint subshift;
combined diffraction; combined Schrödinger + metallic m-scan; defect dictionary) with the mandatory
foreign-control lattice (Fib×Fib, Fib×period-doubling, Fib×random, silver×TM) and the adversarial
laundering-null. Phase Z the delta scoreboard verdict; any H1 via B398, owner present.

---

## Phases 2–3 + the delta verdict (computed 2026-07-10; reproducer `phase23_run.py`)

### Phase 2 — the geometry of the singular verbs: a DICHOTOMY
- **Q3 (exact):** the decimation mapping torus G_dec = ⟨A,B,t | tAt⁻¹=A², tBt⁻¹=B²⟩ contains
  **BS(1,2) = ⟨A,t⟩ exactly** (the edge subgroup embeds — Britton's lemma for ascending HNN; the
  relation is the witness). Hyperbolic groups contain no Baumslag–Solitar subgroups ⇒ **G_dec is NOT
  word-hyperbolic** and not a hyperbolic-3-manifold group. Exact.
- **Q2 (bounded + cite-and-apply):** the atoroidality search for φ_TM (all 117 cyclic classes of length
  ≤ 6, k ≤ 6, powers ≤ 4) finds **no periodic conjugacy class** — bounded evidence that φ_TM is
  atoroidal; by **Mutanguha's theorem** (mapping tori of injective endomorphisms: word-hyperbolic ⟺
  atoroidal — CITED, applied not proved) the TM mapping torus is then word-hyperbolic. Stated as
  bounded evidence + citation, NOT a proof.
- **The 3-manifold question:** G_TM has cohomological dimension 2 (mapping torus of a free group) ⇒
  **not a closed 3-manifold group** (PD(3) needs cd 3) — exact. The with-boundary case: fibered
  3-manifold monodromies are automorphisms and φ_TM is strictly non-surjective (image has infinite
  index — abelianization rank 1); expected NO overall, flagged NEEDS-SPECIALIST for the full statement.
- **The dichotomy (the phase's yield):** the two singular verbs have OPPOSITE geometry — decimation is
  BS-flavored (flexible, non-hyperbolic), TM is (evidence) hyperbolic but with no 3-manifold body: the
  **geometry-less sibling** of the figure-eight, built by the same mapping-torus functor.

### Phase 3 — the interaction program (all six lenses, controls, null)
- **L1 (the joint toral floor — EXACT, the phase's gem):** by U2 the joint gold×TM system on the
  classical floor is F=[[1,1],[1,0]] (invertible) and M=[[1,1],[1,1]]=eeᵀ (rank 1: collapse onto the
  diagonal circle, then doubling). The **sandwich law** M·X·M = (eᵀXe)·M holds for every X, and:
  **M Fᵏ M = F_{k+3}·M** — the TM-sandwich of the golden unit reads out **the Fibonacci numbers** as
  circle-multiplication degrees. The metallic m-scan: the sandwich sequence obeys the sandwiched unit's
  own metallic recursion (s′ = m·s + s_prev; verified m=1..5) — m-dependent, non-rescaling. And
  **M² = 2M**: (M/2) idempotent, the "dim²=2" fusion shape (the Q4 structural first pass; the
  duality-defect reading FIREWALLED → S063). **Laundering assessment:** the mechanism is elementary
  (rank-1 mass readout) and the output is the *unit's own growth data* — so no NEW ingredient; the
  honest content is the exact *measurement algebra*: the singular verb measures the unit and returns
  the unit's growth law. Banked as exact mathematics.
- **L2–L4 (the product constructions — adjudicated exactly):** Kronecker incidence Fib⊗TM has
  eigenvalues {1+√5, 1−√5, 0, 0} — non-Pisot (|1−√5|>1) ⇒ pure-point excluded. The direct product
  X_Fib×X_TM has U = U_Fib⊗U_TM, so its spectral type is the product of the factors': Bragg peaks on
  ℤ[φ]+ℤ[1/2] plus TM's singular-continuous part — a genuinely MIXED spectrum, but **entirely
  determined by the factors** (a tensor product admits no interaction term). **The laundering-null
  fires BY STRUCTURE.**
- **L5 (the coupled Schrödinger operator — the non-product cell; bounded numerics, two sizes 2048/4096,
  stable):** the coupled Fib+TM chain has ≈3× more spectral gaps (56–61) than either factor (20–23) —
  BUT the foreign-control lattice shows comparable enhancement (silver+TM: 50–57; Fib+PD: 39–42), and
  the coupled system's gap labels sit in the **combined module ℤ(φ−1)+ℤ(1/2) mod 1** (top-5 IDS values
  within ≤0.017 of module points at N=4096) — exactly the gap-labeling (laundered) prediction.
  **LAUNDERED at this resolution.** (Fib+random control behaves as disorder: gaps wash out.)
- **L6/Q4:** the structural first pass banked (M²=2M above); the full lattice defect-dictionary
  computation (TCI W on the B221 chain) is the remaining HEAVY cell — queued, not run.

### Phase Z — the delta scoreboard (the honest verdict)
| ingredient | outcome |
|---|---|
| **scale** | the coupled spectrum carries the two module generators (φ−1 and 1/2), but additively — the combined gap-labeling module, i.e. LAUNDERED (each factor contributes its own module; no interaction scale) |
| **multiplicity** | none found in any lens |
| **dynamics** | the det-0 arrow is real (B496 ejection; the Phase-2 dichotomy) but produces no un-laundered spectral novelty at this resolution |
| **un-laundered structure** | NONE survives the control lattice + the structural null |

**Verdict (per the prereg's committed expectation):** at this resolution the interaction program
supplies **no un-laundered delta ingredient** — the mixed spectrum is generic combined-aperiodic-order,
the coupled enhancement is control-matched, the module structure is the laundered prediction. The
campaign's genuine mathematical yield stands elsewhere: **Phase 0's classification** (four strata, two
universal laws), **Phase 2's dichotomy** (the two singular verbs have opposite geometry — BS-flexible
vs hyperbolic-geometry-less), and **L1's exact measurement algebra** (the singular verb reads out the
unit's own growth law; M Fᵏ M = F_{k+3} M). No H1; nothing to escalate; firewall intact.

### Remaining open (the campaign queue)
Phase 1 novelty gates (research window ~Jul 14). Q4 full defect dictionary (heavy; queued). Q2's full
proof (unbounded atoroidality / Mutanguha hypothesis verification) — NEEDS-SPECIALIST or a longer
certified search. The 3-manifold with-boundary statement — NEEDS-SPECIALIST.
