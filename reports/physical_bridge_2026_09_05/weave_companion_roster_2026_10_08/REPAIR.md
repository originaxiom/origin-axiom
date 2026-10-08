# Symbolic equality check repair

The first run at pushed pre-run seal e6830c6d4977e3bd0535d96f8fe632243d4ad617
returned exit1. The only false predicate was norm_coordinate_change. The
test used direct structural equality for two symbolic exponential forms.
The separate critical and regular exponent predicates both passed, as
did all weight, spectrum and mass predicates. Reference and pytest jobs
did not run because the custodian stopped at the first nonzero exit.

Repair: replace structural equality by simplify(lhs-rhs)==0, the intended
mathematical equality. Add a wrong-exponent control that must remain
nonzero. No norm, predicted spectrum, module, physical assumption or
acceptance target is changed. This verifier repair is post hoc and is
sealed again before rerun. The first output and exit receipt are retained
byte-faithfully in FIRST_NATIVE.json and FIRST_NATIVE_RECEIPT.json; the
first pushed seal remains the immutable original source record.

The revised seal includes this disclosure and the changed probe. It
does not overwrite the original ledger row or erase the failed attempt.
