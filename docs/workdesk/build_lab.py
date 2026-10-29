#!/usr/bin/env python3
"""The Weave Lab's data (the Ledger Desk's front; a proposal's prototype, not an arc; see THE_LEDGER_DESK.md).

Read-only over the record at HEAD (and origin/main for the seats' relay rows), it writes one JSON outside the record,
which the lab page embeds as `const LAB=...;`:

  counts    W arcs, cells run and held, seats, open relay rows, and the record's count (0 of 19)
  arcs      NOTE's status table (extract_desk_data.arcs) joined to W_VERDICTS.json's weave_or_thread label and to the
            cells each arc ran: [id, label, verdict, status, what, first day, last day, held, failed, NOTE line]
  cells     every rule cell joined to its one-run outcome: [arc, cell, prior, held, prediction]
  feed      this branch's commit subjects since the weave began, newest first: [hash, day, step, arc, subject]
  routes    per W arc, the commit of each lifecycle step (build_index.lifecycle), and the order flags
  threads   every primitive word in L and R to length 7 that uses both moves, up to rotation and the swap, with its
            matrix: the threads whose invariant foliations the hero draws on the shared fibre
  census    W178's 266 lines: (a, b), order, zero channel, slowest kernel rate, the cusp pattern at both Re tau, the
            local exponents at Im tau 6-8, and the six per ladder height at Re tau 1/8
  w179      the down-lepton D ladder on (1/2, 1/5) with post hoc 1's heights, the data's 3-sigma window, the tau = i
            values, and W180's limit where its output is committed
  seats     this branch's relay ledger rows grouped by sending seat: rows, open, banked, escalated, latest day

    python3 -B docs/workdesk/build_lab.py --out /path/outside/the/record/lab_data.json
    python3 -B docs/workdesk/build_lab.py --out /path/outside/lab_data.json --page /path/outside/site

With --page it also writes the page: the template the_weave_lab.html with its one line `const LAB=__LAB__;` filled
from this data, as <site>/index.html, and the committed ledger page beside it as <site>/ledger.html.
"""
import argparse
import itertools
import json
import math
import re
import sys
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
import build_index as BI  # noqa: E402
import extract_desk_data as X  # noqa: E402

D = REPO / "docs" / "dossiers" / "the_weave_2026-10-07"
L = ((1, 1), (0, 1))
R = ((1, 0), (1, 1))
STEP_WORDS = [("rule", r"'s rule\b"), ("script", r"'s script\b|'s draft\b"), ("output", r"'s output\b"),
              ("post hoc", r"post hoc"), ("recorded", r"\brecorded\b"), ("reading", r"\breading\b|\bReading\b"),
              ("relay", r"\brelay\b|\bledger\b"), ("desk", r"\bdesk\b|\bworkdesk\b|\bLedger Desk\b")]


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def threads(nmax=7):
    seen, out = set(), []
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" not in w or "R" not in w or any(w == w[:d] * (n // d) for d in range(1, n) if n % d == 0):
                continue
            ex = w.translate(str.maketrans("LR", "RL"))
            c = min(min(x[i:] + x[:i] for i in range(n)) for x in (w, ex))
            if c in seen:
                continue
            seen.add(c)
            A = ((1, 0), (0, 1))
            for ch in c:
                A = mul(A, L if ch == "L" else R)
            out.append([c, A[0][0], A[0][1], A[1][0], A[1][1]])
    return out


def r6(v):
    return None if v is None else round(v, 6)


def census():
    w = json.loads((D / "the_six_at_the_cusp.json").read_text(encoding="utf-8"))
    lines, ladder = [], []
    for e in w["per line"]:
        a, b = Fr(e["line"][0]), Fr(e["line"][1])
        order = math.lcm(a.denominator, b.denominator)
        zero = any(p.get("zero channel") for p in e["per Re tau"])
        pats = [[r6(v) for v in p["cusp pattern e(32,48)"]] if not zero else None for p in e["per Re tau"]]
        p0 = e["per Re tau"][0]
        local = p0["local exponents"].get("6,8") if not zero else None
        lines.append([e["line"][0], e["line"][1], order, zero, r6(e["slowest kernel min(l+, l-)"]), pats,
                      [r6(v) for v in local] if local else None, r6(p0.get("|e(32,48) - e(24,32)| max"))])
        ladder.append(None if zero else {k: [None if v is None else round(v, 5) for v in six]
                                         for k, six in p0["six per height"].items()})
    return {"lines": lines, "ladder": ladder, "heights": sorted(float(k) for k in w["per line"][0]["per Re tau"][0]
                                                                   ["six per height"])}


def w179():
    d = json.loads((D / "the_down_lepton_factor.json").read_text(encoding="utf-8"))
    p = json.loads((D / "the_down_lepton_factor_posthoc.json").read_text(encoding="utf-8"))
    line = next(e for e in d["per line"] if e["line"] == ["1/2", "1/5"])
    row = next(r for r in line["cusp"] if r["x"] == 0.125)
    lad = [[float(y), math.exp(v[2])] for y, v in row["ln (r2, r1, D) per height"].items()]
    lad += [[r[0], r[1]] for r in p["per line"][0]["D per height"] if r[2] == "computed"]
    at_i = sorted(math.exp(e["at i"]["ln (r2, r1, D)"][2]) for e in d["per line"] if e["at i"]["status"] == "finite")
    out = {"ladder": sorted(lad), "fit": p["per line"][0]["fit A, B, C"], "window": d["G2"]["window"],
           "data D": d["the data (read once)"]["D"], "at i": [round(v, 5) for v in at_i], "cells": d["cells"]}
    f = D / "the_integer_lambda_limits.json"
    if f.exists() and BI.git("ls-files", "--error-unmatch", str(f.relative_to(REPO))).strip():
        w = json.loads(f.read_text(encoding="utf-8"))
        out["w180 cells"] = w.get("cells")
        out["w180 limits"] = [[r["line"], r["x"], r["D_inf"]] for r in w.get("per pair", []) if "D_inf" in r]
    return out


def feed(n=180):
    rows = []
    for ln in BI.git("log", f"-{n}", "--format=%h|%cs|%s", "HEAD").decode().splitlines():
        h, day, subj = ln.split("|", 2)
        m = re.match(r"(W\d+)", subj)
        step = next((name for name, rx in STEP_WORDS if re.search(rx, subj[:160])), "other")
        rows.append([h, day, step, m.group(1) if m else "", subj[:150]])
    return rows


def seats():
    out = {}
    for seat, ref in (("sm", "HEAD"),):
        text = BI.git("show", f"{ref}:docs/RELAY_LEDGER.md").decode()
        for line in text.splitlines():
            if not line.startswith("| `"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4:
                continue
            name = re.match(r"`([^`]+)`", cells[0]).group(1)
            frm = (BI.DIRECTION.match(name).group("frm") if BI.DIRECTION.match(name) else name.split("_")[0]).lower()
            disp = (cells[1].split() or ["?"])[0].strip("*,;").upper()
            day = BI.LEDGER_DATE.search(cells[2])
            s = out.setdefault(frm, {"seat": frm, "rows": 0, "open": 0, "banked": 0, "escalated": 0, "latest": "",
                                     "on": set()})
            s["rows"] += 1
            s["open"] += disp == "OPEN"
            s["banked"] += disp.startswith("BANKED") or disp in ("INTEGRATED", "HARVESTED")
            s["escalated"] += "ESCALATED(" in "|".join(cells[3:])
            if day and day.group(0) > s["latest"]:
                s["latest"] = day.group(0)
            s["on"].add(seat)
    names = {"cc": "main", "sm": "this seat", "cc3": "cc3", "codex": "codex", "chat1": "chat1",
             "physical": "physical lane", "audit": "audit lane", "web": "web seat", "chatgpt": "chatgpt"}
    rows = sorted((s for s in out.values() if s["seat"] in names), key=lambda s: -s["rows"])
    for s in rows:
        s["name"] = names[s["seat"]]
    for s in rows:
        s["on"] = sorted(s["on"])
    return rows


def build():
    data = X.desk_data()
    reg = json.loads((D / "W_VERDICTS.json").read_text(encoding="utf-8"))
    label = {a["id"]: a.get("weave_or_thread", "") for a in reg["arcs"]}
    held, failed = {}, {}
    for arc, _c, _p, ok, _pred, _src in data["cells"]:
        (held if ok else failed)[arc] = (held if ok else failed).get(arc, 0) + 1
    arcs = sorted(([a[0], label.get(a[0], ""), a[1], a[3], a[4], a[6], a[7], held.get(a[0], 0), failed.get(a[0], 0),
                    a[5]]
                   for a in data["arcs"]), key=lambda r: int(r[0][1:]))
    steps, flags = BI.lifecycle()
    routes = {}
    for s in steps:
        routes.setdefault(s["arc"].split(":")[1], {}).setdefault(s["step"], [s["commit"], s["order"], s["date"][:10]])
    st = seats()
    cells = [[c[0], c[1], c[2], c[3], c[4]] for c in data["cells"]]
    counts = {"W arcs": len(arcs), "cells run": len(cells), "held": sum(c[3] for c in cells),
              "failed as worded": sum(1 - c[3] for c in cells), "seats": len(st),
              "open relay rows": sum(s["open"] for s in st), "record": "0 of 19"}
    return {"head": BI.git("rev-parse", "--short=9", "HEAD").decode().strip(),
            "day": BI.git("show", "-s", "--format=%cs", "HEAD").decode().strip(), "counts": counts, "arcs": arcs,
            "cells": cells, "feed": feed(), "routes": routes, "flags": flags, "threads": threads(),
            "census": census(), "w179": w179(), "seats": st}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--page", help="a directory outside the record for index.html and ledger.html")
    a = ap.parse_args()
    out = Path(a.out).resolve()
    for p in (out, Path(a.page).resolve() if a.page else None):
        if p is not None and (REPO in p.parents or p == REPO):
            raise SystemExit("--out and --page must lie outside the repository: the lab's data is never committed")
    text = json.dumps(build(), ensure_ascii=False, separators=(",", ":"))
    out.write_text(text, encoding="utf-8")
    print(out, out.stat().st_size)
    if a.page:
        site = Path(a.page).resolve()
        site.mkdir(parents=True, exist_ok=True)
        page = (HERE / "the_weave_lab.html").read_text(encoding="utf-8")
        if page.count("const LAB=__LAB__;") != 1:
            raise SystemExit("the template must hold exactly one line `const LAB=__LAB__;`")
        filled = page.replace("const LAB=__LAB__;", "const LAB=" + text.replace("</", "<\\/") + ";")
        (site / "index.html").write_text(filled, encoding="utf-8")
        (site / "ledger.html").write_text((HERE / "the_ledger_desk.html").read_text(encoding="utf-8"), encoding="utf-8")
        print(site / "index.html")


if __name__ == "__main__":
    main()
