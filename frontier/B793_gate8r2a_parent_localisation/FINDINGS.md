# B793 — GATE 8R2-A: sealed, and BLOCKED on an architectural finding about the B788 solver

Sealed prereg: `GATE8R2A_PREREGISTRATION.md`, sha256[0:16] = **d6b6f434206f5c18**.
Origin of the split-gate design: Chat-1 relay 2026-07-28; arithmetic verified independently by cc.
Gate 5 + Gate 5-Q binding. **Nothing here reaches CLAIMS.md.**

## Status: Stage A CANNOT execute against the bank's V₁ solver unmodified

Not a refusal and not a cost objection — an **architectural incompatibility**, found by reading
the code rather than by running it.

## The finding

The B788 bank's V₁ parent control (`build_gate8r_v1_remediation.py` → `search_configuration` in
`build_gate8_v1_control.py`) does this:

```python
optimum = minimize_scalar(
    lambda value: evaluate(float(value))[1]["normalized_smallest_singular_value"],
    bounds=interval, method="bounded", ...)
```

with, from `GATE8R_PROTOCOL.json`:

```json
"source_control": {"search_interval": ["24.50320", "24.50340"]}
```

**That is a bounded scalar minimisation inside a 2×10⁻⁴-wide window centred on the literature
value.** Three consequences, in increasing order of importance:

1. **It is refinement, not detection.** The window is supplied by the answer. The solver locates
   the minimum of σ_min inside a bracket it is told to look in.
2. **`minimize_scalar(method="bounded")` always returns a point.** It has no "no eigenvalue here"
   outcome. A root is produced whether or not one exists.
3. **It cannot count roots in an interval** — and Stage A's entire PASS criterion is *"exactly one
   confirmed root in [0.5, 7.6]"*. Run over that interval, this solver returns exactly one point
   regardless of whether the interval contains zero, one, or five eigenvalues. **The criterion is
   not measurable by this instrument.**

## What Gate 8R's headline actually establishes — restated fairly

The bank is not naive about this. `gate8r_v1_remediation.json` records three genuine negative
controls, all passing:

    displaced_parameter_negative_control_fails    = True   (displacement 0.02)
    outer_band_removal_negative_control_fails     = True
    perturbed_coefficient_negative_control_fails  = True

So the run does establish something real: **there is a sharp σ-minimum near r = 24.5033 and not
at 24.5233.** That is evidence the feature is genuine and localised.

What it does **not** establish, and what the retelling should stop implying:

- Gate 8R's celebrated **"10-digit agreement"** is between two *heights*, each running a bounded
  minimisation over **the same supplied 2×10⁻⁴ window**. That is a **convergence** statement about
  an optimiser, not an independent localisation of an eigenvalue. Chat-1 already flagged that the
  10 digits are internal rather than a literature match; this is the sharper version — the two
  runs share not only the target but the *bracket*.
- The solver has never demonstrated it can find an eigenvalue whose location it was not given.

## Why this matters beyond Stage A

The programme's characterisation of B788 has been *"machinery built and parent-validated; blocker
is wall-clock and checkpointing."* The **parent-validated** half needs qualification: the
validation is bracket-refinement with displacement controls, at **one** r, in a window taken from
a **figure caption**. Whether the machinery can *localise* is untested.

That is exactly the capability Gate 9 requires — Gate 9 must **find** V₅/V₆ eigenvalues at unknown
locations. Its screen does mesh-scan (231 points, `mesh_step` 0.05) before confirming, so the
architecture is there; but the confirmation stage's root-finder inherits the bracket-refine shape,
and **it has never been exercised against a target that was not known in advance.**

## Options for Stage A (not taken unilaterally — the choice changes what the gate means)

- **(a) Convert the copy into a scanner.** Mesh σ_min over [0.5, 7.6], then confirm each dip. This
  is a real modification: the result would no longer be "the bank's V₁ solver passed Stage A", but
  "a scanner built from the bank's assembly passed Stage A". Honest, and weaker as a bank
  validation.
- **(b) Accept cc3's B792 run as Stage A in a different frame.** cc3's solver **does** mesh-scan
  (dr = 0.002) and found exactly one high-parent-weight root at r = 7.072004 in [6.4, 7.35], plus
  relative eigenvalues elsewhere. Methodologically this is **stronger** than the bank's control on
  precisely the axis at issue — it is a detection, not a refinement. It does not validate the
  bank's solver.
- **(c) Leave Stage A blocked** and record the architectural finding as the deliverable, which is
  what this arc does pending a decision.

## Custody protocol — executed and evidenced

Per the sealed prereg, and following the ruling that the bank is a sealed directory rather than a
live process:

| step | result |
|---|---|
| 1. verify bank `ARTIFACT_HASHES.txt` **before** | **84 verified, 0 mismatches** (`bank_hash_baseline_pre.json`) |
| 2. copy solver **out** into `bank_solver_copy/` | done; nothing written into the bank |
| 3. run/inspect here | inspection only — see the finding above |
| 4. re-verify hashes **after** | **84 verified, 0 mismatches — BANK UNMODIFIED** (`bank_hash_baseline_post.json`) |

Step 4 converts "I did not fork it" from an assertion into evidence. Ownership per the numbering
ruling: **the solver is B788's, the run is B793, this receipt cites both.**

### Separate observation on the delivered archive

The 10 unresolved hash entries are the bank's **own lock tests**
(`../../tests/test_b788_maass_*.py`). They are **absent from the delivered zip**. The bank's
*data* is verifiable; its *locks* are not. Not a defect in the bank — a gap in what was shipped —
but it means no seat can currently re-run the bank's own tests.

— cc, 2026-07-28
