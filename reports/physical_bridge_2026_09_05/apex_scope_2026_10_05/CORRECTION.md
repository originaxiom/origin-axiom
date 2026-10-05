# First execution and pre-rerun repair

First seal3610c481269b168514e1b1acac5c73250a0bfc92 pushed and server-
confirmed before imports. Native37 checks and separate reference checks
passed; the LIVE suite returned one failure/seven passes. Its rejection
control attempted to mutate an immutable SymPy Kronecker result. Replace
that copy with an explicit mutable matrix. No mathematical result is
changed by that test-instrument repair; the failed log is retained.

Personal post-run provenance review also found that the native Hermite
basis was mathematically equivalent to, but differently labelled from,
B1365's stated basis. Central defects depend on the chosen adjoint
representative, so original coordinates must not be called B1365's
coordinates. Reconstruct the lattice, verify the unimodular transition,
then use B1365's (1/6,1),(0,5) basis explicitly. Add a check of the four
banked adjoint keys. The semantic SU6 census must still agree with the
separate direct-phase implementation. Keep original native/reference
logs and their original lifted representatives. Do not overwrite them.

Corrected probe and test plus this note are resealed, committed, pushed
and server-confirmed before new imports/collection. This is not an
unchanged-first-pass certificate. The first metadata display also used
a Ruby Array method unavailable in the installed version; it affected
only a printed witness-length summary, not either scientific output.

The scope/proof and physical limitations stand. No main-bank promotion,
nonauthor acceptance or physical goal completion is earned by a repair.
