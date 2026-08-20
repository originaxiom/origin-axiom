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

## Observer-coupling / physics-of-the-object glosses (added Review 26; source R25-4)
- **the incompleteness / the closing**: the object presents an AMBIGUITY or
  gap it does not itself resolve (no chirality, no real anchor, no time, no
  scale, no value); the observer supplies a CLOSING (a choice that resolves
  it). Reality = the observer's closings of the object's incompletenesses
  (B713–B719). The object supplies boundaries; the observer supplies specifics.
- **c-as-swap**: the observer's conjugation c (complex conjugation / orientation
  / time reversal) acts as a SWAP that exchanges the object's two chiral copies
  everywhere (two saddles σ₁↔σ₂, ρ_geom↔ρ̄_geom, τ↔τ̄). The object is
  swap-symmetric; the observer breaks the symmetry by CHOOSING a side. The
  Tomita–Takesaki modular conjugation J realizes it (B713/S070/B723).
- **the child**: a Dehn filling of the cusp of the object (m004) along a slope
  ∈ ℚ∪{∞} → a closed child 3-manifold. SPACE is the observer's choice of slope;
  the being washes out (4₁(5,1)≅5₂(5,1); a non-arithmetic being gives the
  identical child) — reality's structure is the observer's (B716+child/B718).
- **being-only**: a computation that consumes ONLY the object's trace field
  ℚ(√−3) (the "being"), not m004's finer Bianchi/holonomy/cusp arithmetic. The
  field-scoped observer (B723) is being-only; the OBJECT-level observer (m004's
  PSL(2,O₃)) is the next door (cc2's load-bearing catch).
- **native gauge = complex Chern–Simons**: the object's own gauge dynamics is
  SL(2,ℂ) complex Chern–Simons (the 3d–3d correspondence), NOT Yang–Mills;
  T[4₁] is abelian U(1) (B262/B715), no nonabelian gauge on the object.
- **multiplicity = the covering degree**: "how many units" (the trillions, the
  size) is an IMPORTED SCALE = the covering degree, not an object number
  (vol(cover)=deg·base; Mostow fixes shape not size). The count is the
  observer's (B719).
- **the Born ledger**: the arithmetic stratification of the Born rule on the
  object (B725–B729): FORM (\|·\|² conjugation-norm) = being ℚ(√−3) and WEIGHTS
  (non-uniform, 1:φ²) = hearing ℚ(√5) are the object's two QUADRATIC fields (the
  CLASSICAL content); AMPLITUDES ℚ(√(2+φ)) + PHASE ℚ(ζ₅) + associator ℚ(√φ) are
  QUARTIC golden-MTC OVERLAYS (the quantum content), ramified away from the
  object's prime 3. The object supplies the probabilities, not the amplitudes.
- **the First/Second Measurement Theorems (FMT/SMT)**: FMT (P69) — the object's
  2T-superselection charges stratify e₆; three Galois-conjugate first breakings
  (the cubic μ, constant 13³); z = so(10)⊕u(1). SMT — a second measurement of the
  object's own charges lands on su(3)⊕su(2)⊕u(1)³ exactly, skipping SU(5); its
  wall is complex in the split frame and REAL exactly in e₆(2) (B907, sealed).
- **the magic-square identification**: the build IS M(𝕆,ℂ) by explicit
  structure-constants isomorphism (P70; 0/3003 mismatches). The SELECTION of this
  cell by the object's arithmetic is ours; the square itself is classical.
- **the flavor atoms / the pencils**: the 27's intrinsic 15-atom basis (six 3-dim
  colored, nine 1-dim colorless — joint eigenlines of the RATIONAL commuting
  charge family); the colorless 3×3 grid's rows/columns = the even/odd
  transversals of a determinant — whence **I = −1 = the Leibniz sign** (exact).
- **the compact pencil / κ**: the compact charges' wall cubic (constant −19³,
  resolvent √77, field K); its Kummer class EQUALS the charge class (B910's
  One-Class theorem); the numerator law 13⁶/19⁶ per pencil.
- **the canonical gauge / unimodularity**: the basis in which the exact atom
  lines, the primitive ±1 cubic, and the integer H₊ live together; there the
  colorless coupling constant is EXACTLY 1 (B917) — couplings = geometric means
  of H-norms. Cross-observer constants (λ = 2304/953, T = σ₂(t_K)) measure
  basis-relations, not the object (the bridge constant: B916).
- **the value ladder / THE CROSSING**: R1–R4 (norm → scales → table → the sealed
  one-input comparison). The crossing (B915): α_em in, the desert curve out —
  MISS at 16σ; kills "boundary + desert" only; the failure triangle
  (10¹³/10¹⁴/10¹⁶·⁵ GeV, α_s-dominated) is the banked input to R4b (the object's
  D-chain as the desert's replacement, zero free parameters).
- **the One-Class theorem**: all four matter/value cubics (μ, generic, κ, HIER)
  share ONE Kummer class C in F*/(F*)³ (F = ℚ(√77, √−3)), the vacuum its inverse
  (B910 → B918). The compact wall carries the charge orientation; vacuum ⊕ anything
  = split.
- **the observer's place**: the unique degree-one place of K above a split value
  prime. The observer's-place theorem (B918): den(V) = 𝔭₁(953)⁴ exactly — the
  hierarchy's pole lives entirely there; prime-role trichotomy 953-pole /
  421493-trace-zero / 1129-e₂-zero; structure primes decorate numerators, the
  value prime digs the denominator.
- **"measurement" — THE RECONCILING CLAUSE (cc3 audit A3, 2026-08-05)**: the programme
  currently holds TWO formalisms sharing the word: (i) measurement = fiber functor /
  Galois torsor (B700 line; §D of LAW_MAP); (ii) measurement = centralizer of a
  superselection charge (the FMT/SMT line; §F). They are DECLARED DISTINCT NOTIONS
  pending the deciding computation (B787's ι-status question, now re-registered as a
  lead per the audit); no banked result identifies them; any text using the bare word
  should say which. The conjecture that they coincide is open, not assumed.
- **the value-invisibility theorem (B936)**: the sixteen invariant Hermitian
  structures form a torsor Z¹(⟨τ⟩, T_ad[2]) with classes H¹ = (ℤ/2)², and D₂ —
  the hierarchy's carrier — is a COBOUNDARY; **but no value (953, 2304, the
  norms) appears in any invariant of the pair**: the twist-norm law is diagonal,
  frame-relative data. K020's "form, not values" sharpened one level: the object
  does not force the values even cohomologically.
- **the hemisphere check (review protocol item 9)**: every prereg types its
  consumed structures by owning hemisphere (measurement-side vs matter-side);
  an unlicensed cross-hemisphere graft may not seal. Born from B926's autopsy of
  the two dead crossings, which were both such grafts.
- **the three crossings**: B915 (boundary + desert — MISS 16σ), B925 (the object's
  own D-chain as the desert's replacement — OUTCOME B, by the chain's own
  algebra: provably not Pati–Salam), B929 (the twist's shape sheet vs measured
  mixing shape — HIT-SHAPE: mixing-shaped, magnitudes off 5–9×, banked as a
  fenced hint). M0 — the programme as mathematics — is the standing default.

## Added 2026-08-10 (B1013) — two live terminology collisions, named before they cost an arc

- **"conductor" names TWO quantities** (found by B1002 when a check looked open that was banked):
  the **cusp order's conductor** (B675's quantization-index law: golden 4, silver 2) and the
  **word's own conductor / shadow modulus** (B666/B997: m²+4 — golden 5, silver 8). Any sentence
  using "conductor" must say which.
- **"level" now names TWO quantities** (hazard registered by B1012 from the branch): the
  **congruence level** of the Bianchi group (the (4)/(8) doors; the branch line *"the level IS the
  cusp conductor"* is about THIS one) and the **Chern–Simons level k** (Gukov's quantized coupling
  — the one the object is **provably blind to**, ∂S/∂k = −CS = 0). These live in different
  theories; an identification between them would be a **category claim needing its own arc**, and
  no such arc exists.
- **"the value-kernel"** (B1029): the kernel of the frame group's action on the banked coupling
  VALUES — computed to be exactly θ = c∘r (reversal-and-contragredient), because reversal acts on
  values identically to conjugation (SU(2) traces real; unitary characters conjugate under
  inverse). Distinct from θ's rep-level action, which is nontrivial; the scope is the sealed
  inventory (unitary characters × SU(2) traces). "θ-odd value data" is a contradiction in terms
  at this level.
- **"the trit"** (B1025 retype, B1030 verified): the VEV acceptance's residual discrete content —
  one ℤ/3 label choosing which of the 27's three 9-blocks (equivalently which surviving SU(3);
  the two namings are one act via the singlet-bijection) receives the closing. Orbit order
  exactly 3 under triality; log₂3 = 1.585 bits; a finite label, not a modulus. Substrate: B897's
  banked 9-blocks.
- **"the freedom ledger" / "COMPRESSION" / "THE ADDRESS"** (B1028): the retroactive
  look-elsewhere audit of the whole chain. COMPRESSION = structure-bits-out (against declared
  ambient classes) exceed retroactive designer-bits-in; THE ADDRESS = the opposite, with the
  concentrated links named (the campaign's stop-rule trigger). "Retroactive freedom" is distinct
  from "declared inputs" (hypotheses, published and typed): conflating them is a category error
  the ledger prices anyway, in the open.
- **"θ-even" names TWO banked objects** (collision found 2026-08-11 via the audit seat's
  tone-set error and this seat's verification of it, B1032): (1) the **F₄ exponent set
  {1, 5, 7, 11}** — a Lie parity label (B352/B569/B576/B583/B585); (2) **B1011 C6's mirror
  VALUE set** {0, ±¼, ±1/(4φ), ±½, ±1/(2φ), ±φ/4, ±φ/2, ±1} — named "the θ-even value set"
  in its own banked FINDINGS. Any sentence using "θ-even" must say which. Same class as
  two conductors, two levels, three σ's.
- **The value-set registry (B1032)** — four distinct banked menus, never to be conflated in
  pricing: **tones (5)** = |χ_{V₂(2I)}|/2, census 30/24/40/24/2; **mirror (8 magnitudes)** =
  the 2T⊗2I tensor character menu; **the listener family (3)** = (1∓1/√5)/2 and 1 — a
  character-RING element, not a bare character value (the B1032 amendment); **the phases**
  = a ℤ/3 finite label. A nomination prices against the menu it names, with that menu's own
  base rate. Grep lesson attached: search both φ and phi — the corpus writes both.
- **"σ" names THREE quantities** (the collision completed at B1034, after the window
  handoff's two and B945's third): (1) the **gravitational level** σ = ℓ/4G — continuous,
  unquantized, the object SIGHTED in it (∂S/∂σ = −Vol; B1012); (2) the **stage usage** —
  the candidate pin σ = 1 of c = 6σ against c((E₆)₁) = 6 (L154's question; UNDECIDED at
  B1034: unobstructed, unexhibited, the bridge named); (3) **B945's σ = the R↔L swap**
  (fiber orientation flip = chirality) — a discrete ℤ/2 closing bit, an item of the
  price. Any sentence saying only "σ" has not stated its subject (the D-iv clause,
  binding).
- **"π/6" names TWO objects of OPPOSITE TYPE** (adjudicated by the audit seat's item 2,
  verified): (1) **arg κ = ∓π/6** — the meridian-commutator trace's phase at u = ω, a
  conjugation-invariant TRACE (no basis freedom exists; Test-1 clean by construction),
  the MATTER FACE's carrier (B285→B303, B1010), with |κ − 2| = 1 the unit obstruction;
  (2) **arg Y[134] = π/6** — a cubic slot in a chosen H¹ basis, **proved pipeline GAUGE**
  (B647 c3; the invariant carrier is cross-ratio = 1). Both sit at ±π/6 because that is
  where √3-type elements of ℚ(√−3) live — the field's geometry, not a shared mechanism.
  One symbol, one content-carrier, one convention: say which.
- **ONE no-canonicity theorem, FOUR vocabularies** (the Field Ladder's FL-2, verified
  2026-08-12): *no canonical basepoint* (B701 = B700 phase 2 — a dir-less arc, cite it
  so), *no equivariant section* (B782), *no canonical origin* (B704), *no canonical
  ℤ/2 representative* (B942) — the same theorem; searches must run all four phrasings.
  **B58 is DE-LINKED** — its "non-canonical" is a pinv/numerics artifact, unrelated.
  **Precision (the audit seat's Task B §3, textbook-verified):** H¹(F, G) is a POINTED
  SET — its base point is the trivial torsor's class. "No canonical point" is true of
  the (non-trivial) TORSOR, never of its classifying set. S069's "I am a vector space
  with no origin" blurs the same line: a vector space HAS an origin (0); the seam's
  choice-space is the AFFINE object — the torsor. The level at which no-canonicity
  holds is the torsor, one level below where loose restatements put it (the B957
  "one level too high" species, again).

- **Bare arc IDs B1025–B1044 name TWO arcs each; B1045–B1059 are RESERVED on main**
  (2026-08-12, the cloud fork collision — `docs/CLOUD_ALIAS_TABLE.md` is the
  permanent resolver): the cloud consolidation branch forked at B1024's seal and
  numbered independently. Cloud arcs are cited **qB1025…qB1053**, cloud leads
  **qL155…qL166**; main's next arc is **B1060**, next lead **L161**. Any bare
  ID in the colliding range written before 2026-08-12 needs the table. Species:
  the dir-less-arc/two-Task-B retrieval hazard at series scale — now with its
  resolver banked.

- **"c" (central charge) names FOUR referents near the gravity lane** (the row sealed in
  advance of G1's prereg, the D-iv precedent, 2026-08-13): (1) **the Sugawara/level-1
  charge c((E₆)₁) = 6** — Level-3 chiral arithmetic, banked exact via the conformal
  embedding (E₆)₁ ⊃ SU(3)₂×(G₂)₁ with c: 16/5 + 14/5 = 6 (B254); (2) **c_BH = 6σ** —
  the Brown–Henneaux charge of the gravitational dictionary, c = 3ℓ/2G with G = ℓ/4σ
  (B1012; its σ is the D-iv row's referent 1, continuous and unquantized); (3) **the
  cusp-torus theory's c** — G1's object: whatever charge the boundary-torus theory of
  the banked complex CS carries. NOT banked equal to (1) or (2) — m004 is cusped, the
  cusp torus is not a conformal boundary, and the B980 fence holds: equating cusp-c
  with c_BH POSITS k_anyon = k_gravity; (4) **B559's c = 1 chain** — banked only as
  "a candidate holographic *boundary*" (B559), a fourth candidate never identified
  with the others. Numerical agreement among referents is not identification — the
  licensing gap between (3) and (2) is exactly what G1 measures. Any sentence saying
  only "c" near the gravity lane has not stated its subject (binding, as the σ clause).

- **"trace field" names TWO objects for the metallic family** (found 2026-08-13 at
  B1062's ingredient check; load-bearing for the Maclachlan–Reid test): (1) **the
  fiber/eigenvalue field ℚ(√(m²+4))** — the monodromy eigenvalue's field (B148:
  m=1 → ℚ(√5) golden, m=2 → ℚ(√2), m=3 → ℚ(√13)); (2) **the Kleinian trace field**
  — the field generated by the holonomy traces of the 3-manifold group (m=1/m004:
  **ℚ(√−3)**, the Eisenstein field, banked corpus-wide). Same member, two fields,
  different mathematics: arithmeticity criteria (Hao Thm 2.3) run on (2), never
  (1). Any sentence saying "the trace field of member m" without the qualifier has
  not stated its subject.

- **"P" (the record swap) names TWO roles** (found at the digest's row 1.03 port,
  2026-08-14; no document separated them before): (1) **the conjugating element** —
  A7's based-level bit (B979: where φ enters, LR vs RL); (2) **the substrate
  operation** — B16's exchange-symmetry axiom (class-level; outside A1–A6; load-bearing
  for the trace-map surface, counted in COMPUTE_THE_PROGRAM §1's addendum, NOT in
  THE_CLAIM whose chain never consumes it). Any sentence using "the swap" says which
  role. The two-referent pattern's newest member.


## "K" (the letter) — FOUR live referents; unqualified "K" means the charge field (ruled 2026-08-18, the W6 consolidation catch)

**Unqualified `K` in any corpus document = the charge field ℚ[t]/μ ≅ ℚ[x]/(x³−12x−5)**
(the S₃ CUBIC, disc 6237 = 3⁴·7·11, resolvent ℚ(√77)). Every other field the letter has
locally named must be written by its radical: **ℚ(√−3)** (the being field — number-theory
convention's "K" in B1067's ray-class sections), **ℚ(√5)** (the hearing field — B1069's
biography sections use K = ℚ(√5) locally, flagged there), **ℚ(√−15)** (the seam). The
instance that forced this row: "K's class group OPEN" (B1067's headline) is about the
CHARGE field's 953-place — not about B1067's subject field ℚ(√−3), whose h = 1 is a
control row. Three documents carried the unlabeled ambiguity (CAMPAIGN_STATUS,
LISTENER_MAP_SPEC, the W6 draft) — labeled as of this rule.

**"conductor" (extension of the standing two-referent row):** the masterplan window added
two more live senses — the ray-class MODULUS (B1067/B1069's Cl_m) and the ORDER-conductor
f of ℤ+fφℤ / ℤ+fωℤ (B1069's tower; B675's cusp sense). Four senses now live: cusp-order
conductor · shadow modulus · ray-class modulus · order-conductor f. Every use names its
sense.

## Added at Review 47 (2026-08-20) — the B1083–B1101 closing-campaign window's terms

- **the origin torsor, typed correctly (the arrow-is-not-a-bit correction, B1083)** — amends
  `THE_FORCED_AND_THE_FREE.md` §0 (2026-08-19). The four natural Fibonacci substitution
  rules form one free transitive K₄-orbit under reversal-conjugation and swap-conjugation;
  the founding choice `a→ab, b→a` is a basepoint-taking on this torsor. The original typing
  ("reversal = time's arrow, swap = chirality") is **corrected**: all four orbit points are
  FORWARD substitutions (no K₄ element inverts the dynamics), so reversal is a **P-type**
  bit (parity, reading direction) and swap is the **C-type** bit (chirality) — but **the
  arrow is not on the torsor at all**. Its true home is the positive monoid's
  non-surjectivity (the word `bb` has no preimage under the substitution, verified
  exhaustively to length 8 — some configurations are initial-only): an intrinsic,
  **unspendable** structure, named **T** (the register's positivity). **The corrected
  ledger: two spendable bits (C, P) + one unspendable structure (T).** Composition fact
  (same arc): `det M = −1` is the tick's own signature (the Breath ℤ/2 pulse), not a
  torsor bit; `M² = [[2,1],[1,1]] = RL` exactly — the tick squares to the figure-eight
  monodromy — and the one-tick object is the non-orientable Gieseking manifold, so
  **orientability and amphichirality are bought together at tick two** (the object is "the
  double tick"). B1097 (re-deriving a second, independently-authored typing of the same
  first act) settles which physical loss is which bit by composing B1083 with B1095 (below):
  order-loss (the substitution's blindness to letter arrangement) = the P/hand bit;
  sign-loss (`det M = −1 → det M² = +1`, forced by orientability) = the orientability/Breath
  tick; **the arrow is neither** — never destroyed because never a bit, structural (T) at
  every level.

- **the two hands — SECOND, UNRELATED referent (collision flag, B1085)** — `TERMINOLOGY.md`
  already glosses **"the two hands"** (Added Review 26) as the being/hearing faces taken as
  a pair ("one hand cannot clap" = the generation no-go, B685). **B1085 introduces an
  unrelated second sense**: on the Fibonacci Hamiltonian at a half-line Dirichlet cut, the
  two hands are the two SIDES of one cut of the bi-infinite golden Sturmian word (the right
  half read forward, the left half read outward) — a 1D quasicrystal edge construction, with
  no arithmetic being/hearing content. **Any sentence using "the two hands" from B1085 forward
  must say which**; prefer "the cut's two hands" for this sense, matching the file's
  standing discipline for repeated words (cf. "σ," "K," "conductor," "θ-even").

- **reversal-closed window (B1095)** — a half-line cut window of size N (a Fibonacci number)
  at which the cut's two hands' (B1085) words are letter-for-letter reversals of one
  another. Occurs exactly at **even** Fibonacci index (verified N = F₁₆ = 987, F₁₈ = 2584);
  fails at **odd** index (N = F₁₇ = 1597, F₁₉ = 4181), where the reversal identity breaks at
  exactly the two cut-adjacent letters. Reversal-closure is the origin torsor's tick-parity
  (B1083's Breath ℤ/2, `det M = −1`) surfacing at the spectral level: an even number of
  ticks closes the palindrome around the cut, an odd number leaves it open.

- **the mirror-isospectral split (B1095)** — at a reversal-closed window the cut's two hands
  are **exactly isospectral**: the exchange matrix J conjugates one half-line Hamiltonian
  into the other (`J·H_R·J = H_L`), forcing spectral agreement to machine precision (max
  difference `1.3×10⁻¹⁵` over 2584 eigenvalues) — the hand is not merely IDS-blind, it is
  spectrally **invisible**. Yet the eleven shared boundary-capable energies localize
  **complementarily**: five bind to the right hand, six to the left (the ±1 a parity
  remainder of one shared odd-sized family — a family of odd size cannot split evenly).
  **The energies are P-invariant (forced); the localization is P-equivariant (free)** — the
  origin torsor's P-bit (B1083) physically realized as *which* shared state binds where.
  Corrects B1085's own headline ("edge-observable, and ONLY edge-observable") and B1091's
  observer-card row to this precise form; both stand corrected in place, citing B1095.

- **THE LOCATION THEOREM (the four-language wall; B1083/B1084/B1086/B1087)** — the theorem that no CLOSED
  assembly of the object (a twisted double, a compactified 3-manifold) can be **chiral in
  matter counts**, proved independently in four registers shown to be one fact: **PD-pairing**
  (topology — Poincaré duality forces `h¹(D;27) = h¹(D;27̄)` in every twisted-double cell,
  B1086, the spectrum law); **AW non-isolation** (M-theory/G₂ — on the object's flat G₂
  cone every ADE-enhancement collision is non-isolated, so localized matter is vector-like,
  B1084); **the completion-kernel** (the substitution rule — the arrow a completed/closed
  register discards is exactly the structure a cut restores, B1083); **charge/holonomy
  non-commutativity** (representation theory — the Acharya–Witten U(1) charge operator
  exists on the θ-odd dial, spectrum 1-8-9-8-1, but fails to commute with the cusp
  holonomies on any closed object — not merely unbalanced but **undefinable**, B1087).
  Chirality becomes measurable exactly where the object is **not** closed: at a cut (the
  edge, B1085/B1095) or an isolated transversal point (the hatch, B1084/B1098). Fence
  carried verbatim at every landing: **chirality-at-count is NOT claimed** even where the
  matter content is representation-level complex (B1100).

- **the trinification remnant (B1098)** — the unbroken gauge algebra left when the object's
  own Zariski-dense hyperbolic holonomy ρ: π₁(M) → SL(2,ℂ) is composed with the A2-class
  sl₂-embedding into e₆ (the principal sl₂ of one su(3) factor of the trinification
  `e₆ ⊃ su(3)³`): exactly **su(3) ⊕ su(3)**, dimension 16 = 8+8, rank **exactly 4** — color
  in one factor, su(2)×u(1) inside the other, zero extra u(1)s. Named for the mechanism: the
  object's own geometry, taken through its smallest faithful representation, "eats" exactly
  one of trinification's three su(3) factors. See "the hatch / the landing."

- **the hatch / the landing (B1098 / B1100)** — two stages of one construction on THE RANK
  WALL's single live hatch (non-abelian holonomy, B1094). **The hatch**: the stratum of
  sl₂-embeddings φ: SL(2) → E₆ (twenty conjugacy classes, exhaustively enumerated,
  Bala–Carter-saturated) composed with the object's own holonomy; "the hatch opens" =
  the A2 class's centralizer is the trinification remnant, rank exactly 4, matching the SM
  (B1098; a secondary A1 landing gives su(6), SM plus one extra u(1); seventeen classes fall
  below rank 4; the nearby 2A1 candidate is excluded). **The landing**: the matter content
  AT that stratum — the 27's branching under the A2-class sl₂ plus the surviving rank-4
  Cartan, computed exactly (the trinification triplets+singlets tiling the 27), with the
  headline that **the 27 is complex at the landing, witnessed** (a basis-free asymmetry: a
  multiplicity-3 weight class whose negation class has multiplicity 0) — falsifying B959's
  "every route to rank 4 makes the 27 real" **beyond that theorem's own toral/finite-image
  scope** (B959's sealed text stands untouched on its own ground; the correction lands as an
  addendum beside it, never an edit to it) (B1100). Both the class choice (1-of-20, ≈4.3
  bits) and the exact hypercharge value-match are **priced choices, stated as open
  residuals**, never silently treated as forced or as done.

- **the collapse-form vs bijective-form hypercharge test (B1100 §3)** — two ways a candidate
  direction in a landing's surviving Cartan could reproduce the banked hypercharge
  assignment. **Bijective form**: every one of the landing's fifteen exact weight classes
  maps one-to-one onto the banked 6Y multiset's eight value classes — tested and
  **EXCLUDED, exact** (no direction achieves it). **Collapse form**: the direction
  reproduces only the banked target's DEGENERACY PATTERN (sizes 6,6,4,3,3,2,2,1, several
  weight classes sharing one hypercharge value) — **ESTABLISHED at float grade, and shown
  GENERIC** (the first randomly-tried direction already hits the pattern: the compatible
  cone is open in the rank-4 Cartan, not a tuned point). The exact value-match (solving the
  collapse assignment's four unknowns over the cubic-irrational Cartan coordinates and
  verifying all 27 exactly) is the **named residual** — heavier because the raw coordinates
  are cubic irrationalities, not silently dropped. Until it lands, the test's verdict is
  **compatibility**, not identification.

- **the certification envelope (WORKING_RULES §CE; B1101, 2026-08-20, owner-elected)** — the
  binding procedure for any certifying suite run: the working tree is **read-only by
  convention** — (1) landings stage in the scratchpad and land by explicit filename at bank
  time, never a glob, never a new arc dir mid-suite; (2) pre-commit gate checks run on the
  STAGED state; (3) every ledger digest enters by command substitution, with the
  `seal-digests` gate as the read-time backstop recomputing every digest at gate time
  (latest-row-per-path; corrections-by-append supersede); (4) on collision (the tree moved
  mid-suite): **fold-forward** — bank the pending cells plus the head's currency reads in
  ONE commit, one suite, never re-run a stale certificate. Adopted pre-proven: three
  same-window instances of one species (E46, tree-freeze during certification) were all
  caught by the pre-existing exact-tree gate (E39) while the surrounding procedures failed
  under load; filed alongside E45 (schema-from-memory) and E47/E48 (hash-transcription and
  remap-time digest hazards).

- **differential-first preregistration (L173, 2026-08-20; the audit seat's warning +
  B1095's computation, adopted verbatim)** — a discipline now binding on L173's
  laboratory-prediction spec and generalizable to any object-vs-standard-theory comparison:
  before comparing a candidate measurement (e.g. a photonic/polariton Fibonacci-chain edge
  scan against B1085's ρ-sweep) to the object's prediction, the prereg's **first paragraph**
  must state what the STANDARD theory already forces for the same configuration (here: gap
  labeling + bulk–boundary correspondence) and name exactly where the object's prediction
  **differs** from that standard content. Guards against re-litigating a B724-shaped
  defusal — a prediction that is real but not distinctive, because a generic mechanism
  already produces it; per B1095, the correctly-stated differential for L173 is the
  cross-hand mirror-isospectral split, not the raw edge counts (which are conceded standard
  pumping content, in kind).

- **registerable / registerability (B861/B863/B994 — pre-existing term, glossed late; flagged
  at this window's merge)** — a breaking step (and by extension an algebra reached by one) is
  *registerable* iff the 27's generation structure survives it — *"registerable = the
  generation stays chiral"* (`docs/LAW_MAP.md`, B994 row). The cascade's TERMINATION THEOREM
  (B863) states the SM is the **terminal registerable algebra**; B994 proves the ENDPOINT is
  registerability-forced (all six registerable-respecting selection functions land on the SM)
  while the PATH is not — registerability is the **derived** half of the cascade's selection
  principle (B860/B871), maximal-residual-symmetry the **assumed** half, selecting only the
  path. README's opening uses the term with this gloss inline.
