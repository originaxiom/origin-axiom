# Conditional Uniqueness of the Origin Axiom Core

Status: draft theorem note for review. This is not a public preprint and does
not promote any claim.

## Abstract

We isolate a small conditional theorem behind the Origin Axiom core. Given a
two-record integer substrate, reversible orientation-preserving primitive
one-channel updates, torsion-free first mixed closure, minimal hyperbolic
complexity, and a final order convention, the persistent sector is forced to

```text
A = LR = [[2,1],[1,1]]
```

up to the order choice `LR` versus `RL`. The selected matrix has trace `3`,
determinant `1`, characteristic polynomial `t^2 - 3t + 1`, and eigenvalues
`phi^2`, `phi^-2`. The order convention is load-bearing: as a Mobius action,
`LR` has fixed-point polynomial `tau^2 - tau - 1`, while `RL` has
`tau^2 + tau - 1`. The theorem is conditional; it does not derive the substrate,
the order convention, physics, units, particles, gauge groups, or observables.

## 1. Motivation

The project originally asked whether "nothing" could be unstable and generate
structure. The broad survey showed a repeated obstruction: source-free zero
does not move, and candidate mechanisms usually work only after a source,
selector, measure, carrier, unit scale, or observable bridge is supplied.

The positive mathematical result is narrower. Once a minimal two-record
substrate and primitive ordered updates are granted, the downstream core becomes
rigid. This note states that rigidity as a conditional theorem.

## 2. Axioms

The theorem uses the following axioms.

| # | Axiom | Content |
|---|---|---|
| A1 | Two-record substrate | The state space is `Z^2`. |
| A2 | Reversible integer transfer | Updates are invertible integer-linear maps. |
| A3 | Orientation-preserving | The update matrices have determinant `+1`. |
| A4 | Primitive one-channel update | The elementary updates are the primitive shears `L` and `R`. |
| A5 | Torsion-free first mixed closure | The first mixed persistent sector has torsion-free mapping-torus first homology. |
| A6 | Minimality | Among nontrivial admissible closures, choose minimal hyperbolic complexity. |
| A7 | Order convention | Choose the based order `LR` rather than its mirror `RL`. |

The theorem does not derive these axioms. It states what follows once they are
accepted.

## 3. First Mixed Closure

Let

```text
L_a = [[1,a],[0,1]]
R_b = [[1,0],[b,1]]
```

with positive integers `a,b`. The first mixed closure is

```text
B(a,b) = L_a R_b = [[1+ab,a],[b,1]].
```

Direct calculation gives:

```text
det B(a,b) = 1
trace B(a,b) = 2 + ab
det(B(a,b) - I) = -ab
```

The case `a = b = 1` gives:

```text
B(1,1) = L R = [[2,1],[1,1]].
```

## 4. Torsion Lemma

Let `M_B` be the mapping torus of the torus automorphism induced by `B`.
The Wang exact sequence gives:

```text
H1(M_B; Z) = Z plus coker(B - I).
```

If `det(B - I) != 0`, then `coker(B - I)` is finite and:

```text
|torsion H1(M_B; Z)| = |det(B - I)|.
```

For `B(a,b)` this gives torsion order `ab`. Therefore torsion-free closure
forces:

```text
ab = 1.
```

Over positive integers:

```text
a = b = 1.
```

The proof is written in
`papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md`.

## 5. Minimal Trace Route

The same conclusion is reached from minimal hyperbolic trace. Since

```text
trace B(a,b) = 2 + ab,
```

and `a,b` are positive integers, the first hyperbolic trace is:

```text
trace = 3.
```

This again forces:

```text
ab = 1,
a = b = 1.
```

The two routes agree: torsion-free closure and minimal hyperbolic trace both
select the same first mixed sector.

## 6. Theorem

**Theorem.** Under axioms A1-A6, the first mixed persistent sector is forced, up
to the order convention A7, to be:

```text
A = L R = [[2,1],[1,1]].
```

It has:

```text
det A = 1
trace A = 3
charpoly(A) = t^2 - 3t + 1
eigenvalues = phi^2, phi^-2
```

**Proof.** By A4, the first mixed closure has the form `B(a,b) = L_a R_b`.
By the identities above, `det(B(a,b)-I) = -ab`. By A5 and the torsion lemma,
torsion-free closure forces `ab = 1`; over positive integers, this gives
`a = b = 1`. Equivalently, by A6 the first hyperbolic trace is `2 + ab = 3`,
again forcing `ab = 1`. Hence `B(1,1) = LR = A`. The determinant, trace,
characteristic polynomial, and eigenvalues are direct calculations.

## 7. Order Is Not Cosmetic

A1-A6 do not distinguish `LR` from `RL`. The two are conjugate and share trace,
determinant, eigenvalues, and translation length. They are the same unbased
sector.

They differ as based Mobius transformations:

| Sector | Fixed-point polynomial | Roots |
|---|---|---|
| `LR` | `tau^2 - tau - 1` | `phi`, `-1/phi` |
| `RL` | `tau^2 + tau - 1` | `1/phi`, `-phi` |
| `L A L^-1` | `tau^2 - 3 tau + 1` | `phi^2`, `phi^-2` |

Thus the golden fixed-point polynomial is a based invariant of `A = LR`, not a
conjugacy-class invariant. The order convention A7 is the residual binary input
that selects the golden representative over its mirror.

## 8. Downstream Consequences

Given `A`, the governed core P1-P16 follows through existing exact-algebra
claims and tests. This includes the phi-spectrum, figure-eight / punctured-torus
monodromy host, closed-form `log A`, gluing identities, and the Mobius vector
field and derived potential.

This note does not restate those proofs. It only identifies the conditional
route that forces `A` from the stated minimal-record assumptions.

## 9. Non-Claims

This theorem does not claim:

```text
the substrate is derived from nothing
the order convention is forced from weaker data
the result is a theory of physics
units, particles, gauge fields, or observables are derived
the frontier field-theory lift is proven
```

Correct status:

```text
conditional mathematical theorem candidate
ready for external mathematical review
not yet a public preprint
```

## 10. Reproduction

Run from repository root:

```bash
python -m pytest -q
python -m pytest -q tests/test_uniqueness_theorem.py
```

Current expected results:

```text
full suite: 66 passed, 1 skipped
uniqueness theorem tests: 9 passed
```

## 11. Review Questions

External review should focus on:

```text
Are A1-A7 precise enough?
Is the torsion-free closure assumption natural or too tailored?
Is the mapping-torus torsion lemma correct and convention-safe?
Is "unique up to order" the right mathematical phrasing?
Is the based-invariant distinction stated correctly?
Should the P1-P16 corollary be narrowed before public drafting?
```
