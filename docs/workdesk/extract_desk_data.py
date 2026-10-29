#!/usr/bin/env python3
"""The Ledger Desk's read-only extractor (a proposal's prototype, not an arc; see THE_LEDGER_DESK.md). It reads the weave
dossier and git history and writes the compact data the prototype page embeds as `const DESK = ...`:

  cells  every W rule's (cell, prediction, prior) row joined to its one-run output's cells[cell] (post hocs excluded):
         [arc, cell, prior, held, prediction, "W###_RULE.md:line"]
  arcs   every row of NOTE's status table: [arc, status keyword, "WEAVE" / "THREAD" / "", status line, what, NOTE line,
         first commit date, last commit date]. The tag is set only where the cell itself says "weave result" or
         "thread result"; otherwise it is left empty (unlabelled). Nothing is guessed.

  w125   W125's per-thread tower checks: [bundle, volume, worst |Q dV/pi^2 - 1|, worst |Q l/2pi - 1|] (Q >= 400)
  w176   W176's per-order read-outs: [N, lines of order N, least V, Im tau at the least, the least's line]

It writes nothing in the repository unless --out points there.

    python3 -B docs/workdesk/extract_desk_data.py --out /path/to/desk_data.json
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
D = REPO / "docs" / "dossiers" / "the_weave_2026-10-07"
WEAVE_START = "2026-10-07"   # W numbers before the weave dossier name other things (the August waves)


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True).stdout


def priors():
    rows = {}
    row_re = re.compile(r"^\|\s*([A-Za-z]+\d*[a-z′']?)\s*\|(.*)\|\s*(\d{1,3})\s*%\s*\|\s*$")
    for rf in sorted(D.glob("W*_RULE.md")):
        in_tab = False
        for i, ln in enumerate(rf.read_text(encoding="utf-8").splitlines(), 1):
            if re.match(r"^\|\s*cell\s*\|\s*prediction\s*\|\s*prior\s*\|", ln, re.I):
                in_tab = True
                continue
            if in_tab:
                if not ln.startswith("|"):
                    in_tab = False
                    continue
                m = row_re.match(ln)
                if m:
                    rows[(rf.name, m.group(1))] = (int(m.group(3)) / 100, re.sub(r"\*\*", "", m.group(2)).strip(),
                                                   f"{rf.name}:{i}")
    return rows


def outcomes():
    out = {}
    for jf in sorted(D.glob("*.json")):
        if "posthoc" in jf.name:
            continue
        try:
            d = json.loads(jf.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        if not isinstance(d, dict) or not isinstance(d.get("cells"), dict):
            continue
        if "post hoc" in str(d.get("status", "")).lower():
            continue
        rule = d.get("rule")
        if not rule and isinstance(d.get("arc"), str) and re.fullmatch(r"W\d+", d["arc"]):
            rule = f"{d['arc']}_RULE.md"
        if not rule:
            continue
        for c, v in d["cells"].items():
            if isinstance(v, bool):
                out[(Path(str(rule)).name, c)] = v
    return out


def arcs():
    note = (D / "NOTE.md").read_text(encoding="utf-8").splitlines()
    dates = {}
    for ln in git("log", "--format=%h|%cs|%s").splitlines()[::-1]:
        _h, day, subj = ln.split("|", 2)
        if day < WEAVE_START:
            continue
        m = re.match(r"(W\d+)(?:'s| recorded| )", subj)
        if m:
            dates.setdefault(m.group(1), [day, day])[1] = day
    rows, seen = [], set()
    for i, ln in enumerate(note, 1):
        m = re.match(r"^\| (W\d+)[^|]*\| ([^|]+)\| (.+) \|$", ln)
        if not m or m.group(1) in seen:
            continue
        seen.add(m.group(1))
        st = m.group(2).strip()
        kw = re.match(r"([A-Z]+)", st)
        w, t = bool(re.search(r"weave result", st, re.I)), bool(re.search(r"thread result", st, re.I))
        tag = "WEAVE" if w and not t else ("THREAD" if t and not w else "")
        first, last = dates.get(m.group(1), ["", ""])
        rows.append([m.group(1), kw.group(1) if kw else "?", tag, st[:260], m.group(3)[:260], i, first, last])
    return rows


def towers():
    w125 = json.loads((D / "the_quantum_weave.json").read_text(encoding="utf-8"))
    rows = []
    for b in w125["per bundle"]:
        k1 = next(v for k, v in b.items() if k.startswith("K1 worst |Q dV"))
        k2 = next(v for k, v in b.items() if k.startswith("K2 worst |Q l"))
        rows.append([b["bundle"], b["volume"], k1, k2])
    w176 = json.loads((D / "the_class_by_the_dynamics.json").read_text(encoding="utf-8"))
    orders = [[int(n), p["lines"], p["least"]["V"], p["least"]["tau"][1], "(" + ", ".join(p["least"]["line"]) + ")"]
              for n, p in w176["per order"].items()]
    return rows, orders


def desk_data():
    """the page's data, as one dict"""
    p, o = priors(), outcomes()
    cells = [[re.match(r"(W\d+)", rule).group(1), c, pr, int(o[(rule, c)]), pred[:160], src]
             for (rule, c), (pr, pred, src) in p.items() if (rule, c) in o]
    w125, w176 = towers()
    return {"head": git("rev-parse", "--short=9", "HEAD").strip(), "cells": cells, "arcs": arcs(),
            "w125": w125, "w176": w176}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", help="write the JSON here (default: print it)")
    a = ap.parse_args()
    text = json.dumps(desk_data(), ensure_ascii=False, separators=(",", ":"))
    if a.out:
        Path(a.out).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
