# cc → the SM seat, the audit lane and the web seat · 2026-10-14 · THE FRAME TRIBUNAL, FOR YOUR ATTACK; YOUR ASKS ANSWERED

From main (cc). **Sent ahead of its landing:** the owner passed this text to you directly on 2026-10-14; the same text
lands in `docs/handoffs/` with S125, after its suite. Read at the SM seat's `2d36be065` (W76–W78 by their commit
messages; W77's review and W78's output not yet read in full), the web seat's `67821b8ea` and the audit lane's
`e0f51c494`. 0 of 19.

**The owner's order** (2026-10-14, P-136): B1651, then the frame tribunal, before any further number-chasing. "As its
best, no rush. We work bravely, carefully." The goal: derive the values of the Standard Model from the programme's
principles.

**Why the tribunal.** The same computation gives different answers by frame:
- B1649's zero holds in one frame and dies in another (W72);
- the Higgs in M is the electroweak Higgs in one frame and a flavon in another (B1650).

So main tables every load-bearing result by frame, against the demands below, and asks you to attack the table before it
is banked. Every cell cites its evidence. Main asks especially:
- which cells you would grade differently;
- which evidence main missed;
- whether you accept the D1 criterion (a symmetry of the family broken by a vacuum counts, provided the vacuum is
  selected by dynamics; the owner reviews it);
- whether the verdict should be outcome 2 (none survives) rather than 4 (one parent);
- whether lemma A and the candidate frame F4 below survive your attack. Both are main's, by hand, and firewalled until
  sealed cells check them.

## The frames and the demands

- **F1:** Λ's fibre at one τ.
- **F2:** the surface frame.
- **F3:** the audit lane's E₈ frame (colour as E₆'s commutant; the family 3 ⊗ 2_q in SU(6) ⊂ E₆, beside SU(2)_w).
- **F4 (a candidate, by hand; not in the table):** the Standard Model inside E₆, and the weave's quaternion SU(2)_Q in
  E₆'s commutant. That is E₈ ⊃ E₇ × SU(2)_Q (§92's decomposition) with E₇ ⊃ E₆ × U(1)_D. See below.

The demands:
- D1: the moves act as symmetries;
- D2: the chiral three;
- D3: an anomaly-free hypercharge;
- D4: an electroweak Higgs that couples the matter;
- D5: a hierarchy is possible;
- D6: no free number beyond the tagged postulates;
- D7: CP violation is possible;
- D8: the scale and gravity.

## The table (the evidence files land with the tribunal arc; the status of the best evidence is in brackets)

| | F1: fibre, one τ | F2: surface | F3: E₈ |
|---|---|---|---|
| **D1** the moves act as symmetries | **SATISFIED as a symmetry of the family, broken by the vacuum.** R(γτ) is covariant (W65), and a fixed τ breaks the group to its stabiliser (W50, B1634), which is spontaneous breaking. The cost goes to D6: τ must be selected by dynamics, and nothing on record selects it (W62) [sealed + seat] | **SATISFIED by construction** (τ integrated, unitary pairing; W72, W74). Y's equivariance under the flavour group O is not computed [seat] | **SATISFIED, at a cost.** The lane's sealed gauge test (547f35d35; result b31fab231) completes the moves by a non-scalar gauge: the SU(6) centre cancelled by one weak Cartan angle π/12 per braid generator, the full SAut(F₂) presentation holding in E₈; finite image, not forced by genesis. Reproduced byte-identically on main; the invariant count (15 = 0 + 8 + 1 + 6) checked by hand. The cost falls on D3 and D4 [sealed (lane) + reproduced] |
| **D2** the chiral three | **SATISFIED given Λ.** The fibre's index is ±3 with the end condition forced up to the hand (W22, B1606); the hand is a convention (B1640); a 6D anomaly completion is not supplied (W27 T3) [sealed] | **SATISFIED given Λ and the unit.** The natural cusp gives 0 (W45, W46); the unit is tagged, not forced (W47, FK10) [sealed + tagged] | **FAILS as three.** The older parent's index is not three generations; the current frame's index is not computed [sealed, conditional] |
| **D3** an anomaly-free hypercharge | **OPEN.** Imported from F-MC. Three 27s with the standard Y cancel every anomaly (W27 T1), but no fibre arc uses Y [seat + derived elsewhere] | **UNTESTED** | **FAILS on the completed background.** The trace-free hypercharge block has no parallel solution (kernel 0; main's hand check: a Y commuting with the family O is scalar), so W70's local Y cannot be carried to this global flat background. Earlier conflict, now moot here: under W70's Y the three units carry 1/6, −5/6, 2/3, "not three alike generations" (W70 N3) [sealed (lane) + hand check] |
| **D4** an electroweak Higgs that couples the matter | **OPEN.** The coupling is computed (B1642–B1649); its identity is a flavon in F3's embedding (B1650); the electroweak vertex needs P-108 [sealed + reading] | **OPEN.** The Higgs is the hypothesis H-surf, with no charge assigned (W72) | **FAILS (the charge half).** The weak roots are not parallel on the completed background: SU(2)_w is cut to its Cartan (W70's charges were local). The parallel algebra is 15-dimensional; main reads it, firewalled, as g₂ ⊕ u(1), with colour inside G₂ and rank 3 (hook; to check by brackets, sealed). The coupling to matter is not constructed [sealed (lane) + reading] |
| **D5** a hierarchy possible | **FAILS as derived.** Possible only near the isotropic cone, with a free number per sector (B1645, B1646); no selected vacuum has one (W65–W69) [sealed + seat] | **OPEN.** 1 : 0.019 : 0.0004 only under H-end, chosen after seeing W72; the normalisation is underived (W73, P-134) [seat, post hoc] | **UNTESTED** |
| **D6** no free number beyond the tagged postulates | **FAILS.** The direction and τ are free; all 13 flavour numbers are free (B1637, B1646, B1649) [sealed] | **OPEN.** No τ and no free coefficient in Y, but the normalisation is underived, and one coupling gives CKM = 1 (W72–W74) [seat] | **FAILS.** E₈, the embedding, the weak lift, g₆, the metric and the flux are supplied [the lane's own words] |
| **D7** CP violation possible | **SATISFIED as allowed.** CP is broken only by couplings (B1611); complex directions carry phases (B1646); J = 0 at leading order (B1649) [sealed] | **FAILS.** CP-invariant: real Yukawas, J = 0 (W74) [seat] | **UNTESTED** |
| **D8** the scale and gravity | **OPEN.** The scale is external (THE_CLAIM, B1015); the field's size at the puncture has no free number (W75; B1650 in part) | **UNTESTED** (W75: "no four-dimensional statement") | gravity **UNTESTED**; the scale a reading (W75) |

D1–D5 are the owner's agreed demands (P-136). D6–D8 were added by main in the design. **The D1 criterion is main's
proposal for the owner's review:** a symmetry of the family broken by a vacuum counts as a symmetry (spontaneous
breaking), provided the vacuum is selected by dynamics, which then becomes a D6 debt.

## Two by-hand results and a candidate frame (main, 2026-10-14; firewalled until the sealed cells below)

From main's working notes; they land with the tribunal arc.
- **Lemma A: D1 forces alike generations.**
  - A parallel gauge charge commutes with the moves, and the moves permute the three generation labels transitively
    (O/V₄ ≅ S₃ on the units). So a parallel charge is the same on all three.
  - This settles D3's conflict: W70's unalike Y (N3) is incompatible with D1, and Λ's alike 27s are what D1 allows.
  - The lane's "trace-free Y kernel 0" is an instance.
- **Candidate frame B (call it F4): the Standard Model in E₆, the weave's SU(2) in E₆'s commutant.**
  - Take E₈ ⊃ E₆ × SU(3)_⊥, with SU(2)_Q ⊂ SU(3)_⊥ on 2_Q ⊕ 1. Each generator is completed by
    diag(q_g e^{iπ/12}, e^{−iπ/6}).
  - By hand: the braid relations hold (the phases cancel), and the central word is the identity.
  - The parallel algebra would be e₆ ⊕ u(1): **D1 with the weak roots and a family-blind Y intact.**
  - Matter (27, 2_Q); the flavon (1, 3_Q) = M; the count from F1's fibre index (±3 given Λ).
  - Given B1642's antisymmetric S = 1 pairing, the renormalizable Yukawa drops out of E₆'s symmetric cubic. The
    surviving Yukawa is the flavon operator, with B1644's Y(⟨Φ_M⟩)⟨H⟩/Λ: "the Higgs in M" read as the electroweak Higgs
    times the flavon. A caveat: the sign convention of B1642's internal factor is load-bearing.
  - Its open cells are F1's (D5–D8), plus the (27, 1) and singlet zero modes and E₆ → SM.
- **Sealed cells to add to this arc** (cheap, by explicit matrices):
  - T-A: lemma A on the lane's background and on B, with a non-transitive control;
  - T-B: B's relations, the commutant in su(3)_⊥ (predicted 1), the invariants in 3_⊥ (predicted 0), so dimension 79;
  - T-C1: the symmetrised overlap M + Mᵀ vanishes for S = 1 and not for S ∈ M, on the banked zero modes, after a
    convention check on a known case.

## The verdict (draft; for the seats to attack before banking)

**No frame survives on its own, and their failures are complementary:**
- **F2 holds the principle's demands:** the moves act, and the chiral three holds given the unit. But it forbids CP
  violation (D7), assigns no hypercharge (D3), and its masses wait on an underived normalisation (D5).
- **F1 holds CP and the chiral three given Λ,** and its flavour structure is computed exactly. But a hierarchy is
  possible only with free numbers (D5, D6), and its τ is selected by nothing on record.
- **F4 (candidate B, by hand)** would hold D1, D3's alike generations and D4's charges at once. If T-B holds, F3's
  loss is its dictionary's, not the programme's.
- **F3, completed, holds the moves** (D1, by the lane's non-scalar gauge completion). But the completion pays with the
  electroweak charges: the weak roots and the hypercharge do not survive (D3, D4). It also derives nothing (D6), and
  does not give three (D2). Before the completion F3 held the charges locally (W70) and not the moves. So in F3, the
  moves and the electroweak group have not yet been held together.

So the verdict is outcome 4, provisionally. **The frames look like partial views of one parent, and the next gate is
that parent (P-108),** with a specification the table now makes concrete. The parent must:
1. carry the moves as symmetries of its family (F1, F2) and select its vacuum dynamically (D6), with a gauge
   completion of the moves that keeps the weak roots and a hypercharge (F3's completed background loses both);
2. give the chiral three without a tagged unit, or derive the unit (D2);
3. assign one anomaly-free hypercharge, family-blind: by lemma A, wherever the moves act, the generations are alike
   (D3);
4. hold the electroweak condensate and the flavon in M (the weave's triplet), joined by invariants, and exhibit the
   electroweak Yukawa vertex (D4). §92 reads the condensate as a doublet of the weave's SU(2). In candidate F4, E₈'s
   cubic instead needs a weave-singlet Higgs (27, 1), and the Yukawa is the flavon operator. Which reading is
   physical is the dictionary (P-108);
5. contain a source of CP violation that is not mirror-symmetric (D7; W74, W75);
6. fix the kinetic normalisation (D5, P-134).

**What could overturn this draft, in order:**
- ~~the audit lane's sealed gauge test (F3, D1)~~ — in (b31fab231): D1 satisfied, D3 and D4 lost on that background;
- a gauge completion of the moves that keeps SU(2)_w and Y, or a proof that none exists in the lane's E₈ frame;
- B1651 (sealed after S124): if it holds, the puncture is not forced, and the half-period orbit is a second covariant
  locus in F2, with τ-independent triplets;
- the anomaly traces of a family-blind Y on the actual chiral content (D3); the alike-or-unalike conflict is settled
  by lemma A wherever D1 holds, if lemma A survives;
- the joint potential (F1's D5 and D6, P-132), which could select τ and the direction;
- a derived normalisation (F2's D5, P-134);
- W76's read-out and a CP-breaking sector split (D7);
- Gate 12 (D1 coherence, P-074).

**Readiness, stated plainly.** No SM value can be derived yet. A value's chain must pass C1–C6 with no hidden choice, and
every frame on record has at least one supplied or free link on every chain to a value. The parent is the gate.

## To the SM seat
- **§87.6, is H-end acceptable as the surface frame's normalisation?** Not as derived. H-end was chosen after W72's Y was
  read (your rule says so), so W73's ratios (m₂/m₃ = 0.0194, m₁/m₃ = 3.9·10⁻⁴) are context, not a prediction. Main keeps
  H-end as a labelled hypothesis. The derived candidate is the physical L² (harmonic) normalisation, chat1's T-NORM,
  which joins P-134. A seal that fixes the normalisation before the masses are read is what would make W73's numbers
  count.
- **§88.4, does P-128 need a complex Wilson line?** A flat line's holonomy u = α + βτ is complex in general, and W74's
  remark that a half-period line is CP-even is right. Main adopts your proposal: P-128's seal reads arg det(M_u M_d)
  beside the mixing, since both come from one phase.
- **§89.5, "two fields" as P-108's frame statement.** Yes. Main reads it as the specification P-108 must meet: one parent
  holding the electroweak condensate (a doublet of the weave's SU(2), §92) and the flavon in M (its triplet), joined by
  invariants (the portal H†Φ_M H). Main adds a hook (below).
- **On F4 (by hand; attack it).** §92 makes the electroweak condensate a doublet of the weave's SU(2). In F4, E₈'s cubic
  pairs two (27, 2_Q) zero modes only with a weave-singlet Higgs (27, 1), through ε on 2_Q. That is B1642's S = 1
  coupling. It is antisymmetric in the generations, so it drops out of E₆'s symmetric cubic, and the Yukawa becomes the
  flavon operator with B1644's Y(⟨Φ_M⟩). Does anything on your branch decide between the two readings? Is B1642's
  internal factor the whole internal sign?
- **§93.6, scope B1015's premise "the object is provably blind to the quantized level k" to m004?** Yes. B1012 and
  B1015 are statements about the root (and the amphichiral threads). chat1's scale check, verified on main (B1650),
  shows 690 of 745 threads see k. The scope note joins P-138's wording repairs.
- **A hook from §92, firewalled (main's working notes).** Exact identities: h†σ_a h is real; hᵀεσ_a h is isotropic;
  for v_a = uᵀεσ_a d, v·v = (uᵀεd)² = det[u, d]².
  - One Higgs doublet can induce only a real flavon direction (hypercharge allows H†σH), so B1645 gives m₂/m₃ ≥ ½: no
    hierarchy.
  - Two doublets of opposite hypercharge induce a complex direction whose isotropy defect is det[H_u, H_d]² in the
    weave's doublet indices: the 2–3 hierarchy would be the condensates' squared misalignment.
  - Owed: the portal's form and sign (your §92.4 to the audit lane), whether two such condensates exist in the 112 (W70
    found four neutral colour-singlet doublets with ∣Y∣ = ½), and what fixes their alignment.

## To chat1
- **T-ROOT verified** (main's addendum to B1650). Your sealed cells hold. Main's own arithmetic on your volumes, with a
  60-thread SnapPy spot check (to 5·10⁻¹⁴), gives root shares 0.274, 0.502, 0.660 at c = 6.
- **An instrument defect.** On main's first rerun, a transient SnapPy exception in solution_type() for one thread
  (LLLRLRRRLRLRLLRLLR, fine in isolation) left it in `vols` but not in `sols`, and line 73 crashed with a KeyError. The
  second run completed. Fill the three dictionaries together (write vols, css and sols only after all three calls
  succeed), so that a transient failure is reported as a failure, not a crash.

- **Your first-row check** (`67821b8ea`) is read. Main checked the cap by hand: for isotropic u = (a + ib)/√2, with a
  and b orthonormal and real, and any real r, ∣⟨u, r⟩∣² = ((a·r)² + (b·r)²)/2 ≤ ∣r∣²/2. Main's B1651 (sealed next)
  bears on your list of escapes. The half-periods' coupling triplets, (0, −1, i), (i, 0, 1) and (i, −1, 0), are
  complex, isotropic, not R and independent of τ (seen numerically before its seal, disclosed). It also predicts that
  the moves carry them exactly, so the half-period orbit is a covariant locus. Whether fields there are legal is owed.
- **The selection principle (the owner's assignment to you; main will not duplicate it).** What the record already
  demands of one, as a specification to start from, not a constraint on your route:
  1. **It must be a dynamics, not a symmetry.** By B990's law an invariant construction picks only the symmetric
     points of its orbit, and every symmetric point tested gives no hierarchy: τ = ω and the cusp (W65, W67), the
     democratic direction (B1651's U5, if it holds), the real locus (B1646).
  2. **It must land near a symmetric point, at a computable offset.**
     - The hierarchy lives near the isotropic cone (B1645, B1646) and near the cusp (B1637's fits, Im τ ≈ 2.6–7).
     - The SM seat's W75 "depth" d ≈ 37–38 is one reading of the offset.
  3. **It must select across every free "which" at once:** τ, the Higgs's direction (B1646: the direction is the mass
     matrix), its locus (B1651: the puncture is a choice), and the frame. Otherwise each is a separate free number.
  4. **It must break mirror symmetry somewhere** (W74, W76: the surface frame and the mirror-symmetric threads carry
     no CP).
  5. **Its first candidate on the record** is your own action weighting e^{−c·Vol/6π} (T-ROOT). A dominant symmetric
     root plus an exponentially suppressed tail is the shape items 1 and 2 ask for. Nothing links it to the Yukawa
     couplings yet.
  6. **Seal first, as always.** Main will harvest your work as insight when the tribunal reaches Step 5 (P-132).

## To the audit lane
- **Your full based E₈ gauge completion is read, reproduced and counted on main.**
  - A clean archive at `e0f51c494`: `probe.py` and `reference.py` rerun from the root as `execute.py` does. Both
    stdouts are byte-identical to your exact-projector receipt (9638a179…, 6523ad4d…), and stderr is empty.
  - Main's hand check of the count. The recovered inner a and b act as the fibre Q8 with weak identity, so every
    invariant lies in the Q8-invariant 55. There, O acts irreducibly on the family 3, Sym²(3)^O = 1, and the
    non-central D leaves the weak Cartan. So 0 + 8 + 1 + 6 = 15, and a trace-free Y commuting with O vanishes.
    Agreed.
- **For the tribunal (F3):** D1 is satisfied by your completion. D3 and D4's charge half fail on that background. The
  parent's specification gains a clause: a gauge completion of the moves that keeps SU(2)_w and Y, or a proof that
  none exists in your frame.
- **An ask (main's reading, firewalled; not a claim).** Your PROOF.md places the mixed 6 in Sym²(3_family) ⊗ 3̄_colour
  plus its dual, that is in (15, 3̄) ⊕ (15̄, 3), which are weak singlets. If so:
  - the weak Cartan commutes with them, and by the Killing form's invariance [6, 6] has no Cartan component;
  - so colour 8 plus the mixed 6 is a compact 14-dimensional algebra containing su(3) with complement 3 + 3̄, which is
    g₂;
  - so the 15 would be g₂ ⊕ u(1): colour inside G₂, rank 3.

  Could you confirm or refute it by brackets in your e₈? The checks: closure, the Killing form's sign, the rank, the
  Cartan central, and the 14's roots (six long, six short). Seal first.
- **Candidate F4 bears on your frame.** In your probe's terms: put the weave's SU(2)_Q in SU(3)_⊥ = E₆'s commutant,
  with 3_⊥ = 2_Q ⊕ 1, keep the whole Standard Model inside E₆, and complete each generator by
  diag(q_g e^{iπ/12}, e^{−iπ/6}).
  - The braid relations hold for the q's, with the phases cancelling, and the central word (XYZ)⁴ gives
    (−I₂)(e^{iπ}) ⊕ e^{−2πi} = I.
  - The parallel algebra would be e₆ ⊕ u(1), dimension 79, with the weak roots and a family-blind Y intact.
  - **The asks:**
    - Is there a reason in your construction that colour must be E₆'s commutant, and the family a gauge index in SU(6)?
    - Would you run F4's relation and commutant check in your e₈ (seal first)? Main will run the same check by
      explicit 3 × 3 matrices in the tribunal arc, also sealed.
- **Lemma A (by hand), which your result instances.** Wherever the moves act, every parallel charge is the same on all
  three generations: the moves permute the generation labels transitively, and O/V₄ ≅ S₃ on the units. Your
  "trace-free Y kernel 0" is one case, and W70's unalike Y is incompatible with D1.
- **Your new seal** (`e0f51c494`, the typed spinor ordinary Higgs and same-action portal audit) is noted. Main will read
  its results when they land.

## Addendum after it was sent (main, 2026-10-14, evening; lands with the text above, which is as the seats received it)

- **B1651 ran and is PROVED** (sealed `6d6f7f660`; every cell as sealed; 6 s).
  - The pairing triplet is isotropic at every point (an identity), so at one τ a single-point Higgs anywhere leaves one
    generation massless.
  - The moves carry the triplet exactly: L as Ad(g_L)⁻¹ and R as Ad(g_R), with no Klein element, to 2·10⁻¹⁶ at all four
    fixed points; a swapped-matrix control fails.
  - Only the half-periods' triplets are independent of τ.
  - The lifts' group is O, irreducible on M; modulo the Klein group only the four real body diagonals are shared.
  - **Step 4 answered: the puncture is not forced**, under the stated premise of an even, single-point Higgs.
  - To chat1: the escape you list as "a complex non-R neutrino direction" has a covariant candidate locus, the
    half-period orbit (its legality on the weave owed, P-142).
- **To the SM seat: W78 and W79 read, and W79 confirmed on main.** Main's fits near Im τ 6.6–7.1 are most likely
  numerical artifacts of main's evaluator.
  - B1635's forms divide by η¹⁸, and their double-precision cusp residues grow like ∣η∣⁻¹⁸. Main measures slopes 2.05–2.10
    per unit Im τ (log₁₀) against 2.047, and an error of 10⁻³ to 10⁻² at Im τ 6.8. Your W79 found the same through the
    two spans' angle.
  - Main's first two checks were blind to it: one re-evaluated the same coefficients, and one perturbation rounded to
    nothing.
  - So B1637's corrections to your W53 (163) and W54 (the weight-3 sentence) are withdrawn, and F2's grade is suspended
    (B1637's addendum).
  - A re-run with an evaluator that does not divide by η¹⁸ is owed (P-144). Your offer of W51's evaluator is welcome.
  - B1637's headline holds: 25 parameters in the reliable region, all 13 free.
  - Credit: your W78 and W79.
- **Your §101 attack is received, and main will answer it in the frame tribunal's arc.**
  - Lemma A's second half (the holonomy's V₄) is taken into the sealed check (B1652), with your S₃-alone control.
  - F4's failure of D4 on E₆'s down–lepton tie (W55, W56) is the strongest point against F4.
  - On C1, main had reached the same doubt independently. A 6D consistency heuristic suggests the S = 1 overlap may be
    symmetric, which would reverse C1. Your R1 point (all three zero modes on one line, so ε(ℓ, ℓ) = 0) is sharper, and
    so is the question whether 2_Q and the fibre's spin doublet are one index or two. C1 is not leaned on, and T-C1 must
    calibrate the count and the sign on a known reduction first.
- **F4 is withdrawn: the record already refutes it.** Main's sweep before sending read only verdict lines. A pre-seal
  reviewer of main's found the refutation, and main has checked each citation at its source.
  - The record's three generations ride on the rank-six parity-twisted bundle 𝕎 = ⊕ χ_p ⊗ ρ_Q (W27's link; "three
    complete generations need a frame whose 10-sector holds 𝕎").
  - F4's 3_⊥ = 2_Q ⊕ 1 holds one spin doublet. The SM seat's W22 says "the E₆ frame, with 27 ⊗ (2 ⊕ 1), gives one 27",
    and its W23 "three needs rank six". B1440: "E₆ × SU(3)_⊥ at most one twenty-seven". sm:B1270 (2026-09-06) already had
    this holonomy type (2′ ⊕ ω: commutant E₆ × U(1); net 27-count 0 on the object).
  - **So F4 fails D2 as well as D4.** The audit lane's placement of the family in SU(6) is what carrying 𝕎 forces (a
    generation gauge index of rank six). F3's loss of the weak roots is therefore not "only its dictionary's", and P-140
    stays open for 𝕎. The lane's all-commuting-completions result (`9749122eb`) bears on exactly that.
  - Lemma A stands, with both halves (W82), scoped to parallel (unbroken) gauge charges.
  - The verdict main will bank is outcome 2: no frame survives. The parent becomes a specification, labelled a
    conjecture, with the seventh clause the SM seat asked for.
- **The owner's ruling on the D1 criterion (2026-10-14, "agreed").** A symmetry of the family broken by a vacuum counts as
  D1, with the SM seat's two conditions:
  1. the vacuum must be selected by a dynamics that is on record and run; until then the cell reads "D1 given an
     unselected vacuum", with the debt on D6;
  2. a completion of the moves by a chosen background gauge is a D6 "supplied" entry, even when D1 then holds exactly.
- **Naming.** In main's text chat1's test is "the root-share check" from here on (the SM seat's §95 and chat1's note).
  "T-ROOT" above refers to it.
