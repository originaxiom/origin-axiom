# THE TWO ANATOMIES RECONCILED — the corpus's zero-overlap "finding" is not a defect: the two schemes are ORTHOGONAL AXES of one grid, and here is the grid
## (outside bench memo 126, 2026-08-28; certificate `certificates/anatomy_reconcile.py`, GREEN; the owner's "go both", part 1)

The corpus's own CHANGELOG records a finding it never resolved:
*"the programme carries TWO DISJOINT ANATOMIES of one object —
kill_graph's faces versus the atlas's motifs. Overlap: ZERO, not one
face is a motif."* The finding is correct as a **name** fact and was
left as an open blemish. It is decidable from the banked data whether
that blemish is a defect, and this cell decides it.

**The fork, fixed before the run.** Two classifications of the same
arcs can share no vocabulary and still be either
(a) **REDUNDANT** — each face essentially determined by a motif, the
same cut made twice under two names — or (b) **ORTHOGONAL** —
independent axes, in which case the disjointness is a feature and the
schemes should be *used together*, not merged. Criterion fixed in
advance: **≥80% of a face's arcs on a single motif (or vice versa) ⟹
REDUNDANT; otherwise ORTHOGONAL.**

- **R1 — both anatomies from primary** (`origin/main`, read by the
  certificate itself, no scratch files): kill_graph 769 closure
  records, **15 canonical face labels**; atlas 1095 probes, **19
  lexicon motifs**. **NAME-OVERLAP: 0** — the CHANGELOG is right.
- **R2 — the join: 653 arcs carry BOTH a face and a motif.** Enough to
  decide the question.
- **R3 — THE CONTINGENCY TABLE, computed for the first time:**
  **13 faces × 19 motifs, 205 nonzero cells of 247 = 83.0% filled.**
  Not a block-diagonal correspondence; a nearly complete grid.
- **R4 — THE VERDICT: ORTHOGONAL AXES.** *Zero* faces and *zero*
  motifs meet the concentration threshold. Every substantial face
  touches 18–19 of the 19 motifs with a top-motif share of only
  **12–15%** (being 1858 arcs / 19 motifs / 13.2%; hearing 1617 / 19 /
  13.6%; mtc-overlay 675 / 19 / 13.9%; sln-tower 545 / 18 / 13.8%);
  motif top-face shares run **26–46%** (quasicrystal 45.7% is the
  most concentrated and still nowhere near the line).

**THE RECONCILIATION.** kill_graph asks *which part of the object an
arc touched* (a face); the atlas asks *which pattern recurred in it*
(a motif). Those are orthogonal coordinates, so **zero name-overlap
is exactly what a well-formed pair of axes looks like** — it is not a
defect to repair. The honest fix is not a merge but a **stated
pairing**: an arc's full address is **(face, motif)**, and the table
in `outputs/anatomy_reconcile_out.txt` is that grid.

**DATA-QUALITY FINDING, filed at point of occurrence.** **8 of the 23
distinct `faces_consulted` values are free-text prose** — whole
sentences with bank citations pasted into a categorical field (e.g.
*"B1134 (the relay naming the 64 as the value target); B1138 …"*).
They are excluded from the analysis above; **the field needs a schema
check** upstream. Two of the 15 remaining labels (`cascade`,
`character-variety`) carry no joined arcs, which is why the table is
13 faces wide and not 15.

**Fence.** This is repository metadata, not an object claim: the join
covers only arcs present in both artifacts, and arcs missing a face or
a motif are outside it. Gate 5 untouched.

### ⚠ ADDENDUM 1 (2026-08-29) — NUMBERS CORRECTED under the pinned source (codex's floating-ref catch); the VERDICT is unchanged
codex's evidence-contract audit charged that *"multiple outside scripts
depend on **floating Git refs**"*. **Correct, and this memo is the proof.**
Its certificate read `origin/main` — a **moving** ref — so the banked
output no longer matches a re-run. Re-run against the now-**pinned commit**
(main @ B1212, `3c58527b`):

| | banked | at the pin |
|---|---|---|
| kill_graph closure records | 769 | **772** |
| canonical face labels | 15 | **16** (new: `value`) |
| arcs carrying both | 653 | **654** |
| contingency table | 13 × 19 | **14 × 19** |
| nonzero cells | 205 of 247 = 83.0% | **211 of 266 = 79.3%** |

**THE VERDICT IS UNCHANGED AND SURVIVES CLEANLY: ORTHOGONAL AXES** —
**0/14** faces and **0/19** motifs concentrated at the ≥80% criterion.
The data-quality finding on `faces_consulted` also stands.

**All figures in this memo should now be read from the pinned re-run.**
The certificate is fixed at the source (`certificates/_oa_source.py`), so
this class of drift cannot recur in this lane. This addendum is the only
mutation.
