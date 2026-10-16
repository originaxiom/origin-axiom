# Explicit test assertions after the static checker finding

Science at pre-run460dca46e passed29/29each with identical full output.
At result8f65e96e7, first LIVE regression passed13tests192.60s,
capture193.682298s. Governance26PASS/fourFAIL26.635868s, including TWO
NEW test-vacuity paths in the existing failing category. Neither run
was restarted on a timeout or edited while active.331pins,17,672tracked
contents and index remained unchanged in both terminal captures.

The two flagged functions called check(cert,*names), whose BODY asserted
each computed predicate. They did fail on false predicates at runtime,
but the repository's AST checker intentionally does not follow arbitrary
helper calls and sees no assertion in those two test bodies. The gate
finding is retained; it is not waived or called an analytic refutation.

After BOTH runs were terminal, all331original pinned sources, original
INPUTS and ARTIFACT_HASHES were copied byte-faithfully into the failing
governance capture. Before copying, every source digest was checked
against its original manifest. Full raw governance and regression
streams/receipts/inventories remain at their original paths.

Repair: check returns the conjunction of the SAME predicates; each test
body now explicitly asserts it. An additional instrument test copies
the actual result, flips one computed gate toFalse and requires rejection.
No scientific producer, proof, criterion, input or output is changed.
analysis.py, probe.py, reference.py and PROOF.md must retain their
original460dca46e hashes. Reseal and publish BEFORE successor execution.

Two earlier validation launch commands used invalid Ruby -EUTF8 and
returned exit1 before Ruby evaluated any wrapper code: 'unknown encoding
name - UTF8'. No capture directories or scientific child existed at
those attempts. The declared -EUTF-8 was then used for the actual
captures. This is a command-launch error, not a failed scientific run;
the tool outputs are not invented as captured stdout/stderr files.

Keep all four older governance categories and the full untruncated
provenance/data-scope audit obligation. A fixed AST visibility issue
does not complete independent analytic, full-suite or physical acceptance.
