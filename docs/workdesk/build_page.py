#!/usr/bin/env python3
"""The Ledger Desk's page, rebuilt from the record (a proposal's prototype, not an arc; see THE_LEDGER_DESK.md).

It takes the committed page, docs/workdesk/the_ledger_desk.html, keeps its markup and script, and replaces its two data
lines: `const DESK=` with a fresh extraction (extract_desk_data.py, plus the index's page_index.json from
build_index.py) and `const SHA =` with the commit the data came from, so every link points at that commit. It writes
<out>/index.html outside the repository and never writes into it.

Panels recompute from the data. Numbers written into the page's prose are as of the page's last commit; a rebuild does
not change them.

    python3 -B docs/workdesk/build_index.py --out /tmp/desk/index --check
    python3 -B docs/workdesk/build_page.py --index /tmp/desk/index --out /tmp/desk/site
"""
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
import extract_desk_data as X  # noqa: E402

PAGE = HERE / "the_ledger_desk.html"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True, help="the directory build_index.py wrote")
    ap.add_argument("--out", required=True, help="a directory outside the record")
    a = ap.parse_args()
    out = Path(a.out).resolve()
    if REPO in out.parents or out == REPO:
        raise SystemExit("--out must lie outside the repository: the page's data is derived and is never committed")
    data = X.desk_data()
    data["index"] = json.loads((Path(a.index) / "page_index.json").read_text(encoding="utf-8"))
    sha = X.git("rev-parse", "HEAD").strip()
    lines = PAGE.read_text(encoding="utf-8").split("\n")
    swaps = {"const DESK=": "const DESK=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";",
             'const SHA = "': f'const SHA = "{sha}";'}
    for prefix, new in swaps.items():
        at = [i for i, ln in enumerate(lines) if ln.startswith(prefix)]
        if len(at) != 1:
            raise SystemExit(f"the page must hold exactly one line starting {prefix!r}; found {len(at)}")
        lines[at[0]] = new
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"page": str(out / "index.html"), "commit": sha[:9],
                      "arcs": data["index"]["manifest"]["tables"]["arcs"]["rows"]}))


if __name__ == "__main__":
    main()
