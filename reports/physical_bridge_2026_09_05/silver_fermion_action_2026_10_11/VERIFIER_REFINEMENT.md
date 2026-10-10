# A passed control still needs an accurate name

Initial science pushed at a2b1c6601b1c3b1611d28ddc78c167fbeca51018.
Both initial producers passed (22 native/27 reference); focused7 and
four-packet32 tests passed. Their literal stdout and receipts are retained.

During adversarial self-review the native control `wrong_chi_degree_rejected`
was found imprecisely named. It computes Q S_even-S_odd R, whereas the
correct equation is Q S_even=S_odd R*. The nonunitary Higgs fixture makes
that residual nonzero. It rejects substituting R for its actual adjoint,
NOT a standalone assignment of the gaugino to degree zero: for a unitary
coefficient R=R*, and this residual alone cannot distinguish those maps.

Rename the predicate `wrong_adjoint_operator_rejected` in producer and
focused lock. No calculation, fixture, criterion, operator, domain or
scientific conclusion changes. PRESEAL_REFINEMENT rehashes those two files
and preserves the other five hashes. Push before authoritative reruns.
This is a label/scope refinement after successful execution, not an erased
failure or an outside review. The original scripts remain reachable in the
initial commit; original PRESEAL and successful first outputs are retained.
