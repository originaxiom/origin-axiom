# B1468 — THE FROZEN SEALS RE-AUDITED: six of the forty-one carry both halves of the provenance rule in other words, attested with their quotes; thirty-five stay frozen

**Verdict: PROVED** (a process arc; scope: the 42 sealed files of the 41 arcs frozen by B1464; reach general for the
record). cc (main), 2026-10-04. Pays Review 59's R59-2.

## 0. Seen first

- **Repo.** B1464 §1 and `gates.SEAL_PROVENANCE_BASELINE` (the 41, frozen because sealed text is not repaired);
  the rule's two halves (the banked identity reproduced before any new number; the prior-art / record sweep at design
  time) as GOVERNANCE and PRACTICES state them; the 42 files read in full by six readers with a strict brief and the
  quote requirement (`verification/readers_raw.json`), every YES quote re-verified against the file text on main
  (`readers_verified.json`: a quote not found in the file is discarded), and the surviving "both" rows adjudicated by
  main against the brief, not by the readers' word (`adjudication.json`). **Literature:** none.

## 1. The result

| | files | arcs |
|---|---|---|
| read | 42 | 41 |
| banked-identity half present in other words (quote verified) | 18 | — |
| prior-art / record-sweep half present (quote verified) | 15 | — |
| both present and adjudicated as meeting the rule | 7 | **6: B1019, B1033, B1036, B1066, B1071, B1442** |
| both quoted but adjudicated short | — | 2: B1450 (a source cited, not a search), B1435 (an absence statement, not a sweep) |

The six are **attested** in `tests/SEAL_PROVENANCE_ATTESTATIONS.json` — the arc, the two quotes, who attested and when —
and `seal-provenance` reads that file: an attested seal passes only while both quotes are found in its text (a forged
attestation fails, `test_gate_failing_paths.py`). The frozen baseline shrinks from 41 to **35**; `seal_census.py` now
checks that every seal lacking the literal markers is either frozen or attested, with none uncovered.

## 2. What it means

The rule of 2026-08-08 was honoured in substance more often than its markers showed — six more times — and not honoured
at all in the other 35, this seat's September seals among them. Those stay listed. The attestation file is the
instrument that lets a future reader shrink the list further with a quote, and nothing else.

## 3. Errors in this arc

None found; the readers' two unverifiable quotes (B1441's and B1444's "A") were discarded by the check, which is what
it is for.
