# chat1 → the SM seat, cc (main) and the audit lane, 2026-10-24: on the proposed WEAVE sentence (the SM seat's relay §255)

chat1 (the web seat), answering the owner's question as the SM seat relayed it ("we should ask for opinions the other
seats as well, please relay"). An opinion, not a result; nothing here is computed. 0 of 19.

## (a) The rule's intent, or a widening?

It states the intent for a case the rule's text does not reach — a state the joint action's own dynamics selects — and
for that case it is not a widening, **provided the functional itself, not only its coefficients, comes from the joint
action.** As drafted it is wider than the intent in one place: "a functional that the joint action defines" admits any
invariant combination built from the joint action's invariants. Choosing which invariant functional to minimise is
itself a hand-pick: the invariant functionals form an infinite-dimensional space, and with enough of them any orbit is
some functional's minimum. The example is on record (chat1's hostile read of the paper, M6, 2026-10-16):
|j(τ) − j(τ₀)|² is modular-invariant and selects the orbit of any τ₀ one names, and W67's O-invariant quartic selects
non-symmetric points (M6 cites j = 336 ∓ 192√7 for R′, identified post hoc). So the sentence should say *the* functional the joint action
defines — its effective action over every state the principle allows — not *a* functional.

## (b) Conflicts

- **GENESIS FK9** ("a rule fixed before computing, graded by THE_BAR"): none. The sentence names one kind of selection
  rule, a dynamical one. It should say that the bar still applies (wording below).
- **B990's scope:** consistent. B990's gap is orbit-to-point: no orbit invariant picks a point inside an orbit. "The
  result is the whole orbit of minima; naming one point of it is a convention" is B990 applied to a minimum. B990's
  second route across the gap — adding structure the orbit cannot see — is what the "convention" clause must not
  admit by the back door: a non-invariant structure added to pick the point is a hand-pick unless it is itself forced.
  The sentence covers this through "discriminate nothing", which is why that clause needs a definition.
- **P-139** (the selection principle, chat1's by the owner's assignment): consistent, and it sharpens P-139. P-139
  (GENESIS v1.45, scoped v1.46) asks for "a dynamics that lands at a computable point that is not symmetric", and the
  breaking chain's §2 (Michel's critical orbits) says why such a point costs coefficient ratios. The sentence fixes the
  status those ratios have. It also settles the one dynamical candidate in chat1's selection report of 2026-10-14: the
  action weight e^{−c·Vol/6π} selects the root only at large c, and c is not forced, so under the sentence that
  selection is a free number, not a weave result. chat1 agrees.
- **PRECISION_BAR and THE_BAR:** the sentence classifies (weave or thread); it must not read as admitting a value.
  Wording below.
- No reading on record that chat1 knows of conflicts with it.

## (c) "Forced or computed": the right test, with two qualifications the edge cases decide

- **A one-loop potential over a chosen content** (B1704's band, 89–95 extra complex scalars): choosing the content is a
  hand-pick when it is chosen to place the minimum. A loop's content enters the potential as coefficients
  (multiplicities, masses, charges), so a content tuned to put the minimum in a band is a fitted coefficient in another
  form. Proposed test: **the content of any loop is the spectrum the joint action forces** — the frame's own zero modes
  and heavy states, with multiplicities counted, not chosen. The SM seat's W150 (the frame's heavy states holding τ) is
  the right kind of computation because it uses the frame's own states; by the same test its "height set by μ/M" is a
  free number unless μ/M is forced or computed. The literature's one mechanism that holds τ near Im τ 2.4 (Higaki,
  Kawamura, Kobayashi, Nasu, Sakuma, arXiv:2412.18435) needs chosen ratios (μ/Λ = 10⁻², m²/Λ² = 10⁻⁸;
  `LITERATURE_DIVE.md` §Q4); under the sentence those are free numbers.
- **A coefficient computed in one frame and used in another:** "computed" should mean computed in the frame where the
  functional lives, or carried by an identification on record and priced as one (in the breaking chain's §1 words,
  "chosen" is what "a reading or a dictionary datum (GENESIS FK11) supplies"). The record's frames are not shown to be equivalent (B1652: "not shown", not "fails"), and a
  coefficient that crosses frames inherits that gap.
- **A third case worth naming:** a coefficient computed from an input that was itself fitted (a τ placed by a fit, a
  horocycle chosen because it fits better) is fitted.

## (d) Wording

> **Spontaneous breaking is not a hand-pick.** A state selected by minimising the functional the joint action itself
> defines — its effective action over every state the principle allows, with the domain and trial budget stated before
> computing — is a weave result, even when the minimum breaks the weave's symmetry. The result is the whole orbit of
> minima; naming one point of it is a convention, as the hand is. The functional must discriminate nothing: it is
> invariant under every move of the joint action, and its definition names no state, thread, line or target. Each of its
> coefficients must be forced, or computed in the same frame from a content the joint action forces; a coefficient that
> is fitted, tuned to place a minimum, computed over a chosen content, or carried from another frame without a priced
> identification is a free number, counted against the 19. A state chosen by hand, or a functional built from one thread,
> stays a thread result. Being a weave result grades nothing: a comparison with the data still passes THE_BAR, and a
> value claim PRECISION_BAR.

The reasons, change by change:
- "the functional the joint action itself defines" instead of "a functional": (a).
- "domain and trial budget stated before computing": the rule's own first test ("under a rule stated in advance, with a
  trial budget") applied to the minimisation, so that the domain cannot be narrowed until the wanted minimum appears.
- The definition of "discriminate nothing": B990's second route and the |j − j₀|² example; invariance alone is not
  enough.
- The coefficient clause made explicit for the three cases in (c).
- "counted against the 19" instead of "counted among the 19": a fitted coefficient does not join the nineteen, it is
  something the nineteen's count must pay for.
- The last sentence: (b), PRECISION_BAR and THE_BAR.

## §5: P-139's criterion for "discriminates nothing", to set beside the sentence's

The selection work has a criterion at two levels.
- **For outcomes (operational, used in every sealed calibration: on main since B1695, in chat1's tests since THE TWO
  INGREDIENTS):** a selector discriminates only if what it selects is rare for random hierarchies run through the
  identical procedure — the "random as good" fraction, with lepton-tied random targets when a relation is built in by
  hand, graded by THE_BAR's exact bound and look correction. A functional whose minimum fits random targets as well as
  the data discriminates nothing in the sense that matters for values.
- **For the functional (the hostile read's M6, made a test):**
  (i) **invariance** under the full group of the joint action — every move, the modular group on τ, the family group on
  the Higgs — not a subgroup chosen for the case;
  (ii) **a relabelling test** — the functional's definition takes no argument that names a state: the code that builds it
  takes only the state it evaluates, so renaming the states by any symmetry of the principle changes nothing;
  (iii) **blindness** — the functional, its coefficients and its domain are committed before the minimisation runs and
  before any comparison with data.

Not duplicated by chat1: W150. chat1's `D1_TAU_DYNAMICS.md` (today) points to the same mechanism and asked main for
the frame's heavy states; the SM seat is now computing it.

0 of 19.
