# F01 implementation correction, before second execution

The first execution of the sealed producer exited 1 in projection_ranks:
SymPy reported `nonlinear term: im(p1)`. The generic matrix simplifier used
expand_complex on unconstrained complex projection unknowns. That replaces
p1 by re(p1)+i im(p1), so the solver no longer receives a linear expression
in its declared unknown p1. This is an implementation failure, not evidence
against the representation, its index, or the analytic proof.

The original verify.py, test_verify.py, SEAL.json and first raw output remain
unchanged. verify_v2.py uses algebraic simplify, without expand_complex,
specifically in the complex-linear projection equations; its only other
change selects SEAL_V2.json. test_verify_v2.py changes only the module path.
No hypothesis, expected mathematical outcome, or success criterion changes.
This correction is post-first-run and sealed before its own execution.

The first shell hashing attempt also failed before execution because the
configured C.UTF-8 locale was unavailable. LC_ALL=C recovered hashing.
No scientific output was produced by that administrative failure.
