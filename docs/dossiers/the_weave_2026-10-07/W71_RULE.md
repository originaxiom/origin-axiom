# W71 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **P024's second test.** `philosophy/P024_the_field_from_the_end.md` reads the field as forced by the end: a bare end
  admits no finite description, so the end must carry a source (GENESIS GAP3). Its first test (W70) passed. Its second
  is this: "If the principle allows a twist that gaps every channel, the end can be described without a field, and the
  field is not forced." The owner ruled "do as u propose/recomend" (the rulings page).
- **The audit lane's packets were read first** (repo first; the lane's branch head a3e744d99). They establish, in the
  lane's E₈ frame on the punctured fibre with a complete cusp:
  - at the bare end (zero scalar, the quaternion holonomies, peripheral p = −1, untwisted) the 112 p-odd channels of
    every ordinary-spin slot are gapless: the bounding spin's −1 times p's −1 is periodic, with zero radial drift;
  - for the nine R-twists QT = Q45 + a QA + b QB (a, b ∈ {−1, 0, 1}), the slots carry 2s = 1 + a, 1 − a, −1 + b and
    −1 − b. The double twists leave no ordinary-spin slot, and the local form threshold is 1/4. The lane writes that
    this "does not certify its entire global spectrum" and is "not a free repair": it gives two copies of R, which
    admit a symmetric mass;
  - "compact-core holonomy cannot remove essential spectrum localized arbitrarily far along the end", and every
    all-channel gap on the lane's record uses a non-flat flux or the condensate.
- **What the lane did not test:** flat data at the end other than the twists. A flat connection on the punctured fibre
  that commutes with the forced holonomies can change the peripheral holonomy. So can a flat connection of the parent's
  R-symmetry. Either one changes which channels are periodic.
- **This arc is the census of field-free end data.** "Field-free" means flat, with no condensate and no gauge curvature
  at the end, and the weave's forced quaternion holonomies kept. The question: does any such datum gap every channel,
  and what does each one that does give up?

## Weave or thread?

- **Weave-type.** It takes every channel of the 248, every slot of the parent's fermions, every twist the lane bounds,
  and every peripheral class of the stated flat data (none chosen), on the shared fibre's end. Its claim concerns the
  end that every thread shares.
- **The tags.**
  - Given the audit lane's registered E₈ embedding and its (1,1) parent on the punctured fibre with a complete cusp
    (`weave_companion_roster_2026_10_08`), in the coordinates W70 used.
  - Given Λ (GENESIS FK11), and read against it in the verdict.
  - W70's admissible hypercharges, for U(1)_em = T₃ + Y.

## Seen before the rule (disclosed; by hand, from the lane's code and W70's coordinates)

- **The cusp rule.** On the cusp, Fourier modes in the periodic coordinate x reduce a slot's operator to a radial one.
  - In t = log y, a section of K^s has radial operator ∂_t + d + k e^t, where k = 2π(n + θ) and e^{2πiθ} is the
    slot's total transition around the cusp.
  - The drift is d = ½ − s for the slots built on K^s. For the slots of the other six-dimensional chirality it is
    ½ + s, by conjugation.
  - Only k = 0 reaches the continuum, and only when the transition is exactly 1. Its threshold is d². So a
    (slot, channel) pair is **gapless exactly when its transition is 1 and its drift is 0**.
- **The transition** is the product of three factors:
  - the gauge peripheral holonomy's eigenvalue on the channel: p = (−1)^{r·hq} on a root r, times q's eigenvalue
    e^{2πi r·X} when a flat connection with peripheral q = exp(2πiX) is added;
  - the spin factor: −1 for half-integer s (the peripheral loop bounds in the compactified fibre, so all four spin
    lines give −1 in the cusp frame), and +1 for integer s;
  - the R-phase, when a flat R-connection has peripheral holonomy r.
- **The drift.** With the slots as the lane writes them, the drift is 0 exactly on the untwisted slots (2s = ±1) and
  ±½ on the twisted ones (2s ∈ {0, ±2}).
- **The lane's table follows.** Gapless (slot, channel) pairs at the bare end: 4 × 112 = 448 untwisted, 2 × 112 = 224
  for each single twist, and 0 for each double twist. It is the same for all four spin lines.
- **The commutant.** The quaternion holonomies' trivial isotypic part of the 248 has dimension 55 (the lane's
  module): su(3)_c ⊕ su(3)_fam ⊕ (3, 6) ⊕ (3̄, 6̄) = F₄, plus su(2)_w. So a flat connection commuting with the forced
  holonomies takes values in F₄ × SU(2)_w. Its maximal torus is spanned by colour (2), family (W70's block-scalar
  Cartans, 2) and weak (1). By Goto's theorem every element of this connected semisimple group is a commutator, so
  every peripheral class occurs.
- **Gauge Wilson lines.**
  - **With the weak part trivial (q_w = 1),** for every q in F₄'s torus: in each untwisted slot, the 16 colour-singlet
    weak-doublet roots whose SU(6) weight takes one index from each block are family-neutral and colour-neutral. They
    keep transition 1 and drift 0. These are 8 of the 20 weights of Λ³6, times T₃ = ±½. So at least 16 gapless pairs
    remain per untwisted slot, and exactly 16 for generic q in F₄'s torus.
  - **With q_w = −1** (q = exp(2πi·½(e₃ − e₄)) in W70's coordinates), every weak doublet gets an extra −1. Every pair
    is then non-periodic or drifting, and the end is gapped everywhere.
  - **The cost.** q_w ≠ 1 needs weak holonomies that do not commute, since an abelian pair has commutator 1. A
    non-commuting pair in SU(2) has commutant ±1 in the group and 0 in the algebra. So T₃ is broken, and with it
    Q = T₃ + Y for every admissible Y, since Y has no weak component. A flat gauge datum that gaps every channel
    breaks U(1)_em.
- **R-holonomies.**
  - A flat R-connection can have non-trivial peripheral holonomy only in a non-abelian factor the twist leaves whole:
    SU(2)_A when a = 0, and SU(2)_B when b = 0.
  - A generic peripheral R-holonomy gives every slot in that factor a phase other than ±1. Its pairs are then never
    periodic, whatever the channel.
  - So the untwisted end with generic R-holonomies in both factors is gapped everywhere, and so is a single twist with
    one in the factor it leaves whole. Both keep every gauge symmetry, and both break the R-symmetry.
  - Placing the quaternion point in both R factors (r = −1 on every R-doublet) does not gap the end. It moves the
    gapless set to the p-even channels: 136 per untwisted slot.
- **The moves.** A mapping class fixes the peripheral loop up to conjugacy. The peripheral class of any flat datum is
  therefore move-invariant, and so is the twist (K is natural). The moves can neither force nor forbid these gaps.

## The method (fixed here)

- **The channels.** The 240 roots and 8 Cartans of E₈ in W70's coordinates (imported from
  `the_cusp_condensate_charge_map.py`), with p = (−1)^{r·hq}.
- **The slots.** The lane's slots: 2s_j = 1 + a, 1 − a, −1 + b, −1 − b, with R-charges (q_A, q_B) = (½, 0), (−½, 0),
  (0, ½), (0, −½).
- **The drift** of slot j is d_j = −(a q_A + b q_B) times the slot's chirality sign. The cell checks that it is 0
  exactly when 2s_j = ±1.
- **The gauge peripheral classes (exact):**
  - trivial;
  - generic in the family torus;
  - generic in F₄'s torus (colour and family);
  - q_w = −1 alone;
  - generic in the weak torus;
  - generic in the whole torus of F₄ × SU(2)_w.

  "Generic in a subspace V" is decided exactly: the phase r·X is an integer for generic X ∈ V exactly when r ⊥ V, and
  otherwise it is not real.
- **The R peripheral classes:**
  - none;
  - the quaternion point placed in each available R factor (phase −1);
  - generic in each available factor.

  A factor is available exactly when the twist leaves it whole.
- **The gap count** of an end datum is the number of (slot, channel) pairs with transition exactly 1 and drift 0. For
  the gapped periodic pairs, the smallest threshold d² is recorded.
- **The symmetry read-outs** for each datum, from its peripheral class and the commutant lemma: colour kept, weak SU(2)
  kept, U(1)_em kept (for W70's six admissible Y), and R-symmetry kept.
- **The second route (numerical).**
  - The radial model operator A = ∂_t + d + k e^t on [0, T], with Dirichlet conditions at both ends, by second-order
    finite differences (4 000 points per unit of t, capped at 200 000).
  - Its smallest singular value, for the classes (k = 0, d = 0), (k = 0, d = ±½), (k = 0, d = ±1),
    (θ = ½, d = 0) and (θ = ¼, d = 0), at T = 10, 20 and 40.
  - For k = 0 the exact value is √((π/T)² + d²).
  - The census's gapless pairs must all be class (k = 0, d = 0). Every other pair must fall in a class whose
    smallest singular value stays above a positive bound as T grows.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **E1, the twists (the lane's table, checked)** | With no flat datum added: 448 gapless pairs untwisted, 224 for each single twist and 0 for each double twist, the same for all four spin lines. Every gapless pair is an untwisted slot on a p-odd channel. The drift is 0 exactly on the untwisted slots. | 95% |
| **E2, gauge Wilson lines** | Untwisted, with no R-datum: the gapless count is 448 at q trivial; 64 (16 per slot) for generic q in the family torus and in F₄'s torus; 0 for q_w = −1, generic weak, and generic in the whole torus. The 16 per slot are the colour-singlet weak doublets with one SU(6) index per block. Every class with count 0 has q_w ≠ 1, so by the lemma it breaks U(1)_em for all six admissible Y. | 85% |
| **E3, R-holonomies** | Untwisted with generic R-holonomies in both factors and q trivial: 0, with every gauge symmetry kept. With the quaternion point in both R factors: 544 (136 p-even channels per slot). A single twist with a generic R-holonomy in the factor it leaves whole: 0. A double twist admits no peripheral R-holonomy, and its count stays 0. | 85% |
| **E4, the model operator (second route)** | For k = 0 the smallest singular value is within 1% of √((π/T)² + d²) at T = 10, 20 and 40, so it tends to \|d\| and reaches 0 only for d = 0. For θ = ½ and ¼, it changes by less than 1% between T = 20 and T = 40 and stays above 0.1. Every gapless pair of E1–E3 is class (k = 0, d = 0). | 90% |
| **E5, the verdict** | Field-free data that gap every channel exist in the family: the double twist, generic R-holonomies (untwisted, or with a single twist), and a weak Wilson line with q_w ≠ 1. With gauge data only and U(1)_em kept, none does: 16 colour-singlet, family-neutral weak-doublet channels per untwisted slot stay gapless. So P024's second test fails as worded, and the passage survives only in a restricted form (below). | 80% |

**The read-outs (no prior).**
- The full table: for every twist × gauge class × R class, the gapless count, the smallest positive threshold, and the
  symmetries kept.
- The 16 channels: their roots, SU(6) blocks, T₃ and their hypercharge under each of W70's admissible Y.
- The model operator's values at each T.
- The dimension of the forced holonomies' commutant in the 248, by characters, (248 + χ(−1) + 6 χ(g₄))/8 with g₄ of
  order 4 in SU(2)_Q. The lane's module gives 55.

## The reading, written before the run (predicted)

- **The bare end is not describable, and many data make it so.** The weave's forced data alone (the quaternion
  holonomies, ordinary spin, nothing at the end) leave 448 gapless pairs. A flat datum at the end gaps them all in
  three ways:
  - the double twist, which changes the dictionary and doubles R, so the protection of its mass is lost;
  - an R-holonomy, which breaks the parent's R-symmetry and its supersymmetry;
  - a weak Wilson line, which breaks U(1)_em.
- **So P024's passage is false as written.** "A bare end admits no finite description" is true. "So the end must carry
  a field" does not follow: a field-free twist or holonomy can describe it.
- **What survives is a restricted form, with three conditions.**
  - The dictionary is Λ's: ordinary spin, untwisted.
  - The R-symmetry carries no peripheral holonomy.
  - Electromagnetism is kept.

  Given all three, no flat datum describes the end. The end needs a non-flat datum, and the cusp condensate is one that
  keeps SU(3)_c × U(1)_em (W70). The weak SU(2) cannot survive at the end either way: gauge data that gap the 16
  channels must break it.
- **None of the three conditions is the principle's.** Λ is a tagged working postulate (GENESIS FK11), the R-symmetry
  belongs to the lane's parent, and electromagnetism is data. The moves cannot decide the gap, because it depends only
  on move-invariant data. So whether the field is forced reduces to the dictionary, GENESIS FK11's open question.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
- **The scope.** This is the lane's two-dimensional end. The lane's four-dimensional surface operator (the canonical
  β line and the owed odd-sector estimate) is not tested here, and neither are zero modes or chirality.
