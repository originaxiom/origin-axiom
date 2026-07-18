# B679 — THE engine_v7 gate_report PATCH: PREPARED + CORRECTNESS-VERIFIED
# (main seat, 2026-07-18; the PRICED_DOORS item from B678)

## Status: PREPARED, VERIFIED, NOT-YET-DEPLOYED

The engine is NOT a repo-tracked file — it is a SEAT CONDUIT
(veins/v7_conduit/engine_v7.py on the cc2/cc3 seats, byte-identical
copies; frontier cells reference it by that path or inline copies).
So this arc banks the VERIFIED patch as a repo deliverable; the actual
application is a seat-conduit deployment the conduit owners perform —
not a commit in this repo. Nothing in any seat was touched.

## What it fixes

gate_report placed each gate's full O(N³) matrix expression INSIDE a
max(...) generator body, re-evaluated per (i,j) — O(N⁵) per gate. The
patch hoists each expression VERBATIM to a local computed once, scanned
O(N²). One hunk, entirely inside gate_report; the rest of the file is
byte-identical (ast-excision verified).

## Correctness (main-seat verify-on-receipt, independent of the agent)

Recomputed here: OLD vs PATCHED gate_report on IDENTICAL (S,T) for
SU(3)_{1,2,4} (N = 3, 6, 15) and SU(2)_3 — all six gate values
(unitary, symmetric, (ST)³=S², S⁴=I, two_word, rho_unitary) and the
full ρ matrix BIT-IDENTICAL (raw mantissa). Matches the agent's
battery (bit-for-bit through N=28; every distinct call pattern; the
label= printed path character-exact; all 18-lock rerun green; N=55
old-vs-patched agreement through the real d4_ceiling call site
reproducing the banked B673 log character-for-character). NO tolerance
accepted anywhere. The agent's deliberate divergences from cc2's local
fast_gate_report (which was NOT bit-compatible: S†-for-S⁻¹ and
ST·ST·ST-for-(ST)³) were REJECTED to keep two_word/(ST)³ bit-identical
— exactly the right call.

## Speedup (agent battery; the door's price, measured)

N=6: 9.4x; N=15: 67x; N=28: 221x (one old gate_report call at N=28 =
7.4 min — the O(N⁵) tax behind the multi-hour high-level ladder runs).
The N=45 timing cell was still running at bank time (timing-only, not a
correctness gate) — a minor addendum if it lands; correctness does not
depend on it.

## Deployment (for the conduit owners)

Drop engine_v7_patched.py over veins/v7_conduit/engine_v7.py on each
seat (or apply patch.diff). Re-run any live high-level cell to confirm.
Correctness is certified here; the deployment is theirs to execute.
Artifacts: PATCH_REPORT.md, patch.diff, engine_v7_patched.py,
engine_v7_current.py (snapshot), equivalence_proof.py + outputs.
