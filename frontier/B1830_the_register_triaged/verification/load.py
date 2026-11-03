"""Which open register rows bear load on current math?  Open = QUEUED / LEAD / OWNER.  A row bears load when it says a
banked result is owed a check or a correction (keywords) AND that result is a dependency (depends_on, transitively) of
later arcs.  Data-free bookkeeping over docs/POINT_REGISTER.md and frontier/*/arc_verdict.json."""
import collections, datetime, glob, json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
rows = [l for l in (ROOT / "docs/POINT_REGISTER.md").read_text(encoding="utf-8").splitlines() if re.match(r"^\| P-\d+ \|", l)]
R = []
for l in rows:
    c = [x.strip() for x in l.strip("|").split(" | ")]
    R.append(dict(id=c[0], raised=c[1], origin=c[2], text=c[3], disp=c[4], where=c[5], moved=c[-1]))
openr = [r for r in R if r["disp"] in ("QUEUED", "LEAD", "OWNER")]
today = datetime.date(2026, 11, 3)
age = lambda d: (today - datetime.date.fromisoformat(d)).days if re.match(r"\d{4}-\d{2}-\d{2}$", d) else None
print("rows", len(R), "open", len(openr), collections.Counter(r["disp"] for r in openr))
print("by slot:", collections.Counter((re.match(r"(Q\d+)", r["where"]) or [None, "none"])[1] for r in openr).most_common())
ages = [age(r["moved"]) for r in openr]
print("days since last moved:", collections.Counter(min(a // 7, 4) if a is not None else -1 for a in ages), "(bins of a week; 4 = 28+)")
print("ESCALATED notes:", sum("ESCALATED(" in r["where"] or "ESCALATED(" in r["text"] for r in openr))
due = sorted((age(r["moved"]), r["id"]) for r in openr if age(r["moved"]) is not None and age(r["moved"]) >= 14 and "ESCALATED(" not in r["where"])
print("unmoved >= 14 days without ESCALATED:", len(due), "; >= 21:", sum(a >= 21 for a, _ in due))
# the dependency graph
dep = collections.defaultdict(set); claims = {}
for f in glob.glob(str(ROOT / "frontier/*/arc_verdict.json")):
    try: v = json.loads(pathlib.Path(f).read_text(encoding="utf-8"))
    except Exception: continue
    for d in v.get("depends_on") or []: dep[d].add(v["id"])
def downstream(a):
    seen, st = set(), [a]
    while st:
        x = st.pop()
        for y in dep.get(x, ()):
            if y not in seen: seen.add(y); st.append(y)
    return seen
KEY = re.compile(r"correct|wrong|error|unverified|not verified|verify|re-?check|re-?derive|audit|owed|mislabel|overclaim|retract|scope|premise|stale|refut|fails?\b|bug", re.I)
out = []
for r in openr:
    arcs = sorted(set(re.findall(r"\bB(\d{3,4})\b", r["text"])), key=int)
    if not arcs or not KEY.search(r["text"]): continue
    ds = set().union(*(downstream("B" + a) for a in arcs))
    out.append((len(ds), r["id"], r["disp"], r["where"][:3], ["B" + a for a in arcs][:6], r["text"][:150]))
out.sort(reverse=True)
print("\nopen rows that question a cited arc (keyword) -- with the number of later arcs depending on the cited arcs:", len(out))
print("  with >= 1 dependent:", sum(o[0] > 0 for o in out), "; >= 10:", sum(o[0] >= 10 for o in out))
for o in out[:25]: print("%4d  %-6s %-6s %-3s %s  %s" % o)
