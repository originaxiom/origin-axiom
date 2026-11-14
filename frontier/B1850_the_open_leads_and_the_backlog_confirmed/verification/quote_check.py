"""Main's mechanical check of the read-only checkers' evidence (R76-1): every quote behind a decision must be a verbatim
substring (whitespace-normalised) of the file it names. Prints the count; exits 1 on any miss."""
import json, os, pathlib, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
def norm(s): return " ".join(unicodedata.normalize("NFC", s).split())
def check(names=("checks_open_leads.json", "checks_backlog_cloud.json", "checks_backlog_physics.json", "checks_backlog_retired.json")):
    cache, n, bad = {}, 0, []
    for name in names:
        for o in json.load(open(HERE / name, encoding="utf-8")):
            p = o["path"]
            if p not in cache:
                fp = ROOT / p
                if not fp.is_file() and p.startswith(("legacy/", "story/", "paths/", "speculations/", "philosophy/")):
                    fp = ROOT / "docs" / "archive" / p          # 2026-11-13: the historical folders moved under docs/archive/ (docs/REORGANIZATIONS.md, its third entry); the quotes keep their paths as written
                cache[p] = norm(fp.read_text(encoding="utf-8", errors="replace")) if fp.is_file() else None
            if cache[p] is None and p.startswith("audit/"):
                continue      # the gitignored audit room (L185's evidence that its answer lives only there): main's tree only
            n += 1
            if cache[p] is None or norm(o["quote"]) not in cache[p]:
                bad.append((name, o.get("lead") or o.get("row"), p))
    return n, bad
if __name__ == "__main__":
    n, bad = check()
    print(f"{n} quotes checked, {len(bad)} not found verbatim at their paths")
    for b in bad: print("  ", b)
    sys.exit(1 if bad else 0)
