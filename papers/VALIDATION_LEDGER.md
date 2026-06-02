# Validation Ledger

Status: public-safe validation ledger. This file records actionable findings
and the repository decision taken for each. It adds no claims.

Do not record private correspondence, private identity details, raw chats, or
private staging context. Summarize only the technical finding and the repository
action.

## Allowed Status Values

```text
OPEN = logged but not triaged
TRIAGED = decision assigned
PATCHED = accepted finding implemented
CLOSED = no further action
```

## Allowed Decisions

```text
ACCEPT_FIX
ACCEPT_CLARIFY
NEEDS_REPRO
DISPUTE_WITH_REASON
OUT_OF_SCOPE
KILL_OR_RESCOPE
```

## Ledger

| ID | Date | Packet | Competence area | Outcome label | Summary | Actionable findings | Affected files | Decision | Status | Linked commit/PR |
|---|---|---|---|---|---|---|---|---|---|---|
| _pending_ | _YYYY-MM-DD_ | _PC02/PC11_ | _field only_ | _label_ | _one-sentence summary_ | _short list_ | _paths_ | _decision_ | _status_ | _commit/PR_ |
| V1 | 2026-06-01 | PC12 | character varieties / substitution dynamics | STANDARD_REPACKAGE | Internal literature screen: most PC12 blocks are standard methods (Lawton; Baake-Grimm-Roberts; Bellon-Viallet); only the fixed-line splitting (Thm 4) is apparently-new and elementary. | rescale PC12 to a computational note; credit standard methods; present Thm 4 as the lone new bit; quarantine the self-evidencing/FEP framing in paths/E21 | LITERATURE_POSITIONING.md, PAPER_CARD.md, DRAFT_NOTE_SKELETON.md, frontier/B54, paths/E21 | KILL_OR_RESCOPE | PATCHED | branch frontier/pc12-literature-and-hardening (uncommitted) |
| V2 | 2026-06-01 | PC12 | algebraic dynamics | ACCEPT_CLARIFY | B54 verifies [J(m,c),P]=0 for symbolic c (exchange block-diagonalization on the whole fixed line, generalizing B51); the self-evidencing lambda=m condition reduces to the identity 4c^2-2=m^2+2 and predicts no observable. | integrate B54 as standalone math; record self-evidencing as STALLED in paths/E21, not in PC12 | frontier/B54, tests/test_general_c_exchange_structure.py, paths/E21 | ACCEPT_CLARIFY | PATCHED | branch frontier/pc12-literature-and-hardening (uncommitted) |

## Triage Notes

Use one row per coherent technical finding. If one source produces unrelated
findings on PC02 and PC11, split them into separate rows.

Before changing any claim status:

```text
1. reproduce or verify the finding
2. patch docs/tests/proofs on a branch
3. rerun the relevant checks
4. update the affected paper card
5. add the linked commit or PR to this ledger
```
