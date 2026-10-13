# Publication scope and preserved captures

First science is byte-faithful under results/first_science; the disclosed
metadata-only repeat is under results/resealed_science. Both native
stdout hashes are1028dea16c6e4416a17cac654bad08455e32bcc5ffef86d94067c59f6d700159;
both reference hashes are08be518c55e87aaab11781ceedf9a630cd3631ddccf8baa58644350466b699b5.
All four scientific stderr files are empty. No mathematical hypotheses,
producers, proof, criterion or tests changed between these captures.

results/selected_tests contains the original46-test stdout, empty stderr
and capture receipt at the second seal. It is selected regression, not
the full repository suite. Its tracked-tree and source-pin statements
refer only to that execution interval, before publication writing.

The first governance --help call unexpectedly ran the gates and is
preserved in the tool record, not as a reconstructed local stdout.
After its one new source-reference attribution item was repaired, the
next gate process completed and its stdout/stderr were captured intact
under results/governance_post_metadata. Its Ruby post-capture summary
failed on a UTF-8 character because File.read used US-ASCII. That parser
failure is in the tool record; it is not a gate or scientific failure.
No process duration/exit receipt is invented for that failed summary.
The raw output gives26 PASS/four inherited FAIL categories.

The next staged-publication capture, with correct UTF-8 decoding and a
saved process receipt, returned25 PASS/five FAIL categories. Its new
law-map-provenance failure was a publication-format error: unbanked
sublemmas had been put in a table that requires a numbered banked arc in
each row. No unrelated arc is added to satisfy that check. The same
sublemmas, proof references, live locks and limits are retained as an
explicit provisional list pending outside acceptance and normal banking.
This failed capture is preserved under results/governance_publication_failed.
No sealed scientific file or test criterion changed.

The final gate process returned26 PASS/four inherited FAIL categories in
16.026446s, with the law-map-provenance failure repaired. Its exit is1,
not full green. The original raw output and saved process receipt are
under results/governance_publication_final; stdout SHA-256 is
a8b30725d7b756c310b58db9346a6e65d14e35c8281da9efd13ce1c7625cf608.
This capture's Ruby2.6 summary also stopped after saving the process
receipt because Array.filter_map is unavailable. The summary was then
generated from the SAME preserved raw bytes using map/compact; the gate
was not rerun and no process result was inferred from a new execution.
Both wrapper errors remain in the tool record. Failed captures are
never overwritten, and raw logs are explicitly tracked despite the
repository's default log ignore pattern.

No baseline is raised and no stale relay is acknowledged on behalf of
its recipient. No main, foreign branch, PR, canonical GENESIS or shared
number is changed. Both exact implementations have one author. Specialist
review, full-suite/normal banking and the complete physical goal are owed.
