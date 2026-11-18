"""B1957: every record a ground or a note cites exists (added 2026-11-18).  The second reading had removed 54 parent records
whose every line it narrowed, and their grounds went with them while 96 records went on citing them (67 of them their own companions); main found it
when it read an endgame line against a ground that named three such records.  They are restored, each with its ground and
no statement under it.  Two ids are cited as history only: records that were replaced, named here with what replaced them."""
import json, pathlib, re, collections
HERE = pathlib.Path(__file__).resolve().parent; R = HERE.parent / "records"; ids = {q.stem for q in R.glob("*.json")}
REPLACED = {"web-wa2-05r": "web-wa2-05v (and its companion web-wa2-05v-r2p)", "web-wz1-04": "web-wz1-04p"}
pat = re.compile(r"\b(?:%s)-[a-z0-9]+(?:-[a-z0-9]+)*-\d+[a-z]?(?:-r[23][pnc])?\b" % "|".join(map(re.escape, sorted({i.split("-")[0] for i in ids}))))
dead = collections.defaultdict(set); cited = set(); empty = []
for q in R.glob("*.json"):
    d = json.loads(q.read_text())
    if d.get("verdict") != "READ" and not d.get("units"): empty.append(d["id"])
    for m in pat.findall(d.get("how", "") + " " + d.get("note", "")):
        cited.add(m)
        if m not in ids and m not in REPLACED: dead[m].add(d["id"])
orphans = [i for i in ids if re.search(r"-r[23][pnc]$", i) and re.sub(r"-r[23][pnc]$", "", i) not in ids]
print("N1: records: %d; ids cited in grounds and notes: %d; cited and not existing: %d %s; cited as history, replaced: %s" % (len(ids), len(cited), len(dead), sorted(dead)[:5], {k: v for k, v in REPLACED.items() if k in cited}))
print("N2: companion records whose parent record does not exist: %d; records kept for their ground with no statement under them: %d, each saying so in its note: %s"
      % (len(orphans), len(empty), all("no statement under it" in json.loads((R / (e + ".json")).read_text()).get("note", "") for e in empty)))
