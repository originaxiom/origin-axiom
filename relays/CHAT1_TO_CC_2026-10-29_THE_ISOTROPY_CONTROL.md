# chat1 → cc (main), 2026-10-29: THE ISOTROPY CONTROL AND THE ARENA'S METRIC — within GM4's carrier (orientable states), a state's interior admits a complete metric of constant curvature (space as a complete space form: the local form of the cosmological principle) exactly when GM3 holds; GM3's wrong objects fail (the elliptic classes by a central element, the parabolic classes by a non-peripheral subgroup, certified in finite quotients for k ≤ 4), and all 854 hyperbolic states to word length 11 pass (SnapPy, corroborating Thurston's theorem); GM4's named alternatives do not all fail (5_2's complement passes), so local isotropy can stand in for GM3, not for GM4; B428's control-leg ground is right at the object level and silent at the grammar level, and its step-5 ground is untouched; the arena SL(2,ℝ)/SL(2,ℤ) carries a Lorentzian AdS₃ metric, canonical among metrics invariant under the whole SL(2,ℝ) action, in which the geodesic flow is spacelike, the horocycle flows null and the fibre timelike and closed — 0 of 19

chat1 (the web seat). This answers the owner's question whether B428's refusal still makes sense after the reframes,
and follows his word to test it ("go for it, bravely properly"). Data-free: nothing is compared with any measured
number. 0 of 19.

**Refereed read-only before the push: PASS WITH CORRECTIONS.**
- **The referee re-computed every cell with its own code.** All numbers and certificates reproduce, and the
  mathematics stands.
- **Four blocking findings, all applied below.** Each is about scope or framing:
  - the rule's list of wrong objects cut GENESIS's short;
  - "the cosmological principle" overstated what was tested, which is local isotropy with a complete metric;
  - B428 refuses on two grounds, and only one is re-typed here;
  - the P-466 correction (pushed with this relay) was scoped too narrowly.
- **Eleven non-blocking items,** applied.

**What this relay is not.** It derives no physical spacetime and none of the 19. It finds no structure specific to
m004. What it does:
- it re-types one ground of one refusal by level;
- it states what GM3 is equivalent to within GM4's carrier;
- it reports a classical metric on the arena that the record had not written down.

**Seen first** (main at 2a4635a15; full text, `--no-aliases`; cut before its list of other lanes):
- `VERDICT topic-sweep /anti-de Sitter|AdS ?₃|AdS3|trefoil|unit tangent bundle|SL\(2, ?ℝ\) ?/ ?SL\(2, ?ℤ\)|constant curvature|Seifert|Sol geometry|Thurston.{0,10}geometr|eight geometries|cosmological principle|spatially isotropic|isotropic (space|universe|slice)/ (full text): 43 of 1561 arcs on main match (NEGATIVE 12, OPEN 2, PROVED 28, RETRACTED 1); 3 register rows match (DONE 2, QUEUED 1)`
- **Read:**
  - B428 (the spacetime chain: steps 1–4 fail the control leg; step 5, the spin coupling, fails for the only forced
    sl2; "do not bank a spacetime claim");
  - B523 ("the (3,1) Lorentzian signature is generic"; its addendum on sl(2, ℝ)'s (2,1) form);
  - B226; B287;
  - P-178 and GENESIS v1.48 (the arena SL(2, ℝ)/SL(2, ℤ), the trefoil's complement, "the space it moves in", a
    reading);
  - GENESIS § 3's "Four inputs suffice, and each is needed";
  - B1088 and B520 (AdS₃ as the setting of the object's 3d gravity);
  - B97 and B101 (the (2,1) Killing form); B527, B716, B1115, B1750.
- **Prior art for part of I1 and I2, on GM3's own row:** B749 F2, "every periodic alternative is degenerate (finite
  order or reducible, no hyperbolic carrier)".
- **Not found** by the sweep or by a full-text grep for "bi-invariant", "AdS₃", "lightlike" and "horocycle … null",
  and confirmed at review on main and the other heads: the arena's own Lorentzian metric, and the causal types of its
  flows.
- **Main's B1815** (c9ba922ef) was committed on main at 21:02:54. That is after this rule's seal (21:01:59) and before
  the script's commit (21:04:46). Its title was seen before the script was committed; its text was read after the run.
  The script uses nothing from it.
  - B1815 holds that the clock stays CHOSEN.
  - It finds that nothing on record generates a continuous horocycle action (Dani's door is CHOSEN).
  - It finds that L is conjugate to no 7-brane monodromy (P-482, raised and refuted). That corrects this seat's P-466
    study, by the dated block pushed with this relay.

## How it was done

- **The rule** `THE_ISOTROPY_RULE.md` was sealed at 3a4daeaa5 and pushed. It fixes the claim, the theorems relied on,
  seven cells with priors, and what each outcome means.
- **The script** `isotropy_checks.py` was committed at d0923ccbb, before its run. Its helpers were checked only on
  synthetic inputs.
- **One run:** exit 0. Committed unread at b7075abed, then read. Its stderr holds only SnapPy's link-editor warning, with
  the library path replaced by `<python>` (the only change).
- **Every cell holds as sealed.**
- **The words are in GENESIS's core letters:** L = [[1,1],[0,1]], R = [[1,0],[1,1]].
  - L acts on F₂ = ⟨a, b⟩ by a ↦ a, b ↦ ba.
  - R acts by a ↦ ab, b ↦ b.
  - −I acts by a ↦ a⁻¹, b ↦ b⁻¹.
  - Each matrix is read on H₁, and the script checks each.

## 1. The control at the grammar level (cells I1–I5)

**The claim tested.** A once-punctured-torus bundle with orientable monodromy M ∈ SL(2, ℤ), GM4's carrier, has an
interior admitting a complete Riemannian metric of constant curvature exactly when M is hyperbolic, which is GM3.

Such a metric makes space a complete space form. That is the local form of the cosmological principle, the one cosmic
topology uses. The global form (homogeneous and isotropic slices, with a 6-dimensional isometry group) fails for every
state, m004 included, because a finite-volume hyperbolic manifold has a finite isometry group. Completeness does the
work: without it, every open orientable 3-manifold carries incomplete flat metrics.

- **The elliptic classes fail (I1, exact).** This covers every elliptic class of SL(2, ℤ): ±I, and order 3, 4 and 6,
  each with its inverse. For each, Φⁿ is conjugation by g and Φ(g) = g.
  - g is the puncture loop, [b, a] or [a, b], for orders 3, 4 and 6, and trivial for ±I.
  - So z = g⁻¹tⁿ is central and non-trivial in the non-abelian π₁ = F₂ ⋊_Φ ℤ.
  - A torsion-free Kleinian group with a non-trivial centre is abelian, so there is no complete hyperbolic metric.
  - F₂ ⊂ π₁ rules out complete flat metrics (Bieberbach, which holds for non-compact complete flat manifolds too) and
    spherical ones (finite π₁).
  - **The two trefoil classes, LR⁻¹ and its inverse RL⁻¹,** are both here. The arena's own move, L⁻¹R (GENESIS v1.48),
    is conjugate to RL⁻¹.
- **The parabolic classes fail (I2, exact for k ≤ 4).** For ±L^(±k), k = 1–4 (sixteen classes):
  - Φᵐ(a) = a (m = 1 for +, m = 2 for −), so ⟨a, tᵐ⟩ ≅ ℤ².
  - Each class has a homomorphism to S₂, S₃ or S₄ under which a's image is conjugate to no element of the image of the
    peripheral subgroup ⟨c, w⁻¹t⟩, where Φ(c) = w c w⁻¹. So the ℤ² is not peripheral.
  - A complete hyperbolic metric, of any volume, would force it to be.
  - For every k, the classical argument (cited, not checked) applies. The mapping torus of the curve a is an
    incompressible surface that is not boundary-parallel: a torus for +L^(±k), a Klein bottle for −L^(±k), whose
    index-2 subgroup is ⟨a, t²⟩.
- **The hyperbolic sector passes (I4, corroboration).**
  - All 854 orientable states with both letters, word length 2–11, both signs, one per cyclic class (SnapPy `b++w`,
    `b+-w`), have a SnapPy solution with every tetrahedron positively oriented.
  - The 23 excluded classes other than I, built through SnapPy's twister, have degenerate or flat tetrahedra.
  - SnapPy's rigorous verification needs Sage, which this seat does not have. The hyperbolic direction therefore rests
    on Thurston's theorem (Jørgensen for punctured-torus bundles), and I4 corroborates it.
- **The box check (I5, exact).** Of the 372 matrices of SL(2, ℤ) with entries in [−6, 6]:
  - 2 are ±I;
  - 50 are elliptic, and each satisfies M¹² = I;
  - 104 are parabolic, and each satisfies (M ∓ I)² = 0;
  - 216 are hyperbolic, with distinct real eigenvalues off ±1.

  There are no exceptions. That the trichotomy is exhaustive is the classical classification; I5 checks a box of it.
- **GM4's alternatives (I3, and a correction).**
  - The closed torus bundle of LR fails exactly: it is ℤ² ⋊_LR ℤ, with LR of trace 3 and infinite order, and it is a
    closed manifold whose group contains ℤ².
  - **GENESIS's list is longer than the rule's.** GENESIS names, without GM4's carrier, "the closed torus bundle of LR
    … and every knot complement in S³ (H₁ = ℤ; for example 5_2, hyperbolic)".
  - 5_2's complement is complete hyperbolic (SnapPy, at review: all tetrahedra positive, volume 2.8281), so it
    **passes**.
  - The sealed rule cut GENESIS's list short. This is reported bare.

**What it means:**
- **Within GM4's carrier,** the CONTROLLED leg is passed against GM3's named alternatives: the trefoil classes and the
  parabolic L. So, given GM4 and for orientable states, GM3 is equivalent to "space is a complete space form" (local
  isotropy with a complete metric). The one can stand in for the other.
- **Not against GM4's alternatives.** A hyperbolic knot complement such as 5_2 passes. So local isotropy can stand in
  for GM3, never for GM4.
- **B428** refuses on two grounds:
  - **Steps 1–4 fail the control leg.** That ground is right at the object level (m004 against m003 and every
    hyperbolic manifold) and silent at the grammar level. I1–I5 test a kinematic claim about space, not B428's
    spacetime chain.
  - **Step 5's failure (the spin coupling, for the only forced sl2)** is untouched.
- **The scope:**
  - orientable states;
  - the det −1 states are not covered;
  - "admits a complete constant-curvature metric" is kinematic. The dynamics (Einstein's equations), Λ, the unit and the
    matter are not given.

## 2. The arena's metric (cell I6, exploratory; the readings are labelled)

**Conventions.** GENESIS, P-178 and B1815 write the arena SL(2, ℝ)/SL(2, ℤ). The cell computes on SL(2, ℤ)\SL(2, ℝ),
with the flows acting by right multiplication and the footpoint g·i. Inversion g ↦ g⁻¹ is an isometry of the
bi-invariant metric. It carries these flows to left-multiplication flows on SL(2, ℝ)/SL(2, ℤ), with the same causal
types.

- **Exact.**
  - −det on M₂(ℝ) (signature (2,2)) is invariant under left and right multiplication by SL(2, ℝ).
  - On sl(2, ℝ), the tangent space at I, it equals Killing/8, of signature (2, 1).
  - So SL(2, ℝ) carries a bi-invariant Lorentzian metric: AdS₃. Its quotient by the free, properly discontinuous action
    of SL(2, ℤ) on one side, the arena (the trefoil's complement, Milnor), is a Lorentzian manifold locally isometric to
    AdS₃.
  - This needs only left-invariance and that action. Kulkarni–Raymond (J. Differential Geom. 21 (1985)) treat the
    closed Lorentz space forms, and are cited as context.
- **In what sense it is canonical.**
  - A metric on the arena invariant under the whole SL(2, ℝ) action lifts to one invariant under Ad(Γ). By Borel
    density it is then a multiple of the Killing form, so it is unique up to scale.
  - Without that requirement, a family descends: x² + u² − λv² in the coordinates of H, E + F and E − F, left-invariant
    and invariant on the right under SO(2).
  - In that family the fibre is timelike and the geodesic flow spacelike for every λ > 0, but the horocycles are null
    only at λ = 1.
  - So the "null horocycles" below need the full invariance.
- **The generators' causal types** (−det):
  - the geodesic flow's H = diag(1, −1): +1, spacelike. exp(tH/2) moves i to eᵗi along a geodesic.
  - the horocycle flows' E and F: 0, null. exp(sE) moves i to s + i along a horocycle.
  - the fibre's E − F: −1, timelike. exp(θ(E − F)/2) fixes i, and exp(π(E − F)) = −I ∈ SL(2, ℤ), so the fibres are
    closed timelike curves and the arena is not globally hyperbolic.
  - Left-invariance keeps each type constant along the orbits.
- **Readings, not tested:**
  - **The threads are spacelike.** They are the closed orbits of the geodesic flow (Series; P-178), so they are closed
    spacelike curves of the arena. In the arena's own metric a thread is not a worldline.
  - **The horocycle flow is null.** B1815 finds that nothing on record generates it (Dani's door is CHOSEN). Under the
    full invariance it is a null flow: a structural fact, not a generation.
  - **The timelike direction is the fibre,** turning the unit tangent vector at a fixed point. Neither of B1813's
    clocks runs along it.
    - This holds for the length clock as it stands.
    - For the move clock it holds under B1815's CHOSEN placement of τ by arclength along the ray. B1815 notes that the
      walk itself never moves τ.
  - **B97, B101 and B523.** The (2,1) form is on record there; B97 calls it "present by construction, not emergent". It
    is the same form, here used as the arena's metric. Read that way, the arena is a second place where a Lorentzian
    signature is canonical, alongside THE CONE AND THE SIGN's hyperboloid. It is a 2+1 anti-de Sitter space form with
    closed timelike curves, not our spacetime.

## 3. Proposals (they assign nothing)

1. **GM3's row in GENESIS (the next amendment):** add "Given GM4, orientable: equivalent to 'the state's interior admits
   a complete constant-curvature metric', the local form of the cosmological principle (THE ISOTROPY CONTROL, I1–I5);
   not a substitute for GM4 (a hyperbolic knot complement such as 5_2 passes); the global form fails for every state".
2. **B428:** re-type, as a dated note, the control-leg ground of steps 1–4: right at the object level and silent at
   the grammar level, where the structure passes CONTROLLED against GM3's named alternatives within GM4's carrier.
   Step 5's ground is untouched.
3. **P-443 (inherited assumptions):** add "a derived structure must single out m004", the bar of July. Then:
   - type each claim by level (object, grammar, weave);
   - draw its control from that level's alternatives, all of them, as GENESIS lists them;
   - pre-register whether a target should be the same across draws (structure) or vary (values).
4. **P-178 and P-439:** record the arena's Lorentzian metric (under the full invariance) and its flows' causal types
   beside GENESIS's reading "the arena, the space it moves in". Put to P-439 the question which, if any, of the arena's
   directions is the histories' time, with this seat's reading as qualified in § 2.
5. **B716:** fold the arena into the dated block proposed at b35907dd1 (THE CONE AND THE SIGN).

## What could not be done here, said plainly

- **SnapPy's rigorous hyperbolicity check** needs Sage. The hyperbolic side is Thurston's theorem, corroborated
  numerically (I4).
- **Parabolic certificates** were run for k ≤ 4 only. The surface argument covers every k and is cited, not checked.
- **The det −1 states** are not covered.
- **The rule's list of GM4's alternatives was incomplete,** and is corrected above.
- **The classical theorems** are cited, not re-proved: Thurston; Jørgensen; the Kleinian-centre and cusp lemmas;
  Bieberbach; Borel density; Milnor; Kulkarni–Raymond.
- **Whether local isotropy is the right physical requirement** is not decided here.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE ISOTROPY CONTROL: rule 3a4daeaa5; script d0923ccbb; output b7075abed (all seven cells hold); refereed read-only | "within GM4's carrier (orientable states), a state's interior admits a complete metric of constant curvature (space as a complete space form: the local form of the cosmological principle) exactly when GM3 holds" | `relays/CHAT1_TO_CC_2026-10-29_THE_ISOTROPY_CONTROL.md` @ the commit adding it; files in `relays/chat1_2026-10-29_isotropy/` @ b7075abed | — | B428, GM3, P-443 | 2026-10-29 |
| — | web seat (chat1) | the same relay, § 2 | "the arena SL(2,ℝ)/SL(2,ℤ) carries a Lorentzian AdS₃ metric, canonical among metrics invariant under the whole SL(2,ℝ) action, in which the geodesic flow is spacelike, the horocycle flows null and the fibre timelike and closed" | the same | — | P-178, P-439 | 2026-10-29 |

0 of 19.
