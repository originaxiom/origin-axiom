r"""THE RELAY-DEBT GATE — nothing preserves findings, so this does.

THE FAILURE THIS EXISTS TO STOP
-------------------------------
Branch protection preserves FILES. Nothing preserved FINDINGS.

`CC3_TO_CC_2026-07-28_rank4_response.md` answered the iota-status question in
July: B766's rank 3 counts CLOSING AXES and stands, B787's rank 4 counts
REP-VARIETY symmetries, both correct about different objects. It never reached
main. L114 was then promoted and assigned to cc3 asking a question that relay
had already answered, and it cost a full campaign to rediscover.

The mechanism was not neglect. A relay's content lives on main only if somebody
banks it, and NOTHING CHECKED whether that happened. The loss audit found this
class once already; cc actioned it (B909, B920, B921, branch protection); it
recurred anyway, because every one of those fixes preserved files.

THE RULE
--------
Every seat-to-seat relay must carry a DISPOSITION:

    BANKED   — its finding is on main; the row names the arc or ledger row
    DECLINED — considered and rejected; the row says why
    OPEN     — a DEBT, with an age

A relay with no row at all is the failure state: invisible work.
A debt is not an exemption -- B982's lesson, applied here. Debts are listed
with their age and escalated by name past the threshold.

USAGE
-----
    python3 scripts/checks/relay_debt.py            # report
    python3 scripts/checks/relay_debt.py --check    # nonzero if the gate fails
    python3 scripts/checks/relay_debt.py --seed     # write missing rows as OPEN

The ledger is `docs/RELAY_LEDGER.md`, hand-maintained (the disposition is a
judgement, not a computation). This script only checks that it is COMPLETE and
that no debt has gone stale.

Gate 5-Q. Bookkeeping instrument; asserts no mathematics.
"""
import argparse
import datetime
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEDGER = os.path.join(ROOT, 'docs', 'RELAY_LEDGER.md')
RELAY_RE = re.compile(r'^(CC3_TO_CC|CC_TO_CC3)_(\d{4}-\d{2}-\d{2})_(.+)\.md$')

# a debt older than this is escalated BY NAME in the report
STALE_DAYS = 14

VALID = ('BANKED', 'DECLINED', 'OPEN')


def find_relays():
    """Every seat-to-seat relay in the repo root, oldest first."""
    out = []
    for fn in sorted(os.listdir(ROOT)):
        m = RELAY_RE.match(fn)
        if m:
            out.append((fn, m.group(2), m.group(1)))
    return sorted(out, key=lambda r: (r[1], r[0]))


def parse_ledger():
    """{filename: (disposition, note)} from the ledger's table rows."""
    if not os.path.isfile(LEDGER):
        return {}
    rows = {}
    for line in open(LEDGER, encoding='utf-8'):
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 3:
            continue
        name = cells[0].strip('`')
        disp = cells[1].replace('*', '').strip().upper()
        if disp in VALID:
            rows[name] = (disp, cells[2])
    return rows


def _age_days(datestr, today):
    try:
        d = datetime.date.fromisoformat(datestr)
    except ValueError:
        return None
    return (today - d).days


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='exit nonzero if any relay lacks a row')
    ap.add_argument('--seed', action='store_true',
                    help='append missing relays to the ledger as OPEN')
    ap.add_argument('--today', default=None,
                    help='ISO date to age debts against (default: file mtimes '
                         'are not used; pass the review date)')
    args = ap.parse_args()

    today = (datetime.date.fromisoformat(args.today) if args.today
             else datetime.date.today())

    relays = find_relays()
    ledger = parse_ledger()

    missing = [r for r in relays if r[0] not in ledger]
    counts = {d: 0 for d in VALID}
    debts = []
    for fn, date, _ in relays:
        if fn not in ledger:
            continue
        disp, note = ledger[fn]
        counts[disp] += 1
        if disp == 'OPEN':
            debts.append((fn, date, _age_days(date, today), note))

    print(f'relays found            : {len(relays)}')
    print(f'rows in RELAY_LEDGER    : {len(ledger)}')
    print(f'  BANKED   {counts["BANKED"]:3}')
    print(f'  DECLINED {counts["DECLINED"]:3}')
    print(f'  OPEN     {counts["OPEN"]:3}   (debts)')
    print(f'MISSING A ROW           : {len(missing)}')

    if missing:
        print('\n*** INVISIBLE WORK — these relays have no disposition ***')
        for fn, date, _ in missing:
            print(f'   {date}  {fn}')

    stale = [d for d in debts if d[2] is not None and d[2] > STALE_DAYS]
    if stale:
        print(f'\n*** DEBTS OLDER THAN {STALE_DAYS} DAYS — escalated by name ***')
        print('    (a debt is not an exemption — B982)')
        for fn, date, age, note in sorted(stale, key=lambda x: -x[2]):
            print(f'   {age:4}d  {fn}')
            if note:
                print(f'          {note[:96]}')

    if args.seed and missing:
        with open(LEDGER, 'a', encoding='utf-8') as fh:
            for fn, date, _ in missing:
                fh.write(f'| `{fn}` | OPEN | _(disposition owed)_ |\n')
        print(f'\nseeded {len(missing)} rows as OPEN in {LEDGER}')
        return 0

    if args.check:
        if missing:
            print('\nFAIL: every relay must carry a disposition '
                  '(BANKED / DECLINED / OPEN).')
            return 1
        if stale:
            print(f'\nFAIL: {len(stale)} debt(s) older than {STALE_DAYS} days.')
            return 1
        print('\nOK: every relay has a disposition and no debt is stale.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
