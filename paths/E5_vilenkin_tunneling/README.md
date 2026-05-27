# E5 — Vilenkin tunneling from nothing

> **Phase C frontier probe.** Logged observation, not a claim
> (`../../GOVERNANCE.md` §5). See `../README.md` for ground rules.

## The mechanism

The mainstream physics-literature candidate for emergence from nothing.
Vilenkin (1982, 1984) and parallel Hartle–Hawking (1983) work proposed
that a closed FRW universe with positive cosmological constant can be
described by a Wheeler–DeWitt wavefunction `ψ(a)` in the scale factor `a`,
and that the wavefunction supports a *tunneling solution* from `a = 0`
("nothing": no spatial geometry) through a classically forbidden barrier
into the de Sitter expansion regime `a > a_max`.

This is the **quantum-physical** candidate for the missing ingredient that
E14 (formalism) and E11 (counting) could not supply. E14 + E11 sharpen the
question E5 must answer: the Wheeler–DeWitt setup must specify both *the
Hilbert space of "nothing"* and *a non-zero amplitude out of it*, without
either being smuggled in as a prior.

## Minisuperspace setup

Closed FRW metric `ds² = −N² dt² + a(t)² dΩ_3²` (`S³` spatial slices,
homogeneous and isotropic). The Einstein–Hilbert action with cosmological
constant `Λ > 0` reduces, in natural units (`M_Pl = 1`, conventional
operator ordering, conventional measure), to the Wheeler–DeWitt equation

> `[−∂_a² + V(a)] ψ(a) = 0`,    `V(a) = a² − (Λ/3) a⁴`.

The barrier `V(a) > 0` for `0 < a < a_max := √(3/Λ)`. Beyond `a_max` the
potential turns negative — classical de Sitter expansion. The "tunneling
from nothing" wavefunction is the WKB solution that decays inward from
`a = a_max` toward `a = 0` and is outgoing-Lorentzian for `a > a_max`.

## The probe (`probe.py`)

1. Compute `V(a)` and `a_max` for `Λ ∈ {0.1, 0.3, 1.0, 3.0, 10.0}`.
2. Compute the WKB tunneling exponent
   `B(Λ) = ∫₀^{a_max} √V(a) da`
   analytically and numerically (scipy `quad`); cross-check.
3. Report the tunneling-amplitude suppression `|ψ|² ∼ exp(−2B)`.
4. Save `vilenkin_barrier.png` — `V(a)` vs `a` for several `Λ`, with the
   `V = 0` line and `a_max` marked.
5. Save `vilenkin_psi.png` — WKB `|ψ(a)|` across the barrier and into the
   classical region for `Λ = 1`.

Closed-form result: with the substitution `u = (Λ/3) a²`,
`B(Λ) = (3/(2Λ)) ∫₀¹ √(1−u) du = 1/Λ`,
so `|ψ(a_max)|² ∼ exp(−2/Λ)`. (Dimensionful conventions add factors
of order one — e.g. `3π/(2GΛ)` in some operator-ordering schemes; the
qualitative dependence `B ∝ 1/Λ` is convention-independent.)

## What would distinguish E5 from a restatement of standard cosmology

A successful E5 would have to:

(a) deliver a non-zero amplitude — this is met,
(b) be generic across plausible truncations and boundary-condition choices
    rather than a specific minisuperspace artifact,
(c) admit an interpretation where the "probability of a universe" is a
    probability *of something*, not a ratio of WKB amplitudes inside a
    Hilbert space whose construction already presupposes cosmology.

The minisuperspace computation handles (a) immediately. Whether (b) and
(c) survive a careful audit is the verdict question.

## Prior literature

- Vilenkin, *Creation of universes from nothing*, Phys. Lett. B 117 (1982).
- Hartle and Hawking, *Wave function of the universe*, Phys. Rev. D 28 (1983).
- Vilenkin, *Quantum creation of universes*, Phys. Rev. D 30 (1984).
- Halliwell, *Introductory lectures on quantum cosmology*, Proc. Jerusalem
  Winter School (1990) — the standard pedagogical treatment of the
  minisuperspace WKB and the operator-ordering question.
- Feldbrugge, Lehners, Turok, *No smooth beginning for spacetime*, Phys.
  Rev. Lett. 119 (2017) — and the ensuing exchange with Halliwell, Hartle,
  Hertog: a recent dispute over whether the no-boundary path integral is
  even well-defined. Cited here only as evidence that the construction's
  foundations are still contested.

E5 stays at the level of the elementary minisuperspace WKB calculation;
the full path-integral / Picard–Lefschetz dispute is recorded as
context, not adjudicated.
