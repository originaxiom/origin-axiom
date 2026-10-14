#!/usr/bin/env python3
"""point-debt — every point a review raises has a row, a disposition and a place in one queue (docs/POINT_REGISTER.md).

THE FAILURE THIS EXISTS TO STOP (the owner, 2026-10-13)
-------------------------------------------------------
"we come up with conclusions like the ones from this session, we clarify the picture, but fail to address all the points
we made, and get lost to one of the multiple things we have to deal with. then over and over."

A review or audit raises many points; the record banks the one being worked on and the others survive only as prose.
Relays (relay_debt.py), seat items (harvest_debt.py) and leads (lead_debt.py) are aged; a *point* was not.

THE RULE (checked here)
-----------------------
1. Every row `| P-NNN | date | source | point | DISPOSITION | where | moved |` has one of DONE, QUEUED, LEAD, OWNER,
   DECLINED, and a non-empty `where`.
2. The IDs run P-001 … P-N without gaps or repeats, and N >= FLOOR: a row cannot be deleted. Adding rows means raising
   FLOOR in the same commit (the lock checks FLOOR equals N).
3. DONE names something checkable: every arc ID B<n> it names has a frontier directory, every path it names exists.
4. QUEUED names a slot Q<n> defined in the queue table; LEAD names an L<n> registered in docs/OPEN_LEADS.md and a slot.
5. A QUEUED or LEAD row whose `moved` date is more than STALE_DAYS old fails, unless its `where` carries
   ESCALATED(YYYY-MM-DD: next action) dated within STALE_DAYS. A row without a valid date is stale.
The clock is the real date; OA_POINT_TODAY=YYYY-MM-DD overrides it for tests. OA_POINT_REGISTER overrides the file.
"""
from __future__ import annotations

import datetime
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
REGISTER = ROOT / "docs" / "POINT_REGISTER.md"
LEADS = ROOT / "docs" / "OPEN_LEADS.md"
FLOOR = 129
STALE_DAYS = 21
DISPOSITIONS = {"DONE", "QUEUED", "LEAD", "OWNER", "DECLINED"}
ROW_RE = re.compile(r"^\|\s*(P-\d{3})\s*\|(.*)\|\s*$")
SLOT_RE = re.compile(r"^\|\s*(Q\d+)\s*\|")
ESC_RE = re.compile(r"ESCALATED\((\d{4}-\d{2}-\d{2})")
PATH_RE = re.compile(r"(?<![\w/.-])((?:docs|frontier|scripts|tests|papers|reports)/[\w./-]+\.\w+|GENESIS\.md)")


def _today() -> datetime.date:
    env = os.environ.get("OA_POINT_TODAY")
    return datetime.date.fromisoformat(env) if env else datetime.date.today()


def _date(s: str):
    try:
        return datetime.date.fromisoformat(s.strip())
    except ValueError:
        return None


def parse(text: str):
    rows, slots = [], set()
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if m:
            cells = [c.strip() for c in m.group(2).split("|")]
            rows.append((m.group(1), cells))
            continue
        q = SLOT_RE.match(line)
        if q:
            slots.add(q.group(1))
    return rows, slots


def check(text: str, root: pathlib.Path = ROOT, leads_text: str | None = None, today: datetime.date | None = None):
    today = today or _today()
    if leads_text is None:
        leads_text = LEADS.read_text(encoding="utf-8") if (root / "docs" / "OPEN_LEADS.md").exists() else ""
    leads = set(re.findall(r"^## (L\d+)\b", leads_text, flags=re.M))
    frontier = {d.name.split("_")[0] for d in (root / "frontier").iterdir()} if (root / "frontier").exists() else set()
    rows, slots = parse(text)
    fails, open_rows = [], []
    ids = [r[0] for r in rows]
    if len(ids) != len(set(ids)):
        fails.append("repeated ID")
    want = [f"P-{i:03d}" for i in range(1, len(ids) + 1)]
    if ids != want:
        fails.append(f"IDs not P-001..P-{len(ids):03d} in order (a gap is a deleted point)")
    if len(ids) < FLOOR:
        fails.append(f"{len(ids)} rows < FLOOR {FLOOR}: a point was deleted")
    for pid, cells in rows:
        if len(cells) != 6:
            fails.append(f"{pid}: {len(cells)} cells, expected 6"); continue
        _reg, _src, point, disp, where, moved = cells
        if disp not in DISPOSITIONS:
            fails.append(f"{pid}: disposition {disp!r}"); continue
        if not where or not point:
            fails.append(f"{pid}: empty point or where"); continue
        if disp == "DONE":
            for arc in re.findall(r"\bB(\d{3,4})\b", where):
                if f"B{arc}" not in frontier:
                    fails.append(f"{pid}: DONE names B{arc}, no frontier directory")
            for path in PATH_RE.findall(where):
                if not (root / path).exists():
                    fails.append(f"{pid}: DONE names {path}, which does not exist")
        if disp in ("QUEUED", "LEAD"):
            named = set(re.findall(r"\bQ\d+\b", where))
            if not named:
                fails.append(f"{pid}: {disp} without a queue slot")
            for q in named - slots:
                fails.append(f"{pid}: slot {q} not defined in the queue table")
            if disp == "LEAD":
                for lead in re.findall(r"\bL\d+\b", where):
                    if lead not in leads:
                        fails.append(f"{pid}: {lead} not registered in OPEN_LEADS")
                if not re.search(r"\bL\d+\b", where):
                    fails.append(f"{pid}: LEAD without an L-number")
            d = _date(moved)
            esc = [_date(e) for e in ESC_RE.findall(where)]
            fresh_esc = any(e and (today - e).days <= STALE_DAYS for e in esc)
            age = (today - d).days if d else None
            if (age is None or age > STALE_DAYS) and not fresh_esc:
                fails.append(f"{pid}: {disp} unmoved {age if age is not None else '?'} days (> {STALE_DAYS}) without ESCALATED")
            open_rows.append((pid, sorted(named)[0] if named else "?", age))
    return fails, open_rows, rows


def main(argv=None) -> int:
    path = pathlib.Path(os.environ.get("OA_POINT_REGISTER", REGISTER))
    if not path.exists():
        print("point-debt: docs/POINT_REGISTER.md missing"); return 1
    fails, open_rows, rows = check(path.read_text(encoding="utf-8"))
    nxt = min((int(q[1:]), q) for _, q, _ in open_rows if q != "?")[1] if open_rows else "none"
    oldest = max((a for _, _, a in open_rows if a is not None), default=0)
    print(f"point-debt: {len(rows)} points, {len(open_rows)} open (oldest {oldest} days), next slot {nxt}")
    for f in fails:
        print("  FAIL", f)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
