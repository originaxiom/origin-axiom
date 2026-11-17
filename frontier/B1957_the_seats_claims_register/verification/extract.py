"""B1957: every statement in every markdown file the seats added or changed in the window, as registered units.
A unit is a bullet or numbered item, a table row, or a paragraph, with its file, first line and text.  Mechanical, so that
none is skipped.  Run by hand (it needs the seats' remote branches); it writes UNITS.json.  Nothing of a seat's is run."""
import hashlib, json, pathlib, re, subprocess
HERE = pathlib.Path(__file__).resolve().parent
LANES = (  # (lane, the seat's name, branch, base before the window, head harvested to)
    ("agy-exp", "agy-exp", "origin/agy/self-consistent-loop-2026-11-11", "ef140a024", "017266d87"),
    ("agy-002-verify", "agy-002", "origin/agy-002/verify", "53ac6c7d", "62420b533"),
    ("agy-002-endgame", "agy-002", "origin/agy-002/endgame", "613c4f417", "94e511f54"),
    ("agy-002-closure", "agy-002", "origin/agy-002/closure", "94e511f54", "358d61786"),
    ("physical", "physical (codex)", "origin/audit/physical-bridge-2026-09-05", "1aa76251", "f0411fd82"),
    ("web", "the web seat (chat1)", "origin/chat1/web-seat", "b1727da04", "401c9bd7e"),
    ("agy-audit", "agy", "origin/agy/audit-2026-11-02", "da5c7125", "d1c71f255"),
)
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
BUL = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S"); TROW = re.compile(r"^\s*\|.*\|\s*$"); TSEP = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
META = re.compile(r"^\W*(from|to|date|kind|seat|card|read|state|on|needs|next push)\W*[:*]", re.I)


def units_of(text):
    L = text.split("\n"); out = []; cur = None; section = ""; fence = False
    def close():
        nonlocal cur
        if cur: out.append(cur)
        cur = None
    for n, line in enumerate(L, 1):
        if line.strip().startswith("```"):
            fence = not fence
            if cur: cur["text"] += "\n" + line
            continue
        if fence:
            if cur: cur["text"] += "\n" + line
            continue
        if not line.strip(): close(); continue
        if line.lstrip().startswith("#"): close(); section = line.strip().lstrip("#").strip()[:160]; continue
        if TSEP.match(line): close(); continue
        if TROW.match(line):
            close(); head = n < len(L) and bool(TSEP.match(L[n]))       # a row followed by a separator is a table's header
            cur = {"line": n, "form": "head" if head else "row", "section": section, "text": line.strip()}; close(); continue
        if BUL.match(line): close(); cur = {"line": n, "form": "item", "section": section, "text": line.strip()}; continue
        if cur is None: cur = {"line": n, "form": "paragraph", "section": section, "text": line.strip()}
        else: cur["text"] += " " + line.strip()
    close(); return out


def tag(path):
    parts = path.split("/"); stem = re.sub(r"\.md$", "", parts[-1])
    if parts[0] == "relays" and len(parts) == 2: return stem
    return "/".join(parts[1:-1] + [stem]) if parts[0] in ("relays", "reports") else path[:-3]


if __name__ == "__main__":
    allu = []; files = []
    for lane, seat, ref, base, head in LANES:
        assert git("rev-parse", "--short=9", ref).strip() == head, (lane, git("rev-parse", "--short=9", ref).strip(), head)
        names = [f for f in git("diff", "--name-only", "--diff-filter=AM", base, ref, "--", "*.md").split("\n") if f]
        for f in sorted(names):
            text = git("show", "%s:%s" % (ref, f)); us = units_of(text); k = 0
            for u in us:
                t = re.sub(r"\s+", " ", u["text"])
                kind = "meta" if (u["form"] == "head" or len(t) < 25 or META.match(t) or t.strip("*` .") in ("0 of 19", "")) else "statement"
                allu.append({"id": "%s:%s:%d" % (lane, tag(f), u["line"]), "lane": lane, "seat": seat, "file": f, "line": u["line"], "form": u["form"],
                             "section": u["section"], "kind": kind, "sha": hashlib.sha1(t.encode()).hexdigest()[:10], "text": t[:700]}); k += 1
            files.append({"lane": lane, "seat": seat, "file": f, "head": head, "lines": text.count("\n") + 1, "units": k})
    assert len({u["id"] for u in allu}) == len(allu)
    lanes = [dict(zip(("lane", "seat", "branch", "base", "head"), l)) for l in LANES]
    # the committed register holds each unit's id, form, kind and a hash of its text; the text itself is read at the source
    compact = [[u["id"], u["form"][0], u["kind"][0], u["sha"]] for u in allu]
    (HERE / "UNITS.json").write_text(json.dumps({"lanes": lanes, "files": files, "units": compact}, separators=(",", ":"), ensure_ascii=False) + "\n")
    full = HERE.parents[2] / "audit" / "claims" / "UNITS_full.json"; full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(json.dumps({"lanes": lanes, "files": files, "units": allu}, ensure_ascii=False) + "\n")
    import collections
    c = collections.Counter(u["lane"] for u in allu); s = collections.Counter(u["lane"] for u in allu if u["kind"] == "statement"); fl = collections.Counter(x["lane"] for x in files)
    for lane, *_ in LANES: print("%-16s %4d files, %5d units, of which %5d statements" % (lane, fl[lane], c[lane], s[lane]))
    print("total: %d files, %d units, %d statements" % (len(files), len(allu), sum(s.values())))
