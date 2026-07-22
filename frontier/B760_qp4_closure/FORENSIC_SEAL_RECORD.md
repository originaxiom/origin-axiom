# Forensic seal record (B760) — banked so the proof outlives the transcripts

The FINDINGS cite prereg seal `98201bd3` (sha256). The committed PREREGISTRATION.md
hashes fbeafc43 — because at 14:13:04 the sealed file was EDITED to insert its own hash
("This file is sealed before compute.py runs." → "`98201bd3` (sha256, first 8 chars).
Sealed before compute.py runs."). Reconstruction verified at the cc gate (2026-07-22):
the committed file MINUS that one-line annotation hashes to exactly 98201bd3 — the seal
is valid and the edit provably cosmetic. Transcript forensics: the prereg's single Write
at 13:55:56 hashes sha256 98201bd3 directly. Convention trap named at the gate: NEVER
WRITE THE HASH INTO THE SEALED FILE (the self-referential seal) — annotate in
FINDINGS/SEAL_LEDGER instead.
