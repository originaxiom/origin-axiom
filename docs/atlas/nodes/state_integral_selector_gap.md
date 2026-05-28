# State-Integral Selector Gap

Status: atlas node for PC06. Literature bridge and theorem question, not a
solved result.

## Question

Can the figure-eight state-integral route force the nonzero contour, thimble, or
relative-homology class needed to turn quantum-topological host data into a
selector?

## Mathematical Object

The route studies quantum-dilogarithm and state-integral structures associated
with the figure-eight host. The relevant local mechanism is branch or contour
monodromy:

```text
V(y) = Li2(exp(y)) - Li2(exp(-y))
x = exp(y)
dV/dy = -log(1-x) - log(1-1/x)
```

If `w0` winds around `x = 0` and `w1` winds around `x = 1`, the derivative
monodromy has the form:

```text
Delta(dV/dy) = 2 pi i (w0 - 2 w1)
```

This shows a genuine monodromy-residue mechanism. It does not select the
winding.

## What Was Tested

Private staging probes and the public campaign synthesis tested:

```text
branch-cut monodromy residue
global contour winding rules
quantum-dilog source spine
Picard-Lefschetz and Stokes selector language
state-integral host reconstruction
```

Public canonical evidence:

```text
docs/atlas/campaigns/quantum_selector_v1.md
papers/candidates/PC06_quantum_selector_bridge/PAPER_CARD.md
```

## What Passed

The route has serious mathematical hosts:

```text
quantum-dilog state integrals
figure-eight A-polynomial asymptotics
Picard-Lefschetz cycles
complex Chern-Simons state-integral context
Teichmuller TQFT state-integral environment
Stokes and resurgence sector switching
```

The monodromy lattice is nontrivial. Branch data can produce residues.

## What Failed

The selector was not locally forced:

```text
zero winding remains allowed
multiple primitive nonzero windings remain allowed
some nontrivial windings lie in the derivative-monodromy kernel
orientation sign remains unforced
Stokes lateral choice remains a boundary or contour choice
source-level audit did not find a forced nonzero compact-loop class
explicit thimble intersection vector was not constructed locally
```

The route therefore stalls at the same structural wall:

```text
host exists
selector missing
```

## Verdict

```text
NEEDS-EXPERTISE
```

The state-integral route is not dead. It is no longer a toy local route. It
requires source-level theorem work about contours, relative homology, or
thimble intersections.

## Needed Theorem

The precise missing theorem is:

```text
a source-normalized quantum-dilog / Picard-Lefschetz theorem forcing a nonzero
relative-homology or thimble-intersection class for the figure-eight state
integral
```

The theorem must specify:

```text
normalization of the state integral
allowed contour or relative-homology classes
Picard-Lefschetz decomposition data
criterion forcing a nonzero selected class
relation to the figure-eight A-polynomial branch
failure condition if the selector is not unique
```

## Why It Matters

This is the most precise current quantum-topology bridge question. It replaces
vague "quantum selector" language with a concrete object:

```text
the selected contour/thimble/relative-homology class
```

If that object can be forced, PC06 becomes a serious bridge note. If not, the
state-integral route remains a host without a selector.

## What It Does Not Claim

```text
not a proof that the state integral selects the Origin core
not a proof that the contour selector exists
not a derivation of gauge fields, particles, units, or observables
not a physics prediction
```

## Reproduction Commands

Canonical baseline:

```bash
python -m pytest -q
```

The private staging probes behind this node should not be cited as public
reproducers until they are rewritten or migrated under governance. PC06 is
currently a theorem-question dossier, not a reproducible public proof.

## Beginner Explanation

The math has many possible integration paths. Some paths may produce the desired
nonzero contribution, and some may not. The project has not found a rule inside
the current framework that forces the right path. That missing rule is the
selector.

## Formal Explanation

Local branch data give a nontrivial monodromy functional, but the local contour
space still contains zero, sign-opposite, kernel, and multiple primitive
possibilities. Stokes and Picard-Lefschetz language identifies the right kind of
object, but the actual source-normalized contour decomposition or intersection
vector is not constructed. Thus the correct status is expertise-bound theorem
work, not promotion.
