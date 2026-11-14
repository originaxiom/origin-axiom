# Origin Axiom — Gate G4D R-symbol / Braiding Audit

## Purpose

G4D asks whether the record model can recover Fibonacci anyon braid phases.

Earlier gates established:

```text
G4:   fusion-count bridge passes
G4B:  F-symbol amplitude bridge fails/not yet
G4C:  |F|² probability bridge candidate
G4C2: phi switch bias comes from A's Perron vector, conditionally
G4C3: Perron-transition rule remains conditional
```

Now the strict question is:

> Can the record/topology layer recover the Fibonacci R-symbols / braiding phases?

## Executive verdict

G4D does **not** promote us to Fibonacci anyon physics.

Corrected result:

```text
positive L/R braid relation: fail
signed Dehn-twist braid skeleton: partial pass
R-symbol phase derivation: fail
topological quantum anchor: not promoted
```

Important correction:

```text
our positive record shears L,R do not satisfy LRL=RLR.
```

A signed Dehn-twist companion can satisfy the braid relation, but it uses negative entries and therefore exits the positive record-count layer.

## 1. Standard Fibonacci R-symbol data

Using a common Fibonacci convention:

```text
R1   = exp(-4 pi i / 5) = -0.809017-0.587785i
Rtau = exp( 3 pi i / 5) = -0.309017+0.951057i
```

The braid generator in the \((1,tau)\) fusion basis is:

```text
B1 = diag(R1, Rtau)
```

and the adjacent braid is:

```text
B2 = F B1 F
```

These are unitary braid matrices.

## 2. Braid relation audit

| System | Relation | Error | Status | Meaning |
|---|---|---:|---|---|
| Fibonacci braid matrices | B1 B2 B1 = B2 B1 B2 | 3.597534e-16 | pass | unitary braid group representation |
| positive record shears L,R | L R L = R L R | 2.828427e+00 | fail | our positivity convention does not satisfy the braid relation |
| signed Dehn-twist pair L,R_minus | L R_minus L = R_minus L R_minus | 0.000000e+00 | pass | signed geometric Dehn twists can satisfy braid relation, but require negative entries |
| alternative signed inverse pair | L^-1 R L^-1 = R L^-1 R | 0.000000e+00 | pass | another sign convention check |


## 3. Matrix property audit

| Object | Trace | Determinant | Eigenvalues | Unitary error | Projective order | Meaning |
|---|---:|---:|---|---:|---|---|
| record L | 2.000000000000+0.000000000000i | 1.000000000000+0.000000000000i | ['1.0+0.0i', '1.0+0.0i'] | 1.732e+00 |  | positive integer unipotent shear |
| record R | 2.000000000000+0.000000000000i | 1.000000000000+0.000000000000i | ['1.0+0.0i', '1.0+0.0i'] | 1.732e+00 |  | positive integer unipotent shear |
| signed Dehn companion R_minus | 2.000000000000+0.000000000000i | 1.000000000000+0.000000000000i | ['1.0+0.0i', '1.0+0.0i'] | 1.732e+00 |  | orientation-signed Dehn twist companion; breaks positivity |
| record A=LR | 3.000000000000+0.000000000000i | 1.000000000000+0.000000000000i | ['2.618034+0.0i', '0.381966+0.0i'] | 5.916e+00 |  | positive hyperbolic transfer/count matrix |
| Fibonacci F | 0.000000000000+0.000000000000i | -1.000000000000+0.000000000000i | ['1.0+0.0i', '-1.0+0.0i'] | 1.614e-16 | 2 | associativity amplitude matrix |
| Fibonacci braid B1=diag(R1,Rtau) | -1.118033988750+0.363271264003i | 0.809016994375+-0.587785252292i | ['-0.809017-0.587785i', '-0.309017+0.951057i'] | 1.359e-17 | 10 | braid generator in tau-tau fusion basis |
| Fibonacci braid B2=F B1 F | -1.118033988750+0.363271264003i | 0.809016994375+-0.587785252292i | ['-0.309017+0.951057i', '-0.809017-0.587785i'] | 2.486e-16 | 10 | adjacent braid generator in changed fusion basis |


## 4. What passes

### Signed geometric braid skeleton

A signed Dehn-twist pair can satisfy the braid relation.

This suggests there may be a geometric braid skeleton nearby, but it is not the same as the positive record-count pair.

So the lesson is:

```text
positive record layer != signed braid layer
```

If we want braid physics, we may need a separate sign/orientation layer.

## 5. What fails

### Positive record braid relation

The positive \(L,R\) used in the record model fail the braid relation.

So we cannot claim that the positive record monoid itself is a braid group representation.

### R-symbol phases

The record matrices \(L,R,A\) are real positive/integer matrices.

Their eigenvalues are:

```text
L,R: 1
A: phi^2, phi^-2
```

Fibonacci R-symbols are complex roots of unity.

There is no natural map in the current framework from real growth to complex phase without choosing an extra scale.

## 6. Phase-map audit

The file:

```text
G4D_possible_phase_maps_from_A.csv
```

tests maps of the form:

```text
lambda = exp(mu) -> exp(i c mu)
```

Result:

```text
matching Fibonacci phases requires fitted c
```

So this is not derived.

## 7. Layer verdict

| Layer | Record result | Fibonacci result | Status | Caution |
|---|---|---|---|---|
| positive braid relation | positive L,R fail LRL=RLR | Fibonacci B1,B2 pass braid relation | fails for positive record pair | important correction: no braid skeleton with positive L/R |
| signed braid relation | signed Dehn twist pair can satisfy braid relation | braid group representations use invertible generators | possible geometric skeleton | requires negative entries / breaks record positivity |
| unitarity | L,R are not unitary | B1,B2 are unitary | fails | record matrices are count/geometry maps, not quantum gates |
| phase eigenvalues | L,R eigenvalues are 1; A eigenvalues are real positive phi^±2 | R-symbol eigenvalues are complex roots of unity | fails | need extra cyclotomic phase data |
| quantum dimension | PF eigenvalue/eigenvector contains phi | quantum dimension d_tau=phi | passes at dimension level | dimension is not phase |
| topological quantum anchor | fusion counts + probability bridge, no phases | requires F and R data | not promoted | R-symbols not derived |


## 8. Gate verdict

| Criterion | Status | Evidence | Meaning |
|---|---|---|---|
| recover positive braid relation | fail | Positive L,R do not satisfy LRL=RLR; error is nonzero. | no braid-group skeleton inside positive record shears |
| recover signed Dehn-twist braid skeleton | partial_pass | A signed companion R_minus satisfies the braid relation with L. | possible geometric bridge only after leaving positivity |
| recover R-symbol phases | fail | R-symbols are complex phases e^{-4pi i/5}, e^{3pi i/5}; record matrices are real positive/integer. | phase data not present in current record layer |
| derive phases from A eigenvalues naturally | fail | Mapping real growth e^{±mu} to phases requires arbitrary/fitted scale c. | no natural Wick/phase map yet |
| recover quantum dimension / real shadow | pass | A and N_tau contain phi and Q(sqrt(5)) real data. | dimension/count layer remains valid |
| promote to topological quantum anchor | not_promoted | Braid phases and full unitary representation are not derived. | remain at fusion-count/probability bridge, not anyon-amplitude theory |


## 9. Honest conclusion

Allowed:

> The record model reproduces Fibonacci fusion-count/dimension data at the persistent-sector level and has a conditional probability bridge to |F|².

Also allowed:

> A signed geometric Dehn-twist layer near the record construction can satisfy a braid relation.

Not allowed:

> The positive record model derives Fibonacci anyon braiding phases.

Current status:

```text
fusion count: pass
probability bridge: conditional
positive braid relation: fail
signed braid skeleton: partial/geometric
R-symbol phases: fail/not yet
topological quantum anchor: not promoted
```

## 10. Next recommended action

Proceed to **G5: update the reality-check ledger after G4D**.

Reason:

This is an important correction. We should freeze the claim boundaries before exploring G4D2.
