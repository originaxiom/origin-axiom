# F15 implementation correction, before any actual tangent result

The original sealed run (8fb4cbcd; session 84962) terminated with exit
1: **13 failed, 1 passed in 2.83s**. Full emitted output is FIRST_RUN.txt.
All thirteen failures are the coordinate guard comparing an algebraic
number ANP to Python integer 0. The installed ANP equality methods return
NotImplemented on unsupported coercion (source inspection 48944d), so
an exact field zero was incorrectly rejected. The rational-field trivial
representation control passed. No actual exceptional tangent dimension
or obstruction was computed by the failed run.

The new adapter compares the trace with its OWN field's k.zero. Nothing
else in the producer is changed. The original four scientific files and
original tests remain frozen. Every original test is rerun unchanged,
with the corrected producer binding. Additional two-field controls
accept a zero trace, reject identity/nonzero trace, and explicitly
reproduce the original defect. No physical expectation is weakened.

The failed-run record concatenates the exact tool-returned stdout;
no internal whitespace or traceback is elided. Its final newline is
normalized to one newline when adding the text file. No source edits
occurred while the failed test session was live.
