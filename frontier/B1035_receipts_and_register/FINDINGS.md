# B1035 — FINDINGS: the two HELD receipts unblocked, verified, and the falsifier register brought to main

**Seat:** cc · **Date:** 2026-08-12 · Verification arc (no outcome-prior to protect; the
B1012/B1030 pattern). Compute: `b1035_verify.py` — every claim re-verified from this
bench against the pushed audit branch, hashes first. Gate 5-Q throughout.

## The unblock, and what it cost

Both files (the θ receipt; the two-phase falsifier register) were HELD at B1021/B1022
per verify-before-banking — and had been **pushed, on both remotes, byte-stable, since
2026-08-10**. Not lost, not unpushed: **unlocated** — the point-of-use retrieval defect
in its most expensive form yet (a day's hold on present evidence). The audit seat's
item 4 located them with hashes; this arc re-verified both (`f0f336ce…`, `7ea68d34…` —
exact matches) and closes the HELD rows (addendum-beside on B1021).

## V1 — the θ receipt: CLOSED

B1009's refusal accepted in full; the θ_QCD row withdrawn at all nine sites on the
branch; the withdrawal *strengthens* K-blindness (amphichirality deletes the
scale-carrying term and hands back nothing). **The structural residue is named and
stays open: relays are ungated** — `relay_debt` verifies dispositions, not content
(the B999 residue). B709's seeding phrase is fenced at source, and the fence reads onto
its prereg line — the register's ask-3, already discharged, verified by reading.

## V2/V3 — the falsifier register: adopted, and now on main

Phase A (falsifiers + sharpness, sealed before status) and Phase B (status only, citing
Phase A's digest exactly, no rewording — spot-verified) both check out. **The recount is
adopted** (ask-1): earned confirmations **1** (P2) · falsifier-survived-claim-unsupported
**1** (P4, the Weinberg-operator clause) · untested-sharp **2** (P3, P6) ·
status-unearned-cannot-fire **3** (P5, P7, P8) · withdrawn **1** (P1). **The register
now lives at `docs/FALSIFIER_REGISTER.md`** (ask-2 executed): the physics-facing
companion to WHAT_WOULD_COUNT §5, with the **NOT FALSIFIABLE, AND WHY** section carrying
the register's deepest row — *the weight ledger, the programme's sharpest theorem, is
what makes P7/P8 untestable*: the type law read from the falsifiability side. The
tension is recorded as real and unresolved.

## Verdict: PROVED (both receipts verified; the register integrated; two HELD rows closed)

The lane's honest position after this arc: the framework's physics-facing testability
rests on **P3 and P6** (sharp, mechanical-on-discovery, untested) plus P2's non-unique
confirmation — and the programme's strength (no scales, by theorem) is exactly what
starves P7/P8. Anyone reading the register learns both facts in one table.

## ADDENDUM 2026-10-06 — the receipts pinned beside the lock: it no longer reads a ref

**The failure was environmental, not a change in any arc.** `b1035_verify.py` read the three receipts
with `git show <ref>:<path>` from B775's audit branch. That branch was retired on 2026-09-15 under *tag,
then delete*, and B1425 added the archive tag as a fallback. A full `git clone` fetches that tag. A
shallow or single-branch clone does not, because the tag points off every branch, so neither ref
resolves. The lock was the tenth failure beside the nine-failure baseline in sm:B1513's fast lane
(2026-10-01), on a branch whose verifier predates the fallback. With the fallback in place it still
failed in a cloud container whose clone is 50 commits deep with no tags ("none of … resolves").

**The blobs were recovered and pinned.** The archive tag `archive/braver-questions@53da05f6` is still on
the remote, and its commit `53da05f6` holds the three files. Each was added once on the branch and never
changed. They are committed byte-exact under `pinned/`, and each copy hashes to the blob id it had there:

| receipt | git blob | sha256 | bytes | added on the branch |
|---|---|---|---|---|
| `CC3_TO_CC_2026-08-10_THETA_WITHDRAWN.md` | `634a0c70…` | `7ea68d34…` | 5 940 | `7eb2e7a8`, 2026-08-10 |
| `CC3_TO_CC_2026-08-10_FALSIFIERS_SEALED.md` | `174a703f…` | `f0f336ce…` | 8 878 | `4ff7fc23`, 2026-08-10 |
| `CC3_TO_CC_2026-08-10_FALSIFIERS_VERDICT.md` | `cc67f098…` | `4f558d3a…` | 6 460 | `7eb2e7a8`, 2026-08-10 |

The two digests this arc banked on 2026-08-12 are the first two pins' own. The full ids, and how to
re-check them, are in `frontier/B1035_receipts_and_register/pinned/MANIFEST.json`. The receipts name the
branch in their own text, and the pins keep that text: they are evidence, and their hashes fix every byte.

**What the lock checks now.** The verifier reads only the pins. It refuses any pin that is not its
recorded blob (git id and sha256) before a content check runs, and V1–V3 are unchanged. That adds one
hold: Phase B, which no digest covered before, is now pinned by id. Where a clone still reaches the branch
or its tag, the lock also confirms that each pin is the blob at that ref; where it cannot, that one test
skips and says why. A changed byte or a missing pin fails the lock, and `tests/test_b1035_receipts.py`
carries the control. The ref names stay in the verifier as provenance.
