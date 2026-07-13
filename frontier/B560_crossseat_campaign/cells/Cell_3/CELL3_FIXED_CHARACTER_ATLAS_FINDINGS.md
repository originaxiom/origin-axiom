# Cell 3 — Fixed-Character Local Atlas and the Global Completeness Gate

## Repository baseline

```text
383d20f97f83c1453103e38797a2b2690d9b1135
```

No repository files were modified.

## Executive result

Cell 3 does not prove a globally complete fixed-character scheme. It does produce a much stronger certified local atlas:

\[
oxed{253	ext{ recovered support points}=247	ext{ irreducible}+6	ext{ reducible}.}
\]

Among the 247 recovered irreducible characters, 246 are interval-certified reduced isolated points and one is the exact isolated nonreduced trace-zero double point.

The global statement “there are exactly 253” remains open because no exact degree or intersection-number upper bound has been established.

## Numerical discovery

The campaign used 6,000 standard determinant-compatible random starts and 3,600 wide log-scale starts. There were 4,943 successful root solves. The standard family stabilized at 251 support points; the wide family found two additional real irreducible points. No new point appeared during the final 1,800 starts.

This is strong saturation evidence, not a proof of exhaustion.

## Local certification

Each non-special irreducible root was refined at high precision and enclosed by a complex interval Krawczyk box for the 16-variable gauge-fixed system.

```text
KRAWCZYK-CERTIFIED SIMPLE ROOTS       246
FAILED CERTIFICATES                   0
MAXIMUM INCLUSION RATIO               < 9.72e-13
BOX RADII                             1e-18 OR 1e-22
```

Every box proves existence, local uniqueness, reducedness, isolation and irreducibility. The trace-zero point has exact completed local algebra

\[
\widehat{\mathcal O}_{X,x}\cong\mathbb C[[arepsilon]]/(arepsilon^2).
\]

Therefore the recovered irreducible scheme has certified length at least

\[
246+2=248.
\]

## Six reducible characters

The abelian eigencharacters are controlled by

\[
\operatorname{coker}(I-M)\cong\mathbb Z/11.
\]

With charge vector \(Q=(1,3,6,7)\), the eleven diagonal eigencharacters are \(g\mapsto\zeta_{11}^{mQ(g)}\). Weyl inversion identifies \(m\sim-m\), leaving exactly six semisimple reducible character points represented by \(m=0,1,2,3,4,5\). All six commutator traces equal 2.

Their support set is exact. The transverse local fixed-character multiplicities at the reducible quotient locus are not fully certified.

## Observable separation

The rigorous \(\kappa_{ab}=\operatorname{tr}[a,b]\) rectangles of all 246 simple irreducible boxes are pairwise disjoint, and none contains the trace-zero value \(-2\). Thus

\[
oxed{\kappa_{ab}	ext{ set-theoretically separates all 247 recovered irreducible characters}.}
\]

The smallest numerical center gap is approximately 0.007628205499.

However, at the trace-zero double point,

\[
d\kappa_{ij}(v)=0
\]

for all six commutator traces. Therefore \(\kappa_{ab}\) identifies the support point but misses its nilpotent echo. In contrast,

\[
oxed{d\operatorname{tr}(a)(v)=-rac{3\sqrt3}{2}i
e0.}
\]

Hence the pair

\[
oxed{(\kappa_{ab},\operatorname{tr}(a))}
\]

separates all 253 recovered support points and detects the known nonreduced tangent.

## Completeness blocker

An exact global total requires one of:

1. a Gröbner/elimination degree of the fixed-character ideal;
2. a mixed-volume computation and certified homotopy path count;
3. a compactification/Lefschetz intersection bound;
4. an equivalent exact resultant of degree 253.

None is presently available. Therefore hidden additional characters are not excluded.

## Physics interpretation

The fixed-character space is independent of the prefix protocol that conditioned Cell 2. The recovered picture is a large finite-looking field of rigid interaction states plus one exceptional state with an obstructed infinitesimal echo. One relational observable identifies the recovered irreducible support; a second observable is needed to see the hidden nilpotent structure.

This is not yet a physical energy spectrum: no Hamiltonian, measure, transition amplitude or state-selection principle has been supplied.

## Final ledger

```text
RECOVERED SUPPORT POINTS                    253
RECOVERED IRREDUCIBLE SUPPORT POINTS        247
INTERVAL-CERTIFIED REDUCED IRREDUCIBLES     246
EXACT NONREDUCED IRREDUCIBLE DOUBLE POINT   1
EXACT REDUCIBLE SUPPORT CHARACTERS          6
KAPPA_AB SEPARATES IRREDUCIBLE SUPPORT      PROVED ON CERTIFIED ATLAS
KAPPA_AB DETECTS NILPOTENT TANGENT          REFUTED
TRACE_A DETECTS NILPOTENT TANGENT           PROVED EXACTLY
(KAPPA_AB, TRACE_A) SEPARATES RECOVERED SET YES
GLOBAL EXHAUSTION AT 253                     OPEN
CELL STATUS                                  BLOCKED BY GLOBAL DEGREE CERTIFICATE
REPOSITORY WRITES                            NONE
```

The governed campaign now proceeds to Cell 4 — Degree-4 Spectral Measurement Theorem.
