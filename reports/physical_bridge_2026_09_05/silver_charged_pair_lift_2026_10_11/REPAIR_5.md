# Explicit source field for the guarded converter

At983d5269fd8834bef00cb9d306843cf03a674cca the new native converter
failed after10.579835s while coercing an ANP quadratic coefficient into
K(q). Domain.convert cannot infer the source AlgebraicField from that
ANP instance. Pass the already-declared source K explicitly, exercising
the pinned local from_AlgebraicField path. One argument only is changed.

The literal failed transcript, raw/public path-redaction hashes and
receipt remain. Neither the matrix nor its type is reinterpreted, and
unknown fields are still rejected. All original/new opposing controls,
reference, physical criteria, proof, model, inputs and tests remain.
Repair/seal/push precedes the next replay. A typed implementation error
is not a physical obstruction and the failed run is not a certificate.
