# Memo 212 — THREE CELLS IN SEVENTY-FIVE, AND THE STALENESS RUNS BOTH WAYS

**Certificate:** `outside_bench/certificates/the_artifact_pair_sweep.py` ·
**Output:** `outside_bench/outputs/the_artifact_pair_sweep.txt`
**No seal.** A census: every number is a count over tracked files at HEAD, every named
cell quoted from its own files.

---

## 0. The question memo 211 raised

Memo 211 found one cell — `P2W5-L72` — whose committed `results.json` disagreed with its
committed `output.txt` **and** with the code that produced both. How many more?

## 1. The census

| | |
|---|---|
| `results.json` files under `frontier/` | **228** |
| … with an `output.txt` beside them | **114** |
| … with a `compute.py` beside them too | **113** |
| … carrying a verdict on **both** sides | **75** |
| … carrying one on only one side | 29 — a formatting gap, not a contradiction |
| **cells where `output.txt`'s verdict appears NOWHERE in `results.json`** | **3 — 4.0%** |

**Three, not thirty.** The defect memo 211 found is real and is **not** endemic.

## 2. The three, and which artifact is the stale one

| cell | `output.txt` | `results.json` | stale side |
|---|---|---|---|
| `B775_phase2_wave1/cells/P2W5-L72` | `RESOLVED-A` | `UNRESOLVED` | **the JSON** |
| `B771_phase1_wave1/cells/W2-270` | `UNRESOLVED` | `RESOLVED-B` | **the output.txt** |
| `B771_phase1_wave1/cells/W4-017r` | `RESOLVED-A` | `PENDING_PART_B` | **the JSON** |

### (1) P2W5-L72 — settled by re-running the cell's own code

Memo 211: `output.txt` reproduces byte-for-byte, `results.json` differs in 51 fields, and
the JSON records **`h1 = {0, 0, 0, 0, 0, 0}`** for the six E₆ exponents — a failed relator
check from an older code version, preserved as a result.

### (2) W2-270 — settled by reading, and **the direction is reversed**

`output.txt:63` — **`VERDICT: UNRESOLVED (=> EXTERNAL).`** — and `:65` gives as its
obstruction (a) that *"depth 9-11 recomputation did not complete in the available turn
budget."*

`results.json` — verdict **`RESOLVED-B`**, and it **contains `r_seq_depths_7_11` with five
entries plus an Aitken extrapolation.**

> **The JSON holds exactly the data the `output.txt` says did not finish.** Here the
> **text** is the stale artifact, not the JSON.

Both files were **committed in the same commit**, `2026-08-25 17:39:12 +0200`, already
inconsistent with each other.

### (3) W4-017r — the JSON was written mid-run

`output.txt:127` — **`VERDICT: RESOLVED-A`** — after `total runtime 598.6s`.
`results.json` — verdict **`PENDING_PART_B`**, and its **only** result key is `part_A`.

> The file is a snapshot taken between part A and part B and never rewritten. Its verdict
> string says so in words.

**Confirmed by re-running it.** The cell's unmodified `compute.py` was copied to an
isolated tree with its one dependency (`B461_relation_r2_borromean/ptolemy_systems.json`)
and run: **469.9 s**, `VERDICT: RESOLVED-A`, and a `results.json` carrying
`['cell', 'verdict', 'reason', 'part_A', 'part_B', 'runtime_s']`. The committed file has
**two of those six keys** and the wrong verdict.

> **Two of the three are now settled by running the cell's own code, not by reading it.**

## 3. What the shape of it means

> **INTERPRETIVE.** Two facts sit together and neither is comfortable on its own.
>
> **The defect is rare — 3 in 75, 4%.** The corpus's cells do keep their two artifacts in
> agreement, and any reading of memos 207–211 as "the record is broadly untrustworthy"
> would be wrong and is refused here.
>
> **But the staleness runs in both directions**, and that is the part that matters. It is
> not "JSONs rot" — a rule like *always trust the JSON* or *always trust the text* would
> be wrong one time in three. There is no privileged artifact. **A cell's two outputs are
> only as trustworthy as the run that wrote them both, and nothing in the tree records
> whether that happened.**

All three are **bookkeeping**. **No mathematics is wrong in any of them** — P2W5-L72's
splitting was independently reproduced in memo 211; W2-270's own structural obstruction
(its noise floor) is untouched by which verdict string is right; W4-017r's part A and part
B both ran and are both in its text.

## 4. What a fix would be, and it is not this bench's to apply

The cheapest durable fix is a gate, not a cleanup: **a cell's `results.json` and
`output.txt` must be written in the same process exit path**, and a repo check can assert
that every cell carrying a verdict in both places carries the *same* one. That check is
this certificate, and it runs in under a second.

Three files to regenerate on main, each from its own committed `compute.py`:
`P2W5-L72/results.json`, `W2-270/output.txt`, `W4-017r/results.json`.

## 5. The fence

**The census tests one thing: whether a verdict string in `output.txt` also appears
somewhere in `results.json`.** It does not check whether the *numbers* in the two agree, it
does not re-run the 113 cells that have a `compute.py`, and it says nothing about the 29
cells that carry a verdict on only one side or the 114 `results.json` files with no
`output.txt` at all. **A cell passing this check is not thereby verified** — only
not-caught by this one test.
