#!/usr/bin/env python3
"""lead-debt -- a deferral lands in exactly two places, and neither was aged.

THE FAILURE THIS EXISTS TO STOP (2026-09-18, registered in the "nothing is lost" plan)
-------------------------------------------------------------------------------------
The record aged two kinds of debt, both failing the push at 21 days: relays (`relay_debt.py`) and seat items
(`harvest_debt.py`). Nothing aged a LEAD in `docs/OPEN_LEADS.md`, and nothing aged an ARC left at `verdict: OPEN`.
Those are the two places a deferral is written. On 2026-09-18 one seat deferred twelve items in a day; all twelve went
to one of the two, and every gate stayed green.

THE RULE (owner's decisions, 2026-09-18)
----------------------------------------
* A lead or an OPEN arc older than STALE_DAYS is STALE unless its own text carries `ESCALATED(YYYY-MM-DD` -- somebody
  wrote the escalation down with a date and a next action -- or, for an arc that is open by construction, `OPEN-BY-DESIGN(`.
* RATCHET, not immediate failure: the stale counts found when the gate was written are frozen as baselines that may
  only shrink. Any count above its baseline fails. A count below it prints a reminder to lower the constant.
  (Precedent: `harvest_debt.py`'s SCHEDULED_BASELINE.)
* A dateless lead is stale by definition (relay-debt's fourth repair).
* A lead number carried by two different open leads is a COLLISION and fails outright: a closure written on one would
  close the other (the E71 class; it happened twice on 2026-09-18).

WHAT COUNTS
-----------
LEAD: a heading `## L<n> ...` or `### L<n> ...` in docs/OPEN_LEADS.md. Its date is the first `registered [on main ]
YYYY-MM-DD` in the heading, else the first date in the heading. A lead id is CLOSED if any of its headings carries
CLOSED, DISCHARGED or WITHDRAWN in capitals. Its text runs from its first heading to the next `## ` heading of another id.
ARC: a `frontier/*/arc_verdict.json` whose verdict is OPEN. Its date is the last commit that touched the arc's directory.
"""
from __future__ import annotations

import datetime
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
LEADS = ROOT / "docs" / "OPEN_LEADS.md"
STALE_DAYS = 21
# the ratchet: frozen 2026-10-01 at the counts the gate found on the day it was written. LOWER them when debt is paid.
LEAD_STALE_BASELINE = 43
ARC_STALE_BASELINE = 83                       # lowered 2026-10-09 (S106): 83 stale OPEN arcs, the ratchet holds the gain

ESCALATED_RE = re.compile(r"ESCALATED\(\s*[0-9]{4}-[0-9]{2}-[0-9]{2}")
BY_DESIGN_RE = re.compile(r"OPEN-BY-DESIGN\(")
HEAD_RE = re.compile(r"^(#{2,3}) (L\d+[a-z]?)\b(.*)$")
REG_RE = re.compile(r"registered(?: on main)?[ ,]+(\d{4}-\d{2}-\d{2})")
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
# a closure marker, not the word in a title ("THE CLOSED FORM OF ..."): it follows **, a dash, or the lead's own number
CLOSED_RE = re.compile(r"(?:\*\*|— |- |L\d+[a-z]? )(?:CLOSED|DISCHARGED|WITHDRAWN)\b")


def _today() -> datetime.date:
    env = os.environ.get("OA_LEAD_TODAY")
    return datetime.date.fromisoformat(env) if env else datetime.date.today()


def parse_leads(text: str) -> dict:
    """lead id -> dict(headings=[(lineno, level, rest)], date, closed, body)"""
    lines = text.split("\n")
    marks = []                                            # (lineno, level, id, rest)
    for i, ln in enumerate(lines):
        m = HEAD_RE.match(ln)
        if m:
            marks.append((i, len(m.group(1)), m.group(2), m.group(3)))
    top = [i for i, ln in enumerate(lines) if ln.startswith("## ")] + [len(lines)]
    leads: dict = {}
    for (i, level, lid, rest) in marks:
        base = re.match(r"L\d+", lid).group(0) if level == 3 else lid       # `### L145a` belongs to L145
        end = next(t for t in top if t > i)
        d = leads.setdefault(base, dict(headings=[], body=[]))
        d["headings"].append((i + 1, level, lid, rest))
        d["body"].append("\n".join(lines[i:end]))
    for lid, d in leads.items():
        heads = " ".join(h[3] for h in d["headings"])
        first2 = [h for h in d["headings"] if h[1] == 2] or d["headings"]
        m = REG_RE.search(" ".join(h[3] for h in first2)) or REG_RE.search(heads) or DATE_RE.search(first2[0][3])
        d["date"] = m.group(1) if m else None
        d["closed"] = any(CLOSED_RE.search(h[3]) for h in d["headings"])
        d["text"] = "\n".join(d["body"])
        d["escalated"] = bool(ESCALATED_RE.search(d["text"]))
        # collision: two level-2 headings, neither closed, with DIFFERENT registered dates and different titles
        regs = {}
        for (ln, level, _, rest) in d["headings"]:
            if level != 2 or CLOSED_RE.search(rest) or "as registered" in rest or "STATUS UPDATE" in rest:
                continue
            r = REG_RE.search(rest)
            if r:
                regs.setdefault(r.group(1), []).append(ln)
        d["collision"] = sorted(regs) if len(regs) > 1 else []
    return leads


def open_arcs() -> list:
    out = []
    for vf in sorted((ROOT / "frontier").glob("*/arc_verdict.json")):
        try:
            v = json.loads(vf.read_text())
        except Exception:
            continue
        if str(v.get("verdict", "")).strip().upper() != "OPEN":
            continue
        arc = vf.parent
        txt = ""
        for name in ("FINDINGS.md", "arc_verdict.json"):
            p = arc / name
            if p.is_file():
                txt += p.read_text(encoding="utf-8", errors="ignore")
        date = None
        try:
            r = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%cs", "--", str(arc.relative_to(ROOT))],
                               capture_output=True, text=True, timeout=30)
            date = r.stdout.strip() or None
        except Exception:
            date = None
        out.append(dict(arc=arc.name, date=date, excused=bool(ESCALATED_RE.search(txt) or BY_DESIGN_RE.search(txt))))
    return out


def check() -> tuple[list[str], list[str], list[str], dict]:
    if not LEADS.is_file():
        return ([f"{LEADS.relative_to(ROOT)} is MISSING -- the register is constitutive"], [], [], {})
    today = _today()
    leads = parse_leads(LEADS.read_text(encoding="utf-8", errors="ignore"))
    fails, stale_leads, stale_arcs = [], [], []
    n_open = 0
    for lid, d in sorted(leads.items(), key=lambda kv: int(re.search(r"\d+", kv[0]).group(0))):
        if d["collision"]:
            fails.append(f"{lid}: COLLISION -- two open leads share this number (registered {', '.join(d['collision'])})")
        if d["closed"]:
            continue
        n_open += 1
        if d["escalated"]:
            continue
        if d["date"] is None:
            stale_leads.append(f"{lid}: open with NO DATE and no ESCALATED marker")
        else:
            age = (today - datetime.date.fromisoformat(d["date"])).days
            if age > STALE_DAYS:
                stale_leads.append(f"{lid}: open for {age} days (> {STALE_DAYS}), no ESCALATED marker")
    arcs = open_arcs()
    for a in arcs:
        if a["excused"]:
            continue
        if a["date"] is None:
            stale_arcs.append(f"{a['arc']}: verdict OPEN with no commit date readable")
        else:
            age = (today - datetime.date.fromisoformat(a["date"])).days
            if age > STALE_DAYS:
                stale_arcs.append(f"{a['arc']}: verdict OPEN, untouched {age} days (> {STALE_DAYS})")
    counts = dict(leads=len(leads), open_leads=n_open, stale_leads=len(stale_leads),
                  open_arcs=len(arcs), stale_arcs=len(stale_arcs))
    if len(stale_leads) > LEAD_STALE_BASELINE:
        fails.append(f"stale leads {len(stale_leads)} > baseline {LEAD_STALE_BASELINE}: a lead aged past {STALE_DAYS} days "
                     f"with no ESCALATED marker -- close it, escalate it by name, or it is a buried deferral")
    if len(stale_arcs) > ARC_STALE_BASELINE:
        fails.append(f"stale OPEN arcs {len(stale_arcs)} > baseline {ARC_STALE_BASELINE}")
    return fails, stale_leads, stale_arcs, counts


def main() -> int:
    fails, stale_leads, stale_arcs, counts = check()
    if counts:
        print(f"  lead-debt: {counts['open_leads']} open leads of {counts['leads']}, {counts['stale_leads']} stale "
              f"(baseline {LEAD_STALE_BASELINE}); {counts['open_arcs']} OPEN arcs, {counts['stale_arcs']} stale "
              f"(baseline {ARC_STALE_BASELINE})")
        if counts["stale_leads"] < LEAD_STALE_BASELINE or counts["stale_arcs"] < ARC_STALE_BASELINE:
            print("  lead-debt: debt was paid -- LOWER the baseline constants so the ratchet holds the gain")
    if "--list" in sys.argv:
        for s in stale_leads + stale_arcs:
            print(f"    {s}")
    if fails:
        print("  lead-debt: FAILURES --")
        for f in fails:
            print(f"    {f}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
