# TERMINOLOGY — the project's inner vocabulary, glossed (Review 18, 2026-07-15)

This project developed a working vocabulary across hundreds of AI-assisted
sessions. **These are INTERNAL WORKING NAMES, not established mathematical
terminology.** Every load-bearing statement behind a name below is banked as
ordinary mathematics in the referenced artifacts. If a term reads poetic,
that is what it is — the mathematics is in the definition column.

| Inner term | What it actually is |
|---|---|
| **the object** | The figure-eight knot complement 4₁ (once-punctured-torus bundle, monodromy [[2,1],[1,1]]), and by extension its character varieties and quantum invariants. |
| **bank / banked** | Committed to the repository with a passing lock (test) and ledger entries; the project's unit of "result". |
| **B-number (B598, …)** | A banked frontier arc, numbered sequentially; lives in `frontier/B*/FINDINGS.md`. |
| **seat / chat-N / cc2** | One AI assistant session among several run in parallel by the owner; seats cross-check each other (INTERNAL verification — see `PROVENANCE.md` §0). |
| **lock** | A pytest test that recomputes a banked fact (heavy ones gated behind `OA_SLOW=1`). |
| **gate** | A repo-wide consistency check (`scripts/gates/`), or, inside a script, a failure-enforcing assertion. |
| **prereg / sealed** | A preregistration document written and SHA-256-hashed before the outcome-bearing computation runs (`ARTIFACT_HASHES.txt`). |
| **firewall** | The governance rule separating mathematics from physics speculation: no Standard-Model quantity is claimed from the mathematics; speculative motivation lives quarantined in `speculations/`, `philosophy/`. |
| **the stage** | A finite quantum model attached to the object: theta functions / Weil representation at level κ, or an affine-Lie-algebra modular datum (e.g. SU(3)₂ ↔ "golden stage" κ=5; "E₆ level 2" = E₆₂). |
| **the fold / θ** | The order-2 outer automorphism (diagram fold) of E₆; "θ-even/odd" = its ±1 eigenspaces. f₄ is the fixed subalgebra. |
| **the dial** | The six peripheral-centralizer directions v_m (one per adjoint block V_m of e₆ under the principal sl₂, m ∈ {1,4,5,7,8,11}); "θ-odd slots" = m ∈ {4,8}. |
| **the weld / the double** | The figure-eight glued to its mirror along the cusp torus (the mirror-double), optionally with a twist exp(t·v_m) at the gluing ("bending", Johnson–Millson). |
| **hearing / deaf** | Whether a (twist-)deformed amplitude differs from the untwisted one at order ε²: "the hearing law" A^tw − A^plain = −2ε²(u†M_odd u) (B593); sectors where this vanishes identically are "deaf". |
| **the sign-flip theorem** | P_odd·C = −P_odd: conjugation flips the θ-odd block of the open weld matrix exactly (B592-OPEN). |
| **the clock** | The order of a monodromy image in a finite stage (e.g. ord(ρ(A₁))); "the clock is not the cat-map period" = B596's null. |
| **width / τ-labels** | Reidemeister-torsion magnitudes per block; used as non-degenerate labels ("width-respect" = a map must not permute them). |
| **the chain / readiness chain** | The 9-step audited checklist (B598) that had to be fully green before the sealed P3 comparison was allowed to run. |
| **arc / campaign** | A themed sequence of banked steps (e.g. "the L85 campaign" = the D1 existence question). |
| **L-numbers, K-numbers, P-numbers, PC-numbers, S-numbers** | Ledger indices: open leads (L), knowledge notes (K), proven claims in `CLAIMS.md` (P), paper candidates (PC), synthesis sessions (S). |
| **the universal boundary ratio** | I_λ/I_μ = −2√−3: the gauge-invariant content of the peripheral restriction, equal at all six blocks (B598 step 3). |
| **the hearing lines / the two integers** | The θ-odd bending responses: rank-2, supported on m ∈ {4,8}, column law N₄(1+√−3) / N₈(1−√−3) with N₄ = 2⁹·3²·5·7·13, N₈ = 2¹⁵·3⁵·5³·7²·11 (B598 step 4b). |
| **outcome A/B/D** | The locked verdict table of the sealed P3 prereg (existence / structure-with-recorded-defect / no map). L85 resolved as B. |
| **vacuity check (MB12)** | The rule that a preregistered test must be able to both pass and fail — applied to the target, the OPERATION, and the CRITERION (two sealing errors of exactly this kind are on record in B598, amended with hashed errata). |
| **verify-don't-trust** | Every cross-seat claim is recomputed in-sandbox before being banked, including claims marked "verified" by another seat. |

For how verification works and what it does NOT imply, read `PROVENANCE.md`
§0. For how to run the checks yourself, read `REPRODUCIBILITY.md`.

## The four mirror manifolds (permanent names; audit Gate 2, 2026-07-15)

No invariant may be transferred between these without an explicit map.

| name | construction | H₁ | notes |
|---|---|---|---|
| **M_Sol(−A₁)** | the closed torus bundle of the mirror-twisted lift −A₁ | ℤ ⊕ ℤ/5 | SOL geometry (B591-M5); the conductor carrier; the C-twisted quantum play (Z_C = +1/φ) |
| **L(5,2)** | the branched double cover Σ₂(4₁) | ℤ/5 | the classical mirror-pairing manifold (B591-M3) |
| **D_g(M)** | the cusp-complement double M ∪_g M̄ per explicit gluing g | g = ±I → ℤ; g = ±A₁ → 0 (homology sphere) | ±A₁ is peripherally INCOMPATIBLE with the banked 27 local system; the B605 D₄-intertwiner gluings are named D_g(M) with g stated |
| **D_bent(M; m)** | the representation-bent B582/B598 amalgam at bend m | — (local-system object) | h¹(D;27) = 2 at m = 4, 8; 5 at none/1/5/7/11 (B635-reproduced) |
| **D_conjθ(M)** | the conj∘θ-twisted double — **RE-SCOPED (cc2's 2026-07-16 withdrawal):** the h¹ = 3 count used an assumed λ-sign, superseded by B637 part 2a's exact D_φ computations (all four involution gluings: h¹ = 5); the "3" stands only for cc2's specific non-geometric line-identification, NOT for any manifold in the named gluing menu. B639 proved the honest realization is a FIBER-PAIRING (θ₂₇∘conj), still unconstructed (L92). | — | SURVIVING: the parity-typed slope criterion and the universal slope = the cusp modulus −2√−3 (all six blocks) |

## Added at Review 20 (2026-07-16) — the B629–B645 stretch's terms

- **the chord / the mirror-coupled double**: the closed 3-manifold obtained
  by gluing the figure-eight complement to its mirror along the cusp torus
  (a "weld"); "the chord's invariants" = cohomological invariants of that
  closed object (B637–B638). Internal name; the mathematics is an amalgam
  / Mayer–Vietoris computation over an explicit gluing.
- **the core law / 24ζ₆**: the banked exact identity Y[023] = 24ζ₆·Y[123]
  between components of the alternating cubic form on the double's twisted
  H¹ (B637; ζ₆ = e^{iπ/3}).
- **the swap σ***: the pullback action of the double's deck involution on
  twisted cocycles (antilinear; B638).
- **the flip τ***: the (attempted) action of the object's amphichiral
  symmetry on the double — proved NOT to act (B643).
- **the congruence shadow / "the conductor is the ear's modulus"**: the
  theorem that the θ-odd hearing representation factors through reduction
  mod 5 (B644); "shadow" = the image in SL(2,𝔽₅).
- **the 13-dial / the unit cross-ratio law**: exact identities of the
  normalization-free invariants of the Y-tensor across the nine computed
  doubles (B645).
- **the audit seat**: a read-only AI seat operating in a separate clone
  (historically phrased "the external audit" — see PROVENANCE.md §0;
  internal to the project like every seat).
- **the calibration campaign / the one-shot license**: the sealed B648
  protocol — exhaust the grammar (Phase A), count its freedoms (GATE B),
  spend at most ONE held-out comparison under pre-committed statistics
  (Phase C); the license is spent regardless of outcome (B648/B653).
- **the C′ event / zero-calibration**: the campaign branch in which range
  physicality fixed the single free bit with zero measurements (the
  Galois image −φ/2 ∉ [0,1]), making the prediction parameter-free
  (B653's design).
- **the grammar table / the freedom count N**: the sealed inventory of
  every constant in the object's interaction grammar, each labeled
  FORCED / CHOSEN / CONVENTION / COMPUTED-MECH-OPEN / WALL; N = the
  number of genuinely free entries (B652: N = 1, discrete).
- **the conductor-clock law**: clock(κ) = ord(A₁ mod 3κ) — the θ-odd
  block's dynamical order reads the conductor 3κ, not the naive modulus
  κ (B656/G4; B596's table thereby DERIVED).
- **the sign-hears-the-discriminant theorem**: det(w) = (−1)^{v_p(det
  B_w)} for every Weyl element w iff v_p(t²−4) is odd (even rank);
  even valuations give exactly the sign-balanced half (B656/G1).
- **the sector-carry law**: the even θ-sector carries a unit iff the
  mirror channel resonates — the direct and mirror generic laws are
  exact negatives (B656/G3).
- **the (i₁, i₂) reduction**: the dimension grammar {h⁰(M), h¹(M);
  h⁰(D), h¹(D)} is determined by i₁ = dim V^holonomy and i₂ =
  dim V^{peripheral ℤ²} (B656/G5); (1,3) ⇒ 3/5/1.
- **the invariant line**: the h⁰ line of the 27 — a 3-weight h_pr-null
  combination with coefficients (1, −1, 1); NOT the Spin(10) singlet
  (the W0a conflation refutation, B657).
- **the portal (law)**: cupping with the invariant line, P(u) = [v₀ × u]
  via the Jordan cross product — a rank-5 isomorphism H¹(D;27) →
  H¹(D;27̄) on both computed objects (B657).
- **the shadow-class law / the stage-universal character law**:
  |tr_odd(W)| = |χ_D(shadow(W))| — the hearing modulus of any word is
  the absolute character of the stage's shadow-irrep on the word's
  mod-conductor image (golden: |χ₂| of 2I mod 5; E₆ level 2: |χ₃| of
  PSL(2,7) mod 7) (B664/B665/B666).
- **the F4 skeleton**: stab_{e6}(v₀) ≅ f4; both metallic holonomies
  lie in one F₄ fixing the same Jordan unit direction; 27 = 1 ⊕ 26
  (B670).
- **the ceiling law**: the per-word supremum max_κ |Z_κ(w)| of the
  exactly-periodic level ladder — the survivor question of Track H's
  refutation (B669/B673; cc2's D4).
- **the generation sum rule**: [P₂₃] + (7983360/13)·ω·[P₃₄] = 0 with
  [P₂₄] independent — the exact rank-2 relation among the solo
  pairings, two-seat verified (B671/B673).
- **the graded sign rule**: in 27⊗27 the Λ²=351-valued cup classes
  are slot-symmetric and the Sym²-valued (351′/27̄) classes
  slot-antisymmetric — the Koszul parity flip (B666/A′ × cc2 D2).
- **H-EAR (the shadow-realization principle)**: the named hypothesis
  that the hearing stage realizes the object's shadow representation
  — L91's first remaining principle (B666/W32).
- **H-CUSP (the cusp-quantization principle)**: a stage can host the
  hearing only if the object's cusp lattice conformally quantizes the
  stage's weight lattice — proven as the A₂-vs-A₄ dichotomy; L91's
  second principle (B672).
- **the Rogers–Ramanujan recognition**: the weight-5 doublet streams
  are F·η-powers with component ratio R(q), the RR continued
  fraction (B672); the golden rotation: the monodromy's modular lift
  is order-10 elliptic with trace exactly φ (B674).
- **being face / hearing face**: the object's two arithmetic ends —
  being = the holonomy/geometry side (ℚ(√−3), Eisenstein, prime 3, 2T,
  E₆); hearing = the monodromy side (ℚ(√5), golden, prime 5, 2I, E₈).
  Named for the observer-coupling reading; the mathematics is the
  bifocal two-ended structure (B247–B261; EISENSTEIN_ATLAS).
- **the two hands**: the being and hearing faces taken as a pair;
  "one hand cannot clap" = the generation no-go (B685). The hands are
  asymmetric, not a mirror (B690/B691).
- **the totient root**: the arithmetic explanation of the being/hearing
  asymmetry — φ(3)=2 prime (minimal self-conjugate doublet) vs φ(5)=4
  composite (golden Gaussian periods t²+t−1) (B691).
- **the divided-power law**: v₅(den cₙ) = v₅(5ⁿn!) exactly for the
  target carrier (q;q)^{−3/5} — a 5-adic exponential; proved
  unconditional, transfers to (q;q)^{−a/p} for every prime p (B683).
- **Frobenius gluing**: the mechanism by which the golden enters — at
  the ζ₅ evaluation of the Habiro object, via gluing of series at a root
  of unity, nontrivial precisely because 5 is inert in ℚ(√−3) (does not
  divide the discriminant); a coupling phenomenon, not object content
  (B697).
- **conductor-15**: the figure-eight A-polynomial's elliptic model has
  conductor 15 = 3·5 (being prime × hearing prime), curve class 15a,
  j = −1/15, bifocal branch locus {φ²,φ⁻²}∪{ω,ω̄} (B674).
- **deaf = non-CM**: the continued-fraction "voice" of a metallic member
  is algebraic exactly at CM cusps and silent (deaf) at the non-CM one;
  bronze (Galois S₄, non-CM) has no algebraic value and no hosting stage
  (B675).
- **the seam**: the object↔observer boundary, made exact (B704) — the
  object canonically fixes an 𝔽₂-vector space V (the maximal multiquadratic
  Galois structure over the stage fields ℚ(√p*): stages = basis, meetings =
  𝔽₂-sums via genus theory) but NO canonical origin (B701); a measurement is
  a choice of point in V. "Where you end and I begin" = the object gives V,
  the observer picks the point (see [[speculations/S069]]).
- **measurement = fiber functor**: the fiber-functor program's thesis
  (B700/B701) — a measurement is a fiber-functor evaluation of the object
  through a stage; the ambiguity of the value is a Galois torsor (the two
  golden irreps of 2I, swapped by Gal(ℚ(√5)/ℚ)), stage-uniform over ℚ(√p*).
  Provably NON-canonical (B701): the object gives the torsor, never the point.
- **the audibility law**: a stage carries an audible metallic tone ⟺ its
  character/weld field ℚ(√p*) is REAL ⟺ p ≡ 1 mod 4 (B702 corrected/B705);
  golden p=5 hears φ, imaginary stages are silent. Types the seam's basis.
- **the Listening Protocol**: the standing methodology gate
  (`docs/LISTENING_PROTOCOL.md`) that makes the firewall CONSTRUCTIVE —
  compare STRUCTURE, never value; the rung hierarchy (1 field · 2 torsor/seam
  · 3 relation are the object speaking; 4 single-ratio needs a forcing
  mechanism, dead for values by B685; 5 fit = meaningless).
- **the structural comparator**: the rung-1 test — is a measured, convention-
  reduced ratio ALGEBRAIC of low degree over a predicted object field ℚ(√p*)
  (membership, base-rate-immune), surviving MORE digits than found it — vs
  the rung-4 "≈ a nice number" (proximity, base-rate-dead). B706 ran it.
- **rung-1 / rung-2**: positions in the Listening Protocol's comparison
  hierarchy — rung-1 = does a quantity live in the object's field?; rung-2 =
  does an external FREEDOM organize as the object's Galois torsor / the 𝔽₂
  seam? (B706 ran both on the SM flavor sector → NO-MATCH.)
