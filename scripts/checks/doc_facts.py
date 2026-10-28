#!/usr/bin/env python3
"""doc-facts -- a front page must not state a current fact that its source contradicts (P-417, the owner's question of
2026-10-28: "how do we make sure all the documentation ... reflect the most recent state of the repo").

doc-currency (B984) measures recency: a living document's newest arc citation against the corpus. It cannot see a stale
statement next to a fresh one -- the README cited B1792 while its opening banner said "`GENESIS.md` is at v1.14" three weeks
after v1.59. This check reads facts from their sources and every PRESENT-TENSE statement of them on the front pages.

Facts checked (extend FACTS, never weaken a pattern):
  genesis-version  source: GENESIS.md's header "**Version X.Y"; statement: "GENESIS.md is at vX.Y" / "GENESIS is at vX.Y"
Past-tense or dated mentions ("GENESIS v1.14", "was at v1.14") are history and are not checked.
"""
from __future__ import annotations
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
FRONT = ["README.md", "ROADMAP.md", "docs/MAIN_GOAL.md", "docs/INDEX.md", "docs/CAMPAIGN_STATUS.md", "docs/MASTERPLAN.md"]


def genesis_version(root: pathlib.Path) -> str | None:
    m = re.search(r"\*\*Version (\d+\.\d+)", (root / "GENESIS.md").read_text(encoding="utf-8", errors="replace"))
    return m.group(1) if m else None


STATEMENT = re.compile(r"`?GENESIS(?:\.md)?`?\s+is\s+at\s+v(\d+\.\d+)")


def check(root: pathlib.Path = ROOT, front: list[str] = FRONT) -> list[str]:
    problems = []
    gv = genesis_version(root)
    if gv is None:
        return ["genesis-version: GENESIS.md has no '**Version X.Y' header -- the source of the fact is gone"]
    for rel in front:
        p = root / rel
        if not p.is_file():
            continue
        for n, line in enumerate(p.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
            for m in STATEMENT.finditer(line):
                if m.group(1) != gv:
                    problems.append(f"genesis-version: {rel}:{n} says 'is at v{m.group(1)}', GENESIS.md is at v{gv}")
    return problems


def main() -> int:
    problems = check()
    if problems:
        print("  doc-facts: STALE FACTS on the front pages --")
        for p in problems:
            print("    " + p)
        print("  a front page states a current fact its source contradicts: update the line (a one-line fix at landing, P-417).")
        return 1
    print("  doc-facts: ok (genesis-version)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
