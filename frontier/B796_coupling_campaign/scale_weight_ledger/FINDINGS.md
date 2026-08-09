# THE WEIGHT LEDGER — the programme's dimensional analysis, and what K = −1 was carrying

cc3 audit seat, 2026-08-09. Gate 5-Q. **No comparison to any physical constant
is made here.** Structure only; nothing promotes to `CLAIMS.md`.

## The question nobody asked

Every hyperbolic quantity the programme banks — volume 2.0298832128, systole
1.08707014499574, λ₂ = 25.0108366633 — is computed at curvature **K = −1**.
That convention silently fixes the unit of length at the **curvature radius R**.
The programme has spent years asking whether the object can *produce* a scale
while never asking what it *fixed for free* in the first line of every
calculation. `frontier/B666_leads_campaign/cellS/` built an entire torsor
formalism and never pointed it at the metric.

The instrument required is elementary: assign each quantity its scaling weight
under `g → k²g` (equivalently `R → kR`). Nothing here is deep. It was simply
never written down, and it decides three open questions.

## The ledger

| weight | quantity |
|---|---|
| **+1** | length — systole, core length, complex length |
| **+2** | area — cusp cross-section, maximal cusp area |
| **+3** | volume |
| **−2** | Laplace eigenvalue λ = 1 + r² |
| **−1** | volume entropy h = 2/R |
| **0** | trace, trace-field element, Galois datum |
| **0** | Chern–Simons, torsion, η |
| **0** | cusp **shape** τ (not cusp *area*) |
| **0** | level, conductor, index, cohomology class |

## Consequence 1 — the scale-torsor no-go *is* dimensional analysis

Sorting the eleven faces of the anatomy by the weight of the data they carry:

**Scale-blind (weight 0) — 8 of 11:** being, hearing, meeting, congruence-tower,
sln-tower, coupled-double, mtc-overlay, infinite-hecke.

**Scale-sensitive — 3 of 11:** children (+3), emittance-lengths (+1),
emittance-eigenvalues (−2).

A weight-0 structure cannot produce a weight-nonzero output. That is the entire
content of `Hom(G, ℝ₊) = 0` for finite and profinite G — the B666 no-go —
restated without cohomology: **you cannot get a length out of a trace.**

And it explains, structurally, why B738's shortlist is right that the theorem's
hypothesis class excludes emittance: emittance is precisely the part of the
anatomy that is not weight-0.

## Consequence 2 — but emittance does not escape either

**This is a negative against this seat's own most exciting finding of the day,
found within the hour, by the cheapest available check.**

Earlier today I established — and verified in four files — that the programme's
deepest named hatch was blocked only on uncomputed Maass eigenvalues, and that
those eigenvalues now exist. That much stands. What does not follow is that the
spectrum can supply a scale.

A scale exists **iff** the object forces a relation between quantities of
*different* weight, since such a relation has a unique solution for R. But
hyperbolic geometry is **exactly scale-covariant**: `R → kR` carries every
relation to a relation, preserving weight. So no internal relation can be
weight-inhomogeneous — on any face, emittance included. The eigenvalues are
weight −2. They are numbers in units of R, exactly as the volume is.

So for the **dimensionful** reading, the anchor cannot come from the spectrum —
not because a theorem forbids it, but because there is nothing left for a
theorem to forbid. The programme's highest-rated escape route
(`native-continuous-channel`, n = 21, mean revival 3.19) is closed in that
reading, and closed by arithmetic a first-year student could check.

## Consequence 3 — the positive statement: **one input, not a gap**

The object is a **shape**, and a shape has no size. Fix R once, from outside,
and every dimensionful quantity is determined with no further freedom:

```
volume        = 2.02988321282  · R³
systole       = 1.087070145    · R
λ₂            = 25.0108366633  / R²
λ_parent      = 51.013243205   / R²
```

So the programme's "zero free parameters" is exactly: **zero free shape
parameters, one free scale parameter.** That is not a missing ingredient — it is
one number, and it must come from outside. `frontier/B151_firewall_confirmation/`
already observed the fact (*"all dimensionful content carried by ℏ↔k … and none
by the invariant"*); the weight ledger states it as an identity and shows it is
forced rather than incidental.

## Consequence 4 — what needs no input at all

The weight-0 combinations are canonical, choice-free, and independent of R.
They are the object's genuine scale-free numbers, and the **dimensionless**
sector is the only sector they could ever address.

| observable | value | weights |
|---|---|---|
| λ₂ · vol^(2/3) | 40.09672678450524360655 | −2 +2 = 0 |
| λ_parent · vol^(2/3) | 81.78311276508396361058 | −2 +2 = 0 |
| λ₂ · systole² | 29.5558434215393783282 | −2 +2 = 0 |
| λ_parent · systole² | 60.28344628731633370659 | −2 +2 = 0 |
| systole³ / vol | 0.6328512667084538490477 | +3 −3 = 0 |
| systole / vol^(1/3) | 0.8585532131336245526378 | +1 −1 = 0 |
| λ_parent / λ₂ | 2.039645610092237640404 | −2 +2 = 0 |

**Precision, stated exactly.** Only λ₂ (25 certified digits, B922) and the
parent (this seat, all gates PASS) are deep. VOL is exact to the digits shown.
SYS is quoted from B850 at 15 figures, so any product with SYS is good to ~15
figures only. **λ₁ is deliberately absent** — it is not banked at certified
depth on `origin/main`, and a remembered value has no place in a ledger.

## What this does to the two open probes

B738's shortlist carries two probes that were blocked on the eigenvalues. Both
now have answers, and they are **different** answers, which is why conflating
them cost the programme time:

- **The typing probe** — *"type the emittance channel against Definition 1."*
  **Answer: outside the hypothesis class, and the conclusion holds anyway.**
  The spectral outputs are transcendental and continuous, so Definition 1 does
  not reach them (B738 is right); but scale-covariance closes the dimensionful
  question independently, and more cheaply.
- **The anchor probe** — *"is there a canonical nondegenerate real anchor among
  the choice-free spectral data?"* **Answer: yes, and §4 lists instances.**
  If "anchor" means a canonical *real number*, the weight-0 observables are
  exactly that. If it means a *dimensionful* quantity, see the typing probe.

**The word "anchor" was carrying both meanings.** Separating them is the whole
result: one half is answered no on elementary grounds, the other half is
answered yes and is computable today.

## Honest scope

This is dimensional analysis, not a theorem anyone should be proud of proving.
Its value is entirely that it was never applied here, and that it converts an
expensive open question into a cheap closed one plus a cheap open one. It says
nothing about whether the object's dimensionless numbers mean anything — that is
the sealed Cell 9 question, which remains null at 8 digits and untested at 25.

Reproduce: `python3 weight_ledger.py` (self-checks λ₂ against B922's banked value).
