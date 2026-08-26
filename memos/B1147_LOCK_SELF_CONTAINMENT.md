# R005 — B1147 clean-checkout lock defect

## Verdict

At immutable Origin Axiom commit
`9d6979db424c0b878c62541a3f21e0a2ca39f274`, the
[B1147 fast test](https://github.com/originaxiom/origin-axiom/blob/9d6979db424c0b878c62541a3f21e0a2ca39f274/tests/test_b1147_clane_harvest.py)
requires

```text
frontier/B1147_clane_harvest/verification/reproduce.log
```

but that path is absent from the commit tree.  A clean archive therefore gives one failure and four
passes for that test module; the failure is `FileNotFoundError` in
`test_reproduce_evidence_present`.

The self-contained certificate vendors the exact test and exact B1147 tree-path manifest, pins both
SHA-256 digests, and proves the required path is absent.  Reproduce from any checkout and cwd:

```text
python3 certificates/check_b1147_lock.py
```

## Scope

This is a self-containment/record-lock defect.  It does not refute any of memos 30–40.  Their exact
claims must be assessed by independently rerunning the outside-bench certificates.  The repair is
to commit the actual reproduction log (and pin it) or change the test and findings so they do not
claim committed evidence that the tree does not contain.
