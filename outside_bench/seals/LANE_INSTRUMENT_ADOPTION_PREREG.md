# SEAL — THE CORPUS'S OWN INSTRUMENTS, TURNED ON THIS LANE

**Sealed 2026-08-30, pushed BEFORE any run.** Pin `89affd5b`.

Memo 153 found that the corpus had already built the instrument this bench needed
(`already_banked.py`, `B1202`) and that this bench had never run it. **That was one instrument.
There are thirteen.** `scripts/checks/` carries a full suite, and this lane — 40+ standing
documents, 150+ certificates, three years of the owner's questions — has adopted **one** of them,
and only yesterday.

This cell runs the applicable ones on this lane and reports what they find, including nothing.

## The cells

### F1 — path references · **BLIND**
`check_path_references.py`: every backticked repo-path in a tracked `.md` must resolve. This lane's
memos cite paths constantly (`certificates/…`, `seals/…`, `outputs/…`).
- **F1-CLEAN** — every backticked path in `outside_bench/**.md` resolves.
- **F1-BROKEN** — one or more do not; each is named.

### F2 — document currency · **CONFIRMATORY** (two stale documents already known)
`doc_currency.py`: a living document whose newest cited arc lags the corpus. Memo 153 found two by
hand; this is the mechanical version over the whole lane.
- **F2-CONTAINED** — no lane document lags beyond the two already corrected.
- **F2-WIDER** — others do.

### F3 — retraction sweep · **BLIND, and the sharpest cell here**
`retraction_sweep.py`: a claim the corpus has **retracted** still quoted as live. This lane quotes
arcs constantly and has never checked whether any quoted arc was later retracted. **Quoting a
retracted claim as live is a real defect, not a hygiene nit** — it is how a wrong result
re-enters a record that had already removed it.
- **F3-CLEAN** — no retracted claim appears live in this lane.
- **F3-DIRTY** — at least one does; each is named with the retracting arc.

### F4 — how much of the suite can even be pointed here? · **BLIND**
Several instruments are hard-wired to the main corpus's shapes (`frontier/*/results.json`, pytest
locks) which this lane does not use. Report, honestly, how many of the thirteen are runnable
against this lane and **why each unrunnable one is unrunnable** — because "we could not run it" and
"it does not apply" are different, and only the second is acceptable.
- **F4-COVERED** — every instrument either runs or has a stated structural reason it cannot.
- **F4-GAPS** — some are simply unadopted with no reason.

## Binding

- **A clean result is a result** and will be reported as such. This cell is not obliged to find
  anything, and manufacturing a finding to justify the cell is the failure it exists to avoid.
- **No mechanical hit is a verdict until read.** Seven detectors of mine have needed checking
  against themselves this session.
- Corrections by **dated addenda** only.

## Gate 5

No measured value enters. Text and file paths only.
