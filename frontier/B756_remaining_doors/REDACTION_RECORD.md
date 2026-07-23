# Redaction record — RAW_WORKFLOW_OUTPUT.json (2026-07-22, the fourth-pass audit)

The hash-sealed raw workflow log (cc2's seal 1c4920b5…, SEALS.txt) contained the banned
AI-model token at 9 sites ("model" fields) — hidden from the attribution gate by the
per-file exemption that its sealed status had justified. The exemption is REMOVED and the
file REDACTED instead; the seal remains verifiable by reconstruction:

- original sha256: `1c4920b5bfb1c28184825de0a9a6396dec4da3c38829c633cdd60e4ade06a00d` (= the SEALS.txt entry)
- transform: every occurrence of the banned token family → `[redacted-model]` /
  `[redacted-per-attribution-rule]` (12 replacements total: the 9 model fields + 3 harness-path tokens; deterministic regex, case-insensitive)
- redacted sha256: `e5221618126fd229abe96dd74a88f8395ca26cb49da348371e1286def96772a8`

Anyone holding the original (the cc2 seat archive; the relay zip) can verify: apply no
transform and hash. The redaction touches ONLY the banned tokens — no computation content,
verdicts, or timestamps changed. Redaction-with-record supersedes exemption as the standing
pattern (the gate goes blind behind exemptions; it stays sighted over redactions).

## Transform layer 2 (2026-07-23, the R28-9 path sweep — recorded per the layering pattern)

The redacted file was subsequently swept by R28-9 (seat-topology paths → placeholders):
- layer-1 (redacted) sha256: `e5221618…` (above)
- layer-2 transform: the standard R28-9 path replacements (repo → relative; seat dirs →
  `<seat>/`; home → `~`) applied to the redacted text
- layer-2 (current) sha256: `331e1148…`
Verification chain: original (cc2 archive) → redact → `e5221618` → sweep → `331e1148`.
