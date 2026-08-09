# THE CORNERSTONE CAMPAIGN — plan, and what it has already returned

cc3 audit seat, 2026-08-09. Gate 5-Q. Structure only. Nothing banked.

**The owner's ask:** what computations would confirm the derivation of the
Standard Model from this programme well enough to be an unbeatable cornerstone?

**The campaign's design principle**, and the reason it looks the way it does:
a cornerstone is not a result that is *consistent*. It is a result that
**could have come out otherwise and did not**. So every probe below tests
**specificity**, never consistency. Consistency has been tested for a year and
the programme has plenty of it.

---

## THE SPINE UNDER TEST

```
pi_1(m004)  -->>  2T  --McKay-->  E6  --cascade-->  [SU(3)xSU(2)xU(1)]/Z6
```

Everything after the first arrow is group theory that knows nothing about m004.
So **the derivation is exactly as strong as its first fact**: B266's "exactly
two surjections onto 2T", banked as the genuine object-specific arithmetic atom.

That is the load-bearing joint, and it had never been base-rate tested. B855, on
the record: *"the programme has never had a valid control, so 'generic vs
specific' has essentially never been TESTED."*

---

## PHASE A — computations run on this seat (deterministic, reproducible)

### A0 · Validation before anything (DONE)

The surjection counter reproduces B266 exactly. It returns 48 raw surjections
for m004; B266 counts orbits under Aut(2T). `|Aut(SL(2,3))| = 24` was computed
independently here — every automorphism constructed from a generating pair and
checked against the full multiplication table — giving 48/24 = **2**. The script
asserts this and refuses to report a base rate if it fails.

### A1 · The base rate, volume-ordered (DONE)

First 400 one-cusped census manifolds: **36.2 %** admit a surjection onto 2T;
**31.0 %** admit exactly two — m004's own count. Ties include **m003, m007,
m022, m026, m027, m029, m030**.

### A2 · The base rate, unbiased (DONE)

Random 3,995 drawn from all 203,123 one-cusped census manifolds:
**34.9 % admit a surjection; 24.2 % admit exactly two.** The volume-ordered
sample was not an artefact.

> **Result: the atom is generic.** Roughly one hyperbolic 3-manifold in three
> carries the fact the entire derivation begins from. This confirms E20/B727
> (m003 ties m004) and sharpens it from a two-manifold tie to a measured rate.

### A3 · The right reference class — knot complements (RUNNING)

m004 is a knot complement, and by **Reid** it is the *unique arithmetic* knot
complement in S³. So the honest reference class is not "all cusped manifolds"
but "knot complements", where the arithmetic set has size one. Sweeping all
3,116 of `snappy.CensusKnots()`.

**This is the sharpest single number in the campaign.** If 2T is still ~30 %
generic among knot complements, then arithmeticity — the object's one genuinely
unique property — does no work in the chain, and the cornerstone cannot be built
where the programme has been building it.

### A4 · Do m004's *two* surjections differ from everyone else's? (QUEUED)

The 24 % who tie m004 tie it on a *count*. Whether their two surjections carry
the same downstream structure (the same E₆ data, the same congruence behaviour)
is a different and finer question, and it is unrun. If m004's pair is
structurally distinguished, the atom is rescued at a finer resolution. If not,
the count result stands as the whole story.

---

## PHASE B — corpus probes (4 agents, running)

| probe | the question | why it decides something |
|---|---|---|
| **REID** | Does any step of the chain require *arithmetic knot complement*, or only *trace field ℚ(√−3)*? | B803 makes the trace field a **commensurability-class** invariant. If no step consumes Reid's uniqueness, the cascade is a statement about the Bianchi class PSL(2,O₃) and the ledger must say so. |
| **THREE BITS** | The measurement torsor is rank-saturated at **exactly 3** (B733/B766/B782). The cascade has **exactly 3** binary steps (B861/B862). Isomorphism or coincidence? | If each breaking is one of the three saturated bits, the cascade rule stops being an aesthetic choice and becomes a derivation from the object's own measurement structure. **This is the strongest cornerstone available if it holds.** |
| **EXOTICS** | E₆'s 27 = 16 + 10 + 1 leaves twelve exotic states per generation (L134); B978 proves no adjoint VEV can give any 27 fermion a mass. | A framework predicting twelve unobserved states with no mechanism to hide them is **falsifiable by its own internals**. A mechanism is a prediction; no mechanism is a refutation. Either is a cornerstone. |
| **RULE** | Is "largest registerable surviving symmetry" derived, or chosen because it lands on the SM? | B869's control tests *other starting groups with the same rule*. The question here is *the same starting group with other rules* — a different test, possibly never run. If the registerability filter alone leaves one option per step, the "largest symmetry" clause is decorative and the real result is stronger than stated. |

---

## PHASE C — synthesis

A single relay carrying: the verdict, the correction list (what the ledger
currently claims that the base rate contradicts), a ranked and costed list of
what would make the derivation unbeatable, and **the honest ceiling** — what
would still be out of reach even if every probe came back positive.

---

## THE CEILING, STATED IN ADVANCE SO IT CANNOT BE FORGOTTEN

Today's weight ledger established that the object is **scale-free**: every
quantity it owns is a pure number in units of its own curvature radius, and no
internal relation can fix that radius, on any face, emittance included. So even
a perfect result here would be a **structure** cornerstone — the gauge group,
its global form, the matter pattern — and never a mass, a coupling, or a scale.

That is not a small thing to have. It is simply not what a Theory of Everything
means, and the campaign should not be sold as one.

---

## STATUS

- A0, A1, A2 — **done**, committed under `frontier/B796_coupling_campaign/2t_base_rate/`
- A3 — running
- A4 — queued
- Phase B — 4 probes running
- Phase C — pending Phase B

— cc3
