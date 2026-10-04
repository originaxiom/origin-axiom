# B1538 — PREREGISTRATION: THE PUNCTURE CHARACTERS — the line's supply at the characters of the fibre-direction covers that are non-trivial on a puncture (every cover M_{D,w} with 2 ≤ |D| ≤ 12 of the golden pair m004, m003 and the silver pair m136, m135), and the four's supplies wherever the line could carry two

**Sealed before `run.py` read any outcome.** At the seal this arc has computed only:
- **The population, as structure.**
  - The 80 fibre-direction covers with 2 ≤ |D| ≤ 12: 5 of m004, 9 of m003, 29 of m136 and 37 of m135.
  - Their cusps (the orbits of the monodromy on the punctures) and their invariant character groups. On every cover the free
    rank is #cusps − 1, and the puncture-trivial subgroup has order |det(M − 1)|: 1, 5, 4 and 8.
  - The puncture characters' Galois orbits under §5's order rule: 2,406,622 puncture characters in 662,988 Galois orbits.
  - A puncture value (ζ on a puncture loop) is structure; no twisted cohomology at a puncture character has been read.
- **The controls** (§6), on banked data, the literature, or quantities a lemma proved at design time fixes. There are no
  punctures at |D| = 1 (K1, K6); K2 and K5 read puncture-trivial characters, K3 the trivial character, K4 untwisted homology
  of covers of degree ≤ 6, K7 a free group of rank 3, K9 synthetic rows, K10 Proposition H's characters, located by
  structure alone, K11 the population manifest, by formula, and K12 Part F's fourth roots, by brute force.
- **Eight pre-seal slips** (§6), each logged in ERROR_LEDGER or disclosed there. The eighth was found by the audit lane's R87
  and R89, reviewing this arc's pre-seal snapshots.

**Source.**
- **The owner, 2026-10-03:** "are u sure about the math behind your negative conclusions about three generatiosn, sure sure
  sure?"
- The day's binding rules: "aleays verify, make sure we dont hit negatives because of bugs"; "do it correctly, informedly, and
  bug free in all load bearing math"; "all oallowed not just m004, choice might be golden".
- **sm:B1535 Corollary C3, first place.** A count of g ≥ 2 needs n(ν⁴) ≥ g − b0 and n(ν³ ⊗ ρ) ≥ g. Lemma W gives n = 0 at
  every puncture-trivial character, so on abelian covers the line can grow only at characters non-trivial on a puncture
  (sL-10 item 15).
- **sm:B1536 §10** names the covers' own characters as the next question. sm:B1536 reads only pulled-back characters.

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `git fetch --all` ran first. `scripts/checks/prior_work.py` then ran over every head with sixteen terms:
"puncture character", "puncture-trivial", "fibre-direction", "fiber-direction", "line supply", "origami", "square-tiled",
"Wollmilchsau", "Putman", "Prym", "Burau", "torsion coset", "polcyclofactors", "cyclotomic factor", "Lemma W", "b1 > cusps".

| head | commit |
|---|---|
| this branch | `e41609cf` |
| main | `cb09deb0` |
| the audit lane | `d1e0d049` |
| seat/determined-hopper | `7cda35aa` |
| seat/magical-wright | `0043be2b` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| seat/physics-seat-evaluation | `659487bb` |
| sep16-branch | `3205984b` |
| art/camper-van-bar | `b3745696` |

Every head was fetched again before the seal (2026-10-04, about 10:30Z and 11:00Z). Only the audit lane had moved, to
`62f52092` and then `317afd8b`, with five relays to cc and this seat (R85–R89, below).

"origami", "square-tiled", "Wollmilchsau", "torsion coset" and "b1 > cusps" are absent everywhere. The hits that bear on this
arc:
- **This seat's sm:B1532, sm:B1534, sm:B1535 and sm:B1536.**
  - sm:B1535: Theorem C, Lemma W and Corollary C3, the frame this arc reads.
  - sm:B1536: sealed and running. It reads every connected cover of degree ≤ 12 of m004 and m003, which includes the covers
    here of those states, at pulled-back characters only. Its Proposition Q (the Q₈ tower's line, after Putman–Wieland's
    Appendix A) is the non-abelian sibling of this question. This arc reads none of sm:B1536's records.
- **B349** (frontier, a structural census): every cover of the figure-eight through index 6, by SnapPy, with H₁. Its
  index-4 irregular cover with H₁ = ℤ² is m004's |D| = 4 cover here (two cusps, b₁ = 2, Lemma 2).
- **The fresh physics seat's R57**, "The three strands" (`seat/physics-seat-evaluation`, 2026-09-06; not banked; its link to
  θ was withdrawn by its R60).
  - Its three half-periods E[2]∖0, joined into one loop by the monodromy's 3-cycle, are the three-puncture orbit of m004's
    |D| = 4 cover here. A puncture character non-trivial there is a character of the three strands.
  - R57 proposed a count in a fibre frame and computed no twisted cohomology.
  - It also verified the Burau/Alexander fact control K7 uses: (σ₁σ₂⁻¹)² closes to the figure-eight, σ₁σ₂⁻¹ to the unknot.
- **The audit lane's RT6** (R84, RIGIDITY_TRANSPORT_PROOF.md): three needs both supplies at the same ν and an attaining
  class, and bending does not by itself give the line supply.
- **The audit lane's R85–R89** (`62f52092` and `317afd8b`, after the sweep). R85, R86 and R88 concern its joined background
  (the dual join, its relative gluing modes and their kinetics), and R89 the flat coefficient's domain; they do not bear on
  this question.
  - **R87 reviewed this arc's read-out** at the pre-seal snapshot `27dd37e2` and found two coverage holes. A missing cover
    could still read as "every cover read", because no expected manifest was compared. A candidate with an empty Part F
    returned P7 and P8 true, with zero readings and "routes agree".
  - **R89** credited K10 at `0762032d`, re-ran the same diagnostic there (before this seat's fix at `090ac4c0`), and asked
    for a producer-level certificate of covers, chunks, candidates and fourth roots.
  - All of it is closed before the seal: K11's manifest, Part F's candidate headers with the Smith form's count, K12's
    brute-force certificate of the fourth roots, and the rule of §9 (slip 8).
- **Hits that do not bear.** "Burau" on main is B205's q-metallic note. "fiber-direction" is B287's closed torus bundles.
  "cyclotomic factor" appears in unrelated arcs.

No head reads the line's supply at a character of a cover that is non-trivial on a puncture.

**The literature**, read on 2026-10-04:
- **Wikipedia, "Burau representation"**, §Relation to the Alexander polynomial.
  - If K is the closure of f ∈ B_n, then Δ_K(t) ≐ (1 − t)/(1 − tⁿ) det(I − f_*), with f_* the reduced Burau representation.
  - The primary sources it cites (Burau 1936; Birman, *Braids, Links and Mapping Class Groups*) were not read.
- **Wikipedia, "Figure-eight knot (mathematics)":**
  - the knot is the closure of σ₁σ₂⁻¹σ₁σ₂⁻¹, with Δ(t) = −t + 3 − t⁻¹;
  - its complement fibres with monodromy (2 1; 1 1).
- **Putman and Wieland**, J. London Math. Soc. 88 (2013), arXiv:1106.2747, Appendix A, read for sm:B1536 and cited through it.
  The genus-one failure of the higher-Prym conjecture: on the Q₈ cover of the once-punctured torus the mapping class group
  acts on the ℍ part through a finite group.
- **Hironaka**, "Alexander stratifications of character varieties", Ann. Inst. Fourier 47 (1997), Theorem 4.1.1 (Laurent's
  theorem, the torsion points of a subvariety of a torus), read at ar5iv for the design. **Leroux**, arXiv:0911.2594, abstract
  and introduction read: an algorithm for the torsion points. Both bear only on §10, the question of all orders.
- **Shapiro's lemma**, as sm:B1532 and sm:B1536 cite it (Kedlaya, *Notes on class field theory*, Lemma 3.2.3).
- **Gaschütz's theorem** for a finite quotient of a free group, H₁(K_Q; ℚ) ≅ ℚ ⊕ ℚ[Q₈] for F → Q₈, as sm:B1536's Proposition
  Q states and uses it. The finiteness of the units of an order in a definite quaternion algebra is the standard fact that
  Proposition H's proof re-proves in one line.

**Standing: EXTENDS.**
- sm:B1535's Lemma W is extended from abelian covers to every fibre-direction cover (Lemma W′, §3).
- sm:B1515's frame is read for the first time at a cover's own characters that are non-trivial on a puncture.
- Proposition H (§3) states the line's supply at a cover's own puncture character for the first time in this repo: on every
  state's (ℤ/2)² cover, at the character that cuts out the Q₈ cover, it sums to 4 over the roots of unity. Its mechanism is
  the finite quaternion action of Putman–Wieland's Appendix A, as in sm:B1536's Proposition Q.

## 1. The question

On every fibre-direction cover M_{D,w} with 2 ≤ |D| ≤ 12 of m004, m003, m136 and m135:
- At the finite-order characters that are non-trivial on some puncture, how large is the line's interior supply n(χ)?
  Where is it 2 or more?
- At every finite-order ν with ν⁴ such a character and n(ν⁴) ≥ 2: is ν a member, and is the four's supply n((ν⁻³ ⊗ ρ)*) at
  least 2?
By Theorem C, with Lemmas 2 and W′, this decides whether sm:B1515's frame has room for two or more generations at these
characters.

## 2. Definitions and conventions

- **The states.** sm:B1527's presentation Γ = F ⋊ ⟨t⟩, F = ⟨a, b⟩, t g t⁻¹ = φ(g), the cusp ⟨ℓ, t′⟩ with ℓ = abAB and t′ = t
  (+) or abt (−). The states are m004 = +LR, m003 = −LR, m136 = +LLRR and m135 = −LLRR. M is φ on H₁(F) = ℤ², hyperbolic.
- **The covers** (Lemma 1).
  - Take Λ ⊂ ℤ² with MΛ = Λ, of index |D|; D = ℤ²/Λ; K = ker(F → D); and a class w̄ ∈ D.
  - H = ⟨K, τ⟩, with τ = t·u_{w̄}; N = M_{D,w} is the cover with π₁N = H.
  - Γ acts on H\Γ = D by x^a = x + e_a, x^b = x + e_b, x^t = M⁻¹x − w̄.
- **The fibre.**
  - K is free on |D| + 1 Schreier generators.
  - The monodromy is f(k) = τkτ⁻¹ = φ(w k w⁻¹).
  - The punctures are ℓ_x = u_x ℓ u_x⁻¹, x ∈ D, and f sends ℓ_x to a conjugate of ℓ_{π(x)}, with π(x) = M(x + w̄) (+) or
    M(x + w̄) − e_a − e_b (−).
- **Characters.** χ = (ζ, s): ζ a character of K with ζ ∘ f = ζ, and s = χ(τ).
  - A **puncture character** has ζ(ℓ_x) ≠ 1 for some x.
  - The invariant ζ form Hom(coker(f_* − 1), ℚ/ℤ), read from the Smith form.
- **The frame** (sm:B1515, as sm:B1536 states it).
  - A finite-order ν with h¹(N; ν⁵ ⊗ ρ) ≥ 1 is a **member**.
  - capW = b0 + n(ν⁻⁴), with b0 = [ν⁴ = 1].
  - capL2 = n((ν⁻³ ⊗ ρ)*).
  - n is the interior dimension, and ρ the four at the hyperbolic point, exact over ℚ(ζ₂₄).
  - In sm:B1509's dictionary, g generations need min(capW, capL2) ≥ g at some member (sm:B1535 Theorem C).

## 3. The theorems (proved at design time)

**Lemma 1 (the covers).**
- K is normal in Γ, H ∩ F = K, and [Γ : H] = |D|.
- Every subgroup of index |D| meeting F in K whose t-degree map is onto has this form. Two of them are conjugate iff
  w̄ − w̄′ ∈ (M − 1)D (conjugating τ by u ∈ F moves w̄ by (M⁻¹ − 1)ū; conjugating by t multiplies it by M).
- The action on cosets is H u t = H t φ⁻¹(u) = H τ w⁻¹ φ⁻¹(u).
- *Checked by K0* against low_index on degrees up to 12 (m004, m003) and 8 (m136, m135).

**Lemma 2 (b₁ = #cusps; n(1) = 0).**
- H₁(N) = H₁(K)_f ⊕ ℤ. In H₁(K)_f the puncture part (ℤ^D/⟨Σℓ_x⟩)_f = ℤ^{orbits}/⟨(|O|)_O⟩ injects, because H₁(ℤ; Λ) = Λ^M = 0
  (M has no eigenvalue 1).
- The closed torus's part Λ/(M − 1)Λ is finite. So b₁(N) = #orbits = #cusps.
- Half lives, half dies then gives n(1) = b₁ − #cusps = 0.
- *Checked by K3* on every cover of population A.

**Lemma 3 (the puncture characters).**
- The puncture classes span the subgroup ℤ^{orbits}/⟨(|O|)_O⟩ of H₁(N), which is non-zero iff |D| ≥ 2. With one orbit it is
  the torsion ℤ/|D|, so puncture characters exist on every cover with |D| ≥ 2.
- The puncture-trivial invariant characters are those of Λ/(M − 1)Λ, a group of order |det(M − 1)|.
- *Checked as structure:* `Cover.puncture_trivial` asserts the order on all 80 covers.

**Lemma W′ (sm:B1535's Lemma W on every M_{D,w}).** At a finite-order χ trivial on every puncture, n(χ) = 0.
- The fibre closes up to the torus T̄_D, and the monodromy lifts to an Anosov map of it with matrix M.
- sm:B1535's proof then applies verbatim, with R84's corrected wording: the fibration class restricts non-trivially to the
  base loop of a cusp torus.
- *Checked by K2* in both routes.

**Lemma 4 (Wang, route W).** For ζ ≠ 1 on K, H⁰(K; ζ) = 0, and the Lyndon–Hochschild–Serre sequence of
1 → K → H → ⟨τ⟩ → 1 gives h¹(N; χ) = dim ker(J̄_ζ − s).
- J is the Fox Jacobian of f at ζ, and J̄ is J on H¹(K; ζ) = Z¹/ℂβ (β_i = ζ(y_i) − 1). J̄ has dimension |D|.
- For a cocycle z of H, z(f(k)) = s z(k) + (1 − ζ(k)) z(τ), so [z ∘ f] = s[z].
- *Checked by K1* (Part W's banked μ_u = τ_u at |D| = 1), by K7 (the literature), and by route P at every reading.

**Lemma 5 (half lives).** For unitary χ, n(χ) = h¹(N; χ) − #{cusps where χ is trivial}.
- The image of H¹(N) in H¹(∂N) is Lagrangian, and h¹(P; χ) = 2[χ|_P = 1] on a cusp torus P.
- Route P reads r1 directly, so the two routes test this at every reading.

**Lemma 6 (the transfer, route T).** For χ of order k and N′ the cover with π₁N′ = ker χ:
b₁(N′) − #cusps(N′) = Σ_{j mod k} n_N(χ^j).
- Shapiro on N and on its cusps, with Lemma 5 on N′.

**Corollary (where two can live on M_{D,w}).** On N = M_{D,w}, a count of g ≥ 2 at a finite-order member ν needs ν⁴ to be a
puncture character with n(ν⁴) ≥ g, and capL2 ≥ g.
- *Proof.* capW = b0 + n(ν⁻⁴), and n(ν̄) = n(ν) for unitary characters.
  - If ν⁴ = 1, then capW = 1 + n(1) = 1 (Lemma 2).
  - If ν⁴ ≠ 1 is puncture-trivial, then capW = 0 (Lemma W′).
  - Otherwise b0 = 0, and capW = n(ν⁴).
  - Then sm:B1535 Theorem C. □

So Part L's census of n at the puncture characters decides where Part F must look, and Part F decides the rest.

**Proposition H (the quaternion line).** Take N = M_{D,w} with Λ = 2ℤ², so that D = (ℤ/2)², on any state and at any w̄.
Map F → Q₈ = {±1, ±i, ±j, ±k} by a ↦ i, b ↦ j, with kernel K_Q. Then K_Q ⊂ K, K/K_Q is the centre {±1}, and ζ_H(k) is the
image of k there.
- **(H0)** ζ_H is invariant, so (ζ_H, s) is a character of H for every s, and ζ_H(ℓ_x) = −1 at every puncture.
- **(H1)** Σ_s n(ζ_H, s) = 4, the sum over every root of unity s.
- **(H2)** If τ acts on Q₈ (x ↦ φ(w x w⁻¹)) non-trivially, then n(ζ_H, s) ≤ 2 at every s. If τ acts on Q₈ as the identity,
  every n(ζ_H, s) is even.
- **Which covers.**
  - On the golden states m004 and m003, tr M is odd, so M has order 3 mod 2 and τ cycles the axes i, j, k: τ never acts as
    the identity.
  - On the silver states m136 and m135, M ≡ 1 mod 2, so φ acts on Q₈ by an inner automorphism. τ then acts as the identity
    for exactly one of the four classes w̄.
- *Proof.*
  - K_Q is characteristic in F (sm:B1536's Proposition Q: Aut(Q₈) acts simply transitively on the 24 generating pairs). So
    τ preserves K_Q and K, and acts trivially on K/K_Q ≅ ℤ/2: ζ_H is invariant. The puncture loop ℓ = abAB maps to
    [i, j] = −1, and each ℓ_x is a conjugate of ℓ: (H0).
  - Shapiro gives H₁(K_Q; ℚ) = H₁(K; ℚ) ⊕ H₁(K; ℚ_{ζ_H}); the second summand is where the central −1 acts by −1. By Gaschütz,
    H₁(K_Q; ℚ) ≅ ℚ ⊕ ℚ[Q₈], and −1 acts by −1 exactly on the quaternion part: ℍ_ℚ, the rational quaternion algebra as a left
    module over itself. So H¹(K; ζ_H) has dimension 4 = |D|, as Lemma 4 says.
  - τ acts on H₁(K_Q) semilinearly: ψ(g·x) = β(g)·ψ(x), with β ∈ Aut(Q₈). On ℍ_ℚ this gives ψ(x) = β̃(x)·ψ(1), and
    β̃(x) = c x c⁻¹ (Skolem–Noether), so ψ(x) = c x w.
  - Aut(Q₈) is finite, so ψ^e commutes with Q₈ for e = ord β. Then ψ^e is right multiplication by a quaternion u that
    preserves a lattice: a unit of an order of the definite algebra ℍ_ℚ. Its reduced norm is a positive-definite form, so
    there are finitely many such units, and ψ has finite order. It is diagonalisable, with roots of unity as eigenvalues.
  - No cusp is trivial for (ζ_H, s) by (H0), so n = h¹ = dim ker(J̄ − s) (Lemmas 4, 5). The four eigenvalues give (H1).
  - Over ℂ, ℍ ⊗ ℂ ≅ M₂(ℂ), and x ↦ c x w has eigenvalues λ_a μ_b (a, b = 1, 2), the λ_a of c and the μ_b of w.
    - If β ≠ 1, c is not central and λ₁ ≠ λ₂. Any three of the four products include two with the same μ_b and different
      λ_a, so no eigenvalue is threefold.
    - If β = 1, c is central and ψ is right multiplication by w, so every eigenvalue's multiplicity is even: (H2).
  - The axes i, j, k are the three non-zero classes of Q₈/{±1} = D, permuted by M mod 2. When tr M is odd, the
    characteristic polynomial is x² + x + 1 mod 2, of order 3.
  - When M ≡ 1 mod 2, β is conjugation by an element of Q₈. τ = t·u_w̄ composes it with conjugation by w̄'s class, and these
    four conjugations are Inn(Q₈) ≅ (ℤ/2)². So exactly one w̄ gives the identity. □
- *The structure is checked by K10* (the characters, the axis permutation and the identity class; no line is read). The
  supplies themselves are sealed as P9–P11.
- sm:B1536's Proposition Q is this mechanism on the Q₈ tower. There n(1) = dim (ℍ_ℚ)^{ψ^m}, which by the transfer is
  Σ_{s^m = 1} n(ζ_H, s) here.

## 4. The instruments (`verification/`, written and tested before the seal)

All five modules are named `punct_*`: no other module of that name exists on any tracked path (the E12 hazard, §6).
- `punct_covers.py`: the covers, the Schreier basis of K, the monodromy, the punctures and π, and k_x (for χ on Γ's
  Reidemeister–Schreier words).
  - The cusps come from sm:B1536's `cover_lib` (by path, read only), and the invariant character group from the Smith form
    (PARI).
  - Also the Galois-orbit representatives, the puncture-trivial subgroup, and the fourth roots ζ′ of ζ.
- `punct_wang.py` (route W).
  - The Fox Jacobian at ζ, and J̄, exact over ℚ(ζ_m) (PARI).
  - Its characteristic polynomial, normed to ℤ[x], and PARI's `polcyclofactors`, whose entries are split into their
    irreducible factors Φ_k (an entry can be a product: slip 5).
  - Every primitive k-th root s of every cyclotomic factor is tested by the exact rank of J̄ − s over ℚ(ζ_lcm(m,k)). So the
    roots of unity s with h¹ ≥ 1 are found completely.
  - Then the trivial cusps (χ on each cusp's two peripheral words) and n by Lemma 5.
- `punct_present.py` (route P).
  - H presented by Reidemeister–Schreier from Γ, with its own transversal (BFS on t, a, b).
  - The Fox matrix at χ over GF(p), p ≡ 1 mod L (python-flint).
  - h¹, and r1 read directly from the restrictions to the cover's own cusps.
  - Route P4 is the same for modules: the four.
- `punct_transfer.py` (route T).
  - The action of Γ on Γ/ker χ, checked by sm:B1536's `cover_lib.check_cover`, which also confirms that χ is a character.
  - H₁(N′; ℤ) from N′'s own presentation, with its rank by python-flint's fmpz_mat, and N′'s cusps.
  - No twisted coefficient enters.
- `punct_four.py` (Part F).
  - Route R is sm:B1536's `route_r`, loaded by path: PCover, CMod, Coh, base_word with PARI's elimination. The module on
    route R's Schreier generators is ν(w_j) ρ(w_j).
  - Route P4 is route P's presentation and module cohomology.
  - The exact four (sm:B1536's `cover_lib.state`) is mapped to GF(p) by the same field map as the character.
- `run.py` (Part L in chunks of at most 20,000 Galois orbits, largest first, resumable; Part F, each candidate with a header
  row of its planned readings and its fourth roots counted twice, enumerated and by the Smith form), `read_out.py` (P1–P11,
  against K11's manifest and Part F's headers), `controls.py` (K0–K12), `identity.py` (§8).

## 5. The population

**Population A.** The four states; every fibre-direction cover with 2 ≤ |D| ≤ 12, up to conjugacy (80 covers).

**The characters, per cover.**
- Every invariant fibre character ζ with ζ^{m(C)} = 1, read one per Galois orbit. h¹, the cusp triviality and n are Galois
  invariants.
- m(C) = lcm(b, e): e is the exponent of the torsion of the invariant character group, and b is the first of 12, 6, 4, 2, 1
  whose Galois-orbit count is at most 300,000.
- One cover is read at b = 6: m135's |D| = 8 cover (4, 2, 2) at w̄ = 5, with eight cusps and free rank 7. All other covers
  are read at b = 12, and none is above the budget at b = 1.
- Every root of unity s is read, completely (route W). Puncture-trivial ζ are Lemma W′'s and are read in the controls.

| state | covers | puncture characters | Galois orbits |
|---|---|---|---|
| m004 (+LR) | 5 | 583 | 201 |
| m003 (−LR) | 9 | 39,695 | 7,313 |
| m136 (+LLRR) | 29 | 807,820 | 210,524 |
| m135 (−LLRR) | 37 | 1,558,524 | 444,950 |
| **total** | **80** | **2,406,622** | **662,988** |

**At every Galois orbit (Part L).**
- Route W finds every root of unity s with h¹ ≥ 1.
- Route P reads every such (ζ, s) at two primes.
- Route P also reads s = 1 and s = −1 at every orbit, and all of μ₁₂ at a fixed 1-in-50 sample (crc32), against route W's
  list.
- Route T reads every hit (n ≥ 1) whose N′ has degree ≤ 2,400, against Σ_j n(χ^j) read by route P.

**Part F.**
- It runs only at candidates: hits with n ≥ 2.
- At each, every ζ′ with ζ′⁴ = ζ, and s′ with s′⁴ = s, is read. The candidate's header row records the planned readings,
  four per ζ′, and the count of ζ′ twice: enumerated, and by the Smith form. The read-out requires the two counts to agree
  and every planned reading to be present.
- Membership is read in both routes at every ν, and the supplies in both routes at every member.

## 6. Controls and disclosures (before the seal)

The controls (`controls.py`, recorded in `controls.json`, all holding):
- **K0 (Lemma 1).** The covers enumerated here are exactly the transitive actions of degree ≤ 12 (m004, m003) or ≤ 8 (m136,
  m135) on which a and b commute and ⟨a, b⟩ is transitive (low_index, through sm:B1536's cover_lib), compared as Γ-sets.
- **K1 (banked, |D| = 1).** On all 541 rows of sm:B1529's census:
  - route P reproduces sm:B1535 Part W's (h¹, r1) pattern at every (u, κ ∈ μ₁₂);
  - route W finds, at every fibre character u ≠ 0, exactly one root of unity, with h¹ = 1, n = 0 and s = τ_u (Part W's
    μ_u = τ_u).
- **K2 (Lemma W′).** On every cover of population A, at every invariant character trivial on the punctures:
  - every root route W finds has n = 0, and route P agrees on h¹, the trivial cusps and n;
  - route P reads n = 0 at every s ∈ μ₁₂, and agrees with route W's list.
- **K3 (Lemma 2).** b₁ = #cusps on every cover.
- **K4 (route T against SnapPy).** The multisets of (b₁, #cusps) over every cover of degree 2–6 of the four states (286
  covers) equal SnapPy's (`Manifold.covers`).
- **K5 (the transfer on controls).** At the puncture-trivial characters of K2 with a root, route T reads
  b₁(N′) − #cusps(N′) = 0.
- **K6 (Part F, banked).** At |D| = 1 on the four states, at every (u, κ ∈ μ₁₂), route R, route P4 and sm:B1536's own
  pulled-back `route_r.supplies` agree on every supply. The members with capL2 ≥ 1 are exactly the banked ones: m135's u₁, u₂
  at κ = 1 (sm:B1530) and m136's u₁, u₂ at κ = −1 (sm:B1535 C1). m004's only member is the trivial character, with
  capW = 1.
- **K7 (literature).** For the Artin action of (σ₁σ₂⁻¹)² on F₃ at x_i ↦ t, route W's J̄ gives
  det(I − J̄) ≐ (1 + t + t²)(t² − 3t + 1), exactly, at t = ζ_m for m = 5, 7, 8, 9, 12, 20.
- **K8.** The Galois-orbit enumeration is complete: the orbit sizes sum to the number of characters ≠ 1.
- **K9.** The read-out on synthetic rows, twenty-six cases, one per branch, with the predictions fixed by hand. They include
  R87's two probes and the other coverage branches: a missing, duplicated, short or unexpected record, no manifest, a
  candidate short of its planned readings, a candidate whose two fourth-root counts differ, and a refuting row found on
  incomplete records.
- **K10 (Proposition H's structure).** On the ten covers with D = (ℤ/2)² (one each of m004 and m003, four each of m136 and
  m135), by structure alone; no line is read.
  - Every Schreier generator maps to ±1 in Q₈ under a ↦ i, b ↦ j, and to the same signs under a ↦ j, b ↦ k (K_Q is
    characteristic).
  - ζ_H is invariant, −1 at every puncture, and one of the run's own Galois representatives.
  - τ cycles the axes on m004 and m003 (on m004, i ↦ k and j ↦ i), and acts as the identity on exactly one class of each
    silver state (m136 at w̄ = 3, m135 at w̄ = 0).
  - The ten characters are recorded for the read-out.
- **K11 (the population manifest).** For every cover of population A: the chunks `run.py` writes, and the puncture
  characters and their Galois orbits at m(C), by formula rather than by the run's enumeration.
  - All characters with ζ^{m(C)} = 1 by the Smith form's count, their Galois orbits by Möbius inversion (`run.py`'s own
    functions), minus the puncture-trivial characters in range (enumerated, at most 8 per cover) and their orbits.
  - The per-state totals equal §5's table, which was counted by enumeration: 80 covers, 108 chunks.
  - The read-out compares the records with this manifest before it certifies any population-wide prediction.
- **K12 (Part F's fourth roots, the audit lane's R89).** On every cover with |D| ≤ 5 (40 covers): every character ν with
  ν⁴⁸ = 1 is enumerated and grouped by ν⁴. At a fixed sample of characters ζ with ζ¹² = 1, Proposition H's ζ_H always
  among them, `Cover.fourth_roots(ζ, 12)` equals ζ's group and the Smith form's count. Structure only: no line or four is
  read.

**Pre-seal slips**, each logged in ERROR_LEDGER:
1. **A design-note statement.** "Puncture characters exist exactly when #orbits ≥ 2, which holds whenever |D| ≥ 2" was wrong
   both ways.
   - They exist whenever |D| ≥ 2 (Lemma 3).
   - An affine monodromy can be transitive: m003, D = ℤ/5, w̄ ≠ 4 has one cusp.
   - Caught by the structure run, before any outcome.
2. **E12, the library's name.** It was first named `fibre_lib.py`, sm:B1529's module name, and sm:B1529's
   `post_run_exact_m135` imports that by bare name. Caught by the crash; all five modules were renamed `punct_*`.
3. **A read-out bug.** P8's comprehension had its clauses in the wrong order and raised whenever Part F had a member.
   Caught by K9; fixed.
4. **E12 again, in the controls.** sm:B1536's `route_r` puts sm:B1535's directory first on sys.path, and sm:B1535 has its
   own `read_out.py` and `controls.py`. K9's bare import got sm:B1535's. Caught by K9; `read_out` and `controls` are now
   loaded by their paths.
5. **Route W's cyclotomic factors.** PARI's `polcyclofactors` can return a product of distinct cyclotomic polynomials as one
   entry: Φ₅Φ₁₅ = Φ₅(x³), on m003's (2, 0, 2) cover. `poliscyclo` reads such an entry as 0.
   - The index 0 then raised, so no root could be lost silently.
   - Caught by K2's crash, at a puncture-trivial character.
   - Route W now splits every entry into its irreducible factors and asserts that each is cyclotomic. The controls were
     re-run in full on the final code.
6. **The draft's priors contradicted Proposition H.**
   - The draft gave P4 75%, P5 45% and P6 50%.
   - Proposition H, derived afterwards from the mechanism of sm:B1536's sealed Proposition Q, implies P4 and contradicts P5
     and P6.
   - Caught while writing a report to the owner, before the seal. The priors are revised in §7, with the draft's values
     shown.
7. **Two record-format errors in the draft verdict.** Its scope's reach read "character", which the schema does not allow,
   and four fields carried bare pipes that the views put in tables. Caught by the schema test and a pipe check before any
   commit.
8. **The read-out's coverage** (found by the audit lane's R87, at the pre-seal snapshot `27dd37e2`).
   - The read-out compared no expected manifest, so a missing cover could still read as "every cover read".
   - A candidate with an empty Part F returned P7 and P8 true, with zero readings and "routes agree".
   - Either could have certified a negative on incomplete records. Both were reproduced on the old read-out before the fix.
   - R89, reviewing the snapshot `0762032d`, asked further for a producer-level certificate of the fourth roots.
   - Closed: K11's manifest, Part F's candidate headers with both fourth-root counts, K12's brute-force certificate, and the
     rule of §9. K9 now holds both probes as cases.

**Disclosures.**
- **sm:B1536's records are not read here.** Its m004 rows exist in this working tree; this arc reads none of them. After
  sm:B1536 banks, two post-bank cross-checks, outside this verdict:
  - its n(1) on every cover of degree ≤ 12 checks, through the transfer, every puncture character here with k·|D| ≤ 12;
  - its n(1) on m004's and m003's Q₈ tower at level m checks Σ_{s^m = 1} n(ζ_H, s) here (Proposition H).
- **The timing.** Route W and route P cost was measured on the controls' reads, on the same covers and field sizes.
  - K2, with K3 and K5: 462 puncture-trivial characters, 1,271 route-W roots and 6,815 route-P reads in 5.6 s.
  - K1: 567,996 route-P and 46,792 route-W reads at |D| = 1 in 1,097.6 s.
  - The machine was shared with sm:B1536's two sealed runs and a test lane. No puncture character was timed.

## 7. Predictions (sealed; `read_out.py` reads them)

| | prediction | prior |
|---|---|---|
| P1 | the identity holds (§8): K0–K12 reproduce `controls.json`, and every sealed file hashes as sealed | 97% |
| P2 | route P agrees with route W at every root read (both primes), and at every μ₁₂ check | 95% |
| P3 | route T agrees with Σ_j n(χ^j) at every hit it reads | 93% |
| P4 | some puncture character of population A has n ≥ 1 | 97% (draft 75%) |
| P5 | no puncture character of population A has n ≥ 2 | 5% (draft 45%) |
| P6 | no puncture character on m004's covers has n ≥ 1 | 4% (draft 50%) |
| P7 | Part F: at every candidate, no member has capL2 ≥ 2 (true if there is no candidate) | 82% (draft 83%) |
| P8 | the verdict: no member over population A's characters has min(capW, capL2) ≥ 2 | 82% (draft 83%) |
| P9 | Proposition H (H1): Σ_s n(ζ_H, s) = 4 on each of K10's ten covers | 92% |
| P10 | Proposition H (H2): n(ζ_H, s) ≤ 2 at every s on the eight covers where τ acts on Q₈ non-trivially | 88% |
| P11 | Proposition H (H2): n(ζ_H, s) is even at every s on the two covers where τ acts on Q₈ as the identity | 88% |

P7 and P8 coincide when the routes agree, since capW = n(χ) at a candidate's members (the Corollary). The priors expect 8.23
of 11.

**The priors were revised before the seal** (slip 6). The draft's priors for P4–P8 were written before Proposition H.
- By Proposition H, P4 holds and P5 and P6 fail, unless the instruments or the proposition are wrong.
  - P5 fails at the two identity covers (P11 with P9).
  - P6 fails at m004's (ℤ/2)² cover (P9).
- Part F will then have candidates, so P7 and P8 are tested rather than vacuous.
- The draft's values are kept in the table.

## 8. BANKED IDENTITY: checked before reading

Before `run.py` reads anything, `identity.py` re-runs `controls.py` (K0–K12). It requires every field of `controls.json` but
the timings to be reproduced, and every sealed file's sha-256 to match `ARTIFACT_HASHES.txt`. A single difference stops the
run, and nothing is read.

## 9. Reading rules, and what this arc will and will not claim

- **The read-out runs once**, on complete records (every chunk of every cover; Part F's rows if there are candidates). It
  writes `read_out.json` and `read_out_log.txt`. Nothing is re-run after it except as a disclosed post-run check.
- **Coverage decides what can be certified** (the audit lane's R87).
  - Complete records: every chunk of K11's manifest exactly once, read, with no other cover, each cover's puncture orbits
    summing to the manifest's; and, for P7 and P8, every candidate's header, its two fourth-root counts equal, and exactly
    its planned readings.
  - A prediction that a found row refutes is False on that row, whatever the coverage.
  - A population-wide prediction is True only on complete records. Otherwise it is None: missing, duplicate, short or empty
    records never certify a negative.
- **P9 is the run's positive control inside its own population.** A theorem says the line is there. A run that misses it
  has a bug, or the theorem is wrong, and either way no verdict is read until that is resolved and recorded.
- **The verdict.**
  - **NEGATIVE** (scoped) if P1–P3, P9 and P8 hold. No finite-order member over population A's read characters has room
    for two generations in this frame. Stated with its population: the 80 covers, ζ of order dividing m(C), every root of
    unity s, ν with ν⁴ among them.
  - **PROVED** (room for two) if P1–P3 and P9 hold and P8 fails: some member has min(capW, capL2) ≥ 2.
    - That is room, not a count. The class readings (Part O) are then the next arc, sealed separately before any class is
      read.
  - **OPEN** if any of P1–P3 or P9 fails, until the cause is resolved and recorded.
- **P10 and P11 test (H2).** A failure is re-read in both routes and reported as it is before the bank. It does not by itself
  change the verdict's reading.
- **Every negative is read in two routes.**
  - The line in routes W and P. Route T is the transfer's third reading.
  - The four in routes R and P4.
- **This arc does not claim** a count of generations, which state or cover is physical, anything about non-unitary characters
  or off the hyperbolic point, I-26, or the experiential question. **0 of 19 stays 0.**

## 10. What this arc does not decide (the next questions)

- **Every order.** Characters of order not dividing m(C).
  - By Laurent's theorem (Hironaka, Theorem 4.1.1), the torsion points of each jump locus lie in finitely many torsion
    cosets.
  - Reading the cosets themselves (Leroux's algorithm and its relatives) would remove the order bound.
- **Larger covers** (|D| > 12), **the other word states and m004's levels**.
- **Fibre deck groups that are not abelian**: sm:B1536, and its Q₈ tower.
- **Proposition H beyond D = (ℤ/2)².** Every cover whose fibre group lies between K_Q and ker(F → (ℤ/2)²) carries the
  quaternion part, and the four at ζ_H's fourth roots is read only where Part F reaches.
- **Non-unitary characters on covers with several cusps** (C3's third place).
- **R57's question in its own frame:** the count read on the fibre at the three half-periods. This arc reads sm:B1515's frame
  on the 3-manifold.
