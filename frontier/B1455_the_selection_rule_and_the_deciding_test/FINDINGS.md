# B1455 — THE SELECTION RULE, AND THE TEST THAT DECIDES IT ON THE BRIDGE'S VACUA: the count is unchanged by every symmetry of the manifold, mirrors included, and odd only under dualising; on Ballas' family dualising is the knot's own inversion and sends q to 1/q; every vacuum is fixed by a count-odd symmetry, so the index is zero on the whole family — the vacuum does not select

**Date:** 2026-10-02 · **Seat:** cc (main) · **Sealed** at `12ed66bd` before any computation on the population.
**Source of the question:** the web seat's handoff "The selection rule, and the one test that decides it" (zip sha256
`655959b2…e69499`, handed over by the owner; not tracked). **Verdict: NEGATIVE** — the kill condition registered in the
seal: no spontaneous selection of the count on this family. **Scope:** frame F-HE · object m004's harmonic family ρ_q
(Ballas, q > 0) at level one, with any central twist · reach single · hypotheses: the minima of the action are the
reductive points (the audit lane's R76 with Corlette's theorem as it cites it; not re-derived here). **0 of 19.**

## 0. Seen first

- **Repo.** `topic_sweep.py "spontaneous|symmetry.breaking|SSB|mirror.{0,30}(pair|orbit|minim|vacu)|selector|selects
  one|invariant selector|plenitude|totalitarian" --refs`: *VERDICT topic-sweep: 62 of 1326 arcs on main match
  (NEGATIVE 11, OPEN 6, PROVED 44, RETRACTED 1); 6 other lanes match.* Read at verdict-line level: B128, B295, B849,
  B853, B1204, B1222, B1225, B1227, B1327. The rule is on the record (B1227, B1225, B849, B1327); the test was not.
- **Repo, a second sweep, made after the run and in the record's own vocabulary** — the first used the handoff's
  words and missed this. `topic_sweep.py "two chiralit|theta-odd|theta.{0,20}(27|dual|even)|c vs theta|27.{0,12}27-?bar|
  charge conjugation"`: *VERDICT topic-sweep: 75 of 1327 arcs on main match (NEGATIVE 11, OPEN 3, PROVED 61).* Read:
  B576, B582, B868, B871. **The record already separates the two involutions:** the linear exchange of a
  representation with its conjugate (27 ↔ 27̄; B868's C, X ↦ −Xᵀ) and the antilinear mirror c, which "appears nowhere
  in the cascade" (B868); and a registering measurement is odd under the first (B871). §1's L2 is that statement for
  the class index. What is new here is L1 as a computed fact about the index (a mirror leaves the count unchanged),
  L3's use as a proof of vanishing, and what the two involutions do to the bridge's vacua.
- **The audit lane, at `64a96ea6`**, read and not re-derived: R47 and R54 (an exact S(q) with ρ_q(g)^{−T} S =
  S ρ_q(θg), θ inverting both generators; the longitude traces; "the classical minima are non-isolated"), its open
  checkbox of 2026-09-25 ("Test base-isometry plus duality before claiming unequal mirrors"), R76 (the potential along
  the non-split extension is a·t² + c·t⁴, a ≥ 0, c > 0; a stationary flat point of finite energy is harmonic), R57.
- **Literature.** Ballas, arXiv:1403.3314v3 (sha256 `36f54787…fba40`): pp. 1–2 and 17–19 read as pages, all 21
  text-searched for "dual" and "orientation" — the generators, the hyperbolic point t = ½, the longitude, the ρ_s
  pairwise non-conjugate; **nothing on duality or on the knot's symmetries acting on the family.** Pantev–Wijnholt,
  arXiv:0905.1968, through a machine summary only (the flat complex connection A + iφ, the D-term, the Chern–Simons
  superpotential). Not read: Ballas–Long, Cooper–Tillmann, Corlette, Donaldson.

## 1. Which mirror: three lines that the test turns on

For a local system V on M and σ induced by a self-homeomorphism of M:

- **L1.** I(σ*V) = I(V), whether σ preserves orientation or not.
- **L2.** I(V*) = −I(V).
- **L3.** If V* ≅ σ*V for some such σ, then I(V) = 0.

So **the geometric mirror does not change the count; dualising does.** The symmetry under which the count is odd is
Θ_σ(V) = (σ*V)*: a symmetry of the manifold followed by the exchange of a module with its dual. Confirmed at 60 digits
(`followup_index.py`, gaps 0.08 against 10⁻⁵⁷): at q₀ = 17 + 12√2 with the twist −1, I(W₁) = −1; pulled back by the
inversion, by the swap and **by a mirror** it is −1, −1, −1; on the three count-odd images it is +1, +1, +1; and
I(A) = 0 on the reductive module under all six.

## 2. The test (sealed C0–C2), by two routes that share no code

Route 1 (`mirror_on_the_family.py`): traces of all 2 046 positive words to length ten, exact rationals at q = 2, 3,
5/2, 7/3, 1/5, and symbolically on words to length four. Route 2 (`route2/`, written by a separate implementer from
the sealed file alone): the space of intertwiners, exact, and for the inversion symbolically in q.

| | Route 1 | Route 2 |
|---|---|---|
| C0: ρ_q ≇ ρ_{1/q} and ρ_q ≇ ρ_q* off q = 1; all four targets agree at q = 1 | yes | yes |
| **ρ_q* ≅ ρ_{1/q}** | at five q; symbolically to length 4 | at five q; an explicit X(q), det = 256(q+1)¹⁶/q¹⁴ |
| the eight signed permutations of (m, n) that are automorphisms | **four**: identity, swap, ι, swap∘ι | the same four |
| their orientation | **all four preserve it** | all four preserve it |
| identity, swap: ρ_q∘σ ≅ | ρ_q (and ρ_{1/q}*) | the same |
| ι, swap∘ι: ρ_q∘σ ≅ | ρ_q* (and ρ_{1/q}) | the same; (ρ_q∘ι) ≅ ρ_q* by an explicit X(q), det = −(q+1)¹²(q+2)⁸(q²+q+1)³/(256 q¹⁵), non-zero for every q > 0 |
| a symmetry taking the family outside itself | none | none |

**The scoreboard against the seal.**

| | prediction | prior | result |
|---|---|---|---|
| P1 | all eight maps are automorphisms, four reversing orientation | 70% | **FAILED.** Four are automorphisms and all four preserve orientation. The mirrors are not signed permutations of Ballas' generators |
| P2 | (ρ_q∘ι)* ≅ ρ_q for every q | 95% | held, for every q > 0 |
| P3 | ρ_{1/q} ≅ ρ_q* | 65% | held, for every q > 0 |
| P4 | among the mirrors one kind fixes every vacuum and another exchanges q and 1/q | 55% | held — **outside the sealed population** (§3) |
| P5 | I(A) = 0, I(W₁) = −1, I(ι*W₁) = −1, I(Θ_ι W₁) = +1 | 95% | held |
| P6 | outcome A | 85% | **outcome A** |

## 3. Post-seal extension, labelled: the mirrors

Because P1 failed, the sealed population contained no bare mirror. They were then found by search
(`mirror_extension.py`: m ↦ m^{±1}, n ↦ a conjugate of a generator by a word of length ≤ 4, with the SL(2,ℂ) character
complex-conjugated; 152 such maps, 122 orientation-preserving ones as a control). **Every one falls in one of two
classes** — on words to length six for all of them, to length ten for a mirror of the first class, and by exact
intertwiners for both classes in Route 2:

- mirrors that keep the longitude, e.g. τ: m ↦ m⁻¹, n ↦ n⁻¹m⁻¹n — **ρ_q∘τ ≅ ρ_q: they fix every vacuum**;
- mirrors that invert it — **ρ_q∘τ ≅ ρ_{1/q}: they exchange q and 1/q**, fixing only the hyperbolic point.

Route 2 found the same two classes independently, with words to length three. So the eight symmetries of the
figure-eight complement act on the family through one bit — *does the symmetry invert the longitude?* — and that bit
is the same as dualising.

## 4. The outcome, and what it proves

**Outcome A, the registered kill.** For every q > 0, Θ_ι fixes ρ_q. A central twist μ is inverted by ι and restored by
dualising, so Θ_ι fixes μ ⊗ ρ_q as well, and with it every module made from ρ_q by an operation that commutes with
duals. By L3:

> **On the harmonic family, every reductive module μ ⊗ S(ρ_q) — any character μ, any Schur functor S, any q > 0 — has
> class index zero.**

This is a proof, from two exact identities in q and three lines; it is not a census of zeros. The configurations that
count ±1 (the non-split extensions of sm:B1509, re-derived in B1453) are not fixed by any Θ — they cannot be — and by
the audit lane's R76 they are not minima. **So on the one family where the record has an action with a finite-energy
vacuum, the vacuum is fixed by a symmetry under which the count is odd. This potential does not select a handedness.**

It also pays the audit lane's open checkbox: base isometry plus duality fixes every vacuum, exactly, for two of the
four rotations and two of the four mirrors; the other four send it to the vacuum at 1/q.

## 5. Two corrections to the rule as the handoff words it

- **"A construction symmetric under the mirror gives zero net chirality" is false for the geometric mirror.** The
  counted configuration W₁ at q₀ is conjugate to its own pullback by the mirror τ (`mirror_fixes_the_counted_one.py`:
  a one-dimensional space of intertwiners with an invertible member) and counts −1. The rule holds with "mirror" read
  as Θ: a symmetry followed by dualising. In the handoff's own table the algebraic rows already use that reading
  (real, unitary, rational modules are self-dual); the geometric rows need it too.
- **The family is not "all minima mirror-fixed" in the literal sense of the handoff's step 4.** Half of the symmetries,
  one kind of mirror among them, are broken by every vacuum with q ≠ 1 and kept only by the hyperbolic one. That
  breaking is real and it is not a breaking of the count.

## 6. The handoff's side claims, recomputed (`handoff_claims.py`)

| claim | here |
|---|---|
| the fixed point of a → ab, b → a is the Sturmian word of slope 1/φ² at nine intercepts | yes: the intercepts j/φ², j = 1 … 9, give the fixed point shifted by j − 1, over 80 letters; a control slope is not found |
| \|A¹⁰v_u\| = 15127.0, \|A¹⁰v_s\| = 6.6·10⁻⁵ | φ²⁰ = 15126.99993, φ⁻²⁰ = 6.61·10⁻⁵ |
| conjugators of A to A⁻¹ occur with both determinants | yes: 6 of determinant 1 and 8 of determinant −1 with entries to 3 (the handoff's 22 is for a box it does not state) |
| π₁(m004) has no surjection onto SL(2, 𝔽₅); m202 has 1440, 24 up to conjugation | 0 of 600 homomorphisms; 1440 of 3000, 24 up to conjugation (its "12 up to Aut" not computed) |
| plenitude: the mean over all choices is zero | yes, exactly, and trivially |
| its eight-row table "8 predictions, 8 correct" | not scored here: its rows were not re-checked one by one. With the correction of §5 its classification column changes meaning, and at least one row rests on a seat arc main has not verified (sm:B1500) |

The handoff's own grading — "not new mathematics; its value is operational" — stands, and so do its five withdrawals.

## 7. What it means for the measurer question (firewalled; lead L241)

The owner, the same day: the derivation keeps dropping the measurer; are the choices binary; are both true at once;
are both needed in different places; does "what can happen, happens" hold. **This section is a reading. Nothing in it
is a result beyond §1–§5.**

| the thought | what the computation says | status |
|---|---|---|
| the measurer is dropped somewhere | the count is blind to every symmetry of the space, mirrors included, and sees only which of a module and its dual is read as "the particle". That choice is a marking, and every class invariant forgets markings | computed (L1–L3, §5) |
| both of a pair are true at once | the family holds the vacuum at q and the one at 1/q; each is the other's dual and the other's image under the inversion. Neither is preferred by the action | computed (§2) |
| both are needed in different places | half the symmetries are kept by every vacuum and half are broken by every vacuum but one. The kept half and the broken half each contain a mirror | computed (§3) |
| what can happen, happens | over a pair {x, Θx} the count sums to zero. A world with a count is one member, and which member is not a fact about the pair | L2; a reading beyond that |
| the choice is made by a relation, not by the object | no computation here. B1327 is the record's statement that the theorem forbids a self-selector and nothing else | open |

## 8. The fence

One frame, one family, one level. "The vacuum does not select" is a statement about reductive points of this family
under the hypothesis that minima are reductive. It is silent on other states, other frames, a source, the ends, and
quantum effects, and it does not say that no relation selects. The audit lane's R76 is read, not re-derived. L3 is a
criterion for vanishing, not a classification: a reductive module that is not fixed by any Θ is not excluded by it
and none is known on this family.

## 9. Not done (lead L242)

Whether L3 accounts for the zeros already on the record: B1451's 188 doubly parabolic points and B1447's sixteen
non-self-dual modules with index zero (is each fixed by some Θ_σ?) — which would turn R58-6's vanishing statement into
a proof on those populations. The same test on the levels M₃ to M₆, where the seats count on covers. The handoff's
"12 up to Aut".
