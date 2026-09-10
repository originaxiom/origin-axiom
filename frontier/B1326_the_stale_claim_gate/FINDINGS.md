# B1326 — the stale-claim gate, and the sweep that bounds the class at one

**Verdict: PROVED (instrument).**

## Why the gate did not exist

B1181 was retracted by B1235 on 2026-09-02: *"the family is 38/112 amphichiral, not 83/83 — the
method was orientation-blind."* THE PAPER shipped on 2026-09-09 still saying **"all 83 members … are
amphichiral, with no exceptions and no undecided cases."** Nothing caught it, and the reasons are
structural rather than careless:

- the arc-verdict schema gate checks **shape**, not currency;
- the harvest gate tracks **seat debt**, not claim staleness;
- the paper's provenance appendix tests that a claim **points at a record that exists** — B1181's
  record exists, it is simply retracted;
- and THE PAPER **deliberately names no internal identifiers**, so any gate keyed on arc IDs is
  blind to it *by construction*.

## The sweep: the class has one member

| | |
|---|---|
| RETRACTED arcs | 12 |
| arcs with `superseded_by` | 46 |
| **arcs carrying a populated `retracted.by` block — the B1181 signature** | **1** |

The three other RETRACTED arcs an ID-based scan flags (**B964, B731, B519**) are **false positives**:
each is a *self-correcting* arc whose `claim_one_line` **is** the correction, and the live documents
cite the corrected content. B731 is the clean example — its headline "the figure-eight knot group is
non-congruence" was withdrawn, and `THEOREM_LEDGER` correctly says *"m004 IS congruence"*.

**So the paper is not carrying other stale claims.** That is worth stating positively: the sweep is a
clean bill for everything except the one already fixed.

## The instrument

A retraction may now declare **`retracted.stale_phrases`** — the wordings that must not speak
unqualified again. `tests/test_b1326_retracted_claims_do_not_speak.py` enforces this across ten live
documents, requiring a retraction marker within 400 characters of any occurrence.

**The matcher normalises LaTeX and ligatures, and without that it does not work.** The first version
of this gate **missed the historical defect entirely**, because the paper reads `all $83$ members`, not
`all 83 members`. A gate that cannot see through the markup of the document it guards is vacuous —
the same failure mode that made a naive grep report zero figure-eight mentions in a prior-art PDF that
had two.

## Validation against history

| run | result |
|---|---|
| `main.tex` @ `b94ed03` (the shipped draft) | **fires twice on B1181** |
| the corrected paper | **clean** |
| planted unqualified claim | **fires** (bite control) |
| properly qualified mention | **silent** (no false positive) |

A gate validated only forwards is a gate nobody has tested. This one is validated against the actual
defect it exists to prevent.

Reproduce: `verification/stale_sweep.py` (the census), `tests/test_b1326_retracted_claims_do_not_speak.py`
(the gate, with its bite control).
