# Explicit delegation counter

The second six-fixture run at 517a5fc4c passed and is preserved in
SECOND_RUN.txt. Subsequent source review found that the first fixture's
name and design say delegates once, but its overwritten binding record
would not detect repeated identical delegation. That is a coverage gap,
not a production-wrapper failure or a reason to erase the earlier run.

The sentinel now appends its import marker and increments a call counter;
the binding fixture requires one import and exactly one delegation.
The six cases, production wrapper, scientific sources and acceptance
requirements are unchanged. The additional assertion strengthens the
original declared criterion. A third run is recorded separately.
