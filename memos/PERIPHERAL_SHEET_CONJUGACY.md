# The peripheral equality is a specialization of a global sheet conjugacy

## Verdict

The literal statement

\[
\operatorname{tr}(ab^{-1})=3-\kappa
\]

is **false on the full nonabelian m004 Riley component**.  It is exact on the
parabolic divisor, including both selected geometric characters.  The stronger
global statement is:

\[
\operatorname{tr}(ab^{-1})=\sigma(\kappa),\qquad
\sigma(\kappa)=x^2-1-\kappa,
\]

where \(x=\operatorname{tr}a=\operatorname{tr}b\) and \(\sigma\) is the
quadratic deck involution of the Riley component.

## Exact derivation

In trace coordinates the component is

\[
P(x,z)=z^2-x^2z+2x^2-z-1=0,
\]

with \(z=\operatorname{tr}(ab)\).  Fricke identities give

\[
\tau:=\operatorname{tr}(ab^{-1})=x^2-z,
\quad
\kappa=2x^2+z^2-x^2z-2.
\]

Modulo \(P\), \(\kappa=z-1\), hence

\[
\tau+\kappa-3=x^2-4.
\]

The two roots of \(P\) are exchanged by
\(z\mapsto x^2+1-z\).  Under that involution,

\[
\kappa\mapsto x^2-1-\kappa=\tau,
\]

and \(\kappa\) obeys

\[
K^2-(x^2-1)K+(x^2-1)=0.
\]

Thus the component-generic conjugate is not the constant expression
\(3-\kappa\).  It specializes to it exactly when \(x^2=4\).  On the selected
\(x=2\) slice, \(P(2,z)=z^2-5z+7\), giving the two Galois-conjugate geometric
characters and the memo-54 equality scheme-theoretically.

The point

\[
x=0,\qquad z=(1+\sqrt5)/2
\]

lies on the same component and gives \(\tau+\kappa-3=-4\), an explicit
counterexample to any component-wide constant-conjugation reading.

## Consequence for the ledger

- OA-C1083's literal full-component question is `REFUTED`, not `PROVED`.
- Memo 54 correctly closes its residue after narrowing the statement to the
  parabolic scheme.
- The global replacement theorem—quadratic sheet conjugacy—is exact and does
  not require a holonomy-point specialization.

This remains character-variety algebra.  It supplies no spacetime field,
dynamics, coupling value, or Standard-Model parameter.

## Certificate

`certificates/r008_peripheral_sheet_conjugacy.py` uses exact SymPy polynomial
arithmetic and contains both the parabolic proof and the generic counterexample.
