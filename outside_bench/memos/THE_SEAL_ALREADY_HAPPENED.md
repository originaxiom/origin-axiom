# Memo 215 — THE §4A.2 SEAL HAPPENED THREE WEEKS AGO, AND THIS BENCH TOLD THE OWNER TWICE THAT IT HAD NOT

**Certificate:** `outside_bench/certificates/the_seal_already_happened.py` ·
**Output:** `outside_bench/outputs/the_seal_already_happened.txt`
**No seal.** Every claim is a substring test on a tracked file at HEAD.

---

## 1. The correction, first

`docs/WHAT_WOULD_COUNT.md` §4A.2 reads today:

> **`STATUS: SPEC ONLY, OWNER-PENDING`** … *"what has not happened is the seal."*

**The seal happened on 2026-08-21.**

| | |
|---|---|
| `docs/SEAL_LEDGER.md:527` | `\| 2026-08-21 \| THE EDGE SEAL (L173; …` |
| `frontier/B1106_edge_seal/FINDINGS.md:1` | *"THE EDGE SEAL: **the program's first outward-facing falsifier is sealed**"* |
| same, `:5` | **`D-2` executed** (*"the edge lane seals alone"*), **`D-3` executed** (*"placeholder R6 budget"*) — **the owner's rulings** |
| `docs/EDGE_PREREG_SPEC.md:3` | *"Status at landing: **SEALED**"* |

**BENCH ERROR #28.** Register **R113** told the owner §4A.2 was *"blocked on an owner
decision, not on a computation"*; **R114/R115** repeated it as *"one item waiting on your
signature."* **Both are wrong.** The signature was given and executed three weeks before I
said it was pending. I read the tier document and did not read the seal ledger it points at
— the same failure mode as BENCH ERROR #25, at the one item in the whole roadmap that faces
outward.

## 2. And L173's row contradicts itself, in a single line

All four of these are on **`docs/OPEN_LEADS.md` line 1895**:

| | |
|---|---|
| header | **`SEALED 2026-08-21 (B1106; …`** |
| header | *"the aperiodic unseal **RESOLVED**: two crossings, one apparatus"* |
| body | *"**SPEC ONLY** until the aperiodic design's **owner-pending** unseal resolves…"* |
| value column | *"**GATED on the owner's aperiodic unseal** for the seal step"* |

The header was updated when the seal landed; the body and the value column were not. **A
twelfth stale row, and the worst-placed one** — it is the row a reader consults to learn
whether the programme has a live experiment.

## 3. What the seal actually is

Not a gesture. `docs/EDGE_PREREG_SPEC.md` is built to survive the defusal pattern B724
named:

- **§0 — what standard theory already forces, stated BEFORE the prediction.** Gap labeling
  fixes the IDS in every gap to `(ℤ + ℤα) mod 1`; bulk–boundary makes edge modes traverse
  those gaps as the phason scans. The programme's claim starts *after* that paragraph.
- **§1 — the prediction is the differential, not the counts.** At reversal-closed windows
  (even-index Fibonacci, verified at N = 987 and N = 2584): **exact two-hand
  isospectrality** (agreement **1.3×10⁻¹⁵ over 2584 levels** — the hand is spectrally
  invisible); **complementary localization** of the shared boundary-capable energies
  (eleven at N = 987, splitting **5-right / 6-left**, the ±1 a forced parity remainder);
  and an **odd-index control** where the isospectrality must **break**, at exactly the two
  cut-adjacent letters.
- **§2 — three kill conditions.** K1: the hands' spectra differ beyond budget at an
  even-index window. K2: the localization split is absent, or present where parity forbids,
  or sides-random. K3: the odd-index control fails to break the degeneracy.
- **§3 — the genericity control ran and passed BEFORE the seal** (C-GEN: golden closes,
  strict silver never does).

**Amended once, by its own rule.** `SEAL_LEDGER:529`, 2026-08-27: an **addendum-beside**
(B1171) that explicitly *"is NOT edited"*-s the sealed spec and re-poses R6 as
**`R6′ (the commissioned observable)`** — count boundary-capable modes in a *labelled* gap
on a chain long enough to separate 5 from 6 — because the anchor experiment
(Verbin–Zilberberg–Kraus, arXiv 1403.7124) is *"a demonstration paper, not metrology"*:
13–28 waveguides, ~13 fabricated arrays, no error bars, no counts. *"**The program supplies
the KNOB** (the phason = our intercept) but not the READOUT."*

## 4. What is actually left — and it is not a signature

> **A collaborator who can count modes in a labelled Fibonacci gap, on a chain long enough
> to separate a 5-count from a 6-count, while scanning the phason.** Not an owner decision.
> Not a computation. An experimental run that nobody has commissioned.

## 5. The part that must be said in the same breath

> **INTERPRETIVE.** This bench has already priced what passing would buy, in **memo 197**:
> *"THE SEALED EDGE LAW IS THE MODAL BEHAVIOUR OF A RANDOM PHASE"* — the sealed alternation
> is the **mode** of 3000 random phases at 19.77%, so **one phase in five reproduces the
> sealed law exactly over nine windows**. An experimentalist scanning the phason passes
> through the sealed pattern at roughly one phase in five, so **observing it at ρ = α does
> not identify α**. With memo 196's addenda (at the closure windows `H_L` *is* `H_R` read
> backwards, so the differential is a relabelling; and C4 prices the tiling hull as seeing
> only the hearing), **the lab lane's content reduces to slope-specific, not
> phase-specific.**
>
> So the honest statement of §4A.2 is neither *"waiting on the owner"* (false) nor *"the
> laboratory road"* (overstated). It is: **a real, sealed, kill-conditioned falsifier whose
> differential this bench has shown is weaker than the tier's framing implies, waiting on an
> experimentalist nobody has asked.**

## 6. Filed

**The rule from memo 208 gets its second application and its sharpest one.** When a status
line names a gate, **read the gate's own ledger**, not the document that mentions it. The
seal ledger is one grep away and I did not run it before telling the owner, twice, that
their signature was the blocker.

**Recommendation, not an action** — this bench does not edit main's documents:
`WHAT_WOULD_COUNT.md` §4A.2's `STATUS` line and `OPEN_LEADS.md` L173's body and value
column should be brought into agreement with the header and the seal ledger. Registers
**R113, R114 and R115** are **superseded on this point** by this memo.
