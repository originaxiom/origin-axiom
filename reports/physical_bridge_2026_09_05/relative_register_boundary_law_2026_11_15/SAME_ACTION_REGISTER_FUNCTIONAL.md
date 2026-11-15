# The retained transition has a response supplied by the existing action

2026-11-15. Author analytical continuation after the first check output
was sealed at `86ec6ef9a`. This reuses the November 8 core/tail solution
and makes its connection to the relative-reference calculation explicit.
It leaves the frozen checker and proof bytes intact.

## 1. Integrate the fields on both sides of the actual transition

Retain the old complete punctured surface, stationary seed, commuting
generator H, positive generator norm c_H and coupling G=g6^2.
Let a finite cut divide the area as A_C+A_T=A. The old transition
`U(x)=exp(-i phi(x) H)` identifies the tangential connection frames by

\[
 A_C|=A_T|-H\,d\phi,\qquad \oint d\phi=\Phi=2\pi n.
\]

This is a change of connection frame with retained end data. It does
not introduce the boundary matter field of equation (2) in `PROOF.md`.
In the old common-coordinate orientation, let b be the tail circulation.
The already derived exact static responses give

\[
 \Gamma(b,\Phi)=\frac{r_C}{2}(\Phi-b)^2+\frac{r_T}{2}b^2,
 \qquad r_C=\frac{c_H}{G A_C},\quad r_T=\frac{c_H}{G A_T}.
                                                               \tag{1}
\]

Here both response coefficients come from the same action and actual
metric. There is no extra local boundary stiffness to choose in (1).
Periodic zero-winding changes of phi can be absorbed by the corresponding
extendible frame changes while transporting the fields. Flat core periods
remain in the full system, as in the recovered source.

Eliminating the seam circulation gives

\[
 b_* =\frac{r_C}{r_C+r_T}\Phi=\frac{A_T}{A}\Phi,
 \qquad
 \Gamma_{\rm reg}(\Phi)=\frac12\frac{r_Cr_T}{r_C+r_T}\Phi^2
                    =\frac{c_H}{2G A}\Phi^2.             \tag{2}
\]

The core and tail physical curvatures are both Phi/A. Moving the
artificial cut changes b_* and the individual coefficients in (1),
while preserving this curvature and the final functional in (2).
The rational cut controls in run01 recover this identity on three
different cuts. The original infinite-dimensional mean-response proof
supplies its metric and attainment hypotheses.

This supplies a precise conditional reduction for the boundary-response
coefficient. Once the register is identified with this actual transition,
the earlier arbitrary kappa is replaced by the response of the retained
region. The identification itself, the parent, metric, circle embedding
and the nonzero transition sector remain physical inputs or derivation
duties. The result reuses an owned response and does not add a new
fundamental law.

## 2. Why this differs from an independent seam phase

In the separately supplied seam-source model, the two regions are
trivially glued and a new field couples to their common connection.
Its action is

\[
 \frac{r_C+r_T}{2}b^2+\frac p2(b-2\pi n)^2.
\]

The core and tail added fluxes then cancel. Its current and location
are physical source data. In (1), the transition changes the relative
gluing, and the total added flux is Phi. Thus a match of the two scalar
Schur-complement shapes cannot identify their global connection data.
Their fields, frames, source currents and end conditions decide that map.

## 3. A boundary reference by itself does not supply equation (1)

The example with F=0 and a wound reference has nonzero relative class
because its boundary eta is nonzero. Equation (1) additionally assumes
the old physical end law and that transition's actual connection
matching. It thereby determines how much of the relative datum is
carried by physical curvature. Specifying the reference and deriving
its admissible end behavior are separate mathematical tasks.

For a physical unit-carrying end law, the most direct next calculation
is to transport the source's asymptotic trace and normal derivative
into main's modular extension lattice. It must show that the same
integer labels the two domains. It must also retain both spin and
central frame actions, the norm and the full argument map. The earlier
harmonic-transport draft's missed argument factor is a relevant failure
to preserve, so a fibrewise coefficient match alone cannot complete it.

## 4. The remaining dynamical selection problem is explicit

The retained transition energy is

\[
 \Gamma_n=\frac{2\pi^2c_H}{G A}n^2.
\]

Its topology permits all integers. Its supplied positive static action
prefers n=0. A separate restriction to nonzero transitions makes the
two unit sectors the minima. A derivation which changes that preference
must retain the additional physical terms and their normalization.

For example, an instability of the populated zero-added-flux seed could
provide a dynamical route, if the full matter/source action actually
has that instability and a stable finite-amplitude endpoint. The
source's nonzero magnetic stationary saddle and its charged instability
do not decide this distinct question. The actual complete fermion
operator, its zero modes and the magnetic determinant must enter the
same effective functional. Replacing them with flat-character spectra
would recreate the X-ENDGAME mismatch.

The existing modular result already gives three per one supplied end
unit. Selecting a physical unit and earning that operator/domain map
therefore remains a candidate route to input reduction. The present
calculation establishes the mean response which that route must use.
