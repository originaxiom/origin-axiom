# Programme question-map maintenance

This directory is the shared, living source for the Codex seat's hostile closure ledger.  Edit
`inventory/backbone.json`; never hand-edit the generated
`../PROGRAM_QUESTION_ANSWER_MAP.md`.

Wave-5 source locks:

```text
origin/main                  bf580f45840d121a811d2b6606c48beac92c3057
origin outside-bench ref    60bcf01db966ae0b13f18c73c24845040b59fd98
origin paper branch         a6c35d083e9bd7610045093d682afce827034932
golden_gate handoff         6fc86147e553773335b665d6d460e1eaa77aaaf0
```

Wave-5 canonical state after the overnight reconciliation: 154 rows; 60 `PROVED`, 47 `REFUTED`,
14 `CONDITIONAL`, 20 `EXTERNAL_BLOCKER`, 2 `EMPIRICAL`, and 11 `OPEN`.

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
  --as-of 2026-08-27
PYTHONDONTWRITEBYTECODE=1 python3 documents/program-question-map/render.py \
  --source documents/program-question-map/inventory/backbone.json \
  --markdown documents/PROGRAM_QUESTION_ANSWER_MAP.md \
  --as-of 2026-08-27 --check
```

`OPEN` is an honest nonterminal state.  `CONDITIONAL` and `EXTERNAL_BLOCKER` account for an
obligation but do not count as parameter-free physical closure.  The latest hostile audit and
eleven-item live queue are in `evidence/PROGRESS_BANK_2026-08-26_WAVE5.md`.
