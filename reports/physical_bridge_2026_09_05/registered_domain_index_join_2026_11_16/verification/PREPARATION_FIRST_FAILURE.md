# First source-packaging failure

2026-11-16. The initial metadata-only specification builder stopped before
writing its specification or importing any mathematical module.

It tried to read the pinned main-branch input
`frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md` from this
branch's worktree and received FileNotFoundError. The source receipt
identifies a committed Git blob. That does not imply the file is present
on the physical branch.

The repair materializes each absent source from its exact receipt commit,
checks its SHA-256 against that receipt and stores it under this package's
sources directory. SOURCE_RESOLUTION.json records the original commit,
path and hash alongside the local review path. Existing inputs are also
checked against their recorded hashes. The scientific checks remain unrun.
