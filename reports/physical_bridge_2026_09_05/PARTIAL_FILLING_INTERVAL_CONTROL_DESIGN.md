# Interval receipt repair — before control execution, 2026-09-07

BANKED IDENTITY: named partial-filling source and interval runner, sealed
b5924cca before execution; all scientific equations and targets unchanged.
PRIOR ART: first interval JSON and failure receipt are preserved. The
100/160-bit certificates themselves return hyperbolic=true and positive
distance from the quarter lattice; the final checker raises TypeError
when Sage QQ is passed a decimal-string distance. Its algebraic rational
parser expects an integer/fraction string, not that decimal notation.

P0: the same named degree-five partial filling, controls and precisions.
P6: fix serialization only. Override quarter_lattice in a separate import
instance: keep the decimal for reading, and pass the exact rational value
of the MPFR lower endpoint to the old checker as numerator/denominator.
This does not turn a rounded printed decimal into a certified endpoint.
The old interval runner and all assertions remain unchanged on disk.
Repeat the complete verification, not just a string substitution in the
old output. Original first failure stays a failure, not rewritten green.

One additional independent check protects the normalization: convert the
verified CS interval to an exact rational enclosure and prove that adding
1/4 encloses the high-precision numerical class near 0.15759004, up to
the inherent quarter ambiguity. The decisive exclusion continues to use
native interval arithmetic. No exact rational CS value is claimed.

Seal design/source before this control. No B number or physics promotion.
