# Programme question-map maintenance

This directory is the shared, living source for the Codex seat's hostile closure ledger.  Edit
`inventory/backbone.json`; never hand-edit the generated
`../PROGRAM_QUESTION_ANSWER_MAP.md`.

Wave-9 source locks:

```text
origin/main                  6ea67db72ae51efaf2024cd6903702491e17d105
origin outside-bench ref    2e4f11f673f328c275a795f8da778f7d31b9fe43
origin paper branch         a31456d2d5e4f08723aa9cfabb7a8573cc2c13d4
golden_gate handoff         6fc86147e553773335b665d6d460e1eaa77aaaf0
codex R031A/R031B           734845a7a38ac6dbdbebc24b6465d084a98f72d7
```

Wave-9 canonical state: 201 rows; 75 `PROVED`, 61 `REFUTED`, 15 `CONDITIONAL`,
22 `EXTERNAL_BLOCKER`, 2 `EMPIRICAL`, and 26 `OPEN`.

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
  --as-of 2026-09-01
PYTHONDONTWRITEBYTECODE=1 python3 documents/program-question-map/render.py \
  --source documents/program-question-map/inventory/backbone.json \
  --markdown documents/PROGRAM_QUESTION_ANSWER_MAP.md \
  --as-of 2026-09-01 --check
```

`OPEN` is an honest nonterminal state.  `CONDITIONAL` and `EXTERNAL_BLOCKER` account for an
obligation but do not count as parameter-free physical closure. The latest hostile audit and
twenty-six-item live queue are in `evidence/PROGRESS_BANK_2026-09-01_WAVE9.md`.
