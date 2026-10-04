# DOSSIER — the golden covers and room for three (2026-10-04)

cc (the SM-derivation seat), 2026-10-04. **Status: design-time structure and literature. Not sealed. No homology rank and no
twisted cohomology of any cover below has been computed**, except the four's cohomology of the closings F_m at the trivial
character, which checks a published theorem (§4 (c)). Everything here is one of four things:
- group theory reproduced by `gc_icosian.py` and `gc_binary_polyhedral.py` (records `gc_icosian_run.txt` and
  `gc_binary_polyhedral_run.txt`, a few seconds each);
- that published check, `gc_fibonacci.py` (record `gc_fibonacci_run.txt`, about 10 s);
- a published statement read on the date given;
- a claim marked OPEN.

Negatives found on the way are kept beside the positives, and one overstatement of this note's first draft is corrected in
§1b. **Price:** unchanged, 0 of 19.

**Why it is written down now.** The owner, 2026-10-04: "three generations is smth we are after seripuslu"; "make sure u dont
put results under the carpet"; "make sure nothing is lost. make sure we dont abandon the golden pointer". These leads were
found while sm:B1538 and sm:B1536 run sealed; they are registered as sL-12 in `docs/OPEN_LEADS.md`.

## 1. The icosian line on the golden states (computed, structure only)

The fibre group F₂ = ⟨a, b⟩ and each state's monodromy φ (sm:B1527's presentation, through sm:B1538's `punct_covers.State`).
- **The kernels.** SL(2,5) = 2I, the binary icosahedral group, has 9,120 generating pairs. Up to Aut(2I) = PGL(2,5) they give
  76 kernels of F₂ → 2I. They lie 4 over each of the 19 kernels of F₂ → A₅ (Hall's count, reproduced).
- **How the monodromy permutes the 76.**

  | state | fixed 2I-kernels | cycle type of φ on the 76 |
  |---|---|---|
  | m004 = +LR (golden) | 2 | 1, 1, 3, 3, 5, 5, 7, 15, 15, 21 |
  | m003 = −LR (golden) | 2 | 1, 1, 3, 3, 5, 5, 7, 15, 15, 21 |
  | m136 = +LLRR (silver) | 0 | 4⁸, 6⁴, 10² |
  | m135 = −LLRR (silver) | 0 | 4⁸, 6⁴, 10² |

  So at level 1, of these four states, only the golden ones have fibre-direction A₅ covers on which the central character
  ζ of 2I is invariant. This is not special to the golden states among all word states: see §1b.
- **At each of the four fixed kernels:**
  - the puncture loop [a, b] maps to an element of order 6 in SL(2,5). Its A₅ image has order 3, so each boundary of the
    A₅ cover wraps three times and ζ = −1 on every puncture loop: a puncture character with no ζ-trivial cusp;
  - φ acts on 2I by conjugation with determinant 2 or 3, a non-square mod 5: an outer automorphism.
- **The covers.** Over each fixed kernel the twists give 3 inequivalent covers of degree 60, so 6 per golden state and 12 in
  all. By cusp pattern:
  - five cusps of 12, where τ acts on 2I by an outer automorphism of order 4;
  - cusps 3, 3, 18, 18, 18, outer of order 6;
  - cusps 3, 3 and nine of 6 (eleven cusps), outer of order 2.
- **What this implies (argument, not yet a sealed theorem; Proposition H's mechanism, sm:B1538 §3).**
  - The ζ-part of the fibre homology is the faithful part of ℚ[2I]. It contains the icosian algebra, the totally definite
    quaternion algebra over ℚ(√5), with multiplicity one.
  - Its unit group of reduced norm one is finite. So the monodromy acts there with finite order, and 8 of the 60 eigenvalues
    are roots of unity: the icosian line.
  - The automorphism is outer, so it swaps the two Galois-conjugate blocks, and the eigenvalues come in pairs ±.
  - On the eleven-cusp covers (order 2) the line's supply n(ζ, s) can reach 4 at a single s. That happens exactly when τ²
    acts as ±1 on the icosian part. Elsewhere it is at most 2.
  - The other faithful components, 4′ and 6′, are matrix algebras over quaternion algebras. Their finiteness is not forced
    by this argument.
- **Not the simple congruence covers.** Reduced mod 2 (ℤ[ω]/2 = 𝔽₄, PSL(2,4) ≅ A₅), the golden holonomy (sm:B1530's exact
  Eisenstein holonomy) gives these orders:
  - the fibre's image in PGL(2,4) has order 5, on both states;
  - the whole group's image has order 10 on m004 and 5 on m003 (in this presentation);
  - paired with each fixed kernel, the generated subgroup of PSL(2,4) × PSL(2,5) has order 300, not 60.

  So the icosian covers are not m004's level-2 congruence covers, and no known modular-form count predicts the four's supply
  on them. It has to be read.

## 1b. The binary polyhedral census, and a correction (computed, structure only)

`gc_binary_polyhedral.py` counts the kernels of F₂ → G for G = Q₈, 2T, 2O, 2I (unit quaternions, built by closure) through
the regular action, with no matrix model. A kernel is the BFS-canonical Cayley-graph labelling of its generating pair. This
is a second route to §1's 2I numbers, and it reproduces them: 9,120 generating pairs, 76 kernels, and the same cycle types.

| G (order; kernels) | m004 = +LR | m003 = −LR | m136 = +LLRR | m135 = −LLRR |
|---|---|---|---|---|
| Q₈ (8; 1) | fixed; outer, order 3 | fixed; outer, order 3 | fixed; inner | fixed; the identity |
| 2T (24; 16) | none; cycles 2², 6² | none; cycles 2², 6² | none; cycles 4⁴ | none; cycles 4⁴ |
| 2O (48; 18) | none; cycles 9² | none; cycles 9² | 4 fixed, outer | 4 fixed, outer |
| 2I (120; 76) | 2 fixed, outer | 2 fixed, outer | none | none |

- The Q₈ row agrees with sm:B1538's control K10. The golden monodromy cycles the axes. On the silver states it is inner,
  and becomes the identity after the twist K10 names.
- At the silver states' four fixed 2O kernels the puncture loop has order 6. The automorphism is outer, of order 2 modulo
  inner, so it swaps the two Galois-conjugate faithful 2-dim irreps (√2 ↦ −√2). The octahedral analogue of §1's argument
  would apply there (not sealed).
- No state of the four fixes a 2T kernel at level 1. The golden states fix 4 at M₂ and all 16 at M₆; the silver states fix
  all 16 at M₄.
- **The correction.** This note's first draft said that only the golden monodromy fixes icosian kernels at level 1. That
  holds for sm:B1538's four states only. Over every word state of length 2 to 6 (25 cyclic words, both signs):
  - 28 of the 50 fix a 2I kernel at level 1, 14 fix a 2O kernel and 20 fix a 2T kernel; 8 fix none of the three;
  - for example ±LLLLR (trace 6) fixes 2 icosian kernels, while ±LLRR (also trace 6) fixes octahedral ones.
  - So the binary polyhedral group a state fixes is not read off its trace field. The icosian line is a property of many
    states, not a golden selection. The golden states are among those that carry it.

## 2. What counts against it (kept, not buried)

- **Membership over the icosian line needs genuine interior classes of the four.**
  - Let ν be a character of the cover with ν⁴ = (ζ, s). On each cusp the fibre's boundary loop ∂ has ζ(∂) = −1, so ν(∂) is a
    primitive 8th root of unity and ν⁵(∂) = −ν(∂) ≠ 1.
  - The four is unipotent on the cusp group, so ν⁵ ⊗ ρ has no cusp cohomology. Then h¹(N; ν⁵ ⊗ ρ) is all interior: ν is a
    member only if the four has an interior class at ν⁵.
  - The boundary, which makes every ν with ν⁵ trivial on a cusp a member, gives nothing here.
  - So on the icosian covers capW is not the bottleneck. The four is.
- **m004's bending surfaces are not small.**
  - Jung and Reid (arXiv 2003.05427, abstract read 2026-10-04) study closed embedded totally geodesic 2-orbifolds in the Bianchi
    orbifolds H³/PSL(2, O_d). They list conjecturally the d for which there are none.
  - d = 3 has none: m004 is a degree-12 cover of H³/PSL(2, O₃), and as the complement of a small knot it has no closed
    embedded incompressible surface.
  - So the closed totally geodesic surfaces of §3 embed only in genuinely larger covers of m004. A census of small covers can
    come back negative even if room for three exists higher up.

## 3. Room for three by bending (literature chain; partly verified)

In sm:B1515's frame with sm:B1535's Theorem C (g ≤ min(capW, capL2)), at the trivial character ν = 1 of a finite cover N:
- every ν = 1 is a member (the cusps give h¹(N; ρ) ≥ #cusps);
- capW = 1 + n(1), with n(1) = b₁ − #cusps;
- capL2 = n(ρ), the four's interior supply, since ρ is real and self-dual.

So **room for three at ν = 1 ⟺ n(1) ≥ 2 and n(ρ) ≥ 3**. A chain of published results would give such an N.

1. m004 is arithmetic (PSL(2, O₃)), and non-cocompact arithmetic Kleinian groups contain cocompact arithmetic Fuchsian
   subgroups, so m004 contains closed immersed totally geodesic surfaces. **OPEN:** read Maclachlan–Reid, *The Arithmetic of
   Hyperbolic 3-Manifolds*, ch. 9, at source.
2. **Long** (Bull. London Math. Soc. 19, 1987): immersed totally geodesic surfaces lift to embedded non-separating surfaces in
   finite covers. **Verified as cited:** DeBlois, "Totally geodesic surfaces and homology", Algebr. Geom. Topol. 6 (2006)
   1413–1428, introduction, read 2026-10-04. Long's paper itself is not yet read.
3. **Bending.** Scannell, "Infinitesimal deformations of some SO(3,1) lattices", Pacific J. Math. 194 (2000) 455–464 (read
   in full 2026-10-04). A closed embedded totally geodesic surface gives non-trivial deformations into SO₀(4,1), which the
   paper calls well known and credits to Johnson–Millson and to Apanasov's examples.
   - so(4,1) = so(3,1) ⊕ ℝ^{3,1}, so these are classes of the four.
   - Bart–Scannell (Canad. J. Math. 58, 2006, read in full for sm:B1536) and Monroe (arXiv 2604.22004, cited by sm:B1535)
     carry bending to finite volume, with lower bounds.
   - **OPEN:** read the independence statement, that k disjoint surfaces give k independent interior classes.
4. Two non-separating, non-homologous closed surfaces give two independent compactly supported dual classes, so n(1) ≥ 2.
   Parallel lifts in a cyclic cover are homologous modulo the cusps and do not count twice. **OPEN:** written proof.

**If 1–4 hold**, some finite cover of m004 has min(capW, capL2) ≥ 3 at ν = 1, and likewise any arithmetic cusped M.
- Theorem C's caps then cannot exclude three generations on every finite cover. Negatives are scoped to their populations:
  sm:B1536's degree ≤ 12 and Q₈ towers, sm:B1538's fibre-direction abelian covers.
- The decisive questions become:
  - the class count, a generation-shaped (−3, −3) at a member with room;
  - which cover is selected. GENESIS GAP4 and THE_BAR apply: room on large covers without a selector is a landscape, not a
    prediction.
- This is room, not a count.

## 4. The golden pointer (not to be abandoned)

Three strands, all golden:
- **(a) The icosian covers (§1).** Of sm:B1538's four states only the golden ones fix icosian kernels at level 1. Many other
  word states do as well (§1b). The 12 golden covers are explicit and small enough (degree 60; 2I double covers of degree 120)
  for the four's supply to be read exactly.
- **(b) Q₈ and 2T.** On the golden states the monodromy τ of the (ℤ/2)² cover cycles the axes of Q₈ (on m004
  i ↦ k ↦ j ↦ i, order 3; sm:B1538's control K10, the structure behind its Proposition H). Q₈ ⋊ ℤ/3 = 2T, the binary
  tetrahedral group the record already meets: 2T is the pointwise stabiliser of the E₆ locus in the record's flat G₂
  orbifolds (B1084, B1353, B1357), the McKay group of E₆. That is a coincidence of groups, not yet a mechanism: nothing here
  links the cover's deck group to that stabiliser. sm:B1536 reads the Q₈ tower (n(1) = 4 there by its Proposition Q, so
  capW = 5 at κ = 1), and its read-out gives n(ρ) on that tower.
- **(c) The Fibonacci manifolds, which are the record's closings Yₙ.**
  - F_m is the m-fold cyclic cover of S³ branched over the figure-eight knot, with π₁ = F(2, 2m). It is hyperbolic for
    m ≥ 4, Euclidean at m = 3 (Hantzsche–Wendt) and the lens space L(5, 2) at m = 2.
  - These are the record's closings Yₙ (B1273, B1301, B1303: π₁(Yₙ) is the fixed quotient of φⁿ, and |H₁(Yₙ)| = L₂ₙ − 2).
    sm:B1515's population A takes every character of the torsion of H₁(Mₙ) at λ = 1 on M₁–M₆, which is 1, 5, 16, 45, 121
    and 320 characters. Those are exactly the character groups of H₁(Y₁), …, H₁(Y₆).
  - **Scannell, read at source** (Pacific J. Math. 194 (2000) 455–464, read in full 2026-10-04).
    - Theorem 4.3: for every m ≥ 4, dim H¹(π₁F_m; so(4,1)) = dim H¹(π₁F_m; ℝ^{3,1}) = 2.
    - Corollary 4.2 gives the bound ≤ 2. F_m is the 2-fold branched cover of the Turk's-head 3-braid B_m, so the orbifold
      group is generated by three involutions.
    - F₄ has the volume of 4_1, is non-Haken, and has no non-elementary Fuchsian subgroup, so these classes do not come from
      bending.
    - Integrability is left open in the paper.
  - **Verified with own code** (`gc_fibonacci.py`, record `gc_fibonacci_run.txt`, about 10 s).
    - dim H¹(F_m; ℝ^{3,1}) = 2 at m = 4, …, 8.
    - Control on banked data: the cusped levels M₁–M₆ at their own holonomy give 1, the cusp's half. This agrees with
      sm:B1515: no interior class at the trivial character through level 6.
    - The 78 other fillings (p, 1) of M₄–M₈ with the same |H₁| all give 0.
  - **What it means for three (kept, not buried).**
    - Positive: on the golden closings the four has exactly two classes at the trivial character, with no totally geodesic
      surface. Among the fillings tested, only the branched-cover filling has them.
    - Negative, scoped: F_m is a rational homology sphere, and the record's 2×2 criterion (B1303) gives h¹(Yₙ; ψ) ≤ 1 at
      every non-trivial character ψ. With b0 = [ν⁴ = 1], capW = b0 + n(ν⁴) ≤ 1 at every character of every Yₙ. So if
      Theorem C's caps are read on a closed manifold, the closings host at most one generation. That reading is not
      established: sm:B1515's frame is set at a cusped hyperbolic point. B1351's index theorem already makes the closings
      vector-like in its own frame.
    - The Fibonacci strand locates the four's classes. It is not a host for three.
    - Open: n(ψ ⊗ ρ) at the non-trivial characters ψ of H₁(Yₙ), the closed counterpart of sm:B1515's population A (where
      M₆ gave n = 2 at its four order-5 characters). This is an open outcome, to be sealed before it is computed.
  - **Next:** the four's classes on covers where the line can exceed one per character: the Q₈/2T and icosian covers of the
    golden states, cusped or closed.

## 5. Next steps (registered; each sealed before any outcome is read)

1. Bank sm:B1538 and sm:B1536; read their n(ρ) and caps first.
2. A sealed census at the trivial character: n(1) and n(ρ) on every connected cover of m004 and m003 of degree 13 to D (low_index),
   the 12 icosian covers and their 2I double covers at the levels where the icosian part is trivial, then the class counts
   wherever room exists. The routes are Fox matrices with 4-dimensional coefficients at two primes, plus a second route.
3. Literature at source: Long 1987; Maclachlan–Reid ch. 9; Johnson–Millson's independence; Monroe's theorem. Scannell's
   Fibonacci construction is read (§4 (c)).
4. Then decide whether "room for three on some finite cover" is a theorem of the record, with a written proof and a lock.

## 6. Added 2026-10-04 afternoon: the chain read further, the Bianchi bridge, and the next arc (designed, not sealed)

Written while sm:B1538's Part F′ runs. Nothing here reads a twisted cohomology group at a new character: it is literature,
structure (`gc_structure.py`, record `gc_structure_run.txt`), or controls on banked data and on values the banked rows already
fix (`gc_own_chars_controls.py`, record `gc_own_chars_controls_run.txt`).

**(a) The chain of §3, read further.**
- **Item 1 (the surfaces exist).** Reid, Proc. Edinburgh Math. Soc. 34 (1991) 77–88, as stated and cited by Jaipong,
  "Totally geodesic surfaces with arbitrarily many compressions", arXiv:1008.1296 (read 2026-10-04): the figure-eight
  complement contains infinitely many commensurability classes of closed immersed totally geodesic surfaces.
  - Jaipong makes them explicit. Γ₈ = ⟨(1 1; 0 1), (1 0; −ω 1)⟩ has index 12 in PSL(2, O₃).
  - Γ_D = Stab_{Γ₈}(C_D), for C_D a circle about 0 indexed by D ∈ ℤ⁺, has finite co-area. For D ≡ 2 mod 3 it is cocompact,
    and S_D = P_D/Γ_D is a closed (acylindrical) totally geodesic surface in m004.
  - Reid's paper and Maclachlan–Reid ch. 9 themselves are not yet read.
- **Item 3 (independence).** Monroe, arXiv:2604.22004, Theorem 1.3, citing Johnson–Millson (1987):
  > "Suppose a manifold M = Γ∖ℍⁿ contains r disjoint embedded two-sided connected totally geodesic hypersurfaces
  > M₁, M₂, …, M_r. Then we have that the dimension of deformations into G is at least r."
  - For closed surfaces in a cusped manifold the bending cocycles miss the cusps, so they are interior classes of the four:
    n(ρ) ≥ r. Monroe identifies PH¹ with the cuspidal part (Kapovich).
  - His Corollary 1.5.1 uses the implication contrapositively: the Borromean rings have H¹ = 3 and PH¹ = 0, so they contain
    no closed embedded totally geodesic surface.
  - Branched bending along cusped faces (his Theorem 1.1; Bart–Scannell for n = 3) gives non-cuspidal classes only.
- **Item 4 (n(1) ≥ 2)** stays OPEN as a written proof. (c) below gives a computable route.

**(b) The Bianchi bridge** (`gc_structure.py`, Part 1).
- Every trace of m004 (23 minimal polynomials) and m003 (21) over the words of length ≤ 4 is an algebraic integer of ℚ(√−3).
  The discriminants are −3 times squares.
- So both groups have trace field = invariant trace field = ℚ(√−3) with integral traces, and are derived from M₂(ℚ(√−3))
  (Maclachlan–Reid ch. 8). ℚ(√−3) has class number 1, so each lies in PSL(2, O₃) up to conjugacy, of index 12
  (vol PSL(2, O₃)∖ℍ³ = 0.16916 = 2.02988/12).
- **Consequence.** For an ideal 𝔫 of O₃, Γ ∩ Γ₀(𝔫) gives an explicit cover of either golden state, and interior classes
  pull back injectively:
  - n(1) ≥ dim H¹_cusp(Γ₀(𝔫); ℂ), the weight-2 Bianchi cusp forms;
  - n(ρ) ≥ dim H¹_cusp(Γ₀(𝔫); E₁,₁), the weight-3 ones, since ρ = h ⊗ h̄ = E₁,₁.
- **What the tables say.** LMFDB (read 2026-10-04) lists no weight-2 Bianchi newform over ℚ(√−3) of level norm below 73
  (73.1-a, 73.2-a, then 75.1-a). Rahm's dimension tables, which would give weight 3, are offline (HTTP 404).
- Whether sm:B1536's small covers, with interior classes from degree 5, are congruence covers is not decided here.

**(c) The cyclic covers of the room covers: the next arc's question.**
- **Lemma A.** For an own character ε of order k of a cover N, the cyclic cover N_ε has, for E = 1 or ρ,
  n_{N_ε}(E) = Σ_{j mod k} n_N(E ⊗ εʲ).
  - Proof: Shapiro and Mackey, with ℂ[μ_k] in place of sm:B1536's permutation module. The interior parts split.
- **Lemma B.** For E real (the line, the four), n_N(E ⊗ ε̄) = n_N(E ⊗ ε).
  - Proof: complex conjugation is an isomorphism of cochain complexes that commutes with restriction to the cusps.
- **Corollary.** One own character of order ≥ 3 with n_N(ε) ≥ 1 and n_N(ρ ⊗ ε) ≥ 1 adds at least 2 to both supplies. On
  m003's d5.2 or d5.3, which have (n(1), n(ρ)) = (1, 1), it gives room for three on a cover of degree 15.
- **H₁ of the 28 covers** of degree ≤ 12 with n(1) ≥ 1 and n(ρ) ≥ 1 (`gc_structure.py`, Part 2; b₁ = #cusps + n(1) on
  all 28):
  - d5.2, d5.3: ℤ³;
  - m004's d10.3, d10.24: ℤ⁴;
  - m003's degree-10 covers: ℤ⁴, ℤ⁵ or ℤ³ ⊕ ℤ/2.
- **Controls** (`gc_own_chars_controls.py`), all holding:
  - **K1:** route R′ (route_r on the cover's own modules) reproduces sm:B1536's banked supplies at 36 pulled-back
    characters. The abelianisation recovers each one.
  - **K2:** the 14 order-2 own characters of d5.2 and d5.3. Each double cover N_ε is identified with a banked degree-10
    cover, and three readings agree: route N on N_ε, the banked row, and route R′'s sums.
  - **K3:** route P′ (sm:B1538's punct_present on a shim of the cover; python-flint) agrees with route R′ at 52 readings.
- **What the banked rows already fix.**
  - On d5.2 and d5.3, every order-2 own character has n(ε) = 0.
  - Four of seven on each have n(ρ ⊗ ε) = 1. Their double covers are d10.4, d10.13, d10.9, d10.14 and d10.18, d10.36,
    d10.24, d10.38: eight of the sixteen room-two covers.
  - So at order 2 only the four grows. Room for three needs the line to grow at an own character of order ≥ 3 where the four
    grows too. **Not read: any own character of order ≥ 3.** It is sealed first.

**(d) A check of sm:B1536's banked negative (it holds).**
- Its class counts include (1, −1) ×52 and (2, −2) ×12 + 4. With one sign flipped those would be generations, so the
  dictionary was re-derived.
- E₈ ⊃ SU(5) × SU(5)′ gives 248 ⊃ (10, 5) + (5̄, 10) + (10̄, 5̄) + (5, 10̄), as in sm:B1509 §1. N(10′) and N(5̄′) carry
  the same sign in every convention, so a generation needs I(W₁) = I(Λ²W₁) (sm:B1509: "that holds in both conventions").
- The SU(5) cubic anomaly confirms it: (−3, −3) cancels (3 − 3 = 0), while (2, −2) gives −2 − 2 = −4. So (k, −k) is
  anomalous, not k generations.
- sm:B1535's Theorem C (i) also forces I(Λ²W₁) ≤ 0 at every class.

**(e) The next arc.** Draft: `NEXT_ARC_DRAFT_the_room_above_the_room.md`; instruments `gc_own_chars.py`. It is sealed after
sm:B1538 banks, before any own character of order ≥ 3 is read.

## Reproduce

- `python3 docs/dossiers/golden_covers_2026-10-04/gc_icosian.py` prints `gc_icosian_run.txt` (group theory only). It
  imports sm:B1538's `punct_covers` (the states) and sm:B1530's `exact_states` (the Eisenstein holonomy) by path.
- `gc_binary_polyhedral.py` prints `gc_binary_polyhedral_run.txt` (group theory only; the states by path).
- `gc_fibonacci.py` prints `gc_fibonacci_run.txt` (SnapPy; a published theorem and a banked control).
- `gc_structure.py` prints `gc_structure_run.txt` (§6 (b), (c): traces and H₁; structure only).
- `gc_own_chars_controls.py` prints `gc_own_chars_controls_run.txt` (§6 (c): the next arc's controls on banked data;
  `gc_own_chars.py` is the draft library, loading sm:B1536's route_r, route_n, population and sm:B1538's
  punct_present by path).
- `gc_draft_population.py` prints `gc_draft_population_run.txt` (§6 (e): the next arc's population as structure — 30 covers,
  72,816 own characters, 35,890 cyclic subgroups). `gc_draft_run.py` and `gc_draft_read_out.py` are the drafts of its run
  and read-out; not sealed and not run.

## Seen first (the repo sweep and the literature)

- **The repo sweep.** `git fetch --all`, then `scripts/checks/prior_work.py` over every head.
  - Present, and read for this note:
    - "icosian" (116 files; B1270, B206; THEOREM_REGISTRY's T-ONE-ELEMENT-TWO-FACES: an order-3 icosian unit);
    - "binary tetrahedral" (B1353, B1357);
    - "definite quaternion" (B1271, B1507);
    - "Johnson–Millson" (sm:B1515, sm:B1523, sm:B1530);
    - "totally geodesic surface" (sm:B1535, sm:B1536, B1505).
  - Absent everywhere: "Chevalley–Weil", "Heisenberg cover", "arithmetic quotients of the mapping class group", "LERF",
    "subgroup separab", "virtually special", "room for three".
- **The literature**, read 2026-10-04:
  - Putman–Wieland (JLMS 2013, App. A: the Q₈ cover only; no binary polyhedral groups);
  - Grunewald–Larsen–Lubotzky–Malestein (arXiv 1307.2593, abstract);
  - DeBlois (AGT 2006, introduction);
  - Scannell (PJM 2000, in full);
  - Jung–Reid (arXiv 2003.05427, abstract);
  - Monroe (arXiv 2604.22004, abstract);
  - the Encyclopedia of Mathematics on Fibonacci manifolds.
- Pointers not yet read:
  - Grunewald–Lubotzky (GAFA 2009; Gaschütz);
  - McMullen (Math. Ann. 2013);
  - Biswas–Gupta–Mj–Whang (finite orbits; binary polyhedral groups);
  - Masters (virtual Betti numbers of genus-2 bundles);
  - Long 1987; Maclachlan–Reid;
  - Helling–Kim–Mennicke and Mednykh–Vesnin (as cited by Scannell);
  - Hadari, Koberda, Looijenga 1997 (Prym representations), Koberda–Santharoubane, Malestein–Putman;
  - Dubrovin–Mazzocco through the character-variety finite-orbit literature.

**0 of 19 stays 0.**
