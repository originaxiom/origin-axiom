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

### PRIOR ART — B727 got here first, and this arc understated it

**Correction, made on this seat before the result was relayed.** The text above
originally described B727 as finding "m003 ties m004", a two-manifold tie. That
understates it. B727 (banked 2026-07-20) already ran this control and already
drew this conclusion:

> *"**NEW computed fact (strengthens the negative): π₁ ↠ 2T is NOT unique to
> the arithmetic knot.** 4/13 hyperbolic knots surject onto 2T = SL(2,𝔽₃),
> **including the non-arithmetic 7₂, 7₃, 8₁**. So even the 2T surjection is
> shadowed by non-arithmetic knots; what is object-specific is only the
> arithmetic *origin*, not the surjection."*

4/13 = 30.8 %, against the 36.4 % measured here on 3,112 knot complements.
**B727's answer was already right.** This arc's contribution is sample size —
n = 13 → n = 3,112, a 240× extension that moves the claim from "suggestive on a
small set" to "settled" — plus the general-census figures and the
Aut(2T)-validated counter. That is worth having; it is **not** a new finding,
and this file will not present it as one.

Recording the near-miss deliberately: declaring open what was already banked is
the failure this seat spent the morning auditing in cc's ledger. It very nearly
committed it here.

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

## The unbiased confirmation (added after the random sweep completed)

A random sample of **3995** drawn from all **203,123** one-cusped
census manifolds, seed 20260809:

| | count | share |
|---|---|---|
| admit ≥ 1 surjection onto 2T | 1396 | **34.9 %** |
| admit exactly 2 — m004's count | 966 | **24.2 %** |

Skipped 5 presentations with more than three generators. The
volume-ordered figure (36.2 % / 31.0 %) was therefore **not** an artefact of
sampling small manifolds. The "admits a surjection" rate is stable at ~35 %;
the "exactly two" rate falls from 31 % to 24 % in the unbiased sample, because
larger manifolds tend to admit more surjections — which sharpens rather than
softens the finding: m004's count is not even a local maximum of rarity.

## A3 — THE RIGHT REFERENCE CLASS, AND IT SETTLES ITEM 1

m004 is a **knot complement**, and by **Reid** it is the *unique arithmetic*
knot complement in S³. So the honest comparison class is not "all cusped
manifolds" but **knot complements**, where the arithmetic set has size exactly
one. If arithmeticity were doing any work in producing 2T, it would show here.

All **3112** of `snappy.CensusKnots()` (4 skipped, >3 generators):

| | count | share |
|---|---|---|
| admit ≥ 1 surjection onto 2T | 1207 | **38.8 %** |
| admit **exactly 2** — m004's count | 1134 | **36.4 %** |

Examples sharing m004's count: `K2_1`, `K4_2`, `K5_1`, `K5_2`, `K5_4`, `K5_8`, `K5_11`, `K5_12`, …

**Restricting to the class where m004 is unique makes the atom MORE generic,
not less** — 36.4 % versus 24.2 % across all cusped manifolds. Being a knot
complement raises the odds of carrying the fact the derivation starts from.

**This settles cornerstone item 1, negatively.** Arithmeticity does no work in
the chain. m004's one genuinely unique property is not what produces the
surjection onto 2T; more than a third of knot complements produce it without
being arithmetic at all.

### One genuine structural difference, worth recording

Among knot complements the surjection count takes **only the values 0, 2 and
10** — never 4, 6, 8, or the higher values seen across the general census
({0, 2, 4, 6, 8, 10, 12, 14, 16, 20, 22}). Distribution: 0 → 1905,
2 → 1134, 10 → 73.

That quantisation is a real fact about knot groups (H₁ = ℤ constrains where the
meridian can go) and it is **not** something this arc set out to find. It does
not rescue m004 — m004 sits in the modal class of 1,134 — but it is a clean
unregistered observation about the reference class, and someone should take it.

## Honest scope

The 400-manifold run is in census (volume) order and biased toward small
volume; the 3995-manifold run above removes that bias. Presentations with more than three
generators were skipped (none occurred in this sample). The count is of
surjections onto 2T only; it says nothing about the *further* structure the
programme derives from the two specific surjections m004 admits, which may yet
differ from the other 31 % — **that is exactly item 1 above, and it is unrun.**

Reproduce: `python3 base_rate_2T.py --n 400` (asserts the B266 validation first).

---

# THE CONJUNCTION SWEEP — the specificity is real, and the derivation does not use it

The cornerstone synthesis's #1 recommendation: stop asking about the atom and
ask about the **conjunction** — trace field ℚ(√−3) **and** exactly two 2T
surjections **and** H₁ = ℤ. Run here.

**Method caveat — and it was wrong in the stated direction; corrected below.**
Sage was unavailable when this first ran, so the trace-field test was numeric:
sampled holonomy traces `tr = x + iy` tested for `x ∈ ℚ` and `y/√3 ∈ ℚ` at
bounded denominator. I wrote that this **over-counts**. **It under-counts.**
The proxy tests the *generator* trace field; the invariant trace field is
*contained* in it, so a manifold can have invariant trace field ℚ(√−3) while
some generator trace lies outside — the proxy then says no and the exact answer
is yes. Measured below: **0 false positives, 4 false negatives in 400.**

## Results

**One-cusped census, 4,000 manifolds:**

| condition | count | share |
|---|---|---|
| exactly two 2T surjections | 1,020 | 25.5 % |
| H₁ = ℤ | 2,473 | 61.8 % |
| **trace field ⊆ ℚ(√−3)** | **7** | **0.18 %** |
| all three | **1** | **m004 alone** |

**All 3,112 census knot complements:**

| condition | count |
|---|---|
| exactly two 2T surjections | 1,134 |
| H₁ = ℤ | 3,112 (all — they are knots) |
| **trace field ⊆ ℚ(√−3)** | **1** |
| all three | **1 — `K2_1`, verified isometric to m004** |

## What this establishes, precisely

**The rare condition was never 2T. It is the trace field.** 2T is carried by a
quarter to a third of everything; ℚ(√−3) by 0.18 % of the census and by
**exactly one knot complement in 3,112**.

And that one knot is m004. **This is Reid's theorem appearing as a measurement**
— m004 is the unique arithmetic knot complement in S³ — recovered here
independently, from census data, without assuming it.

## Why this does NOT rescue the derivation, and what it does instead

Two things must not be conflated:

1. **m004 is genuinely unique** in the conjunction *knot* ∧ *ℚ(√−3)*. Measured
   above; Reid proved it.
2. **The derivation does not use that conjunction.** The REID probe traced every
   step and found knot-ness consumed nowhere: B266's arithmetic route consumes
   ℤ[ω]; McKay consumes a finite subgroup of SU(2); the cascade
   (B861/B862/B864) consumes nothing from the object at all. The chain runs on
   the **trace field alone**, which B803 established is a
   **commensurability-class invariant**.

So the specificity is real and it is sitting **one condition away from the
chain that needs it.** Conditioning on the trace field selects the Bianchi
class PSL(2,O₃) — m003, m206 and infinitely many others. Adding H₁ = ℤ cuts
that to m004 alone. The derivation adds the first condition and never the
second.

**That is the cornerstone opportunity, stated exactly:** find a step that
consumes **H₁ = ℤ** (or knot-ness in S³) and the derivation inherits Reid's
uniqueness. Until such a step exists, the cascade is a theorem about the class,
and m004's uniqueness is a true fact the argument never touches.

Note the shape of this: it is the *same* finding as B727's — *"the SM-resonance
is the field's, the arithmetic-knot uniqueness is the knot's; they live on
different objects and do not reinforce each other"* — now with both sides
measured. B727 said it in prose in July; this is the census behind it.

## THE EXACT RE-RUN — Sage installed, proxy validated, conjunction confirmed

Sage 10.7 was installed (micromamba env `sage`) with SnapPy 3.3.2 alongside it,
removing the blocker B735 recorded as *"no Maass eigenvalue computed — Sage
unavailable"*. The **exact invariant trace field** is now computable:

    m004 invariant trace field = x² − x + 1  →  ℚ(ζ₆) = ℚ(√−3)   ✓

**Proxy vs exact, 400 one-cusped census manifolds:**

| | |
|---|---|
| agree | 396 / 400 (99.0 %) |
| **false positives** | **0** |
| false negatives | 4 — `m208`, `m410`, `s118`, `s119` |
| undecided (`find_field` failed) | 325, skipped |

Zero false positives is the load-bearing number: **every manifold the proxy
flagged genuinely has invariant trace field ℚ(√−3)**, so the conjunction's
survivor list is sound. The four false negatives mean the *ℚ(√−3) column* was
an under-count — which cannot add survivors, because all four carry H₁ torsion.

**The eight exact ℚ(√−3) manifolds in that slice, with their homology:**

| manifold | volume | H₁ |
|---|---|---|
| m003 | 2.029883213 | ℤ/5 + ℤ |
| **m004** | **2.029883213** | **ℤ** |
| m206 | 4.059766426 | ℤ/5 + ℤ |
| m207 | 4.059766426 | ℤ/3 + ℤ/3 + ℤ |
| m208 | 4.059766426 | ℤ/10 + ℤ |
| m410 | 5.074708032 | ℤ/2 + ℤ |
| s118 | 4.059766426 | ℤ/2 + ℤ |
| s119 | 4.059766426 | ℤ/2 + ℤ |

**Exact invariant trace field ℚ(√−3) ∧ H₁ = ℤ → `m004` alone.**

Every other member of the class carries torsion in H₁, and a knot complement in
S³ has H₁ = ℤ exactly — so none of them can be a knot. That is the mechanism
behind Reid's theorem, visible in one column of a table, and it is now
established here with exact arithmetic rather than a numerical proxy.

It also sharpens the conclusion above rather than changing it: **H₁ = ℤ is the
condition that isolates m004 inside its own commensurability class, and it is
the one condition the derivation never consumes.**

Reproduce: `python3 conjunction_sweep.py --n 4000` and `--knots --n 3200`
(numeric, fast); `exact_trace_field.py --n 400` inside the `sage` env with
`PATH=$MAMBA/envs/sage/bin:$PATH` so Singular resolves (exact, slow).
