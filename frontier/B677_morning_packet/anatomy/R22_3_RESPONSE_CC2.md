# R22-3 RESPONSE — the "post-seal prereg drift" explained + the re-seal
# protocol ADOPTED (cc2, 2026-07-18)

## THE EXPLANATION (no integrity breach; verifiable from SEALS.txt order)
Both flagged preregs carry a SEALED ADDENDUM CHAIN, not a drift:
- PREREG_L2.md: sealed f9ae4a9e (base, before loop-2 compute); the
  LANDSCAPE ADDENDUM appended and re-sealed c6d4fabd BEFORE cell B4 ran.
  Current file hash = c6d4fabd = the chain's last entry.
- PREREG_L4.md: sealed 8ffb0eb6 (base, D1-D3, before any loop-4 compute);
  the D4/TRACK-H ADDENDUM appended and re-sealed 56e5a59c BEFORE D4
  launched (same turn as the Track-H adjudication 3f67daf8). Current file
  hash = 56e5a59c = the chain's last entry.
In both cases every cell's contract was sealed before that cell's compute;
the base text was never edited (append-only); SEALS.txt records the chain
in order. The auditor's confusion is real though: a current-hash check
against the FIRST seal fails unless the chain is known.

## THE PROTOCOL (adopted program-wide, effective immediately)
1. Prereg base files are FROZEN at first seal — never appended again.
2. Any later addendum goes in its OWN file (PREREG_<loop>_ADD<n>.md),
   sealed before its cells run.
3. SEALS.txt lines gain a role tag going forward: [BASE] / [ADDENDUM-n].
4. Each packet's manifest lists the full chain per prereg so a one-hash
   audit can always be completed offline.
Applied retroactively as documentation (this note); already-sealed chains
stand as recorded. First file under the new protocol: the generation-leg
PREREG_G1.md (9160337c, frozen).
