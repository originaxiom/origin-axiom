# THE BASE-RATE CONTROL — the 2T atom is generic

cc3 audit seat, 2026-08-09. Gate 5-Q. Structure only; no physical constant
appears. Nothing promotes.

## Why this was run

The owner asked what computations would confirm the derivation of the Standard
Model well enough to be an unbeatable cornerstone. The chain is:

```
pi_1(m004)  -->>  2T  --McKay-->  E6  --cascade-->  [SU(3)xSU(2)xU(1)]/Z6
```

Everything after the first arrow is group theory that knows nothing about m004.
**The one object-specific fact carrying the whole derivation is the surjection
onto 2T** (B266: "exactly two surjections", banked as the genuine
object-specific arithmetic atom).

So the derivation is only as strong as that atom is rare. B855, on the record:
*"the programme has never had a valid control, so 'generic vs specific' has
essentially never been TESTED."* This is that control.

## Method, and its validation

2T = binary tetrahedral = SL(2,3), order 24, built explicitly. For a census
manifold, take the SnapPy presentation of π₁ and enumerate **every** map from
generators into 2T, keep those satisfying all relators, and keep those whose
image is the whole group. Surjection counts are a property of the group, not of
the presentation.

**Validation before any census number was believed.** The counter returns 48
raw surjections for m004, against B266's "exactly two". The discrepancy is
convention: B266 counts orbits under Aut(2T). |Aut(SL(2,3))| was computed
independently here — by constructing every automorphism from a generating pair
and checking it against the full multiplication table — and equals **24**. So
48 / 24 = **2**, reproducing B266 exactly. The script asserts this and refuses
to report a base rate if it fails.

## The result

First 400 one-cusped census manifolds (ordered by volume):

| | count | share |
|---|---|---|
| swept | 400 | — |
| admit **≥ 1** surjection onto 2T | 145 | **36.2 %** |
| admit **exactly 2** — m004's own count | 124 | **31.0 %** |

Distribution: 0 → 63.75 %, **2 → 31.00 %**, 4 → 3.50 %, 6 → 1.00 %,
10 → 0.50 %, 12 → 0.25 %.

Other manifolds with exactly two surjections onto 2T:
**m003, m004, m007, m022, m026, m027, m029, m030, …**

## What this means

**The atom is not an atom.** B266's "exactly two surjections onto 2T" — the
fact the programme treats as m004's own — is shared by roughly **one hyperbolic
3-manifold in three.** Not by its sister alone, as B727/E20 already found; by a
third of the census.

Every consequence downstream inherits this. 2T → E₆ is McKay, which is a fixed
correspondence. E₆ → SO(10) → SU(5) → SM is the cascade, which is group theory.
None of it can be more object-specific than the atom it starts from. **So the
cascade, as currently derived, selects roughly a third of the census — not
m004.**

This confirms E20/B727 and sharpens it from a two-manifold tie to a measured
base rate.

## What this does NOT kill

- **The cascade itself.** E₆ → … → SM, unique at each step with ℤ₆ forced
  (B861/B862/B864) and a non-vacuity control (B869), stands as banked. It is a
  theorem about **E₆**, and it remains one. What it is not is a theorem about
  m004.
- **Reid's uniqueness.** m004 *is* the unique arithmetic knot complement in S³.
  That is a genuine uniqueness theorem and it is not base-rate.

**The gap between those two bullets is the whole problem.** The object has a
genuinely unique property (arithmetic **and** a knot complement). The
derivation does not use it: the chain runs through the trace field, which B803
established is a **commensurability-class** invariant. So the load-bearing
property is shared by a class, while the unique property is load-bearing
nowhere.

## The cornerstone computations this identifies

Ranked. A cornerstone must rest on something **not** shared by 31 % of the
census, so every item below is a test of specificity, not of consistency.

1. **Does arithmeticity correlate with the 2T surjection at all?** Re-run this
   control split by arithmetic / non-arithmetic. If the 31 % is indifferent to
   arithmeticity, then m004's one unique property is decorative in this chain
   and the derivation needs a different starting fact. **Cheap; decisive; run
   it next.**
2. **Make Reid's uniqueness load-bearing, or admit it is not used.** Find a step
   in the chain that requires *arithmetic knot complement*, not merely *trace
   field ℚ(√−3)*. If no such step exists, say so in the ledger — the cascade is
   then a statement about the Bianchi class PSL(2,O₃).
3. **Is the cascade's rule forced or chosen?** The rule is "among registerable
   options take the largest surviving symmetry." Enumerate rules of comparable
   simplicity and count how many also land on the SM. Then the sharp version:
   B766 proves the measurement torsor is **rank-saturated at exactly 3**, and
   the cascade has **exactly 3 steps**. Is that an isomorphism or a coincidence?
   If the three breakings are the three bits, the rule stops being an aesthetic
   choice and becomes a derivation.
4. **Resolve the exotics tension, which is a live falsification risk.** E₆'s
   27 = 16 + 10 + 1 leaves twelve exotic states per generation (L134), and B978
   proves **no adjoint VEV can give any 27 fermion a mass**. A framework that
   predicts twelve exotics and has no mechanism to make them heavy is
   falsifiable *by its own internals*. Either outcome is a cornerstone: a
   mechanism is a prediction, no mechanism is a refutation.
5. **The deep-precision value test.** Cell 9 rung (i) at 25 digits — already
   pre-registered before the eigenvalues existed, so running it executes the
   seal rather than extending it. B798's power law says 8 digits had no
   exclusion power; 25 does.

## Honest scope

400 manifolds, one-cusped, in census (volume) order — so the sample is biased
toward small volume. A random 4000-manifold sweep across the full 203,123 is
running; this file will be updated with it. Presentations with more than three
generators were skipped (none occurred in this sample). The count is of
surjections onto 2T only; it says nothing about the *further* structure the
programme derives from the two specific surjections m004 admits, which may yet
differ from the other 31 % — **that is exactly item 1 above, and it is unrun.**

Reproduce: `python3 base_rate_2T.py --n 400` (asserts the B266 validation first).
