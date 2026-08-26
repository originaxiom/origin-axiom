# Programme question-map maintenance

This directory is the shared, living source for the Codex seat's hostile closure ledger.  Edit
`inventory/backbone.json`; never hand-edit the generated
`../PROGRAM_QUESTION_ANSWER_MAP.md`.

Current source locks:

```text
origin/main                  9d6979db424c0b878c62541a3f21e0a2ca39f274
origin outside-bench ref    0fcdb66cd57edeb13c8703b7f05717fcc2609893
golden_gate handoff         15b3366937af19e643a54d564883253f013fc651
```

Current canonical state: 108 rows; 37 `PROVED`, 36 `REFUTED`, 13 `CONDITIONAL`, 16
`EXTERNAL_BLOCKER`, 1 `EMPIRICAL`, and 5 `OPEN`.

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
five-item live queue are in `evidence/PROGRESS_BANK_2026-08-26_WAVE3.md`.
