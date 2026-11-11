"""B1889 -- check every quote in a reader's digest against the harvest row it names, at the commit the digest is of.

A quote is EXACT if, after collapsing whitespace, it is a substring of the named row.  It is LOOSE if it is one after markdown
marks are dropped and dashes and quotation marks are folded.  It is ELSEWHERE if it is in another row and not in the named one,
and NOT FOUND if it is in no row.  What could fail: a reader that paraphrases, or names the wrong row.

    python3 -B frontier/B1889_the_seats_digested/verification/quote_check.py            # check against the committed run
    python3 -B frontier/B1889_the_seats_digested/verification/quote_check.py --write    # write the run
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = next(p for p in HERE.parents if (p / "GENESIS.md").is_file())
QUOTE = re.compile(r'"((?:[^"\\]|\\.)*)"')


def ledger(text):
    R = {}
    for l in text.split("\n"):
        m = re.match(r"^\| (\d+) \|", l)
        if m:
            R[int(m.group(1))] = l
    return R


def ws(s):
    return re.sub(r"\s+", " ", s).strip()


def loose(s):
    s = s.replace("\\\"", "\"")
    s = re.sub(r"[*`_]", "", s)
    s = re.sub(r"[\u2010\u2011\u2012\u2013\u2014\u2212]", "-", s)
    s = re.sub(r"[\u201c\u201d\u201e]", "\"", s)
    s = re.sub(r"[\u2018\u2019]", "'", s)
    return ws(s).lower()


def pairs(text, valid):
    for ln, line in enumerate(text.split("\n"), 1):
        for m in QUOTE.finditer(line):
            q = m.group(1).replace("\\\"", "\"")
            if len(q.split()) < 3:
                continue
            nums = [int(x) for x in re.findall(r"(?<![\w.])(\d{1,4})(?![\w.]*\d)", line[:m.start()]) if int(x) in valid]
            yield ln, nums[::-1], q


def check(reader_text, R):
    out = []
    for ln, cands, q in pairs(reader_text, set(R)):
        verdict, where = "NOT FOUND", None
        for i, n in enumerate(cands):
            if ws(q) in ws(R[n]):
                verdict, where = ("EXACT" if i == 0 else "EXACT, ANOTHER ROW NAMED ON THE LINE"), n
                break
        if where is None:
            for n in cands:
                if loose(q) in loose(R[n]):
                    verdict, where = "LOOSE", n
                    break
        if where is None:
            hits = [n for n in R if ws(q) in ws(R[n])] or [n for n in R if loose(q) in loose(R[n])]
            if hits:
                verdict, where = "ELSEWHERE", hits[0]
        out.append(dict(line=ln, named=cands[:1], quote=q, verdict=verdict, row=where))
    return out


def run(commit, text=None):
    if text is None:
        r = subprocess.run(["git", "-C", str(ROOT), "show", "%s:docs/HARVEST_LEDGER.md" % commit], capture_output=True)
        if r.returncode != 0:
            raise SystemExit("cannot read the harvest ledger at %s: is this a full clone?" % commit)
        text = r.stdout.decode("utf-8")
    R = ledger(text)
    res = {}
    for f in sorted((HERE / "readers").glob("reader_G*.txt")):
        got = check(f.read_text(encoding="utf-8"), R)
        tally = {}
        for g in got:
            tally[g["verdict"]] = tally.get(g["verdict"], 0) + 1
        res[f.name] = dict(quotes=len(got), tally=dict(sorted(tally.items())),
                           not_exact=[dict(line=g["line"], verdict=g["verdict"], quote=g["quote"]) for g in got if not g["verdict"].startswith("EXACT")])
    exact = sum(v for r in res.values() for k, v in r["tally"].items() if k.startswith("EXACT"))
    return dict(as_of=commit, readers=res, quotes=sum(r["quotes"] for r in res.values()), exact=exact)


def report(B):
    L = ["the readers' quotes, checked against the harvest ledger at %s" % B["as_of"][:9]]
    for name, r in B["readers"].items():
        L.append("  %-28s %3d quotes: %s" % (name, r["quotes"], r["tally"]))
        for x in r["not_exact"]:
            L.append("      line %d, %s: %s" % (x["line"], x["verdict"], x["quote"][:100]))
    L.append("%d of %d quotes are in the named row word for word" % (B["exact"], B["quotes"]))
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    as_of = json.loads((ARC / "SEATS.json").read_text(encoding="utf-8"))["as_of"]
    B = run(as_of)
    if "--write" in sys.argv:
        (HERE / "quote_check.json").write_text(json.dumps(B, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        (HERE / "quote_check_run.txt").write_text(report(B), encoding="utf-8")
    same = B == json.loads((HERE / "quote_check.json").read_text(encoding="utf-8"))
    sys.stdout.write(report(B))
    print("THE RUN IS THE COMMITTED ONE" if same else "THE RUN DIFFERS FROM THE COMMITTED ONE")
    sys.exit(0 if same else 1)
