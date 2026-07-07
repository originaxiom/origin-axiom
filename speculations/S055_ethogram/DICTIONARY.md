# S055 — THE ETHOGRAM: the ethological dictionary (E0 card deck)

**Status: POSTULATED (campaign frame), owner-approved full ethological frame. Firewalled one-way;
biology names are a LENS on banked mathematics; nothing here promotes. Campaign:
`docs/OPEN_LEADS.md` §"The Ethogram campaign"; prereg: `frontier/B452_ethogram_dictionary/`.
Rule (binding): a card that fails its falsifier is RETIRED — logged, never patched.**

Every card: **definition in the object's dynamics · the computation that measures it · the
falsifier that would kill the mapping**. Two tiers: DESCRIPTIVE (banked facts wearing
ethological names; falsifier = a forward prediction that must hold at the next level/order) and
DECISIVE (open computations). Disanalogy lines are stated where the metaphor is weakest — they
are the deck's armor, not its embarrassment.

---

## Tier 1 — DESCRIPTIVE cards

### birth
- definition: the forced closure chain σ → abelianization → monodromy → mapping torus → 4₁ →
  hyperbolic structure → ℚ(√−3) — canonical at every step (banked, B449; Chat-1's caveat
  recorded: *which functor to apply* is ours; each construction is unique once chosen).
- computation: banked (B449 `conductor_law.py`; the forcing-chain record).
- falsifier (forward): the same chain run on any other admissible seed word must land on the
  corresponding bundle with zero choices — checked whenever a new seed is introduced.

### growth
- definition: the substitution's iteration; age = level; growth rate = the Perron–Frobenius
  eigenvalue λ (a theorem, not an observation).
- computation: per-level word statistics (machinery: B156/B163/B417/B448).
- falsifier (forward): the level-(L+1) statistics predicted from level-L via PF must hold
  exactly; any deviation kills the card (and would be a sensation).
- disanalogy: growth without nourishment — nothing is consumed.

### metabolism (the beats)
- definition: the object's internal periodic activity — the four banked pulses (the cocycle
  2-cycle; the Pisano SFF revival; the log-periodic C(T); the orbit tower on the Markov locus).
- computation: banked (B446/B447/B448); mechanisms distinct, kept apart.
- falsifier (forward): each pulse predicts its next beat (the next tower level's revival time
  π(N)/2; the next orbit period's eliminant) — checked whenever the tower/period is extended.
- disanalogy: a metabolism that consumes nothing — the dynamics is conservative, dissipation-free.

---

## Tier 2 — DECISIVE cards

### reproduction & heredity
- definition: forced emission of a new object by self-application (the surgery move: 4₁ → the
  forced ±5 filling → the child 4₁(5,1)).
- computation: banked one round (B434–B443); the open cell = the cover-lineage (E1: the ℤ/5
  cyclic cover of the child — b₁, torsion, the virtual-fibering degree).
- falsifier: "a parent-unique heritable invariant exists" — **status: already TESTED-NEGATIVE
  (B443, the Inversion Law)**. The honest card: *the object reproduces exactly once by surgery,
  WITHOUT heredity; the offspring is congenitally sterile* (closed ⇒ Weil-rigid ⇒ no moduli, no
  cusp, no further filling).
- disanalogy (the deck's most attackable point, pre-empted): **no heredity ⇒ no Darwinian
  anything** — no selection, no adaptation, no evolution in the biological sense. The lineage
  continues only *virtually* (Agol's theorem — a background fact, not an observation).

### homeostasis (restoring response)
- definition: perturbed off its conserved surface (the κ level set), does the dynamics RETURN?
- computation: E3-adjacent — perturb (x,y,z) off κ=−2, iterate, measure the κ-distance profile.
- falsifier: built in — if the dynamics does not return (expected: it does NOT; conservative
  systems have no attractor transverse to the invariant), **the card retires with a
  computation**, which is exactly how the frame is supposed to work. [The v1 version —
  "homeostasis = κ conservation" — was an unfalsifiable rename; killed at red-team.]

### exhaustion / end of evolution
- definition: a channel is exhausted when its new invariants at the next round are all
  whitelist-derivable (the burden-inversion test applied per round).
- computation: E2 — the closure LEMMA (primary; one induction over the B448 recursion) + the
  bounded counterexample scan (L=8, secondary).
- falsifier: a non-whitelist structure at any level ≤ 8 (fires the escalation bin); the lemma
  failing to close while the scan stays clean = UNDECIDED-AT-DEPTH-8, reported as such.

### response (stimulus → behavior)
- definition: what the object DOES under graded perturbation — finite deformation along its six
  E₆ moduli directions; filling as external stimulus.
- computation: E3 — integrate the five non-geometric directions (landing-verdict taxonomy:
  COMPONENT-FOUND / WALL / OBSTRUCTED-AT-ORDER-k / DIVERGENT); the geometric direction = the
  known A-polynomial curve = the gate.
- falsifier: per landing verdict — an inadmissible outcome ("nothing happened") retires the run,
  not the card; the card dies only if no direction admits ANY classified landing.

### choice vs compulsion
- definition: at each generative step, is the next move FORCED (unique canonical continuation)
  or a genuine bifurcation (feedback-dependent choice)?
- computation: E2's per-level forcing analysis (the B449 method applied per round). The
  chain-level answer is banked: forcing runs through the seam field; genuine choice enters at
  L57 (representation/pairing/theta).
- falsifier: a step claimed forced that admits a second inequivalent continuation (or vice
  versa) — auditable per step.

---

## The cards the frame demands (new)

### environment
- definition: the ambient class the object lives in — the m-family / word space / knot census /
  the ambient E₆ variety. **"Probing outside" ≔ producing structure not derivable from
  whitelist + class data.** (This types E2's headline and makes "stimulus-response" coherent:
  stimuli come FROM the environment; responses are measured against it.)
- computation: the null ensembles ARE the environment sampled (random words n≥1000, Thue–Morse,
  foreign knots, silver/bronze).
- falsifier: an "outside" claim that an environment-sample also exhibits (kills object-specificity).

### death / the end
- definition: the honest card — **the object cannot die.** The dynamics is conservative and
  reversible; nothing decays. Evolution ends only by exhaustion-of-novelty (the closure lemma),
  never by cessation.
- computation: E2's verdict is this card's content.
- falsifier: none needed — the card asserts an absence and is retired if E2 finds decay-like
  behavior (it will not; that would itself be a sensation).
- disanalogy: "senescence" is wrong everywhere here — the child's sterility is congenital
  (rigidity from birth), not acquired.
