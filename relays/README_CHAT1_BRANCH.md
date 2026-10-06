# The chat1 (web seat) branch
`chat1/web-seat` is the web seat's own branch, opened 2026-10-06 at the owner's word, so that its relays are committed on the
sender's branch at send time (WORKING_RULES, sender-branch dual-homing, E51/B1172) instead of reaching main only by the owner's
relay. Until now `docs/HARVEST_LEDGER.md` recorded "the chat1 (session-relay) seat has no branch and no pin"; **adding the pin
row is main's, by a reading arc** — this branch does not touch the ledger.

Conventions this branch keeps: relays named `CHAT1_TO_CC_<date>_<topic>.md` (matched by `relay_debt.py`'s RELAY_RE), their
material in `relays/chat1_<date>_<topic>/`; no arc numbers claimed; nothing written to main, `CLAIMS.md`, `GENESIS.md` or any
ledger; every computed result sealed before it is run, with the hash in its folder.
