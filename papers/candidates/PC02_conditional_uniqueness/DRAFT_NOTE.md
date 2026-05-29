# Draft Note -- Conditional Uniqueness of the Origin Axiom Core

Status: external-review draft note. This is not a public preprint and does not
promote any claim beyond `CLAIMS.md`.

## Abstract

We record a conditional rigidity result for the Origin Axiom core. Given explicit
minimal-record axioms A1-A7, the first mixed persistent sector is forced to be
`A=LR` up to order. The downstream algebraic consequences P1-P16 are
machine-checked in the canonical repository. The result is conditional: the
record substrate, primitive-update filters, torsion-free closure, and based
order convention are hypotheses, not derived laws of nature.

## Main Theorem

Under the minimal-record axioms A1-A7 in `docs/UNIQUENESS_THEOREM.md`, the first
mixed closure is:

```text
A = L R = [[2,1],[1,1]]
```

up to the `LR/RL` order choice. It has trace `3`, determinant `1`,
characteristic polynomial `t^2-3t+1`, eigenvalues `phi^2` and `phi^-2`, and
discriminant `5`.

## Proof Route

The theorem is proven in the repository as a chain of exact computations and a
standard topology lemma:

```text
positive primitive shears L_a, R_b
  -> B(a,b)=L_a R_b = [[1+ab,a],[b,1]]
  -> det(B-I)=-ab
  -> torsion-free/minimal closure forces ab=1
  -> a=b=1
  -> A=LR, up to order
```

The mapping-torus homology step is written in
`MAPPING_TORUS_TORSION_LEMMA.md`:

```text
H1(mapping torus of B) = Z plus coker(B-I)
torsion order = abs(det(B-I)) when det(B-I) is nonzero
```

The machine-checked lemmas are in `tests/test_uniqueness_theorem.py`.

## Downstream Exact Algebra

Given `A`, the governed core P1-P16 follows through existing tested modules:

```text
A
  -> phi-spectrum and Fibonacci transfer structure
  -> preserved phase-space form
  -> figure-eight monodromy and torsion growth
  -> log(A) sl(2,R) decomposition
  -> Mobius vector field
  -> derived cubic potential
```

The Mobius vector field and potential are exact algebra about `A`; they are not
physics claims.

## Half-Step Appendix

Frontier probes B13-B19 refine the based structure. The operational half-step
condition

```text
(L X)^2 = A
```

isolates `X=+/-P` in exact bounded searches, with `F=LP` and `F^2=A`.
This is useful structure, but it remains conditional on the half-step condition
or an exchange-symmetry interpretation of the two-record substrate.

## Trace-Map Appendix

B18 establishes that the Fibonacci trace map is the functorial half-trace lift
of the half-step `F`. At `(1,1,1)` its Jacobian has:

```text
(t+1)(t^2-3t+1)
```

The `-1` factor is generic for orientation-reversing lifts. B22 shows the
special object is the `A` quadratic sector, which appears for the primitive
half-step condition `det=-1`, `trace=+/-1`.

No spacetime, matter, gauge, or awareness dictionary is claimed.

## Motivated Spectral Anchor

B25 tests the Fibonacci Hamiltonian at `lambda=1`. Finite approximants show
strict Fibonacci gap-label residuals for the largest gaps and a mid-scale
box-counting slope near `0.75` at word index `20`.

This is not an exact Hausdorff-dimension claim and not a prediction of the core.
B26 strengthens the coupling motivation. The projective half-return
linearization of the trace-map orbit through `(0,0,c)` contains the `A`
quadratic sector only at:

```text
4c^2 - 2 = 3
c^2 = 5/4
I = c^2 - 1 = 1/4
lambda=1
```

The caveat is load-bearing: `(0,0,c)` is not a literal period-3 orbit of the
signed trace map; it is a sign-flipping half-return. Thus `lambda=1` is selected
by a natural projective self-similarity criterion, but that criterion is still
an additional rule rather than a consequence of A1-A7.

B26 also shows that the same projective criterion gives an exact Lucas hierarchy:

```text
char(F^n)=t^2-L_n t+1       (n even)
I=(L_n-2)/4
lambda^2=L_n-2 = 1, 5, 16, 45, 121, ...
```

The full-return control is different: the literal `T^6` return matches `A` at
real `I=-3/4`, not at the B25 `I=1/4` surface.

Relevant literature control: Damanik, Gorodetski, and Yessen, *The Fibonacci
Hamiltonian*, `arXiv:1403.7823`.

## Explicit Non-Claims

```text
not a derivation from absolute nothing
not a physical theory
not a derivation of 3+1 dimensions
not a derivation of matter, gauge groups, constants, or observables
not proof that lambda=1 is forced
not a new gap-labeling theorem for the Fibonacci Hamiltonian
```

## Reviewer Questions

1. Are A1-A7 stated minimally, or can any hypothesis be weakened without losing
   the uniqueness theorem?
2. Is the `LR/RL` order dependence presented correctly as based data rather
   than conjugacy-invariant data?
3. Is the mapping-torus torsion lemma stated with the right hypotheses?
4. Is the half-step trace-lift bridge known standard material, new packaging, or
   incorrectly framed?
5. Is the B26 projective half-return criterion natural or standard in the
   character-variety/Fibonacci-Hamiltonian literature, or is it an inserted
   selector?

## Reproduction

```bash
python -m pytest -q
python -m pytest -q tests/test_uniqueness_theorem.py
python frontier/B25_fibonacci_spectrum_anchor/probe.py
python frontier/B26_lambda1_derivation_attempt/probe.py
```
