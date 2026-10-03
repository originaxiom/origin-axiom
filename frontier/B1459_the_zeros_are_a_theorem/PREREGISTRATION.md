# B1459 — PREREGISTRATION: THE ZEROS AT THE COMPLETE POINTS ARE A THEOREM, NOT A CENSUS

**Sealed before the population is run.** cc (main), 2026-10-03. Lead L242.

## 0. Seen first

- **Repo.** `topic_sweep.py "vector-like|period-2|charge conjugation|doubly parabolic|complete point|cusp invariant|t0 = 0"`:
  *VERDICT topic-sweep: 33 of 1330 arcs on main match (NEGATIVE 3, PROVED 30).* Read: B1297 (the class index is
  homeomorphism-invariant, odd under duality, zero on self-dual modules, zero when the cusp has no invariants —
  "t0 = 0 ⇒ 0" — and the fibre's period-2 involution is charge conjugation on the cyclic tower's reducible
  configurations), B1444 (the index is zero off the reducible end "by B1297's identity: the cusp holonomy has no
  invariant vector in a doublet"), B1446 and B1451 (the class index zero at 24 and at 188 doubly parabolic points,
  observed, with 40 of the 188 repaired after the lock found the ranks unresolved), B1455 (L1–L3 and their instance on
  the SL(4) family). The open item is R58-6: "the vanishing of the class index on irreducible modules — a proof or a
  counterexample".
- **Literature.** None needed: the argument is three lines of the record's own and a finite computation.

## 1. The claim to be tested

Let M be a level of a word state, F its fibre, ι the elliptic involution of F (x ↦ x⁻¹, y ↦ y⁻¹), central in Out(F),
so that it extends to an automorphism ι̃ of π₁(M) carrying the meridian to a fibre element times the meridian. For an
SL(2,ℂ) representation ρ of π₁(M) irreducible on F: ι̃*ρ restricted to F has the same character as ρ (tr w⁻¹ = tr w in
SL(2)), hence is conjugate to it, so **ι̃*ρ ≅ ρ ⊗ ε with ε a sign character on the meridian.** A fibre character χ
satisfies χ∘ι = χ⁻¹. B1451's modules are V = ρ_ℓ ⊗ ρ_η ⊗ χ with ρ_ℓ, ρ_η the points of two periodic curves (irreducible
on F by B1444, Theorem A). Therefore

  ι̃*V ≅ ρ_ℓ ⊗ ρ_η ⊗ χ⁻¹ ⊗ ε = V* ⊗ ε,  ε = ε_ℓ ε_η,     and by L1, L2:  I(V) = I(ι̃*V) = I(V* ⊗ ε) = −I(V ⊗ ε).

- If ε = +1: **I(V) = 0.**
- If ε = −1: I(V) = −I(V ⊗ ε), and V ⊗ ε has meridian −T. At a doubly parabolic point T is unipotent, so −T has no
  eigenvalue 1, the cusp fixes no vector of V ⊗ ε, and I(V ⊗ ε) = 0 by B1297's identity; hence **I(V) = 0** again.

So every one of the 188 zeros (and B1446's 24) is a consequence of L1–L3 and the sign data — if the signs behave as
stated. The computation decides the signs and checks the ε = −1 branch numerically rather than by citation.

## 2. The computation (`verification/zeros_are_a_theorem.py`)

For each of the 188 couplings of B1451's run records with both points parabolic (16 levels), at the recorded
coordinates (X, Y, Z) of each point:
- rebuild ρ (`rep`) and its meridian T (`intertwiner`, the record's normalisation);
- form ι*ρ on the fibre (the inverses), its meridian T_ι by the same intertwiner, and the unique Y₀ with
  Y₀ (ι*ρ) Y₀⁻¹ = ρ; read **ε = ±1 from Y₀ T_ι Y₀⁻¹ = ε T** (anything else fails the run);
- ε = ε_ℓ ε_η; recompute I(V) with main's index instrument (expected 0, as recorded); where ε = −1 compute I(V ⊗ ε)
  with meridian −T and record the cusp's invariants.
- Controls: a module on which the argument is silent — the counted non-split W₁ of B1455 at q₀, I = −1 — through
  the same code path with its ι (no symmetry fixes it, and the code must say so); and a random sign flip of ε on one
  point, which must change the predicted identity.

## 3. Predictions

| | prediction | prior |
|---|---|---|
| P1 | at every point ι*ρ ≅ ρ ⊗ ε with ε = ±1 exactly (the intertwiner exists and squares to the identity on T up to sign) | 99% |
| P2 | both signs occur across the 376 factors | 60% |
| P3 | where ε_ℓε_η = −1, I(V ⊗ ε) = 0 and the cusp of V ⊗ ε fixes no vector | 90% |
| P4 | the recomputed I(V) is 0 at every point where the recorded ranks were resolved | 99% |
| **P5** | **every one of the 188 zeros follows from L1–L3 and the computed signs: the theorem holds on the whole population** | 90% |

**What a failure would mean:** a point with ε ≠ ±1 would mean ι̃*ρ is not ρ up to a meridian sign (the fibre
irreducibility or the extension of ι would have failed there); a point with ε = −1 and I(V ⊗ ε) ≠ 0 would be a zero
the criterion does not explain — reported as such, the theorem then holding on the complement.

## 4. Disclosed

Known before the seal: all 188 indices are 0 (B1451), all 24 of B1446 are 0; L1–L3 hold numerically on W₁ (B1455);
B1297's "t0 = 0 ⇒ 0". Not computed before the seal: any ε, any I(V ⊗ ε). The script is written and has not been run on
any level.
