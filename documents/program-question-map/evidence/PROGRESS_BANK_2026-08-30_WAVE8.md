# Progress bank — 2026-08-30 — Wave 8

## Source pins

- `fresh/main = 4cc38d8a60aa93c85bca7157df008766e3f2861b`
- `fresh/claude/outside-bench = 941b60e0baeda1bce91f3535b3a298c98f7121e0`
- prior Codex bank = `53d1f527698af01325b640d798bf144cf0f53a85`

## Verified upstream delta

### B1218

A clean `git archive` of fresh main was used, not the working branch.

```text
bash frontier/B1218_open_claim_sweep/verification/reproduce.sh
positive 5/5, negative PASS
REPRODUCES
```

The standalone sweep exits zero.  The local machine's system Python lacks
pytest, so the pytest wrapper was not used as evidence; the arc's own
reproduction path and instrument were executed directly.

### B323/B324

Both source certificates independently exit zero in the Sage environment.
The Codex stdlib certificate then re-derives the discriminating carrier fact
without importing either source: the three order-three labels have exact
intertwiners on one carrier and one character-variety point.

### B632 currency

Current main contradicts outside memo 157's “queued and unrun” sentence.  The
same B632 `FINDINGS.md` contains the completed cell-2 section after the older
cell-1 forward pointer.  `REPAIR_ADJUDICATION.md`, failed transcripts and the
exhaustive verifier are present.  Exact cell 1 was rerun and reproduced
`27=V(16)+V(8)+V(0)` and `(h0,h1,h2)=(1,3,2)`.  The exhaustive cell-2 rerun
reproduced its canonical-chain, 162 coboundary-descent, alternation and
rank-two gates.

## New exact hostile certificate

```text
PYTHONDONTWRITEBYTECODE=1 python3 certificates/r029_upstream_hostile_corrections.py
PYTHONDONTWRITEBYTECODE=1 python3 -O certificates/r029_upstream_hostile_corrections.py
```

Both return:

```text
GATE_C character_orbit_size=1 PASS
GATE_D exact_full_trace_identity=lambda^2+2 PASS
GATE_D allowed_lambda_on_chosen_branch={+w,-w} SIGN_NOT_SELECTED
GATE_D finite_approximant_degrees {6: 21, 8: 55, 10: 144}
GATE_D exact_in_window_interior_witnesses=(6,8,10) PASS
GATE_D finite_sigma_has_nonempty_interior_by_FTA_and_continuity
GATE_D finite_sigma_planar_box_dimension=2
VERDICT GATE_C_ROUTE_REFUTED; GATE_D_EXACT_CORE_NARROWED; LIMIT_OPEN
```

The certificate records the externally checked upstream script blob, reported
three levels and `[-6,6]^2` sample window, then reconstructs the recurrence
independently.  It gives an exact strict-interior
witness in that window for every level.  Independently, a nonconstant complex
polynomial has a zero and its strict disk preimage is open.  A bounded subset
of the plane with nonempty interior has Minkowski/box dimension two.  The
finite mask in outside memo 156 therefore cannot have exact dimension `0.794`;
the grid failed to resolve its thin open components.  Nothing here settles the
limiting intersection.

## Canonical map changes

- OA-C0008 and OA-C0009: current generation result reconciled.
- OA-C1170: commensurator order three does not create three copies — REFUTED.
- OA-C1171: B632 integer three is not three generations — REFUTED.
- OA-C1172: L57 boundary-theta / beat-spin comparison — OPEN.
- OA-C1173: L175 word-property/mechanism — PROVED.
- OA-C1174: limiting complex Fibonacci spectral theorem — OPEN.
- OA-C1175: current discrete ledger exactly `{C,P}` — PROVED, scoped.

Final counts:

```text
192 total
72 PROVED
58 REFUTED
15 CONDITIONAL
22 EXTERNAL_BLOCKER
2 EMPIRICAL
23 OPEN
```

## Mechanical gates

```text
python3 -m json.tool documents/program-question-map/inventory/backbone.json
PYTHONDONTWRITEBYTECODE=1 python3 documents/program-question-map/validate.py
PYTHONDONTWRITEBYTECODE=1 python3 documents/program-question-map/render.py \
  --source documents/program-question-map/inventory/backbone.json \
  --markdown documents/PROGRAM_QUESTION_ANSWER_MAP.md \
  --as-of 2026-08-30 --check
```

All pass.  The deterministic Markdown is current.
