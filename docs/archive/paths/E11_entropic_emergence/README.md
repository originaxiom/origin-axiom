# E11 — Entropic emergence

> **Phase C frontier probe.** Logged observation, not a claim
> (`../../GOVERNANCE.md` §5). See `../README.md` for ground rules.

## The mechanism

The Boltzmann argument applied to existence: *"nothing"* is exactly one
microstate (every cell empty); *"something"* is exponentially many; the second
law forces flow from low-multiplicity to high-multiplicity macrostates. If
counting alone suffices, the empty configuration is essentially unreachable in
any system large enough to be called "real."

This is the **statistical** candidate for the emergence ingredient that E14
showed pure formalism cannot supply. The question this probe answers is narrow
and definite: does counting alone produce emergence, or does it require
additional structure?

## The probe (`probe.py`)

Define an `n`-cell binary lattice (each cell ∈ {0, 1}). Compute:

1. **Total microstates** `2^n` and the *empty* count `1`.
2. **Multiplicity** at each occupancy `k`: `C(n, k)`.
3. **Peak multiplicity** (at `k = n/2`).
4. The **entropic "force"** on the empty state: `log( peak_multiplicity )`,
   which is the standard Boltzmann pull from `k = 0` to the binomial peak.
5. The **probability of empty** under a uniform distribution: `1/2^n`.

Also save a log-scale plot of multiplicity vs occupancy for `n = 64`, showing
the exponential gap between `k = 0` (mult 1) and the half-filled peak.

These are all elementary combinatorial computations — no free parameters, no
fits. The interesting question is what they license one to *claim*.

## What would distinguish E11 from a trivial restatement

A successful E11 would do more than "in a configuration space, empty is rare."
That is immediate. It would need to construct the configuration space *from
nothing* — to derive both the lattice and the uniform distribution from a
prior even more minimal than "a lattice exists." Whether the probe achieves
that is the verdict question.

## Prior literature

- Boltzmann's H-theorem, foundational statistical mechanics — the standard
  multiplicity-of-microstates argument.
- Jaynes, *Information Theory and Statistical Mechanics* — maximum-entropy
  derivation of equilibrium distributions.
- Tegmark, *Our Mathematical Universe* — a related but stronger claim
  (mathematical existence ⇒ physical existence) which presupposes a measure on
  mathematical structures.
- Kragh, *Cosmology and Controversy* — historical discussion of statistical
  arguments for cosmic emergence.

E11 stays at the level of the elementary combinatorial fact; the larger
claims of Tegmark-style multiverse arguments live elsewhere (closer to E13 /
P3 territory).
