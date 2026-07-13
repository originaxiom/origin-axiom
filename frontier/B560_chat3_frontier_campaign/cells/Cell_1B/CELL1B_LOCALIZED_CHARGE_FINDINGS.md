# Cell 1B — Localized Z/11 Charge Carriers

## Main result

The universal mod-11 charge has finite localized carriers.

A defect is an exact pair

\[
L\,u\,R,\qquad L\,v\,R
\]

with the same three-letter left and right contexts and equal core lengths. Its
charge is

\[
\Delta Q=Q(v)-Q(u)\pmod{11}.
\]

Explicit witnesses realize every nonzero residue:

| charge | first core length in the frozen exact census |
|---:|---:|
| 1 | 3 |
| 2 | 9 |
| 3 | 3 |
| 4 | 16 |
| 5 | 14 |
| 6 | 14 |
| 7 | 16 |
| 8 | 3 |
| 9 | 9 |
| 10 | 3 |

Therefore

\[
\boxed{\text{all ten nonzero classes of }\mathbb Z/11
\text{have explicit finite localized carriers}.}
\]

Shortest witnesses include

\[
\texttt{abA}[\texttt{ABa}]\texttt{ABa}
\to
\texttt{abA}[\texttt{Bab}]\texttt{ABa},
\qquad\Delta Q=8,
\]

and

\[
\texttt{BaA}[\texttt{Bab}]\texttt{ABa}
\to
\texttt{BaA}[\texttt{abA}]\texttt{ABa},
\qquad\Delta Q=10.
\]

The reverse orientations give charges 3 and 1.

**Status:** `PROVED BY EXPLICIT EXACT WITNESSES`

## Inflation transport

Since \(Q(\sigma(w))=Q(w)\),

\[
Q(\sigma^n(v))-Q(\sigma^n(u))
=
Q(v)-Q(u)\pmod{11}.
\]

The common contexts inflate identically. Every carrier therefore has an exact
hierarchy of larger carriers with the same charge.

**Status:** `PROVED EXACTLY`

## Spectral control

For the conditioned onsite model

\[
H=\text{nearest-neighbor adjacency}+\operatorname{diag}(V),
\]

with

\[
V(a)=1,\quad V(b)=4/5,\quad V(A)=3/5,\quad V(B)=2/5,
\]

defects with the same charge can have different exact values of

\[
\Delta\operatorname{Tr}H,\qquad\Delta\operatorname{Tr}H^2.
\]

This occurs already for charges 3 and 8 by core length 30.

Thus

\[
\boxed{\Delta Q\text{ alone does not determine spectral response}.}
\]

The charge is structural, while its energy signature remains conditioned on
the carrier shape and Hamiltonian.

## Physics status

Established:

- observer-independent Z/11 charge;
- finite carriers for every nonzero charge;
- exact charge preservation under inflation.

Open:

- allowed motion;
- binding and annihilation;
- dynamic stability;
- gauge-field interpretation;
- physical-particle identification.

The correct current term is:

> scale-transported localized torsion-charge carriers.

## Next computation

Construct the finite graph of admissible local rewrite moves. Determine whether
charged carriers can move, combine, split, or annihilate while conserving total
charge.
