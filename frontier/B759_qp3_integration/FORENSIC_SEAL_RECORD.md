# Forensic seal record (B759) — banked so the proof outlives the transcripts

The FINDINGS cite prereg seal `192c3032`. The committed PREREGISTRATION.md hashes
sha256 8b0b2ff0 / sha1 426386ee — NEITHER matches, because the seal was taken with
`git hash-object` (SHA-1 over "blob <len>\0<content>"): the git-blob hash of the
committed file IS `192c303264380a6f04b5446cf2c7f7ad58c6c079` (verified at the cc gate,
2026-07-22: `git show <commit>:...PREREGISTRATION.md | git hash-object --stdin`).
Transcript forensics (cc3 session, preserved extracts): the prereg was written ONCE at
13:23:00, the seal command (`git hash-object frontier/QP3_integration/PREREGISTRATION.md`)
ran at 13:23:06, compute.py was written at 13:24:27 — seal-first HOLDS; the file was
never edited. Convention trap named at the gate: A SEAL MUST NAME ITS ALGORITHM.
