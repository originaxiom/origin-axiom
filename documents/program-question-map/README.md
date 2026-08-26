# Programme question-map maintenance

This directory is the shared, living source for the Codex seat's hostile closure ledger.  Edit
`inventory/backbone.json`; never hand-edit the generated
`../PROGRAM_QUESTION_ANSWER_MAP.md`.

Wave-4 source locks:

```text
origin/main                  68383e80718e732e7cf5b9e57077a19dff753ad6
origin outside-bench ref    59680460721a0b9e4f672ad6e997724c226ceb56
origin paper branch         61a243c65f1a84c700e3c3d9755b11c30a5f0699
golden_gate handoff         15b3366937af19e643a54d564883253f013fc651
```

Wave-4 canonical state: 120 rows; 45 `PROVED`, 40 `REFUTED`, 13 `CONDITIONAL`, 16
`EXTERNAL_BLOCKER`, 2 `EMPIRICAL`, and 4 `OPEN`.

## Update loop

1. Fetch source branches read-only and record immutable commit IDs.
2. Deduplicate by the typed proposition, not by memo title.
3. Add every newly exposed child question before claiming exhaustion.
4. Preserve scope and hidden inputs in the row itself.
5. Put a self-contained certificate on this branch before citing it as a new result.
6. Run:

```text
PYTHONDONTWRITEBYTECODE=1 python3 documents/program-question-map/validate.py
PYTHONDONTWRITEBYTECODE=1 python3 documents/program-question-map/render.py \
  --source documents/program-question-map/inventory/backbone.json \
  --markdown documents/PROGRAM_QUESTION_ANSWER_MAP.md \
  --as-of 2026-08-26
PYTHONDONTWRITEBYTECODE=1 python3 documents/program-question-map/render.py \
  --source documents/program-question-map/inventory/backbone.json \
  --markdown documents/PROGRAM_QUESTION_ANSWER_MAP.md \
  --as-of 2026-08-26 --check
```

`OPEN` is an honest nonterminal state.  `CONDITIONAL` and `EXTERNAL_BLOCKER` account for an
obligation but do not count as parameter-free physical closure.  The latest hostile audit and
four-item live queue are in `evidence/PROGRESS_BANK_2026-08-26_WAVE4.md`.
