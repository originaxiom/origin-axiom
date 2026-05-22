# Origin Axiom — Matrix/Topology Sieve

Date: 2026-05-20

## Scope

This is a bounded, reproducible algebraic sieve for the proposed minimal paired-record topology.

It verifies the matrix-level claims and the algebraic topology filter for once-punctured torus bundles. It does **not** run SnapPy/Sage/Regina and does **not** independently verify hyperbolic census facts or cusp shapes.

## Core matrices

Minimal two-record update:

\[
F = \begin{pmatrix}1&1\\1&0\end{pmatrix}
\]

- det(F) = -1
- characteristic polynomial = `λ² - λ - 1`
- eigenvalues = `φ`, `-φ⁻¹`

Orientation-preserving square:

\[
A = F^2 = \begin{pmatrix}2&1\\1&1\end{pmatrix}
\]

- det(A) = 1
- trace(A) = 3
- characteristic polynomial = `λ² - 3λ + 1`
- eigenvalues = `φ²`, `φ⁻²`
- entropy = `log(φ²) = 0.9624236501192069`

## Periodic-record counts

For:

\[
P_n = |\det(A^n - I)|
\]

the first values are:

| n | P_n |
|---:|---:|
| 1 | 1 |
| 2 | 5 |
| 3 | 16 |
| 4 | 45 |
| 5 | 121 |
| 6 | 320 |
| 7 | 841 |
| 8 | 2205 |
| 9 | 5776 |
| 10 | 15125 |

The associated record zeta function is:

\[
\zeta_A(z)=\exp\left(\sum_{n\ge1}\frac{P_n}{n}z^n\right)
=\frac{(1-z)^2}{1-3z+z^2}
\]

The denominator `1 - 3z + z²` is the reciprocal form of the same polynomial `t² - 3t + 1`.

## Homology/torsion filter

For a once-punctured torus bundle with monodromy `B`:

\[
H_1(M_B) \cong \mathbb Z \oplus \mathrm{coker}(B-I)
\]

For `B ∈ SL(2,Z)`:

\[
\det(B-I)=2-\mathrm{tr}(B)
\]

So the finite torsion order is:

\[
|2-\mathrm{tr}(B)|
\]

Torsion-free means:

\[
|2-\mathrm{tr}(B)|=1
\]

so:

\[
\mathrm{tr}(B)=1 \text{ or } 3
\]

Hyperbolic persistence requires:

\[
|\mathrm{tr}(B)|>2
\]

Therefore the only hyperbolic torsion-free trace is:

\[
\mathrm{tr}(B)=3
\]

## Bounded enumeration

Entries were enumerated in the box `[-8,8]` for all `2x2` integer matrices with determinant `1`.

| stage | count |
|---|---:|
| det=1 entries <=8 | 692 |
| hyperbolic |tr|>2 | 456 |
| torsion-free coker(M-I) within bound | 44 |
| hyperbolic + torsion-free | 16 |


All `hyperbolic + torsion-free` matrices found in this box had trace `3`.

Those matrices are:

```text
[[-1, -5], [1, 4]]
[[-1, -1], [5, 4]]
[[-1, 1], [-5, 4]]
[[-1, 5], [-1, 4]]
[[0, -1], [1, 3]]
[[0, 1], [-1, 3]]
[[1, -1], [-1, 2]]
[[1, 1], [1, 2]]
[[2, -1], [-1, 1]]
[[2, 1], [1, 1]]
[[3, -1], [1, 0]]
[[3, 1], [-1, 0]]
[[4, -5], [1, -1]]
[[4, -1], [5, -1]]
[[4, 1], [-5, -1]]
[[4, 5], [-1, -1]]
```

A bounded conjugacy search found each of these conjugate to the canonical trace-3 matrix `A` or `A⁻¹` by a `GL(2,Z)` matrix with entries searched up to absolute value 10. This is computational evidence, not a standalone proof of global conjugacy.

## Positive primitive trace-3 candidates

If we require all entries nonnegative/positive, determinant `1`, trace `3`, and hyperbolic torsion-free behavior, the only matrices found are:

```text
[[1, 1], [1, 2]]
[[2, 1], [1, 1]]
```

These are relabelings/transposes of the same minimal paired-record update.

## Metallic family check

For substitutions:

\[
S_m = \begin{pmatrix}m&1\\1&0\end{pmatrix}
\]

the orientation-preserving square is:

\[
M_m=S_m^2=\begin{pmatrix}m^2+1&m\\m&1\end{pmatrix}
\]

| m | trace(M_m) | torsion | largest eigenvalue | entropy |
|---:|---:|---:|---:|---:|
| 1 | 3 | 1 | 2.618033988750 | 0.962423650119 |
| 2 | 6 | 4 | 5.828427124746 | 1.762747174039 |
| 3 | 11 | 9 | 10.908326913196 | 2.389526434574 |
| 4 | 18 | 16 | 17.944271909999 | 2.887270950358 |
| 5 | 27 | 25 | 26.962912017836 | 3.294462292742 |
| 6 | 38 | 36 | 37.973665961010 | 3.636892918464 |
| 7 | 51 | 49 | 50.980384612482 | 3.931440943299 |


Only `m=1` is torsion-free. This is the Fibonacci/figure-eight candidate.

## Polynomial factorization check

Figure-eight state-integral/spectral polynomial used in the audit:

\[
p^4 - 2p^3 - p^2 - 2p + 1
\]

Factorization:

\[
(p^2 - 3p + 1)(p^2 + p + 1)
\]

- `p² - 3p + 1`: record/golden factor, discriminant `5`
- `p² + p + 1`: equilateral/Eisenstein factor, discriminant `-3`

Resultant:

\[
\mathrm{Res}(p^2-3p+1, p^2+p+1)=16
\]

Full quartic discriminant:

\[
-3840 = -2^8 \cdot 3 \cdot 5
\]

Competitor polynomial checked:

\[
p^4 - 2p^3 - 5p^2 - 2p + 1
\]

It is irreducible over `Q` in this computation.

## Strongest safe conclusion

Under the **minimal positive paired-record sieve**, the first orientation-preserving hyperbolic torsion-free update is:

\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}
\]

It has characteristic polynomial:

\[
t^2-3t+1
\]

This matches the figure-eight Alexander polynomial up to the usual sign/unit normalization.

The associated once-punctured torus bundle has:

\[
H_1 \cong \mathbb Z
\]

whereas the `-A` sister branch has:

\[
H_1 \cong \mathbb Z \oplus \mathbb Z/5
\]

## Important limitations

- This does **not** prove the universe is the figure-eight complement.
- This does **not** prove global uniqueness among all higher-dimensional/higher-memory systems.
- This does **not** independently verify SnapPy census, cusp shapes, or hyperbolic volume.
- This proves a conditional algebraic/topological selection result under the stated minimal paired-record assumptions.
