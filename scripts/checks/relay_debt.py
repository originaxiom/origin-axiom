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
**A debt is not an exemption** (B982): debts are listed with their age and **escalation
is ENFORCED** (B1172): an OPEN row older than STALE_DAYS **fails the gate** unless its
note carries an explicit `ESCALATED(YYYY-MM-DD` marker — escalation-by-name means
somebody actually wrote the escalation down, with a date and a named next action.
A DATELESS open row is treated as stale (the dateless exemption was how the oldest
artifact in the ledger stayed structurally invisible for 10 weeks).

B1172'S FOUR REPAIRS (the sweep found this gate silently dead)
--------------------------------------------------------------
1. `_today()` read the ledger's own stamp — frozen at 2026-08-09 — so the gate believed
   no time ever passed and the 21-day rule NEVER FIRED. Now: the real date, with the
   `OA_RELAY_TODAY` env override for deterministic tests.
2. Stale debts were PRINTED but never failed the gate. Now they fail (minus ESCALATED).
3. `RELAY_RE` matched only the cc3 lane; `CC_TO_CODEX_*` / `CC_TO_CLOUD_*` /
   `CC_TO_ALL_SEATS_*` were invisible (the MC1 assignment went unrowed exactly there).
   Now: any `<SEAT>_TO_<SEATS>_<date>_*.md` plus the proposal/handoff shapes.
   (B1307: the sender list was still a closed set -- SM/FC/FAB5/CHAT1 were invisible; now
   any upper-case sender token. The seat BRANCHES are aged by `harvest_debt.py`.)
4. Dateless OPEN rows skipped the age check entirely. Now stale-by-definition.

DISCIPLINE ON WHO MAY MARK WHAT
-------------------------------
A seat may seed its own relays as OPEN. **A seat may not mark its own relay BANKED** —
that is marking your own homework. BANKED is the receiving seat's judgement and its row
must name the arc that carries the finding, so the claim is checkable by grep.
"""
from __future__ import annotations

import datetime
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
LEDGER = ROOT / "docs" / "RELAY_LEDGER.md"
STALE_DAYS = 21
ESCALATED_RE = re.compile(r"ESCALATED\(\s*[0-9]{4}-[0-9]{2}-[0-9]{2}")

# Relays live outside the tree by the standing rule, so the gate reads the LEDGER as the
# register of what exists, and cross-checks any relay file that IS tracked.
# B1004: widened after cc3 found the ONE artifact that went unadopted today was INVISIBLE to
# this gate. B1172: widened again to every seat lane (CC/CC3/CODEX/CLOUD/ALL_SEATS, any
# direction) after the sweep found the codex/cloud lanes structurally invisible.
# B1307: widened a third time -- `SM_TO_CC`, `FC_TO_CC`, `FAB5_TO_CC`, `CHAT1_TO_CC` were invisible (the lanes that opened after
# B1172); the physics seat's relay of R64-R72 had no row for three days and nothing said so. Any `<SEAT>_TO_<SEATS>_<date>` now.
RELAY_RE = re.compile(
    r"([A-Z0-9]+_TO_[A-Z0-9_]+_[0-9]{4}-[0-9]{2}-[0-9]{2}[A-Za-z0-9_.\-]*\.md"
    r"|[A-Za-z0-9_.\-]*_PROPOSAL\.md|PROPOSAL_[A-Za-z0-9_.\-]*\.md"
    r"|[A-Za-z0-9_.\-]*_HANDOFF\.md|HANDOFF_[A-Za-z0-9_.\-]*\.md)")
# B1307: the first cell may carry text after the name -- "(on the seat's branch @ pin)", a zip's contents -- and three
# BANKED rows (SM x2, cloud) plus the chat1 row were silently unparsed, so the chat1 relay archived on main read as INVISIBLE.
# xB032/xB033 (2026-09-28), the FOURTH invisibility repair on this gate -- and the first that does not
# widen a pattern. B1004, B1172 and B1307 each widened RELAY_RE after a lane turned out to be
# structurally invisible; none added a check that the LEDGER ITSELF parses. Three holes were found at
# once, all silent:
#   (1) a disposition outside {BANKED, DECLINED, OPEN} made the row vanish ENTIRELY -- not counted,
#       not aged, not failed. Four rows were invisible this way: BANKED-AS-LEADS x2, LOGGED, HARVESTED.
#   (2) the note was captured as [^|]*, so a note containing an internal pipe (e.g. \|Cl/Cl²\|,
#       \|Vub\|) had its TAIL UNREAD -- which is how an ESCALATED marker appended to such a row was
#       invisible to the gate that demanded it.
#   (3) rows were collected into a dict keyed by name, so a DUPLICATE name silently dropped the
#       earlier row from every check.
# The repair: recognise the vocabulary actually in use, read the whole note, check EVERY occurrence,
# and -- the part that generalises -- FAIL LOUDLY on any ledger row this regex cannot parse, so the
# next vocabulary drift reports itself instead of disappearing.
DISPOSITIONS = ("BANKED-AS-LEADS", "BANKED", "DECLINED", "OPEN", "LOGGED", "HARVESTED")
CLOSED_WITH_ARC = ("BANKED", "BANKED-AS-LEADS", "HARVESTED")   # must name an arc
ROW_RE = re.compile(
    r"^\|\s*`?(?P<name>[A-Za-z0-9_.\-]+\.md)`?[^|]*\|\s*(?P<disp>" + "|".join(DISPOSITIONS) + r")\s*\|"
    r"\s*(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2}|—|-)\s*\|\s*(?P<note>.*)\|\s*$", re.M)
# any ledger line whose first cell is a .md name -- the population ROW_RE must cover completely
NAMEROW_RE = re.compile(r"^\|\s*`?[A-Za-z0-9_.\-]+\.md`?\s*\|", re.M)


def _today() -> datetime.date:
    # B1172: the real date. The old stamp-based clock froze at 2026-08-09 and the gate
    # never fired. OA_RELAY_TODAY overrides for deterministic tests only.
    env = os.environ.get("OA_RELAY_TODAY")
    if env:
        return datetime.date.fromisoformat(env)
    return datetime.date.today()


def _read(p: pathlib.Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def tracked_relays() -> set[str]:
    """relay files TRACKED by git (the name says tracked; the old filesystem walk red-lit a gitignored archive under audit/ -- Review 56)"""
    import subprocess
    out = set()
    try:
        r = subprocess.run(["git", "-C", str(ROOT), "ls-files", "--", "*.md"], capture_output=True, text=True, timeout=60)
        files = r.stdout.split("\n") if r.returncode == 0 else None
    except Exception:
        files = None
    if files is None:                                   # git unavailable: the walk, minus anything git would ignore by the standing rule (audit/)
        files = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*.md") if ".git" not in p.parts and not str(p.relative_to(ROOT)).startswith("audit/")]
    for rel in files:
        if not rel:
            continue
        name = rel.rsplit("/", 1)[-1]
        if RELAY_RE.fullmatch(name):
            out.add(name)
    return out


def check() -> tuple[list[str], list[str], dict]:
    if not LEDGER.is_file():
        return ([f"{LEDGER.relative_to(ROOT)} is MISSING — the register is constitutive"], [], {})
    text = _read(LEDGER)
    matches = list(ROW_RE.finditer(text))
    fails, stale = [], []
    counts = {d: 0 for d in DISPOSITIONS}
    today = _today()

    # xB033 repair (3): check EVERY occurrence, so a duplicate name cannot shadow an earlier row.
    rows = {m.group("name"): m for m in matches}
    seen = {}
    for m in matches:
        seen[m.group("name")] = seen.get(m.group("name"), 0) + 1
    dups = sorted(n for n, c in seen.items() if c > 1)

    # xB033 repair (1), and the part that generalises: every ledger row must PARSE.
    lines = text.split("\n")
    parsed_lines = set()
    for m in matches:
        parsed_lines.add(text.count("\n", 0, m.start()) + 1)
    unparsed = []
    for i, ln in enumerate(lines, 1):
        if NAMEROW_RE.match(ln) and i not in parsed_lines:
            cell = [c.strip() for c in ln.split("|")]
            unparsed.append(f"line {i}: disposition {cell[2]!r} is not one of {DISPOSITIONS}")
    for u in unparsed:
        fails.append(f"UNPARSED LEDGER ROW — invisible to every check below — {u}")

    for m in matches:
        name = m.group("name")
        d = m.group("disp")
        counts[d] += 1
        note = m.group("note").strip()
        if d in CLOSED_WITH_ARC and not re.search(r"\bB\d{1,4}\b", note):
            fails.append(f"{name}: {d} but the note names no arc — unverifiable")
        if d == "DECLINED" and len(note) < 12:
            fails.append(f"{name}: DECLINED with no reason given")
        if d == "LOGGED" and len(note) < 12:
            fails.append(f"{name}: LOGGED with no content")
        if d == "OPEN":
            escalated = bool(ESCALATED_RE.search(note))
            if m.group("date") in ("—", "-"):
                # B1172: dateless OPEN = stale by definition (repair 4)
                if not escalated:
                    stale.append(f"{name}: OPEN with NO DATE and no ESCALATED marker")
            else:
                age = (today - datetime.date.fromisoformat(m.group("date"))).days
                if age > STALE_DAYS and not escalated:
                    stale.append(f"{name}: OPEN for {age} days (> {STALE_DAYS}), no ESCALATED marker")

    # invisible work: a relay file present in the tree with no ledger row
    for name in sorted(tracked_relays() - set(rows)):
        fails.append(f"{name}: INVISIBLE WORK — relay present with no ledger row")
    return fails, stale, counts


def main() -> int:
    fails, stale, counts = check()
    if counts:
        # xB033: report EVERY disposition present. The old line printed only three, so the four
        # rows this repair made visible would have stayed invisible in the summary -- the same
        # class of blindness one layer up.
        shown = ", ".join(f"{v} {k.lower()}" for k, v in counts.items() if v)
        print(f"  relay-debt: {shown}")
        # recomputed here rather than returned, so check()'s 3-tuple signature stays intact
        # for tests/test_relay_debt_gate.py which imports this module.
        _names = [m.group("name") for m in ROW_RE.finditer(_read(LEDGER))]
        _dups = sorted({n for n in _names if _names.count(n) > 1})
        if _dups:
            print(f"  relay-debt: {len(_dups)} DUPLICATE ledger name(s), all occurrences now "
                  f"checked (previously the earlier row was silently dropped): {', '.join(_dups)}")
    if stale:
        print(f"  relay-debt: {len(stale)} UNESCALATED STALE DEBT(S) — escalate by name or close --")
        for s in stale:
            print(f"    {s}")
    if fails:
        print("  relay-debt: FAILURES --")
        for f in fails:
            print(f"    {f}")
    # B1172 repair 2: stale debts FAIL the gate (they used to be printed and swallowed)
    return 1 if (fails or stale) else 0


if __name__ == "__main__":
    sys.exit(main())
