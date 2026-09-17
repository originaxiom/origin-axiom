# B1423 — THE DOOR MADE A LINK, AND THE TWO GATES THAT COULD NOT SEE: the sweep now reads executables (where the retracted claim was hiding), the harvest gate counts its debt from the ledger rather than from live remotes, and the McKay door enters the chain as C57 after fifteen months as prose

cc, 2026-09-17. **Owner-directed:** *"how do we fix it"*, after S15 found two green tests asserting a retracted
claim, a closed-chapter gate held against the paper, and two structural gaps named but unrepaired.
**Verdict: PROVED (the door, with both controls) + the two gate repairs.**

## 1. THE SWEEP NOW READS EXECUTABLES — the hole the worst failure hid in
`scripts/checks/retraction_sweep.py` swept tracked `.md` and `.tex`. It had been widened once before, from `.md`
only, after a retracted phrase survived a week in the paper. **The second hole was worse than prose**: E82's
retraction survived in two *tests* that PASSED while asserting it, and which the paper's verification package lists
as locks for the claim row that states the correction.

- **Widened** to every tracked `.py`: 7 224 files, where assertions and the comments that justify them live.
- **Made fast enough to keep**: a whole-file flatten-and-reject pass before any line work. The naive widening took
  minutes; it now runs in about ten seconds, and a gate slow enough to skip is a gate that gets skipped.
- **Taught to recognise a refutation**: an executable that refutes a phrase must quote it (*"a draft claimed…"*,
  *"this arc's draft headline"*, *"previously read"*). Those cues are now mentions, and the locks whose purpose is
  to keep a phrase refuted are exempt by name — a lock that may not name what it refutes cannot refute it.
- **It immediately found one more**: `tests/test_b1253_generation_count.py` opened with the docstring *"B1253 — the
  generation count is forced at three"*, which is the arc's **draft headline**, refuted by a test **in the same
  file** (all fifteen 16-blocks lie in one Weyl orbit, so the three 16s of any triple are conjugates sharing one
  character). The refuted claim was the title of the file that refutes it. Corrected.
- **Now: 24 registered phrases, 7 224 files, 0 live violations.**

## 2. THE HARVEST GATE COUNTS FROM THE LEDGER, NOT FROM LIVE REMOTES (L224 closed)
`harvest_debt.py` computed its SCHEDULED count per seat, and a seat whose remote is unconfigured or whose ref is
unfetched is SKIPPED — so when codex, cc3, cloud, braver and qor5up were retired or merged on 2026-09-15, their
debt became invisible. The gate reported a handful of rows against a ledger carrying **282**.

- A **ledger-side, remote-independent** count is now computed and printed beside the per-seat one:
  *"SCHEDULED rows 81 (ledger-wide, remote-independent: 282)"*, with a by-seat split.
- A **growth ratchet** (`SCHEDULED_BASELINE = 282`) fails the gate if the backlog grows. Failing on the whole
  backlog would block every landing, which is a stop and not a gate; failing on growth is the instrument that fits.
- **Retiring a seat can no longer retire its debt.**

## 3. THE DOOR IS NOW A LINK — C57 (`verification/mckay_door.py`, `.out.txt`)
The step from the object's arithmetic to the exceptional algebra — the step everything downstream walks through —
was prose in the paper and had **no chain link at all**; the chain ran from the invariant trace field at link 6 to a
presumed $\mathfrak{e}_6$ at link 24. Verified here end to end, in one script, each part able to fail:

| step | computed | result |
|---|---|---|
| the ramified prime | `disc ℚ(√−3) = −3`; `(3) = (√−3)²`, one prime above 3 | residue field order **3** |
| the finite group | `SL(2, O_K/(√−3)) = SL(2,𝔽₃) = 2T` | order 24 |
| the surjection | `GQuotients(π₁(m004), SL(2,3))` | **2** classes up to automorphism |
| the correspondence | McKay graph of 2T at its faithful 2-dim representation | **7 nodes, 6 edges, marks 1,1,1,2,2,2,3 = affine E₆** |
| **control A** | the same construction on Q₈ | **affine D₄** (5 nodes) — the criterion can return something else |
| **control B** | `GQuotients(π₁(m004), SL(2,5))` | **0** — the door does not open onto E₈ |

Minted as **C57 [THEOREM]**, with its scope travelling with it: the surjection is *generic* (about one one-cusped
census manifold in three), so the link carries the arithmetic to the algebra and carries **no** claim that the
object is distinguished by doing so. The chain is now **57 links, 53 forced, 36 theorems**; the paper's prose,
figure axis and provenance row are updated, and the paper says plainly that this step had been narrated without
being listed.

## What this does not fix
The era's four exact reproductions of published invariants (an A-polynomial matching Cooper–Long literally, two
SL(3) matches, a Ptolemy cross-check) and the two *geometric* selections of the object (systole, minimal volume)
are still absent from the paper, whose opening anxiety is precisely that its verification is internal. They are
verified work that would answer that anxiety directly, and they are the next thing to carry.

## Locks
`tests/test_b1423_the_door.py` (the four steps, both controls, and that the chain and the paper carry the link).
The two gate repairs are exercised by the gates themselves at every landing.
