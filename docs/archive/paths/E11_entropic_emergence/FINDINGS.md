# E11 — Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Result

(a) **The combinatorics are immediate and exact.** For an `n`-cell binary
lattice:

| n   | P(empty) = 2⁻ⁿ | peak multiplicity C(n, n/2) | entropic pull log(peak/1) |
|----:|---------------:|----------------------------:|--------------------------:|
| 2   | 2.5 × 10⁻¹     | 2                           | 0.69                      |
| 8   | 3.9 × 10⁻³     | 70                          | 4.25                      |
| 32  | 2.3 × 10⁻¹⁰    | 6.01 × 10⁸                  | 20.21                     |
| 64  | 5.4 × 10⁻²⁰    | 1.83 × 10¹⁸                 | 42.05                     |
| 128 | 2.9 × 10⁻³⁹    | 2.40 × 10³⁷                 | 86.07                     |

Asymptotically `P(empty) = 2⁻ⁿ` and `peak ∼ 2ⁿ/√(nπ/2)`, so the Boltzmann
pull `log(peak/empty) ∼ n·log 2 − ½·log(nπ/2)` grows linearly in `n`. There
are no free parameters and no fits. The plot
(`entropy_multiplicity.png`) shows the log-scale gap between `k = 0`
(multiplicity 1, red dashed line) and the half-filled peak for `n = 64`.

(b) **The mechanism works as a selector but not as a generator.** Given a
lattice of `n` cells and the uniform measure over the `2ⁿ` microstates, the
empty configuration is exponentially suppressed. That is the standard
Boltzmann fact and it is correct. But to *state* this fact one must
already have:

1. a configuration space (the `n`-cell lattice — which is structure, not
   nothing),
2. a measure on that space (here uniform — which is a choice, not nothing),
3. a notion of "occupancy" defined on the cells.

All three are external inputs. The counting argument runs *inside* a
prebuilt phase space; it does not construct that phase space. The
philosophical content of "nothing" is exactly that none of (1)–(3) is yet
available. **Entropy selects within possibility; it does not produce
possibility.**

(c) **This is structurally the same wall E14 named.** E14 showed that the
formal characterizations of "nothing" (initial object, empty type, ∅) are
well-defined but do not, by themselves, force emergence — the *target* is
clean, but the *force* must come from elsewhere. E11 is now the test of one
specific candidate force — counting — and the candidate fails for the same
reason: the counting argument is structurally a function on a pre-existing
measure space. The empty measure space (no σ-algebra, no measure) does not
support the inequality `1 ≪ 2ⁿ`.

The probe is honest about what the table shows: in any reasonably-sized
configuration space, empty is rare. That is a statement about
*configuration spaces*, not about reality vs. void.

## What this means for the Origin Axiom program

E11 closes out the **statistical** candidate ingredient with a `STALLED`
verdict that parallels E14's `STALLED`. Together they bracket the
problem from two sides:

- E14: pure formalism gives a well-defined target without a force.
- E11: counting gives a force but only when the target (the phase space)
  is already given.

Neither alone supplies the missing piece. The remaining first-batch probe
**E5 (Vilenkin tunneling)** is the test of the *quantum-physical* candidate:
whether tunneling-from-nothing supplies both the configuration space and
the dynamics in one move. E14 + E11 sharpen the question E5 must answer:
the Wheeler-DeWitt setup must specify both the Hilbert space of "nothing"
and a non-zero amplitude out of it, without either being smuggled in as a
prior.

A measure-theoretic refinement of the entropic mechanism — does the *absence*
of a measure on the empty space carry information? — is the natural follow-up
and belongs to **E13** (Class E, measure-theoretic), not E11. E11 stays at
the elementary combinatorial fact.

## Verdict

**`STALLED`**

The combinatorics are exact and the conclusion is sharp: counting is a
selection mechanism, not a generation mechanism. The suppression of the
empty configuration is real but conditional on a pre-existing
configuration space and measure, which are precisely what "nothing" lacks.
The unconstructed step is the construction of the phase space itself from a
prior more minimal than "a lattice and a uniform measure exist." Without
that step, the Boltzmann pull computes the suppression of empty *given*
something, not the emergence of something from *nothing*.

This is the second `STALLED` in a row in Phase C's first batch, and the
two stalls have the same shape — formalism without force, force without
target. The pattern is informative on its own: it raises the prior that
the candidate ingredient sought in Phase C is genuinely external to both
the formal and statistical levels, and lives in physics (E5, E9, E20) or
in a structural primitive yet unnamed.
