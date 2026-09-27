# First-run instrument correction, separately sealed

The initial producer at seal 02ea6154290a34e362337a1e9a36c947ee35d9f8
exited 1 while serializing the first certificate: SymPy factor
multiplicities were symbolic Integers, which ordinary json.dumps rejects.
The accompanying focused suite exited 1 with five passing tests and one
failure: the synthetic determinant was exactly -t^2+t, but the expected
Poly used ZZ while the producer's explicitly declared domain was QQ.

FIRST_FAILURES.json preserves both exact terminal receipts and traces.
No exceptional-root diagnostics completed in that producer run.

Repairs: convert factor multiplicities to Python int at the output boundary;
specify QQ in the synthetic comparator; add a JSON round-trip assertion
to that comparator. No relator, representation, minor selection, target
rank, expected scientific result or scope changes. Both failed processes
were terminal before these edits. Hash and commit before rerunning.
