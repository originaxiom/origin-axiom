# Exact Wilson charge coefficients for the two relative gauge observables

October 27, 2026. UNREVIEWED author hand derivation. No scientific
producer/import/CAS/test run. Continue the specified stationary parallel
SM gauge phase and its declared SU5 hypercharge map. This does not
select a Wilson vacuum, compute a physical determinant or certify values.

## 1. Carry one Wilson coordinate through all fields

The source's hypercharge Wilson connection is flat, supported in the
compact core and commuting with the structure triple. Set Q=6Y, with
Q|5=diag(-2,-2,-2,3,3), and normalize its marked cycle holonomy as
exp(i theta Q). A charge-q mode sees the same character exp(i q theta).
The spin line, structure connection, potential and domain travel with
it; q is not an independently fitted sector twist. The source example
exp(2pi i T/7), T=12Y=2Q, corresponds to theta=4pi/7. Its choice is
still supplied; no special angle is selected by this calculation.

Let H_R(q) denote ONE fixed species' actual gauge-insertion/internal
spectral functional in gauge SU5 representation R with charge-q flat
line. It may be a regulated heat density before proper-time integration,
or a separately justified heavy determinant coefficient. Keep that
choice consistent throughout the equations. Do not call H a numerical
function or a finite determinant until its full operator/measure/domain
and matching prescription are admitted. Gauge multiplicities are not
included in H; they are the explicit coefficients below. Structure
representations (5_b,10_b,1_b) and physical spin species have different
H functions. No equality between those functions is assumed.

## 2. Derive the charge/index table, not a separate shift per observable

Normalize T2(2)=T3(3)=1/2 and T1=(3/5) Tr Y^2 over every SM multiplet,
including colour and weak spectator dimensions. For the SU5 fundamentals:

  R   SM sector        Q-charge       (T1,T2,T3)
   5  (3,1)               -2          (1/5,  0,1/2)
   5  (1,2)               +3          (3/10,1/2,  0)
  10  (3,2)               +1          (1/10,3/2,  1)
  10  (bar3,1)            -4          (4/5,  0,1/2)
  10  (1,1)               +6          (3/5,  0,  0)
  24  (8,1)                0          (0,    0,  3)
  24  (1,3)                0          (0,    2,  0)
  24  (1,1)                0          (0,    0,  0)
  24  (3,2)               -5          (5/2,3/2,  1)
  24  (bar3,2)            +5          (5/2,3/2,  1).

All entries follow directly by squaring hypercharges or tracing one
normalized nonabelian generator. Sums on each5,10,24 recover equal
indices1/2,3/2,5 respectively. Conjugate multiplets have opposite
Q-charge and the same index tuple; keep them with their actual conjugate
structure/spin operator rather than silently doubling one answer.

Define differences D21=K2-K1 and D31=K3-K1 for the SAME regulated
functional K. For each gauge representation their charge-resolved
contributions are exactly

  D21[5]=(1/5)(H_5(3)-H_5(-2)),
  D31[5]=(3/10)(H_5(-2)-H_5(3))=-(3/2)D21[5],            (1)

  D21[10]=(1/5)(7H_10(1)-4H_10(-4)-3H_10(6)),
  D31[10]=(1/10)(9H_10(1)-3H_10(-4)-6H_10(6)),            (2)

  D21[24]=2H_24(0)-H_24(5)-H_24(-5),
  D31[24]=3H_24(0)-(3/2)(H_24(5)+H_24(-5))
          =(3/2)D21[24].                                (3)

Gauge-singlet structure24_b contributes zero to these inserted traces.
For the real complete E8 roster use its actual species/trace weights
and sum5/bar5,10/bar10,24 with their own H functions. A physical gauge
loop includes external spacetime-spin and ghost factors. Equations
(1)-(3) give the GROUP-THEORETIC coefficients of those functions; they
do not determine the full physical factors or replace their derivation.
The proportionalities are useful two-sided controls PER representation,
not universal relations for the total threshold with different H_R.

## 3. Central-holonomy and symmetric-end recovery are exact

If theta=2pi n/5, the five holonomy is central. All charge phases within
a given R then coincide: differences of its listed charges are multiples
of five. Provided the full domain is carried by the same source symmetry,
the corresponding H_R(q) are equal WITHIN R. Equations (1)-(3) vanish.
They do not require that common central-twist value equal H_R(0).
This preserves the source's full-SU5 control without deleting its
possibly nontrivial central flat line.

The Wilson field is zero on the tail. There each R's asymptotic model
has no charge distinction and (1)-(3) vanish as in the prior six-
threshold computation. Complete global heat kernels can retain
core-travelling loops and need not vanish. No global equality is inferred
from an end coefficient, and no relative trace convergence is claimed
merely from writing these cancellations.

## 4. The Wilson-loop polynomial is fixed before geometric evaluation

Where a valid universal-cover heat/path representation is established,
a deck element with marked winding n receives z^(n q), z=exp(i theta).
All its nonabelian structure/spin transport remains in the geometric
coefficient; it is not replaced by a scalar torus kernel. In each R,
the group factor for that loop in the relative insertion is therefore

  P21^5(n)= (z^(3n)-z^(-2n))/5,
  P31^5(n)=-(3/2)P21^5(n),
  P21^10(n)=(7z^n-4z^(-4n)-3z^(6n))/5,
  P31^10(n)=(9z^n-3z^(-4n)-6z^(6n))/10,
  P21^24(n)=2-z^(5n)-z^(-5n)=2-2cos(5n theta),
  P31^24(n)=(3/2)P21^24(n).                              (4)

These finite Laurent polynomials are derived algebra, not a completed
infinite loop expansion or numerical heat calculation. Every n=0
factor vanishes: loops invisible to this Wilson character cannot
supply relative splitting. Not all noncontractible loops have n!=0;
ones in the character kernel cancel too. Central theta makes all
polynomials zero, supplying an exact positive symmetry recovery.
Conjugate paths/fields and their actual reality law must be paired in
the final physical functional. Do not drop imaginary terms by decree.

The entire unknown geometric loop weight is common to the charge
sectors of a fixed R because only the flat central character differs;
the structure triple commutes with gauge SU5. Finite-cutoff boundaries,
extra matter backgrounds or different domains could spoil this
factorization and would need an exhibited new map. They are not
assumptions to change after seeing the measured couplings.

## 5. What has been reduced and what remains to derive

Before: potentially unrelated sector corrections to three gauge readouts.
After: a single admitted Wilson field gives definite charges and the
coefficients(1)-(4); source-symmetric local terms cancel, and the unknowns
are explicit SAME-operator spectral functions H_R(q). No free correction
is allowed per observable while calling it an output. This is conditional
structure reduction, not a numerical prediction or new foundational
law. The Wilson angle/state, metric/action, charged domain, regulator,
light-mode split and geometric spectral functions remain priced duties.

Next recover the full real background-field operators and formulate the
relative heat trace on the actual core/cusp, with(1)-(4) as exact controls.
A controlled trace formula or convergent spectral solver may then evaluate
the derived family; only after freezing that calculation compare with
observations. A value calibrated from those observations is still an
input. A derived nonmatching curve is still a result, not something to
replace with target-minus-tree shifts.

No external empirical target was consumed in this proof, no new scientific
execution packet is admitted and no prior review scope is enlarged.
The actual smooth fixed-domain phase remains charged-index paired;
three generations and gravity are not supplied by these trace polynomials.
The full programme and its other generated phases remain live.
