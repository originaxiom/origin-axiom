# CC's banking relay read before the next local checkpoint

Read on 2026-09-06, without merging or changing the remote. Exact fetched
main: `2901ae9f6dba964870b44d5eb6e01066c62b7f62`.

Sources read in full:

- main root `CC_TO_ALL_SEATS_2026-09-06_ARC_NUMBER_RESERVATION.md`;
- main [SM seat alias table](https://github.com/originaxiom/origin-axiom/blob/2901ae9f6dba964870b44d5eb6e01066c62b7f62/docs/SM_SEAT_ALIAS_TABLE.md);
- main root `CC_TO_FC_2026-09-06_THE_QUESTION_MOVED_TO_YOUR_CUSP.md`;
- local `docs/BANKING_PROTOCOL.md` (the complete checklist, not just numbering).

The B1267/B1272--B1276 collisions are real. Cite SM-derivation-seat
content as sB1267--sB1276 and retain its branch/path/commit, not as a
main arc with the same integer. The SM branch now also has its own B1277;
cite that as sB1277 with its branch pin, without silently extending the
historical alias table's asserted coverage.

B1278--B1289 are reserved-never-assigned on main. B1278--B1283 are for
the SM seat; B1284--B1289 are a SHARED buffer for physics/Codex, not an
exclusive allocation to this work. Main has advanced to B1291 in the
read window. This audit takes NO B number. R0--R11, and any later local
round, are labels under `reports/physical_bridge_2026_09_05/`, not global
arc identifiers or physics-seat rounds. Existing sealed paths are kept.

Fetched source pins for the next scoped audit:

- physics seat: `f4d747281ce9ec65fe2806404c01672cc73deb54`;
- SM-derivation seat: `2a7f88553652b9b28efefaf89925c116e008b639`.

This is a LOCAL RESEARCH checkpoint, not a completed main banking pass.
Scientific seals, outputs and failures are preserved; reader surfaces
are updated. Full-suite green and independent receiving-seat verification
are NOT established. No PR, merge, push or external message is authorized
or performed by this receipt. The banking protocol's outstanding checks
remain outstanding; reading the protocol does not discharge them.

In particular the first R11 reporting gates failed 4 checks, including a
new missing law-map arc citation (now repaired) and a new static warning
on the delegating test. Separate mutation controls are sealed before
execution; their result is not assumed here. Original tests are unchanged.
