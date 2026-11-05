"""S297 recheck of the S296 triage: which open rows typed LEAD or PROCESS carry a load signal? Data-free bookkeeping."""
import collections, glob, json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
R = {}
for l in (ROOT / "docs/POINT_REGISTER.md").read_text(encoding="utf-8").splitlines():
    if not re.match(r"^\| P-\d+ \|", l): continue
    c = [x.strip() for x in l.strip().strip("|").split(" | ")]
    R[c[0]] = dict(id=c[0], text=c[3], disp=c[4], where=c[5], moved=c[6])
op = {k: r for k, r in R.items() if r["disp"] in ("QUEUED", "LEAD", "OWNER")}
typ = lambda r: (re.findall(r"\[(DEBT|LEAD|PROCESS)\]", r["where"]) or ["-"])[0]
print("open", len(op), collections.Counter((r["disp"], typ(r)) for r in op.values()))
dep = collections.defaultdict(set); verdict = {}
for f in glob.glob(str(ROOT / "frontier/*/arc_verdict.json")):
    try: v = json.loads(pathlib.Path(f).read_text(encoding="utf-8"))
    except Exception: continue
    verdict[v.get("id")] = v.get("verdict") or v.get("status")
    for d in v.get("depends_on") or []: dep[d].add(v["id"])
def down(a):
    s, st = set(), [a]
    while st:
        x = st.pop()
        for y in dep.get(x, ()):
            if y not in s: s.add(y); st.append(y)
    return s
KEY = re.compile(r"correct|wrong|error|unverified|not verified|verify|re-?check|re-?derive|audit|owed|mislabel|overclaim|retract|scope|premise|stale|refut|fails?\b|bug", re.I)
FOUND = re.compile(r"GENESIS|THE_BAR|KIND_TABLE|LAW_MAP|IDENTIFICATION_LEDGER|CLAIMS|README|P9|paper|CAMPAIGN_STATUS|FRAMING_LEDGER|FINAL_ACTS_BAR|LOOK_LEDGER|PRACTICES|WORKING_RULES|METHOD|TERMINOLOGY|SM_SPEC|THE_TOWERS|THE_LAMBDA|PROVENANCE|GOVERNANCE")
load72 = []
for r in op.values():
    arcs = sorted(set(re.findall(r"\bB(\d{3,4})\b", r["text"])), key=int)
    if arcs and KEY.search(r["text"]):
        ds = set().union(*(down("B" + a) for a in arcs)); load72.append((len(ds), r["id"]))
load72.sort(reverse=True)
print("\nthe 72-screen now:", len(load72), collections.Counter(typ(op[i]) for _, i in load72))
flag = {}
for n, i in load72:
    if typ(op[i]) != "DEBT": flag.setdefault(i, []).append("load%d" % n)
for r in op.values():
    if typ(r) == "DEBT": continue
    t = r["text"]
    if FOUND.search(t) and KEY.search(t): flag.setdefault(r["id"], []).append("found+key")
    if re.search(r"cannot fail|vacuous|tautolog|false pass|never ran|not run|unpaid|errat|misstat|lags?\b|inconsisten|contradict", t, re.I): flag.setdefault(r["id"], []).append("integrity")
print("\nLEAD/PROCESS/OWNER rows flagged:", len(flag))
for i in sorted(flag, key=lambda x: int(x[2:])):
    print(i, typ(op[i]), op[i]["disp"], flag[i])
json.dump({i: dict(type=typ(op[i]), disp=op[i]["disp"], flags=flag[i], text=op[i]["text"], where=op[i]["where"]) for i in flag},
          open(pathlib.Path(__file__).with_name("flagged.json"), "w"), ensure_ascii=False, indent=1)
