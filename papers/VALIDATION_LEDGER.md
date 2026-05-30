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
