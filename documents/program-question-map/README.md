# Programme question-map maintenance

This directory is the shared, living source for the Codex seat's hostile closure ledger.  Edit
`inventory/backbone.json`; never hand-edit the generated
`../PROGRAM_QUESTION_ANSWER_MAP.md`.

Wave-6 source locks:

```text
origin/main                  4526eb49214cdc3c038191870421f32d6819b79d
origin outside-bench ref    287e8f75efa34141dfb00ff2c30215cd50036ee5
origin paper branch         a31456d2d5e4f08723aa9cfabb7a8573cc2c13d4
golden_gate handoff         6fc86147e553773335b665d6d460e1eaa77aaaf0
```

Wave-6 canonical state: 185 rows; 70 `PROVED`, 55 `REFUTED`, 15 `CONDITIONAL`,
22 `EXTERNAL_BLOCKER`, 2 `EMPIRICAL`, and 21 `OPEN`.

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
  --as-of 2026-08-29
PYTHONDONTWRITEBYTECODE=1 python3 documents/program-question-map/render.py \
  --source documents/program-question-map/inventory/backbone.json \
  --markdown documents/PROGRAM_QUESTION_ANSWER_MAP.md \
  --as-of 2026-08-29 --check
```

`OPEN` is an honest nonterminal state.  `CONDITIONAL` and `EXTERNAL_BLOCKER` account for an
obligation but do not count as parameter-free physical closure. The latest hostile audit and
twenty-one-item live queue are in `evidence/PROGRESS_BANK_2026-08-28_WAVE6.md`.
