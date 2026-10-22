# W127 — is the field forced to exist? GENESIS PF1 read at the weave's cusp, in three forms, and whether any of them forbids the empty end (the rule, committed before the script)

The SM-derivation seat, 2026-10-22. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's question (2026-10-22).** How can we check whether the Higgs field is forced to exist, or whether the
  approach is conceptually wrong? This is the first of three checks the seat proposed, in this order:
  1. GENESIS PF1 at the end (this arc);
  2. the consistency route (W128);
  3. the framings compared (W129).
- **Where the record stands (GENESIS v1.54, read on main).**
  - GENESIS FK15 (OPEN) asks for the field's genesis: "forced to exist, not forced which". It is settled by a
    derivation of the field's existence from GENESIS PF1–PF3, or by the owner adopting a fourth face ("what exists is
    read").
  - GENESIS FK10 carries the cusp's unit as a tagged working postulate (v1.39). B1629 shows that nothing dynamical
    supplies it.
  - W123, as corrected, shows that with line-bundle end data O(nδ), a Higgs at weight 3/2 exists iff n ≥ 1, and its
    space has dimension 3n, the chiral count. So whether the field is forced is whether the empty end, n = 0, is
    forbidden.
- **The test.** GENESIS PF1 says existence is "a frustrated cancellation". GENESIS §1 records its mathematical form as
  a reading, not a derivation: κ = tr[a, b] ≠ 2, with κ = 2 where the cancellation completes. This arc states three
  forms of "PF1 at the end", computes what each forbids on the weave's own surface, and reads off whether the field
  follows.

## The objects

- **The weave's surface and its end data** (W45, W46, W47; all from the record's lifts, unchanged).
  - **A puncture condition** cond ∈ {0, V2, V4, L6}, with fibre index f = −3, −1, +1, +3. The condition 0 is the
    canonical one, the owner's natural condition; L6 is its mirror; the sign of f is the hand.
  - **A flat twist** ε_r = v_η^r. The six with r ∈ {0, 4, 8, 12, 16, 20} keep the forced weights (W47 K1); the
    other 18 give no sections.
  - **n uniform units at the cusp**: line-bundle end data O(nδ), with n ∈ {−1, 0, 1, 2} in this arc's box.
- **The four-dimensional index** I(cond, r, n) = −χ_{3/2+12n}(T ⊗ ε_r) + Σ_{p ∈ cond} χ_{1+12n}(p ⊗ ε_r), as in W46
  and W47. W47 K5 found I = n·f + t_r(cond), with t_r(cond) = −1 at (r = 4: 0, V4) and (r = 20: V2, L6), and 0
  otherwise.
- **The Higgs space**, as W123 defines it: the weight-3/2 sections of the matter's representation, here twisted.
  - In the canonical hand it is h(r, n) = dim M_{3/2+12n}(T ⊗ ε_r).
  - In the mirror hand it is h̄(r, n) = dim M_{1/2+12n}(T̄ ⊗ ε_r), the form W123's Y6 used.
- **An exact route for h** (W123's exact route, extended; by hand, to be checked).
  - A section F of T ⊗ ε_r is η^r·g, with g a weakly holomorphic form of T at weight 3/2 − r/2, since η has no zeros
    on the upper half plane.
  - Every such g is c₀R + c₁∂R + c₂∂²R with c_j ∈ Δ^{−N}ℂ[E₄, E₆] (B1691's Wronskian).
  - On g's lines (exponents ⅛, ⅜, ⅞), n units and the twist together allow m_e = n + w_e(r) units on each line.
    Here w_e(r) = 1 when e + r/24 ≥ 1, which happens on the ⅞ line for r ≥ 4 and on the ⅜ line for r ≥ 16, and 0
    otherwise.
  - So h(r, n) is the kernel of an exact rational matrix, with no collocation and no threshold.
- **The mirror** through Serre duality (by hand, to be checked): h̄(r, n) = χ_{1/2+12n}(T̄ ⊗ ε_r) + h(24 − r, −n).
  - The second term is dim S_{3/2−12n}(T ⊗ ε_{24−r}).
  - No exponent of a twisted T is an integer (W47 K2), so its holomorphic forms are cusp forms.

## The three forms of GENESIS PF1 at the end

- **F1, frustration** (GENESIS §1's form, carried to both ends). The cancellation completes where a monodromy has the
  eigenvalue 1 (κ = 2 on the fibre). The end is frustrated iff:
  - the fibre's commutator trace is not 2 at the record's forced fibre points; and
  - no piece's cusp monodromy has the eigenvalue 1, under its twist.
  The empty end is forbidden iff it fails this.
- **F2, a non-cancelling index.** "Cancelling to nothing" is a net zero-mode count of 0, so the end is frustrated iff
  I ≠ 0. It is read in two ways:
  - **per end datum** (cond, r, n);
  - **at weave level**, where the field is twisted by all six allowed characters at once and the joint index is
    Σ_r I(cond, r, n).
- **F3, a non-empty end.** The end must carry data: n ≠ 0 in the line-bundle menu, or m ≠ 0 in W123's per-line menu.
  F3 is GENESIS FK10's unit postulate restated, and it is included to show what it gives, not as a derivation.
- **Least remainder** (GENESIS SE1's reading) orders the data that a form allows: least |n| first, then least |I|.

## Weave or thread

**Weave-type, as W45 to W47.**
- The weave's own surface, with every move at once.
- Every flat twist the surface admits that keeps the forced weights, with none chosen.
- Every puncture condition the moves keep, and every n in the stated box.
- The joint quantity is the index of the field twisted by all six characters together.
- The per-datum minima are selections made by a stated order, and are labelled so.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| P0 | the instrument reproduces the record: W46's table at r = 0 for n ∈ {−1, 0, 1}; W47's K2 exponents and K3 table; W123's exact h(0, 0) = 0, h(0, 1) = 3, h(0, 2) = 6, and one section for one unit on each single line | 97% |
| P1 | F1 holds at every end datum in the box, the empty one included. The commutator trace is −2 at both forced fibre points (the hyperbolic torus with Markov triple (3, 3, 3), and the quaternion point). Every cusp exponent of T, T̄, the six, V2 and V4 is an odd multiple of 1/24 under every allowed twist. Neither depends on n | 97% |
| P2 | canonical hand, exact: h(r, 0) = 1 at r = 4 and 0 at the other five r; h(r, n) = 3n + h(r, 0) for n = 1, 2; h(r, −1) = 0. N = 5 and N = 6 agree. Riemann–Roch holds: h(r, n) = χ_{3/2+12n}(T ⊗ ε_r) for n ≥ 1, and h(r, 0) − dim S_{1/2}(T̄ ⊗ ε_{24−r}) = χ_{3/2}(T ⊗ ε_r) with the dual counted numerically | 85% |
| P2′ | the field at r = 4, n = 0 is η⁴R. The kernel is ℂ·R exactly, compared to x⁶⁰, and its line orders are 1/24, 7/24 and 13/24 | 95% |
| P2″ | mirror hand: h̄(r, 0) = 0 at every r; h̄(r, 1) = 3 except h̄(20, 1) = 2; h̄(r, −1) = 0 (the duality formula); the numerical dimensions at n = 0 agree | 80% |
| P3 | F2: I = n·f + t_r on the whole box. The untwisted empty end cancels (I = 0) at every condition. At each natural condition, the least non-cancelling datum is unique and lies at the empty end: (0, r = 4, n = 0) and (L6, r = 20, n = 0), each with I = −1. At weave level Σ_r I = 6n·f − 1, so −1 at n = 0 at every condition | 90% |
| P4 | F3: the least line-bundle datum, n = 1, gives h = 3 and I = −3 (+3) at the canonical (mirror) condition. The least per-line datum, one unit on one line, gives h = 1 and I = −1, at the price of a chosen line (W123) | 95% |
| P5 | the read-out: for each form, whether the empty end is forbidden, the least datum it allows, its Higgs space in both hands, its chiral count, and its cost | — |

## What the outcomes mean (fixed now)

- **P0 to P4 hold.** Then:
  - **F1 forbids nothing.** The empty end is already frustrated, and F1 cannot see the end datum.
  - **F2 per datum forbids only the untwisted empty end.**
    - Its least non-cancelling datum is a flat order-6 twist at the empty end.
    - In the canonical hand that datum carries one weight-3/2 form, η⁴R, and one chiral generation.
    - In the mirror hand it carries no form: the one mode is an obstruction class, not a section.
    - F2 without least remainder forces no field, since n = −1 is non-cancelling and carries none.
  - **F2 at weave level forbids nothing.** The six twists together already give −1 at the empty end.
  - **F3 forbids the empty end by definition.** It is the unit postulate itself, and its least datum gives three.
  - **So no form of GENESIS PF1 that is not the unit restated forces three.**
    - Read on the index with least remainder, GENESIS PF1 forces a field in the canonical hand only: one form,
      η⁴R, and one generation.
    - That the result depends on the hand, which the record holds to be a convention, is itself a finding about the
      identification "Higgs = weight-3/2 section". It is recorded as a READING for W129.
- **P2 or P2′ fails.** The exact route and the record disagree. That is recorded, and nothing in P3 to P5 is read
  until it is resolved post hoc, labelled so.
- **P2″ fails.** The duality formula or the mirror's definition is wrong. It is recorded; the canonical hand's
  results stand.
- **P3's uniqueness fails.** The least datum is a set, not a point. It is recorded with the set, and the reading
  names the choice it costs.

## What stays out

- Per-line end data with twists, and non-flat twists other than O(nδ).
- Couplings, τ and masses.
- The consistency route (W128) and the comparison of framings (W129).

## Seen before the rule (disclosed)

- **Read:**
  - main's GENESIS v1.54 (§1, GENESIS FK10, GENESIS FK15) and its field meditation (S_THE_FIELDS_GENESIS on main);
  - W45 to W47 and W123 with their outputs, including W47's K2 to K4 tables. Those tables already show the index at
    n = 0 under every twist, and that M_{3/2}(T ⊗ ε₄) has dimension 1 while every other n = 0 space is zero.
- **By hand, from those tables:**
  - that form is η⁴R, since R has line orders ⅛, ⅜, −⅛ and η⁴ adds ⅙;
  - the weave total of −1 at n = 0;
  - the Riemann–Roch predictions in P2 and P2″;
  - the translation of a twist into per-line units.
- **No exact dimension under a twist, and no mirror dimension,** has been computed.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
