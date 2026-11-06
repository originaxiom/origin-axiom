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
   [2026-11-03, the owner's ruling on P-587] This applies to DEBT rows only (rule 6).
6. TYPED (the owner, 2026-11-03, P-587: "yes" to main's proposal): every QUEUED or LEAD row's `where` carries exactly one
   type tag -- [DEBT] (a result the record uses is owed a check or a correction), [LEAD] (an idea, a question, a computation
   not done; nothing current rests on it) or [PROCESS] (tooling, documents, harvests, governance). Only debts age. Every
   open DEBT row is named in the register's ranked list (the section headed "## The debts, by load"), and that list names
   only open DEBT rows: debts are worked in that order.
7. DIRECTION LEADS AGE (the owner's ruling of 2026-11-04 on P-659, M1): a [LEAD] row that comes from the owner (source OW),
   from the brainstorms re-read or a brainstorm (BS), a meditation, the framing ledger (FL-nn) or a review (R7n) ages like a
   debt: unmoved for STALE_DAYS it fails unless ESCALATED -- its first step run, a dated decline, or put to the owner.
   Phase-in: the clock starts at M1_START for rows older than it.
8. A HOST CANNOT CLOSE OVER ITS CHILDREN (M2, M3): a row that says "joined under P-H" or "merged into P-H" keeps its own
   disposition, and P-H cannot be DONE while it is open; an umbrella row listing "children P-..." cannot be DONE while a
   listed child is open.
9. AUDIT-ROOM DRAFTS LAND OR ARE DECLINED (M6): an open row citing a gitignored audit/ path fails once its moved date is
   more than DRAFT_DAYS old (STALE_DAYS for rows older than M1_START, the phase-in), unless its where carries
   DRAFT-DECLINED(YYYY-MM-DD: reason) -- land the draft (cite the tracked path) or decline it.
Every run also prints the open OWNER rows (M6: every report to the owner lists them) and, report-only until CARRY_FROM,
the carry scan (M4): a FINDINGS line of an arc from B1833 on saying "owed", "carried forward", "not computed" or "never
computed" whose arc no register row cites.
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
FLOOR = 729
STALE_DAYS = 21
M1_START = datetime.date(2026, 11, 4)   # the owner's ruling on P-659: direction leads and drafts age from here
DRAFT_DAYS = 7
CARRY_FROM = datetime.date(2026, 11, 18)   # M4 report-only before this date, failing from it
DIRECTION_SRC = re.compile(r"\b(OW|BS)\b|^R7\d")
DIRECTION_POINT = re.compile(r"\bFL-\d+|Meditation")
LINK_RE = re.compile(r"(?:joined under|merged into) (P-\d{3})")
CHILDREN_RE = re.compile(r"children ((?:P-\d{3}(?:, | and |,)?)+)")
DRAFT_DECLINED = re.compile(r"DRAFT-DECLINED\((\d{4}-\d{2}-\d{2})")
DISPOSITIONS = {"DONE", "QUEUED", "LEAD", "OWNER", "DECLINED"}
ROW_RE = re.compile(r"^\|\s*(P-\d{3})\s*\|(.*)\|\s*$")
SLOT_RE = re.compile(r"^\|\s*(Q\d+)\s*\|")
ESC_RE = re.compile(r"ESCALATED\((\d{4}-\d{2}-\d{2})")
TYPE_RE = re.compile(r"\[(DEBT|LEAD|PROCESS)\]")
RANK_HEAD = "## The debts, by load"
PATH_RE = re.compile(r"(?<![\w/.-])((?:docs|frontier|scripts|tests|papers|reports)/[\w./-]+\.\w+|GENESIS\.md)")


def _today() -> datetime.date:
    env = os.environ.get("OA_POINT_TODAY")
    return datetime.date.fromisoformat(env) if env else datetime.date.today()


def _date(s: str):
    try:
        return datetime.date.fromisoformat(s.strip())
    except ValueError:
        return None


def ranked(text: str):
    """the P-ids of the ranked debt list, in order (the numbered lines under RANK_HEAD, up to the next heading)"""
    out, inside = [], False
    for line in text.splitlines():
        if line.startswith(RANK_HEAD):
            inside = True; continue
        if inside and line.startswith("## "):
            break
        if inside:
            m = re.match(r"^\s*\d+\.\s+\**(P-\d{3})\b", line)
            if m: out.append(m.group(1))
    return out


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
            types = set(TYPE_RE.findall(where))
            if len(types) != 1:
                fails.append(f"{pid}: {disp} row {'untyped' if not types else 'with two types'} -- tag it [DEBT], [LEAD] or [PROCESS] (rule 6)")
            typ = next(iter(types)) if len(types) == 1 else "?"
            d = _date(moved)
            esc = [_date(e) for e in ESC_RE.findall(where)]
            fresh_esc = any(e and (today - e).days <= STALE_DAYS for e in esc)
            age = (today - d).days if d else None
            if typ == "DEBT" and (age is None or age > STALE_DAYS) and not fresh_esc:
                fails.append(f"{pid}: {disp} DEBT unmoved {age if age is not None else '?'} days (> {STALE_DAYS}) without ESCALATED")
            clock = (today - max(d, M1_START)).days if d else None
            if typ == "LEAD" and (DIRECTION_SRC.search(_src) or DIRECTION_POINT.search(point)) and not fresh_esc \
                    and (clock is None or clock > STALE_DAYS):
                fails.append(f"{pid}: a direction lead unmoved {clock if clock is not None else '?'} days (> {STALE_DAYS}) -- run its first step, decline it with a date, or put it to the owner (rule 7, M1)")
            if "audit/" in point + where and not DRAFT_DECLINED.search(where) and d:
                limit = DRAFT_DAYS if d >= M1_START else STALE_DAYS
                if clock is not None and clock > limit:
                    fails.append(f"{pid}: cites an audit-room draft unmoved {clock} days (> {limit}) -- land it at a tracked path or mark DRAFT-DECLINED (rule 9, M6)")
            open_rows.append((pid, sorted(named)[0] if named else "?", age, typ))
    disp_of = {pid: cells[3] for pid, cells in rows if len(cells) == 6}
    open_ids = {pid for pid, dd in disp_of.items() if dd in ("QUEUED", "LEAD", "OWNER")}
    for pid, cells in rows:
        if len(cells) != 6:
            continue
        for host in LINK_RE.findall(cells[2] + " " + cells[4]):
            if pid in open_ids and disp_of.get(host) == "DONE":
                fails.append(f"{host}: DONE while {pid}, joined or merged into it, is open (rule 8, M3)")
        if cells[3] == "DONE":
            for grp in CHILDREN_RE.findall(cells[2]):
                for child in re.findall(r"P-\d{3}", grp):
                    if child in open_ids:
                        fails.append(f"{pid}: an umbrella DONE while its child {child} is open (rule 8, M2)")
    rank = ranked(text)
    debts = {pid for pid, _, _, t in open_rows if t == "DEBT"}
    for pid in sorted(debts - set(rank)):
        fails.append(f"{pid}: an open DEBT missing from the ranked list ({RANK_HEAD!r})")
    for pid in rank:
        if pid not in debts:
            fails.append(f"the ranked list names {pid}, which is not an open DEBT row")
    if len(rank) != len(set(rank)):
        fails.append("the ranked list names a row twice")
    return fails, open_rows, rows


def main(argv=None) -> int:
    path = pathlib.Path(os.environ.get("OA_POINT_REGISTER", REGISTER))
    if not path.exists():
        print("point-debt: docs/POINT_REGISTER.md missing"); return 1
    fails, open_rows, rows = check(path.read_text(encoding="utf-8"))
    text = path.read_text(encoding="utf-8")
    rank = ranked(text)
    by = {t: [r for r in open_rows if r[3] == t] for t in ("DEBT", "LEAD", "PROCESS", "?")}
    oldest = max((a for _, _, a, t in open_rows if t == "DEBT" and a is not None), default=0)
    print(f"point-debt: {len(rows)} points, {len(open_rows)} open -- {len(by['DEBT'])} debts (oldest {oldest} days), "
          f"{len(by['LEAD'])} leads, {len(by['PROCESS'])} process" + (f", {len(by['?'])} untyped" if by['?'] else "")
          + f"; next debt {rank[0] if rank else 'none'}")
    owner = [pid for pid, cells in rows if len(cells) == 6 and cells[3] == "OWNER"]
    print(f"  owner calls open ({len(owner)}): " + ", ".join(owner))
    carry = carry_scan(text)
    today = _today()
    if carry:
        tag = "FAIL" if today >= CARRY_FROM else "carry-scan (report-only until %s)" % CARRY_FROM
        for c in carry[:8]:
            print("  " + tag, c)
        if today >= CARRY_FROM:
            fails = fails + carry
    for f in fails:
        print("  FAIL", f)
    return 1 if fails else 0


def carry_scan(text: str, root: pathlib.Path = ROOT, first: int = 1833):
    """M4: every 'owed / carried forward / not computed' line in an arc's FINDINGS (from B1833 on) has a register row citing the arc"""
    out = []
    fr = root / "frontier"
    if not fr.exists():
        return out
    for dd in sorted(fr.iterdir()):
        mm = re.match(r"B(\d+)_", dd.name)
        if not mm or int(mm.group(1)) < first or not (dd / "FINDINGS.md").exists():
            continue
        body = (dd / "FINDINGS.md").read_text(encoding="utf-8", errors="replace")
        if re.search(r"\b(owed|carried forward|not computed|never computed)\b", body, flags=re.I) and \
                not re.search(r"\bB%s\b" % mm.group(1), text):
            out.append(f"B{mm.group(1)}: its FINDINGS name owed or uncomputed work and no register row cites the arc (M4)")
    return out


if __name__ == "__main__":
    sys.exit(main())
