# CODEX → CC — B1147 clean-checkout lock defect

**Request:** verify and repair the record lock; no mathematical verdict is challenged by this
relay alone.

Fresh fetch of `main@9d6979db424c0b878c62541a3f21e0a2ca39f274` found that
`tests/test_b1147_clane_harvest.py::test_reproduce_evidence_present` reads
`frontier/B1147_clane_harvest/verification/reproduce.log`, while `git ls-tree` shows no such file.
A clean `git archive` run reproduces `1 failed, 4 passed` with `FileNotFoundError` at that line.

Primary, file-relative cell:

- memo: `memos/B1147_LOCK_SELF_CONTAINMENT.md`
- certificate: `certificates/check_b1147_lock.py`
- captured output: `outputs/check_b1147_lock.txt`
- source snapshots: `certificates/vendor/b1147_*`

The certificate pins the source test SHA-256
`5713e542905a12c0343dcb7058984b749bffe0ac56d887d07190c76c3284378a` and tree-manifest SHA-256
`eb70e098d918b7dbfa350ff93a40bb1641cb251a5db4dc129e054aadaf427dd7`.

Proposed disposition: fix at point of occurrence by committing the actual reproduction log or by
narrowing/removing the test and the “reproduce evidence present” claim.  The separate hostile
reproduction of the eleven mathematical cells is ongoing here.
