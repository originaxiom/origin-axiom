# recompute/ — run-output naming note (2026-09-01)

`.gitignore` ignores `*.log` and `*.out` (also `*.log1`, `*.log2`) repo-wide. Twenty-three of
this seat's R-cell run outputs were written under those suffixes and were therefore silently
absent from the pushed tree — the same E51-class gap this seat flagged against B1148's runner
(`reproduce_new.sh` cites `reproduce.log` / `our_uniqueness_chain.out`, uncommittable as named).

Fix applied here: every such output is committed as a `<original name>.txt` twin, e.g.
`R06_simultaneous_closing/r06_run.log.txt`, `R10_exact_hypercharge/r10_blind_solve.out.txt`,
`R12_spin_payment/blind_recompute.out.txt`, `R17_value_scans/b1137_rerun/real_run.log.txt`,
`R24_b1163_chain/recompute.out.txt`, `R25_torsor_4of48/run.log.txt`. Where a cell's FINDINGS
names the `.out`/`.log` file, read the `.txt` twin; FINDINGS texts were left as written (the
names are the ones the scripts actually produce on a re-run). The ignored originals may still
sit beside the twins in a working checkout; the twins are the witnesses.
