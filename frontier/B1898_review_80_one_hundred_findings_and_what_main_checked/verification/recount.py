#!/usr/bin/env python3
"""Review 80: every count that the arc's page and the review's entry give, made again from the two tables as main wrote
them, from the outputs main kept, and from git at the three commits named below.

    python3 frontier/B1898_review_80_one_hundred_findings_and_what_main_checked/verification/recount.py [--write]

Each count is printed with the way it was made.  With --write the same is written beside this file as recount.json.
Nothing is read from the working tree but this arc's own files; everything else is read from git, so that the counts do
not move when the tree does.  Where a commit is not in the clone (a shallow clone, an export) the counts that need it are
given as null and said to be missing: they are never guessed.

What this does not do: it judges no finding and reads no reader's file.  The four readers' files are read only by the
checks main wrote (in checks/), which print counts and nothing of a file that is read through a mask."""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = ARC.parents[1]
ANCHOR_BEFORE = "0dda7b472"         # the anchor of Review 79: where this review's window begins
READ = "c40446392"                  # the commit the four readers read: where the window ends, and this review's anchor
BASE = "10fbbc1c2"                  # main's head when the builder was given the folder (its message M14)
HANDOFF = "docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80"


def git(*a):
    r = subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def have(commit):
    return git("cat-file", "-e", commit + "^{commit}") is not None


def rows_of(path, pattern):
    """(id, cells) for every row of a table whose first cell fits `pattern`"""
    out = []
    for line in (ARC / path).read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^\| (%s) \|(.*)\|\s*$" % pattern, line)
        if m:
            out.append((m.group(1), [c.strip() for c in m.group(2).split("|")]))
    return out


def the_tables():
    first = rows_of("ANSWERS_the_first_43.md", r"W\d+|A\d+(?: to A\d+)?")
    second = rows_of("STATUS_OF_THE_57.md", r"\d\d|F\d+|W\d+")
    span = lambda rid: (lambda m: int(m.group(2)) - int(m.group(1)) + 1 if m else 1)(re.fullmatch(r"A(\d+) to A(\d+)", rid))
    n1 = {"the web seat": sum(span(r) for r, _ in first if r.startswith("W")), "agy-002": sum(span(r) for r, _ in first if r.startswith("A"))}
    n2 = {"the SM seat": sum(1 for r, _ in second if r.isdigit()), "agy-exp": sum(1 for r, _ in second if r.startswith("F")),
          "the web seat's addition": sum(1 for r, _ in second if r.startswith("W"))}
    unchecked = [r for r, c in second if c[2].lower() == "not checked"]
    in_part = [r for r, c in second if "not checked" in c[2].lower() and r not in unchecked]
    waits = [r for r, c in second if "to build" in c[3].lower()]
    mended = [r for r, c in second if r not in waits and "mended" in c[3].lower()]
    noted = [r for r, c in second if r not in waits and r not in mended and "noted" in c[3].lower()]
    other = [r for r, c in second if r not in waits + mended + noted]
    to_builder = [r for r, c in first if c[3].lower().startswith("to the builder")]
    debt = [r for r, c in first if "registered as a debt" in c[3].lower()]
    owner = [r for r, c in first if "decided by the owner" in c[3].lower()]
    return {
        "the first table: rows": len(first), "the first table: findings, by reader": n1, "the first table: findings": sum(n1.values()),
        "the second table: rows": len(second), "the second table: findings, by reader": n2, "the second table: findings": sum(n2.values()),
        "findings in all": sum(n1.values()) + sum(n2.values()),
        "the second table: cells in every row": sorted({len(c) for _, c in second}),
        "the second table: main's check is 'not checked'": unchecked,
        "the second table: 'not checked' for a part of the row": in_part,
        "the second table: checked by main in full": len(second) - len(unchecked) - len(in_part),
        "the second table: the state says 'to build'": waits,
        "the second table: 'mended', and nothing to build": mended,
        "the second table: 'noted', and nothing to build": noted,
        "the second table: none of the three": other,
        "the first table: sent to the builder, the whole row": to_builder,
        "the first table: findings sent to the builder, whole rows": sum(span(r) for r in to_builder),
        "the first table: a part registered as a debt": debt,
        "the first table: decided by the owner": owner,
        "checked by main in full, both tables": sum(n1.values()) + len(second) - len(unchecked) - len(in_part),
        "how": "the rows of the two tables as they stand in this arc: a row is a line that begins with a bar and whose first cell is a finding's number; "
               "'A24 to A36' is one row of thirteen findings",
    }


def the_kept_outputs():
    out = {}
    j = lambda name: json.loads((HERE / "checks" / name).read_text(encoding="utf-8"))
    a, s, x = j("quote_check_agy002.json")["summary"], j("quote_check_sm.json")["summary"], j("quote_check_agyexp.json")["summary"]
    out["agy-002: quotations found, of"] = [a["found exactly or when lines are joined"], a["rows"]]
    out["the SM seat: quotations placed, of, in findings"] = [s["placed"], s["quotations"], s["findings"]]
    out["agy-exp: quotations found, of"] = [x["every line of the quotation found in that file"], x["findings"]]
    out["controls found, in the three"] = [a["controls found"], s["controls found"], x["controls found"]]
    r = j("strict_recheck_r79_quotations.json")["all"]
    out["Review 79's quotations checked again strictly"] = {k: r[k] for k in ("quotations", "in the file the finding names", "in the arc's own folder (no file named)", "in a wide page only", "found nowhere, strictly")}
    p = j("plants_b1881_third.json")
    out["main's plants against B1881's lock: the plant and the lock's answer"] = [[e["plant"], e["the lock"]] for e in p]
    q = j("plants_agy002.json")
    out["main's plants for agy-002's rows: the lock's answer, counted"] = {k: sum(1 for e in q if e["the lock"] == k) for k in sorted({e["the lock"] for e in q})}
    out["main's plants for agy-002's rows that the lock passes, a plant being made"] = [[e["arc"], e["plant"]] for e in q if e["the lock"] == "passes" and e["plant"] != "nothing planted"]
    b = j("b1895_probes.json")
    out["main's computation on B1895"] = {"sequences": b["(1) sequences"], "on which the second word, built, is the first conjugated by the swap": b["(1) the second word, built over the integers, equals J W J"],
                                          "matrices": b["(3) matrices"], "agreement of the swapped-mark recipe, mark by mark": b["(3) agreement of the swapped-mark recipe, mark by mark"]}
    rows = j("builder_rows_probe2.json")
    out["the kept probe of the builder's rows: the rows it covers, its cases, those made again"] = [sorted({e["row"] for e in rows}), len(rows), sum(1 for e in rows if e["reproduced"])]
    out["the rows of the SM seat's file that main's recount covers"] = sorted(j("sm_rows_probe.json"))
    out["how"] = "read from the files main kept, in checks/; none of them is made again by this script"
    return out


def table_lines(text):
    """the lines of a page's tables less their rules, which is how main counted the rows of the law map and of the theorem
    registry at this review (its answer to agy-002's finding 20); and the same less each table's header"""
    bars = [l for l in text.split("\n") if l.startswith("|")]
    rules = [l for l in bars if re.match(r"^\|\s*:?-{2,}", l)]
    return len(bars) - len(rules), len(bars) - 2 * len(rules)


def from_git():
    if not (have(ANCHOR_BEFORE) and have(READ)):
        return {"missing": "the window's two commits are not both in this clone: nothing of the window is counted"}
    out = {}
    w = ANCHOR_BEFORE + ".." + READ
    out["commits in the window"] = int(git("rev-list", "--count", w))
    out["of them on main's own line"] = int(git("rev-list", "--count", "--first-parent", w))
    added = [p for p in git("diff", "--name-only", "--diff-filter=A", ANCHOR_BEFORE, READ).split("\n") if p]
    arcs = sorted({m.group(1) for p in added for m in [re.match(r"frontier/(B\d+)_[^/]*/arc_verdict\.json$", p)] if m}, key=lambda b: int(b[1:]))
    out["arcs added in the window"] = arcs
    changed = [p for p in git("diff", "--name-only", ANCHOR_BEFORE, READ).split("\n") if p.startswith("frontier/B")]
    folders = sorted({p.split("/")[1] for p in changed})
    older = [f for f in folders if f.split("_")[0] not in arcs]
    out["older arcs with a file changed in the window"] = len(older)
    out["of them, with the verdict file changed"] = len({p.split("/")[1] for p in changed if p.endswith("/arc_verdict.json")} - {f for f in folders if f.split("_")[0] in arcs})
    out["files changed in the window"] = len([p for p in git("diff", "--name-only", ANCHOR_BEFORE, READ).split("\n") if p])
    for name, path in (("the law map", "docs/LAW_MAP.md"), ("the theorem registry", "docs/THEOREM_REGISTRY.md")):
        a, b = table_lines(git("show", "%s:%s" % (ANCHOR_BEFORE, path))), table_lines(git("show", "%s:%s" % (READ, path)))
        out[name + ": lines of its tables less the rules, at the two ends"] = [a[0], b[0]]
        out[name + ": the same less each table's header"] = [a[1], b[1]]
        d = git("diff", "--numstat", ANCHOR_BEFORE, READ, "--", path).split()
        out[name + ": lines added and removed in the window"] = [int(d[0]), int(d[1])] if d else [0, 0]
    for name, path in (("the error ledger", "docs/ERROR_LEDGER.md"), ("the terminology page", "TERMINOLOGY.md"), ("the foundation", "GENESIS.md")):
        d = git("diff", "--numstat", ANCHOR_BEFORE, READ, "--", path).split()
        out[name + ": lines added and removed in the window"] = [int(d[0]), int(d[1])] if d else [0, 0]
    out["pages under papers/ changed in the window"] = sorted(p for p in git("diff", "--name-only", ANCHOR_BEFORE, READ, "--", "papers").split("\n") if p)
    out["hash lists added in the window (a seal's)"] = sorted(p for p in added if p.endswith("ARTIFACT_HASHES.txt"))
    reg = json.loads(git("show", READ + ":tests/GATE_CONTROLS.json"))
    out["controls registered at the commit read"] = len(reg)
    seal = [l for l in (git("diff", ANCHOR_BEFORE, READ, "--", "docs/SEAL_LEDGER.md") or "").split("\n") if l.startswith("+") and not l.startswith("+++")]
    out["the seal ledger: lines added in the window, and those of them that are empty"] = [len(seal), sum(1 for l in seal if not l[1:].strip())]

    def pins(rev):
        t = git("show", rev + ":docs/HARVEST_LEDGER.md")
        return dict(re.findall(r"^\| ([\w-]+) \| .*? \| `([0-9a-f]{7,40})` \|", t[t.index("## Pins"):t.index("## The rows")], re.M))
    a, b = pins(ANCHOR_BEFORE), pins(READ)
    out["pin rows of the harvest ledger at the two ends"] = [len(a), len(b)]
    out["lanes whose pin moved in the window"] = sorted(k for k in a if k in b and a[k] != b[k])
    out["lanes newly pinned in the window"] = sorted(set(b) - set(a))

    def packages(rev):
        d = json.loads(git("show", rev + ":frontier/B1861_the_closure_programme/PROGRAMME.json"))
        states = [p.get("status") for p in d["packages"]]
        return [len(states), sum(1 for s in states if str(s).startswith("DONE"))]
    out["the programme's packages, and those done, at the two ends"] = [packages(ANCHOR_BEFORE), packages(READ)]
    if have(BASE):
        out["commits on main's own line after the commit read, up to main's head at the handing over"] = int(git("rev-list", "--count", "--first-parent", READ + ".." + BASE))
        same = {}
        for f in ["ANSWERS_the_first_43.md", "STATUS_OF_THE_57.md"] + ["verification/checks/" + p.name for p in sorted((HERE / "checks").iterdir())]:
            theirs = git("show", "%s:%s/%s" % (BASE, HANDOFF, f.replace("verification/", "")))
            same[f] = theirs is not None and theirs.encode("utf-8") == (ARC / f).read_bytes()
        out["files of this arc that are main's, byte for byte, as its folder holds them at its head"] = [sum(same.values()), len(same)]
        out["files that are not"] = sorted(f for f, ok in same.items() if not ok)
    out["how"] = ("git, between %s and %s: rev-list --count for the commits; diff --name-only for the files, with --diff-filter=A for what was added; "
                  "show for a page at either end; diff --numstat for its lines" % (ANCHOR_BEFORE, READ))
    return out


def recount():
    return {"the two tables": the_tables(), "the outputs main kept": the_kept_outputs(), "git": from_git(),
            "the commits": {"the window begins at": ANCHOR_BEFORE, "the readers read": READ, "main's head at the handing over": BASE}}


if __name__ == "__main__":
    r = recount()
    text = json.dumps(r, indent=1, ensure_ascii=False) + "\n"
    print(text, end="")
    if "--write" in sys.argv:
        (HERE / "recount.json").write_text(text, encoding="utf-8")
