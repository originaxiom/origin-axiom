#!/usr/bin/env python3
"""B1905: the record read for selection and chirality.  Main's check of the readers' rows, and the tables.

THE ROWS (rows.json.txt, one JSON object a line, 636 lines): written by six read-only readers, one reader an arc, from
the verdict file and the head of the page of every arc whose verdict line or title the topic sweep matched
(arcs_by_title.json).  Each row: the question, the wall (classes W1 to W8), the kind of principle (codes A to K, several
where combined), the outcome, whether the arc settled the question it asked, why, and a quotation with its file.
WHAT THIS DOES
  1. Every row has its 13 keys.  Every quotation is looked for, word for word on one line, in the file it names AT THE
     COMMIT THE READERS READ (git show), so that a later note on a page does not change the answer.  A verdict line is
     one string of a JSON file: it is compared inside the parsed field.  CONTROL: each quotation with its last word
     doubled must not be found.
  2. The tables: wall by outcome; kind of principle by outcome; the combinations; and a split of the settled rows of
     four walls by the words of their outcome (crude, and said so).
  Written to sweep_tables.json; printed as sweep_tables_run.txt.
WHAT IT IS NOT: a judgement of main's.  The classes are the readers', one reader an arc, not independently checked.
HOW IT COULD FAIL: a row without a key; a quotation not found; a control found; the commit not in the clone (said aloud)."""
import json, collections, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]
READ = "a15516d43"
KEYS = ["arc", "verdict", "topic", "date", "question", "wall", "principle", "principle_note", "outcome", "settled", "why", "quote", "quote_file"]
S = ["yes", "partly", "no", "question was wrong", "later corrected or retracted"]
NAMES = {"A": "extremum", "B": "census", "C": "symmetry", "D": "uniqueness", "E": "consistency", "F": "arithmetic", "G": "dynamics", "H": "read-out", "I": "declared", "J": "measure", "K": "other"}
WALLS = {"W1": "the mirror pair not split", "W2": "one member of a family not picked", "W3": "a value or modulus not picked", "W4": "a count not forced",
         "W5": "a scale or hierarchy", "W6": "an identification borrowed", "W7": "a construction not canonical", "W8": "other"}
NEG = re.compile(r"\b(no|not|cannot|none|never|neither|nothing|refut\w*|fails?|forbid\w*|isospectral|preserv\w*|invariant|amphichiral|does not|do not|is not|are not|without|unforced|free|open|absent|blind|even)\b", re.I)
POS = re.compile(r"\b(selects?|selected|picks?|picked|unique\w*|forced|forces|fix(es|ed)|determin\w+|singles? out|derive[sd]?|only one|exactly one)\b", re.I)


def load():
    rows = []
    for n, l in enumerate((HERE / "rows.json.txt").read_text(encoding="utf-8").split("\n"), 1):
        if not l.strip(): continue
        r = json.loads(l); assert sorted(r) == sorted(KEYS), "row %d has not the 13 keys" % n
        if isinstance(r["principle"], str):
            s = r["principle"].strip()
            try: r["principle"] = json.loads(s) if s.startswith("[") else [x.strip() for x in re.split(r"[;,|]", s) if x.strip()]
            except Exception: r["principle"] = [s]
        r["principle"] = [str(x).strip() for x in r["principle"]]
        rows.append(r)
    return rows


def have(commit):
    return subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", commit + "^{commit}"], capture_output=True).returncode == 0


def quotes(rows, commit=READ):
    cache = {}
    def text(p):
        if p not in cache:
            r = subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s" % (commit, p)], capture_output=True, text=True)
            cache[p] = r.stdout if r.returncode == 0 else None
        return cache[p]
    def there(q, p):
        t = text(p)
        if t is None: return False
        if any(q in line for line in t.split("\n")): return True
        if p.endswith(".json"):
            try: return q in json.loads(t).get("claim_one_line", "")
            except Exception: return False
        return False
    asked = [r for r in rows if not (r["topic"] == "neither" and r["quote"] in ("n/a", ""))]
    found = [r["arc"] for r in asked if there(r["quote"], r["quote_file"])]
    missing = [r["arc"] for r in asked if r["arc"] not in set(found)]
    ctl = sum(1 for r in asked if there(" ".join(r["quote"].rstrip().split(" ") + [r["quote"].rstrip().split(" ")[-1]]), r["quote_file"]))
    return {"quotations": len(asked), "found on one line of the file named, at the commit read": len(found), "not found": missing, "controls found": ctl, "the commit read": commit}


def tables(rows):
    live = [r for r in rows if r["topic"] != "neither"]
    wall = lambda r: r["wall"].split(" ")[0] if r["wall"][:1] == "W" else "?"
    kinds = lambda r: sorted({p.split(" ")[0] for p in r["principle"] if p.split(" ")[0] in NAMES})
    def direction(r):
        p, n = bool(POS.search(r["outcome"])), bool(NEG.search(r["outcome"]))
        return "picks" if p and not n else ("mixed" if p and n else ("does not pick" if n else "other"))
    T = {"rows": len(rows), "neither on reading": len(rows) - len(live), "about selection or chirality": len(live),
         "by topic": dict(collections.Counter(r["topic"] for r in live)), "by outcome": {s: sum(r["settled"] == s for r in live) for s in S}}
    T["wall by outcome"] = {w: [sum(1 for r in live if wall(r) == w and r["settled"] == s) for s in S] for w in WALLS}
    T["kind of principle by outcome, all walls"] = {k: [sum(1 for r in live if k in kinds(r) and r["settled"] == s) for s in S] for k in NAMES}
    T["kind of principle by outcome, wall by wall"] = {w: {k: [sum(1 for r in live if wall(r) == w and k in kinds(r) and r["settled"] == s) for s in S] for k in NAMES} for w in ("W1", "W2", "W3", "W4", "W7")}
    comb = collections.Counter(frozenset(kinds(r)) for r in live if len(kinds(r)) == 2)
    T["pairs of kinds used together"] = {"+".join(sorted(k)): v for k, v in comb.most_common(8)}
    T["settled or partly, by the words of the outcome"] = {w: dict(collections.Counter(direction(r) for r in live if wall(r) == w and r["settled"] in ("yes", "partly"))) for w in ("W1", "W2", "W3", "W4")}
    T["arcs whose question was found to be wrong"] = sorted((r["arc"] for r in live if r["settled"] == "question was wrong"), key=lambda b: int(b[1:]))
    T["arcs later corrected or retracted"] = len([r for r in live if r["settled"] == "later corrected or retracted"])
    return T


if __name__ == "__main__":
    rows = load(); T = tables(rows)
    Q = quotes(rows) if have(READ) else {"NOT RUN": "the commit the readers read, %s, is not in this clone" % READ}
    out = {"the quotations": Q, "the tables": T}
    (HERE / "sweep_tables.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("rows %d; about selection or chirality %d; neither on reading %d" % (T["rows"], T["about selection or chirality"], T["neither on reading"]))
    print("quotations: %s" % json.dumps(Q))
    print("by topic: %s" % T["by topic"]); print("by outcome: %s" % T["by outcome"])
    print("\nWALL: settled / partly / not / the question was wrong / later corrected")
    for w, c in T["wall by outcome"].items(): print("  %s %-36s %4d  %s" % (w, WALLS[w], sum(c), "  ".join("%3d" % x for x in c)))
    print("\nKIND OF PRINCIPLE, all walls: arcs  settled / partly / not / wrong / corrected   share settled")
    for k, c in T["kind of principle by outcome, all walls"].items(): print("  %s %-12s %4d  %s   %2d%%" % (k, NAMES[k], sum(c), "  ".join("%3d" % x for x in c), round(100 * c[0] / sum(c)) if sum(c) else 0))
    for w, tab in T["kind of principle by outcome, wall by wall"].items():
        print("\n%s, %s:" % (w, WALLS[w]))
        for k, c in tab.items():
            if sum(c): print("  %s %-12s %4d  %s" % (k, NAMES[k], sum(c), "  ".join("%3d" % x for x in c)))
    print("\npairs of kinds used together: %s" % T["pairs of kinds used together"])
    print("settled or partly, by the words of the outcome: %s" % T["settled or partly, by the words of the outcome"])
    print("the question was found to be wrong: %s" % T["arcs whose question was found to be wrong"])
