# Archive import: one binary upload remains

This branch is an incomplete archive until the recovery ZIP is committed and RESTORE_RECEIPT.json records a verified Git index. Importer tests are local tests, not evidence that the complete archive is already on GitHub.

## Upload exactly one file

Upload the unchanged `Weave_All_13_Runs_Artifact_Archive.zip` from the ChatGPT conversation to the ROOT of this branch:

`chatgpt/weave-physics-archive-2026-10-11`

Keep its filename unchanged. Do not upload it to main. No extraction or copying of individual research files is needed.

Expected size: **1,266,286 bytes**.

Expected SHA-256:

```
afdf14b8b0691db97345d5b947fb2bbea08de4872140667e1ccdcef860c1011e
```

The branch-only workflow `.github/workflows/weave-archive-01-13.yml` is triggered by that file's push. It checks the whole ZIP before writing files, restores all 291 recovery members under this directory, checks all 289 manifest entries and all 254 original ZIP members, and checks the Git index against the original blob hashes and file modes. Only then does it commit the restored files to this same branch. It never executes archived scientific programs and never merges or pushes to main. A concurrent branch change causes the normal fast-forward push to fail instead of overwriting it.

## Preserved content and scope

The recovery ZIP contains all thirteen original run ZIPs, the initial independent-audit ZIP, all 254 member files, the original manuscript, fifteen standalone snapshots, inventories and checksums. Original reports, mathematical derivations, scripts, failed attempts, corrections and logs remain unchanged. It is a file-artifact archive, not an official export of all chat-only wording or unsaved tool output.

The initial independent-audit ZIP was already transferred with a matching Git blob hash and is committed here now. The previous session's corrupt and partial transport blobs are not accepted into this archive. The remaining binary input is still in the conversation download, not certified as present remotely.

## Why this path

The connected GitHub write actions take text/base64 strings rather than a mounted-file upload. Previous manual encoded transfers produced checksum failures. The container also cannot resolve github.com for a direct git upload. This one-file GitHub upload avoids retranscribing compressed bytes.

Local restoration, repeat restoration, all-file Git staging (even with autocrlf enabled), corruption rejection, conflict rejection and bad-mode rejection were tested. See IMPORTER_LOCAL_TESTS.json. A local importer population-comparison correction is disclosed there; no scientific data was changed.

After success, read README.md and RESTORE_RECEIPT.json in this directory. The exact recovery ZIP remains in the branch root as an additional original backup.
