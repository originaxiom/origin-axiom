#!/usr/bin/env python3
"""relay-debt — every seat-to-seat relay carries a disposition, or it is invisible work.

THE FAILURE THIS EXISTS TO STOP (B999; the design is cc3's, re-implemented here)
-------------------------------------------------------------------------------
Branch protection preserves FILES. Nothing preserved FINDINGS.

`CC3_TO_CC_2026-07-28_rank4_response.md` answered the iota-status question in July.
It never reached main. **L114 was then promoted asking a question that relay had
already answered**, and it cost a full campaign to rediscover.

The mechanism was not neglect: a relay's content lives on main only if somebody banks
it, and NOTHING CHECKED whether that happened. The loss audit found this class once and
it was actioned three ways (B909, B920, B921, branch protection) — and it recurred
anyway, because **every one of those fixes preserved files.**

THE RULE
--------
Every relay carries exactly one disposition in `docs/RELAY_LEDGER.md`:

    BANKED   — the finding is on main; the row NAMES the arc
    DECLINED — considered and rejected; the row says WHY
    OPEN     — a debt, carrying an age

**A relay with no row is the failure state: invisible work.** That fails the gate.
**A debt is not an exemption** (B982): debts are listed with their age and escalated
by name past the threshold.

DISCIPLINE ON WHO MAY MARK WHAT
-------------------------------
A seat may seed its own relays as OPEN. **A seat may not mark its own relay BANKED** —
that is marking your own homework. BANKED is the receiving seat's judgement and its row
must name the arc that carries the finding, so the claim is checkable by grep.
"""
from __future__ import annotations

import datetime
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
LEDGER = ROOT / "docs" / "RELAY_LEDGER.md"
STALE_DAYS = 21

# Relays live outside the tree by the standing rule, so the gate reads the LEDGER as the
# register of what exists, and cross-checks any relay file that IS tracked.
RELAY_RE = re.compile(r"(CC3?_TO_CC3?_[0-9]{4}-[0-9]{2}-[0-9]{2}[A-Za-z0-9_.\-]*\.md)")
ROW_RE = re.compile(
    r"^\|\s*`?(?P<name>[A-Za-z0-9_.\-]+\.md)`?\s*\|\s*(?P<disp>BANKED|DECLINED|OPEN)\s*\|"
    r"\s*(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2}|—|-)\s*\|\s*(?P<note>[^|]*)\|", re.M)


def _today() -> datetime.date:
    # Date is read from the ledger's own stamp when present, so the gate is deterministic
    # under replay and does not depend on wall-clock (which scripts here may not use).
    m = re.search(r"<!--\s*relay-ledger-date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", _read(LEDGER))
    return datetime.date.fromisoformat(m.group(1)) if m else datetime.date(2026, 8, 9)


def _read(p: pathlib.Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def tracked_relays() -> set[str]:
    out = set()
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts:
            continue
        m = RELAY_RE.fullmatch(p.name)
        if m:
            out.add(p.name)
    return out


def check() -> tuple[list[str], list[str], dict]:
    if not LEDGER.is_file():
        return ([f"{LEDGER.relative_to(ROOT)} is MISSING — the register is constitutive"], [], {})
    text = _read(LEDGER)
    rows = {m.group("name"): m for m in ROW_RE.finditer(text)}
    fails, stale = [], []
    counts = {"BANKED": 0, "DECLINED": 0, "OPEN": 0}
    today = _today()

    for name, m in rows.items():
        d = m.group("disp")
        counts[d] += 1
        note = m.group("note").strip()
        if d == "BANKED" and not re.search(r"\bB\d{1,4}\b", note):
            fails.append(f"{name}: BANKED but the note names no arc — unverifiable")
        if d == "DECLINED" and len(note) < 12:
            fails.append(f"{name}: DECLINED with no reason given")
        if d == "OPEN" and m.group("date") not in ("—", "-"):
            age = (today - datetime.date.fromisoformat(m.group("date"))).days
            if age > STALE_DAYS:
                stale.append(f"{name}: OPEN for {age} days (> {STALE_DAYS})")

    # invisible work: a relay file present in the tree with no ledger row
    for name in sorted(tracked_relays() - set(rows)):
        fails.append(f"{name}: INVISIBLE WORK — relay present with no ledger row")
    return fails, stale, counts


def main() -> int:
    fails, stale, counts = check()
    if counts:
        print(f"  relay-debt: {counts['BANKED']} banked, {counts['DECLINED']} declined, "
              f"{counts['OPEN']} open")
    if stale:
        print(f"  relay-debt: {len(stale)} STALE DEBT(S), escalated by name --")
        for s in stale:
            print(f"    {s}")
    if fails:
        print("  relay-debt: FAILURES --")
        for f in fails:
            print(f"    {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
