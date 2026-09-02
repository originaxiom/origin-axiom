# R040 — free orientation reversal selects the zero Chern–Simons class: theorem closed, census cusped

Source state: `fresh/main@52010c9e` (B1235). Verdict: **exact theorem for
closed hyperbolic 3-manifolds; exhaustive finite numerical confirmation on the
1,260-member nonorientable cusped census; the cusped universal remains open.**

## Closed theorem

Let `M` be a closed oriented hyperbolic three-manifold admitting a free
orientation-reversing involution. In the Coulson--Goodman--Hodgson--Neumann
normalization,

```text
cs(M) = 0 mod 1.
```

The proof separates the two jobs that B1224/B1235 had left conflated.

1. Freeness makes the fixed set empty. Kawauchi's Definition 1.2 and Theorem
   III therefore give `alpha(M)=0`; Theorem I/Definition 1.1 identify this with
   `Tor H1(M;Z)=A+A`. The number `tau` of 2-primary cyclic summands is even.
2. Hyperbolic rigidity supplies an orientation-reversing isometry in the same
   homotopy class. It need not literally be the original free involution;
   freeness was used only in step 1. Orientation reversal negates the odd-signature operator, so its
   spectrum is paired and `eta(M)=0`.
3. For a compact three-manifold, CGHN quote the APS congruence

   ```text
   3 eta(M) = 2 cs(M) + tau mod 2.
   ```

   Substitution gives `2 cs=0 mod 2`, hence `cs=0 mod 1` in the closed lift.

Primary sources: Akio Kawauchi, *On 3-manifolds admitting
orientation-reversing involutions*, Definitions 1.1--1.2 and Theorems I/III,
[DOI 10.2969/jmsj/03340571](https://doi.org/10.2969/jmsj/03340571); D. Coulson,
O. A. Goodman, C. D. Hodgson and W. D. Neumann, *Computing Arithmetic
Invariants of 3-Manifolds*, §§5.1--5.2, especially pp. 13--15,
[primary PDF](https://www.math.columbia.edu/department/neumann/preprints/snappaper3.pdf).

## The actual A6/cusped population

B1235 tested the first 40 nonorientable cusped census manifolds and found every
orientation double cover at `cs=0`, explicitly registering a datum rather than
a theorem. R040 exhausts the available population with SnapPy 3.3.2:

```text
NonorientableCuspedCensus:                 1260
orientation covers computed:              1260
cs=0 mod 1/2:                              1260
cs=1/4 or other:                               0
orientability/cusp/degree-two controls:     PASS
maximum numerical CS residue:          1.80e-15
```

Thus the `40/40` was not a slice accident: it is `1260/1260` on the entire
SnapPy census. This is still a finite numerical result. It does not prove a
universal theorem for arbitrary cusped manifolds.

## Why the cusp fence is real

CGHN define cusped `cs` only modulo `1/2`; their cusped eta invariant requires
a chosen homology basis at every cusp, and the noncompact PSL fundamental class
has an order-two ambiguity. Kawauchi's theorem is explicitly closed. Therefore
the closed proof cannot simply be copied across the ideal boundary. A valid
cusped proof must show that the free deck transformation is compatible with the
peripheral basis/framing and kills that ambiguity.

R040 strengthens B1235/L194 in exactly two ways: it proves the closed analogue
and exhausts the finite cusped census. It does **not** restore B1234's slogan
that A6 causes all eight value walls. Even a future universal cusped-CS theorem
would pay only the CS/k-blind arrow; rank, generation, scale, dynamics and
arithmetic value-disjointness have independent mechanisms.

## Reproduce

```text
python3 certificates/r040_free_deck_cs/free_deck_cs.py
```

The census half requires SnapPy 3.3.2; the primary-source/parity half is pinned
in `source_snapshot.json`.
