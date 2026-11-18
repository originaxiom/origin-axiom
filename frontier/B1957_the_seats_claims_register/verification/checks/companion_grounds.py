"""B1957: companion records (-r2x, -r3x) whose grounds list lines they no longer hold (the web seat's section 24.5, item 1;
its rv64 script read as text, not run; rebuilt here). A companion's ground is its reading's account: a line it lists and no
longer holds must be held where its unit now is, by exactly one record, whose ground or note names the line with a dated move.
 G1  per lane, at a commit (or the working tree): companions listing such lines; their lines, placed by the receiving record's
     verdict; lines not placed (no candidate or several); placed lines whose receiving record does not name the move.
Lines listed are read from three forms of a ground: 'Lines: a, b', 'line n:' and the 'by line' list."""
import collections, glob, json, os, re, subprocess, sys
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
V = "frontier/B1957_the_seats_claims_register/verification/records/"
def load(at):
    if at is None: return {os.path.basename(p)[:-5]: json.load(open(p)) for p in glob.glob(V + "*.json")}
    return {os.path.basename(f)[:-5]: json.loads(git("show", "%s:%s" % (at, f))) for f in git("ls-tree", "--name-only", at, V).split() if f.endswith(".json")}
def survey(recs, lane_prefix):
    owner = {u: k for k, r in recs.items() if isinstance(r.get("units"), list) for u in r["units"]}
    comps, silent, placed, amb, undated = 0, 0, collections.Counter(), [], []
    for k, r in sorted(recs.items()):
        if not k.startswith(lane_prefix) or not re.search(r"-r[23][pncs]$", k): continue
        h = r.get("how", ""); nums = set()
        for m in re.finditer(r"Lines?: ([\d, ]+)", h): nums |= set(re.findall(r"\d+", m.group(1)))
        nums |= set(re.findall(r"\bline (\d+):", h)); i = h.find("by line")
        if i >= 0: nums |= set(re.findall(r"(?:\): |; )(\d+): ", h[i:]))
        parent = re.sub(r"-r[23][pncs]$", "", k); tags = set()
        for c in recs:
            if c == k or c == parent or c.startswith(parent + "-r"): tags |= {u.split(":")[1] for u in recs[c].get("units", [])}
        held = {u.rsplit(":", 1)[1] for u in r.get("units", [])}; miss = sorted((n for n in nums if n not in held), key=int)
        if not miss: continue
        comps += 1; note = r.get("note", "")
        if not any(s in note for s in ("KEPT 2026-11-18 for its ground", "HAS MOVED", "restored to", "never held", "companion's ground is its reading's account")): silent += 1
        for n in miss:
            c = [u for u in owner if u.rsplit(":", 1)[1] == n and u.split(":")[1] in tags and owner[u] != k]
            if len(c) != 1: amb.append((k, n, len(c))); continue
            o = owner[c[0]]; placed[recs[o]["verdict"]] += 1; txt = recs[o].get("note", "") + " " + recs[o].get("how", "")
            if not (re.search(r"(RESTORED|REFILED|moved|returned)[^.]{0,200}\b(line|lines|row)\b[^.]{0,80}\b%s\b" % n, txt) or "(line %s)" % n in txt or "line %s of" % n in txt):
                undated.append((k, n, o))
    return comps, silent, sum(placed.values()), dict(sorted(placed.items())), amb, undated
for at, lab in (("7d3776b67", "at 7d3776b67"), (None, "now")):
    recs = load(at)
    for lane in ("web-",):
        c, s, n, p, a, u = survey(recs, lane)
        print("G1 %s, lane %s: companions listing lines they no longer hold %d (notes silent on it %d); such lines placed %d, by the receiving verdict %s; not placed %s; placed without a dated move named %d %s"
              % (lab, lane, c, s, n, p, a, len(u), u[:5]))
