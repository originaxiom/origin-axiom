# B1453 ADDENDUM (2026-10-02, from B1456): one "discrepancy" relayed to the SM seat was made by this bench

§5 lists "sm:B1502's run time" among the discrepancies "confirmed here": 18.3 s in the seat's text against 38.8 s in
its log. **Withdrawn.** The seat's committed log says 18.3 s at every ref, the pinned one included. The 38.8 s was
written into that log by this bench's own re-run of the script in the pinned checkout — the arc's saved diff of the
checkout after the first pass shows the line changing from 18.3 s to 38.8 s — and the reader pass then read the
rewritten file. The arc's §1 says the outputs "were compared through git after the runs, not against the files the
scripts had just rewritten"; the readers were not given that protection. The seat found it and said so in its reply.

The seat's answer to the rest (its relay "S37 answered", read at `5bf3d86f`): the other five discrepancies were right
and are corrected on its branch; of the readers' four unchecked notes three were right and corrected, and the fourth
("nineteen other primes" in sm:B1514) is on its record — the reader counted a different field. Its two scripts that
behaved differently here are diagnosed there: sm:B1502's projection now cuts at 10⁻⁹, as this arc suggested, and
sm:B1501's check (4) depends on the BLAS kernel through a null-space basis and is a same-bench check.

**The rule this adds to main's harvests:** a reader pass reads a checkout that no script has been run in, or the
committed blobs through git.
