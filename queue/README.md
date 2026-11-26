# The queue

The framework's queue of claim cards (draft 1 of `docs/handoffs/MAIN_TO_ADVISOR_2026-11-26_THE_FRAMEWORK/DRAFT.md`, § 9;
register row P-885). Each card the intake has seen is one file, `queue/cards/Q<nnnn>.json`, written by the intake runner
to the queue's own branch; main holds the schema and the gate that reads it.

- The schema and its command: `scripts/queue/queue_schema.py` (run it with `--ref <the queue's branch>` to read the cards
  there without a checkout).
- The gate: `queue-schema`, on every card in this checkout's `queue/cards/`.

A card's history is append-only. A returned card is refiled as a new card that names the old one.
