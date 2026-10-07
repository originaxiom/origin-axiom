#!/usr/bin/env python3
"""W6 of the weave (docs/THE_WEAVE.md): what each of the weave's three lines carries, on every thread of the census.

It joins three records, and computes no count:
- the structure census (the_lines_census.py's record): every thread's member orbits;
- Theorem G's check (the_lines.json): each orbit's line structure;
- sm:B1550's banked read-out (frontier/B1550_the_three_parities/verification/read_out.json): the generic count at every
  member orbit of +LR, -LR, +LLLR and -LLLR, keyed by (state, order, orbit size, m_A, n), alike in its two routes.
On the third level M_3 an orbit with lines gives one local system per line (Theorem G), carrying the member's count; an
orbit fixed by all of V4 gives three local systems cycled by the weave, on no single line. A thread whose member orbits
have no banked count is reported as such; its counts would be sealed before they are read.

    python3 the_lines_content.py CENSUS.json   ->  the_lines_content.json beside this file"""
import ast
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _root():
    for p in HERE.parents:
        if (p / "frontier").is_dir():
            return p
    raise RuntimeError("the repository root was not found")


def main(path):
    census = {r["state"]: r for r in (json.loads(x) for x in open(path) if x.strip())}
    lines = json.loads((HERE / "the_lines.json").read_text())
    ro = json.loads((_root() / "frontier" / "B1550_the_three_parities" / "verification" / "read_out.json").read_text())
    banked = {}
    for k, v in ro["generic counts by (route, state, order, orbit size, m_A, n, count)"].items():
        route, sw, order, size, ma, n, cnt = ast.literal_eval(k)
        banked.setdefault((sw, order, size, ma, n), set()).add(tuple(cnt))
    assert all(len(v) == 1 for v in banked.values()), "the two routes disagree somewhere in the banked read-out"
    out = {}
    for sw, r in census.items():
        per_line, off_line, unread = {}, [], []
        for mo, lo in zip(r["member orbits"], lines[sw]["member orbits"]):
            key = (sw, mo["order"], mo["size"], mo["m_A"], mo["n"])
            cnt = next(iter(banked[key])) if key in banked else None
            kind = f"order {mo['order']}, orbit size {mo['size']}, m_A {mo['m_A']}, n {mo['n']}"
            if cnt is None:
                unread.append(kind)
            elif "members per line" in lo:
                for p in lo["members per line"]:
                    per_line.setdefault(p, []).append({"kind": kind, "count": list(cnt)})
            else:
                off_line.append({"kind": kind, "count": list(cnt), "local systems on M_3": 3})
        gen = {p: sum(1 for x in v if x["count"] == [-1, -1]) for p, v in per_line.items()}
        out[sw] = {"trace": lines[sw]["trace"], "members": r["members"],
                   "each line carries, on the third level (one local system per orbit with lines)": per_line,
                   "generations per line (local systems reading (-1, -1))": gen,
                   "on no single line (orbits fixed by all of V4)": off_line,
                   "member orbits with no banked count": unread}
    (HERE / "the_lines_content.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main(sys.argv[1])
